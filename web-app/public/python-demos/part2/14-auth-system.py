"""
Demo Project 14: Authentication System
Part 2: Backend Development - Hour 20
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- JWT authentication
- Password hashing with bcrypt
- Protected routes
- Role-based access control
- User registration and login
"""

# Note: This requires Flask and JWT extensions
# pip install flask flask-jwt-extended flask-cors bcrypt

try:
    from flask import Flask, jsonify, request
    from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
    from flask_cors import CORS
    import bcrypt
    from datetime import timedelta
    
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    jwt = JWTManager(app)
    CORS(app)
    
    # In-memory user store (use database in production)
    users = {}
    
    def hash_password(password):
        """Hash password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify_password(password, hashed):
        """Verify password"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    
    @app.route('/')
    def home():
        return jsonify({
            'message': 'Authentication API',
            'endpoints': {
                'POST /api/auth/register': 'Register user',
                'POST /api/auth/login': 'Login user',
                'GET /api/auth/profile': 'Get profile (protected)',
                'GET /api/auth/protected': 'Protected route example'
            }
        })
    
    @app.route('/api/auth/register', methods=['POST'])
    def register():
        """Register a new user"""
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({
                'success': False,
                'error': 'Username and password are required'
            }), 400
        
        username = data['username']
        
        if username in users:
            return jsonify({
                'success': False,
                'error': 'Username already exists'
            }), 400
        
        # Hash password
        hashed_password = hash_password(data['password'])
        
        # Store user
        users[username] = {
            'username': username,
            'password': hashed_password,
            'email': data.get('email', ''),
            'role': data.get('role', 'user')
        }
        
        return jsonify({
            'success': True,
            'message': 'User registered successfully'
        }), 201
    
    @app.route('/api/auth/login', methods=['POST'])
    def login():
        """Login user"""
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({
                'success': False,
                'error': 'Username and password are required'
            }), 400
        
        username = data['username']
        password = data['password']
        
        if username not in users:
            return jsonify({
                'success': False,
                'error': 'Invalid credentials'
            }), 401
        
        user = users[username]
        
        if not verify_password(password, user['password']):
            return jsonify({
                'success': False,
                'error': 'Invalid credentials'
            }), 401
        
        # Create access token
        access_token = create_access_token(
            identity=username,
            additional_claims={'role': user['role']}
        )
        
        return jsonify({
            'success': True,
            'access_token': access_token,
            'user': {
                'username': username,
                'email': user['email'],
                'role': user['role']
            }
        })
    
    @app.route('/api/auth/profile', methods=['GET'])
    @jwt_required()
    def get_profile():
        """Get user profile (protected route)"""
        current_user = get_jwt_identity()
        
        if current_user not in users:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
        
        user = users[current_user]
        return jsonify({
            'success': True,
            'user': {
                'username': user['username'],
                'email': user['email'],
                'role': user['role']
            }
        })
    
    @app.route('/api/auth/protected', methods=['GET'])
    @jwt_required()
    def protected():
        """Example protected route"""
        current_user = get_jwt_identity()
        return jsonify({
            'success': True,
            'message': f'Hello {current_user}! This is a protected route.',
            'user': current_user
        })
    
    if __name__ == '__main__':
        print("🚀 Starting Authentication API...")
        print("📝 API available at: http://localhost:5000")
        print("\nExample usage:")
        print("1. Register: POST /api/auth/register")
        print("   Body: {'username': 'test', 'password': 'test123'}")
        print("2. Login: POST /api/auth/login")
        print("   Body: {'username': 'test', 'password': 'test123'}")
        print("3. Access protected: GET /api/auth/profile")
        print("   Header: Authorization: Bearer <token>")
        app.run(debug=True, port=5000)

except ImportError:
    print("❌ Required packages not installed!")
    print("Install with: pip install flask flask-jwt-extended flask-cors bcrypt")


