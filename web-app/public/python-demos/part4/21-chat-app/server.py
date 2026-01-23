"""
Real-time Chat Application - Backend Server
Part 4: Advanced Topics - Hour 37
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- WebSocket connections
- Real-time messaging
- Multiple chat rooms
- User presence
- Message history
"""

# Note: Requires Flask-SocketIO
# pip install flask flask-socketio flask-cors

try:
    from flask import Flask, request, send_file
    from flask_socketio import SocketIO, emit, join_room, leave_room
    from flask_cors import CORS
    from datetime import datetime
    from collections import defaultdict
    import os

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    CORS(app, resources={r"/*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
    
    print("=" * 60)
    print("🎯 Socket.IO initialized with logging enabled")
    print("=" * 60)

    # In-memory storage
    users = {}  # {sid: username}
    rooms = defaultdict(list)  # {room_name: [messages]}
    user_rooms = defaultdict(set)  # {username: {room1, room2}}

    @app.route('/')
    def index():
        """Serve the chat client interface"""
        try:
            with open('client.html', 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/html'}
        except Exception as e:
            print(f"Error serving client.html: {e}")
            return {
                'message': 'Chat Server API',
                'status': 'running',
                'error': str(e),
                'client': 'Access client at /client.html',
                'endpoints': {
                    'GET /rooms': 'Get all rooms',
                    'GET /rooms/<room>/messages': 'Get room messages',
                    'GET /users': 'Get online users'
                }
            }

    @app.route('/client.html')
    def client():
        """Serve the chat client HTML file"""
        try:
            with open('client.html', 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/html'}
        except Exception as e:
            return {'error': str(e), 'message': 'Could not load client.html'}, 500

    @app.route('/rooms')
    def get_rooms():
        """Get all available rooms"""
        return {'rooms': list(rooms.keys())}

    @app.route('/rooms/<room>/messages')
    def get_messages(room):
        """Get messages for a room"""
        return {'room': room, 'messages': rooms.get(room, [])}

    @app.route('/users')
    def get_users():
        """Get online users"""
        return {'users': list(set(users.values()))}

    @socketio.on('connect')
    def handle_connect():
        """Handle client connection"""
        print(f'✅ Client connected: {request.sid}')
        emit('connected', {'message': 'Connected to chat server'})

    @socketio.on('disconnect')
    def handle_disconnect():
        """Handle client disconnection"""
        username = users.get(request.sid)
        print(f'❌ Client disconnecting: {request.sid}, username: {username}')
        if username:
            # Leave all rooms
            for room in user_rooms.get(username, set()):
                leave_room(room)
                emit('user_left', {'username': username}, room=room, broadcast=True)
            
            # Remove user
            del users[request.sid]
            if username in user_rooms:
                del user_rooms[username]
            
            print(f'User {username} disconnected')

    @socketio.on('join')
    def handle_join(data):
        """Handle user joining"""
        print(f'🔵 JOIN EVENT RECEIVED! Data: {data}, SID: {request.sid}')
        
        username = data.get('username')
        room = data.get('room', 'general')
        
        print(f'📝 Username: {username}, Room: {room}')
        
        if not username:
            print('❌ Username missing!')
            emit('error', {'message': 'Username is required'})
            return
        
        # Store user
        users[request.sid] = username
        print(f'✅ User stored: {username} -> {request.sid}')
        
        # Join room
        join_room(room)
        user_rooms[username].add(room)
        print(f'✅ User joined room: {room}')
        
        # Notify others
        emit('user_joined', {
            'username': username,
            'room': room,
            'timestamp': datetime.now().isoformat()
        }, room=room, broadcast=True, include_self=False)
        print(f'📢 Broadcast user_joined event')
        
        # Send room history
        if room in rooms:
            emit('room_history', {'messages': rooms[room][-50:]})  # Last 50 messages
            print(f'📜 Sent room history')
        
        print(f'✅ {username} joined room: {room}')

    @socketio.on('leave')
    def handle_leave(data):
        """Handle user leaving room"""
        username = users.get(request.sid)
        room = data.get('room', 'general')
        
        if username:
            leave_room(room)
            user_rooms[username].discard(room)
            
            emit('user_left', {
                'username': username,
                'room': room,
                'timestamp': datetime.now().isoformat()
            }, room=room, broadcast=True)
            
            print(f'{username} left room: {room}')

    @socketio.on('message')
    def handle_message(data):
        """Handle incoming message"""
        print(f'💬 MESSAGE EVENT RECEIVED! Data: {data}, SID: {request.sid}')
        
        username = users.get(request.sid)
        room = data.get('room', 'general')
        message_text = data.get('message', '')
        
        print(f'📝 Username: {username}, Room: {room}, Message: {message_text}')
        
        if not username:
            print('❌ User not found!')
            emit('error', {'message': 'You must join first'})
            return
        
        if not message_text:
            print('❌ Empty message!')
            emit('error', {'message': 'Message cannot be empty'})
            return
        
        # Create message object
        message = {
            'username': username,
            'message': message_text,
            'room': room,
            'timestamp': datetime.now().isoformat()
        }
        
        # Store message
        rooms[room].append(message)
        print(f'💾 Message stored in room {room}')
        
        # Keep only last 100 messages per room
        if len(rooms[room]) > 100:
            rooms[room] = rooms[room][-100:]
        
        # Broadcast to room
        emit('message', message, room=room, broadcast=True)
        print(f'📢 Broadcasting message to room {room}')
        
        print(f'✅ {username} in {room}: {message_text}')

    @socketio.on('typing')
    def handle_typing(data):
        """Handle typing indicator"""
        username = users.get(request.sid)
        room = data.get('room', 'general')
        is_typing = data.get('typing', False)
        
        if username:
            emit('typing', {
                'username': username,
                'typing': is_typing,
                'room': room
            }, room=room, broadcast=True, include_self=False)

    if __name__ == '__main__':
        print("🚀 Starting Chat Server on http://localhost:5000")
        print("📝 WebSocket endpoint: ws://localhost:5000")
        print("\nTo test:")
        print("1. Open multiple browser windows")
        print("2. Connect to ws://localhost:5000")
        print("3. Join a room and start chatting!")
        # Disable reloader because it causes event handlers to not be registered
        socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)

except ImportError:
    print("❌ Flask-SocketIO not installed!")
    print("Install with: pip install flask flask-socketio flask-cors")
    print("\nTo run the chat server:")
    print("1. Install: pip install flask flask-socketio flask-cors")
    print("2. Run: python server.py")
    print("3. Server will start on http://localhost:5000")


