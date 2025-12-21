# Real-time Chat Application

## Overview
WebSocket-based real-time chat application with multiple rooms and user presence.

## Features
- WebSocket connections
- Real-time messaging
- Multiple chat rooms
- User presence
- Typing indicators
- Message history

## Setup

### Backend (Flask-SocketIO)
```bash
pip install flask flask-socketio flask-cors
python server.py
```

### Frontend
```bash
npm install socket.io-client react
npm start
```

## Project Structure
```
21-chat-app/
├── backend/
│   └── server.py
└── frontend/
    ├── src/
    │   ├── App.js
    │   └── components/
    └── package.json
```

## Usage
1. Start backend: `python backend/server.py` (port 5000)
2. Start frontend: `npm start` (port 3000)
3. Open multiple browser windows to test real-time chat

## Features Demo
- Join different rooms
- Send messages in real-time
- See typing indicators
- View user list
- Message history

## Quick Start

### Backend
```bash
pip install flask flask-socketio flask-cors
python server.py
```

### Frontend (HTML Client)
1. Open `client.html` in your browser
2. Enter username and room name
3. Start chatting!

## Testing

### Test with Multiple Clients
1. Start server: `python server.py`
2. Open `client.html` in multiple browser windows
3. Join the same room
4. Send messages and see real-time updates

### API Endpoints
```bash
# Get all rooms
curl http://localhost:5000/rooms

# Get room messages
curl http://localhost:5000/rooms/general/messages

# Get online users
curl http://localhost:5000/users
```

## Files
- `server.py` - Flask-SocketIO backend server
- `client.html` - HTML/JavaScript client (no React needed!)

## Features Demonstrated
- ✅ WebSocket connections
- ✅ Real-time messaging
- ✅ Multiple chat rooms
- ✅ User presence (join/leave notifications)
- ✅ Typing indicators
- ✅ Message history

## Note
This is a simplified demo. Full implementation requires Socket.IO setup and React frontend.

