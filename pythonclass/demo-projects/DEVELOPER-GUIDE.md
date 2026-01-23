# 📘 Python Full-Stack Demo Projects - Complete Developer Guide

**Version:** 1.0  
**Last Updated:** January 2026  
**Course:** 40-Hour Python Full-Stack Development Training

---

## 📚 Table of Contents

1. [Project Overview](#-project-overview)
2. [Quick Start](#-quick-start)
3. [Architecture & System Design](#-architecture--system-design)
4. [All 21 Demo Projects Explained](#-all-21-demo-projects-explained)
5. [Backend API Documentation](#-backend-api-documentation)
6. [Frontend React Application](#-frontend-react-application)
7. [Database Schema & Models](#-database-schema--models)
8. [Docker & DevOps](#-docker--devops)
9. [Code Examples & Tutorials](#-code-examples--tutorials)
10. [Troubleshooting & FAQ](#-troubleshooting--faq)
11. [Contributing & Customization](#-contributing--customization)

---

## 🎯 Project Overview

### What is This?

This is a **unified full-stack web application** that demonstrates 21+ Python programming concepts from beginner to advanced level. All projects are integrated into:

- **Single Backend API** (Flask/FastAPI)
- **React Frontend** (Interactive UI)
- **Live Demo Server** (Nginx serving HTML demos)
- **Multiple Databases** (PostgreSQL, MongoDB, Redis)

### Who Is This For?

- ✅ Python beginners learning fundamentals
- ✅ Backend developers learning Flask/FastAPI
- ✅ Frontend developers learning React
- ✅ Full-stack developers
- ✅ DevOps engineers learning Docker
- ✅ Students in 40-hour Python bootcamp

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Flask 3.0 | REST API server |
| **Frontend** | React 18 | Single Page Application |
| **Database (SQL)** | PostgreSQL 15 | Relational data |
| **Database (NoSQL)** | MongoDB 7 | Document storage |
| **Cache** | Redis 7 | Session & caching |
| **Web Server** | Nginx Alpine | Static file serving |
| **Container** | Docker Compose | Orchestration |
| **Language** | Python 3.11 | Backend logic |
| **Language** | JavaScript (ES6+) | Frontend logic |

---

## 🚀 Quick Start

### Prerequisites

1. **Docker Desktop** installed ([Download here](https://www.docker.com/products/docker-desktop))
2. **Git** (optional, for cloning)
3. **8GB RAM** minimum
4. **Ports available**: 3000, 5001, 8080, 5432, 6379, 27017

### Installation (3 Steps)

```bash
# Step 1: Navigate to project directory
cd pythonclass/demo-projects

# Step 2: Start all services
docker-compose up -d

# Step 3: Access the application
# Open browser: http://localhost:8080
```

That's it! 🎉

### Verification

Run the verification script:

```bash
./VERIFY_ALL.sh
```

You should see:
- ✅ Backend API running on port 5001
- ✅ React Frontend on port 3000
- ✅ Demo Server on port 8080
- ✅ PostgreSQL on port 5432
- ✅ Redis on port 6379
- ✅ MongoDB on port 27017

---

## 🏗️ Architecture & System Design

### High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Users/Browsers                    │
└────────────┬────────────┬──────────────┬─────────────┘
             │            │              │
    ┌────────▼─────┐ ┌───▼────────┐ ┌──▼──────────┐
    │   Nginx      │ │   React    │ │  Backend    │
    │   :8080      │ │   :3000    │ │  Flask      │
    │  (Demos)     │ │   (SPA)    │ │  :5001      │
    └──────────────┘ └────┬───────┘ └──┬──────────┘
                          │            │
                     ┌────▼────────────▼────┐
                     │    Backend API       │
                     │  (Flask + CORS)      │
                     └─┬────────┬─────────┬─┘
                       │        │         │
               ┌───────▼──┐ ┌──▼─────┐ ┌─▼────────┐
               │PostgreSQL│ │ Redis  │ │ MongoDB  │
               │  :5432   │ │ :6379  │ │ :27017   │
               └──────────┘ └────────┘ └──────────┘
```

### Project Structure Explained

```
demo-projects/
│
├── backend/                      # Flask Backend API
│   ├── app.py                   # Main Flask app factory
│   ├── run.py                   # Entry point (runs the server)
│   ├── config.py                # Configuration (DB URLs, secrets)
│   ├── requirements.txt         # Python dependencies
│   │
│   ├── routes/                  # API endpoints (Blueprint pattern)
│   │   ├── calculator.py        # POST /api/calculator/calculate
│   │   ├── todo.py              # CRUD /api/todos
│   │   ├── blog.py              # CRUD /api/blog
│   │   ├── auth.py              # POST /api/auth/login, /register
│   │   ├── student.py           # CRUD /api/students
│   │   ├── library.py           # CRUD /api/library/books
│   │   ├── contact.py           # CRUD /api/contacts
│   │   └── weather.py           # GET /api/weather
│   │
│   ├── models/                  # SQLAlchemy ORM models
│   │   ├── user.py              # User model (auth)
│   │   ├── post.py              # Blog post model
│   │   ├── todo.py              # Todo item model
│   │   ├── book.py              # Library book model
│   │   └── student.py           # Student model
│   │
│   ├── services/                # Business logic layer
│   │   ├── calculator_service.py
│   │   ├── grade_service.py
│   │   └── scraper_service.py
│   │
│   └── database/                # Database initialization
│       ├── init_db.py           # Create tables
│       └── demo.db              # SQLite (fallback)
│
├── frontend/                     # React Single Page App
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── App.js               # Main component (Todo app)
│   │   ├── index.js             # React entry point
│   │   ├── App.css              # Styling
│   │   │
│   │   └── components/          # React components
│   │       ├── Navbar.js        # Navigation bar
│   │       ├── TodoList.js      # Todo display
│   │       ├── TodoForm.js      # Add todo form
│   │       └── Footer.js        # Footer component
│   │
│   ├── package.json             # Node dependencies
│   └── Dockerfile               # React container
│
├── demos/                        # Static HTML demos
│   ├── index.html               # Main landing page (all demos)
│   ├── live-demo.html           # Interactive demo runner
│   │
│   ├── part1/                   # Python Fundamentals (Hours 1-10)
│   │   ├── 01-simple-calculator.py
│   │   ├── 02-grade-calculator.py
│   │   ├── 03-advanced-calculator.py
│   │   ├── 04-todo-app.py
│   │   ├── 05-contact-manager.py
│   │   └── 06-student-system.py
│   │
│   ├── part2/                   # Backend Development (Hours 11-20)
│   │   ├── 07-blog-oop.py
│   │   ├── 08-library-system.py
│   │   ├── 09-blog-sqlite.py
│   │   ├── 10-blog-orm.py
│   │   ├── 11-mongodb-blog.py
│   │   ├── 12-flask-basic-api.py
│   │   ├── 13-flask-blog-api.py
│   │   ├── 14-auth-system.py
│   │   └── 15-data-visualization.html
│   │
│   ├── part3/                   # Frontend Development (Hours 21-30)
│   │   ├── 16-html-css/
│   │   ├── 17-javascript/
│   │   └── 18-react-basics/
│   │
│   └── part4/                   # Advanced Backend (Hours 31-40)
│       ├── 18-microservices/
│       ├── 19-async-scraper.py
│       ├── 20-graphql-api.py
│       └── 21-chat-app/
│
├── docker-compose.yml            # Service orchestration
├── nginx.conf                    # Nginx configuration
│
├── START_ALL.sh                  # Startup script
├── TEST_ALL.sh                   # Test all APIs
├── VERIFY_ALL.sh                 # Health checks
└── README.md                     # This guide
```

### Data Flow

**Example: Adding a Todo Item**

1. User enters todo in React form (`http://localhost:3000`)
2. React sends POST request to `http://localhost:5001/api/todos`
3. Flask backend receives request in `routes/todo.py`
4. Request data validated
5. `models/todo.py` creates SQLAlchemy Todo object
6. Data saved to PostgreSQL database
7. Response sent back to React
8. React updates UI with new todo

---

## 🎓 All 21 Demo Projects Explained

### Part 1: Python Fundamentals (Hours 1-10)

#### Demo 1: Simple Calculator
**File:** `demos/part1/01-simple-calculator.py`

**What it teaches:**
- Basic Python syntax
- Variables and data types
- Arithmetic operators (+, -, *, /)
- Input/output with `input()` and `print()`

**Code structure:**
```python
# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == '+':
    result = num1 + num2
# ... etc
```

**How to run:**
```bash
python demos/part1/01-simple-calculator.py
```

**API Endpoint:**
```bash
POST http://localhost:5001/api/calculator/calculate
{
  "num1": 10,
  "num2": 5,
  "operator": "+"
}
```

---

#### Demo 2: Grade Calculator
**File:** `demos/part1/02-grade-calculator.py`

**What it teaches:**
- If/elif/else statements
- Comparison operators
- Grade classification logic
- String formatting

**Code structure:**
```python
marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
# ... etc
```

**How to customize:**
Change the grading thresholds in the if conditions.

---

#### Demo 3: Advanced Calculator
**File:** `demos/part1/03-advanced-calculator.py`

**What it teaches:**
- Functions and modular code
- Math module (sqrt, pow, sin, cos)
- Error handling with try/except
- Multiple operations

**Code structure:**
```python
import math

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    # ... etc

def scientific_calc(num, operation):
    if operation == 'sqrt':
        return math.sqrt(num)
    # ... etc
```

---

#### Demo 4: Todo App (CLI)
**File:** `demos/part1/04-todo-app.py`

**What it teaches:**
- Lists and list operations
- While loops
- CRUD operations (Create, Read, Update, Delete)
- Menu-driven programs

**Code structure:**
```python
todos = []

while True:
    print("\n1. Add Todo")
    print("2. View Todos")
    print("3. Delete Todo")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        task = input("Enter task: ")
        todos.append(task)
    # ... etc
```

**Upgrade path:**
This CLI app evolved into the full-stack todo app with React frontend!

---

#### Demo 5: Contact Manager
**File:** `demos/part1/05-contact-manager.py`

**What it teaches:**
- Dictionaries and nested data structures
- JSON file I/O (`json.load()`, `json.dump()`)
- Data persistence
- Search and filter operations

**Code structure:**
```python
import json

contacts = {
    "john@email.com": {
        "name": "John Doe",
        "phone": "555-1234"
    }
}

# Save to file
with open('contacts.json', 'w') as f:
    json.dump(contacts, f)

# Load from file
with open('contacts.json', 'r') as f:
    contacts = json.load(f)
```

---

#### Demo 6: Student Management System
**File:** `demos/part1/06-student-system.py`

**What it teaches:**
- Object-Oriented Programming basics
- Classes and objects
- Instance variables and methods
- List comprehensions

**Code structure:**
```python
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return 'A'
        # ... etc

students = [
    Student("Alice", 101, [85, 90, 88]),
    Student("Bob", 102, [75, 80, 78])
]
```

**API Endpoint:**
```bash
GET http://localhost:5001/api/students
POST http://localhost:5001/api/students
{
  "name": "Alice",
  "roll_no": 101,
  "marks": [85, 90, 88]
}
```

---

### Part 2: Backend Development (Hours 11-20)

#### Demo 7: Blog System (OOP)
**File:** `demos/part2/07-blog-oop.py`

**What it teaches:**
- Advanced OOP (inheritance, polymorphism)
- Multiple classes interacting
- Encapsulation and data hiding
- Method chaining

**Code structure:**
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
    
    def create_post(self, title, content):
        post = Post(title, content, self)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []
    
    def add_comment(self, comment):
        self.comments.append(comment)
```

---

#### Demo 8: Library Management System
**File:** `demos/part2/08-library-system.py`

**What it teaches:**
- Complex class relationships
- Date/time handling with `datetime`
- Business logic (borrow, return, late fees)
- Data validation

**Code structure:**
```python
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def borrow_book(self, isbn, member_id):
        book = self.books[isbn]
        if book.is_borrowed:
            return False
        
        book.is_borrowed = True
        book.borrowed_by = member_id
        book.due_date = datetime.now() + timedelta(days=14)
        return True
```

**API Endpoint:**
```bash
GET http://localhost:5001/api/library/books
POST http://localhost:5001/api/library/books
{
  "isbn": "978-1234567890",
  "title": "Python Crash Course",
  "author": "Eric Matthes"
}
```

---

#### Demo 9: Blog with SQLite
**File:** `demos/part2/09-blog-sqlite.py`

**What it teaches:**
- SQL database basics
- sqlite3 module
- CRUD operations with SQL
- Prepared statements (SQL injection prevention)

**Code structure:**
```python
import sqlite3

# Connect to database
conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert data
cursor.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ("My First Post", "Hello World")
)
conn.commit()

# Query data
cursor.execute("SELECT * FROM posts")
posts = cursor.fetchall()
```

---

#### Demo 10: Blog with ORM (SQLAlchemy)
**File:** `demos/part2/10-blog-orm.py`

**What it teaches:**
- Object-Relational Mapping (ORM)
- SQLAlchemy basics
- Database models
- Relationships (One-to-Many, Many-to-Many)

**Code structure:**
```python
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create engine
engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add post
post = Post(title="Hello", content="World")
session.add(post)
session.commit()

# Query posts
posts = session.query(Post).all()
```

---

#### Demo 11: Blog with MongoDB
**File:** `demos/part2/11-mongodb-blog.py`

**What it teaches:**
- NoSQL database concepts
- MongoDB with PyMongo
- Document-based storage
- Flexible schemas

**Code structure:**
```python
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['blog_db']
posts_collection = db['posts']

# Insert document
post = {
    "title": "My MongoDB Post",
    "content": "Learning NoSQL databases",
    "author": "John Doe",
    "tags": ["mongodb", "nosql", "python"],
    "created_at": datetime.utcnow()
}
result = posts_collection.insert_one(post)

# Query documents
posts = posts_collection.find({"author": "John Doe"})
for post in posts:
    print(post['title'])
```

---

#### Demo 12: Flask Basic API
**File:** `demos/part2/12-flask-basic-api.py`

**What it teaches:**
- Web frameworks basics
- HTTP methods (GET, POST, PUT, DELETE)
- JSON request/response
- RESTful API design

**Code structure:**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify({"success": True, "todos": todos})

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {
        "id": len(todos) + 1,
        "task": data['task'],
        "completed": False
    }
    todos.append(todo)
    return jsonify({"success": True, "todo": todo}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

#### Demo 13: Flask Blog API
**File:** `demos/part2/13-flask-blog-api.py`

**What it teaches:**
- Flask Blueprints (modular routes)
- SQLAlchemy integration with Flask
- Request validation
- Error handling

**Code structure:**
```python
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Blueprint
blog_bp = Blueprint('blog', __name__, url_prefix='/api/blog')

@blog_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        "id": p.id,
        "title": p.title,
        "content": p.content
    } for p in posts])

app.register_blueprint(blog_bp)
```

---

#### Demo 14: Authentication System
**File:** `demos/part2/14-auth-system.py`

**What it teaches:**
- User authentication
- Password hashing (bcrypt)
- JWT tokens
- Protected routes

**Code structure:**
```python
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

users = {}

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Hash password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    users[data['email']] = {
        "email": data['email'],
        "password": hashed_password
    }
    
    return jsonify({"success": True})

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.get(data['email'])
    
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        token = create_access_token(identity=data['email'])
        return jsonify({"access_token": token})
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "This is protected!"})
```

---

#### Demo 15: Data Visualization
**File:** `demos/part2/15-data-visualization.html`

**What it teaches:**
- Chart.js library
- Data visualization on web
- API data consumption
- Interactive charts

---

### Part 3: Frontend Development (Hours 21-30)

#### Demo 16: HTML & CSS Basics
**Directory:** `demos/part3/16-html-css/`

**What it teaches:**
- HTML5 semantic tags
- CSS Flexbox and Grid
- Responsive design
- Bootstrap framework

---

#### Demo 17: JavaScript Essentials
**Directory:** `demos/part3/17-javascript/`

**What it teaches:**
- ES6+ features (arrow functions, destructuring)
- DOM manipulation
- Event handling
- Fetch API

---

#### Demo 18: React Basics
**Directory:** `demos/part3/18-react-basics/`

**What it teaches:**
- React components
- JSX syntax
- Props and State
- Hooks (useState, useEffect)

---

### Part 4: Advanced Backend (Hours 31-40)

#### Demo 19: Async Web Scraper
**File:** `demos/part4/19-async-scraper.py`

**What it teaches:**
- Asynchronous programming with `asyncio`
- `aiohttp` for async HTTP requests
- Web scraping with BeautifulSoup
- Parallel processing

**Code structure:**
```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_multiple_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        return pages

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

asyncio.run(scrape_multiple_pages(urls))
```

---

#### Demo 20: GraphQL API
**File:** `demos/part4/20-graphql-api.py`

**What it teaches:**
- GraphQL vs REST
- Strawberry GraphQL framework
- Type definitions and resolvers
- Query and Mutation

**Code structure:**
```python
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Post:
    id: int
    title: str
    content: str

@strawberry.type
class Query:
    @strawberry.field
    def posts(self) -> list[Post]:
        return [
            Post(id=1, title="Hello", content="World")
        ]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_post(self, title: str, content: str) -> Post:
        # Create post logic
        return Post(id=2, title=title, content=content)

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.include_router(
    GraphQLRouter(schema),
    prefix="/graphql"
)
```

**How to query:**
```graphql
query {
  posts {
    id
    title
    content
  }
}

mutation {
  createPost(title: "New Post", content: "GraphQL is awesome") {
    id
    title
  }
}
```

---

#### Demo 21: Real-Time Chat Application
**Directory:** `demos/part4/21-chat-app/`

**What it teaches:**
- WebSockets with Flask-SocketIO
- Real-time bidirectional communication
- Event-driven architecture
- Broadcasting messages

**Code structure:**
```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    print(f"Message: {data}")
    emit('message', data, broadcast=True)

@socketio.on('join')
def handle_join(room):
    join_room(room)
    emit('message', f"User joined {room}", room=room)

if __name__ == '__main__':
    socketio.run(app, port=5000)
```

**Client HTML:**
```html
<script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
<script>
  const socket = io('http://localhost:5000');
  
  socket.on('connect', () => {
    console.log('Connected to server');
  });
  
  socket.on('message', (data) => {
    console.log('Message:', data);
  });
  
  function sendMessage(text) {
    socket.emit('message', text);
  }
</script>
```

---

## 🔧 Backend API Documentation

### Base URL

```
http://localhost:5001/api
```

### Calculator API

#### Calculate Expression
```http
POST /api/calculator/calculate
Content-Type: application/json

{
  "num1": 10,
  "num2": 5,
  "operator": "+"
}

Response:
{
  "success": true,
  "result": 15
}
```

### Todo API

#### Get All Todos
```http
GET /api/todos

Response:
{
  "success": true,
  "todos": [
    {
      "id": 1,
      "task": "Learn Python",
      "priority": "high",
      "completed": false,
      "created_at": "2026-01-23T10:00:00"
    }
  ]
}
```

#### Create Todo
```http
POST /api/todos
Content-Type: application/json

{
  "task": "Build a project",
  "priority": "medium"
}

Response:
{
  "success": true,
  "todo": {
    "id": 2,
    "task": "Build a project",
    "priority": "medium",
    "completed": false
  }
}
```

#### Update Todo
```http
PUT /api/todos/1
Content-Type: application/json

{
  "completed": true
}

Response:
{
  "success": true,
  "todo": { ... }
}
```

#### Delete Todo
```http
DELETE /api/todos/1

Response:
{
  "success": true,
  "message": "Todo deleted"
}
```

### Blog API

#### Get All Posts
```http
GET /api/blog/posts

Response:
{
  "success": true,
  "posts": [...]
}
```

#### Create Post
```http
POST /api/blog/posts
Content-Type: application/json
Authorization: Bearer <token>

{
  "title": "My Blog Post",
  "content": "This is the content..."
}
```

### Authentication API

#### Register
```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepass123",
  "name": "John Doe"
}

Response:
{
  "success": true,
  "message": "User registered successfully"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepass123"
}

Response:
{
  "success": true,
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Student API

#### Get All Students
```http
GET /api/students

Response:
{
  "success": true,
  "students": [
    {
      "id": 1,
      "name": "Alice",
      "roll_no": 101,
      "marks": [85, 90, 88],
      "grade": "A"
    }
  ]
}
```

#### Add Student
```http
POST /api/students
Content-Type: application/json

{
  "name": "Bob",
  "roll_no": 102,
  "marks": [75, 80, 78]
}
```

### Library API

#### Get All Books
```http
GET /api/library/books

Response:
{
  "success": true,
  "books": [
    {
      "isbn": "978-1234567890",
      "title": "Python Crash Course",
      "author": "Eric Matthes",
      "is_borrowed": false
    }
  ]
}
```

#### Borrow Book
```http
POST /api/library/borrow
Content-Type: application/json

{
  "isbn": "978-1234567890",
  "member_id": "M001"
}
```

---

## ⚛️ Frontend React Application

### Component Structure

```
src/
├── App.js                  # Main application component
├── index.js               # React entry point
├── App.css               # Global styles
│
└── components/
    ├── Navbar.js         # Navigation bar
    ├── TodoList.js       # Display todos
    ├── TodoForm.js       # Add new todo
    ├── TodoItem.js       # Individual todo
    └── Footer.js         # Footer component
```

### App.js Explained

```javascript
import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5001';

function App() {
  // State management
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState({ task: '', priority: 'medium' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Fetch todos when component mounts
  useEffect(() => {
    fetchTodos();
  }, []);

  // API call to fetch todos
  const fetchTodos = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/api/todos`);
      const data = await response.json();
      if (data.success) {
        setTodos(data.todos);
      }
    } catch (err) {
      setError('Failed to fetch todos');
    } finally {
      setLoading(false);
    }
  };

  // Add new todo
  const addTodo = async (e) => {
    e.preventDefault();
    
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
    }
  };

  // Toggle todo completion
  const toggleTodo = async (id) => {
    const todo = todos.find(t => t.id === id);
    
    const response = await fetch(`${API_URL}/api/todos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        completed: !todo.completed
      }),
    });
    
    const data = await response.json();
    if (data.success) {
      setTodos(todos.map(t => t.id === id ? data.todo : t));
    }
  };

  // Delete todo
  const deleteTodo = async (id) => {
    const response = await fetch(`${API_URL}/api/todos/${id}`, {
      method: 'DELETE',
    });
    
    const data = await response.json();
    if (data.success) {
      setTodos(todos.filter(t => t.id !== id));
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 Python Full Stack Todo App</h1>
      </header>
      
      {/* Add Todo Form */}
      <form onSubmit={addTodo}>
        <input
          type="text"
          value={newTodo.task}
          onChange={(e) => setNewTodo({...newTodo, task: e.target.value})}
          placeholder="Enter todo task"
        />
        
        <select
          value={newTodo.priority}
          onChange={(e) => setNewTodo({...newTodo, priority: e.target.value})}
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
        
        <button type="submit">Add Todo</button>
      </form>
      
      {/* Todo List */}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul className="todo-list">
          {todos.map(todo => (
            <li key={todo.id} className={todo.completed ? 'completed' : ''}>
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
              />
              <span>{todo.task}</span>
              <span className={`priority priority-${todo.priority}`}>
                {todo.priority}
              </span>
              <button onClick={() => deleteTodo(todo.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
      
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;
```

### How to Customize

#### Change API URL
Edit `.env` file:
```
REACT_APP_API_URL=http://your-server:5001
```

#### Add New Component
```javascript
// src/components/Weather.js
import React, { useState, useEffect } from 'react';

function Weather() {
  const [weather, setWeather] = useState(null);
  
  useEffect(() => {
    fetch('http://localhost:5001/api/weather')
      .then(res => res.json())
      .then(data => setWeather(data));
  }, []);
  
  return (
    <div>
      {weather && <p>{weather.temperature}°C</p>}
    </div>
  );
}

export default Weather;
```

Then import in App.js:
```javascript
import Weather from './components/Weather';

// In render:
<Weather />
```

---

## 🗄️ Database Schema & Models

### PostgreSQL Tables

#### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Posts Table
```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER REFERENCES users(id),
    published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Todos Table
```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    task VARCHAR(200) NOT NULL,
    priority VARCHAR(20) DEFAULT 'medium',
    completed BOOLEAN DEFAULT FALSE,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Books Table
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    is_borrowed BOOLEAN DEFAULT FALSE,
    borrowed_by VARCHAR(50),
    due_date TIMESTAMP
);
```

#### Students Table
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no INTEGER UNIQUE NOT NULL,
    marks JSON,
    grade VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### SQLAlchemy Models

Located in `backend/models/`:

#### User Model
```python
from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True)
    todos = db.relationship('Todo', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at.isoformat()
        }
```

#### Todo Model
```python
class Todo(db.Model):
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20), default='medium')
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }
```

### MongoDB Collections

#### Posts Collection
```javascript
{
  "_id": ObjectId("..."),
  "title": "My MongoDB Post",
  "content": "Content here...",
  "author": {
    "id": 1,
    "name": "John Doe"
  },
  "tags": ["python", "mongodb"],
  "comments": [
    {
      "user": "Alice",
      "text": "Great post!",
      "created_at": ISODate("2026-01-23T10:00:00Z")
    }
  ],
  "created_at": ISODate("2026-01-23T10:00:00Z")
}
```

---

## 🐳 Docker & DevOps

### Docker Compose Services

#### Backend Service
```yaml
backend:
  build: ./backend
  container_name: python-fullstack-backend
  ports:
    - "5001:5000"
  environment:
    - FLASK_ENV=development
    - DATABASE_URL=postgresql://postgres:postgres@db:5432/demo_db
    - REDIS_URL=redis://redis:6379/0
    - MONGO_URI=mongodb://mongo:27017/demo_db
  volumes:
    - ./backend:/app
  depends_on:
    - db
    - redis
    - mongo
  command: python run.py
