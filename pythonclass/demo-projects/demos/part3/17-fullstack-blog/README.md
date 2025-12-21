# Full Stack Blog Application

## Overview
Complete full-stack application with React frontend and Flask backend.

## Features
- React frontend
- Flask REST API backend
- Database integration
- User authentication
- CRUD operations

## Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Project Structure
```
17-fullstack-blog/
├── backend/
│   ├── app.py
│   ├── models/
│   └── routes/
└── frontend/
    ├── src/
    └── package.json
```

## Usage
1. Start backend: `python backend/app.py` (port 5000)
2. Start frontend: `npm start` (port 3000)
3. Open http://localhost:3000

## Note
This is a simplified demo. For full implementation, see the main demo-projects directory.


