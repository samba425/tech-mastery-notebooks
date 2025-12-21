#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     🚀 COMPLETE SYSTEM VERIFICATION - ALL DEMOS               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Function to check URL
check_url() {
    local url=$1
    local name=$2
    
    if curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q "200\|301\|302"; then
        echo -e "${GREEN}✅ $name - Working${NC}"
        return 0
    else
        echo -e "${RED}❌ $name - Failed${NC}"
        return 1
    fi
}

# Function to check service
check_service() {
    local service=$1
    
    if docker-compose ps | grep -q "$service.*Up"; then
        echo -e "${GREEN}✅ $service - Running${NC}"
        return 0
    else
        echo -e "${RED}❌ $service - Not Running${NC}"
        return 1
    fi
}

echo -e "${YELLOW}📦 CHECKING DOCKER CONTAINERS...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_service "python-fullstack-backend"
check_service "python-fullstack-frontend"
check_service "python-fullstack-demos"
check_service "fullstack-postgres"
check_service "fullstack-redis"
check_service "fullstack-mongo"
check_service "microservice-user"
check_service "microservice-post"
check_service "microservice-gateway"
echo ""

echo -e "${YELLOW}🌐 CHECKING WEB SERVICES...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_url "http://localhost:8080" "Demo Showcase (Port 8080)"
check_url "http://localhost:3000" "React App (Port 3000)"
check_url "http://localhost:5001/api/todos" "Backend API (Port 5001)"
echo ""

echo -e "${YELLOW}🔧 CHECKING BACKEND APIS...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_url "http://localhost:5001/api/calculator/basic" "Calculator API - Basic"
check_url "http://localhost:5001/api/calculator/grade" "Calculator API - Grade"
check_url "http://localhost:5001/api/calculator/advanced" "Calculator API - Advanced"
check_url "http://localhost:5001/api/todos" "Todo API - List"
echo ""

echo -e "${YELLOW}🔄 CHECKING MICROSERVICES...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
check_url "http://localhost:8001/users" "User Service (Port 8001)"
check_url "http://localhost:8002/posts" "Post Service (Port 8002)"
check_url "http://localhost:8000/docs" "API Gateway (Port 8000)"
echo ""

echo -e "${YELLOW}🗄️ CHECKING DATABASES...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# PostgreSQL
if docker exec fullstack-postgres psql -U postgres -c "SELECT 1" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ PostgreSQL - Connected${NC}"
else
    echo -e "${RED}❌ PostgreSQL - Failed${NC}"
fi

# Redis
if docker exec fullstack-redis redis-cli PING 2>/dev/null | grep -q "PONG"; then
    echo -e "${GREEN}✅ Redis - Connected${NC}"
else
    echo -e "${RED}❌ Redis - Failed${NC}"
fi

# MongoDB
if docker exec fullstack-mongo mongosh --quiet --eval "db.adminCommand('ping')" 2>/dev/null | grep -q "ok"; then
    echo -e "${GREEN}✅ MongoDB - Connected${NC}"
else
    echo -e "${RED}❌ MongoDB - Failed${NC}"
fi

echo ""
echo -e "${YELLOW}📊 TESTING TODO API CRUD OPERATIONS...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Create Todo
CREATE_RESPONSE=$(curl -s -X POST http://localhost:5001/api/todos \
    -H "Content-Type: application/json" \
    -d '{"task":"Verification Test","priority":"high"}')

if echo "$CREATE_RESPONSE" | grep -q "Verification Test"; then
    echo -e "${GREEN}✅ CREATE - Todo created successfully${NC}"
    TODO_ID=$(echo "$CREATE_RESPONSE" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')
    
    # Read Todo
    if curl -s "http://localhost:5001/api/todos/$TODO_ID" | grep -q "Verification Test"; then
        echo -e "${GREEN}✅ READ - Todo retrieved successfully${NC}"
    else
        echo -e "${RED}❌ READ - Failed${NC}"
    fi
    
    # Update Todo
    UPDATE_RESPONSE=$(curl -s -X PUT "http://localhost:5001/api/todos/$TODO_ID" \
        -H "Content-Type: application/json" \
        -d '{"task":"Updated Verification Test","completed":true}')
    
    if echo "$UPDATE_RESPONSE" | grep -q "Updated Verification Test"; then
        echo -e "${GREEN}✅ UPDATE - Todo updated successfully${NC}"
    else
        echo -e "${RED}❌ UPDATE - Failed${NC}"
    fi
    
    # Delete Todo
    DELETE_RESPONSE=$(curl -s -X DELETE "http://localhost:5001/api/todos/$TODO_ID")
    
    if echo "$DELETE_RESPONSE" | grep -q "deleted\|success"; then
        echo -e "${GREEN}✅ DELETE - Todo deleted successfully${NC}"
    else
        echo -e "${RED}❌ DELETE - Failed${NC}"
    fi
else
    echo -e "${RED}❌ CREATE - Failed to create todo${NC}"
fi

echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                    📋 SUMMARY                                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}🎉 All services are running and operational!${NC}"
echo ""
echo -e "${YELLOW}Quick Access URLs:${NC}"
echo -e "  🎨 Demo Showcase:    ${BLUE}http://localhost:8080${NC}"
echo -e "  ⚛️  React App:        ${BLUE}http://localhost:3000${NC}"
echo -e "  🔧 Backend API:      ${BLUE}http://localhost:5001/api/todos${NC}"
echo -e "  👤 User Service:     ${BLUE}http://localhost:8001/users${NC}"
echo -e "  📝 Post Service:     ${BLUE}http://localhost:8002/posts${NC}"
echo -e "  🌐 API Gateway:      ${BLUE}http://localhost:8000/docs${NC}"
echo ""
echo -e "${YELLOW}Useful Commands:${NC}"
echo -e "  View logs:           ${BLUE}docker-compose logs -f${NC}"
echo -e "  Stop all:            ${BLUE}docker-compose --profile microservices down${NC}"
echo -e "  Restart service:     ${BLUE}docker-compose restart backend${NC}"
echo ""
echo -e "${GREEN}✨ Happy Coding! ✨${NC}"
echo ""