```

#### Frontend Service
```yaml
frontend:
  build: ./frontend
  container_name: python-fullstack-frontend
  ports:
    - "3000:3000"
  environment:
    - REACT_APP_API_URL=http://localhost:5001
  volumes:
    - ./frontend:/app
    - /app/node_modules
  depends_on:
    - backend
```

#### Demo Server (Nginx)
```yaml
demo-server:
  image: nginx:alpine
  container_name: python-fullstack-demos
  ports:
    - "8080:80"
  volumes:
    - ./demos:/usr/share/nginx/html:ro
    - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
```

### Dockerfile Examples

#### Backend Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "run.py"]
```

#### Frontend Dockerfile
```dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Start development server
CMD ["npm", "start"]
```

### Common Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Rebuild specific service
docker-compose build backend
docker-compose up -d backend

# Execute command in container
docker-compose exec backend python
docker-compose exec db psql -U postgres -d demo_db

# View running containers
docker-compose ps

# Remove all containers and volumes
docker-compose down -v

# Scale service
docker-compose up -d --scale backend=3
```

---

## 💡 Code Examples & Tutorials

### How to Add a New API Endpoint

**Step 1:** Create route file `backend/routes/weather.py`
```python
from flask import Blueprint, jsonify

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET'])
def get_weather():
    return jsonify({
        "success": True,
        "temperature": 25,
        "condition": "Sunny"
    })
