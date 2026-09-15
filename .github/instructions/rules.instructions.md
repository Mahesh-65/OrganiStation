---
applyTo: '**'
---
# rules

## Naming Conventions
### API Endpoints

**Resource-Based URLs**
- Use plural nouns for resource collections: `/api/employees`, `/api/projects`
- Use singular identifiers for specific resources: `/api/employees/{eid}`, `/api/tasks/{tid}`
- Nest related resources appropriately: `/api/projects/{pid}/tasks`

**HTTP Methods**
- `GET` for retrieving resources
- `POST` for creating new resources
- `PUT` for updating existing resources
- `DELETE` for removing resources

### Health Check Endpoints

**Standard Health Endpoints**
- `/health` - Basic health status
- `/api/health` - API-specific health check
- `/ready` - Readiness probe for container orchestration

### Path Parameters

`{pid}` for project ID

## Architecture Rules
### Layer Boundaries

**Gateway Layer**
- Must serve as the single entry point for all client requests
- Responsible for routing API calls to appropriate microservices
- Must serve frontend static assets
- Cannot directly access service databases

**Frontend Layer**
- Must communicate exclusively through the gateway
- Cannot make direct calls to backend services
- Must handle authentication context management
- Should maintain separation of concerns with React components

**Service Layer**
- Each microservice must maintain domain boundaries:
  - `auth-service`: Authentication and authorization only
  - `hr-service`: Human resources management only
  - `finance-service`: Budget and financial operations only
  - `notification-service`: Notification handling only
- Services cannot directly communicate with each other
- Must expose RESTful APIs for gateway consumption

### Import Rules

**Frontend Dependencies**
- Frontend must not import backend service code
- API communication must use defined contracts only
- Authentication context must be centrally managed

### Forbidden Patterns

**Direct Service Communication**
- ❌ Service-to-service direct API calls
- ❌ Shared databases between services
- ❌ Frontend bypassing gateway for service access

**Tight Coupling**
- ❌ Services sharing business logic implementations
- ❌ Cross-domain data access (e.g., HR service accessing finance data directly)
- ❌ Gateway implementing business logic beyond routing

## Database Access
### ORM Usage

- **Prefer ORM methods** for standard CRUD operations to maintain consistency and leverage built-in security features
- **Use type-safe queries** when available in your ORM to catch errors at compile time
- **Implement proper error handling** for database operations with appropriate logging
- **Follow the repository pattern** to abstract database access and improve testability

### Raw SQL Guidelines

### Query Performance

- **Index frequently queried columns** based on service-specific access patterns
- **Use database query analysis tools** to identify slow queries

### Migration Conventions

complete change
- **Document breaking changes** in migration comments, team communications
- **Coordinate cross-service migrations** when changes affect multiple microservices

### Connection Management

## Testing Standards
### Test File Naming

#### Unit Tests
- Format: `{component}.test.{ext}`
- Examples: `employee.test.js`, `project.service.test.ts`

#### Integration Tests
- Format: `{feature}.integration.test.{ext}`
- Examples: `employee-api.integration.test.js`, `database.integration.test.ts`

#### End-to-End Tests
- Format: `{workflow}.e2e.test.{ext}`
- Examples: `employee-management.e2e.test.js`, `project-creation.e2e.test.js`

### Test Function Naming

#### Descriptive Test Names
- Use clear, descriptive names that explain what is being tested
- Format: `should_{expected_behavior}_when_{condition}`
- Examples:
  - `should_return_employee_data_when_valid_id_provided`
  - `should_throw_error_when_employee_not_found`
  - `should_create_project_when_valid_data_submitted`

#### Test Suite Organization
- Group related tests using `describe()` blocks
- Use nested `describe()` blocks for different scenarios
- Example structure:

### Test Data Management

#### Test Data Naming
- Use descriptive variable names for test data
- Prefix with `mock`, `stub`, or `fixture` as appropriate
- Examples: `mockEmployeeData`, `stubProjectResponse`, `validUserFixture`

#### Test Database
- Use separate test database with `_test` suffix
- Example: `organistation_test`
- Clean up test data after each test run