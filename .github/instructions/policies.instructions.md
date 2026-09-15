---
applyTo: '**'
---
# policies

## Security Architecture
### Authentication and Authorization

**Authentication Flow**
- All user authentication is centralized through the dedicated auth-service
- Frontend applications must authenticate users before accessing protected resources
- Authentication context is maintained throughout the React application lifecycle

**API Security**
- All external API access is routed through the API Gateway
- Gateway enforces authentication and authorization policies before forwarding requests
- Microservices rely on gateway-level security validation

**Service-to-Service Communication**
- Internal service communication occurs within the secured microservices network
- Each service (hr-service, finance-service, notification-service) operates within isolated boundaries
- Services handle domain-specific authorization for their respective resources

### Access Control Principles
