---
applyTo: '**'
---
# rules

## Naming Conventions
### Python Code Standards

**Functions, Methods**
- Use snake_case for function

### API Endpoints

**URL Structure**
- Use lowercase with hyphens for multi-word resources
- Follow RESTful conventions with resource-based URLs
- Example: `/api/employees`, `/api/employee-records`

**HTTP Methods**
- GET: Retrieve resources
- POST: Create new resources
- DELETE: Remove resources
- PUT/PATCH: Update existing resources

### File and Directory Names

`models/`

### Health Check Endpoints

**Standard Endpoints**
- `/health` - Basic application health status
- `/ready` - Readiness probe for container orchestration
- `/api/health` - API-specific health check

All health endpoints should use GET method and return appropriate HTTP status codes.

## Architecture Rules
### Layer Boundaries

#### Service Isolation
- Each service (auth-service, hr-service, finance-service, notification-service) must maintain strict boundaries
- Services communicate only through well-defined API contracts
- No direct database access between services
- Shared data must be accessed through service APIs

#### Gateway Layer
- All external client requests must route through the API gateway
- Gateway handles routing, load balancing, and cross-cutting concerns
- Services must not expose direct external endpoints

### Import Rules

#### Service Dependencies
- Services must not import code directly from other services
- Shared utilities should be extracted to common libraries
- Database models are service-private and must not be imported across services

#### Frontend Dependencies
- Frontend may only communicate with services through the gateway
- No direct service-to-frontend connections allowed
- Authentication context must be managed centrally

### Forbidden Patterns

#### Cross-Service Database Access
- ❌ Direct database connections between services
- ❌ Shared database schemas across service boundaries
- ❌ Foreign key relationships spanning service databases

#### Tight Coupling
- ❌ Synchronous service-to-service calls for non-critical operations
- ❌ Shared mutable state between services
- ❌ Service-specific logic in the gateway layer

#### Security Violations
- ❌ Services bypassing authentication through the auth-service
- ❌ Direct client access to internal service endpoints
- ❌ Hardcoded credentials or tokens in service code

### Compliance Requirements

- All services must implement health check endpoints
- Services must use standardized logging, environment-specific

## Security Rules
### Input Validation

### Authentication Implementation

Flask-Login

### OWASP Compliance

### Secret Management Rules

## Async & Concurrency
### Required Async Patterns

- Use `async`/`await` for I/O operations (file

### Forbidden Sync Patterns

### Best Practices

## Error Handling
### Required Patterns

### Forbidden Patterns

### Exception Guidelines

## Database Access
### ORM Usage

- **Prefer ORM over raw SQL**: Use the framework's ORM (Object-Relational Mapping) for standard database operations
- **Model-based queries**: Leverage model classes for type-safe database interactions
- **Relationship handling**: Use ORM relationship definitions for joins and foreign key operations

### Raw SQL Guidelines

### Migration Conventions

### Service-Specific Database Rules

- **auth-service**: Handle user, role, and permission models with appropriate indexing
- **hr-service**: Implement attendance tracking with proper timestamp handling
- **finance-service**: Ensure decimal precision for monetary calculations
- **notification-service**: Optimize configuration queries for performance

## Testing Standards
### Test File Organization

### Naming Rules

#### Test Files
- **MUST** start with `test_`
- **MUST** end with `.py`
- **MUST** mirror source code structure

#### Test Functions
- **MUST** start with `test_`
- **MUST** use descriptive names indicating what is being tested
- **MUST** include expected outcome in name
- **SHOULD** use snake_case

#### Test Classes
- **MUST** start with `Test`
- **MUST** use PascalCase
- **SHOULD** group related test methods

### Test Quality Rules

#### Test Independence
- Tests **MUST NOT** depend on execution order
- Tests **MUST** clean up their own state
- Tests **MUST NOT** share mutable state

#### Assertion Rules
- **MUST** have at least one assertion per test
- **SHOULD** use descriptive assertion messages
- **MUST** test one logical concept per test function

#### API Testing Requirements
- **MUST** test all HTTP methods (GET, POST, DELETE)
- **MUST** test both success and error scenarios
- **MUST** validate response status codes
- **MUST** validate response data structure

### Coverage Requirements

`/health`

## Anti-Patterns (Never Do)
### Code Organization

Java

### Development Practices

passwords

### Documentation