---
applyTo: '**'
---
# README

## Repository Overview
OrganiStation is a microservices-based organizational management platform that integrates human resources, financial management, project tracking, and communication tools into a unified system.

### What is OrganiStation?

- Employee records and HR operations
- Financial budgets, expenses, and invoices
- Project management with tasks and milestones
- Document storage with AI-powered search
- Internal notifications and communications

### System Architecture

The platform consists of multiple microservices:

- **Gateway**: API routing and frontend serving
- **Auth Service**: User authentication and authorization
- **HR Service**: Human resources management
- **Finance Service**: Financial operations
- **Notification Service**: Communication system
- **Frontend**: React web application

### Technology Stack

- **Backend**: Python-based microservices
- **Frontend**: React application
- **Database**: MongoDB
- **Authentication**: JWT-based security
- **Architecture**: RESTful APIs with gateway pattern

## Deployment Architecture
### Service Layout

OrganiStation deploys as a distributed microservices system:

```
Gateway Service (Entry Point)
├── Frontend Assets (React SPA)
└── API Routes (/api/*)
    ├── /api/auth/* → Auth Service
    ├── /api/hr/* → HR Service
    ├── /api/finance/* → Finance Service
    └── /api/notifications/* → Notification Service
```

### Required Infrastructure

| Component | Purpose | Dependencies |
|-----------|---------|-------------|
| Auth Service | Authentication & authorization | MongoDB |
| HR Service | Human resources management | MongoDB |
| Finance Service | Budget & financial operations | MongoDB |
| Notification Service | System notifications | MongoDB |
| MongoDB | Data persistence | None |

### Environment Variables

```bash
# Core Configuration
PORT=<service-port>
HOST=<bind-address>
MONGODB_URI=<mongodb-connection-string>

# Security
JWT_SECRET=<jwt-signing-secret>
INTERNAL_SERVICE_SECRET=<inter-service-auth>

# Service Discovery
FINANCE_SERVICE_URL=<finance-service-endpoint>
```

### Deployment Considerations

- **Gateway First**: Deploy gateway service as the primary entry point
- **Database**: Ensure MongoDB is accessible to all services
- **Service Discovery**: Configure service URLs for inter-service communication
- **Security**: Use consistent secrets across all services for internal authentication

## Prerequisites
Before setting up OrganiStation

### Required Software

### Development Tools

etc.)

### Environment Setup

| Variable | Description | Required |
|----------|-------------|----------|
| `PORT` | Application port number | Yes |
| `INTERNAL_SERVICE_SECRET` | Secret for internal service communication | Yes |
| `MONGODB_URI` | MongoDB connection string | Yes |
| `JWT_SECRET` | Secret key for JWT token signing | Yes |
| `FINANCE_SERVICE_URL` | URL for the finance service | Yes |
| `HOST` | Application host address | Yes |

### System Requirements

## Installation
### Prerequisites

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd OrganiStation
   ```

3. **Environment Configuration**

Create a `.env` file in the root directory and configure the following variables:

   ```env
   PORT=3000
   HOST=localhost
   MONGODB_URI=mongodb://localhost:27017/organistation
   JWT_SECRET=your-jwt-secret-key
   INTERNAL_SERVICE_SECRET=your-internal-service-secret
   FINANCE_SERVICE_URL=http://localhost:3001
   ```

4. **Database Setup**

Ensure MongoDB is running and accessible via the configured `MONGODB_URI`.

5. **Start the Application**

   ```bash
   npm start
   # or
   yarn start
   ```

### Troubleshooting

## Configuration
### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGODB_URI` | MongoDB connection string | Yes |
| `JWT_SECRET` | Secret key for JWT token signing | Yes |
| `INTERNAL_SERVICE_SECRET` | Secret for internal service communication | Yes |
| `FINANCE_SERVICE_URL` | URL endpoint for the finance service | Yes |

### Configuration Setup

1. Create a `.env` file in the project root:

2. Update the `.env` file with your specific values:

   ```env
   PORT=3000
   HOST=localhost
   MONGODB_URI=mongodb://localhost:27017/organistation
   JWT_SECRET=your-secure-jwt-secret
   INTERNAL_SERVICE_SECRET=your-internal-service-secret
   FINANCE_SERVICE_URL=http://localhost:3001
   ```

## Development Environment
### Local Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd OrganiStation
   ```

3. **Environment Configuration**
   Create a `.env` file in the root directory with the following variables:

   ```env
   PORT=3000
   HOST=localhost
   MONGODB_URI=mongodb://localhost:27017/organistation
   JWT_SECRET=your-jwt-secret-key
   INTERNAL_SERVICE_SECRET=your-internal-service-secret
   FINANCE_SERVICE_URL=http://localhost:3001
   ```

### Development Workflow

1. **Start MongoDB**
   Ensure MongoDB is running locally or update `MONGODB_URI` to point to your MongoDB instance.

2. **Run the application**

   ```bash
   npm run dev
   ```

3. **Access the application**
   - Main application: `http://localhost:3000`
   - API endpoints available at the configured HOST and PORT

### Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|-----------|
| `PORT` | Application port | Yes |
| `HOST` | Application host | Yes |
| `MONGODB_URI` | MongoDB connection string | Yes |
| `JWT_SECRET` | Secret for JWT token signing | Yes |
| `INTERNAL_SERVICE_SECRET` | Secret for internal service communication | Yes |
| `FINANCE_SERVICE_URL` | URL for finance service integration | Yes |

### Development Tips

## Troubleshooting
### Common Issues and Solutions

#### Environment Variables Not Loading
**Problem**: Application fails to start with missing environment variable errors.

#### MongoDB Connection Issues
**Problem**: Cannot connect to MongoDB database.

permissions

#### Port Already in Use
**Problem**: Application fails to start with "port already in use" error.

#### Service Communication Failures
**Problem**: Internal service calls fail or timeout.

#### JWT Token Issues
**Problem**: Authentication failures or invalid token errors.
