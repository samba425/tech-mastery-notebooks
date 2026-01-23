"""
Demo Project 12: Flask Basic API
Part 2: Backend Development - Hour 18
Difficulty: ⭐⭐⭐ Advanced

Features:
- RESTful API with Flask
- Routes and HTTP methods
- Request handling
- JSON responses
- Error handling
"""

# Note: This requires Flask to be installed
# pip install flask flask-cors

try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
    
    app = Flask(__name__)
    CORS(app)
    
    # In-memory data store
    todos = []
    next_id = 1
    
    @app.route('/')
    def home():
        """Home endpoint"""
        return jsonify({
            'message': 'Flask Basic API Demo',
            'endpoints': {
                'GET /api/todos': 'Get all todos',
                'POST /api/todos': 'Create todo',
                'GET /api/todos/<id>': 'Get todo by ID',
                'PUT /api/todos/<id>': 'Update todo',
                'DELETE /api/todos/<id>': 'Delete todo'
            }
        })
    
    @app.route('/api/todos', methods=['GET'])
    def get_todos():
        """Get all todos"""
        return jsonify({
            'success': True,
            'count': len(todos),
            'todos': todos
        })
    
    @app.route('/api/todos', methods=['POST'])
    def create_todo():
        """Create a new todo"""
        global next_id
        
        data = request.get_json()
        
        if not data or 'task' not in data:
            return jsonify({
                'success': False,
                'error': 'Task is required'
            }), 400
        
        todo = {
            'id': next_id,
            'task': data['task'],
            'completed': False,
            'priority': data.get('priority', 'medium')
        }
        
        todos.append(todo)
        next_id += 1
        
        return jsonify({
            'success': True,
            'todo': todo
        }), 201
    
    @app.route('/api/todos/<int:todo_id>', methods=['GET'])
    def get_todo(todo_id):
        """Get todo by ID"""
        todo = next((t for t in todos if t['id'] == todo_id), None)
        
        if not todo:
            return jsonify({
                'success': False,
                'error': 'Todo not found'
            }), 404
        
        return jsonify({
            'success': True,
            'todo': todo
        })
    
    @app.route('/api/todos/<int:todo_id>', methods=['PUT'])
    def update_todo(todo_id):
        """Update todo"""
        todo = next((t for t in todos if t['id'] == todo_id), None)
        
        if not todo:
            return jsonify({
                'success': False,
                'error': 'Todo not found'
            }), 404
        
        data = request.get_json()
        if 'task' in data:
            todo['task'] = data['task']
        if 'completed' in data:
            todo['completed'] = data['completed']
        if 'priority' in data:
            todo['priority'] = data['priority']
        
        return jsonify({
            'success': True,
            'todo': todo
        })
    
    @app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        """Delete todo"""
        global todos
        todo = next((t for t in todos if t['id'] == todo_id), None)
        
        if not todo:
            return jsonify({
                'success': False,
                'error': 'Todo not found'
            }), 404
        
        todos = [t for t in todos if t['id'] != todo_id]
        
        return jsonify({
            'success': True,
            'message': 'Todo deleted'
        })
    
    @app.route('/health', methods=['GET'])
    def health():
        """Health check"""
        return jsonify({
            'status': 'healthy',
            'todos_count': len(todos)
        })
    
    if __name__ == '__main__':
        print("🚀 Starting Flask API server...")
        print("📝 API available at: http://localhost:5000")
        print("📚 API docs at: http://localhost:5000/")
        app.run(debug=True, port=5000)

except ImportError:
    print("❌ Flask not installed!")
    print("Install it with: pip install flask flask-cors")
    print("\nTo run this API:")
    print("1. Install Flask: pip install flask flask-cors")
    print("2. Run: python 12-flask-basic-api.py")
    print("3. Test with: curl http://localhost:5000/api/todos")


