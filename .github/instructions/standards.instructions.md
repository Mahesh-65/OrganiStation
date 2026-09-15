---
applyTo: '**'
---
# standards

## API Standards
### REST API Design

**Resource Naming**
- Use plural nouns for resource collections: `/api/employees`, `/api/projects`
- Use singular identifiers for specific resources: `/api/employees/{eid}`, `/api/projects/{pid}`
- Maintain consistent parameter naming across services (e.g., `eid` for employee ID, `pid` for project ID)

**HTTP Methods**
- `GET` for retrieving resources and collections
- `POST` for creating new resources and operations
- `PUT` for updating existing resources
- `DELETE` for removing resources

**Response Schemas**
- All API responses must follow standardized schema patterns
- Use configuration classes for response validation:
  - `RoleResponse.Config` for role data
  - `UserResponse.Config` for user data
  - `PermissionResponse.Config` for permission data

**Authentication & Authorization**
- JWT token-based authentication with standardized `TokenPayload` structure
- Token payload includes: `exp`, `permissions`, `role`, and `sub` fields
- Consistent authentication endpoints: `/login`, `/logout`, `/refresh`, `/register`

**Error Handling**
- Standardized error response format across all services
- Consistent HTTP status codes for similar operations
- Proper error messages for client consumption

**Service Integration**
- Health check endpoints: `/api/auth/health`
- Consistent service configuration through `Settings` classes
- Standardized notification patterns for cross-service communication

## Testing Standards
### Test Coverage Requirements

- **Minimum Coverage**: 80% code coverage for all Python modules
- **Critical Path Coverage**: 100% coverage for API endpoints

### Required Test Types

#### Unit Tests
- **Scope**: Individual functions, methods, and classes
- **Framework**: pytest (primary testing framework for Python)
- **Isolation**: Tests must be independent and not rely on external dependencies
- **Mocking**: Use unittest.mock for external service dependencies

#### Integration Tests
- **API Endpoints**: All REST endpoints (GET, POST, DELETE) must have integration tests
- **Health Checks**: Dedicated tests for health monitoring endpoints (`/api/health`, `/health`, `/ready`)
- **Database Integration**: Tests for data persistence and retrieval operations

#### End-to-End Tests
- **User Workflows**: Complete user journeys through the application
- **API Workflows**: Full request-response cycles for critical business processes

### Test Naming Conventions

#### Test Files
- **Pattern**: `test_<module_name>.py`
- **Location**: Mirror source code structure in `tests/` directory
- **Example**: `tests/test_employee_service.py` for `src/employee_service.py`

#### Test Functions
- **Unit Tests**: `test_<function_name>_<scenario>()`
- **Integration Tests**: `test_<endpoint>_<http_method>_<expected_outcome>()`
- **Examples**:
  - `test_create_employee_success()`
  - `test_get_employees_returns_list()`
  - `test_delete_employee_invalid_id_returns_404()`

#### Test Classes
- **Pattern**: `Test<ClassName>`
- **Example**: `TestEmployeeService`, `TestHealthEndpoints`

### Test Data Management

## API Standards
### RESTful Design Principles

The OrganiStation API follows RESTful design principles with consistent HTTP method usage and resource-based URL patterns:

- **GET**: Retrieve resources (collections and individual items)
- **POST**: Create new resources
- **PUT**: Update existing resources
- **DELETE**: Remove resources

### URL Structure

APIs follow a hierarchical resource-based structure:

#### Examples:
- `GET /api/employees` - List all employees
- `GET /api/employees/{eid}` - Get specific employee
- `GET /api/employees/{eid}/attendance` - Get employee attendance records
- `POST /api/employees` - Create new employee
- `PUT /api/employees/{eid}` - Update employee
- `DELETE /api/employees/{eid}` - Delete employee

### Resource Naming Conventions

- Use plural nouns for resource collections (`/employees`, `/projects`, `/tickets`)
- Use lowercase with hyphens for multi-word resources
- Path parameters use descriptive names (`{eid}` for employee ID, `{pid}` for project ID)

### HTTP Methods by Resource Type

| Resource | GET | POST | PUT | DELETE |
|----------|-----|------|-----|--------|
| Employees | ✓ List/Get | ✓ Create | ✓ Update | ✓ Delete |
| Projects | ✓ List/Get | ✓ Create | ✓ Update | ✓ Delete |
| Documents | ✓ List/Get | ✓ Upload | - | ✓ Delete |
| Tickets | ✓ List/Get | ✓ Create | ✓ Update | ✓ Delete |
| Expenses | ✓ List/Get | ✓ Create | ✓ Update | ✓ Delete |
| Invoices | ✓ List/Get | ✓ Create | ✓ Update | ✓ Delete |

### Health Check Endpoints

Multiple health monitoring endpoints are implemented for system status verification:

- `GET /health` - Basic health check
- `GET /ready` - Readiness probe
- `GET /api/health` - API-specific health status
- `GET /api/auth/health` - Authentication service health

### Special Endpoints

#### System Operations
- `GET /api/summary` - System summary information
- `POST /api/reset` - Database reset (development/testing)
- `POST /refresh` - System refresh operation

#### Document Operations
- `GET /api/documents/view/{doc_hash}` - Serve original document files
- `POST /api/query` - Query documents
- `POST /ingest` - Document ingestion

#### Authentication & User Management
- `POST /login` - User authentication
- `POST /logout` - User logout
- `POST /register` - User registration
- `POST /change-password` - Password change

#### Notifications
- `POST /notifications/broadcast` - Broadcast to all users
- `POST /notifications/user/{userId}` - User-specific notifications
- `POST /notifications/send-email` - Email notifications

### API Versioning

## Engineering Standards
### Code Review Standards

architectural consistency
- Ensure proper error handling

### Documentation Standards

- Maintain clear and comprehensive API documentation
- Document all endpoints with proper HTTP method usage
- Include health check endpoint documentation for monitoring purposes

### Development Standards

#### Programming Language
- **Primary Language**: Python
- Follow Python PEP standards and best practices
- Maintain consistent coding style across the codebase

#### API Design Standards
- **RESTful Design**: Use consistent HTTP methods with resource-based URLs
  - `GET` for retrieving resources
  - `POST` for creating new resources
  - `DELETE` for removing resources
- **Resource Naming**: Use clear, descriptive resource paths (e.g., `/api/employees`)
- **HTTP Status Codes**: Return appropriate status codes for different operations

#### Health Monitoring Standards
- Implement multiple health check endpoints for comprehensive system monitoring:
  - `/api/health` - API-specific health status
  - `/health` - General application health
  - `/ready` - Readiness probe for deployment orchestration
- Health endpoints should return consistent response formats
- Include relevant system status information in health responses

#### Quality Assurance
- Implement proper error handling and validation
- Follow consistent patterns for request/response handling
- Maintain backward compatibility when making API changes
- Use appropriate logging levels and structured logging formats

## Code Quality Standards
### Programming Language Standards

### API Standards

- **RESTful Design**: Implement consistent HTTP methods with resource-based URLs
  - GET for data retrieval
  - POST for resource creation
  - DELETE for resource removal
- **Health Monitoring**: Implement standardized health check endpoints
  - `/api/health` - Application health status
  - `/health` - Basic health check
  - `/ready` - Readiness probe for deployment

### Code Quality Metrics

### Quality Gates