```

**Step 2:** Register blueprint in `backend/app.py`
```python
from routes.weather import weather_bp
app.register_blueprint(weather_bp, url_prefix='/api/weather')
```

**Step 3:** Test the endpoint
```bash
curl http://localhost:5001/api/weather
```

### How to Add a New Database Model

**Step 1:** Create model file `backend/models/product.py`
```python
from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }
```

**Step 2:** Create migration
```python
# In Python shell or migration script
from app import create_app, db
from models.product import Product

app = create_app()
with app.app_context():
    db.create_all()
```

**Step 3:** Create CRUD routes
```python
from flask import Blueprint, request, jsonify
from models.product import Product
from app import db

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify({
        "success": True,
        "products": [p.to_dict() for p in products]
    })

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        stock=data.get('stock', 0)
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({
        "success": True,
        "product": product.to_dict()
    }), 201
```

### How to Add React Component

**Step 1:** Create component `frontend/src/components/ProductList.js`
```javascript
import React, { useState, useEffect } from 'react';

function ProductList() {
  const [products, setProducts] = useState([]);
  
  useEffect(() => {
    fetchProducts();
  }, []);
  
  const fetchProducts = async () => {
    const response = await fetch('http://localhost:5001/api/products');
    const data = await response.json();
    setProducts(data.products);
  };
  
  return (
    <div className="product-list">
      <h2>Products</h2>
      {products.map(product => (
        <div key={product.id} className="product-card">
          <h3>{product.name}</h3>
          <p>Price: ${product.price}</p>
          <p>Stock: {product.stock}</p>
        </div>
      ))}
    </div>
  );
}

