---
applyTo: '**'
---
# standards

## API Standards
### RESTful Design Principles

All APIs follow RESTful design patterns with consistent resource naming and HTTP method usage:

- **GET** - Retrieve resources or collections
- **POST** - Create new resources
- **PUT** - Update existing resources
- **DELETE** - Remove resources

### Resource Identification

Resources use consistent identifier patterns:

| Resource | Identifier | Example |
|----------|------------|----------|
| Documents | `doc_hash` | `/api/documents/{doc_hash}` |
| Employees | `eid` | `/api/employees/{eid}` |
| Expenses | `eid` | `/api/expenses/{eid}` |
| Invoices | `iid` | `/api/invoices/{iid}` |
| Projects | `pid` | `/api/projects/{pid}` |
| Tickets | `tid` | `/api/tickets/{tid}` |
| Users | `user_id` | `/{user_id}` |

### Response Schema Standards

All services implement standardized response schemas:

- **UserResponse** - User entity responses with configuration
- **RoleResponse** - Role entity responses with permissions
- **PermissionResponse** - Permission entity responses

### Health Check Endpoints

All services must implement health check endpoints:

```
GET /api/{service}/health
```

### Error Handling

APIs return consistent HTTP status codes:

## Testing Standards
### Test Coverage Requirements

### Required Test Types

#### API Testing
- All REST endpoints must have corresponding test cases
- Test both success and error scenarios
- Validate HTTP status codes, response structure, and data integrity
- Include tests for edge cases and boundary conditions

#### Database Testing
- Test CRUD operations for all entities
- Validate data constraints and relationships
- Test transaction rollback scenarios
- Include performance tests for complex queries

#### Security Testing
- Authentication and authorization tests
- Input validation and sanitization tests
- SQL injection and XSS prevention tests

### Test Organization

#### Directory Structure

#### Test Categories
- **Unit Tests**: Test individual functions and methods in isolation
- **Integration Tests**: Test component interactions and API endpoints
- **System Tests**: Test complete workflows and user scenarios

### Performance Testing
- Load testing for API endpoints under expected traffic
- Database performance testing for complex queries
- Memory usage and resource consumption monitoring

## API Standards
### RESTful Design Principles

The OrganiStation API follows REST architectural conventions with proper HTTP method usage and resource-based URL structures:

- **GET** - Retrieve resources (collections and individual items)
- **POST** - Create new resources
- **PUT** - Update existing resources
- **DELETE** - Remove resources

### URL Structure

All API endpoints follow a consistent resource-based URL pattern:

```
/api/{resource}
/api/{resource}/{id}
/api/{resource}/{id}/{sub-resource}
```

**Examples:**
- `/api/employees` - Employee collection
- `/api/employees/{eid}` - Individual employee
- `/api/employees/{eid}/attendance` - Employee sub-resource
- `/api/projects/{pid}/tasks` - Nested resource operations

### HTTP Methods and Operations

| Method | Purpose | Example Endpoints |
|--------|---------|------------------|
| GET | Retrieve data | `/api/employees`, `/api/projects/{pid}` |
| POST | Create resources | `/api/employees`, `/api/projects/{pid}/tasks` |
| PUT | Update resources | `/api/employees/{eid}`, `/api/tasks/{tid}` |
| DELETE | Remove resources | `/api/employees/{eid}`, `/api/projects/{pid}` |

### Resource Naming Conventions

`{pid}` for project ID, `{tid}` for task/ticket ID

### Health Check Standards

Multiple health check endpoints are provided for comprehensive system monitoring:

- `/api/health` - General API health status
- `/api/auth/health` - Authentication service health
- `/health` - System-level health check
- `/ready` - Readiness probe endpoint

### API Versioning

### Response Standards

- Consistent JSON response format
- Appropriate HTTP status codes
- Resource-specific endpoints for different operations (view, list, create, update, delete)
- Document viewing through dedicated endpoints: `/api/documents/view/{doc_hash}`

## Engineering Standards
### Code Review Standards

#### API Design Standards
- **RESTful API Design**: All APIs must follow REST conventions with proper HTTP methods and resource-based URLs
  - Use appropriate HTTP methods: GET for retrieval, POST for creation, PUT for updates, DELETE for removal
  - Implement resource-based URL patterns (e.g., `/api/employees`, `/api/projects/{pid}/tasks`)
  - Maintain consistent endpoint naming conventions

#### Monitoring and Health Checks
- **Health Check Implementation**: All services must provide comprehensive health check endpoints
  - Primary health endpoint: `/api/health`
  - System health endpoint: `/health`
  - Readiness probe endpoint: `/ready`
  - Health checks should verify service dependencies and system state

### Documentation Standards

#### API Documentation
- All API endpoints must be documented with:
  - Request/response schemas
  - HTTP status codes
  - Error handling patterns
  - Authentication requirements

#### Code Documentation
- Functions and classes must include clear docstrings
- Complex business logic requires inline comments
- README files must be maintained for each service/module

### Development Standards

#### Code Quality
- Follow language-specific style guides
- Implement proper error handling and logging
- Use meaningful variable and function names
- Maintain consistent code formatting

#### Testing Requirements
- Unit tests for all business logic
- Integration tests for API endpoints
- Health check endpoint validation
- Minimum code coverage thresholds must be maintained

## Code Quality Standards
### API Design Standards

#### RESTful API Conventions
The codebase follows REST architectural principles with proper HTTP method usage:

- **GET** requests for data retrieval (e.g., `/api/employees`)
- **POST** requests for resource creation (e.g., `/api/employees`, `/api/projects/{pid}/tasks`)
- **PUT** requests for resource updates (e.g., `/api/tasks/{tid}`)
- **DELETE** requests for resource removal (e.g., `/api/employees/{eid}`)

#### Resource-Based URL Structure
APIs use clear, hierarchical resource paths:
- Employee management: `/api/employees`
- Task management within projects: `/api/projects/{pid}/tasks`
- Individual task operations: `/api/tasks/{tid}`

### Monitoring and Health Checks

#### Health Check Implementation
Multiple health check endpoints are implemented for comprehensive system monitoring:

| Endpoint | Purpose |
|----------|----------|
| `/api/health` | API service health status |
| `/health` | General application health |
| `/ready` | Readiness probe for deployment |

These endpoints enable proper monitoring