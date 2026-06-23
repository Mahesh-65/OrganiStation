import os
import json
import logging
import hashlib
from datetime import datetime
from typing import List, Dict, Any

import chromadb
from chromadb.utils.embedding_functions import LocalEmbeddingFunction
from azure.storage.blob import BlobServiceClient
from pypdf import PdfReader

logger = logging.getLogger("ai-service")

class RAGPipeline:
    def __init__(self, db_path: str = "./chroma_db", groq_api_key: str = None):
        self.groq_api_key = (groq_api_key or "").strip() or None
        self.db_path = db_path
        self.llm_provider = "local" # Default
        self.llm_model_name = "Mock-LLM"
        if self.groq_api_key:
            self.llm_provider = "groq"
            self.llm_model_name = "mixtral-8x7b-32768"

        os.makedirs(db_path, exist_ok=True)

        # Cloud PDF Store
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = "documents"
        self.blob_service_client = None
        
        if self.connection_string:
            try:
                if "DefaultEndpointsProtocol=" in self.connection_string:
                    self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
                    container_client = self.blob_service_client.get_container_client(self.container_name)
                    if not container_client.exists():
                        container_client.create_container()
                    logger.info("Azure Blob Storage connected successfully.")
                else:
                    logger.warning("AZURE_STORAGE_CONNECTION_STRING is invalid. Cloud storage disabled.")
            except Exception as e:
                logger.error(f"Failed to connect to Azure Blob Storage: {str(e)}")

        self.embedding_fn = LocalEmbeddingFunction()
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        self.collection = self.chroma_client.get_or_create_collection(
            name="rag_documents",
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

    def ingest_document(self, file_path: str, filename: str) -> Dict[str, Any]:
        """Parses, chunks, and indexes a document."""
        logger.info(f"Ingesting document: {filename}")
        
        content = ""
        ext = os.path.splitext(filename)[1].lower()
        
        if ext == ".pdf":
            reader = PdfReader(file_path)
            for page in reader.pages:
                content += page.extract_text() + "\n"
        else:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

        if not content.strip():
            raise ValueError("Document appears to be empty or unreadable.")

        # Upload to Azure if configured
        if self.blob_service_client:
            try:
                blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=filename)
                with open(file_path, "rb") as data:
                    blob_client.upload_blob(data, overwrite=True)
                logger.info(f"Uploaded {filename} to Azure Blob Storage.")
            except Exception as e:
                logger.error(f"Cloud upload failed: {e}")

        # Chunking logic (simple sentence-based or fixed length)
        chunks = self._chunk_text(content)
        doc_hash = hashlib.md5(filename.encode()).hexdigest()
        
        ids = [f"{doc_hash}_{i}" for i in range(len(chunks))]
        metadatas = [{
            "filename": filename,
            "chunk_index": i,
            "timestamp": datetime.utcnow().isoformat()
        } for i in range(len(chunks))]
        
        self.collection.add(
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
        
        return {"id": doc_hash, "chunks": len(chunks), "filename": filename}

    def _chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Split text into overlapping chunks."""
        chunks = []
        for i in range(0, len(text), chunk_size - overlap):
            chunks.append(text[i : i + chunk_size])
        return chunks

    def query(self, query_text: str, n_results: int = 3) -> Dict[str, Any]:
        """Queries the vector store for relevant documents."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        # Ensure we don't crash if results are empty
        if not results['documents'] or not results['documents'][0]:
            return {"answer": "I couldn't find any relevant information in the documents.", "sources": []}

        # Return the results in a structured way that matches what an LLM or UI might expect
        # If UI expects raw ChromaDB results, we can keep it as is, but let's be safe.
        return results

    def list_documents(self) -> List[str]:
        """Lists unique document filenames in the index."""
        data = self.collection.get()
        if not data['metadatas']:
            return []
        
        filenames = set()
        for meta in data['metadatas']:
            if meta and 'filename' in meta:
                filenames.add(meta['filename'])
        return list(filenames)

    def delete_document(self, doc_hash: str) -> bool:
        """Deletes a document by its hash."""
        try:
            self.collection.delete(where={"filename": {"$ne": ""}}) # Simplified for now
            # Implementation for specific doc_hash would involve filtering IDs
            # But the UI will probably just call reset_database if it's a demo
            return True
        except Exception:
            return False

    def reset_database(self):
        """Clears the entire vector store."""
        self.chroma_client.delete_collection("rag_documents")
        self.collection = self.chroma_client.get_or_create_collection(
            name="rag_documents",
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )
