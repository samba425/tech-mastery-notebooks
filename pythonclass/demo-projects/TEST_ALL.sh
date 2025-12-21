#!/bin/bash

# Test All Demo Projects
# Validates that all services are working correctly

echo "=========================================="
echo "🧪 Testing All Demo Projects"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASSED=0
FAILED=0

test_endpoint() {
    local name=$1
    local url=$2
    local expected=$3
    
    echo -n "Testing $name... "
    
    response=$(curl -s -w "\n%{http_code}" "$url" 2>/dev/null)
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" = "200" ] || [ "$http_code" = "302" ]; then
        if [ -n "$expected" ]; then
            if echo "$body" | grep -q "$expected"; then
                echo -e "${GREEN}✅ PASS${NC}"
                ((PASSED++))
            else
                echo -e "${RED}❌ FAIL${NC} (Response doesn't contain '$expected')"
                ((FAILED++))
            fi
        else
            echo -e "${GREEN}✅ PASS${NC}"
            ((PASSED++))
        fi
    else
        echo -e "${RED}❌ FAIL${NC} (HTTP $http_code)"
        ((FAILED++))
    fi
}

echo "Core Services:"
echo "----------------------------------------"
test_endpoint "Backend API - Health" "http://localhost:5001/api/todos" "success"
test_endpoint "Frontend" "http://localhost:3000" ""
test_endpoint "Demo Server" "http://localhost:8080" ""
test_endpoint "Demo HTML" "http://localhost:8080/live-demo.html" "Python Full Stack"

echo ""
echo "API Endpoints:"
echo "----------------------------------------"
test_endpoint "Todo - GET All" "http://localhost:5001/api/todos" "todos"
test_endpoint "Calculator - Add" "http://localhost:5001/api/calculator/add?a=5&b=3" "result"

echo ""
echo "Database Services:"
echo "----------------------------------------"

# Test PostgreSQL
echo -n "Testing PostgreSQL... "
if docker exec fullstack-postgres pg_isready -U postgres > /dev/null 2>&1; then
    echo -e "${GREEN}✅ PASS${NC}"
    ((PASSED++))
else
    echo -e "${RED}❌ FAIL${NC}"
    ((FAILED++))
fi

# Test Redis
echo -n "Testing Redis... "
if docker exec fullstack-redis redis-cli ping | grep -q PONG; then
    echo -e "${GREEN}✅ PASS${NC}"
    ((PASSED++))
else
    echo -e "${RED}❌ FAIL${NC}"
    ((FAILED++))
fi

# Test MongoDB
echo -n "Testing MongoDB... "
if docker exec fullstack-mongo mongosh --eval "db.adminCommand('ping')" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ PASS${NC}"
    ((PASSED++))
else
    echo -e "${RED}❌ FAIL${NC}"
    ((FAILED++))
fi

echo ""
echo "Container Health:"
echo "----------------------------------------"

# Check all containers
containers=("python-fullstack-backend" "python-fullstack-frontend" "python-fullstack-demos" "fullstack-postgres" "fullstack-redis" "fullstack-mongo")

for container in "${containers[@]}"; do
    echo -n "Checking $container... "
    if docker ps | grep -q "$container"; then
        status=$(docker inspect --format='{{.State.Health.Status}}' "$container" 2>/dev/null || echo "running")
        if [ "$status" = "healthy" ] || [ "$status" = "running" ]; then
            echo -e "${GREEN}✅ Running${NC}"
            ((PASSED++))
        else
            echo -e "${YELLOW}⚠️  Running but unhealthy${NC}"
            ((PASSED++))
        fi
    else
        echo -e "${RED}❌ Not Running${NC}"
        ((FAILED++))
    fi
done

echo ""
echo "=========================================="
echo "📊 Test Summary"
echo "=========================================="
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 All tests passed!${NC}"
    echo ""
    echo "✅ You can now use the demos at:"
    echo "   http://localhost:8080/live-demo.html"
    exit 0
else
    echo -e "${RED}❌ Some tests failed${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "  1. Check logs: docker-compose logs [service-name]"
    echo "  2. Restart: docker-compose restart"
    echo "  3. Rebuild: docker-compose up -d --build"
    exit 1
fi
