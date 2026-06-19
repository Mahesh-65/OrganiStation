# Comprehensive Azure Portal Deployment Guide: OrganiStation

This guide provides a clinical, step-by-step walkthrough for deploying the OrganiStation platform using only the **Azure Portal (UI)**.

---

## 🏗 Phase 1: The Core Infrastructure

### 1.1 Create a Resource Group
1.  Search for **Resource Groups** in the top search bar.
2.  Click **+ Create**.
3.  **Name**: `rg-organistation-prod`
4.  **Region**: `East US` (or your preferred region).
5.  Click **Review + Create**, then **Create**.

### 1.2 Create Azure Container Registry (ACR)
1.  Search for **Container Registries**.
2.  Click **+ Create**.
3.  **Resource Group**: Select `rg-organistation-prod`.
4.  **Registry Name**: `organistationacr` (must be unique).
5.  **SKU**: `Basic`.
6.  Click **Review + Create**, then **Create**.

---

## 🔐 Phase 2: Secure Secret Management

### 2.1 Create Azure Key Vault
1.  Search for **Key Vaults**.
2.  Click **+ Create**.
3.  **Key Vault Name**: `organistation-kv`.
4.  **Access Configuration**: Ensure **Azure role-based access control (RBAC)** is selected (Recommended) or **Vault Access Policy**.
5.  Click **Review + Create**, then **Create**.

### 2.2 Adding your Secrets
1.  Open your new Key Vault.
2.  In the left menu, click **Secrets**.
3.  Click **+ Generate/Import**.
4.  **Name**: `MONGODB-URI` | **Value**: `mongodb+srv://...`
5.  **Name**: `JWT-SECRET` | **Value**: `your-super-secret-key`
6.  *Repeat for all secrets needed by your services.*

---

## ☸️ Phase 3: Creating the AKS Cluster (Crucial Steps)

1.  Search for **Kubernetes services**.
2.  Click **+ Create** -> **Create a Kubernetes cluster**.
3.  **Basics Tab**:
    *   **Cluster preset configuration**: `Standard`.
    *   **Kubernetes cluster name**: `organistation-aks`.
4.  **Networking Tab (IMPORTANT)**:
    *   **Network configuration**: `Azure CNI (Overlay)`.
    *   **Application Gateway ingress controller**: Check **Enable**.
    *   **App gateway name**: `organistation-gw`.
5.  **Integrations Tab**:
    *   **Container registry**: Select `organistationacr` (from Phase 1.2).
    *   **Azure Key Vault Secrets Provider**: Check **Enable**.
6.  Click **Review + Create**, then **Create**. (This takes 5-10 minutes).

---

## 🔗 Phase 4: Connecting the Services

### 4.1 How the Ingress talks to the Gateway
We use **Azure Application Gateway (AGIC)**. 
- When you deploy the `Ingress` resource via Helm, it tells Azure: "Please route all traffic coming to the public IP on path `/api` to the internal K8s service named `gateway`."

### 4.2 How the Gateway talks to Microservices
Inside your cluster, every service has a **Service Name** (e.g., `auth`, `hr`, `ai`).
- The **Gateway** microservice has an environment variable like `AUTH_SERVICE_URL`. 
- **The Connection**: The Gateway sends an internal HTTP request to `http://auth:80`. Kubernetes' internal DNS automatically routes this to the correct pod.

---

## 🚀 Phase 5: Pushing Images & Final Deployment

*Note: While infrastructure is done in the Portal, you must still push your code. Use the **Azure Cloud Shell** (terminal icon at the top of the portal).*

### 5.1 Push your Images
Paste these commands into the Cloud Shell:
```bash
az acr login --name organistationacr
# Run the build/push process for each folder as described in Phase 4 of the CLI guide.
```

### 5.2 Deploy via Helm
In the Cloud Shell:
1.  Connect to your cluster: `az aks get-credentials -g rg-organistation-prod -n organistation-aks`
2.  Create namespace: `kubectl create namespace organistation-ns`
3.  Navigate to your repository and run:
    ```bash
    helm install organistation ./organistation-chart -n organistation-ns
    ```

---

## ✅ Verification
1.  Go to **Application Gateway** in the portal.
2.  Find the **Frontend IP configuration** to see your Public IP.
3.  Paste that IP into your browser. 
4.  **Success!** Your AGIC is routing `/` to the Frontend and `/api` to the Gateway.
