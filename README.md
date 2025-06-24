# 🏗️ Microservices E-commerce Backend

A comprehensive microservices-based e-commerce backend built with Django, Docker, and PostgreSQL. This project follows modern microservices architecture patterns with independent services for different business domains.

## 📋 Table of Contents

- [Architecture Overview](#-architecture-overview)
- [Services](#-services)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Database Schema](#-database-schema)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

## 🏛️ Architecture Overview

This project implements a microservices architecture with the following principles:

- **Service Independence**: Each service can be developed, deployed, and scaled independently
- **Database per Service**: Each service owns its data and database
- **API Gateway**: Centralized entry point for all client requests
- **Event-Driven Communication**: Services communicate via Kafka for async operations
- **Containerization**: All services are containerized using Docker

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend/     │    │   API Gateway   │    │    Load         │
│   Mobile App    │───▶│    (Port TBD)   │───▶│   Balancer      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
        ┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼──────┐
        │ Auth Service │ │Product      │ │ Order      │
        │ (Port 8000)  │ │Service      │ │Service     │
        └──────────────┘ │(Port TBD)   │ │(Port TBD)  │
                         └─────────────┘ └────────────┘
                │               │               │
        ┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼──────┐
        │ PostgreSQL   │ │PostgreSQL   │ │PostgreSQL  │
        │ (Port 5432)  │ │(Port 5433)  │ │(Port TBD)  │
        └──────────────┘ └─────────────┘ └────────────┘
```

## 🔧 Services

### ✅ Auth Service (Implemented)
- **Port**: 8000
- **Database**: PostgreSQL (Port 5432)
- **Features**:
  - User registration with phone number
  - JWT-based authentication
  - Custom phone number authentication backend
  - User profile management

### 🚧 In Development
- **API Gateway**: Central routing and authentication
- **Product Service**: Product catalog management
- **Cart Service**: Shopping cart functionality
- **Order Service**: Order processing and management
- **Payment Service**: Payment processing integration
- **Chat Service**: Customer support chat

### 🔧 Infrastructure
- **Kafka**: Message broker for inter-service communication
- **Redis**: Caching and session storage
- **PostgreSQL**: Primary database for each service

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.1.2 + Django REST Framework
- **Database**: PostgreSQL 15+
- **Authentication**: JWT (Simple JWT)
- **API Documentation**: (To be added)
- **Message Queue**: Apache Kafka
- **Cache**: Redis

### DevOps
- **Containerization**: Docker & Docker Compose
- **Database Migration**: Django ORM
- **Process Manager**: Gunicorn
- **Networking**: Docker Bridge Network

### Development Tools
- **Python**: 3.12+
- **Package Management**: pip + requirements.txt
- **Environment**: Docker containers
- **Database Client**: PostgreSQL client tools

## 📋 Prerequisites

- **Docker** and **Docker Compose** installed
- **Git** for version control
- **Python 3.12+** (for local development)
- **PostgreSQL client tools** (optional, for database access)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
# HTTPS
git clone https://github.com/minhminh12315/backend.git

# SSH
git clone git@github.com:minhminh12315/backend.git

cd backend
```

### 2. Environment Setup

Create environment variables file:

```bash
# Create .env file in project root
touch .env
```

Add the following environment variables to `.env`:

```bash
# Database Configuration
POSTGRES_PASSWORD=your_postgres_password
DB_PASSWORD=your_db_password
DB_NAME=auth_db
DB_USER=postgres
DB_HOST=postgres
DB_PORT=5432

# Django Configuration
SECRET_KEY=your_secret_key_here
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# JWT Configuration
JWT_SECRET_KEY=your_jwt_secret_key
```

### 3. Start Services

```bash
# Build and start all services
docker-compose up --build

# Or start specific service
docker-compose up auth-service

# Run in background
docker-compose up -d
```

### 4. Database Setup

The auth-service automatically runs migrations on startup, but you can also run them manually:

```bash
# Access auth-service container
docker-compose exec auth-service bash

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## 📚 API Documentation

### Auth Service Endpoints

**Base URL**: `http://localhost:8000/api/`

#### User Registration
```http
POST /api/register/
Content-Type: application/json

{
    "phone_number": "+1234567890",
    "password": "secure_password",
    "fullname": "John Doe"
}
```

**Response**:
```json
{
    "message": "User created successfully",
    "user_id": 1
}
```

#### User Login
```http
POST /api/login/
Content-Type: application/json

{
    "phone_number": "+1234567890",
    "password": "secure_password"
}
```

**Response**:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user_id": 1,
    "phone_number": "+1234567890"
}
```

### Authentication

Include the access token in the Authorization header for protected endpoints:

```http
Authorization: Bearer <access_token>
```

## 💻 Development

### Local Development Setup

If you prefer to develop without Docker:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
cd auth-service
pip install -r requirements.txt

# Set up local PostgreSQL database
# Update settings.py with local database configuration

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver 8000
```

### Code Structure

```
auth-service/
├── auth_service/              # Django project settings
│   ├── __init__.py
│   ├── settings.py           # Main configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── apps/
│   └── users/               # User management app
│       ├── models.py        # User model
│       ├── views.py         # API views
│       ├── urls.py          # App URLs
│       ├── backends.py      # Custom auth backend
│       ├── admin.py         # Admin configuration
│       └── migrations/      # Database migrations
├── Dockerfile               # Container configuration
├── requirements.txt         # Python dependencies
└── manage.py               # Django management
```

### Adding New Services

1. Create new service directory
2. Add Dockerfile
3. Update docker-compose.yml
4. Add database configuration
5. Implement service logic
6. Update API Gateway routing

## 🗄️ Database Schema

### Auth Service Database (auth_db)

#### users_user table
```sql
CREATE TABLE users_user (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE,
    email VARCHAR(254),
    phone_number VARCHAR(15) UNIQUE,
    fullname VARCHAR(255),
    password VARCHAR(128) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    date_joined TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## 🧪 Testing

### Running Tests

```bash
# Run tests in Docker container
docker-compose exec auth-service python manage.py test

# Run specific test file
docker-compose exec auth-service python manage.py test apps.users.tests

# Run with coverage
docker-compose exec auth-service coverage run --source='.' manage.py test
docker-compose exec auth-service coverage report
```

### Manual API Testing

```bash
# Register a new user
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+1234567890",
    "password": "testpassword",
    "fullname": "Test User"
  }'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+1234567890",
    "password": "testpassword"
  }'