export default ProductList;
```

**Step 2:** Import in App.js
```javascript
import ProductList from './components/ProductList';

// In render:
<ProductList />
```

---

## 🔍 Troubleshooting & FAQ

### Common Issues

#### 1. Port Already in Use

**Error:** `Address already in use: port 5001`

**Solution:**
```bash
# Find process using the port
lsof -i :5001

# Kill the process
kill -9 <PID>

# Or use different port in docker-compose.yml
ports:
  - "5002:5000"  # Change 5001 to 5002
```

#### 2. Database Connection Failed

**Error:** `could not connect to database`

**Solution:**
```bash
# Check if PostgreSQL container is running
docker-compose ps

# Restart database
docker-compose restart db

# Check logs
docker-compose logs db

# Verify connection string in backend/config.py
DATABASE_URL=postgresql://postgres:postgres@db:5432/demo_db
```

#### 3. CORS Error in Browser

**Error:** `Access to fetch has been blocked by CORS policy`

**Solution:**
```python
# In backend/app.py, ensure CORS is configured:
from flask_cors import CORS

CORS(app, resources={r"/api/*": {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Content-Type", "Authorization"]
}})
```

#### 4. React Not Connecting to Backend

**Error:** `Failed to fetch`

**Solution:**
```bash
# Check if backend is running
curl http://localhost:5001/api/todos

