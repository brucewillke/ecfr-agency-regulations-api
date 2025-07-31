#!/bin/bash
# Startup script for eCFR API

echo "🚀 Starting eCFR Agency Regulations API..."
echo "=================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv/installed" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    touch venv/installed
fi

echo "🌐 Starting API server on http://localhost:8000"
echo "📚 Interactive docs available at http://localhost:8000/docs"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start the API server
python main.py