```

## 🚀 Deployment

### Production Deployment

1. **Update Environment Variables**:
   ```bash
   DEBUG=0
   ALLOWED_HOSTS=your-domain.com
   SECRET_KEY=production_secret_key
   ```

2. **Use Production Database**:
   - Set up managed PostgreSQL instance
   - Update database connection settings

3. **Configure SSL/TLS**:
   - Set up reverse proxy (nginx)
   - Configure SSL certificates

4. **Deploy with Docker**:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Scaling Services

```bash
# Scale specific service
docker-compose up --scale auth-service=3

# Use Docker Swarm for production scaling
docker stack deploy -c docker-compose.yml gozic-backend
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Write comprehensive tests
- Document new API endpoints
- Update README for new features
- Use meaningful commit messages

## 📞 Support

- **GitHub Issues**: [Create an issue](https://github.com/minhminh12315/backend/issues)
- **Documentation**: [Wiki](https://github.com/minhminh12315/backend/wiki)
- **Discussions**: [GitHub Discussions](https://github.com/minhminh12315/backend/discussions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Auth Service with JWT
- ✅ Docker containerization
- ✅ PostgreSQL integration

### Phase 2 (Next)
- 🚧 API Gateway implementation
- 🚧 Product Service
- 🚧 Cart Service

### Phase 3 (Future)
- 📋 Order Management
- 📋 Payment Integration
- 📋 Real-time Chat
- 📋 Notification Service
- 📋 Analytics Dashboard

---

**Built with ❤️ by the GoZic Team**

For more information, visit our [GitHub repository](https://github.com/minhminh12315/backend).
