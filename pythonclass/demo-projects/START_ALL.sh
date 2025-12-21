#!/bin/bash

# Complete Docker Setup and Start Script
# This script builds and starts ALL demo projects

set -e  # Exit on error

echo "=========================================="
echo "🚀 Python Full Stack - Complete Setup"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not running!${NC}"
    echo "Please start Docker Desktop and try again."
    exit 1
fi

echo -e "${GREEN}✅ Docker is running${NC}"
echo ""

# Clean up old containers and volumes
echo -e "${YELLOW}🧹 Cleaning up old containers...${NC}"
docker-compose down -v 2>/dev/null || true

echo ""
echo -e "${YELLOW}📦 Building Docker images...${NC}"
echo "This may take 5-10 minutes on first run..."
echo ""

# Build all services
docker-compose build --no-cache

echo ""
echo -e "${GREEN}✅ Build complete!${NC}"
echo ""
echo -e "${YELLOW}🚀 Starting all services...${NC}"
echo ""

# Start core services
docker-compose up -d backend frontend demo-server db redis mongo

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo -e "${GREEN}✅ Core services started!${NC}"
echo ""
echo "=========================================="
echo "📊 Service Status"
echo "=========================================="

# Check service status
docker-compose ps

echo ""
echo "=========================================="
echo "🌐 Access Points"
echo "=========================================="
echo ""
echo -e "${GREEN}Main Application:${NC}"
echo "  📱 Live Demos:     http://localhost:8080"
echo "  🎨 React Frontend: http://localhost:3000"
echo "  🔧 Backend API:    http://localhost:5000/api"
echo ""
echo -e "${GREEN}Databases:${NC}"
echo "  🐘 PostgreSQL:     localhost:5432"
echo "  🔴 Redis:          localhost:6379"
echo "  🍃 MongoDB:        localhost:27017"
echo ""
echo -e "${YELLOW}Optional Services (use profiles):${NC}"
echo "  🔧 Microservices:  docker-compose --profile microservices up -d"
echo "  💬 Chat Server:    docker-compose --profile chat up -d"
echo ""
echo "=========================================="
echo "🧪 Quick Tests"
echo "=========================================="
echo ""

# Test backend API
echo -n "Testing Backend API... "
if curl -s http://localhost:5000/api/todos > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Working${NC}"
else
    echo -e "${RED}❌ Failed${NC}"
    echo "Run: docker logs python-fullstack-backend"
fi

# Test frontend
echo -n "Testing Frontend... "
if curl -s http://localhost:3000 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Working${NC}"
else
    echo -e "${RED}❌ Failed${NC}"
    echo "Run: docker logs python-fullstack-frontend"
fi

# Test demo server
echo -n "Testing Demo Server... "
if curl -s http://localhost:8080 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Working${NC}"
else
    echo -e "${RED}❌ Failed${NC}"
    echo "Run: docker logs python-fullstack-demos"
fi

echo ""
echo "=========================================="
echo "📝 Next Steps"
echo "=========================================="
echo ""
echo "1. Open your browser to: http://localhost:8080"
echo "2. Click on any demo to test it"
echo "3. Check logs: docker-compose logs -f [service-name]"
echo "4. Stop all: docker-compose down"
echo ""
echo -e "${GREEN}🎉 Setup Complete! Happy Coding!${NC}"
echo ""
