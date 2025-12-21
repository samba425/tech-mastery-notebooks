#!/bin/bash

# Flask Backend Startup Script
# This script sets up and runs the Flask backend server

echo "=================================="
echo "🚀 Starting Flask Backend Server"
echo "=================================="

# Navigate to backend directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Set Flask environment variables
export FLASK_APP=run.py
export FLASK_ENV=development

# Create instance folder if it doesn't exist
mkdir -p instance

echo ""
echo "✅ Setup complete!"
echo "=================================="
echo "📍 Server will run on: http://localhost:5000"
echo "📊 API Base URL: http://localhost:5000/api/"
echo "🌐 CORS: Enabled for all origins"
echo "=================================="
echo ""
echo "Starting server..."
echo ""

# Run Flask application
python run.py
