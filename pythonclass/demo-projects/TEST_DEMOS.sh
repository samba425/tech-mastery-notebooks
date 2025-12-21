#!/bin/bash

echo "=========================================="
echo "🧪 Testing All 17 Live Demos"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

passed=0
failed=0

test_demo() {
    local demo_name=$1
    local test_command=$2
    local expected=$3
    
    echo -n "Testing $demo_name... "
    
    result=$(eval "$test_command" 2>&1)
    
    if echo "$result" | grep -q "$expected"; then
        echo -e "${GREEN}✅ PASS${NC}"
        ((passed++))
    else
        echo -e "${RED}❌ FAIL${NC}"
        echo "  Expected: $expected"
        echo "  Got: $(echo $result | head -c 100)..."
        ((failed++))
    fi
}

echo "Part 1: Fundamentals"
echo "----------------------------------------"
test_demo "Calculator (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Simple Calculator'" "1"
test_demo "Grade Calculator (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Grade Calculator'" "1"
test_demo "Advanced Calculator API" "curl -s -X POST http://localhost:5001/api/calculator/advanced -H 'Content-Type: application/json' -d '{\"expression\": \"2+2\"}' | grep -c 'result'" "1"
test_demo "Todo API - GET" "curl -s http://localhost:5001/api/todos | grep -c 'success'" "1"
test_demo "Todo API - POST" "curl -s -X POST http://localhost:5001/api/todos -H 'Content-Type: application/json' -d '{\"title\": \"Test\", \"description\": \"Test\"}' | grep -c 'success'" "1"

echo ""
echo "Part 2: Backend"
echo "----------------------------------------"
test_demo "Contact Manager (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Contact Manager'" "1"
test_demo "Student System (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Student System'" "1"
test_demo "Blog OOP (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Blog System'" "1"
test_demo "Library System (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Library System'" "1"
test_demo "Flask API Demo" "curl -s http://localhost:5001/api | grep -c 'endpoints'" "1"
test_demo "Auth System (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Auth System'" "1"

echo ""
echo "Part 3: Frontend"
echo "----------------------------------------"
test_demo "React Todo (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'React Todo'" "1"
test_demo "Weather App (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Weather'" "1"
test_demo "Full Stack Blog (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Full Stack Blog'" "1"

echo ""
echo "Part 4: Advanced"
echo "----------------------------------------"
test_demo "Microservices Info" "curl -s http://localhost:8080/live-demo.html | grep -c 'Microservices'" "1"
test_demo "Async Scraper (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Async Scraper'" "1"
test_demo "GraphQL Demo (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'GraphQL'" "1"
test_demo "Chat App (Frontend)" "curl -s http://localhost:8080/live-demo.html | grep -c 'Chat App'" "1"

echo ""
echo "=========================================="
echo "📊 Test Summary"
echo "=========================================="
echo -e "${GREEN}Passed: $passed${NC}"
echo -e "${RED}Failed: $failed${NC}"
echo ""

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}✅ All demos accessible!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some demos need attention${NC}"
    exit 1
fi