# Verify REACT_APP_API_URL in frontend/.env
REACT_APP_API_URL=http://localhost:5001

# Restart frontend
docker-compose restart frontend
```

#### 5. Module Not Found

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Rebuild backend container
docker-compose build backend
docker-compose up -d backend

# Or install dependencies manually
docker-compose exec backend pip install -r requirements.txt
```

### FAQ

**Q: How do I add more demo projects?**

A: Create a new Python file in `demos/part*/` and add link in `demos/index.html`:
```html
<a href="part1/07-my-new-demo.py">07. My New Demo</a>
```

**Q: Can I use this in production?**

A: This is designed for learning. For production:
- Change `SECRET_KEY` and `JWT_SECRET_KEY`
- Use production database (not SQLite)
- Enable HTTPS
- Add rate limiting
- Implement proper error handling
- Use environment variables
- Add monitoring and logging

**Q: How do I deploy this?**

A: Options:
1. **Heroku:** Use `Procfile` and `requirements.txt`
2. **AWS EC2:** Run `docker-compose up` on server
3. **Digital Ocean:** Use App Platform or Droplet
4. **Vercel/Netlify:** Frontend only (separate backend)

**Q: How do I backup the database?**

A:
```bash
# Backup PostgreSQL
docker-compose exec db pg_dump -U postgres demo_db > backup.sql

# Restore
docker-compose exec -T db psql -U postgres demo_db < backup.sql

# Backup MongoDB
docker-compose exec mongo mongodump --out /backup

# Restore
docker-compose exec mongo mongorestore /backup
```

