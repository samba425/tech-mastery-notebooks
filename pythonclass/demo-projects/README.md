# 🚀 Python Full-Stack Demo Projects# 🚀 Python Full Stack Demo Projects - Unified Application



**Complete 40-hour Python Full-Stack Development Training - All Projects in One Place**## Overview

This is a unified web application that showcases all 21 Python Full Stack projects in one interactive interface. Click through different projects and see live demos!

This repository contains 21+ working demo projects covering Python fundamentals, backend development, frontend with React, and advanced topics including microservices, async programming, GraphQL, and real-time chat.

## Features

---- ✅ Single page application with navigation

- ✅ All 21 projects accessible from one UI

## 📋 Table of Contents- ✅ Backend API supporting all features

- ✅ Responsive design

- [Quick Start](#-quick-start)- ✅ Dark/Light mode

- [Project Overview](#-project-overview)- ✅ Real-time updates

- [All Demo Projects](#-all-demo-projects)- ✅ Database integration

- [Architecture](#-architecture)

- [How to Use](#-how-to-use)## Project Structure

- [Testing & Verification](#-testing--verification)

- [API Documentation](#-api-documentation)```

- [Troubleshooting](#-troubleshooting)demo-projects/

├── backend/                    # Flask Backend API

---│   ├── app.py                 # Main application

│   ├── config.py              # Configuration

## 🎯 Quick Start│   ├── requirements.txt       # Dependencies

│   ├── routes/                # API Routes

### One-Command Setup (Recommended)│   │   ├── calculator.py      # Calculator APIs

│   │   ├── todo.py            # Todo APIs

**Start everything including microservices:**│   │   ├── blog.py            # Blog APIs

```bash│   │   ├── library.py         # Library APIs

docker-compose --profile microservices up -d│   │   ├── student.py         # Student APIs

```│   │   ├── contact.py         # Contact APIs

│   │   ├── auth.py            # Authentication APIs

**Start only main services (without microservices):**│   │   └── weather.py         # Weather APIs

```bash│   ├── models/                # Database Models

docker-compose up -d│   │   ├── user.py

```│   │   ├── post.py

│   │   ├── todo.py

**That's it!** All services will be running and accessible.│   │   ├── book.py

│   │   └── student.py

### Access Your Applications│   ├── services/              # Business Logic

│   │   ├── calculator_service.py

| Service | URL | Description |│   │   ├── grade_service.py

|---------|-----|-------------|│   │   └── scraper_service.py

| 🎨 **All Demos** | http://localhost:8080 | Interactive demo showcase with navigation |│   └── database/              # Database Files

| ⚛️ **React Todo App** | http://localhost:3000 | Full-featured React application |│       ├── init_db.py

| 🔧 **Backend API** | http://localhost:5001 | Flask REST API server |│       └── demo.db

| 🔌 **API Docs** | http://localhost:5001/api/todos | Todo API endpoint |├── frontend/                   # React Frontend

| 🗄️ **PostgreSQL** | localhost:5432 | Database server |│   ├── public/

| 🚀 **Redis** | localhost:6379 | Cache server |│   ├── src/

| 🍃 **MongoDB** | localhost:27017 | Document database |│   │   ├── App.js             # Main App

| 👤 **User Service** | http://localhost:8001 | Microservice (with profile) |│   │   ├── components/        # React Components

| 📝 **Post Service** | http://localhost:8002 | Microservice (with profile) |│   │   │   ├── Navbar.js

| 🌐 **API Gateway** | http://localhost:8000 | Microservice gateway (with profile) |│   │   │   ├── Sidebar.js

│   │   │   ├── Dashboard.js

---│   │   │   └── projects/      # Project Components

│   │   │       ├── Calculator.js

## 📚 Project Overview│   │   │       ├── GradeCalculator.js

│   │   │       ├── TodoList.js

This project is based on the **Python Teaching Plan (12 Days / 40 Hours)** covering:│   │   │       ├── BlogSystem.js

│   │   │       ├── LibrarySystem.js

### **Part 1: Python Fundamentals (Hours 1-10)**│   │   │       ├── StudentSystem.js

- Variables, Data Types, Control Flow│   │   │       ├── ContactManager.js

- Functions, Data Structures│   │   │       ├── WeatherApp.js

- Object-Oriented Programming│   │   │       └── ChatApp.js

- File Operations, Exception Handling│   │   ├── styles/

│   │   └── utils/

### **Part 2: Backend Development (Hours 11-20)**│   ├── package.json

- Flask Web Framework│   └── README.md

- REST API Development├── docker-compose.yml          # Docker setup

- Database Integration (SQLAlchemy, PostgreSQL)├── .env.example               # Environment variables

- Authentication & Authorization└── README.md                  # This file

```

### **Part 3: Frontend Development (Hours 21-30)**

- React Fundamentals## Quick Start

- Components, Props, State

- API Integration### Option 1: Using Docker (Recommended)

- Modern UI Development```bash

# Clone and navigate

### **Part 4: Advanced Backend (Hours 31-40)**cd demo-projects

- Microservices Architecture

- Async Programming# Start all services

- GraphQLdocker-compose up -d

- Real-time WebSockets

- Deployment & DevOps# Access application

# Frontend: http://localhost:3000

---# Backend API: http://localhost:5000

# API Docs: http://localhost:5000/docs

## 🎪 All Demo Projects```



### **Interactive Demo Page (Port 8080)**### Option 2: Manual Setup



Access all demos through a beautiful, unified interface at **http://localhost:8080**#### Backend Setup

```bash

#### **Part 1 & 2: Core Python & Backend (13 Demos)**cd backend



1. **🔢 Calculator API** - Basic arithmetic operations# Create virtual environment

   - `/api/calculator/basic` - Add, subtract, multiply, dividepython -m venv venv

   - `/api/calculator/grade` - Grade calculationsource venv/bin/activate  # On Windows: venv\Scripts\activate

   - `/api/calculator/advanced` - Power, sqrt, modulus

# Install dependencies

2. **✅ Todo List API** - Full CRUD operationspip install -r requirements.txt

   - `GET /api/todos` - List all todos

   - `POST /api/todos` - Create todo# Initialize database

   - `PUT /api/todos/<id>` - Update todopython database/init_db.py

   - `DELETE /api/todos/<id>` - Delete todo

# Run backend

3. **👨‍🎓 Student Management** - Student records systempython app.py

   - Add, view, update, delete students# Backend runs on http://localhost:5000

   - Grade management```



4. **📝 Blog System** - Article management#### Frontend Setup

   - Create, read, update, delete articles```bash

   - Author managementcd frontend



5. **📚 Library Management** - Book inventory# Install dependencies

   - Book catalognpm install

   - Borrowing system

# Start React app

6. **🔐 Authentication System** - User authnpm start

   - Registration# Frontend runs on http://localhost:3000

   - Login/Logout```

   - JWT tokens

## Environment Variables

7. **🌤️ Weather API** - Weather data

   - Current weatherCreate `.env` file in root:

   - Forecasts

   - Multiple cities```env

# Backend

8. **💳 E-commerce Cart** - Shopping functionalityFLASK_ENV=development

   - Add to cartSECRET_KEY=your-secret-key-here

   - Update quantitiesDATABASE_URL=sqlite:///demo.db

   - Checkout processJWT_SECRET_KEY=your-jwt-secret



9. **📧 Email System** - Email operations# MongoDB (optional)

   - Send emailsMONGO_URI=mongodb://localhost:27017/demo_db

   - Templates

   - Attachments# API Keys

WEATHER_API_KEY=your-openweather-api-key

10. **📊 Data Visualization** - Charts & graphs```

    - Bar charts

    - Line graphs## API Documentation

    - Pie charts

### Calculator APIs

11. **🔍 Search Engine** - Search functionality- `POST /api/calculator/basic` - Basic calculations

    - Full-text search- `POST /api/calculator/advanced` - Advanced calculations

    - Filters- `POST /api/calculator/bmi` - BMI calculator

    - Pagination

### Todo APIs

12. **📱 Social Media API** - Social features- `GET /api/todos` - Get all todos

    - Posts- `POST /api/todos` - Create todo

    - Comments- `PUT /api/todos/:id` - Update todo

    - Likes- `DELETE /api/todos/:id` - Delete todo



13. **💬 Chat Application** - Real-time messaging### Blog APIs

    - WebSocket support- `GET /api/blog/posts` - Get all posts

    - Group chat- `POST /api/blog/posts` - Create post

    - Private messages- `PUT /api/blog/posts/:id` - Update post

- `DELETE /api/blog/posts/:id` - Delete post

#### **Part 3: React Frontend (3 Demos)**- `POST /api/blog/posts/:id/like` - Like post

- `POST /api/blog/posts/:id/comment` - Add comment

14. **⚛️ React Todo App** (Port 3000)

    - Modern React with Hooks### Student APIs

    - Full CRUD operations- `GET /api/students` - Get all students

    - Priority management- `POST /api/students` - Create student

    - Real-time updates- `POST /api/students/:id/grades` - Add grade

- `GET /api/students/:id/gpa` - Calculate GPA

15. **🎨 Component Library** - Reusable UI components- `GET /api/students/:id/transcript` - Get transcript

    - Buttons, Forms, Cards

    - Navigation, Modals### Library APIs

    - Best practices- `GET /api/library/books` - Get all books

- `POST /api/library/books` - Add book

16. **🔄 State Management** - Advanced React patterns- `POST /api/library/borrow/:id` - Borrow book

    - Context API- `POST /api/library/return/:id` - Return book

    - Custom hooks

    - State optimization### Contact APIs

- `GET /api/contacts` - Get all contacts

#### **Part 4: Advanced Topics (5 Demos)**- `POST /api/contacts` - Create contact

- `PUT /api/contacts/:id` - Update contact

17. **🌐 GraphQL API** - Modern API queries- `DELETE /api/contacts/:id` - Delete contact

    - Flexible queries

    - Mutations### Authentication APIs

    - Subscriptions- `POST /api/auth/register` - Register user

- `POST /api/auth/login` - Login user

18. **🔄 Microservices** (Ports 8000-8002)- `POST /api/auth/logout` - Logout user

    - User Service (8001)- `GET /api/auth/profile` - Get profile (protected)

    - Post Service (8002)

    - API Gateway (8000)## Features by Project

    - Service communication

### 1. Simple Calculator ⭐

19. **⚡ Async Python** - Asynchronous programming- Basic arithmetic operations

    - Async/await- Real-time calculation

    - Concurrent operations- Error handling

    - Performance optimization- History tracking



20. **🕷️ Web Scraper** - Data extraction### 2. Grade Calculator ⭐⭐

    - BeautifulSoup- Student grade calculation

    - Async scraping- Letter grade conversion

    - Data processing- Pass/Fail status

- Grade statistics

21. **🤖 AI Integration** - Machine Learning

    - Model integration### 3. Advanced Calculator ⭐⭐⭐

    - Predictions- 9 calculation modes

    - Data analysis- Scientific functions

- BMI calculator

---- Area calculators

- Unit conversions

## 🏗️ Architecture

### 4. Todo List App ⭐⭐⭐

```- Create, read, update, delete todos

┌─────────────────────────────────────────────────────────────┐- Priority levels

│                     NGINX (Port 8080)                        │- Filter by status

│              Static HTML Demo Showcase                       │- Persistent storage

└─────────────────────────────────────────────────────────────┘- Export to JSON

                              │

                              ▼### 5. Contact Manager ⭐⭐⭐

┌─────────────────────────────────────────────────────────────┐- Contact CRUD operations

│                  React Frontend (Port 3000)                  │- Search functionality

│                  Modern Single Page App                      │- Import/Export contacts

└─────────────────────────────────────────────────────────────┘- Group management

                              │

                              ▼### 6. Student Management ⭐⭐⭐

┌─────────────────────────────────────────────────────────────┐- Student enrollment

│                 Flask Backend (Port 5001)                    │- Grade management

│                      REST API Server                         │- GPA calculation

│  ┌─────────────────────────────────────────────────────┐   │- Transcript generation

│  │  Routes:                                             │   │- Course statistics

│  │  • /api/todos        - Todo operations               │   │

│  │  • /api/calculator   - Calculator functions          │   │### 7. Blog System ⭐⭐

│  │  • /api/students     - Student management            │   │- Create posts

│  │  • /api/blog         - Blog system                   │   │- Like and comment

│  │  • /api/auth         - Authentication                │   │- User profiles

│  └─────────────────────────────────────────────────────┘   │- Post statistics

└─────────────────────────────────────────────────────────────┘

                              │### 8. Library System ⭐⭐⭐

                ┌─────────────┼─────────────┐- Book management

                ▼             ▼             ▼- Borrow/Return system

         ┌──────────┐  ┌──────────┐  ┌──────────┐- Search and filter

         │PostgreSQL│  │  Redis   │  │ MongoDB  │- Multiple book types

         │Port 5432 │  │Port 6379 │  │Port 27017│

         └──────────┘  └──────────┘  └──────────┘### 9-14. Database Projects ⭐⭐⭐

- SQLite integration

┌─────────────────────────────────────────────────────────────┐- MongoDB support

│           Microservices (Optional Profile)                   │- ORM examples

│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │- Query optimization

│  │   User      │  │    Post     │  │     API     │        │

│  │  Service    │  │  Service    │  │   Gateway   │        │### 15-17. Frontend Projects ⭐⭐⭐

│  │  Port 8001  │  │  Port 8002  │  │  Port 8000  │        │- React components

│  └─────────────┘  └─────────────┘  └─────────────┘        │- State management

└─────────────────────────────────────────────────────────────┘- API integration

```- Responsive design



### Technology Stack### 18-21. Advanced Projects ⭐⭐⭐⭐

- Microservices

**Backend:**- WebSockets

- Python 3.11- GraphQL

- Flask 3.1.2 (Web Framework)- Async operations

- SQLAlchemy (ORM)

- Flask-CORS (Cross-Origin Support)## Technologies Used

- PostgreSQL (Primary Database)

- Redis (Caching)### Backend

- MongoDB (Document Store)- Flask 3.0

- SQLAlchemy 2.0

**Frontend:**- PyMongo

- React 18- Flask-JWT-Extended

- Modern Hooks (useState, useEffect)- Flask-CORS

- Fetch API for HTTP requests- Bcrypt

- Responsive CSS- Python 3.10+



**Microservices:**### Frontend

- FastAPI (High-performance async framework)- React 18

- Uvicorn (ASGI server)- React Router 6

- Service-to-service communication- Axios

- Material-UI

**DevOps:**- Socket.IO Client

- Docker & Docker Compose- Chart.js

- Nginx (Static file serving)

- Multi-container orchestration### Database

- SQLite (development)

---- PostgreSQL (production)

- MongoDB (NoSQL examples)

## 💻 How to Use- Redis (caching)



### Prerequisites### DevOps

- Docker

- Docker Desktop installed- Docker Compose

- Ports available: 3000, 5001, 5432, 6379, 8000-8002, 8080, 27017- Nginx

- GitHub Actions

### Step 1: Start Services

## Testing

**Option A: Everything (Recommended)**

```bash```bash

docker-compose --profile microservices up -d# Backend tests

```cd backend

pytest tests/

**Option B: Main Services Only**

```bash# Frontend tests

docker-compose up -dcd frontend

```npm test



### Step 2: Verify Services# E2E tests

npm run test:e2e

```bash```

# Check all running containers

docker-compose ps## Deployment



# View logs### Deploy to Heroku

docker-compose logs -f```bash

# Login to Heroku

# Check specific serviceheroku login

docker-compose logs -f backend

```# Create app

heroku create python-fullstack-demo

### Step 3: Access Applications

# Deploy

1. **Open Demo Showcase**: http://localhost:8080git push heroku main

   - Click through all 21 demos

   - Interactive UI for each project# Open app

heroku open

2. **Try React App**: http://localhost:3000```

   - Add todos

   - Mark complete### Deploy to AWS

   - Delete items- Use AWS Elastic Beanstalk

- Configure RDS for database

3. **Test APIs**: http://localhost:5001/api/todos- Use S3 for static files

   - Use browser or Postman- CloudFront for CDN

   - Full REST operations

## Contributing

### Step 4: Stop ServicesThis is a demo/teaching project. Feel free to fork and customize!



```bash## License

# Stop all servicesMIT License - Free for educational use

docker-compose --profile microservices down

## Support

# Stop and remove volumes (clean slate)For issues or questions, create an issue in the repository.

docker-compose --profile microservices down -v

```---



---**Happy Coding! 🎉**


## ✅ Testing & Verification

### Automated Testing

**Run comprehensive test suite:**
```bash
./TEST_ALL.sh
```

This script tests:
- ✅ All Docker containers running
- ✅ Database connections (PostgreSQL, Redis, MongoDB)
- ✅ Backend API endpoints
- ✅ React frontend
- ✅ Demo server
- ✅ Microservices (if running)

**Test individual demos:**
```bash
./TEST_DEMOS.sh
```

### Manual Testing

#### Test Backend APIs

```bash
# Test Calculator API
curl http://localhost:5001/api/calculator/basic

# Test Todo API - List all
curl http://localhost:5001/api/todos

# Create a Todo
curl -X POST http://localhost:5001/api/todos \
  -H "Content-Type: application/json" \
  -d '{"task": "Test task", "priority": "high"}'

# Update a Todo
curl -X PUT http://localhost:5001/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"task": "Updated task", "completed": true}'

# Delete a Todo
curl -X DELETE http://localhost:5001/api/todos/1
```

#### Test Microservices

```bash
# Test User Service
curl http://localhost:8001/users

# Test Post Service
curl http://localhost:8002/posts

# Test API Gateway
curl http://localhost:8000/gateway/users
curl http://localhost:8000/gateway/posts
```

#### Test Databases

```bash
# PostgreSQL
docker exec -it fullstack-postgres psql -U postgres -d fullstack_db -c "SELECT * FROM todos;"

# Redis
docker exec -it fullstack-redis redis-cli PING

# MongoDB
docker exec -it fullstack-mongo mongosh --eval "db.adminCommand('ping')"
```

### Health Checks

```bash
# Check service health
docker-compose ps

# View health status
docker inspect python-fullstack-backend | grep -A 10 Health
```

---

## 📖 API Documentation

### Calculator API

**Base URL:** `http://localhost:5001/api/calculator`

#### Endpoints

```javascript
// Basic Operations
GET /api/calculator/basic
Response: { "add": 15, "subtract": 5, "multiply": 50, "divide": 2 }

// Grade Calculator
GET /api/calculator/grade
Response: { "average": 85.5, "grade": "B", "passed": true }

// Advanced Operations
GET /api/calculator/advanced
Response: { "power": 8, "sqrt": 3.0, "modulus": 1 }
```

### Todo API

**Base URL:** `http://localhost:5001/api/todos`

#### Endpoints

```javascript
// Get all todos
GET /api/todos
Response: [
  {
    "id": 1,
    "task": "Complete project",
    "priority": "high",
    "completed": false,
    "created_at": "2025-12-21T10:30:00"
  }
]

// Create todo
POST /api/todos
Body: {
  "task": "New task",
  "priority": "medium"  // low, medium, high
}
Response: { "id": 2, "task": "New task", "priority": "medium", "completed": false }

// Update todo
PUT /api/todos/{id}
Body: {
  "task": "Updated task",
  "priority": "high",
  "completed": true
}
Response: { "id": 1, "task": "Updated task", "completed": true }

// Delete todo
DELETE /api/todos/{id}
Response: { "message": "Todo deleted successfully" }
```

### Microservices API

**User Service:** `http://localhost:8001`
```javascript
GET /users
GET /users/{id}
POST /users
PUT /users/{id}
DELETE /users/{id}
```

**Post Service:** `http://localhost:8002`
```javascript
GET /posts
GET /posts/{id}
POST /posts
PUT /posts/{id}
DELETE /posts/{id}
```

**API Gateway:** `http://localhost:8000`
```javascript
GET /gateway/users
GET /gateway/posts
// Routes requests to appropriate services
```

---

## 🔧 Troubleshooting

### Common Issues

#### Port Already in Use

**Problem:** Port 5000, 3000, or 8080 already in use

**Solution:**
```bash
# macOS: Stop AirPlay (uses port 5000)
# System Settings → General → AirDrop & Handoff → Disable "AirPlay Receiver"

# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>
```

#### Containers Not Starting

**Problem:** Docker containers fail to start

**Solution:**
```bash
# Stop all containers
docker-compose down

# Remove volumes
docker-compose down -v

# Rebuild and restart
docker-compose build --no-cache
docker-compose --profile microservices up -d
```

#### CORS Errors

**Problem:** Browser shows CORS policy errors

**Solution:**
- Already fixed in backend with `flask-cors`
- Ensure backend is running on port 5001
- Check browser console for specific errors

#### Database Connection Errors

**Problem:** Backend can't connect to database

**Solution:**
```bash
# Check database is running
docker-compose ps db

# Check logs
docker-compose logs db

# Restart database
docker-compose restart db

# Recreate with fresh data
docker-compose down -v
docker-compose up -d
```

#### React App Not Loading

**Problem:** React app shows blank page or errors

**Solution:**
```bash
# Check frontend logs
docker-compose logs frontend

# Rebuild frontend
docker-compose build frontend
docker-compose up -d frontend

# Check browser console for errors
```

### Service-Specific Logs

```bash
# Backend
docker-compose logs -f backend

# Frontend
docker-compose logs -f frontend

# Database
docker-compose logs -f db

# All services
docker-compose logs -f
```

### Reset Everything

```bash
# Nuclear option - start fresh
docker-compose --profile microservices down -v
docker system prune -a --volumes
docker-compose --profile microservices up -d --build
```

---

## 🎓 Learning Path

### Beginner (Hours 1-10)
1. Start with **Calculator API** demo
2. Try **Todo List** for CRUD operations
3. Explore **Student Management**
4. Learn from code in `backend/routes/`

### Intermediate (Hours 11-20)
1. Study **Authentication System**
2. Build **Blog System**
3. Implement **Library Management**
4. Review `backend/models/` for database design

### Advanced (Hours 21-30)
1. **React Todo App** - Modern frontend
2. **Component Library** - Reusable components
3. **State Management** - Advanced patterns
4. Study `frontend/src/` code

### Expert (Hours 31-40)
1. **Microservices** - Distributed architecture
2. **GraphQL** - Modern API design
3. **Async Python** - Performance optimization
4. **Web Scraping** - Data extraction
5. Explore `demos/part4/` implementations

---

## 📁 Project Structure

```
demo-projects/
├── backend/                    # Flask REST API
│   ├── app.py                 # Main application
│   ├── run.py                 # Entry point
│   ├── models/                # Database models
│   │   └── todo.py           # Todo model
│   ├── routes/                # API routes
│   │   ├── calculator.py     # Calculator endpoints
│   │   └── todo.py           # Todo endpoints
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile            # Backend container
│
├── frontend/                  # React application
│   ├── src/
│   │   ├── App.js            # Main component
│   │   ├── App.css           # Styles
│   │   └── index.js          # Entry point
│   ├── public/
│   │   └── index.html        # HTML template
│   ├── package.json          # Node dependencies
│   └── Dockerfile            # Frontend container
│
├── demos/                     # All demo projects
│   ├── live-demo.html        # Unified demo interface
│   ├── part1/                # Python fundamentals
│   ├── part2/                # Backend development
│   ├── part3/                # React frontend
│   └── part4/                # Advanced topics
│       └── 18-microservices/ # Microservices demo
│           ├── user-service.py
│           ├── post-service.py
│           ├── api-gateway.py
│           └── docker-compose.yml
│
├── docker-compose.yml         # Main orchestration
├── nginx.conf                # Demo server config
├── START_ALL.sh              # Startup script
├── TEST_ALL.sh               # Test script
├── TEST_DEMOS.sh             # Demo verification
└── README.md                 # This file
```

---

## 🚀 Deployment

### Production Considerations

**Environment Variables:**
```bash
# Create .env file
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379
MONGODB_URL=mongodb://host:27017
```

**Security:**
- Use environment variables for secrets
- Enable HTTPS/TLS
- Set up proper authentication
- Configure CORS properly
- Use production database

**Scaling:**
```bash
# Scale services
docker-compose --profile microservices up -d --scale backend=3

# Use load balancer
# Add health checks
# Monitor with tools like Prometheus
```

---

## 📝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

---

## 📄 License

This project is for educational purposes as part of the Python Full-Stack Development Training.

---

## 🎉 Success Checklist

- [ ] Docker containers running (`docker-compose ps`)
- [ ] Demo page accessible (http://localhost:8080)
- [ ] React app working (http://localhost:3000)
- [ ] Backend API responding (http://localhost:5001/api/todos)
- [ ] Calculator API working (http://localhost:5001/api/calculator/basic)
- [ ] Can create/update/delete todos
- [ ] All demos visible in showcase
- [ ] Microservices running (if using profile)
- [ ] No errors in logs (`docker-compose logs`)
- [ ] All tests passing (`./TEST_ALL.sh`)

---

## 🆘 Support

**Common Commands:**
```bash
# Start everything
docker-compose --profile microservices up -d

# Stop everything
docker-compose down

# View logs
docker-compose logs -f

# Restart service
docker-compose restart backend

# Access container
docker exec -it python-fullstack-backend /bin/bash

# Check status
docker-compose ps
```

**Quick Health Check:**
```bash
# All in one
curl http://localhost:5001/api/todos && \
curl http://localhost:5001/api/calculator/basic && \
echo "\n✅ Backend is healthy!"
```

---

## 🌟 Features

✅ **21+ Working Demo Projects**  
✅ **One-Command Deployment**  
✅ **Complete Docker Setup**  
✅ **React Frontend**  
✅ **Flask Backend**  
✅ **Multiple Databases**  
✅ **Microservices Architecture**  
✅ **Real-time Features**  
✅ **Modern Tech Stack**  
✅ **Production-Ready Code**  
✅ **Comprehensive Testing**  
✅ **Full Documentation**

---

**Happy Coding! 🎊**

For questions or issues, check the logs: `docker-compose logs -f`
