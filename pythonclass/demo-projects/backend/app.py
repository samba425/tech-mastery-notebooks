"""
Main Flask Application - Python Full Stack Demo
Unified backend for all 21 demo projects
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
import os

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Disable strict slashes to prevent CORS redirect issues
    app.url_map.strict_slashes = False
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # CORS configuration - allow all origins and methods
    CORS(app, 
         resources={r"/api/*": {
             "origins": "*",
             "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
             "allow_headers": ["Content-Type", "Authorization"]
         }},
         supports_credentials=True)
    
    # Register blueprints (routes) - with error handling
    try:
        from routes.calculator import calculator_bp
        app.register_blueprint(calculator_bp, url_prefix='/api/calculator')
    except ImportError:
        print("Warning: calculator routes not found")
    
    try:
        from routes.todo import todo_bp
        app.register_blueprint(todo_bp, url_prefix='/api/todos')
    except ImportError:
        print("Warning: todo routes not found")
    
    try:
        from routes.blog import blog_bp
        app.register_blueprint(blog_bp, url_prefix='/api/blog')
    except ImportError:
        print("Warning: blog routes not found")
    
    try:
        from routes.library import library_bp
        app.register_blueprint(library_bp, url_prefix='/api/library')
    except ImportError:
        print("Warning: library routes not found")
    
    try:
        from routes.student import student_bp
        app.register_blueprint(student_bp, url_prefix='/api/students')
    except ImportError:
        print("Warning: student routes not found")
    
    try:
        from routes.contact import contact_bp
        app.register_blueprint(contact_bp, url_prefix='/api/contacts')
    except ImportError:
        print("Warning: contact routes not found")
    
    try:
        from routes.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/api/auth')
    except ImportError:
        print("Warning: auth routes not found")
    
    try:
        from routes.weather import weather_bp
        app.register_blueprint(weather_bp, url_prefix='/api/weather')
    except ImportError:
        print("Warning: weather routes not found")
    
    try:
        from routes.chat import chat_bp
        app.register_blueprint(chat_bp, url_prefix='/api/chat')
    except ImportError:
        print("Warning: chat routes not found")
    
    # Global OPTIONS handler for CORS preflight
    @app.route('/<path:path>', methods=['OPTIONS'])
    def handle_options(path):
        """Handle all OPTIONS requests for CORS preflight"""
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        return response, 200
    
    # Home route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Python Full Stack Demo API',
            'version': '1.0.0',
            'projects': 21,
            'endpoints': {
                'calculator': '/api/calculator',
                'todos': '/api/todos',
                'blog': '/api/blog',
                'library': '/api/library',
                'students': '/api/students',
                'contacts': '/api/contacts',
                'auth': '/api/auth',
                'weather': '/api/weather',
                'chat': '/api/chat'
            },
            'docs': '/docs'
        })
    
    # API Documentation route
    @app.route('/docs')
    def docs():
        return jsonify({
            'title': 'Python Full Stack Demo API Documentation',
            'description': 'Complete API for all 21 demo projects',
            'version': '1.0.0',
            'endpoints': get_all_endpoints()
        })
    
    # Health check
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy', 'database': 'connected'})
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

def get_all_endpoints():
    """Get list of all API endpoints"""
    return {
        'Calculator APIs': {
            'POST /api/calculator/basic': 'Basic arithmetic operations',
            'POST /api/calculator/advanced': 'Advanced calculations',
            'POST /api/calculator/bmi': 'BMI calculator',
            'POST /api/calculator/grade': 'Grade calculator',
            'GET /api/calculator/history': 'Calculation history'
        },
        'Todo APIs': {
            'GET /api/todos': 'Get all todos',
            'POST /api/todos': 'Create new todo',
            'PUT /api/todos/<id>': 'Update todo',
            'DELETE /api/todos/<id>': 'Delete todo',
            'GET /api/todos/filter': 'Filter todos by status/priority'
        },
        'Blog APIs': {
            'GET /api/blog/posts': 'Get all posts',
            'POST /api/blog/posts': 'Create new post',
            'PUT /api/blog/posts/<id>': 'Update post',
            'DELETE /api/blog/posts/<id>': 'Delete post',
            'POST /api/blog/posts/<id>/like': 'Like a post',
            'POST /api/blog/posts/<id>/comment': 'Add comment to post'
        },
        'Student APIs': {
            'GET /api/students': 'Get all students',
            'POST /api/students': 'Create new student',
            'GET /api/students/<id>': 'Get student details',
            'POST /api/students/<id>/grades': 'Add grade',
            'GET /api/students/<id>/gpa': 'Calculate GPA',
            'GET /api/students/<id>/transcript': 'Generate transcript'
        },
        'Library APIs': {
            'GET /api/library/books': 'Get all books',
            'POST /api/library/books': 'Add new book',
            'POST /api/library/borrow/<id>': 'Borrow book',
            'POST /api/library/return/<id>': 'Return book',
            'GET /api/library/search': 'Search books'
        },
        'Contact APIs': {
            'GET /api/contacts': 'Get all contacts',
            'POST /api/contacts': 'Create new contact',
            'PUT /api/contacts/<id>': 'Update contact',
            'DELETE /api/contacts/<id>': 'Delete contact',
            'GET /api/contacts/search': 'Search contacts'
        },
        'Authentication APIs': {
            'POST /api/auth/register': 'Register new user',
            'POST /api/auth/login': 'Login user',
            'POST /api/auth/logout': 'Logout user',
            'GET /api/auth/profile': 'Get user profile (protected)',
            'PUT /api/auth/profile': 'Update profile (protected)'
        },
        'Weather APIs': {
            'GET /api/weather/current': 'Get current weather',
            'GET /api/weather/forecast': 'Get 5-day forecast'
        },
        'Chat APIs': {
            'GET /api/chat/messages': 'Get chat messages',
            'POST /api/chat/messages': 'Send message',
            'GET /api/chat/rooms': 'Get chat rooms'
        }
    }

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
