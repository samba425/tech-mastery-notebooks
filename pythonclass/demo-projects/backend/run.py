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
    # Detect environment
    is_docker = os.path.exists('/.dockerenv')
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    # Port selection (Render uses PORT env var)
    port = int(os.environ.get('PORT', 5000 if is_docker else 5001))
    
    print("=" * 50)
    print("🚀 Python Full Stack Demo - Backend Server")
    print("=" * 50)
    print(f"📍 Server running on: http://0.0.0.0:{port}")
    print(f"📊 API endpoints available at: http://localhost:{port}/api/")
    print(f"🌍 Environment: {'Production' if is_production else 'Development'}")
    print("🔧 CORS enabled for all origins")
    if not is_docker and not is_production:
        print("💡 Note: Using port 5001 (5000 is used by macOS AirPlay)")
    print("=" * 50)
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=not is_production,  # Disable debug in production
        use_reloader=not is_production  # Disable reloader in production
    )
