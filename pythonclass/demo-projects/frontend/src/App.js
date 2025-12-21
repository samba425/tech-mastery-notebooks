import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5001';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState({ task: '', priority: 'medium' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Fetch todos on component mount
  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_URL}/api/todos`);
      const data = await response.json();
      if (data.success) {
        setTodos(data.todos);
      }
    } catch (err) {
      setError('Failed to fetch todos: ' + err.message);
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const addTodo = async (e) => {
    e.preventDefault();
    if (!newTodo.task.trim()) {
      alert('Please enter a todo task');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_URL}/api/todos`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newTodo),
      });
      const data = await response.json();
      if (data.success) {
        setTodos([...todos, data.todo]);
        setNewTodo({ task: '', priority: 'medium' });
      } else {
        setError(data.error || 'Failed to add todo');
      }
    } catch (err) {
      setError('Failed to add todo: ' + err.message);
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const toggleTodo = async (id) => {
    const todo = todos.find(t => t.id === id);
    if (!todo) return;

    try {
      const response = await fetch(`${API_URL}/api/todos/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ...todo, completed: !todo.completed }),
      });
      const data = await response.json();
      if (data.success) {
        setTodos(todos.map(t => t.id === id ? data.todo : t));
      }
    } catch (err) {
      setError('Failed to update todo: ' + err.message);
      console.error('Error:', err);
    }
  };

  const deleteTodo = async (id) => {
    if (!window.confirm('Are you sure you want to delete this todo?')) return;

    try {
      const response = await fetch(`${API_URL}/api/todos/${id}`, {
        method: 'DELETE',
      });
      const data = await response.json();
      if (data.success) {
        setTodos(todos.filter(t => t.id !== id));
      }
    } catch (err) {
      setError('Failed to delete todo: ' + err.message);
      console.error('Error:', err);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>⚛️ React Todo List</h1>
        <p>Full Stack Demo with React + Flask</p>
      </header>

      <div className="container">
        {error && (
          <div className="error">
            ❌ {error}
          </div>
        )}

        <div className="demo-content">
          <h2>Add New Todo</h2>
          <form onSubmit={addTodo} className="todo-form">
            <input
              type="text"
              placeholder="Enter todo task..."
              value={newTodo.task}
              onChange={(e) => setNewTodo({ ...newTodo, task: e.target.value })}
              disabled={loading}
            />
            <select
              value={newTodo.priority}
              onChange={(e) => setNewTodo({ ...newTodo, priority: e.target.value })}
              disabled={loading}
            >
              <option value="low">Low Priority</option>
              <option value="medium">Medium Priority</option>
              <option value="high">High Priority</option>
            </select>
            <button type="submit" disabled={loading}>
              {loading ? '⏳ Adding...' : '➕ Add Todo'}
            </button>
          </form>

          <div className="todos-section">
            <h2>My Todos ({todos.length})</h2>
            
            {loading && todos.length === 0 ? (
              <div className="loading">⏳ Loading todos...</div>
            ) : todos.length === 0 ? (
              <div className="empty-state">
                <p>📝 No todos yet. Add your first todo above!</p>
              </div>
            ) : (
              <div className="todos-list">
                {todos.map(todo => (
                  <div key={todo.id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
                    <div className="todo-checkbox">
                      <input
                        type="checkbox"
                        checked={todo.completed || false}
                        onChange={() => toggleTodo(todo.id)}
                      />
                    </div>
                    <div className="todo-content">
                      <h3>{todo.task}</h3>
                      <small>
                        {todo.completed ? '✅ Completed' : '⏳ Pending'}
                        {todo.priority && ` • Priority: ${todo.priority}`}
                      </small>
                    </div>
                    <div className="todo-actions">
                      <button 
                        onClick={() => deleteTodo(todo.id)}
                        className="delete-btn"
                        title="Delete"
                      >
                        🗑️
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="info-section">
            <h3>ℹ️ About This Demo</h3>
            <ul>
              <li>✅ React frontend with hooks (useState, useEffect)</li>
              <li>✅ Full CRUD operations (Create, Read, Update, Delete)</li>
              <li>✅ API integration with Flask backend</li>
              <li>✅ Real-time updates</li>
              <li>✅ Responsive design</li>
            </ul>
            <p>
              <strong>Backend API:</strong> <a href={`${API_URL}/api/todos`} target="_blank" rel="noopener noreferrer">
                {API_URL}/api/todos
              </a>
            </p>
            <p>
              <strong>More Demos:</strong> <a href="http://localhost:8080/live-demo.html" target="_blank" rel="noopener noreferrer">
                View All 17 Demos
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
