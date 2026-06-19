variable "resource_group_name" {
  description = "Name of the resource group"
  default     = "rg-organistation-prod"
}

variable "location" {
  description = "Azure region"
  default     = "East US"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  default     = "organistationacr001" # Must be globally unique
}

variable "aks_name" {
  description = "Name of the AKS cluster"
  default     = "organistation-aks"
}

variable "kv_name" {
  description = "Name of the Key Vault"
  default     = "organistation-kv-001" # Must be globally unique
}

variable "kubernetes_version" {
  description = "Kubernetes version"
  default     = "1.28.9"
}
