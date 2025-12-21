"""
Todo Route - Handles all todo-related operations
CRUD operations for todo list management
"""

from flask import Blueprint, request, jsonify
from app import db
from models.todo import Todo
from datetime import datetime

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/', methods=['GET'])
def get_all_todos():
    """
    Get all todos
    GET /api/todos
    Query params: ?status=completed&priority=high
    """
    try:
        status = request.args.get('status')
        priority = request.args.get('priority')
        
        query = Todo.query
        
        if status:
            completed = (status.lower() == 'completed')
            query = query.filter_by(completed=completed)
        
        if priority:
            query = query.filter_by(priority=priority)
        
        todos = query.order_by(Todo.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'todos': [todo.to_dict() for todo in todos],
            'count': len(todos)
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/', methods=['POST'])
def create_todo():
    """
    Create new todo
    POST /api/todos
    Body: {
        "task": "Learn Python",
        "priority": "high"  # low, medium, high
    }
    """
    try:
        data = request.get_json()
        
        if not data.get('task'):
            return jsonify({'success': False, 'error': 'Task is required'}), 400
        
        todo = Todo(
            task=data['task'],
            priority=data.get('priority', 'medium'),
            completed=False
        )
        
        db.session.add(todo)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Todo created successfully',
            'todo': todo.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get specific todo by ID"""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'success': False, 'error': 'Todo not found'}), 404
        
        return jsonify({
            'success': True,
            'todo': todo.to_dict()
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update todo
    PUT /api/todos/<id>
    Body: {
        "task": "Updated task",
        "priority": "low",
        "completed": true
    }
    """
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'success': False, 'error': 'Todo not found'}), 404
        
        data = request.get_json()
        
        if 'task' in data:
            todo.task = data['task']
        if 'priority' in data:
            todo.priority = data['priority']
        if 'completed' in data:
            todo.completed = data['completed']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Todo updated successfully',
            'todo': todo.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete todo"""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'success': False, 'error': 'Todo not found'}), 404
        
        db.session.delete(todo)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Todo deleted successfully'
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/<int:todo_id>/toggle', methods=['PATCH'])
def toggle_todo(todo_id):
    """Toggle todo completion status"""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'success': False, 'error': 'Todo not found'}), 404
        
        todo.completed = not todo.completed
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Todo status toggled',
            'todo': todo.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get todo statistics"""
    try:
        total = Todo.query.count()
        completed = Todo.query.filter_by(completed=True).count()
        pending = total - completed
        
        high_priority = Todo.query.filter_by(priority='high', completed=False).count()
        
        return jsonify({
            'success': True,
            'stats': {
                'total': total,
                'completed': completed,
                'pending': pending,
                'high_priority': high_priority,
                'completion_rate': round((completed / total * 100) if total > 0 else 0, 1)
            }
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@todo_bp.route('/clear-completed', methods=['DELETE'])
def clear_completed():
    """Delete all completed todos"""
    try:
        Todo.query.filter_by(completed=True).delete()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Completed todos cleared'
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
