"""
Flask Application Runner
Run this file to start the backend server
"""

from app import create_app, db
import os

# Create Flask application
app = create_app()

# Create database tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully")

if __name__ == '__main__':
    # Detect if running in Docker
    is_docker = os.path.exists('/.dockerenv')
    port = 5000 if is_docker else 5001
    
    print("=" * 50)
    print("🚀 Python Full Stack Demo - Backend Server")
    print("=" * 50)
    print(f"📍 Server running on: http://localhost:{port}")
    print(f"📊 API endpoints available at: http://localhost:{port}/api/")
    print("🔧 CORS enabled for all origins")
    if not is_docker:
        print("💡 Note: Using port 5001 (5000 is used by macOS AirPlay)")
    print("=" * 50)
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        use_reloader=True
    )