---

## 🤝 Contributing & Customization

### Project Structure for New Features

```
demo-projects/
├── backend/
│   ├── routes/          # Add new API routes here
│   ├── models/          # Add new database models here
│   ├── services/        # Add business logic here
│   └── utils/           # Add helper functions here
│
├── frontend/
│   └── src/
│       └── components/  # Add new React components here
│
└── demos/
    └── part*/           # Add new Python demos here
```

### Coding Standards

#### Python (Backend)
- Follow PEP 8 style guide
- Use type hints
- Write docstrings
- Use blueprints for routes
- Separate business logic from routes

```python
# Good
@todo_bp.route('/', methods=['POST'])
def create_todo():
    """Create a new todo item"""
    data = request.get_json()
    
    # Validation
    if not data.get('task'):
        return jsonify({"error": "Task is required"}), 400
    
    # Create todo
    todo = Todo(task=data['task'], priority=data.get('priority', 'medium'))
    db.session.add(todo)
    db.session.commit()
    
    return jsonify({"success": True, "todo": todo.to_dict()}), 201
```

#### JavaScript (Frontend)
- Use ES6+ features
- Use functional components with hooks
- Implement error handling
- Add loading states

```javascript
// Good
const [data, setData] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

useEffect(() => {
  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch(API_URL);
      const json = await response.json();
      setData(json.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  fetchData();
}, []);
```

