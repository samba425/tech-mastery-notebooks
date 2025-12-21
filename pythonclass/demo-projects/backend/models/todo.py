"""
Todo Model - Database model for todo items
"""

from app import db
from datetime import datetime

class Todo(db.Model):
    """Todo model for task management"""
    
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Todo {self.id}: {self.task}>'
    
    def to_dict(self):
        """Convert todo to dictionary"""
        return {
            'id': self.id,
            'task': self.task,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def create(cls, task, priority='medium'):
        """Create new todo"""
        todo = cls(task=task, priority=priority)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    def update(self, **kwargs):
        """Update todo attributes"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        """Delete todo"""
        db.session.delete(self)
        db.session.commit()
    
    def toggle_complete(self):
        """Toggle completion status"""
        self.completed = not self.completed
        self.updated_at = datetime.utcnow()
        db.session.commit()
