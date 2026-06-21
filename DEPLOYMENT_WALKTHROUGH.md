# 🚀 OrganiStation: The Definitive Deployment Walkthrough

Follow these 10 steps in exact order to deploy the entire platform from zero to a live production URL.

---

## 🏗️ Phase 1: The Azure Foundation

### Step 1: Manual Azure Bootstrap
You must create the "Deployment Identity" that GitHub will use.
1.  **Create a Service Principal (SPN)** via Azure CLI or Portal.
2.  Assign the SPN **Contributor** and **User Access Administrator** roles on your Subscription.
3.  **Create a Storage Account** manually (e.g., `organistationtfstate`) and a container named `tfstate`. This will hold your Terraform remote state.

### Step 2: Initial GitHub Secrets
Navigate to your **GitHub Organization Settings -> Secrets and variables -> Actions**.
Add these **Secrets**:
*   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`.
Add these **Variables**:
*   `BACKEND_RG`: The Resource Group of the storage you created in Step 1.
*   `BACKEND_STORAGE`: The name of the storage account from Step 1.

### Step 3: Provision Infrastructure (Terraform)
1.  Push the `terraform-project` folder to its repository.
2.  Navigate to **Actions** and run the `terraform-apply.yml` workflow.
3.  **Wait** for it to complete. This will create your AKS, ACR, CosmosDB, and Service Bus.

---

## 🛡️ Phase 2: Security & Build Integration

### Step 4: Harvest Post-Infra Values
After Step 3, go to the Azure Portal and collect these new values:
1.  **ACR Login Server**: (e.g., `organistationacr.azurecr.io`).
2.  **AKS Cluster Name**: (e.g., `organistation-aks-prod`).
3.  **AKS Resource Group**: (The one created by Terraform).

### Step 5: Update GitHub Settings
Add the harvested values to your GitHub Organization:
*   **Secrets**: `ACR_USERNAME`, `ACR_PASSWORD`.
*   **Variables**: `ACR_LOGIN_SERVER`, `AKS_CLUSTER_NAME`, `AKS_RESOURCE_GROUP`.
*   **Audit Secrets**: Sign up for [SonarCloud.io](https://sonarcloud.io) and [Snyk.io](https://snyk.io), and add `SONAR_TOKEN` and `SNYK_TOKEN`.

### Step 6: Deploy Shared Workflows
1.  Push the `shared-workflows` folder to its repository.
2.  Ensure it is named exactly as referenced in your `build.yaml` files (e.g., `shared-workflows`).

### Step 7: Build the Microservices
1.  Push all 8 microservice folders (`auth`, `ai`, `hr`, etc.) to their respective repositories.
2.  The **`build.yaml`** in each repo will trigger automatically.
3.  Verify that all 8 images are successfully pushed to your **Azure Container Registry (ACR)**.

---

## ⛵ Phase 3: Application Orchestration

### Step 8: Configure Helm Values
1.  Open `dev-values.yaml` or `prod-values.yaml` in your `organistation-chart` repository.
2.  Ensure the `global.imageTag` matches the Git SHA of your successful builds from Step 7.

### Step 9: Trigger Final Deployment
1.  Push the `organistation-chart` folder to its repository.
2.  Navigate to **Actions** -> **Continuous Deployment (Helm)**.
3.  Click **Run workflow**, select `prod` or `dev`, and enter your image tag.
4.  Helm will perform an **Atomic Upgrade**—it will either succeed 100% or roll back automatically.

---

## ✅ Phase 4: Final Verification

### Step 10: Smoke Test & Access
1.  Get the External IP of the Gateway:
    ```bash
    kubectl get svc gateway -n prod-ns
    ```
2.  Visit the IP in your browser.
3.  **Login**: Use the default `admin@organistation.com` credentials (check the `auth-service` seeder for initial password).
4.  **Security Check**: Navigate to the Team Directory to ensure RBAC and Workload Identity are communicating with CosmosDB correctly.
