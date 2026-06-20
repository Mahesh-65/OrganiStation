# README: Mahesh OrganiStation Infrastructure

## Project Structure
- `modules/`: Reusable logic for each Azure service.
- `environments/`: Environment-specific overrides.
- `main.tf`: Root orchestrator.

## Deployment Steps
1. **Login**: `az login`
2. **Initialize**: `terraform init`
3. **Setup Dev**:
   - `terraform workspace new dev`
   - `terraform apply`
4. **Setup Prod**:
   - `terraform workspace new prod`
   - `terraform apply`

## Security Features
- **Zero Public Access**: CosmosDB and Key Vault are on Private Endpoints.
- **Workload Identity**: AKS pods use federated credentials to reach Key Vault. No secrets stored in K8s!
- **RBAC**: All access is granted via Managed Identity roles.
- **WAF**: Application Gateway provides Layer 7 protection.

## Monitoring
- Log Analytics captures AKS logs and Metrics.
- CPU/Memory alerts are configured in the Monitoring module.
