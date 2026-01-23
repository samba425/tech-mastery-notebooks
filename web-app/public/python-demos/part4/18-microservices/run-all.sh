#!/bin/bash

# Script to run all microservices locally (without Docker)

echo "🚀 Starting Microservices Demo"
echo "================================"
echo ""

# Check if required packages are installed
echo "Checking dependencies..."
python3 -c "import fastapi, uvicorn, httpx" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies. Installing..."
    pip install fastapi uvicorn httpx
fi

echo ""
echo "Starting services..."
echo ""

# Start User Service in background
echo "📦 Starting User Service on port 8001..."
python3 user-service.py > user-service.log 2>&1 &
USER_PID=$!
sleep 2

# Start Post Service in background
echo "📦 Starting Post Service on port 8002..."
python3 post-service.py > post-service.log 2>&1 &
POST_PID=$!
sleep 2

# Start API Gateway
echo "🌐 Starting API Gateway on port 8000..."
echo ""
echo "✅ All services started!"
echo ""
echo "Access points:"
echo "  - API Gateway: http://localhost:8000"
echo "  - User Service: http://localhost:8001"
echo "  - Post Service: http://localhost:8002"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for interrupt
trap "kill $USER_PID $POST_PID; echo ''; echo 'Stopped all services'; exit" INT TERM

# Keep script running
wait