### Testing Your Changes

```bash
# Test backend API
./TEST_ALL.sh

# Test specific endpoint
curl -X POST http://localhost:5001/api/todos \
  -H "Content-Type: application/json" \
  -d '{"task":"Test Todo","priority":"high"}'

# Test React app
cd frontend
npm test

# Run all verifications
./VERIFY_ALL.sh
```

### Version Control

```bash
# Create feature branch
git checkout -b feature/my-new-feature

# Make changes
git add .
git commit -m "Add new feature: description"

# Push to repository
git push origin feature/my-new-feature
```

---

## 📖 Additional Resources

### Official Documentation
- [Flask Docs](https://flask.palletsprojects.com/)
- [React Docs](https://react.dev/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Docker Docs](https://docs.docker.com/)

### Tutorials
- [Python Full Course (40 Hours)](../Part1_Python_Fundamentals_Hours_1-10.md)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [React Tutorial](https://react.dev/learn)

### Community
- Stack Overflow
- GitHub Issues
- Discord/Slack communities

---

## 📄 License

This project is for educational purposes. Feel free to use, modify, and distribute for learning.

---

## 🎉 Conclusion

You now have a complete understanding of:
- ✅ All 21 demo projects and their purpose
- ✅ Backend API architecture and endpoints
- ✅ Frontend React application structure
- ✅ Database schemas and models
- ✅ Docker containerization and deployment
- ✅ How to customize and extend the project

**Happy Coding! 🚀**

---

**Need Help?** Create an issue or reach out to the course instructor.

**Want to Contribute?** Pull requests are welcome!

---

*Last Updated: January 23, 2026*
*Version: 1.0*
