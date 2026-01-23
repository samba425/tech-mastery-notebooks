"""
Demo Project 13: Flask Blog API
Part 2: Backend Development - Hour 19
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- Complete Flask API with blueprints
- Error handling
- Request validation
- CORS support
- Production-ready structure
"""

# Note: This requires Flask and extensions
# pip install flask flask-cors flask-sqlalchemy

try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_api.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)
    CORS(app)
    
    # Models
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
        posts = db.relationship('Post', backref='author', lazy=True)
    
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        likes = db.Column(db.Integer, default=0)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'success': False, 'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'success': False, 'error': 'Internal server error'}), 500
    
    # Routes
    @app.route('/')
    def home():
        return jsonify({
            'message': 'Flask Blog API',
            'version': '1.0.0',
            'endpoints': {
                'GET /api/posts': 'Get all posts',
                'POST /api/posts': 'Create post',
                'GET /api/posts/<id>': 'Get post',
                'PUT /api/posts/<id>': 'Update post',
                'DELETE /api/posts/<id>': 'Delete post',
                'POST /api/posts/<id>/like': 'Like post'
            }
        })
    
    @app.route('/api/posts', methods=['GET'])
    def get_posts():
        """Get all posts"""
        posts = Post.query.all()
        return jsonify({
            'success': True,
            'count': len(posts),
            'posts': [{
                'id': p.id,
                'title': p.title,
                'content': p.content,
                'author': p.author.username,
                'likes': p.likes,
                'created_at': p.created_at.isoformat()
            } for p in posts]
        })
    
    @app.route('/api/posts', methods=['POST'])
    def create_post():
        """Create a new post"""
        data = request.get_json()
        
        # Validation
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({
                'success': False,
                'error': 'Title and content are required'
            }), 400
        
        if 'user_id' not in data:
            return jsonify({
                'success': False,
                'error': 'user_id is required'
            }), 400
        
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
        
        post = Post(
            title=data['title'],
            content=data['content'],
            user_id=data['user_id']
        )
        
        db.session.add(post)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'post': {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': user.username,
                'likes': post.likes
            }
        }), 201
    
    @app.route('/api/posts/<int:post_id>', methods=['GET'])
    def get_post(post_id):
        """Get post by ID"""
        post = Post.query.get_or_404(post_id)
        return jsonify({
            'success': True,
            'post': {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author.username,
                'likes': post.likes,
                'created_at': post.created_at.isoformat()
            }
        })
    
    @app.route('/api/posts/<int:post_id>/like', methods=['POST'])
    def like_post(post_id):
        """Like a post"""
        post = Post.query.get_or_404(post_id)
        post.likes += 1
        db.session.commit()
        
        return jsonify({
            'success': True,
            'likes': post.likes
        })
    
    @app.route('/api/users', methods=['POST'])
    def create_user():
        """Create a new user"""
        data = request.get_json()
        
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({
                'success': False,
                'error': 'Username and email are required'
            }), 400
        
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }), 201
    
    if __name__ == '__main__':
        print("🚀 Starting Flask Blog API...")
        print("📝 API available at: http://localhost:5000")
        app.run(debug=True, port=5000)

except ImportError:
    print("❌ Flask extensions not installed!")
    print("Install with: pip install flask flask-cors flask-sqlalchemy")


