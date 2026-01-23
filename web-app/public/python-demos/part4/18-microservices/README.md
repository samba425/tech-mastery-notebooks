# Microservices Architecture Demo

## Overview
Microservices architecture with FastAPI, Docker, and service communication.

## Features
- Multiple microservices
- FastAPI framework
- Docker containerization
- Service communication
- API Gateway

## Setup

```bash
# Install dependencies
pip install fastapi uvicorn docker

# Build Docker images
docker-compose build

# Start all services
docker-compose up
```

## Project Structure
```
18-microservices/
├── user-service/
│   └── main.py
├── post-service/
│   └── main.py
├── api-gateway/
│   └── main.py
└── docker-compose.yml
```

## Services
- User Service: Port 8001
- Post Service: Port 8002
- API Gateway: Port 8000

## Usage
1. Start all services: `docker-compose up`
2. Access API Gateway: http://localhost:8000
3. Check service health: http://localhost:8000/health

## Quick Start (Without Docker)

### Option 1: Run All Services with Script
```bash
chmod +x run-all.sh
./run-all.sh
```

### Option 2: Run Services Manually
```bash
# Terminal 1 - User Service
python user-service.py

# Terminal 2 - Post Service  
python post-service.py

# Terminal 3 - API Gateway
python api-gateway.py
```

## Testing

### Test User Service
```bash
# Get all users
curl http://localhost:8001/users

# Create user
curl -X POST http://localhost:8001/users \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "email": "alice@example.com"}'
```

### Test Post Service
```bash
# Get all posts
curl http://localhost:8002/posts

# Create post
curl -X POST http://localhost:8002/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello", "content": "World", "author_id": 1}'
```

### Test API Gateway
```bash
# Check health
curl http://localhost:8000/health

# Get users through gateway
curl http://localhost:8000/users

# Get posts through gateway
curl http://localhost:8000/posts
```

## Files
- `user-service.py` - User microservice (port 8001)
- `post-service.py` - Post microservice (port 8002)
- `api-gateway.py` - API Gateway (port 8000)
- `docker-compose.yml` - Docker configuration
- `run-all.sh` - Script to run all services

## Note
This is a simplified demo. Full implementation requires Docker and multiple service configurations.

