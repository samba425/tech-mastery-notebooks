# Part 4: Advanced Backend Development
## Hours 31-40 (Performance, Microservices, Production)

**Duration:** 10 hours total  
**Target:** Students who completed Frontend development  
**Format:** 1 hour per session  
**Style:** Read and teach directly, copy-paste examples

---

## 📚 TABLE OF CONTENTS

- [Hour 31: Asynchronous Python (asyncio & FastAPI)](#hour-31)
- [Hour 32: FastAPI Deep Dive](#hour-32)
- [Hour 33: Caching & Performance](#hour-33)
- [Hour 34: Message Queues & Background Processing](#hour-34)
- [Hour 35: File Uploads, Media Handling & S3](#hour-35)
- [Hour 36: Security Best Practices](#hour-36)
- [Hour 37: GraphQL Introduction](#hour-37)
- [Hour 38: Microservices & API Gateway Concepts](#hour-38)
- [Hour 39: Observability: Logging, Metrics & Tracing](#hour-39)
- [Hour 40: Testing & CI for Backend](#hour-40)

---

<a name="hour-31"></a>
## 📅 Hour 31: Asynchronous Python (asyncio & FastAPI)

### 🎯 Learning Objectives
- Understand async/await and when to use asynchronous programming
- Learn the difference between sync and async operations
- Build your first FastAPI application
- Convert Flask endpoints to FastAPI async endpoints
- Benchmark performance differences

### 📖 What to Teach

**"Today we learn asynchronous programming - the secret to building high-performance web applications!"**

---

### 1️⃣ What is Asynchronous Programming? (10 minutes)

**Real-Life Analogy:**

```
Synchronous (Blocking):
├── Chef cooks one dish at a time
├── Waits for each dish to complete
└── Restaurant serves 10 customers/hour

Asynchronous (Non-blocking):
├── Chef starts multiple dishes simultaneously
├── Works on other tasks while food cooks
└── Restaurant serves 50 customers/hour
```

**Synchronous vs Asynchronous Code:**

```python
import time
import requests
import asyncio
import aiohttp

# SYNCHRONOUS (BLOCKING)
def fetch_data_sync():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    
    results = []
    start_time = time.time()
    
    for url in urls:
        response = requests.get(url)  # Blocks until response
        results.append(response.json())
        print(f"Fetched {url}")
    
    end_time = time.time()
    print(f"Sync took: {end_time - start_time:.2f} seconds")
    return results

# ASYNCHRONOUS (NON-BLOCKING)
async def fetch_data_async():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # Start all requests simultaneously
        tasks = [fetch_single(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"Async took: {end_time - start_time:.2f} seconds")
    return results

async def fetch_single(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"Fetched {url}")
        return data

# Run the comparison
if __name__ == "__main__":
    # Sync version
    sync_results = fetch_data_sync()
    
    # Async version
    async_results = asyncio.run(fetch_data_async())
```

**When to Use Async:**
- ✅ **I/O Heavy Operations**: Database queries, API calls, file operations
- ✅ **High Concurrency**: Many simultaneous users
- ✅ **Real-time Applications**: WebSockets, streaming data
- ❌ **CPU-intensive Tasks**: Mathematical calculations, image processing

---

### 2️⃣ FastAPI Basics (15 minutes)

**Install FastAPI:**

```bash
pip install fastapi uvicorn[standard] aiohttp aiosqlite
```

**Your First FastAPI App:**

```python
# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import aiohttp
import uvicorn

app = FastAPI(
    title="Async Todo API",
    description="A high-performance async Todo API built with FastAPI",
    version="1.0.0"
)

# Pydantic models for request/response validation
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None

# In-memory storage (replace with database in production)
todos_db = []
todo_counter = 1

@app.get("/")
async def root():
    """Welcome endpoint with async example"""
    # Simulate async operation
    await asyncio.sleep(0.1)
    return {"message": "Welcome to Async Todo API!"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "async": True}

@app.post("/todos", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    """Create a new todo item"""
    global todo_counter
    
    # Simulate async database operation
    await asyncio.sleep(0.05)
    
    new_todo = {
        "id": todo_counter,
        "title": todo.title,
        "description": todo.description,
        "completed": False,
        "priority": todo.priority
    }
    
    todos_db.append(new_todo)
    todo_counter += 1
    
    return new_todo

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos(skip: int = 0, limit: int = 10):
    """Get all todos with pagination"""
    # Simulate async database query
    await asyncio.sleep(0.02)
    
    return todos_db[skip:skip + limit]

@app.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int):
    """Get a specific todo by ID"""
    # Simulate async database lookup
    await asyncio.sleep(0.02)
    
    for todo in todos_db:
        if todo["id"] == todo_id:
            return todo
    
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    """Update a specific todo"""
    # Simulate async database update
    await asyncio.sleep(0.03)
    
    for todo in todos_db:
        if todo["id"] == todo_id:
            if todo_update.title is not None:
                todo["title"] = todo_update.title
            if todo_update.description is not None:
                todo["description"] = todo_update.description
            if todo_update.completed is not None:
                todo["completed"] = todo_update.completed
            if todo_update.priority is not None:
                todo["priority"] = todo_update.priority
            
            return todo
    
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """Delete a specific todo"""
    # Simulate async database deletion
    await asyncio.sleep(0.03)
    
    for i, todo in enumerate(todos_db):
        if todo["id"] == todo_id:
            deleted_todo = todos_db.pop(i)
            return {"message": "Todo deleted successfully", "deleted_todo": deleted_todo}
    
    raise HTTPException(status_code=404, detail="Todo not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

**Run FastAPI App:**

```bash
# Method 1: Using uvicorn directly
uvicorn main:app --reload

# Method 2: Using python
python main.py

# Access your API:
# http://127.0.0.1:8000 - API root
# http://127.0.0.1:8000/docs - Interactive API docs (Swagger)
# http://127.0.0.1:8000/redoc - Alternative docs
```

---

### 3️⃣ Converting Flask to FastAPI (15 minutes)

**Flask Version (Synchronous):**

```python
# flask_app.py
from flask import Flask, request, jsonify
import time
import requests

app = Flask(__name__)

@app.route('/external-data', methods=['GET'])
def get_external_data():
    """Fetch data from multiple external APIs - SYNC version"""
    start_time = time.time()
    
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/users/1',
        'https://jsonplaceholder.typicode.com/albums/1'
    ]
    
    results = []
    for url in urls:
        response = requests.get(url)  # BLOCKING operation
        results.append(response.json())
    
    end_time = time.time()
    
    return jsonify({
        "data": results,
        "processing_time": f"{end_time - start_time:.2f}s",
        "type": "synchronous"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**FastAPI Version (Asynchronous):**

```python
# fastapi_app.py
from fastapi import FastAPI
import time
import asyncio
import aiohttp
from typing import List, Dict, Any

app = FastAPI()

@app.get("/external-data")
async def get_external_data() -> Dict[str, Any]:
    """Fetch data from multiple external APIs - ASYNC version"""
    start_time = time.time()
    
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/users/1',
        'https://jsonplaceholder.typicode.com/albums/1'
    ]
    
    # Fetch all URLs concurrently
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    return {
        "data": results,
        "processing_time": f"{end_time - start_time:.2f}s",
        "type": "asynchronous"
    }

async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """Helper function to fetch a single URL"""
    async with session.get(url) as response:
        return await response.json()

# Additional async endpoint for database simulation
@app.get("/slow-operation")
async def slow_operation():
    """Simulate a slow database operation"""
    # This could be a database query, file I/O, etc.
    await asyncio.sleep(2)  # Non-blocking wait
    
    return {
        "message": "Operation completed",
        "note": "This was async - server could handle other requests during the wait"
    }

# Concurrent requests handler
@app.get("/concurrent-test/{num_requests}")
async def concurrent_test(num_requests: int):
    """Test concurrent request handling"""
    start_time = time.time()
    
    # Simulate multiple async operations
    tasks = [simulate_work(i) for i in range(num_requests)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    return {
        "results": results,
        "total_requests": num_requests,
        "total_time": f"{end_time - start_time:.2f}s",
        "average_time_per_request": f"{(end_time - start_time) / num_requests:.2f}s"
    }

async def simulate_work(task_id: int) -> Dict[str, Any]:
    """Simulate some async work"""
    # Random delay between 0.1 and 0.5 seconds
    delay = 0.1 + (task_id % 5) * 0.1
    await asyncio.sleep(delay)
    
    return {
        "task_id": task_id,
        "delay": delay,
        "status": "completed"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
```

---

### 4️⃣ Database Operations with AsyncIO (15 minutes)

**Async Database Setup:**

```python
# database.py
import aiosqlite
from typing import List, Dict, Any, Optional
import asyncio
import json

class AsyncTodoDatabase:
    def __init__(self, db_path: str = "async_todos.db"):
        self.db_path = db_path
    
    async def init_database(self):
        """Initialize the database with tables"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    completed BOOLEAN DEFAULT FALSE,
                    priority TEXT DEFAULT 'medium',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            await db.commit()
    
    async def create_todo(self, title: str, description: str = None, priority: str = "medium") -> Dict[str, Any]:
        """Create a new todo item"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                INSERT INTO todos (title, description, priority)
                VALUES (?, ?, ?)
                """,
                (title, description, priority)
            )
            await db.commit()
            
            todo_id = cursor.lastrowid
            
            # Fetch the created todo
            cursor = await db.execute(
                "SELECT * FROM todos WHERE id = ?", (todo_id,)
            )
            row = await cursor.fetchone()
            
            return {
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "completed": bool(row[3]),
                "priority": row[4],
                "created_at": row[5],
                "updated_at": row[6]
            }
    
    async def get_todos(self, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        """Get todos with pagination"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                SELECT * FROM todos
                ORDER BY created_at DESC
                LIMIT ? OFFSET ?
                """,
                (limit, skip)
            )
            rows = await cursor.fetchall()
            
            return [
                {
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "completed": bool(row[3]),
                    "priority": row[4],
                    "created_at": row[5],
                    "updated_at": row[6]
                }
                for row in rows
            ]
    
    async def get_todo_by_id(self, todo_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific todo by ID"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "SELECT * FROM todos WHERE id = ?", (todo_id,)
            )
            row = await cursor.fetchone()
            
            if row:
                return {
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "completed": bool(row[3]),
                    "priority": row[4],
                    "created_at": row[5],
                    "updated_at": row[6]
                }
            return None
    
    async def update_todo(self, todo_id: int, **kwargs) -> Optional[Dict[str, Any]]:
        """Update a todo item"""
        # Build dynamic update query
        update_fields = []
        values = []
        
        for field, value in kwargs.items():
            if value is not None and field in ['title', 'description', 'completed', 'priority']:
                update_fields.append(f"{field} = ?")
                values.append(value)
        
        if not update_fields:
            return await self.get_todo_by_id(todo_id)
        
        # Add updated_at field
        update_fields.append("updated_at = CURRENT_TIMESTAMP")
        values.append(todo_id)
        
        query = f"UPDATE todos SET {', '.join(update_fields)} WHERE id = ?"
        
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(query, values)
            await db.commit()
            
            return await self.get_todo_by_id(todo_id)
    
    async def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "DELETE FROM todos WHERE id = ?", (todo_id,)
            )
            await db.commit()
            
            return cursor.rowcount > 0

# Usage in FastAPI
from fastapi import FastAPI, HTTPException, Depends
from database import AsyncTodoDatabase

app = FastAPI()
db = AsyncTodoDatabase()

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    await db.init_database()

@app.post("/todos")
async def create_todo_endpoint(title: str, description: str = None, priority: str = "medium"):
    """Create todo with async database"""
    todo = await db.create_todo(title, description, priority)
    return todo

@app.get("/todos")
async def get_todos_endpoint(skip: int = 0, limit: int = 10):
    """Get todos with async database"""
    todos = await db.get_todos(skip, limit)
    return todos

@app.get("/todos/{todo_id}")
async def get_todo_endpoint(todo_id: int):
    """Get single todo with async database"""
    todo = await db.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
```

---

### 5️⃣ Performance Benchmarking (5 minutes)

**Load Testing Script:**

```python
# benchmark.py
import asyncio
import aiohttp
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import statistics

async def benchmark_async_endpoint(url: str, num_requests: int = 100):
    """Benchmark async endpoint"""
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [make_async_request(session, url) for _ in range(num_requests)]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = time.time()
    
    successful_requests = [r for r in results if not isinstance(r, Exception)]
    
    return {
        "total_time": end_time - start_time,
        "requests_per_second": len(successful_requests) / (end_time - start_time),
        "successful_requests": len(successful_requests),
        "failed_requests": num_requests - len(successful_requests)
    }

async def make_async_request(session: aiohttp.ClientSession, url: str):
    """Make a single async request"""
    try:
        async with session.get(url) as response:
            return await response.json()
    except Exception as e:
        return e

def benchmark_sync_endpoint(url: str, num_requests: int = 100, max_workers: int = 10):
    """Benchmark sync endpoint with ThreadPoolExecutor"""
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(make_sync_request, url) for _ in range(num_requests)]
        results = [future.result() for future in futures]
    
    end_time = time.time()
    
    successful_requests = [r for r in results if not isinstance(r, Exception)]
    
    return {
        "total_time": end_time - start_time,
        "requests_per_second": len(successful_requests) / (end_time - start_time),
        "successful_requests": len(successful_requests),
        "failed_requests": num_requests - len(successful_requests)
    }

def make_sync_request(url: str):
    """Make a single sync request"""
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return e

async def run_benchmark():
    """Run the benchmark comparison"""
    fastapi_url = "http://127.0.0.1:8000/external-data"
    flask_url = "http://127.0.0.1:5000/external-data"
    
    print("🚀 Starting Performance Benchmark...")
    print("=" * 50)
    
    # Benchmark FastAPI (async)
    print("Testing FastAPI (Async)...")
    async_results = await benchmark_async_endpoint(fastapi_url, 50)
    
    # Benchmark Flask (sync with threads)
    print("Testing Flask (Sync with threads)...")
    sync_results = benchmark_sync_endpoint(flask_url, 50)
    
    # Display results
    print("\n📊 BENCHMARK RESULTS")
    print("=" * 50)
    print(f"FastAPI (Async):")
    print(f"  Total time: {async_results['total_time']:.2f}s")
    print(f"  Requests/sec: {async_results['requests_per_second']:.2f}")
    print(f"  Success rate: {async_results['successful_requests']}/50")
    
    print(f"\nFlask (Sync + Threads):")
    print(f"  Total time: {sync_results['total_time']:.2f}s")
    print(f"  Requests/sec: {sync_results['requests_per_second']:.2f}")
    print(f"  Success rate: {sync_results['successful_requests']}/50")
    
    # Performance comparison
    improvement = async_results['requests_per_second'] / sync_results['requests_per_second']
    print(f"\n🏆 FastAPI is {improvement:.1f}x faster!")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
```

**Run Benchmark:**

```bash
# Terminal 1: Start FastAPI
uvicorn fastapi_app:app --port 8000

# Terminal 2: Start Flask  
python flask_app.py

# Terminal 3: Run benchmark
python benchmark.py
```

---

### 🏠 Homework: Benchmark Sync vs Async

**Task:** Compare performance of synchronous vs asynchronous endpoints

```python
# Create two endpoints:
# 1. /sync-heavy - Makes 5 sequential API calls
# 2. /async-heavy - Makes 5 concurrent API calls

# Benchmark with different loads:
# - 10 requests
# - 50 requests  
# - 100 requests

# Measure and record:
# - Total response time
# - Requests per second
# - Memory usage
# - CPU usage

# Create a report with your findings
```

---

### 📝 Key Takeaways

✅ Async = Non-blocking I/O operations
✅ FastAPI = Modern async Python web framework
✅ asyncio = Python's async programming library
✅ Performance = Significant improvement for I/O heavy apps
✅ When to use = High concurrency, external API calls, database queries

---

<a name="hour-32"></a>
## 📅 Hour 32: FastAPI Deep Dive

### 🎯 Learning Objectives
- Master dependency injection in FastAPI
- Create robust Pydantic models with validation
- Implement background tasks and async workers
- Use auto-generated API documentation
- Build a complete CRUD system with advanced features

### 📖 What to Teach

**"Today we master FastAPI's advanced features that make it a production-ready framework!"**

---

### 1️⃣ Dependency Injection (15 minutes)

**What is Dependency Injection?**

```python
# Without DI - Hard to test and maintain
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    db = Database()  # Hardcoded dependency
    user = db.get_user(user_id)
    return user

# With DI - Flexible and testable
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Database = Depends(get_database)):
    user = await db.get_user(user_id)
    return user
```

**Database Dependency:**

```python
# dependencies.py
import aiosqlite
from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta

# Database dependency
async def get_database() -> AsyncGenerator[aiosqlite.Connection, None]:
    """Provide database connection"""
    async with aiosqlite.connect("blog.db") as db:
        yield db

# Authentication dependency
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current authenticated user"""
    try:
        payload = jwt.decode(credentials.credentials, "secret_key", algorithms=["HS256"])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        return {"user_id": user_id, "username": payload.get("username")}
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

# Optional authentication (user can be None)
async def get_current_user_optional(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user if authenticated, None otherwise"""
    try:
        return await get_current_user(credentials)
    except HTTPException:
        return None

# Pagination dependency
class PaginationParams:
    def __init__(self, page: int = 1, size: int = 10):
        self.page = max(1, page)
        self.size = min(100, max(1, size))  # Limit max size
        self.offset = (self.page - 1) * self.size

def get_pagination_params(page: int = 1, size: int = 10) -> PaginationParams:
    """Get pagination parameters"""
    return PaginationParams(page, size)

# Admin role dependency
async def require_admin_user(current_user: dict = Depends(get_current_user)):
    """Require admin role"""
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user
```

**Using Dependencies in Endpoints:**

```python
# blog_api.py
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from dependencies import get_database, get_current_user, get_pagination_params
from models import PostCreate, PostResponse, PostUpdate
import aiosqlite
from typing import List

app = FastAPI(
    title="Blog API",
    description="Advanced FastAPI blog with dependency injection",
    version="2.0.0"
)

@app.post("/posts", response_model=PostResponse)
async def create_post(
    post: PostCreate,
    current_user: dict = Depends(get_current_user),
    db: aiosqlite.Connection = Depends(get_database),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    """Create a new blog post"""
    # Insert post into database
    cursor = await db.execute(
        """
        INSERT INTO posts (title, content, author_id, status)
        VALUES (?, ?, ?, ?)
        """,
        (post.title, post.content, current_user["user_id"], "published")
    )
    await db.commit()
    
    post_id = cursor.lastrowid
    
    # Add background task to send notifications
    background_tasks.add_task(notify_subscribers, post_id, post.title)
    
    # Fetch and return the created post
    cursor = await db.execute(
        """
        SELECT p.*, u.username as author_name 
        FROM posts p 
        JOIN users u ON p.author_id = u.id 
        WHERE p.id = ?
        """,
        (post_id,)
    )
    row = await cursor.fetchone()
    
    return PostResponse(
        id=row[0],
        title=row[1],
        content=row[2],
        author_id=row[3],
        author_name=row[6],
        status=row[4],
        created_at=row[5]
    )

@app.get("/posts", response_model=List[PostResponse])
async def get_posts(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: aiosqlite.Connection = Depends(get_database),
    tag: str = None,
    author: str = None
):
    """Get posts with filtering and pagination"""
    query = """
        SELECT p.*, u.username as author_name 
        FROM posts p 
        JOIN users u ON p.author_id = u.id 
        WHERE p.status = 'published'
    """
    params = []
    
    # Add filters
    if tag:
        query += " AND p.tags LIKE ?"
        params.append(f"%{tag}%")
    
    if author:
        query += " AND u.username = ?"
        params.append(author)
    
    # Add ordering and pagination
    query += " ORDER BY p.created_at DESC LIMIT ? OFFSET ?"
    params.extend([pagination.size, pagination.offset])
    
    cursor = await db.execute(query, params)
    rows = await cursor.fetchall()
    
    return [
        PostResponse(
            id=row[0],
            title=row[1],
            content=row[2],
            author_id=row[3],
            author_name=row[6],
            status=row[4],
            created_at=row[5]
        )
        for row in rows
    ]

# Background task function
async def notify_subscribers(post_id: int, post_title: str):
    """Send notification to subscribers (background task)"""
    import asyncio
    # Simulate sending notifications
    print(f"📧 Sending notifications for post: {post_title}")
    await asyncio.sleep(2)  # Simulate email sending
    print(f"✅ Notifications sent for post {post_id}")
```

---

### 2️⃣ Advanced Pydantic Models (15 minutes)

**Comprehensive Model Definitions:**

```python
# models.py
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum

class PostStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class UserRole(str, Enum):
    USER = "user"
    AUTHOR = "author"
    ADMIN = "admin"

# Base models
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9_]+$")
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    
    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "bio": "Software developer and tech enthusiast"
            }
        }

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')  
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v

class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime
    posts_count: int = 0
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

# Post models
class PostBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=10)
    summary: Optional[str] = Field(None, max_length=500)
    tags: List[str] = Field(default_factory=list, max_items=10)
    status: PostStatus = PostStatus.DRAFT
    priority: Priority = Priority.MEDIUM
    
    @validator('tags')
    def validate_tags(cls, v):
        # Remove duplicates and clean tags
        cleaned_tags = []
        for tag in v:
            clean_tag = tag.strip().lower()
            if clean_tag and clean_tag not in cleaned_tags:
                cleaned_tags.append(clean_tag)
        return cleaned_tags[:10]  # Limit to 10 tags

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    content: Optional[str] = Field(None, min_length=10)
    summary: Optional[str] = Field(None, max_length=500)
    tags: Optional[List[str]] = Field(None, max_items=10)
    status: Optional[PostStatus] = None
    priority: Optional[Priority] = None

class PostResponse(PostBase):
    id: int
    author_id: int
    author_name: str
    slug: str
    views_count: int = 0
    likes_count: int = 0
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# Comment models
class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)
    parent_id: Optional[int] = None  # For nested comments

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    post_id: int
    author_id: int
    author_name: str
    created_at: datetime
    replies: List['CommentResponse'] = []
    
    class Config:
        orm_mode = True

# Update forward reference
CommentResponse.model_rebuild()

# Pagination models
class PaginationResponse(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool

class PostListResponse(BaseModel):
    posts: List[PostResponse]
    pagination: PaginationResponse

# Search models
class SearchQuery(BaseModel):
    q: str = Field(..., min_length=1, max_length=100)
    category: Optional[str] = None
    author: Optional[str] = None
    status: Optional[PostStatus] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None

class SearchResponse(BaseModel):
    query: str
    results: List[PostResponse]
    total_results: int
    search_time_ms: float

# Analytics models
class PostAnalytics(BaseModel):
    post_id: int
    views_today: int
    views_week: int
    views_month: int
    likes_count: int
    comments_count: int
    shares_count: int

class UserAnalytics(BaseModel):
    user_id: int
    posts_published: int
    total_views: int
    total_likes: int
    avg_engagement: float
    top_posts: List[PostResponse]
```

**Model Validation Examples:**

```python
# validation_examples.py
from models import PostCreate, UserCreate
from pydantic import ValidationError
import json

# Test valid data
valid_post = {
    "title": "Getting Started with FastAPI",
    "content": "FastAPI is a modern, fast web framework for building APIs with Python...",
    "tags": ["python", "fastapi", "web", "api"],
    "status": "published",
    "priority": "high"
}

try:
    post = PostCreate(**valid_post)
    print("✅ Valid post created:", post.dict())
except ValidationError as e:
    print("❌ Validation error:", e.json())

# Test invalid data
invalid_post = {
    "title": "Hi",  # Too short
    "content": "Short",  # Too short
    "tags": ["python"] * 15,  # Too many tags
    "status": "invalid_status",  # Invalid enum
    "priority": "urgent"  # Invalid enum
}

try:
    post = PostCreate(**invalid_post)
    print("✅ Post created:", post.dict())
except ValidationError as e:
    print("❌ Validation errors:")
    for error in e.errors():
        print(f"  - {error['loc']}: {error['msg']}")
```

---

### 3️⃣ Background Tasks and Workers (15 minutes)

**Background Tasks in FastAPI:**

```python
# background_tasks.py
from fastapi import FastAPI, BackgroundTasks
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import aiofiles
import json
from datetime import datetime
import aiohttp

app = FastAPI()

# Simple background task
async def send_notification_email(user_email: str, subject: str, message: str):
    """Send notification email (simulated)"""
    print(f"📧 Sending email to {user_email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    
    # Simulate email sending delay
    await asyncio.sleep(2)
    
    # Log the email
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "to": user_email,
        "subject": subject,
        "status": "sent"
    }
    
    async with aiofiles.open("email_log.json", "a") as f:
        await f.write(json.dumps(log_data) + "\n")
    
    print(f"✅ Email sent to {user_email}")

# Background task for analytics
async def update_post_analytics(post_id: int, action: str):
    """Update post analytics in background"""
    print(f"📊 Updating analytics for post {post_id}: {action}")
    
    # Simulate analytics update
    await asyncio.sleep(1)
    
    analytics_data = {
        "timestamp": datetime.now().isoformat(),
        "post_id": post_id,
        "action": action,
        "ip_address": "127.0.0.1",  # In real app, get from request
        "user_agent": "FastAPI Client"
    }
    
    async with aiofiles.open("analytics.json", "a") as f:
        await f.write(json.dumps(analytics_data) + "\n")
    
    print(f"✅ Analytics updated for post {post_id}")

# Background task for external API calls
async def sync_with_external_service(post_data: dict):
    """Sync post with external service"""
    print(f"🔄 Syncing post with external service...")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.example.com/posts",
                json=post_data,
                timeout=30
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    print(f"✅ Successfully synced post: {result}")
                else:
                    print(f"❌ Sync failed with status: {response.status}")
    except Exception as e:
        print(f"❌ Sync error: {str(e)}")

# Endpoints using background tasks
@app.post("/posts/{post_id}/view")
async def view_post(post_id: int, background_tasks: BackgroundTasks):
    """Record post view with background analytics"""
    # Immediate response
    response = {"message": "Post viewed", "post_id": post_id}
    
    # Background analytics update
    background_tasks.add_task(update_post_analytics, post_id, "view")
    
    return response

@app.post("/posts")
async def create_post_with_notifications(
    post: PostCreate,
    background_tasks: BackgroundTasks,
    current_user: dict = Depends(get_current_user)
):
    """Create post with background notifications"""
    # Create post (immediate)
    # ... post creation logic ...
    
    post_data = {
        "id": 123,  # Would be actual post ID
        "title": post.title,
        "author": current_user["username"]
    }
    
    # Add background tasks
    if post.status == "published":
        # Notify subscribers
        background_tasks.add_task(
            send_notification_email,
            "subscribers@blog.com",
            f"New Post: {post.title}",
            f"A new post '{post.title}' has been published!"
        )
        
        # Sync with external service
        background_tasks.add_task(sync_with_external_service, post_data)
        
        # Update search index
        background_tasks.add_task(update_search_index, post_data)
    
    return {"message": "Post created", "id": 123}

async def update_search_index(post_data: dict):
    """Update search index for the post"""
    print(f"🔍 Updating search index for post: {post_data['title']}")
    await asyncio.sleep(3)  # Simulate indexing time
    print(f"✅ Search index updated")

# Advanced: Periodic background tasks
import asyncio
from contextlib import asynccontextmanager

async def cleanup_old_logs():
    """Periodic cleanup task"""
    while True:
        print("🧹 Running cleanup task...")
        # Cleanup old log files, temporary data, etc.
        await asyncio.sleep(3600)  # Run every hour

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start background tasks
    cleanup_task = asyncio.create_task(cleanup_old_logs())
    
    yield
    
    # Cleanup
    cleanup_task.cancel()
    try:
        await cleanup_task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan)
```

**Advanced Worker with Celery (Optional):**

```python
# celery_worker.py (for production use)
from celery import Celery
import smtplib
from email.mime.text import MIMEText
import requests
import time

# Configure Celery
celery_app = Celery(
    "blog_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def send_email_task(to_email: str, subject: str, body: str):
    """Send email via Celery worker"""
    print(f"📧 Celery task: Sending email to {to_email}")
    
    # Email sending logic here
    time.sleep(5)  # Simulate email sending
    
    return f"Email sent to {to_email}"

@celery_app.task
def generate_report_task(user_id: int):
    """Generate user analytics report"""
    print(f"📊 Generating report for user {user_id}")
    
    # Complex report generation
    time.sleep(30)  # Simulate long processing
    
    return f"Report generated for user {user_id}"

@celery_app.task(retry_kwargs={'max_retries': 3, 'countdown': 60})
def sync_external_api_task(data: dict):
    """Sync with external API with retry logic"""
    try:
        response = requests.post("https://api.example.com/sync", json=data)
        response.raise_for_status()
        return "Sync successful"
    except Exception as e:
        print(f"Sync failed: {e}")
        # This will automatically retry
        sync_external_api_task.retry(exc=e)

# FastAPI integration with Celery
from fastapi import FastAPI

app = FastAPI()

@app.post("/send-newsletter")
async def send_newsletter(emails: List[str], subject: str, content: str):
    """Send newsletter to multiple emails"""
    # Queue tasks for each email
    task_ids = []
    for email in emails:
        task = send_email_task.delay(email, subject, content)
        task_ids.append(task.id)
    
    return {
        "message": f"Newsletter queued for {len(emails)} recipients",
        "task_ids": task_ids
    }

@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    """Check task status"""
    task = celery_app.AsyncResult(task_id)
    
    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result if task.ready() else None
    }
```

---

### 4️⃣ API Documentation Features (10 minutes)

**Enhanced Documentation:**

```python
# documented_api.py
from fastapi import FastAPI, Query, Path, Body, Header
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from typing import List, Optional
import json

app = FastAPI(
    title="Advanced Blog API",
    description="""
    ## Blog Management API
    
    This API provides comprehensive blog management features including:
    
    * **Posts** - Create, read, update, and delete blog posts
    * **Users** - User management and authentication
    * **Comments** - Nested comment system
    * **Analytics** - Real-time analytics and reporting
    
    ### Authentication
    
    Most endpoints require authentication using JWT tokens in the Authorization header:
    ```
    Authorization: Bearer <your_jwt_token>
    ```
    
    ### Rate Limiting
    
    All endpoints are rate limited to prevent abuse:
    - **Authenticated users**: 1000 requests/hour
    - **Anonymous users**: 100 requests/hour
    """,
    version="2.0.0",
    contact={
        "name": "Blog API Support",
        "url": "https://blog-api.example.com/contact",
        "email": "support@blog-api.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_tags=[
        {
            "name": "posts",
            "description": "Blog post operations",
        },
        {
            "name": "users", 
            "description": "User management operations",
        },
        {
            "name": "analytics",
            "description": "Analytics and reporting endpoints",
        }
    ]
)

@app.get(
    "/posts/{post_id}",
    response_model=PostResponse,
    tags=["posts"],
    summary="Get a specific blog post",
    description="Retrieve a blog post by its ID. Returns detailed post information including author details and engagement metrics.",
    responses={
        200: {
            "description": "Post retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Getting Started with FastAPI",
                        "content": "FastAPI is a modern web framework...",
                        "author_name": "John Doe",
                        "status": "published",
                        "views_count": 150,
                        "likes_count": 25
                    }
                }
            }
        },
        404: {
            "description": "Post not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Post not found"}
                }
            }
        }
    }
)
async def get_post(
    post_id: int = Path(..., description="The unique identifier for the blog post", gt=0),
    include_analytics: bool = Query(False, description="Include detailed analytics data"),
    x_client_version: Optional[str] = Header(None, description="Client application version")
):
    """
    Retrieve a specific blog post by ID.
    
    This endpoint returns detailed information about a blog post including:
    - Post content and metadata
    - Author information
    - Engagement metrics (views, likes, comments)
    - Optional analytics data
    
    **Example Usage:**
    ```python
    import requests
    
    response = requests.get(
        "http://localhost:8000/posts/1",
        params={"include_analytics": True},
        headers={"X-Client-Version": "1.2.0"}
    )
    ```
    """
    # Implementation here
    pass

@app.post(
    "/posts",
    response_model=PostResponse,
    status_code=201,
    tags=["posts"],
    summary="Create a new blog post",
    description="Create a new blog post with title, content, and optional metadata."
)
async def create_post(
    post: PostCreate = Body(
        ...,
        example={
            "title": "My Amazing Blog Post",
            "content": "This is the content of my blog post with **markdown** support.",
            "tags": ["python", "fastapi", "web"],
            "status": "published",
            "priority": "high"
        }
    ),
    x_request_id: Optional[str] = Header(None, description="Unique request identifier for tracing")
):
    """
    Create a new blog post.
    
    **Request Body:**
    - **title**: Post title (5-200 characters)
    - **content**: Post content (minimum 10 characters) 
    - **tags**: List of tags (max 10)
    - **status**: Post status (draft/published/archived)
    - **priority**: Post priority (low/medium/high)
    
    **Background Processing:**
    - Sends notification emails to subscribers
    - Updates search index
    - Syncs with external services
    """
    # Implementation here
    pass

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Advanced Blog API",
        version="2.0.0",
        description="Comprehensive blog management API with advanced features",
        routes=app.routes,
    )
    
    # Add custom security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    
    # Add server information
    openapi_schema["servers"] = [
        {"url": "http://localhost:8000", "description": "Development server"},
        {"url": "https://api.blog.com", "description": "Production server"},
    ]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

---

### 5️⃣ CRUD with Pagination & Filtering (5 minutes)

**Advanced CRUD Implementation:**

```python
# advanced_crud.py
from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy import and_, or_, desc, asc
from typing import Optional, List
from enum import Enum

class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"

class PostSortBy(str, Enum):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at" 
    TITLE = "title"
    VIEWS = "views_count"
    LIKES = "likes_count"

@app.get("/posts", response_model=PostListResponse)
async def get_posts_advanced(
    # Pagination
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page"),
    
    # Sorting
    sort_by: PostSortBy = Query(PostSortBy.CREATED_AT, description="Sort field"),
    sort_order: SortOrder = Query(SortOrder.DESC, description="Sort order"),
    
    # Filtering
    search: Optional[str] = Query(None, description="Search in title and content"),
    author: Optional[str] = Query(None, description="Filter by author username"),
    tags: Optional[List[str]] = Query(None, description="Filter by tags"),
    status: Optional[PostStatus] = Query(None, description="Filter by status"),
    
    # Date filtering
    created_after: Optional[datetime] = Query(None, description="Posts created after date"),
    created_before: Optional[datetime] = Query(None, description="Posts created before date"),
    
    # Dependencies
    db: Session = Depends(get_database)
):
    """
    Get posts with advanced filtering, sorting, and pagination.
    
    Supports multiple filter combinations and full-text search.
    """
    
    # Build query
    query = db.query(Post).join(User)
    
    # Apply filters
    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%")
            )
        )
    
    if author:
        query = query.filter(User.username == author)
    
    if tags:
        for tag in tags:
            query = query.filter(Post.tags.contains([tag]))
    
    if status:
        query = query.filter(Post.status == status)
    
    if created_after:
        query = query.filter(Post.created_at >= created_after)
    
    if created_before:
        query = query.filter(Post.created_at <= created_before)
    
    # Apply sorting
    sort_field = getattr(Post, sort_by.value)
    if sort_order == SortOrder.DESC:
        query = query.order_by(desc(sort_field))
    else:
        query = query.order_by(asc(sort_field))
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    offset = (page - 1) * size
    posts = query.offset(offset).limit(size).all()
    
    # Calculate pagination metadata
    total_pages = (total + size - 1) // size
    has_next = page < total_pages
    has_prev = page > 1
    
    return PostListResponse(
        posts=[PostResponse.from_orm(post) for post in posts],
        pagination=PaginationResponse(
            page=page,
            size=size,
            total=total,
            total_pages=total_pages,
            has_next=has_next,
            has_prev=has_prev
        )
    )
```

---

### 🏠 Homework: Add Pagination & Filtering

**Task:** Enhance your blog API with advanced features

```python
# Create these enhancements:
# 1. Add search functionality across title and content
# 2. Implement tag-based filtering
# 3. Add date range filtering
# 4. Create sorting by multiple fields
# 5. Add response caching for expensive queries
# 6. Implement user-specific post filtering
# 7. Add analytics endpoints with background processing

# Example endpoints to create:
# GET /posts/search?q=fastapi&tags=python,web&sort=views&order=desc
# GET /posts/analytics/{post_id}
# POST /posts/{post_id}/like (with background analytics update)
# GET /users/{user_id}/posts?status=published&limit=5
```

---

### 📝 Key Takeaways

✅ Dependency Injection = Flexible, testable code architecture
✅ Pydantic Models = Robust data validation and documentation
✅ Background Tasks = Non-blocking operations for better UX  
✅ Auto Documentation = Interactive API docs with examples
✅ Advanced CRUD = Filtering, sorting, pagination out of the box

---

<a name="hour-33"></a>
## 📅 Hour 33: Caching & Performance

### 🎯 Learning Objectives
- Understand different caching strategies and when to use them
- Implement Redis caching for expensive operations
- Optimize database queries and identify bottlenecks
- Use profiling tools to measure performance
- Build a high-performance caching layer

### 📖 What to Teach

**"Today we make our APIs lightning fast with caching and performance optimization!"**

---

### 1️⃣ Caching Strategies (10 minutes)

**Types of Caching:**

```python
# 1. IN-MEMORY CACHING (Simple, fast, limited)
from functools import lru_cache
import time
from typing import Dict, Any

# Simple in-memory cache with LRU
@lru_cache(maxsize=128)
def get_expensive_calculation(number: int) -> int:
    """Expensive calculation with caching"""
    print(f"🔢 Computing factorial of {number}...")
    time.sleep(2)  # Simulate expensive operation
    
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Manual in-memory cache
class InMemoryCache:
    def __init__(self, ttl: int = 300):  # 5 minutes TTL
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = ttl
    
    def get(self, key: str) -> Any:
        if key in self.cache:
            data = self.cache[key]
            if time.time() - data['timestamp'] < self.ttl:
                print(f"💾 Cache HIT: {key}")
                return data['value']
            else:
                print(f"⏰ Cache EXPIRED: {key}")
                del self.cache[key]
        
        print(f"❌ Cache MISS: {key}")
        return None
    
    def set(self, key: str, value: Any) -> None:
        self.cache[key] = {
            'value': value,
            'timestamp': time.time()
        }
        print(f"💾 Cache SET: {key}")
    
    def delete(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
            print(f"🗑️ Cache DELETE: {key}")

# Usage example
cache = InMemoryCache(ttl=60)  # 1 minute TTL

def get_user_profile(user_id: int) -> Dict[str, Any]:
    cache_key = f"user_profile:{user_id}"
    
    # Try cache first
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result
    
    # Simulate database query
    print(f"🗄️ Querying database for user {user_id}")
    time.sleep(1)  # Simulate DB delay
    
    user_data = {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
        "posts_count": user_id * 10
    }
    
    # Cache the result
    cache.set(cache_key, user_data)
    return user_data
```

**Caching Patterns:**

```python
# 2. CACHE-ASIDE PATTERN (Most common)
async def get_post_with_cache_aside(post_id: int, db: Session, cache: RedisCache):
    """Cache-aside pattern implementation"""
    cache_key = f"post:{post_id}"
    
    # 1. Check cache first
    cached_post = await cache.get(cache_key)
    if cached_post:
        return json.loads(cached_post)
    
    # 2. Cache miss - query database
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # 3. Store in cache for next time
    post_data = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username
    }
    
    await cache.set(cache_key, json.dumps(post_data), ttl=300)
    return post_data

# 3. WRITE-THROUGH PATTERN
async def update_post_write_through(post_id: int, update_data: dict, db: Session, cache: RedisCache):
    """Write-through pattern - update DB and cache simultaneously"""
    # 1. Update database
    post = db.query(Post).filter(Post.id == post_id).first()
    for key, value in update_data.items():
        setattr(post, key, value)
    db.commit()
    
    # 2. Update cache immediately
    cache_key = f"post:{post_id}"
    post_data = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username
    }
    
    await cache.set(cache_key, json.dumps(post_data), ttl=300)
    return post_data

# 4. WRITE-BEHIND PATTERN (Advanced)
write_queue = []

async def update_post_write_behind(post_id: int, update_data: dict, cache: RedisCache):
    """Write-behind pattern - update cache immediately, DB later"""
    # 1. Update cache immediately
    cache_key = f"post:{post_id}"
    cached_post = await cache.get(cache_key)
    
    if cached_post:
        post_data = json.loads(cached_post)
        post_data.update(update_data)
        await cache.set(cache_key, json.dumps(post_data), ttl=300)
    
    # 2. Queue database update for later
    write_queue.append({
        "post_id": post_id,
        "update_data": update_data,
        "timestamp": time.time()
    })
    
    return {"message": "Update queued"}
```

---

### 2️⃣ Redis Integration (15 minutes)

**Redis Setup and Configuration:**

```python
# redis_client.py
import redis.asyncio as redis
import json
import pickle
from typing import Any, Optional, Union
from datetime import timedelta
import asyncio

class RedisCache:
    def __init__(self, url: str = "redis://localhost:6379/0"):
        self.redis = redis.from_url(url, decode_responses=True)
    
    async def get(self, key: str) -> Optional[str]:
        """Get value from cache"""
        try:
            value = await self.redis.get(key)
            if value:
                print(f"💾 Redis HIT: {key}")
                return value
            print(f"❌ Redis MISS: {key}")
            return None
        except Exception as e:
            print(f"🚫 Redis GET error: {e}")
            return None
    
    async def set(self, key: str, value: str, ttl: int = 300) -> bool:
        """Set value in cache with TTL"""
        try:
            await self.redis.setex(key, ttl, value)
            print(f"💾 Redis SET: {key} (TTL: {ttl}s)")
            return True
        except Exception as e:
            print(f"🚫 Redis SET error: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache"""
        try:
            result = await self.redis.delete(key)
            print(f"🗑️ Redis DELETE: {key}")
            return bool(result)
        except Exception as e:
            print(f"🚫 Redis DELETE error: {e}")
            return False
    
    async def get_json(self, key: str) -> Optional[dict]:
        """Get and deserialize JSON value"""
        value = await self.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                print(f"🚫 Invalid JSON in cache: {key}")
                await self.delete(key)
        return None
    
    async def set_json(self, key: str, value: dict, ttl: int = 300) -> bool:
        """Serialize and set JSON value"""
        try:
            json_str = json.dumps(value)
            return await self.set(key, json_str, ttl)
        except (TypeError, ValueError) as e:
            print(f"🚫 JSON serialization error: {e}")
            return False
    
    async def increment(self, key: str, amount: int = 1) -> int:
        """Increment a counter"""
        try:
            result = await self.redis.incrby(key, amount)
            print(f"➕ Redis INCREMENT: {key} by {amount} = {result}")
            return result
        except Exception as e:
            print(f"🚫 Redis INCREMENT error: {e}")
            return 0
    
    async def expire(self, key: str, ttl: int) -> bool:
        """Set expiration for existing key"""
        try:
            result = await self.redis.expire(key, ttl)
            return bool(result)
        except Exception as e:
            print(f"🚫 Redis EXPIRE error: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Check if key exists"""
        try:
            result = await self.redis.exists(key)
            return bool(result)
        except Exception as e:
            print(f"🚫 Redis EXISTS error: {e}")
            return False
    
    async def flush_pattern(self, pattern: str) -> int:
        """Delete all keys matching pattern"""
        try:
            keys = await self.redis.keys(pattern)
            if keys:
                result = await self.redis.delete(*keys)
                print(f"🗑️ Redis FLUSH: {len(keys)} keys matching '{pattern}'")
                return result
            return 0
        except Exception as e:
            print(f"🚫 Redis FLUSH error: {e}")
            return 0

# Initialize Redis cache
cache = RedisCache()
```

**FastAPI Integration with Redis:**

```python
# cached_api.py
from fastapi import FastAPI, Depends, HTTPException, Query
from redis_client import RedisCache
import json
import hashlib
from typing import List, Optional
import time

app = FastAPI(title="Cached Blog API")

# Cache dependency
async def get_cache() -> RedisCache:
    return RedisCache()

# Cache decorator
def cache_response(ttl: int = 300):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            # Generate cache key from function name and arguments
            cache_data = {
                "func": func.__name__,
                "args": args,
                "kwargs": {k: v for k, v in kwargs.items() if k != 'cache'}
            }
            cache_key = f"api:{hashlib.md5(json.dumps(cache_data, sort_keys=True).encode()).hexdigest()}"
            
            # Try cache first
            cache = await get_cache()
            cached_result = await cache.get_json(cache_key)
            if cached_result:
                return cached_result
            
            # Execute function and cache result
            result = await func(*args, **kwargs)
            await cache.set_json(cache_key, result, ttl)
            
            return result
        return wrapper
    return decorator

@app.get("/posts/{post_id}")
@cache_response(ttl=300)  # 5 minutes
async def get_post_cached(post_id: int, cache: RedisCache = Depends(get_cache)):
    """Get post with caching"""
    # Simulate database query
    await asyncio.sleep(1)  # Simulate slow DB
    
    post_data = {
        "id": post_id,
        "title": f"Post {post_id}",
        "content": f"This is the content of post {post_id}",
        "views": post_id * 100,
        "cached_at": time.time()
    }
    
    return post_data

@app.get("/posts")
async def get_posts_with_cache(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    tag: Optional[str] = None,
    cache: RedisCache = Depends(get_cache)
):
    """Get posts with intelligent caching"""
    
    # Create cache key based on parameters
    cache_params = {"page": page, "size": size, "tag": tag}
    cache_key = f"posts:list:{hashlib.md5(json.dumps(cache_params, sort_keys=True).encode()).hexdigest()}"
    
    # Try cache first
    cached_posts = await cache.get_json(cache_key)
    if cached_posts:
        cached_posts["from_cache"] = True
        return cached_posts
    
    # Simulate database query
    print(f"🗄️ Querying database: page={page}, size={size}, tag={tag}")
    await asyncio.sleep(2)  # Simulate slow query
    
    # Generate fake data
    start_id = (page - 1) * size + 1
    posts = []
    
    for i in range(start_id, start_id + size):
        posts.append({
            "id": i,
            "title": f"Post {i}",
            "content": f"Content for post {i}",
            "tag": tag if tag else f"tag{i % 5}",
            "views": i * 50
        })
    
    result = {
        "posts": posts,
        "page": page,
        "size": size,
        "total": 1000,  # Fake total
        "from_cache": False
    }
    
    # Cache for 2 minutes (shorter for list endpoints)
    await cache.set_json(cache_key, result, ttl=120)
    
    return result

@app.post("/posts/{post_id}/view")
async def increment_post_views(post_id: int, cache: RedisCache = Depends(get_cache)):
    """Increment post views with Redis counter"""
    
    # Increment view counter
    view_key = f"post:views:{post_id}"
    new_count = await cache.increment(view_key, 1)
    
    # Set expiration if this is a new key
    if new_count == 1:
        await cache.expire(view_key, 86400)  # Expire in 24 hours
    
    # Invalidate cached post data
    await cache.flush_pattern(f"api:*post_id*{post_id}*")
    
    return {
        "post_id": post_id,
        "views": new_count,
        "message": "View count updated"
    }

@app.delete("/cache/{pattern}")
async def clear_cache(pattern: str, cache: RedisCache = Depends(get_cache)):
    """Clear cache by pattern (admin endpoint)"""
    deleted_count = await cache.flush_pattern(pattern)
    
    return {
        "message": f"Cleared {deleted_count} cache entries",
        "pattern": pattern
    }

# Advanced caching with cache warming
@app.post("/cache/warm")
async def warm_cache(cache: RedisCache = Depends(get_cache)):
    """Warm up cache with popular content"""
    print("🔥 Warming up cache...")
    
    # Pre-load popular posts
    popular_post_ids = [1, 2, 3, 4, 5]
    
    for post_id in popular_post_ids:
        # Simulate loading post data
        post_data = {
            "id": post_id,
            "title": f"Popular Post {post_id}",
            "content": f"This is a popular post {post_id}",
            "views": post_id * 1000
        }
        
        cache_key = f"post:{post_id}"
        await cache.set_json(cache_key, post_data, ttl=600)  # 10 minutes
    
    # Pre-load first page of posts
    first_page_data = {
        "posts": [{"id": i, "title": f"Post {i}"} for i in range(1, 11)],
        "page": 1,
        "size": 10,
        "total": 1000
    }
    
    await cache.set_json("posts:list:page_1", first_page_data, ttl=300)
    
    return {"message": f"Cache warmed with {len(popular_post_ids) + 1} items"}
```

---

### 3️⃣ Database Query Optimization (15 minutes)

**Query Performance Analysis:**

```python
# query_optimization.py
import time
import asyncio
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import logging

# Enable SQL logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class QueryProfiler:
    def __init__(self):
        self.queries = []
    
    def profile_query(self, description: str = ""):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                result = await func(*args, **kwargs)
                end_time = time.time()
                
                execution_time = end_time - start_time
                self.queries.append({
                    "description": description or func.__name__,
                    "execution_time": execution_time,
                    "timestamp": start_time
                })
                
                if execution_time > 1.0:  # Slow query threshold
                    print(f"🐌 SLOW QUERY: {description} took {execution_time:.3f}s")
                else:
                    print(f"⚡ Query: {description} took {execution_time:.3f}s")
                
                return result
            return wrapper
        return decorator
    
    def get_report(self):
        if not self.queries:
            return "No queries recorded"
        
        total_time = sum(q["execution_time"] for q in self.queries)
        avg_time = total_time / len(self.queries)
        slowest = max(self.queries, key=lambda q: q["execution_time"])
        
        report = f"""
📊 QUERY PERFORMANCE REPORT
================================
Total Queries: {len(self.queries)}
Total Time: {total_time:.3f}s
Average Time: {avg_time:.3f}s
Slowest Query: {slowest['description']} ({slowest['execution_time']:.3f}s)

Query Details:
"""
        for i, query in enumerate(self.queries, 1):
            report += f"{i}. {query['description']}: {query['execution_time']:.3f}s\n"
        
        return report

profiler = QueryProfiler()

# BAD: N+1 Query Problem
@profiler.profile_query("Bad: N+1 queries for posts with authors")
async def get_posts_bad_way(db: Session, limit: int = 10):
    """Demonstrates N+1 query problem"""
    
    # 1 query to get posts
    posts = db.query(Post).limit(limit).all()
    
    result = []
    for post in posts:
        # N queries to get authors (one for each post)
        author = db.query(User).filter(User.id == post.author_id).first()
        result.append({
            "id": post.id,
            "title": post.title,
            "author_name": author.username if author else "Unknown"
        })
    
    return result

# GOOD: Eager Loading with JOIN
@profiler.profile_query("Good: Single query with JOIN")
async def get_posts_good_way(db: Session, limit: int = 10):
    """Optimized with eager loading"""
    
    # Single query with JOIN
    posts = (
        db.query(Post, User.username)
        .join(User, Post.author_id == User.id)
        .limit(limit)
        .all()
    )
    
    return [
        {
            "id": post.id,
            "title": post.title,
            "author_name": username
        }
        for post, username in posts
    ]

# BETTER: Optimized query with specific fields
@profiler.profile_query("Better: Optimized field selection")
async def get_posts_optimized(db: Session, limit: int = 10):
    """Optimized with specific field selection"""
    
    # Select only needed fields
    result = (
        db.query(
            Post.id,
            Post.title,
            Post.created_at,
            User.username.label('author_name')
        )
        .join(User, Post.author_id == User.id)
        .filter(Post.status == 'published')  # Add index on status
        .order_by(Post.created_at.desc())    # Add index on created_at
        .limit(limit)
        .all()
    )
    
    return [
        {
            "id": row.id,
            "title": row.title,
            "author_name": row.author_name,
            "created_at": row.created_at.isoformat()
        }
        for row in result
    ]

# Database indexing examples
async def create_performance_indexes(db: Session):
    """Create indexes for better performance"""
    
    indexes = [
        # Index on frequently queried columns
        "CREATE INDEX IF NOT EXISTS idx_posts_status ON posts(status)",
        "CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at)",
        "CREATE INDEX IF NOT EXISTS idx_posts_author_id ON posts(author_id)",
        
        # Composite indexes for common query combinations
        "CREATE INDEX IF NOT EXISTS idx_posts_status_created ON posts(status, created_at DESC)",
        "CREATE INDEX IF NOT EXISTS idx_posts_author_status ON posts(author_id, status)",
        
        # Index on search fields (if using text search)
        "CREATE INDEX IF NOT EXISTS idx_posts_title_gin ON posts USING gin(to_tsvector('english', title))",
        
        # Index on foreign keys
        "CREATE INDEX IF NOT EXISTS idx_comments_post_id ON comments(post_id)",
        "CREATE INDEX IF NOT EXISTS idx_comments_author_id ON comments(author_id)"
    ]
    
    for index_sql in indexes:
        try:
            await db.execute(text(index_sql))
            print(f"✅ Created index: {index_sql}")
        except Exception as e:
            print(f"❌ Index creation failed: {e}")
    
    await db.commit()

# Query caching with database-level cache
class QueryCache:
    def __init__(self, redis_cache: RedisCache):
        self.cache = redis_cache
    
    async def cached_query(self, query_key: str, query_func, ttl: int = 300):
        """Execute query with caching"""
        
        # Try cache first
        cached_result = await self.cache.get_json(f"query:{query_key}")
        if cached_result:
            return cached_result
        
        # Execute query
        start_time = time.time()
        result = await query_func()
        execution_time = time.time() - start_time
        
        # Cache the result
        cache_data = {
            "data": result,
            "execution_time": execution_time,
            "cached_at": time.time()
        }
        
        await self.cache.set_json(f"query:{query_key}", cache_data, ttl)
        
        print(f"💾 Cached query '{query_key}' (execution: {execution_time:.3f}s)")
        return cache_data

# Usage in FastAPI endpoints
@app.get("/posts/popular")
async def get_popular_posts(
    cache: RedisCache = Depends(get_cache),
    db: Session = Depends(get_database)
):
    """Get popular posts with query caching"""
    
    query_cache = QueryCache(cache)
    
    async def expensive_query():
        # Complex query that takes time
        result = await db.execute(text("""
            SELECT 
                p.id,
                p.title,
                p.content,
                u.username as author_name,
                COUNT(DISTINCT c.id) as comment_count,
                COUNT(DISTINCT l.id) as like_count,
                AVG(r.rating) as avg_rating
            FROM posts p
            JOIN users u ON p.author_id = u.id
            LEFT JOIN comments c ON p.id = c.post_id
            LEFT JOIN likes l ON p.id = l.post_id
            LEFT JOIN ratings r ON p.id = r.post_id
            WHERE p.status = 'published'
              AND p.created_at > NOW() - INTERVAL '30 days'
            GROUP BY p.id, p.title, p.content, u.username
            HAVING COUNT(DISTINCT c.id) > 5 OR COUNT(DISTINCT l.id) > 10
            ORDER BY (COUNT(DISTINCT c.id) + COUNT(DISTINCT l.id)) DESC
            LIMIT 10
        """))
        
        return [dict(row) for row in result]
    
    # Use cached query
    cache_result = await query_cache.cached_query(
        "popular_posts_30days", 
        expensive_query, 
        ttl=1800  # 30 minutes
    )
    
    return {
        "posts": cache_result["data"],
        "from_cache": "cached_at" in cache_result,
        "execution_time": cache_result.get("execution_time", 0)
    }
```

---

### 4️⃣ Performance Profiling (10 minutes)

**Application Profiling Tools:**

```python
# profiler.py
import cProfile
import pstats
import io
from functools import wraps
import time
import psutil
import tracemalloc
from fastapi import FastAPI, Request
from contextual import middleware
import asyncio

class PerformanceProfiler:
    def __init__(self):
        self.request_times = []
        self.memory_usage = []
        
    def profile_endpoint(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Memory profiling
            tracemalloc.start()
            process = psutil.Process()
            memory_before = process.memory_info().rss / 1024 / 1024  # MB
            
            # Time profiling
            start_time = time.time()
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Calculate metrics
            end_time = time.time()
            execution_time = end_time - start_time
            
            memory_after = process.memory_info().rss / 1024 / 1024  # MB
            memory_diff = memory_after - memory_before
            
            # Memory trace
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            # Log performance data
            perf_data = {
                "function": func.__name__,
                "execution_time": execution_time,
                "memory_before": memory_before,
                "memory_after": memory_after,
                "memory_diff": memory_diff,
                "memory_peak": peak / 1024 / 1024,  # MB
                "timestamp": start_time
            }
            
            self.request_times.append(perf_data)
            
            # Print warnings for slow operations
            if execution_time > 1.0:
                print(f"🐌 SLOW OPERATION: {func.__name__} took {execution_time:.3f}s")
            
            if memory_diff > 50:  # More than 50MB increase
                print(f"🧠 HIGH MEMORY: {func.__name__} used {memory_diff:.1f}MB extra")
            
            return result
        
        return wrapper
    
    def get_stats(self):
        if not self.request_times:
            return {"message": "No performance data available"}
        
        execution_times = [r["execution_time"] for r in self.request_times]
        memory_diffs = [r["memory_diff"] for r in self.request_times]
        
        return {
            "total_requests": len(self.request_times),
            "avg_execution_time": sum(execution_times) / len(execution_times),
            "max_execution_time": max(execution_times),
            "min_execution_time": min(execution_times),
            "avg_memory_usage": sum(memory_diffs) / len(memory_diffs),
            "max_memory_usage": max(memory_diffs),
            "recent_requests": self.request_times[-10:]  # Last 10 requests
        }

# Global profiler instance
profiler = PerformanceProfiler()

# FastAPI middleware for automatic profiling
@middleware("http")
async def performance_middleware(request: Request, call_next):
    start_time = time.time()
    
    # Memory tracking
    process = psutil.Process()
    memory_before = process.memory_info().rss / 1024 / 1024
    
    # Process request
    response = await call_next(request)
    
    # Calculate metrics
    end_time = time.time()
    execution_time = end_time - start_time
    memory_after = process.memory_info().rss / 1024 / 1024
    
    # Add performance headers
    response.headers["X-Response-Time"] = f"{execution_time:.3f}s"
    response.headers["X-Memory-Usage"] = f"{memory_after - memory_before:.1f}MB"
    
    # Log slow requests
    if execution_time > 2.0:
        print(f"🐌 SLOW REQUEST: {request.method} {request.url} took {execution_time:.3f}s")
    
    return response

# CPU Profiling decorator
def cpu_profile(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        
        result = await func(*args, **kwargs)
        
        profiler.disable()
        
        # Generate profile report
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s)
        ps.sort_stats('cumulative')
        ps.print_stats(10)  # Top 10 functions
        
        print(f"\n📊 CPU PROFILE for {func.__name__}:")
        print(s.getvalue())
        
        return result
    
    return wrapper

# Memory leak detection
class MemoryTracker:
    def __init__(self):
        self.snapshots = []
    
    async def take_snapshot(self, description: str):
        """Take memory snapshot"""
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        
        snapshot = tracemalloc.take_snapshot()
        self.snapshots.append({
            "description": description,
            "snapshot": snapshot,
            "timestamp": time.time()
        })
    
    def compare_snapshots(self, index1: int = -2, index2: int = -1):
        """Compare two snapshots to detect memory leaks"""
        if len(self.snapshots) < 2:
            return "Need at least 2 snapshots to compare"
        
        snap1 = self.snapshots[index1]["snapshot"]
        snap2 = self.snapshots[index2]["snapshot"]
        
        top_stats = snap2.compare_to(snap1, 'lineno')
        
        print(f"\n🧠 MEMORY COMPARISON:")
        print(f"From: {self.snapshots[index1]['description']}")
        print(f"To: {self.snapshots[index2]['description']}")
        print("\nTop 10 memory differences:")
        
        for stat in top_stats[:10]:
            print(stat)
        
        return top_stats

# Usage examples
memory_tracker = MemoryTracker()

@app.get("/profile/start")
async def start_profiling():
    """Start memory profiling"""
    await memory_tracker.take_snapshot("Profiling started")
    return {"message": "Memory profiling started"}

@app.get("/profile/snapshot/{description}")
async def take_snapshot(description: str):
    """Take memory snapshot"""
    await memory_tracker.take_snapshot(description)
    return {"message": f"Snapshot taken: {description}"}

@app.get("/profile/compare")
async def compare_memory():
    """Compare memory snapshots"""
    stats = memory_tracker.compare_snapshots()
    return {"message": "Memory comparison complete - check logs"}

@app.get("/profile/stats")
async def get_performance_stats():
    """Get performance statistics"""
    return profiler.get_stats()

# Load testing endpoint
@app.get("/test/load/{num_requests}")
async def simulate_load(num_requests: int):
    """Simulate load for testing"""
    
    @profiler.profile_endpoint
    async def simulate_work():
        # Simulate CPU work
        result = sum(i * i for i in range(1000))
        
        # Simulate I/O work
        await asyncio.sleep(0.1)
        
        # Simulate memory allocation
        data = [i for i in range(1000)]
        
        return result
    
    start_time = time.time()
    
    # Run concurrent requests
    tasks = [simulate_work() for _ in range(num_requests)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    return {
        "num_requests": num_requests,
        "total_time": end_time - start_time,
        "requests_per_second": num_requests / (end_time - start_time),
        "avg_response_time": (end_time - start_time) / num_requests
    }
```

---

### 5️⃣ Production Caching Setup (5 minutes)

**Production Configuration:**

```python
# production_cache.py
import os
from typing import Optional
import redis.asyncio as redis
from fastapi import FastAPI
import json
import hashlib

class ProductionCache:
    def __init__(self):
        # Environment-based configuration
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.redis = redis.from_url(redis_url, 
                                   decode_responses=True,
                                   max_connections=20,
                                   retry_on_timeout=True)
        
        # Cache configuration
        self.default_ttl = int(os.getenv("CACHE_DEFAULT_TTL", "300"))
        self.enabled = os.getenv("CACHE_ENABLED", "true").lower() == "true"
        
    async def health_check(self) -> bool:
        """Check cache health"""
        try:
            await self.redis.ping()
            return True
        except Exception:
            return False
    
    async def get_or_set(self, key: str, fetch_func, ttl: Optional[int] = None):
        """Get from cache or fetch and set"""
        if not self.enabled:
            return await fetch_func()
        
        # Try cache first
        cached = await self.get_json(key)
        if cached:
            return cached
        
        # Fetch and cache
        data = await fetch_func()
        await self.set_json(key, data, ttl or self.default_ttl)
        return data

# Environment-specific cache settings
CACHE_SETTINGS = {
    "development": {
        "redis_url": "redis://localhost:6379/0",
        "default_ttl": 60,  # Short TTL for development
        "enabled": True
    },
    "production": {
        "redis_url": os.getenv("REDIS_URL"),
        "default_ttl": 300,
        "enabled": True
    },
    "testing": {
        "redis_url": "redis://localhost:6379/15",  # Different DB for tests
        "default_ttl": 10,
        "enabled": False  # Disable caching in tests
    }
}

# Cache warming for production
async def warm_production_cache():
    """Warm up cache with essential data"""
    cache = ProductionCache()
    
    warming_tasks = [
        # Popular posts
        warm_popular_posts(cache),
        # User profiles  
        warm_user_profiles(cache),
        # Category data
        warm_categories(cache),
        # Static content
        warm_static_content(cache)
    ]
    
    await asyncio.gather(*warming_tasks)
    print("🔥 Production cache warming complete!")

async def warm_popular_posts(cache: ProductionCache):
    """Warm popular posts cache"""
    # Implementation here
    pass
```

---

### 🏠 Homework: Profile and Optimize

**Task:** Add Redis caching to expensive endpoint and optimize performance

```python
# Performance optimization challenge:

# 1. Add Redis caching to your blog API
# 2. Implement cache invalidation strategy
# 3. Profile a slow endpoint and optimize it
# 4. Add performance monitoring middleware
# 5. Create cache warming script
# 6. Implement cache-aside pattern
# 7. Add memory leak detection

# Deliverables:
# - Before/after performance benchmarks
# - Cache hit rate analysis  
# - Query optimization report
# - Memory usage analysis
```

---

### 📝 Key Takeaways

✅ Caching = Dramatic performance improvement for I/O operations
✅ Redis = Distributed caching for production applications
✅ Query optimization = Use indexes, avoid N+1 problems
✅ Profiling = Measure first, optimize second
✅ Cache strategies = Choose the right pattern for your use case

---

<a name="hour-34"></a>
## 📅 Hour 34: Message Queues & Background Processing

### 🎯 Learning Objectives
- Understand message queues and when to use them
- Implement background job processing with Celery
- Handle task retries, failures, and monitoring
- Build scalable asynchronous processing systems
- Create email notifications and file processing tasks

### 📖 What to Teach

**"Today we learn to handle heavy work in the background while keeping our API responses fast!"**

---

### 1️⃣ Message Queue Concepts (10 minutes)

**Why Message Queues?**

```python
# WITHOUT MESSAGE QUEUES (Bad for user experience)
@app.post("/send-newsletter")
async def send_newsletter_bad(emails: List[str], content: str):
    """Bad: Blocks the request until all emails are sent"""
    
    start_time = time.time()
    
    # This blocks the HTTP request for minutes!
    for email in emails:  # Could be 10,000 emails!
        await send_email(email, content)  # 2 seconds each = 20,000 seconds!
        
    end_time = time.time()
    
    return {
        "message": f"Newsletter sent to {len(emails)} recipients",
        "time_taken": f"{end_time - start_time:.1f} seconds"
    }

# WITH MESSAGE QUEUES (Good user experience)
@app.post("/send-newsletter")
async def send_newsletter_good(emails: List[str], content: str):
    """Good: Returns immediately, work happens in background"""
    
    # Queue the work for background processing
    task = send_newsletter_task.delay(emails, content)
    
    return {
        "message": f"Newsletter queued for {len(emails)} recipients",
        "task_id": task.id,
        "status": "processing"
    }
```

**Message Queue Components:**

```
Producer → Queue → Consumer(s)
   ↓         ↓         ↓
 FastAPI   Redis    Celery Worker(s)

Flow:
1. FastAPI receives request
2. Creates job and adds to queue
3. Returns immediately to user
4. Worker picks up job from queue
5. Worker processes job in background
6. Results stored (database, cache, etc.)
```

**Real-World Use Cases:**
- ✅ **Email notifications** (newsletters, confirmations)
- ✅ **Image processing** (resizing, thumbnails, filters)
- ✅ **Report generation** (PDF creation, data exports)
- ✅ **Data synchronization** (third-party API sync)
- ✅ **Cleanup tasks** (log rotation, temporary file deletion)

---

### 2️⃣ Celery Setup and Configuration (15 minutes)

**Install Celery and Redis:**

```bash
pip install celery redis flower
# flower is for monitoring Celery tasks
```

**Celery Configuration:**

```python
# celery_app.py
from celery import Celery
import os
from kombu import Queue

# Celery configuration
celery_app = Celery(
    "blog_worker",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
    include=["tasks.email_tasks", "tasks.image_tasks", "tasks.report_tasks"]
)

# Configuration settings
celery_app.conf.update(
    # Task routing
    task_routes={
        'tasks.email_tasks.*': {'queue': 'email'},
        'tasks.image_tasks.*': {'queue': 'images'},
        'tasks.report_tasks.*': {'queue': 'reports'},
    },
    
    # Queue definitions
    task_queues=(
        Queue('email', routing_key='email'),
        Queue('images', routing_key='images'),
        Queue('reports', routing_key='reports'),
        Queue('default', routing_key='default'),
    ),
    
    # Task settings
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    
    # Result backend settings
    result_expires=3600,  # 1 hour
    
    # Worker settings
    worker_prefetch_multiplier=1,
    task_acks_late=True,
    
    # Retry settings
    task_default_retry_delay=60,  # 1 minute
    task_max_retries=3,
    
    # Rate limiting
    task_annotations={
        'tasks.email_tasks.send_email': {'rate_limit': '10/m'},  # 10 emails per minute
        'tasks.image_tasks.process_image': {'rate_limit': '5/m'},  # 5 images per minute
    }
)

# Beat scheduler for periodic tasks
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    # Daily cleanup task
    'cleanup-temp-files': {
        'task': 'tasks.cleanup_tasks.cleanup_temp_files',
        'schedule': crontab(hour=2, minute=0),  # 2 AM daily
    },
    
    # Weekly report generation
    'weekly-analytics-report': {
        'task': 'tasks.report_tasks.generate_weekly_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),  # 9 AM Monday
    },
    
    # Hourly health check
    'health-check': {
        'task': 'tasks.monitoring_tasks.health_check',
        'schedule': crontab(minute=0),  # Every hour
    },
}
```

**Task Implementation:**

```python
# tasks/email_tasks.py
from celery import current_task
from celery.exceptions import Retry
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import logging
from typing import List
import requests

logger = logging.getLogger(__name__)

@celery_app.task(bind=True, max_retries=3)
def send_email(self, to_email: str, subject: str, body: str, html_body: str = None):
    """Send a single email with retry logic"""
    
    try:
        # Update task progress
        self.update_state(state='PROGRESS', meta={'step': 'connecting'})
        
        # Email configuration
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_username = os.getenv("SMTP_USERNAME")
        smtp_password = os.getenv("SMTP_PASSWORD")
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = to_email
        
        # Add text content
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Add HTML content if provided
        if html_body:
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)
        
        # Update progress
        self.update_state(state='PROGRESS', meta={'step': 'sending'})
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        
        logger.info(f"✅ Email sent successfully to {to_email}")
        
        return {
            'status': 'success',
            'to_email': to_email,
            'subject': subject,
            'sent_at': time.time()
        }
        
    except smtplib.SMTPException as e:
        logger.error(f"❌ SMTP error sending email to {to_email}: {str(e)}")
        
        # Retry with exponential backoff
        countdown = 60 * (2 ** self.request.retries)  # 60s, 120s, 240s
        
        raise self.retry(countdown=countdown, exc=e)
        
    except Exception as e:
        logger.error(f"❌ Unexpected error sending email to {to_email}: {str(e)}")
        
        # Don't retry on unexpected errors
        return {
            'status': 'failed',
            'to_email': to_email,
            'error': str(e),
            'failed_at': time.time()
        }

@celery_app.task(bind=True)
def send_bulk_emails(self, email_list: List[dict], template: str):
    """Send emails to multiple recipients with progress tracking"""
    
    total_emails = len(email_list)
    sent_count = 0
    failed_count = 0
    results = []
    
    for i, email_data in enumerate(email_list):
        try:
            # Update overall progress
            progress = int((i / total_emails) * 100)
            self.update_state(
                state='PROGRESS',
                meta={
                    'current': i,
                    'total': total_emails,
                    'progress': progress,
                    'sent': sent_count,
                    'failed': failed_count
                }
            )
            
            # Send individual email
            result = send_email.delay(
                email_data['email'],
                email_data['subject'],
                template.format(**email_data.get('variables', {}))
            )
            
            # Wait for result (or use result.get() for synchronous)
            email_result = result.get(timeout=30)
            
            if email_result['status'] == 'success':
                sent_count += 1
            else:
                failed_count += 1
            
            results.append(email_result)
            
        except Exception as e:
            failed_count += 1
            results.append({
                'status': 'failed',
                'to_email': email_data['email'],
                'error': str(e)
            })
            
            logger.error(f"Error in bulk email {i}: {str(e)}")
    
    return {
        'total_emails': total_emails,
        'sent_count': sent_count,
        'failed_count': failed_count,
        'results': results,
        'completed_at': time.time()
    }

@celery_app.task
def send_newsletter(subscriber_emails: List[str], newsletter_content: str):
    """Send newsletter to all subscribers"""
    
    logger.info(f"📧 Starting newsletter send to {len(subscriber_emails)} subscribers")
    
    # Prepare email data
    email_jobs = []
    for email in subscriber_emails:
        email_jobs.append({
            'email': email,
            'subject': 'Weekly Newsletter - Blog Updates',
            'variables': {'subscriber_email': email}
        })
    
    # Use bulk email task
    result = send_bulk_emails.delay(email_jobs, newsletter_content)
    
    return {
        'newsletter_task_id': result.id,
        'subscriber_count': len(subscriber_emails),
        'status': 'processing'
    }
```

**Image Processing Tasks:**

```python
# tasks/image_tasks.py
from PIL import Image
import os
import boto3
from io import BytesIO
import requests
import hashlib

@celery_app.task(bind=True, max_retries=3)
def process_uploaded_image(self, image_path: str, user_id: int):
    """Process uploaded image: resize, create thumbnails, upload to S3"""
    
    try:
        self.update_state(state='PROGRESS', meta={'step': 'loading_image'})
        
        # Load image
        with Image.open(image_path) as img:
            original_size = img.size
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Generate different sizes
            sizes = {
                'thumbnail': (150, 150),
                'medium': (500, 500),
                'large': (1200, 1200)
            }
            
            processed_images = {}
            
            for size_name, dimensions in sizes.items():
                self.update_state(
                    state='PROGRESS', 
                    meta={'step': f'creating_{size_name}', 'progress': 25}
                )
                
                # Resize image
                resized_img = img.copy()
                resized_img.thumbnail(dimensions, Image.Resampling.LANCZOS)
                
                # Save to buffer
                buffer = BytesIO()
                resized_img.save(buffer, format='JPEG', quality=85, optimize=True)
                buffer.seek(0)
                
                # Generate filename
                filename = f"user_{user_id}_{size_name}_{int(time.time())}.jpg"
                
                # Upload to S3 (or save locally)
                s3_url = upload_to_s3(buffer, filename)
                
                processed_images[size_name] = {
                    'url': s3_url,
                    'size': resized_img.size,
                    'filename': filename
                }
            
            self.update_state(state='PROGRESS', meta={'step': 'cleanup', 'progress': 90})
            
            # Cleanup original file
            os.remove(image_path)
            
            return {
                'status': 'success',
                'original_size': original_size,
                'processed_images': processed_images,
                'user_id': user_id,
                'processed_at': time.time()
            }
            
    except Exception as e:
        logger.error(f"❌ Image processing failed: {str(e)}")
        
        # Retry with backoff
        countdown = 30 * (2 ** self.request.retries)
        raise self.retry(countdown=countdown, exc=e)

def upload_to_s3(file_buffer: BytesIO, filename: str) -> str:
    """Upload file to S3 and return URL"""
    
    # S3 configuration
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION', 'us-east-1')
    )
    
    bucket_name = os.getenv('S3_BUCKET_NAME')
    
    try:
        # Upload file
        s3_client.upload_fileobj(
            file_buffer,
            bucket_name,
            filename,
            ExtraArgs={
                'ContentType': 'image/jpeg',
                'CacheControl': 'max-age=31536000',  # 1 year
            }
        )
        
        # Return public URL
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"
        return s3_url
        
    except Exception as e:
        logger.error(f"❌ S3 upload failed: {str(e)}")
        
        # Fallback: save locally
        local_path = f"uploads/{filename}"
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f:
            file_buffer.seek(0)
            f.write(file_buffer.read())
        
        return f"/uploads/{filename}"

@celery_app.task
def generate_image_thumbnails_batch(image_urls: List[str]):
    """Generate thumbnails for multiple images"""
    
    results = []
    
    for url in image_urls:
        try:
            # Download image
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Process image
            task = process_uploaded_image.delay(url, 0)  # user_id=0 for batch
            result = task.get(timeout=60)
            
            results.append({
                'original_url': url,
                'status': 'success',
                'thumbnails': result['processed_images']
            })
            
        except Exception as e:
            results.append({
                'original_url': url,
                'status': 'failed',
                'error': str(e)
            })
    
    return results
```

---

### 3️⃣ Task Monitoring and Retry Logic (15 minutes)

**Advanced Task Management:**

```python
# tasks/monitoring_tasks.py
import psutil
import subprocess
from datetime import datetime, timedelta

@celery_app.task(bind=True)
def long_running_task(self, duration: int):
    """Example long-running task with progress updates"""
    
    total_steps = duration
    
    for i in range(total_steps):
        # Simulate work
        time.sleep(1)
        
        # Update progress
        progress = int((i / total_steps) * 100)
        self.update_state(
            state='PROGRESS',
            meta={
                'current': i,
                'total': total_steps,
                'progress': progress,
                'message': f'Processing step {i+1} of {total_steps}'
            }
        )
    
    return {
        'status': 'completed',
        'duration': duration,
        'completed_at': time.time()
    }

@celery_app.task(bind=True, max_retries=5)
def unreliable_api_call(self, api_url: str, payload: dict):
    """Task that calls unreliable external API with smart retry logic"""
    
    try:
        self.update_state(state='PROGRESS', meta={'step': 'making_request'})
        
        response = requests.post(
            api_url, 
            json=payload, 
            timeout=30,
            headers={'User-Agent': 'Blog-API/1.0'}
        )
        
        # Different retry logic based on status code
        if response.status_code == 429:  # Rate limited
            # Longer retry for rate limiting
            retry_after = int(response.headers.get('Retry-After', 60))
            logger.warning(f"⏳ Rate limited, retrying after {retry_after}s")
            raise self.retry(countdown=retry_after)
        
        elif response.status_code >= 500:  # Server error
            # Exponential backoff for server errors
            countdown = 30 * (2 ** self.request.retries)
            logger.warning(f"🔄 Server error {response.status_code}, retrying in {countdown}s")
            raise self.retry(countdown=countdown)
        
        elif response.status_code == 400:  # Client error
            # Don't retry client errors
            logger.error(f"❌ Client error {response.status_code}: {response.text}")
            return {
                'status': 'failed',
                'error': 'Client error - not retrying',
                'response_code': response.status_code,
                'response_text': response.text
            }
        
        response.raise_for_status()
        
        return {
            'status': 'success',
            'response_data': response.json(),
            'response_code': response.status_code,
            'completed_at': time.time()
        }
        
    except requests.RequestException as e:
        logger.error(f"❌ Request failed: {str(e)}")
        
        # Final attempt reached
        if self.request.retries >= self.max_retries:
            return {
                'status': 'failed',
                'error': str(e),
                'retries_exhausted': True,
                'failed_at': time.time()
            }
        
        # Retry with backoff
        countdown = 15 * (2 ** self.request.retries)
        raise self.retry(countdown=countdown, exc=e)

@celery_app.task
def health_check():
    """System health check task"""
    
    health_data = {
        'timestamp': datetime.now().isoformat(),
        'system': {},
        'services': {},
        'celery': {}
    }
    
    # System metrics
    health_data['system'] = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else None
    }
    
    # Service checks
    services = ['redis', 'postgresql']
    for service in services:
        try:
            result = subprocess.run(['systemctl', 'is-active', service], 
                                  capture_output=True, text=True, timeout=5)
            health_data['services'][service] = {
                'status': 'active' if result.returncode == 0 else 'inactive',
                'output': result.stdout.strip()
            }
        except Exception as e:
            health_data['services'][service] = {
                'status': 'error',
                'error': str(e)
            }
    
    # Celery worker stats
    inspect = celery_app.control.inspect()
    try:
        stats = inspect.stats()
        active = inspect.active()
        
        health_data['celery'] = {
            'workers': len(stats) if stats else 0,
            'active_tasks': sum(len(tasks) for tasks in active.values()) if active else 0,
            'worker_stats': stats
        }
    except Exception as e:
        health_data['celery'] = {
            'error': str(e)
        }
    
    # Log health status
    logger.info(f"🏥 Health check completed: {json.dumps(health_data, indent=2)}")
    
    return health_data

# Custom task class with automatic retry
class AutoRetryTask(celery_app.Task):
    """Base task class with automatic retry on failure"""
    
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': 3, 'countdown': 60}
    retry_backoff = True
    retry_backoff_max = 600  # 10 minutes
    retry_jitter = False

@celery_app.task(base=AutoRetryTask)
def reliable_data_sync(data_source: str, destination: str):
    """Sync data between systems with automatic retry"""
    
    logger.info(f"🔄 Starting data sync from {data_source} to {destination}")
    
    # This will automatically retry on any exception
    # with exponential backoff
    
    try:
        # Simulate data sync operation
        if random.random() < 0.3:  # 30% failure rate for testing
            raise ConnectionError("Simulated connection failure")
        
        time.sleep(2)  # Simulate work
        
        return {
            'status': 'success',
            'source': data_source,
            'destination': destination,
            'synced_at': time.time()
        }
        
    except Exception as e:
        logger.error(f"❌ Data sync failed: {str(e)}")
        raise  # This will trigger automatic retry
```

**Task Result Tracking:**

```python
# tasks/result_tracking.py
from celery.result import AsyncResult
from typing import Dict, Any

class TaskTracker:
    def __init__(self, celery_app):
        self.celery_app = celery_app
    
    def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """Get comprehensive task status"""
        
        result = AsyncResult(task_id, app=self.celery_app)
        
        task_info = {
            'task_id': task_id,
            'status': result.status,
            'ready': result.ready(),
            'successful': result.successful() if result.ready() else None,
            'failed': result.failed() if result.ready() else None,
        }
        
        if result.ready():
            if result.successful():
                task_info['result'] = result.result
            else:
                task_info['error'] = str(result.info)
                task_info['traceback'] = result.traceback
        else:
            # Task is still running - get progress info
            if result.info and isinstance(result.info, dict):
                task_info['progress'] = result.info
        
        return task_info
    
    def cancel_task(self, task_id: str) -> Dict[str, Any]:
        """Cancel a running task"""
        
        result = AsyncResult(task_id, app=self.celery_app)
        
        if not result.ready():
            result.revoke(terminate=True)
            return {
                'task_id': task_id,
                'status': 'cancelled',
                'message': 'Task cancelled successfully'
            }
        else:
            return {
                'task_id': task_id,
                'status': result.status,
                'message': 'Task already completed'
            }
    
    def get_active_tasks(self) -> Dict[str, Any]:
        """Get all active tasks across workers"""
        
        inspect = self.celery_app.control.inspect()
        
        try:
            active = inspect.active()
            scheduled = inspect.scheduled()
            reserved = inspect.reserved()
            
            return {
                'active_tasks': active,
                'scheduled_tasks': scheduled,
                'reserved_tasks': reserved,
                'worker_count': len(active) if active else 0
            }
        except Exception as e:
            return {
                'error': str(e),
                'message': 'Could not retrieve worker information'
            }

# Global task tracker
task_tracker = TaskTracker(celery_app)
```

---

### 4️⃣ FastAPI Integration (10 minutes)

**FastAPI Endpoints with Background Tasks:**

```python
# main.py - FastAPI integration
from fastapi import FastAPI, BackgroundTasks, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
import os

app = FastAPI(title="Background Processing API")

class EmailRequest(BaseModel):
    recipients: List[str]
    subject: str
    body: str
    html_body: Optional[str] = None

class NewsletterRequest(BaseModel):
    subscriber_emails: List[str]
    content: str
    send_immediately: bool = False

@app.post("/send-email")
async def send_email_endpoint(email_request: EmailRequest):
    """Send email via background task"""
    
    if len(email_request.recipients) == 1:
        # Single email
        task = send_email.delay(
            email_request.recipients[0],
            email_request.subject,
            email_request.body,
            email_request.html_body
        )
        
        return {
            "message": "Email queued for sending",
            "task_id": task.id,
            "recipient_count": 1
        }
    else:
        # Bulk emails
        email_jobs = [
            {
                'email': recipient,
                'subject': email_request.subject,
                'variables': {'recipient': recipient}
            }
            for recipient in email_request.recipients
        ]
        
        task = send_bulk_emails.delay(email_jobs, email_request.body)
        
        return {
            "message": f"Bulk email queued for {len(email_request.recipients)} recipients",
            "task_id": task.id,
            "recipient_count": len(email_request.recipients)
        }

@app.post("/newsletter")
async def send_newsletter_endpoint(newsletter: NewsletterRequest):
    """Send newsletter to subscribers"""
    
    if newsletter.send_immediately:
        # Use FastAPI background task for small lists
        if len(newsletter.subscriber_emails) <= 10:
            background_tasks = BackgroundTasks()
            
            def send_immediate_newsletter():
                for email in newsletter.subscriber_emails:
                    # Simulate sending
                    time.sleep(0.1)
                    print(f"📧 Newsletter sent to {email}")
            
            background_tasks.add_task(send_immediate_newsletter)
            
            return {
                "message": "Newsletter sent immediately",
                "recipient_count": len(newsletter.subscriber_emails)
            }
    
    # Use Celery for large lists or scheduled sending
    task = send_newsletter.delay(
        newsletter.subscriber_emails, 
        newsletter.content
    )
    
    return {
        "message": f"Newsletter queued for {len(newsletter.subscriber_emails)} subscribers",
        "task_id": task.id,
        "status": "processing"
    }

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...), user_id: int = 1):
    """Upload and process image"""
    
    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Save uploaded file temporarily
    upload_dir = "temp_uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_extension = file.filename.split('.')[-1] if '.' in file.filename else 'jpg'
    temp_filename = f"{uuid.uuid4()}.{file_extension}"
    temp_path = os.path.join(upload_dir, temp_filename)
    
    # Save file
    with open(temp_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Queue image processing
    task = process_uploaded_image.delay(temp_path, user_id)
    
    return {
        "message": "Image uploaded and queued for processing",
        "task_id": task.id,
        "filename": file.filename,
        "file_size": len(content)
    }

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Get task status and result"""
    
    task_info = task_tracker.get_task_status(task_id)
    
    if not task_info:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task_info

@app.delete("/tasks/{task_id}")
async def cancel_task(task_id: str):
    """Cancel a running task"""
    
    result = task_tracker.cancel_task(task_id)
    return result

@app.get("/tasks")
async def get_active_tasks():
    """Get all active tasks"""
    
    return task_tracker.get_active_tasks()

@app.post("/test/load-test")
async def create_load_test(num_tasks: int = 100, task_duration: int = 5):
    """Create multiple background tasks for testing"""
    
    task_ids = []
    
    for i in range(num_tasks):
        task = long_running_task.delay(task_duration)
        task_ids.append(task.id)
    
    return {
        "message": f"Created {num_tasks} background tasks",
        "task_ids": task_ids[:10],  # Return first 10 IDs
        "total_tasks": len(task_ids)
    }

# Periodic task status endpoint
@app.get("/health/workers")
async def get_worker_health():
    """Get Celery worker health status"""
    
    inspect = celery_app.control.inspect()
    
    try:
        # Get worker statistics
        stats = inspect.stats()
        active = inspect.active()
        reserved = inspect.reserved()
        
        if not stats:
            return {
                "status": "error",
                "message": "No workers available",
                "workers": []
            }
        
        worker_info = []
        for worker_name, worker_stats in stats.items():
            worker_info.append({
                "name": worker_name,
                "status": "active",
                "active_tasks": len(active.get(worker_name, [])),
                "reserved_tasks": len(reserved.get(worker_name, [])),
                "total_tasks": worker_stats.get('total', 0),
                "pool_processes": worker_stats.get('pool', {}).get('processes', 0)
            })
        
        return {
            "status": "healthy",
            "worker_count": len(worker_info),
            "workers": worker_info
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "workers": []
        }
```

---

### 5️⃣ Running and Monitoring (5 minutes)

**Start Celery Workers:**

```bash
# Start Redis (message broker)
redis-server

# Start Celery worker (in separate terminal)
celery -A celery_app worker --loglevel=info --concurrency=4

# Start Celery worker with specific queues
celery -A celery_app worker --loglevel=info --queues=email,images

# Start Celery Beat (periodic tasks scheduler)
celery -A celery_app beat --loglevel=info

# Start Flower (monitoring web UI)
celery -A celery_app flower --port=5555

# Production: Start all services
# Worker processes
celery multi start worker1 -A celery_app --pidfile="./celery/%n.pid" --logfile="./celery/%n%I.log"

# Beat scheduler  
celery -A celery_app beat --pidfile="./celery/beat.pid" --logfile="./celery/beat.log" --detach

# Flower monitoring
celery -A celery_app flower --port=5555 --persistent=True --db=./celery/flower
```

**Production Configuration:**

```python
# production_celery.py
import os
from celery import Celery

def create_celery_app():
    """Create production Celery app"""
    
    # Environment-based configuration
    broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    result_backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    
    celery = Celery('production_app')
    
    # Production settings
    celery.conf.update(
        broker_url=broker_url,
        result_backend=result_backend,
        
        # Performance settings
        worker_prefetch_multiplier=1,
        task_acks_late=True,
        worker_max_tasks_per_child=1000,
        
        # Security
        worker_hijack_root_logger=False,
        worker_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
        
        # Monitoring
        worker_send_task_events=True,
        task_send_sent_event=True,
        
        # Error handling
        task_reject_on_worker_lost=True,
        task_ignore_result=False,
    )
    
    return celery

# Deployment script
def deploy_workers():
    """Deploy Celery workers in production"""
    
    # Stop existing workers
    os.system("celery multi stopwait worker1 worker2 worker3")
    
    # Start new workers
    os.system("""
        celery multi start worker1 worker2 worker3 \
        -A production_celery:create_celery_app \
        --pidfile=./run/celery/%n.pid \
        --logfile=./logs/celery/%n%I.log \
        --loglevel=INFO \
        --concurrency=4
    """)
    
    print("✅ Celery workers deployed successfully")

if __name__ == "__main__":
    deploy_workers()
```

---

### 🏠 Homework: Create Background Task System

**Task:** Implement a complete background processing system

```python
# Create these background tasks:
# 1. Email notification system with retry logic
# 2. Image processing pipeline (resize, thumbnail, S3 upload)
# 3. Report generation task with progress tracking
# 4. Data backup task that runs daily
# 5. API sync task with external services

# Requirements:
# - Proper error handling and retries
# - Progress tracking for long-running tasks
# - Task monitoring and health checks
# - Queue management (separate queues for different task types)
# - Production-ready configuration

# Bonus:
# - Create a web dashboard to monitor tasks
# - Implement task scheduling with Celery Beat
# - Add metrics and alerting for failed tasks
```

---

### 📝 Key Takeaways

✅ Message Queues = Decouple heavy work from HTTP requests
✅ Celery = Distributed task queue for Python applications
✅ Retry Logic = Handle failures gracefully with backoff strategies
✅ Task Monitoring = Track progress and debug issues effectively
✅ Background Processing = Essential for scalable web applications

---

<a name="hour-35"></a>
## 📅 Hour 35: File Uploads, Media Handling & S3

### 🎯 Learning Objectives
- Handle secure file uploads with validation
- Implement streaming uploads for large files
- Store files in AWS S3 and CloudFront
- Create file processing pipelines
- Build image galleries and file management systems

### 📖 What to Teach

**"Today we master file handling from upload to cloud storage with security and performance!"**

---

### 1️⃣ Secure File Upload Implementation (15 minutes)

**File Upload Security & Validation:**

```python
# file_upload.py
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional, BinaryIO
import aiofiles
import os
import uuid
import hashlib
import magic
import PIL.Image
from pathlib import Path
import asyncio
from datetime import datetime, timedelta

app = FastAPI(title="Advanced File Upload API")
security = HTTPBearer()

# File upload configuration
class FileConfig:
    # File size limits (bytes)
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB for images
    MAX_VIDEO_SIZE = 100 * 1024 * 1024  # 100MB for videos
    
    # Allowed file types
    ALLOWED_IMAGE_TYPES = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image/gif': '.gif',
        'image/webp': '.webp'
    }
    
    ALLOWED_DOCUMENT_TYPES = {
        'application/pdf': '.pdf',
        'application/msword': '.doc',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
        'text/plain': '.txt',
        'text/csv': '.csv'
    }
    
    ALLOWED_VIDEO_TYPES = {
        'video/mp4': '.mp4',
        'video/avi': '.avi',
        'video/quicktime': '.mov',
        'video/x-msvideo': '.avi'
    }
    
    # Storage paths
    UPLOAD_DIR = Path("uploads")
    TEMP_DIR = Path("temp")
    PROCESSED_DIR = Path("processed")

class FileValidator:
    """Comprehensive file validation"""
    
    def __init__(self):
        self.config = FileConfig()
    
    async def validate_file(self, file: UploadFile, file_type: str = "any") -> dict:
        """Validate uploaded file with comprehensive checks"""
        
        validation_result = {
            'valid': False,
            'errors': [],
            'file_info': {},
            'security_checks': {}
        }
        
        try:
            # 1. Basic file info
            file_size = 0
            content = await file.read()
            file_size = len(content)
            await file.seek(0)  # Reset file pointer
            
            validation_result['file_info'] = {
                'filename': file.filename,
                'content_type': file.content_type,
                'size': file_size,
                'size_mb': round(file_size / (1024 * 1024), 2)
            }
            
            # 2. File size validation
            max_size = self._get_max_size_for_type(file_type)
            if file_size > max_size:
                validation_result['errors'].append(
                    f"File too large: {validation_result['file_info']['size_mb']}MB "
                    f"(max: {max_size / (1024 * 1024)}MB)"
                )
            
            if file_size == 0:
                validation_result['errors'].append("Empty file not allowed")
            
            # 3. MIME type validation using python-magic
            try:
                detected_mime = magic.from_buffer(content[:2048], mime=True)
                validation_result['file_info']['detected_mime'] = detected_mime
                
                # Check if detected MIME matches declared MIME
                if detected_mime != file.content_type:
                    validation_result['security_checks']['mime_mismatch'] = True
                    validation_result['errors'].append(
                        f"MIME type mismatch: declared {file.content_type}, "
                        f"detected {detected_mime}"
                    )
            except Exception as e:
                validation_result['errors'].append(f"MIME detection failed: {str(e)}")
            
            # 4. File type validation
            allowed_types = self._get_allowed_types_for_category(file_type)
            if file.content_type not in allowed_types:
                validation_result['errors'].append(
                    f"File type not allowed: {file.content_type}"
                )
            
            # 5. Filename validation
            if not file.filename or len(file.filename) > 255:
                validation_result['errors'].append("Invalid filename")
            
            # Check for dangerous characters
            dangerous_chars = ['..', '/', '\\', '<', '>', ':', '"', '|', '?', '*']
            if any(char in file.filename for char in dangerous_chars):
                validation_result['errors'].append("Filename contains dangerous characters")
            
            # 6. Content validation (specific to file type)
            if file_type == "image":
                image_validation = await self._validate_image_content(content)
                validation_result.update(image_validation)
            
            # 7. Malware scanning (basic)
            malware_check = await self._basic_malware_scan(content)
            validation_result['security_checks']['malware_scan'] = malware_check
            
            # 8. Generate file hash for deduplication
            file_hash = hashlib.sha256(content).hexdigest()
            validation_result['file_info']['sha256'] = file_hash
            
            # Set validation status
            validation_result['valid'] = len(validation_result['errors']) == 0
            
            return validation_result
            
        except Exception as e:
            validation_result['errors'].append(f"Validation error: {str(e)}")
            return validation_result
    
    def _get_max_size_for_type(self, file_type: str) -> int:
        """Get maximum file size for type"""
        size_map = {
            'image': self.config.MAX_IMAGE_SIZE,
            'video': self.config.MAX_VIDEO_SIZE,
            'document': self.config.MAX_FILE_SIZE,
            'any': self.config.MAX_FILE_SIZE
        }
        return size_map.get(file_type, self.config.MAX_FILE_SIZE)
    
    def _get_allowed_types_for_category(self, category: str) -> dict:
        """Get allowed MIME types for category"""
        type_map = {
            'image': self.config.ALLOWED_IMAGE_TYPES,
            'document': self.config.ALLOWED_DOCUMENT_TYPES,
            'video': self.config.ALLOWED_VIDEO_TYPES,
            'any': {**self.config.ALLOWED_IMAGE_TYPES, 
                   **self.config.ALLOWED_DOCUMENT_TYPES}
        }
        return type_map.get(category, {})
    
    async def _validate_image_content(self, content: bytes) -> dict:
        """Validate image-specific content"""
        result = {'image_validation': {}}
        
        try:
            # Try to open image with PIL
            from io import BytesIO
            image = PIL.Image.open(BytesIO(content))
            
            result['image_validation'] = {
                'dimensions': image.size,
                'format': image.format,
                'mode': image.mode,
                'valid': True
            }
            
            # Check for extremely large images
            width, height = image.size
            if width * height > 50_000_000:  # 50 megapixels
                result['errors'] = result.get('errors', [])
                result['errors'].append("Image resolution too high")
            
        except Exception as e:
            result['errors'] = result.get('errors', [])
            result['errors'].append(f"Invalid image file: {str(e)}")
            result['image_validation']['valid'] = False
        
        return result
    
    async def _basic_malware_scan(self, content: bytes) -> dict:
        """Basic malware detection"""
        
        # Simple signature-based detection
        malware_signatures = [
            b'<?php',  # PHP code injection
            b'<script',  # JavaScript injection
            b'eval(',  # Code evaluation
            b'system(',  # System calls
            b'exec(',  # Command execution
        ]
        
        threats_found = []
        for signature in malware_signatures:
            if signature.lower() in content.lower():
                threats_found.append(signature.decode('utf-8', errors='ignore'))
        
        return {
            'scan_completed': True,
            'threats_found': threats_found,
            'is_safe': len(threats_found) == 0
        }

# File upload endpoints
file_validator = FileValidator()

@app.post("/upload/single")
async def upload_single_file(
    file: UploadFile = File(...),
    file_type: str = Form("any"),
    description: Optional[str] = Form(None),
    user_id: int = Form(...),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Upload a single file with comprehensive validation"""
    
    # Validate file
    validation = await file_validator.validate_file(file, file_type)
    
    if not validation['valid']:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "File validation failed",
                "errors": validation['errors'],
                "file_info": validation['file_info']
            }
        )
    
    try:
        # Generate unique filename
        file_extension = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        
        # Create user directory
        user_dir = FileConfig.UPLOAD_DIR / str(user_id)
        user_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = user_dir / unique_filename
        
        # Save file asynchronously
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Create file record
        file_record = {
            'id': str(uuid.uuid4()),
            'original_filename': file.filename,
            'stored_filename': unique_filename,
            'file_path': str(file_path),
            'user_id': user_id,
            'description': description,
            'file_type': file_type,
            'mime_type': file.content_type,
            'file_size': validation['file_info']['size'],
            'file_hash': validation['file_info']['sha256'],
            'upload_timestamp': datetime.now().isoformat(),
            'validation_result': validation
        }
        
        # TODO: Save file_record to database
        
        return {
            "message": "File uploaded successfully",
            "file_id": file_record['id'],
            "filename": unique_filename,
            "size": validation['file_info']['size_mb'],
            "type": file.content_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@app.post("/upload/multiple")
async def upload_multiple_files(
    files: List[UploadFile] = File(...),
    file_type: str = Form("any"),
    user_id: int = Form(...),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Upload multiple files with batch processing"""
    
    if len(files) > 10:  # Limit batch size
        raise HTTPException(status_code=400, detail="Maximum 10 files per batch")
    
    upload_results = []
    failed_uploads = []
    
    for file in files:
        try:
            # Validate each file
            validation = await file_validator.validate_file(file, file_type)
            
            if not validation['valid']:
                failed_uploads.append({
                    'filename': file.filename,
                    'errors': validation['errors']
                })
                continue
            
            # Process valid files
            file_extension = Path(file.filename).suffix
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            
            user_dir = FileConfig.UPLOAD_DIR / str(user_id)
            user_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = user_dir / unique_filename
            
            # Save file
            async with aiofiles.open(file_path, 'wb') as f:
                content = await file.read()
                await f.write(content)
            
            upload_results.append({
                'original_filename': file.filename,
                'stored_filename': unique_filename,
                'size_mb': validation['file_info']['size_mb'],
                'file_hash': validation['file_info']['sha256']
            })
            
        except Exception as e:
            failed_uploads.append({
                'filename': file.filename,
                'error': str(e)
            })
    
    return {
        "message": f"Batch upload completed",
        "successful_uploads": len(upload_results),
        "failed_uploads": len(failed_uploads),
        "results": upload_results,
        "failures": failed_uploads
    }
```

**Streaming Upload for Large Files:**

```python
# streaming_upload.py
import aiofiles
from fastapi import Request, Response
import asyncio

class StreamingUploadHandler:
    """Handle streaming uploads for large files"""
    
    def __init__(self, chunk_size: int = 8192):
        self.chunk_size = chunk_size
    
    async def handle_streaming_upload(
        self, 
        request: Request, 
        file_path: Path,
        max_size: int = 100 * 1024 * 1024  # 100MB
    ) -> dict:
        """Handle streaming file upload with progress tracking"""
        
        total_size = 0
        chunks_received = 0
        
        try:
            async with aiofiles.open(file_path, 'wb') as f:
                async for chunk in self._read_chunks(request):
                    chunk_size = len(chunk)
                    total_size += chunk_size
                    chunks_received += 1
                    
                    # Size limit check
                    if total_size > max_size:
                        # Cleanup partial file
                        await f.close()
                        file_path.unlink(missing_ok=True)
                        
                        raise HTTPException(
                            status_code=413,
                            detail=f"File too large. Max size: {max_size / (1024*1024):.1f}MB"
                        )
                    
                    await f.write(chunk)
                    
                    # Progress callback (could emit WebSocket events)
                    progress = (total_size / max_size) * 100
                    if chunks_received % 100 == 0:  # Every 100 chunks
                        await self._emit_progress(progress, total_size)
        
            return {
                'total_size': total_size,
                'chunks_received': chunks_received,
                'file_path': str(file_path)
            }
            
        except Exception as e:
            # Cleanup on error
            file_path.unlink(missing_ok=True)
            raise e
    
    async def _read_chunks(self, request: Request):
        """Read request body in chunks"""
        async for chunk in request.stream():
            if chunk:
                yield chunk
    
    async def _emit_progress(self, progress: float, bytes_received: int):
        """Emit progress updates (WebSocket, SSE, etc.)"""
        # Could emit to WebSocket or store in Redis for polling
        print(f"📈 Upload progress: {progress:.1f}% ({bytes_received:,} bytes)")

@app.post("/upload/streaming/{file_id}")
async def streaming_upload(
    file_id: str,
    request: Request,
    user_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Handle streaming file upload"""
    
    # Validate file_id and user permissions
    if not file_id or len(file_id) != 36:  # UUID length
        raise HTTPException(status_code=400, detail="Invalid file ID")
    
    # Create file path
    user_dir = FileConfig.UPLOAD_DIR / str(user_id)
    user_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = user_dir / f"{file_id}.tmp"
    
    # Handle streaming upload
    streaming_handler = StreamingUploadHandler()
    
    try:
        result = await streaming_handler.handle_streaming_upload(
            request, 
            file_path,
            max_size=FileConfig.MAX_FILE_SIZE
        )
        
        return {
            "message": "Streaming upload completed",
            "file_id": file_id,
            "size": result['total_size'],
            "chunks": result['chunks_received']
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/upload/progress/{file_id}")
async def get_upload_progress(file_id: str):
    """Get upload progress for streaming uploads"""
    
    # In production, store progress in Redis
    # This is a simplified example
    
    progress_data = {
        'file_id': file_id,
        'progress': 75.5,
        'bytes_received': 7550000,
        'status': 'uploading',
        'eta_seconds': 30
    }
    
    return progress_data
```

---

### 2️⃣ AWS S3 Integration (15 minutes)

**S3 Configuration and Upload:**

```python
# s3_handler.py
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from botocore.config import Config
import os
from typing import BinaryIO, Optional, Dict, Any
import mimetypes
from urllib.parse import quote
import asyncio
from concurrent.futures import ThreadPoolExecutor
import logging

logger = logging.getLogger(__name__)

class S3FileManager:
    """Advanced S3 file management with multipart uploads"""
    
    def __init__(self):
        # S3 configuration
        self.bucket_name = os.getenv('AWS_S3_BUCKET', 'my-app-uploads')
        self.region = os.getenv('AWS_REGION', 'us-east-1')
        self.access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        
        # CloudFront distribution (optional)
        self.cloudfront_domain = os.getenv('CLOUDFRONT_DOMAIN')
        
        # Create S3 client with retry configuration
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region,
            config=Config(
                region_name=self.region,
                retries={'max_attempts': 3, 'mode': 'adaptive'},
                max_pool_connections=50
            )
        )
        
        # Thread pool for async operations
        self.executor = ThreadPoolExecutor(max_workers=10)
    
    async def upload_file(
        self,
        file_path: str,
        s3_key: str,
        content_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        public_read: bool = False
    ) -> Dict[str, Any]:
        """Upload file to S3 with comprehensive options"""
        
        try:
            # Auto-detect content type if not provided
            if not content_type:
                content_type, _ = mimetypes.guess_type(file_path)
                if not content_type:
                    content_type = 'application/octet-stream'
            
            # Prepare upload arguments
            upload_args = {
                'Bucket': self.bucket_name,
                'Key': s3_key,
                'ContentType': content_type
            }
            
            # Add metadata
            if metadata:
                upload_args['Metadata'] = metadata
            
            # Set permissions
            if public_read:
                upload_args['ACL'] = 'public-read'
            
            # Add cache control for static assets
            if content_type.startswith(('image/', 'video/', 'audio/')):
                upload_args['CacheControl'] = 'max-age=31536000'  # 1 year
            
            # Upload file asynchronously
            loop = asyncio.get_event_loop()
            
            def _upload():
                return self.s3_client.upload_file(
                    file_path,
                    **upload_args
                )
            
            await loop.run_in_executor(self.executor, _upload)
            
            # Generate URLs
            s3_url = f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{quote(s3_key)}"
            
            # Use CloudFront URL if available
            if self.cloudfront_domain:
                cdn_url = f"https://{self.cloudfront_domain}/{quote(s3_key)}"
            else:
                cdn_url = s3_url
            
            logger.info(f"✅ File uploaded to S3: {s3_key}")
            
            return {
                'success': True,
                's3_key': s3_key,
                's3_url': s3_url,
                'cdn_url': cdn_url,
                'bucket': self.bucket_name,
                'content_type': content_type
            }
            
        except FileNotFoundError:
            logger.error(f"❌ File not found: {file_path}")
            return {'success': False, 'error': 'File not found'}
            
        except NoCredentialsError:
            logger.error("❌ AWS credentials not found")
            return {'success': False, 'error': 'AWS credentials not configured'}
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            
            logger.error(f"❌ S3 upload failed: {error_code} - {error_message}")
            
            return {
                'success': False,
                'error': f"S3 error: {error_code}",
                'details': error_message
            }
        
        except Exception as e:
            logger.error(f"❌ Unexpected upload error: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    async def upload_multipart(
        self,
        file_path: str,
        s3_key: str,
        part_size: int = 100 * 1024 * 1024,  # 100MB parts
        content_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Upload large file using multipart upload"""
        
        try:
            file_size = os.path.getsize(file_path)
            
            if file_size < part_size:
                # Use regular upload for small files
                return await self.upload_file(file_path, s3_key, content_type)
            
            # Auto-detect content type
            if not content_type:
                content_type, _ = mimetypes.guess_type(file_path)
                if not content_type:
                    content_type = 'application/octet-stream'
            
            logger.info(f"🔄 Starting multipart upload: {s3_key} ({file_size:,} bytes)")
            
            # Initiate multipart upload
            loop = asyncio.get_event_loop()
            
            def _initiate_multipart():
                return self.s3_client.create_multipart_upload(
                    Bucket=self.bucket_name,
                    Key=s3_key,
                    ContentType=content_type
                )
            
            response = await loop.run_in_executor(self.executor, _initiate_multipart)
            upload_id = response['UploadId']
            
            # Upload parts
            parts = []
            part_number = 1
            
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(part_size)
                    if not chunk:
                        break
                    
                    def _upload_part():
                        return self.s3_client.upload_part(
                            Bucket=self.bucket_name,
                            Key=s3_key,
                            PartNumber=part_number,
                            UploadId=upload_id,
                            Body=chunk
                        )
                    
                    part_response = await loop.run_in_executor(self.executor, _upload_part)
                    
                    parts.append({
                        'ETag': part_response['ETag'],
                        'PartNumber': part_number
                    })
                    
                    logger.info(f"📤 Uploaded part {part_number} ({len(chunk):,} bytes)")
                    part_number += 1
            
            # Complete multipart upload
            def _complete_multipart():
                return self.s3_client.complete_multipart_upload(
                    Bucket=self.bucket_name,
                    Key=s3_key,
                    UploadId=upload_id,
                    MultipartUpload={'Parts': parts}
                )
            
            await loop.run_in_executor(self.executor, _complete_multipart)
            
            # Generate URLs
            s3_url = f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{quote(s3_key)}"
            cdn_url = f"https://{self.cloudfront_domain}/{quote(s3_key)}" if self.cloudfront_domain else s3_url
            
            logger.info(f"✅ Multipart upload completed: {s3_key}")
            
            return {
                'success': True,
                's3_key': s3_key,
                's3_url': s3_url,
                'cdn_url': cdn_url,
                'file_size': file_size,
                'parts_uploaded': len(parts),
                'upload_method': 'multipart'
            }
            
        except Exception as e:
            # Cleanup failed multipart upload
            if 'upload_id' in locals():
                try:
                    await loop.run_in_executor(
                        self.executor,
                        lambda: self.s3_client.abort_multipart_upload(
                            Bucket=self.bucket_name,
                            Key=s3_key,
                            UploadId=upload_id
                        )
                    )
                except:
                    pass
            
            logger.error(f"❌ Multipart upload failed: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    async def generate_presigned_url(
        self,
        s3_key: str,
        expiration: int = 3600,
        http_method: str = 'GET'
    ) -> Dict[str, Any]:
        """Generate presigned URL for secure file access"""
        
        try:
            loop = asyncio.get_event_loop()
            
            def _generate_url():
                return self.s3_client.generate_presigned_url(
                    http_method.upper(),
                    Params={'Bucket': self.bucket_name, 'Key': s3_key},
                    ExpiresIn=expiration
                )
            
            presigned_url = await loop.run_in_executor(self.executor, _generate_url)
            
            return {
                'success': True,
                'presigned_url': presigned_url,
                'expires_in': expiration,
                's3_key': s3_key
            }
            
        except Exception as e:
            logger.error(f"❌ Presigned URL generation failed: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    async def delete_file(self, s3_key: str) -> Dict[str, Any]:
        """Delete file from S3"""
        
        try:
            loop = asyncio.get_event_loop()
            
            def _delete():
                return self.s3_client.delete_object(
                    Bucket=self.bucket_name,
                    Key=s3_key
                )
            
            await loop.run_in_executor(self.executor, _delete)
            
            logger.info(f"🗑️ File deleted from S3: {s3_key}")
            
            return {
                'success': True,
                's3_key': s3_key,
                'message': 'File deleted successfully'
            }
            
        except Exception as e:
            logger.error(f"❌ S3 delete failed: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    async def list_files(
        self,
        prefix: str = '',
        max_keys: int = 1000
    ) -> Dict[str, Any]:
        """List files in S3 bucket"""
        
        try:
            loop = asyncio.get_event_loop()
            
            def _list_objects():
                return self.s3_client.list_objects_v2(
                    Bucket=self.bucket_name,
                    Prefix=prefix,
                    MaxKeys=max_keys
                )
            
            response = await loop.run_in_executor(self.executor, _list_objects)
            
            files = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    files.append({
                        'key': obj['Key'],
                        'size': obj['Size'],
                        'last_modified': obj['LastModified'].isoformat(),
                        'url': f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{quote(obj['Key'])}"
                    })
            
            return {
                'success': True,
                'files': files,
                'count': len(files),
                'prefix': prefix
            }
            
        except Exception as e:
            logger.error(f"❌ S3 list failed: {str(e)}")
            return {'success': False, 'error': str(e)}

# Initialize S3 manager
s3_manager = S3FileManager()
```

**S3 Upload Endpoints:**

```python
# S3 integration with FastAPI
@app.post("/upload/s3")
async def upload_to_s3(
    file: UploadFile = File(...),
    folder: str = Form("uploads"),
    user_id: int = Form(...),
    make_public: bool = Form(False),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Upload file directly to S3"""
    
    # Validate file
    validation = await file_validator.validate_file(file, "any")
    
    if not validation['valid']:
        raise HTTPException(status_code=400, detail=validation['errors'])
    
    try:
        # Save file temporarily
        temp_dir = FileConfig.TEMP_DIR
        temp_dir.mkdir(exist_ok=True)
        
        temp_filename = f"{uuid.uuid4()}{Path(file.filename).suffix}"
        temp_path = temp_dir / temp_filename
        
        # Save uploaded file
        async with aiofiles.open(temp_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Generate S3 key
        file_hash = validation['file_info']['sha256'][:12]  # First 12 chars of hash
        s3_key = f"{folder}/user_{user_id}/{file_hash}_{temp_filename}"
        
        # Upload to S3
        if validation['file_info']['size'] > 100 * 1024 * 1024:  # 100MB
            # Use multipart upload for large files
            result = await s3_manager.upload_multipart(
                str(temp_path),
                s3_key,
                content_type=file.content_type
            )
        else:
            # Regular upload for smaller files
            metadata = {
                'original-filename': file.filename,
                'user-id': str(user_id),
                'upload-timestamp': datetime.now().isoformat()
            }
            
            result = await s3_manager.upload_file(
                str(temp_path),
                s3_key,
                content_type=file.content_type,
                metadata=metadata,
                public_read=make_public
            )
        
        # Cleanup temp file
        temp_path.unlink(missing_ok=True)
        
        if result['success']:
            return {
                "message": "File uploaded to S3 successfully",
                "s3_key": result['s3_key'],
                "url": result['cdn_url'],
                "size": validation['file_info']['size'],
                "content_type": file.content_type
            }
        else:
            raise HTTPException(status_code=500, detail=result['error'])
            
    except Exception as e:
        # Cleanup on error
        if 'temp_path' in locals():
            temp_path.unlink(missing_ok=True)
        
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/files/s3/{s3_key:path}/download")
async def download_from_s3(
    s3_key: str,
    expires_in: int = 3600,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Generate secure download URL for S3 file"""
    
    result = await s3_manager.generate_presigned_url(
        s3_key,
        expiration=expires_in,
        http_method='GET'
    )
    
    if result['success']:
        return {
            "download_url": result['presigned_url'],
            "expires_in": expires_in,
            "s3_key": s3_key
        }
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.delete("/files/s3/{s3_key:path}")
async def delete_from_s3(
    s3_key: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Delete file from S3"""
    
    result = await s3_manager.delete_file(s3_key)
    
    if result['success']:
        return {"message": "File deleted successfully", "s3_key": s3_key}
    else:
        raise HTTPException(status_code=500, detail=result['error'])
```

---

### 3️⃣ Image Processing Pipeline (10 minutes)

**Advanced Image Processing:**

```python
# image_processing.py
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import asyncio
from concurrent.futures import ProcessPoolExecutor
import io
import base64
from typing import Tuple, List, Dict, Any

class ImageProcessor:
    """Advanced image processing with async support"""
    
    def __init__(self):
        self.executor = ProcessPoolExecutor(max_workers=4)
    
    async def process_image_variants(
        self,
        image_path: str,
        variants: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Process multiple image variants asynchronously"""
        
        loop = asyncio.get_event_loop()
        
        def _process_all_variants():
            results = {}
            
            with Image.open(image_path) as img:
                # Convert to RGB if needed
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                for variant_name, config in variants.items():
                    try:
                        processed_img = self._apply_transformations(img.copy(), config)
                        
                        # Save variant
                        output_buffer = io.BytesIO()
                        format_type = config.get('format', 'JPEG')
                        quality = config.get('quality', 85)
                        
                        processed_img.save(
                            output_buffer,
                            format=format_type,
                            quality=quality,
                            optimize=True
                        )
                        
                        results[variant_name] = {
                            'buffer': output_buffer.getvalue(),
                            'size': processed_img.size,
                            'format': format_type,
                            'file_size': len(output_buffer.getvalue())
                        }
                        
                    except Exception as e:
                        results[variant_name] = {'error': str(e)}
            
            return results
        
        return await loop.run_in_executor(self.executor, _process_all_variants)
    
    def _apply_transformations(self, img: Image.Image, config: Dict[str, Any]) -> Image.Image:
        """Apply image transformations based on configuration"""
        
        # Resize/thumbnail
        if 'size' in config:
            size = config['size']
            if isinstance(size, (list, tuple)) and len(size) == 2:
                if config.get('crop', False):
                    img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
                else:
                    img.thumbnail(size, Image.Resampling.LANCZOS)
        
        # Rotation
        if 'rotate' in config:
            img = img.rotate(config['rotate'], expand=True)
        
        # Filters
        filters = config.get('filters', [])
        for filter_config in filters:
            filter_type = filter_config.get('type')
            
            if filter_type == 'blur':
                radius = filter_config.get('radius', 2)
                img = img.filter(ImageFilter.GaussianBlur(radius=radius))
            
            elif filter_type == 'sharpen':
                img = img.filter(ImageFilter.SHARPEN)
            
            elif filter_type == 'enhance':
                factor = filter_config.get('factor', 1.2)
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(factor)
        
        # Color adjustments
        if 'brightness' in config:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(config['brightness'])
        
        if 'contrast' in config:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(config['contrast'])
        
        if 'saturation' in config:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(config['saturation'])
        
        return img
    
    async def create_responsive_images(self, image_path: str, base_name: str) -> Dict[str, Any]:
        """Create responsive image set for web use"""
        
        variants = {
            'thumbnail': {
                'size': (150, 150),
                'crop': True,
                'quality': 80,
                'format': 'JPEG'
            },
            'small': {
                'size': (400, 300),
                'quality': 85,
                'format': 'JPEG'
            },
            'medium': {
                'size': (800, 600),
                'quality': 85,
                'format': 'JPEG'
            },
            'large': {
                'size': (1200, 900),
                'quality': 90,
                'format': 'JPEG'
            },
            'webp_small': {
                'size': (400, 300),
                'quality': 80,
                'format': 'WebP'
            },
            'webp_medium': {
                'size': (800, 600),
                'quality': 80,
                'format': 'WebP'
            }
        }
        
        results = await self.process_image_variants(image_path, variants)
        
        # Upload all variants to S3
        upload_tasks = []
        for variant_name, variant_data in results.items():
            if 'error' not in variant_data:
                # Create temp file and upload
                temp_path = f"/tmp/{base_name}_{variant_name}.{variant_data['format'].lower()}"
                
                with open(temp_path, 'wb') as f:
                    f.write(variant_data['buffer'])
                
                s3_key = f"images/{base_name}/{variant_name}.{variant_data['format'].lower()}"
                upload_task = s3_manager.upload_file(temp_path, s3_key)
                upload_tasks.append((variant_name, upload_task))
        
        # Wait for all uploads
        upload_results = {}
        for variant_name, upload_task in upload_tasks:
            upload_result = await upload_task
            upload_results[variant_name] = upload_result
        
        return {
            'variants': results,
            'uploads': upload_results,
            'responsive_set': self._create_responsive_html(upload_results)
        }
    
    def _create_responsive_html(self, upload_results: Dict[str, Any]) -> str:
        """Generate HTML for responsive images"""
        
        # Create srcset for different sizes
        jpeg_variants = []
        webp_variants = []
        
        for variant_name, upload_result in upload_results.items():
            if upload_result.get('success'):
                url = upload_result['cdn_url']
                
                if 'webp' in variant_name:
                    if 'small' in variant_name:
                        webp_variants.append(f"{url} 400w")
                    elif 'medium' in variant_name:
                        webp_variants.append(f"{url} 800w")
                else:
                    if 'small' in variant_name:
                        jpeg_variants.append(f"{url} 400w")
                    elif 'medium' in variant_name:
                        jpeg_variants.append(f"{url} 800w")
                    elif 'large' in variant_name:
                        jpeg_variants.append(f"{url} 1200w")
        
        # Generate picture element
        html = "<picture>\n"
        
        if webp_variants:
            html += f'  <source srcset="{", ".join(webp_variants)}" type="image/webp">\n'
        
        if jpeg_variants:
            html += f'  <img srcset="{", ".join(jpeg_variants)}" '
            html += 'sizes="(max-width: 400px) 100vw, (max-width: 800px) 50vw, 33vw" '
            html += f'src="{upload_results.get("medium", {}).get("cdn_url", "")}" '
            html += 'alt="Responsive image" loading="lazy">\n'
        
        html += "</picture>"
        
        return html

# Initialize image processor
image_processor = ImageProcessor()
```

---

### 4️⃣ File Management System (10 minutes)

**Complete File Management API:**

```python
# file_management.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from typing import List, Optional
import json

# Database models
Base = declarative_base()

class FileRecord(Base):
    __tablename__ = "files"
    
    id = Column(String, primary_key=True)
    user_id = Column(Integer, nullable=False)
    original_filename = Column(String(255), nullable=False)
    stored_filename = Column(String(255), nullable=False)
    s3_key = Column(String(512))
    file_type = Column(String(50))
    mime_type = Column(String(100))
    file_size = Column(Integer)
    file_hash = Column(String(64))
    description = Column(Text)
    tags = Column(Text)  # JSON array
    is_public = Column(Boolean, default=False)
    upload_timestamp = Column(DateTime, default=datetime.utcnow)
    last_accessed = Column(DateTime)
    download_count = Column(Integer, default=0)
    processing_status = Column(String(50), default='pending')
    metadata = Column(Text)  # JSON

class FileManager:
    """Complete file management system"""
    
    def __init__(self, db_session: Session):
        self.db = db_session
    
    def create_file_record(self, file_data: Dict[str, Any]) -> FileRecord:
        """Create new file record in database"""
        
        file_record = FileRecord(
            id=file_data['id'],
            user_id=file_data['user_id'],
            original_filename=file_data['original_filename'],
            stored_filename=file_data['stored_filename'],
            s3_key=file_data.get('s3_key'),
            file_type=file_data['file_type'],
            mime_type=file_data['mime_type'],
            file_size=file_data['file_size'],
            file_hash=file_data['file_hash'],
            description=file_data.get('description'),
            tags=json.dumps(file_data.get('tags', [])),
            is_public=file_data.get('is_public', False),
            metadata=json.dumps(file_data.get('metadata', {}))
        )
        
        self.db.add(file_record)
        self.db.commit()
        self.db.refresh(file_record)
        
        return file_record
    
    def get_user_files(
        self,
        user_id: int,
        file_type: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[FileRecord]:
        """Get paginated file list for user"""
        
        query = self.db.query(FileRecord).filter(FileRecord.user_id == user_id)
        
        if file_type:
            query = query.filter(FileRecord.file_type == file_type)
        
        return query.order_by(FileRecord.upload_timestamp.desc()).offset(offset).limit(limit).all()
    
    def search_files(
        self,
        user_id: int,
        search_term: str,
        file_type: Optional[str] = None
    ) -> List[FileRecord]:
        """Search files by filename or description"""
        
        query = self.db.query(FileRecord).filter(FileRecord.user_id == user_id)
        
        # Search in filename and description
        search_filter = (
            FileRecord.original_filename.ilike(f"%{search_term}%") |
            FileRecord.description.ilike(f"%{search_term}%")
        )
        query = query.filter(search_filter)
        
        if file_type:
            query = query.filter(FileRecord.file_type == file_type)
        
        return query.order_by(FileRecord.upload_timestamp.desc()).all()
    
    def update_file_access(self, file_id: str):
        """Update file access statistics"""
        
        file_record = self.db.query(FileRecord).filter(FileRecord.id == file_id).first()
        if file_record:
            file_record.last_accessed = datetime.utcnow()
            file_record.download_count += 1
            self.db.commit()
    
    def delete_file_record(self, file_id: str, user_id: int) -> bool:
        """Delete file record (user must own the file)"""
        
        file_record = self.db.query(FileRecord).filter(
            FileRecord.id == file_id,
            FileRecord.user_id == user_id
        ).first()
        
        if file_record:
            self.db.delete(file_record)
            self.db.commit()
            return True
        
        return False

# File management endpoints
@app.get("/files/user/{user_id}")
async def get_user_files(
    user_id: int,
    file_type: Optional[str] = None,
    page: int = 1,
    per_page: int = 20,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get paginated file list for user"""
    
    file_manager = FileManager(db)
    
    offset = (page - 1) * per_page
    files = file_manager.get_user_files(user_id, file_type, per_page, offset)
    
    # Convert to response format
    file_list = []
    for file_record in files:
        file_data = {
            'id': file_record.id,
            'filename': file_record.original_filename,
            'file_type': file_record.file_type,
            'mime_type': file_record.mime_type,
            'file_size': file_record.file_size,
            'description': file_record.description,
            'upload_date': file_record.upload_timestamp.isoformat(),
            'download_count': file_record.download_count,
            'is_public': file_record.is_public
        }
        
        # Add download URL
        if file_record.s3_key:
            presigned_result = await s3_manager.generate_presigned_url(file_record.s3_key)
            if presigned_result['success']:
                file_data['download_url'] = presigned_result['presigned_url']
        
        file_list.append(file_data)
    
    return {
        'files': file_list,
        'page': page,
        'per_page': per_page,
        'total_files': len(file_list)
    }

@app.get("/files/search")
async def search_files(
    user_id: int,
    q: str,
    file_type: Optional[str] = None,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Search user files"""
    
    if len(q) < 3:
        raise HTTPException(status_code=400, detail="Search term must be at least 3 characters")
    
    file_manager = FileManager(db)
    files = file_manager.search_files(user_id, q, file_type)
    
    search_results = []
    for file_record in files:
        search_results.append({
            'id': file_record.id,
            'filename': file_record.original_filename,
            'description': file_record.description,
            'file_type': file_record.file_type,
            'upload_date': file_record.upload_timestamp.isoformat(),
            'relevance_score': 1.0  # Could implement proper relevance scoring
        })
    
    return {
        'results': search_results,
        'query': q,
        'total_results': len(search_results)
    }

@app.post("/files/{file_id}/process-images")
async def process_file_images(
    file_id: str,
    user_id: int,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Process uploaded images to create responsive variants"""
    
    file_manager = FileManager(db)
    
    # Get file record
    file_record = db.query(FileRecord).filter(
        FileRecord.id == file_id,
        FileRecord.user_id == user_id,
        FileRecord.file_type == 'image'
    ).first()
    
    if not file_record:
        raise HTTPException(status_code=404, detail="Image file not found")
    
    if not file_record.s3_key:
        raise HTTPException(status_code=400, detail="File not stored in S3")
    
    # Download original file temporarily
    temp_dir = Path("/tmp/image_processing")
    temp_dir.mkdir(exist_ok=True)
    
    original_path = temp_dir / f"original_{file_id}"
    
    # Download from S3 (simplified - in production use proper S3 download)
    # This would download the S3 object to local temp file
    
    # Process images
    base_name = f"{file_id}_{int(datetime.now().timestamp())}"
    processing_result = await image_processor.create_responsive_images(
        str(original_path), 
        base_name
    )
    
    # Update file record with processing results
    metadata = json.loads(file_record.metadata or '{}')
    metadata['responsive_images'] = processing_result['uploads']
    metadata['responsive_html'] = processing_result['responsive_set']
    
    file_record.metadata = json.dumps(metadata)
    file_record.processing_status = 'completed'
    db.commit()
    
    # Cleanup temp file
    original_path.unlink(missing_ok=True)
    
    return {
        'message': 'Image processing completed',
        'file_id': file_id,
        'variants_created': len(processing_result['variants']),
        'responsive_html': processing_result['responsive_set']
    }
```

---

### 🏠 Homework: Build File Management System

**Task:** Create a complete file management system with S3 integration

```python
# Build a system with:
# 1. Secure file upload with comprehensive validation
# 2. S3 storage with multipart uploads for large files
# 3. Image processing pipeline with responsive variants
# 4. File organization (folders, tags, search)
# 5. User permissions and file sharing
# 6. File versioning and backup
# 7. CDN integration with CloudFront
# 8. File analytics (downloads, popular files)

# Requirements:
# - Handle files up to 1GB
# - Support image, video, and document types
# - Automatic thumbnail generation
# - Virus scanning integration
# - File deduplication
# - Bandwidth optimization

# Bonus:
# - File compression and optimization
# - Automatic backups to multiple regions
# - File expiration and cleanup
# - Integration with office document preview
```

---

### 📝 Key Takeaways

✅ File Security = Always validate uploads thoroughly
✅ S3 Integration = Scalable cloud storage with CDN
✅ Streaming Uploads = Handle large files efficiently  
✅ Image Processing = Create responsive variants automatically
✅ File Management = Complete CRUD with search and analytics

---

<a name="hour-36"></a>
## 📅 Hour 36: Security Best Practices

### 🎯 Learning Objectives
- Implement OWASP Top 10 security measures
- Handle authentication and authorization securely
- Protect against common web vulnerabilities
- Implement security headers and middleware
- Create secure API endpoints with proper validation

### 📖 What to Teach

**"Today we build fortress-level security into our applications - because security is not optional!"**

---

### 1️⃣ OWASP Top 10 Implementation (15 minutes)

**1. Injection Prevention (SQL, NoSQL, Command Injection):**

```python
# secure_database.py
from sqlalchemy.orm import Session
from sqlalchemy import text
import bleach
import re
from typing import Any, List, Dict
import logging

logger = logging.getLogger(__name__)

class SecureDatabase:
    """Database operations with injection prevention"""
    
    def __init__(self, db_session: Session):
        self.db = db_session
    
    def safe_query_with_params(self, query: str, params: Dict[str, Any]) -> List[Any]:
        """Execute parameterized queries safely"""
        
        try:
            # Use SQLAlchemy's text() with bound parameters
            # This automatically prevents SQL injection
            result = self.db.execute(text(query), params)
            return result.fetchall()
            
        except Exception as e:
            logger.error(f"❌ Database query failed: {str(e)}")
            raise ValueError("Database query failed")
    
    def sanitize_search_input(self, search_term: str) -> str:
        """Sanitize user input for search queries"""
        
        if not search_term:
            return ""
        
        # Remove potential SQL injection patterns
        dangerous_patterns = [
            r"(\%27)|(\')|(\-\-)|(\%23)|(#)",  # SQL comment patterns
            r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",  # SQL injection patterns
            r"w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))",  # 'or' patterns
            r"((\%27)|(\'))union",  # UNION patterns
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, search_term, re.IGNORECASE):
                logger.warning(f"⚠️ Potential SQL injection attempt blocked: {search_term}")
                raise ValueError("Invalid search parameters")
        
        # Sanitize and limit length
        sanitized = bleach.clean(search_term, tags=[], strip=True)
        return sanitized[:100]  # Limit length
    
    def get_user_posts_safe(self, user_id: int, search_term: str = None) -> List[Any]:
        """Safe user posts retrieval with optional search"""
        
        # Validate user_id
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("Invalid user ID")
        
        base_query = """
            SELECT p.id, p.title, p.content, p.created_at 
            FROM posts p 
            WHERE p.user_id = :user_id AND p.deleted_at IS NULL
        """
        
        params = {'user_id': user_id}
        
        if search_term:
            sanitized_search = self.sanitize_search_input(search_term)
            base_query += " AND (p.title ILIKE :search OR p.content ILIKE :search)"
            params['search'] = f"%{sanitized_search}%"
        
        base_query += " ORDER BY p.created_at DESC LIMIT 50"
        
        return self.safe_query_with_params(base_query, params)

# Command injection prevention
class SecureSystemOperations:
    """Secure system operations without command injection"""
    
    @staticmethod
    def validate_filename(filename: str) -> str:
        """Validate and sanitize filename"""
        
        if not filename:
            raise ValueError("Filename cannot be empty")
        
        # Remove dangerous characters
        dangerous_chars = ['..', '/', '\\', '|', ';', '&', '$', '>', '<', '`', '!']
        for char in dangerous_chars:
            if char in filename:
                raise ValueError(f"Filename contains dangerous character: {char}")
        
        # Only allow alphanumeric, dots, hyphens, underscores
        if not re.match(r'^[a-zA-Z0-9._-]+$', filename):
            raise ValueError("Filename contains invalid characters")
        
        # Limit length
        if len(filename) > 255:
            raise ValueError("Filename too long")
        
        return filename
    
    @staticmethod
    def safe_file_operations(operation: str, filename: str) -> Dict[str, Any]:
        """Safe file operations without command injection"""
        
        validated_filename = SecureSystemOperations.validate_filename(filename)
        
        import os
        import subprocess
        from pathlib import Path
        
        # Define safe operations with whitelisted commands
        safe_operations = {
            'get_file_info': ['stat', '-c', '%s %Y'],  # size and modification time
            'check_permissions': ['test', '-r'],  # readable test
            'get_file_type': ['file', '--mime-type', '-b']  # MIME type detection
        }
        
        if operation not in safe_operations:
            raise ValueError(f"Operation not allowed: {operation}")
        
        try:
            # Build command safely
            cmd = safe_operations[operation] + [validated_filename]
            
            # Execute with security constraints
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,  # Prevent hanging
                cwd='/safe/directory',  # Restrict working directory
                env={'PATH': '/usr/bin:/bin'}  # Minimal environment
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout.strip(),
                'error': result.stderr.strip() if result.stderr else None
            }
            
        except subprocess.TimeoutExpired:
            logger.error(f"❌ Command timeout for operation: {operation}")
            return {'success': False, 'error': 'Operation timed out'}
        
        except Exception as e:
            logger.error(f"❌ Safe operation failed: {str(e)}")
            return {'success': False, 'error': str(e)}
```

**2. Broken Authentication Prevention:**

```python
# secure_auth.py
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import bcrypt
import secrets
import redis
import hashlib
from typing import Optional, Dict, Any
import time
import logging

logger = logging.getLogger(__name__)

class SecureAuthentication:
    """Secure authentication with best practices"""
    
    def __init__(self):
        # Password hashing
        self.pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto",
            bcrypt__rounds=12  # Strong hashing rounds
        )
        
        # JWT configuration
        self.SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_urlsafe(32))
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.REFRESH_TOKEN_EXPIRE_DAYS = 7
        
        # Rate limiting
        self.redis_client = redis.Redis(host='localhost', port=6379, db=1)
        
        # Password policy
        self.password_policy = {
            'min_length': 8,
            'max_length': 128,
            'require_uppercase': True,
            'require_lowercase': True,
            'require_numbers': True,
            'require_special': True,
            'special_chars': "!@#$%^&*()_+-=[]{}|;:,.<>?"
        }
    
    def validate_password_strength(self, password: str) -> Dict[str, Any]:
        """Comprehensive password strength validation"""
        
        validation_result = {
            'valid': False,
            'errors': [],
            'strength_score': 0
        }
        
        # Length check
        if len(password) < self.password_policy['min_length']:
            validation_result['errors'].append(
                f"Password must be at least {self.password_policy['min_length']} characters"
            )
        elif len(password) > self.password_policy['max_length']:
            validation_result['errors'].append(
                f"Password must be less than {self.password_policy['max_length']} characters"
            )
        else:
            validation_result['strength_score'] += 25
        
        # Character requirements
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.password_policy['special_chars'] for c in password)
        
        if self.password_policy['require_uppercase'] and not has_upper:
            validation_result['errors'].append("Password must contain uppercase letters")
        elif has_upper:
            validation_result['strength_score'] += 20
        
        if self.password_policy['require_lowercase'] and not has_lower:
            validation_result['errors'].append("Password must contain lowercase letters")
        elif has_lower:
            validation_result['strength_score'] += 15
        
        if self.password_policy['require_numbers'] and not has_digit:
            validation_result['errors'].append("Password must contain numbers")
        elif has_digit:
            validation_result['strength_score'] += 20
        
        if self.password_policy['require_special'] and not has_special:
            validation_result['errors'].append("Password must contain special characters")
        elif has_special:
            validation_result['strength_score'] += 20
        
        # Common password check (simplified)
        common_passwords = [
            'password', '123456', 'password123', 'admin', 'qwerty',
            'letmein', 'welcome', 'monkey', '1234567890'
        ]
        
        if password.lower() in common_passwords:
            validation_result['errors'].append("Password is too common")
            validation_result['strength_score'] = 0
        
        # Set validity
        validation_result['valid'] = len(validation_result['errors']) == 0
        
        return validation_result
    
    def hash_password(self, password: str) -> str:
        """Hash password securely with salt"""
        
        # Validate password strength first
        validation = self.validate_password_strength(password)
        if not validation['valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['errors'])}")
        
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def check_rate_limit(self, identifier: str, action: str, limit: int, window: int) -> bool:
        """Rate limiting for authentication attempts"""
        
        key = f"rate_limit:{action}:{identifier}"
        current_time = int(time.time())
        window_start = current_time - window
        
        try:
            # Remove old entries
            self.redis_client.zremrangebyscore(key, 0, window_start)
            
            # Count recent attempts
            recent_attempts = self.redis_client.zcard(key)
            
            if recent_attempts >= limit:
                logger.warning(f"⚠️ Rate limit exceeded for {identifier} on {action}")
                return False
            
            # Add current attempt
            self.redis_client.zadd(key, {str(current_time): current_time})
            self.redis_client.expire(key, window)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Rate limiting error: {str(e)}")
            return True  # Allow on Redis errors (fail open)
    
    def create_access_token(self, data: Dict[str, Any]) -> str:
        """Create JWT access token"""
        
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire, "type": "access"})
        
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
    
    def create_refresh_token(self, data: Dict[str, Any]) -> str:
        """Create JWT refresh token"""
        
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=self.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "type": "refresh"})
        
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
    
    def verify_token(self, token: str, token_type: str = "access") -> Dict[str, Any]:
        """Verify and decode JWT token"""
        
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            
            # Check token type
            if payload.get("type") != token_type:
                raise JWTError("Invalid token type")
            
            return payload
            
        except JWTError as e:
            logger.warning(f"⚠️ Token verification failed: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    def revoke_token(self, token: str) -> bool:
        """Revoke token (add to blacklist)"""
        
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            jti = payload.get("jti", hashlib.sha256(token.encode()).hexdigest())
            exp = payload.get("exp", int(time.time()) + 3600)
            
            # Add to blacklist with expiration
            self.redis_client.setex(f"blacklist:{jti}", exp - int(time.time()), "revoked")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Token revocation failed: {str(e)}")
            return False
    
    def is_token_blacklisted(self, token: str) -> bool:
        """Check if token is blacklisted"""
        
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            jti = payload.get("jti", hashlib.sha256(token.encode()).hexdigest())
            
            return self.redis_client.exists(f"blacklist:{jti}")
            
        except:
            return False

# Authentication endpoints
auth_handler = SecureAuthentication()
security = HTTPBearer()

@app.post("/auth/register")
async def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    request: Request = None
):
    """Secure user registration"""
    
    # Rate limiting
    client_ip = request.client.host
    if not auth_handler.check_rate_limit(client_ip, "register", 5, 300):  # 5 attempts per 5 minutes
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many registration attempts. Please try again later."
        )
    
    # Validate input
    if len(username) < 3 or len(username) > 50:
        raise HTTPException(status_code=400, detail="Username must be 3-50 characters")
    
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    # Hash password securely
    try:
        hashed_password = auth_handler.hash_password(password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # TODO: Save user to database
    # user = create_user(username, email, hashed_password)
    
    return {
        "message": "User registered successfully",
        "username": username,
        "email": email
    }

@app.post("/auth/login")
async def login_user(
    username: str = Form(...),
    password: str = Form(...),
    request: Request = None
):
    """Secure user login"""
    
    # Rate limiting
    client_ip = request.client.host
    if not auth_handler.check_rate_limit(client_ip, "login", 5, 300):  # 5 attempts per 5 minutes
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login attempts. Please try again later."
        )
    
    # Additional rate limiting per user
    if not auth_handler.check_rate_limit(username, "user_login", 3, 600):  # 3 per 10 minutes per user
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login attempts for this account. Please try again later."
        )
    
    # TODO: Get user from database
    # user = get_user_by_username(username)
    
    # Simulate user lookup (replace with actual database call)
    user = {
        'id': 1,
        'username': username,
        'email': 'user@example.com',
        'hashed_password': auth_handler.hash_password('correct_password'),  # Example
        'is_active': True,
        'is_verified': True
    }
    
    # Verify user exists and is active
    if not user or not user['is_active']:
        # Use generic error to prevent user enumeration
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Verify password
    if not auth_handler.verify_password(password, user['hashed_password']):
        logger.warning(f"⚠️ Failed login attempt for user: {username} from IP: {client_ip}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Create tokens
    token_data = {
        "sub": str(user['id']),
        "username": user['username'],
        "jti": secrets.token_urlsafe(32)  # Unique token ID for revocation
    }
    
    access_token = auth_handler.create_access_token(token_data)
    refresh_token = auth_handler.create_refresh_token(token_data)
    
    logger.info(f"✅ Successful login for user: {username} from IP: {client_ip}")
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": auth_handler.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current authenticated user"""
    
    token = credentials.credentials
    
    # Check if token is blacklisted
    if auth_handler.is_token_blacklisted(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been revoked"
        )
    
    # Verify token
    payload = auth_handler.verify_token(token, "access")
    
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    # TODO: Get user from database
    # user = get_user_by_id(user_id)
    
    # Simulate user lookup
    user = {
        'id': int(user_id),
        'username': payload.get('username'),
        'is_active': True
    }
    
    if not user or not user['is_active']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive"
        )
    
    return user
```

**3. Sensitive Data Exposure Prevention:**

```python
# data_protection.py
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import json
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)

class DataProtection:
    """Protect sensitive data with encryption"""
    
    def __init__(self):
        # Get encryption key from environment or generate
        self.encryption_key = self._get_or_create_key()
        self.fernet = Fernet(self.encryption_key)
        
        # Fields that should be encrypted
        self.encrypted_fields = {
            'ssn', 'social_security_number',
            'credit_card', 'card_number',
            'phone_number', 'phone',
            'personal_data', 'sensitive_info'
        }
        
        # Fields that should be masked in logs
        self.masked_fields = {
            'password', 'token', 'secret',
            'api_key', 'private_key',
            'ssn', 'credit_card'
        }
    
    def _get_or_create_key(self) -> bytes:
        """Get encryption key from environment or create new one"""
        
        key_env = os.getenv('DATA_ENCRYPTION_KEY')
        if key_env:
            return base64.urlsafe_b64decode(key_env.encode())
        
        # Generate new key (in production, store securely)
        password = os.getenv('ENCRYPTION_PASSWORD', 'default-password').encode()
        salt = os.getenv('ENCRYPTION_SALT', 'default-salt').encode()
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password))
        logger.warning("⚠️ Generated new encryption key - store securely!")
        
        return key
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        
        if not data:
            return data
        
        try:
            encrypted_data = self.fernet.encrypt(data.encode())
            return base64.urlsafe_b64encode(encrypted_data).decode()
        except Exception as e:
            logger.error(f"❌ Encryption failed: {str(e)}")
            raise ValueError("Failed to encrypt data")
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        
        if not encrypted_data:
            return encrypted_data
        
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted_data = self.fernet.decrypt(decoded_data)
            return decrypted_data.decode()
        except Exception as e:
            logger.error(f"❌ Decryption failed: {str(e)}")
            raise ValueError("Failed to decrypt data")
    
    def process_user_data(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process user data with automatic encryption"""
        
        processed_data = user_data.copy()
        
        for field, value in user_data.items():
            if field.lower() in self.encrypted_fields and value:
                processed_data[field] = self.encrypt_sensitive_data(str(value))
                logger.info(f"🔒 Encrypted field: {field}")
        
        return processed_data
    
    def mask_sensitive_logs(self, log_data: Dict[str, Any]) -> Dict[str, Any]:
        """Mask sensitive data in logs"""
        
        masked_data = {}
        
        for key, value in log_data.items():
            if key.lower() in self.masked_fields:
                if isinstance(value, str) and len(value) > 4:
                    # Show only first 2 and last 2 characters
                    masked_data[key] = f"{value[:2]}***{value[-2:]}"
                else:
                    masked_data[key] = "***"
            else:
                masked_data[key] = value
        
        return masked_data
    
    def secure_compare(self, a: str, b: str) -> bool:
        """Timing-safe string comparison"""
        
        import hmac
        return hmac.compare_digest(a.encode('utf-8'), b.encode('utf-8'))

# Data protection middleware
data_protector = DataProtection()

class SecurityHeaders:
    """Security headers middleware"""
    
    @staticmethod
    def get_security_headers() -> Dict[str, str]:
        """Get comprehensive security headers"""
        
        return {
            # XSS Protection
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            
            # HTTPS enforcement
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            
            # Content Security Policy
            "Content-Security-Policy": (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
                "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
                "font-src 'self' https://fonts.gstatic.com; "
                "img-src 'self' data: https:; "
                "connect-src 'self'; "
                "frame-ancestors 'none';"
            ),
            
            # Referrer policy
            "Referrer-Policy": "strict-origin-when-cross-origin",
            
            # Permissions policy
            "Permissions-Policy": (
                "geolocation=(), "
                "microphone=(), "
                "camera=()"
            ),
            
            # Cache control for sensitive pages
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Add security headers to all responses"""
    
    response = await call_next(request)
    
    # Add security headers
    security_headers = SecurityHeaders.get_security_headers()
    for header, value in security_headers.items():
        response.headers[header] = value
    
    return response
```

---

### 2️⃣ Input Validation and Sanitization (10 minutes)

**Comprehensive Input Validation:**

```python
# input_validation.py
from pydantic import BaseModel, validator, Field
from typing import Optional, List, Dict, Any
import re
import html
import bleach
from urllib.parse import urlparse
import ipaddress

class SecureInputValidator:
    """Comprehensive input validation and sanitization"""
    
    @staticmethod
    def sanitize_html_input(content: str, allowed_tags: List[str] = None) -> str:
        """Sanitize HTML content to prevent XSS"""
        
        if not content:
            return ""
        
        # Default allowed tags for rich text
        default_allowed_tags = [
            'p', 'br', 'strong', 'em', 'u', 'ol', 'ul', 'li',
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'blockquote', 'code', 'pre'
        ]
        
        allowed_tags = allowed_tags or default_allowed_tags
        
        # Allowed attributes for tags
        allowed_attributes = {
            'a': ['href', 'title'],
            'img': ['src', 'alt', 'width', 'height'],
            'code': ['class']
        }
        
        # Clean HTML with bleach
        cleaned_content = bleach.clean(
            content,
            tags=allowed_tags,
            attributes=allowed_attributes,
            strip=True  # Remove disallowed tags entirely
        )
        
        return cleaned_content
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email address format"""
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))
    
    @staticmethod
    def validate_url(url: str, allowed_schemes: List[str] = None) -> Dict[str, Any]:
        """Validate URL and check for security issues"""
        
        if not url:
            return {'valid': False, 'error': 'URL is empty'}
        
        allowed_schemes = allowed_schemes or ['http', 'https']
        
        try:
            parsed = urlparse(url)
            
            # Check scheme
            if parsed.scheme not in allowed_schemes:
                return {
                    'valid': False, 
                    'error': f'Scheme not allowed: {parsed.scheme}'
                }
            
            # Check for localhost/private IPs (prevent SSRF)
            if parsed.hostname:
                try:
                    ip = ipaddress.ip_address(parsed.hostname)
                    if ip.is_private or ip.is_loopback:
                        return {
                            'valid': False,
                            'error': 'Private/localhost URLs not allowed'
                        }
                except ValueError:
                    # Not an IP address, check hostname
                    forbidden_hosts = [
                        'localhost', '127.0.0.1', '0.0.0.0',
                        'metadata.google.internal',  # Cloud metadata
                        '169.254.169.254'  # AWS metadata
                    ]
                    
                    if parsed.hostname.lower() in forbidden_hosts:
                        return {
                            'valid': False,
                            'error': 'Forbidden hostname'
                        }
            
            return {
                'valid': True,
                'parsed': parsed,
                'clean_url': parsed.geturl()
            }
            
        except Exception as e:
            return {'valid': False, 'error': f'Invalid URL: {str(e)}'}
    
    @staticmethod
    def validate_phone_number(phone: str, country_code: str = None) -> Dict[str, Any]:
        """Validate phone number format"""
        
        if not phone:
            return {'valid': False, 'error': 'Phone number is empty'}
        
        # Remove all non-digit characters
        digits_only = re.sub(r'\D', '', phone)
        
        # Basic validation
        if len(digits_only) < 10 or len(digits_only) > 15:
            return {
                'valid': False,
                'error': 'Phone number must be 10-15 digits'
            }
        
        # Format validation by country (simplified)
        patterns = {
            'US': r'^\+?1?[2-9]\d{2}[2-9]\d{2}\d{4}$',
            'UK': r'^\+?44[1-9]\d{8,9}$',
            'international': r'^\+?[1-9]\d{10,14}$'
        }
        
        pattern = patterns.get(country_code, patterns['international'])
        
        if not re.match(pattern, phone):
            return {
                'valid': False,
                'error': f'Invalid phone format for {country_code or "international"}'
            }
        
        return {
            'valid': True,
            'formatted': digits_only,
            'display': f"+{digits_only}" if not phone.startswith('+') else phone
        }

# Pydantic models with validation
class SecureUserInput(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., max_length=254)
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    website: Optional[str] = Field(None, max_length=200)
    phone: Optional[str] = Field(None, max_length=20)
    
    @validator('username')
    def validate_username(cls, v):
        """Validate username format"""
        
        # Only alphanumeric, underscore, hyphen allowed
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Username can only contain letters, numbers, underscore, and hyphen')
        
        # Check for reserved usernames
        reserved = [
            'admin', 'root', 'administrator', 'moderator',
            'api', 'www', 'mail', 'ftp', 'support'
        ]
        
        if v.lower() in reserved:
            raise ValueError('Username is reserved')
        
        return v.lower()  # Normalize to lowercase
    
    @validator('email')
    def validate_email_format(cls, v):
        """Validate email format"""
        
        if not SecureInputValidator.validate_email(v):
            raise ValueError('Invalid email format')
        
        return v.lower()  # Normalize to lowercase
    
    @validator('full_name')
    def sanitize_full_name(cls, v):
        """Sanitize full name"""
        
        if not v:
            return v
        
        # Remove HTML and dangerous characters
        sanitized = html.escape(v.strip())
        
        # Only allow letters, spaces, hyphens, apostrophes
        if not re.match(r"^[a-zA-Z\s\-']+$", sanitized):
            raise ValueError('Full name contains invalid characters')
        
        return sanitized
    
    @validator('bio')
    def sanitize_bio(cls, v):
        """Sanitize bio content"""
        
        if not v:
            return v
        
        # Allow basic formatting but remove dangerous content
        sanitized = SecureInputValidator.sanitize_html_input(
            v,
            allowed_tags=['p', 'br', 'strong', 'em']
        )
        
        return sanitized
    
    @validator('website')
    def validate_website_url(cls, v):
        """Validate website URL"""
        
        if not v:
            return v
        
        url_validation = SecureInputValidator.validate_url(v, ['http', 'https'])
        
        if not url_validation['valid']:
            raise ValueError(f"Invalid website URL: {url_validation['error']}")
        
        return url_validation['clean_url']
    
    @validator('phone')
    def validate_phone_format(cls, v):
        """Validate phone number"""
        
        if not v:
            return v
        
        phone_validation = SecureInputValidator.validate_phone_number(v)
        
        if not phone_validation['valid']:
            raise ValueError(f"Invalid phone number: {phone_validation['error']}")
        
        return phone_validation['formatted']

class SecurePostInput(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1, max_length=10000)
    tags: Optional[List[str]] = Field(None, max_items=10)
    category: Optional[str] = Field(None, max_length=50)
    is_published: bool = False
    
    @validator('title')
    def sanitize_title(cls, v):
        """Sanitize post title"""
        
        # Remove HTML and normalize whitespace
        sanitized = html.escape(v.strip())
        sanitized = re.sub(r'\s+', ' ', sanitized)
        
        return sanitized
    
    @validator('content')
    def sanitize_content(cls, v):
        """Sanitize post content"""
        
        # Allow rich text formatting but sanitize
        sanitized = SecureInputValidator.sanitize_html_input(
            v,
            allowed_tags=[
                'p', 'br', 'strong', 'em', 'u', 'ol', 'ul', 'li',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                'blockquote', 'code', 'pre', 'a'
            ]
        )
        
        return sanitized
    
    @validator('tags')
    def sanitize_tags(cls, v):
        """Sanitize and validate tags"""
        
        if not v:
            return v
        
        sanitized_tags = []
        
        for tag in v:
            # Remove HTML and normalize
            clean_tag = html.escape(tag.strip().lower())
            
            # Validate tag format (letters, numbers, hyphens only)
            if re.match(r'^[a-zA-Z0-9-]+$', clean_tag) and len(clean_tag) <= 30:
                sanitized_tags.append(clean_tag)
        
        # Remove duplicates
        return list(set(sanitized_tags))
    
    @validator('category')
    def validate_category(cls, v):
        """Validate category"""
        
        if not v:
            return v
        
        # Predefined allowed categories
        allowed_categories = [
            'technology', 'science', 'business', 'health',
            'entertainment', 'sports', 'politics', 'lifestyle'
        ]
        
        clean_category = v.strip().lower()
        
        if clean_category not in allowed_categories:
            raise ValueError(f'Invalid category. Allowed: {", ".join(allowed_categories)}')
        
        return clean_category
```

---

### 3️⃣ CORS and CSRF Protection (10 minutes)

**CORS and CSRF Implementation:**

```python
# security_middleware.py
from fastapi import Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import secrets
import time
from typing import Dict, List
import hmac
import hashlib

class CSRFProtection:
    """CSRF protection middleware"""
    
    def __init__(self, secret_key: str = None):
        self.secret_key = secret_key or secrets.token_urlsafe(32)
        self.token_lifetime = 3600  # 1 hour
    
    def generate_csrf_token(self, session_id: str) -> str:
        """Generate CSRF token for session"""
        
        timestamp = str(int(time.time()))
        message = f"{session_id}:{timestamp}"
        
        signature = hmac.new(
            self.secret_key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        token = f"{message}:{signature}"
        return base64.urlsafe_b64encode(token.encode()).decode()
    
    def validate_csrf_token(self, token: str, session_id: str) -> bool:
        """Validate CSRF token"""
        
        try:
            decoded_token = base64.urlsafe_b64decode(token.encode()).decode()
            parts = decoded_token.split(':')
            
            if len(parts) != 3:
                return False
            
            token_session_id, timestamp, signature = parts
            
            # Check session ID matches
            if token_session_id != session_id:
                return False
            
            # Check token age
            token_time = int(timestamp)
            if time.time() - token_time > self.token_lifetime:
                return False
            
            # Verify signature
            message = f"{token_session_id}:{timestamp}"
            expected_signature = hmac.new(
                self.secret_key.encode(),
                message.encode(),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature, expected_signature)
            
        except Exception:
            return False

class SecurityMiddleware(BaseHTTPMiddleware):
    """Comprehensive security middleware"""
    
    def __init__(self, app, allowed_hosts: List[str] = None):
        super().__init__(app)
        self.allowed_hosts = allowed_hosts or ['localhost', '127.0.0.1']
        self.csrf_protection = CSRFProtection()
        
        # Rate limiting storage (use Redis in production)
        self.rate_limit_storage = {}
    
    async def dispatch(self, request: Request, call_next):
        """Apply security checks to all requests"""
        
        # 1. Host header validation
        if not self._validate_host_header(request):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Host header"
            )
        
        # 2. Content type validation for POST/PUT requests
        if request.method in ["POST", "PUT", "PATCH"]:
            if not self._validate_content_type(request):
                raise HTTPException(
                    status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                    detail="Unsupported content type"
                )
        
        # 3. CSRF protection for state-changing operations
        if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            if not await self._validate_csrf(request):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="CSRF token missing or invalid"
                )
        
        # 4. Request size validation
        if not await self._validate_request_size(request):
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="Request body too large"
            )
        
        # Process request
        response = await call_next(request)
        
        # Add security headers
        self._add_security_headers(response)
        
        return response
    
    def _validate_host_header(self, request: Request) -> bool:
        """Validate Host header to prevent Host header injection"""
        
        host = request.headers.get("host", "").lower()
        
        if not host:
            return False
        
        # Extract hostname (remove port if present)
        hostname = host.split(':')[0]
        
        return hostname in self.allowed_hosts
    
    def _validate_content_type(self, request: Request) -> bool:
        """Validate Content-Type header"""
        
        content_type = request.headers.get("content-type", "").lower()
        
        allowed_types = [
            'application/json',
            'application/x-www-form-urlencoded',
            'multipart/form-data',
            'text/plain'
        ]
        
        # Check if content type starts with allowed type
        return any(content_type.startswith(allowed) for allowed in allowed_types)
    
    async def _validate_csrf(self, request: Request) -> bool:
        """Validate CSRF token"""
        
        # Skip CSRF for API endpoints with proper authentication
        if request.url.path.startswith('/api/'):
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                return True  # API endpoints use token auth instead of CSRF
        
        # Get CSRF token from header or form data
        csrf_token = request.headers.get('X-CSRF-Token')
        
        if not csrf_token:
            # Try to get from form data
            if hasattr(request, 'form'):
                form = await request.form()
                csrf_token = form.get('csrf_token')
        
        if not csrf_token:
            return False
        
        # Get session ID (in production, use actual session)
        session_id = request.cookies.get('session_id', 'default_session')
        
        return self.csrf_protection.validate_csrf_token(csrf_token, session_id)
    
    async def _validate_request_size(self, request: Request) -> bool:
        """Validate request body size"""
        
        content_length = request.headers.get('content-length')
        
        if content_length:
            try:
                size = int(content_length)
                max_size = 50 * 1024 * 1024  # 50MB limit
                
                return size <= max_size
            except ValueError:
                return False
        
        return True
    
    def _add_security_headers(self, response):
        """Add security headers to response"""
        
        security_headers = {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        
        for header, value in security_headers.items():
            response.headers[header] = value

# Configure CORS properly
def setup_cors(app):
    """Setup CORS with secure configuration"""
    
    # Production CORS settings
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://yourdomain.com",
            "https://app.yourdomain.com",
            # Add your trusted domains
        ],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=[
            "Authorization",
            "Content-Type", 
            "X-CSRF-Token",
            "X-Requested-With"
        ],
        expose_headers=["X-CSRF-Token"],
        max_age=3600,  # Cache preflight for 1 hour
    )

# CSRF token endpoints
@app.get("/auth/csrf-token")
async def get_csrf_token(request: Request):
    """Get CSRF token for forms"""
    
    session_id = request.cookies.get('session_id', 'default_session')
    
    csrf_middleware = SecurityMiddleware(None)
    csrf_token = csrf_middleware.csrf_protection.generate_csrf_token(session_id)
    
    return {
        "csrf_token": csrf_token,
        "expires_in": 3600
    }
```

---

### 4️⃣ API Security Implementation (10 minutes)

**Secure API Design:**

```python
# secure_api.py
from fastapi import Depends, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import hashlib
import hmac
from datetime import datetime
import json

# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# API Key authentication
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
api_key_query = APIKeyQuery(name="api_key", auto_error=False)

class APIKeyManager:
    """Manage API keys securely"""
    
    def __init__(self):
        # In production, store in database with proper encryption
        self.api_keys = {
            "test_key_123": {
                "user_id": 1,
                "name": "Test Application",
                "permissions": ["read", "write"],
                "rate_limit": 100,  # requests per minute
                "is_active": True,
                "created_at": datetime.now()
            }
        }
    
    def validate_api_key(self, api_key: str) -> Dict[str, Any]:
        """Validate API key and return key info"""
        
        if not api_key:
            return None
        
        # Hash the API key for comparison (if stored hashed)
        key_hash = hashlib.sha256(api_key.encode()).hexdigest()
        
        key_info = self.api_keys.get(api_key)
        
        if key_info and key_info.get('is_active', False):
            return key_info
        
        return None
    
    def check_api_permissions(self, key_info: Dict[str, Any], required_permission: str) -> bool:
        """Check if API key has required permission"""
        
        permissions = key_info.get('permissions', [])
        return required_permission in permissions or 'admin' in permissions

api_key_manager = APIKeyManager()

async def get_api_key(
    api_key_header: str = Security(api_key_header),
    api_key_query: str = Security(api_key_query)
) -> Dict[str, Any]:
    """Validate API key from header or query parameter"""
    
    api_key = api_key_header or api_key_query
    
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key required",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    
    key_info = api_key_manager.validate_api_key(api_key)
    
    if not key_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired API key"
        )
    
    return key_info

# Webhook signature validation
class WebhookValidator:
    """Validate webhook signatures"""
    
    @staticmethod
    def validate_github_signature(payload: bytes, signature: str, secret: str) -> bool:
        """Validate GitHub webhook signature"""
        
        if not signature.startswith('sha256='):
            return False
        
        expected_signature = hmac.new(
            secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        received_signature = signature[7:]  # Remove 'sha256=' prefix
        
        return hmac.compare_digest(expected_signature, received_signature)
    
    @staticmethod
    def validate_stripe_signature(payload: bytes, sig_header: str, endpoint_secret: str) -> bool:
        """Validate Stripe webhook signature"""
        
        try:
            import stripe
            stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
            return True
        except (stripe.error.SignatureVerificationError, ValueError):
            return False

# Secure API endpoints with comprehensive protection
@app.post("/api/v1/posts")
@limiter.limit("10/minute")  # Rate limiting
async def create_post(
    request: Request,
    post_data: SecurePostInput,
    api_key_info: Dict[str, Any] = Depends(get_api_key),
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    """Create post with comprehensive security"""
    
    # Check API permissions
    if not api_key_manager.check_api_permissions(api_key_info, "write"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient API permissions"
        )
    
    # Input validation is handled by Pydantic model (SecurePostInput)
    
    # Log the action (with masked sensitive data)
    log_data = {
        'action': 'create_post',
        'user_id': current_user['id'],
        'api_key': api_key_info.get('name', 'Unknown'),
        'ip_address': request.client.host,
        'timestamp': datetime.now().isoformat(),
        'post_title': post_data.title[:50],  # Only log first 50 chars
    }
    
    logger.info(f"📝 Post creation: {json.dumps(log_data)}")
    
    # Create post (database logic would go here)
    post_id = f"post_{secrets.token_urlsafe(8)}"
    
    return {
        "message": "Post created successfully",
        "post_id": post_id,
        "title": post_data.title
    }

@app.webhook("/webhooks/github")
async def github_webhook(request: Request):
    """Secure GitHub webhook handler"""
    
    # Get signature
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        raise HTTPException(status_code=400, detail="Missing signature")
    
    # Get payload
    payload = await request.body()
    
    # Validate signature
    webhook_secret = os.getenv('GITHUB_WEBHOOK_SECRET')
    if not WebhookValidator.validate_github_signature(payload, signature, webhook_secret):
        logger.warning(f"⚠️ Invalid GitHub webhook signature from {request.client.host}")
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Process webhook
    try:
        data = json.loads(payload.decode())
        event_type = request.headers.get('X-GitHub-Event')
        
        logger.info(f"📨 GitHub webhook received: {event_type}")
        
        # Handle different event types
        if event_type == 'push':
            # Handle push events
            pass
        elif event_type == 'pull_request':
            # Handle PR events
            pass
        
        return {"status": "success", "event": event_type}
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

# Security monitoring endpoint
@app.get("/admin/security/logs")
async def get_security_logs(
    current_user: Dict[str, Any] = Depends(get_current_user),
    api_key_info: Dict[str, Any] = Depends(get_api_key)
):
    """Get security logs (admin only)"""
    
    # Check admin permissions
    if not api_key_manager.check_api_permissions(api_key_info, "admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    # In production, fetch from security logging system
    security_logs = [
        {
            "timestamp": "2024-01-15T10:30:00Z",
            "event": "login_attempt",
            "status": "failed",
            "ip": "192.168.1.100",
            "user_agent": "Mozilla/5.0..."
        },
        {
            "timestamp": "2024-01-15T10:25:00Z",
            "event": "rate_limit_exceeded",
            "ip": "10.0.0.5",
            "endpoint": "/api/v1/posts"
        }
    ]
    
    return {
        "logs": security_logs,
        "total": len(security_logs)
    }
```

---

### 🏠 Homework: Implement Security Fortress

**Task:** Build comprehensive security for your blog application

```python
# Implement complete security measures:
# 1. OWASP Top 10 protection (all vulnerabilities)
# 2. Secure authentication with MFA support
# 3. Comprehensive input validation and sanitization
# 4. CORS and CSRF protection
# 5. API security with rate limiting and key management
# 6. Security headers and middleware
# 7. Audit logging and monitoring
# 8. Vulnerability scanning integration

# Requirements:
# - Password policy enforcement
# - Session management with secure cookies
# - SQL injection prevention
# - XSS protection with CSP
# - File upload security
# - API rate limiting
# - Security incident response

# Bonus:
# - Implement security dashboard
# - Add intrusion detection
# - Create security audit reports
# - Integrate with security scanning tools
```

---

### 📝 Key Takeaways

✅ OWASP Top 10 = Essential security checklist for web apps
✅ Input Validation = Never trust user input, validate everything
✅ Authentication = Multi-layered security with proper sessions
✅ CORS & CSRF = Protect against cross-origin attacks
✅ API Security = Rate limiting, authentication, and monitoring

---

<a name="hour-37"></a>
## 📅 Hour 37: GraphQL Introduction

### 🎯 Learning Objectives
- Understand GraphQL concepts vs REST APIs
- Implement GraphQL schema and resolvers
- Handle queries, mutations, and subscriptions
- Add authentication and authorization to GraphQL
- Optimize GraphQL performance and prevent common issues

### 📖 What to Teach

**"Today we master GraphQL - the query language that lets clients ask for exactly what they need!"**

---

### 1️⃣ GraphQL vs REST Comparison (10 minutes)

**REST API Problems GraphQL Solves:**

```python
# REST API - Multiple requests needed
"""
❌ REST API Problems:

1. Over-fetching:
   GET /api/users/123
   Returns: { id, name, email, bio, avatar, created_at, updated_at, settings... }
   Client only needs: { id, name, email }

2. Under-fetching:
   GET /api/posts/456           # Get post
   GET /api/users/123           # Get author info
   GET /api/posts/456/comments  # Get comments
   GET /api/comments/*/authors  # Get comment authors
   
   4 requests to show a blog post with comments!

3. API Versioning:
   /api/v1/users vs /api/v2/users
   Multiple versions to maintain

4. Fixed Response Structure:
   Can't customize what fields to include
"""

# GraphQL - Single request with exact data
"""
✅ GraphQL Solutions:

1. Exact Data Fetching:
   query {
     user(id: 123) {
       id
       name
       email
     }
   }
   Returns exactly: { "user": { "id": 123, "name": "John", "email": "john@example.com" }}

2. Single Request for Complex Data:
   query {
     post(id: 456) {
       title
       content
       author {
         name
         avatar
       }
       comments {
         content
         author {
           name
         }
       }
     }
   }

3. No Versioning Needed:
   Schema evolution without breaking existing clients

4. Flexible Response Structure:
   Client specifies exactly what they need
"""
```

**When to Use GraphQL vs REST:**

```python
# Use GraphQL when:
graphql_use_cases = {
    "Mobile Applications": "Reduce bandwidth and battery usage",
    "Complex UIs": "Many interconnected data requirements", 
    "Rapid Development": "Frontend teams need flexible data fetching",
    "Multiple Clients": "Different apps need different data subsets",
    "Real-time Features": "Built-in subscription support",
    "Developer Experience": "Self-documenting schema and tooling"
}

# Use REST when:
rest_use_cases = {
    "Simple CRUD": "Basic create, read, update, delete operations",
    "File Operations": "File uploads, downloads, streaming",
    "Caching": "HTTP caching is critical",
    "Team Familiarity": "Team is not ready for GraphQL complexity",
    "Third-party Integration": "Existing REST services integration",
    "Microservices": "Service-to-service communication"
}

# GraphQL Benefits:
benefits = """
✅ Single endpoint (/graphql)
✅ Client specifies data requirements
✅ Strongly typed schema
✅ Introspection and tooling
✅ Real-time subscriptions
✅ No over/under fetching
✅ Backward compatible evolution
"""

# GraphQL Challenges:
challenges = """
⚠️ Learning curve and complexity
⚠️ Caching is more complex
⚠️ File uploads need special handling
⚠️ Query complexity attacks
⚠️ N+1 query problems
⚠️ HTTP status codes less meaningful
"""
```

---

### 2️⃣ GraphQL Schema and Resolvers (15 minutes)

**Setting up GraphQL with Strawberry:**

```bash
# Install GraphQL dependencies
pip install strawberry-graphql[fastapi] graphql-core
```

**Schema Definition:**

```python
# graphql_schema.py
import strawberry
from typing import List, Optional, AsyncGenerator
from datetime import datetime
import asyncio
from dataclasses import dataclass

# Type Definitions
@strawberry.type
class User:
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime
    is_active: bool
    
    # Computed field
    @strawberry.field
    def display_name(self) -> str:
        return self.full_name or self.username

@strawberry.type 
class Post:
    id: int
    title: str
    content: str
    excerpt: Optional[str] = None
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    published: bool = False
    tags: List[str] = strawberry.field(default_factory=list)
    
    # Relationship fields (resolved separately)
    @strawberry.field
    async def author(self, info) -> User:
        """Get post author - this is a resolver"""
        # Access the database through context
        db = info.context["db"]
        user_service = info.context["user_service"]
        
        return await user_service.get_user_by_id(self.author_id)
    
    @strawberry.field
    async def comments(self, info) -> List["Comment"]:
        """Get post comments"""
        comment_service = info.context["comment_service"] 
        return await comment_service.get_comments_by_post_id(self.id)
    
    @strawberry.field
    def word_count(self) -> int:
        """Computed field for word count"""
        return len(self.content.split())

@strawberry.type
class Comment:
    id: int
    content: str
    post_id: int
    author_id: int
    created_at: datetime
    parent_id: Optional[int] = None  # For nested comments
    
    @strawberry.field
    async def author(self, info) -> User:
        user_service = info.context["user_service"]
        return await user_service.get_user_by_id(self.author_id)
    
    @strawberry.field
    async def replies(self, info) -> List["Comment"]:
        """Get nested replies to this comment"""
        comment_service = info.context["comment_service"]
        return await comment_service.get_replies(self.id)

# Input Types for Mutations
@strawberry.input
class CreatePostInput:
    title: str
    content: str
    tags: Optional[List[str]] = None
    published: bool = False

@strawberry.input
class UpdatePostInput:
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    published: Optional[bool] = None

@strawberry.input
class CreateCommentInput:
    content: str
    post_id: int
    parent_id: Optional[int] = None

# Custom Scalars
@strawberry.scalar(
    serialize=lambda v: v.isoformat(),
    parse_value=lambda v: datetime.fromisoformat(v)
)
class DateTime:
    """Custom DateTime scalar"""
    pass

# Pagination Types
@strawberry.type
class PageInfo:
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str] = None
    end_cursor: Optional[str] = None

@strawberry.type
class PostConnection:
    edges: List["PostEdge"]
    page_info: PageInfo
    total_count: int

@strawberry.type
class PostEdge:
    node: Post
    cursor: str

# Error Types
@strawberry.type
class ValidationError:
    field: str
    message: str

@strawberry.type
class PostResult:
    post: Optional[Post] = None
    errors: List[ValidationError] = strawberry.field(default_factory=list)
```

**Query Resolvers:**

```python
# graphql_queries.py
from typing import List, Optional
import strawberry

@strawberry.type
class Query:
    """GraphQL Query root"""
    
    @strawberry.field
    async def users(
        self, 
        info,
        first: Optional[int] = 10,
        search: Optional[str] = None
    ) -> List[User]:
        """Get list of users with optional search"""
        
        user_service = info.context["user_service"]
        
        # Apply search filter if provided
        if search:
            return await user_service.search_users(search, limit=first)
        
        return await user_service.get_users(limit=first)
    
    @strawberry.field
    async def user(self, info, id: int) -> Optional[User]:
        """Get user by ID"""
        
        user_service = info.context["user_service"]
        return await user_service.get_user_by_id(id)
    
    @strawberry.field
    async def posts(
        self,
        info,
        first: Optional[int] = 10,
        after: Optional[str] = None,
        author_id: Optional[int] = None,
        published_only: bool = True,
        search: Optional[str] = None
    ) -> PostConnection:
        """Get paginated posts with filtering"""
        
        post_service = info.context["post_service"]
        
        # Build filters
        filters = {
            "limit": first,
            "after_cursor": after,
            "author_id": author_id,
            "published_only": published_only,
            "search": search
        }
        
        result = await post_service.get_posts_paginated(**filters)
        
        # Convert to GraphQL connection format
        edges = [
            PostEdge(node=post, cursor=post_service.encode_cursor(post.id))
            for post in result["posts"]
        ]
        
        page_info = PageInfo(
            has_next_page=result["has_next"],
            has_previous_page=result["has_previous"],
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None
        )
        
        return PostConnection(
            edges=edges,
            page_info=page_info,
            total_count=result["total_count"]
        )
    
    @strawberry.field
    async def post(self, info, id: int) -> Optional[Post]:
        """Get single post by ID"""
        
        post_service = info.context["post_service"]
        return await post_service.get_post_by_id(id)
    
    @strawberry.field
    async def popular_tags(self, info, limit: int = 10) -> List[str]:
        """Get most popular tags"""
        
        post_service = info.context["post_service"]
        return await post_service.get_popular_tags(limit)
    
    @strawberry.field
    async def search(
        self,
        info,
        query: str,
        type: Optional[str] = None,  # "posts", "users", "all"
        limit: int = 20
    ) -> "SearchResult":
        """Universal search across content types"""
        
        search_service = info.context["search_service"]
        
        if type == "posts":
            posts = await search_service.search_posts(query, limit)
            return SearchResult(posts=posts, users=[], total_count=len(posts))
        
        elif type == "users":
            users = await search_service.search_users(query, limit)
            return SearchResult(posts=[], users=users, total_count=len(users))
        
        else:  # Search all
            results = await search_service.universal_search(query, limit)
            return SearchResult(
                posts=results["posts"],
                users=results["users"],
                total_count=results["total_count"]
            )

@strawberry.type
class SearchResult:
    posts: List[Post]
    users: List[User]
    total_count: int
```

**Mutation Resolvers:**

```python
# graphql_mutations.py
import strawberry
from typing import List

@strawberry.type
class Mutation:
    """GraphQL Mutation root"""
    
    @strawberry.field
    async def create_post(
        self,
        info,
        input: CreatePostInput
    ) -> PostResult:
        """Create a new blog post"""
        
        # Get current user from context (authentication)
        current_user = info.context.get("current_user")
        if not current_user:
            return PostResult(
                errors=[ValidationError(field="auth", message="Authentication required")]
            )
        
        # Validate input
        errors = []
        
        if not input.title or len(input.title.strip()) < 3:
            errors.append(ValidationError(
                field="title",
                message="Title must be at least 3 characters"
            ))
        
        if not input.content or len(input.content.strip()) < 10:
            errors.append(ValidationError(
                field="content", 
                message="Content must be at least 10 characters"
            ))
        
        if errors:
            return PostResult(errors=errors)
        
        # Create post
        post_service = info.context["post_service"]
        
        try:
            post = await post_service.create_post(
                title=input.title,
                content=input.content,
                author_id=current_user["id"],
                tags=input.tags or [],
                published=input.published
            )
            
            return PostResult(post=post)
            
        except Exception as e:
            return PostResult(
                errors=[ValidationError(field="general", message=str(e))]
            )
    
    @strawberry.field
    async def update_post(
        self,
        info,
        id: int,
        input: UpdatePostInput
    ) -> PostResult:
        """Update existing post"""
        
        current_user = info.context.get("current_user")
        if not current_user:
            return PostResult(
                errors=[ValidationError(field="auth", message="Authentication required")]
            )
        
        post_service = info.context["post_service"]
        
        # Check if post exists and user owns it
        existing_post = await post_service.get_post_by_id(id)
        if not existing_post:
            return PostResult(
                errors=[ValidationError(field="id", message="Post not found")]
            )
        
        if existing_post.author_id != current_user["id"]:
            return PostResult(
                errors=[ValidationError(field="auth", message="Not authorized to edit this post")]
            )
        
        # Update post
        try:
            updated_post = await post_service.update_post(id, input)
            return PostResult(post=updated_post)
            
        except Exception as e:
            return PostResult(
                errors=[ValidationError(field="general", message=str(e))]
            )
    
    @strawberry.field
    async def delete_post(self, info, id: int) -> bool:
        """Delete a post"""
        
        current_user = info.context.get("current_user")
        if not current_user:
            return False
        
        post_service = info.context["post_service"]
        
        # Check ownership
        post = await post_service.get_post_by_id(id)
        if not post or post.author_id != current_user["id"]:
            return False
        
        return await post_service.delete_post(id)
    
    @strawberry.field
    async def create_comment(
        self,
        info,
        input: CreateCommentInput
    ) -> "CommentResult":
        """Create a comment on a post"""
        
        current_user = info.context.get("current_user")
        if not current_user:
            return CommentResult(
                errors=[ValidationError(field="auth", message="Authentication required")]
            )
        
        # Validate input
        if not input.content or len(input.content.strip()) < 1:
            return CommentResult(
                errors=[ValidationError(field="content", message="Comment cannot be empty")]
            )
        
        comment_service = info.context["comment_service"]
        
        try:
            comment = await comment_service.create_comment(
                content=input.content,
                post_id=input.post_id,
                author_id=current_user["id"],
                parent_id=input.parent_id
            )
            
            return CommentResult(comment=comment)
            
        except Exception as e:
            return CommentResult(
                errors=[ValidationError(field="general", message=str(e))]
            )

@strawberry.type
class CommentResult:
    comment: Optional[Comment] = None
    errors: List[ValidationError] = strawberry.field(default_factory=list)
```

**Subscriptions for Real-time Updates:**

```python
# graphql_subscriptions.py
import strawberry
import asyncio
from typing import AsyncGenerator

@strawberry.type
class Subscription:
    """GraphQL Subscription root for real-time updates"""
    
    @strawberry.subscription
    async def post_comments(self, info, post_id: int) -> AsyncGenerator[Comment, None]:
        """Subscribe to new comments on a post"""
        
        # In production, use Redis pub/sub or WebSocket manager
        comment_service = info.context["comment_service"]
        
        # Create a subscription channel
        channel = f"post_comments_{post_id}"
        
        try:
            while True:
                # Wait for new comments (this would be event-driven in production)
                new_comment = await comment_service.wait_for_new_comment(post_id)
                
                if new_comment:
                    yield new_comment
                
                # Small delay to prevent busy waiting
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            # Cleanup subscription
            await comment_service.cleanup_subscription(channel)
            raise
    
    @strawberry.subscription
    async def user_notifications(self, info) -> AsyncGenerator["Notification", None]:
        """Subscribe to user notifications"""
        
        current_user = info.context.get("current_user")
        if not current_user:
            return
        
        notification_service = info.context["notification_service"]
        user_id = current_user["id"]
        
        try:
            async for notification in notification_service.subscribe_user_notifications(user_id):
                yield notification
                
        except asyncio.CancelledError:
            await notification_service.cleanup_user_subscription(user_id)
            raise

@strawberry.type
class Notification:
    id: int
    title: str
    message: str
    type: str  # "comment", "like", "follow", etc.
    created_at: datetime
    read: bool = False
```

---

### 3️⃣ GraphQL Performance Optimization (10 minutes)

**Solving N+1 Query Problem:**

```python
# graphql_dataloaders.py
from aiodataloader import DataLoader
from typing import List, Dict, Any
import asyncio

class UserDataLoader(DataLoader):
    """Batch load users to prevent N+1 queries"""
    
    def __init__(self, user_service):
        super().__init__()
        self.user_service = user_service
    
    async def batch_load_fn(self, user_ids: List[int]) -> List[User]:
        """Load multiple users in a single query"""
        
        # Single database query for all requested user IDs
        users = await self.user_service.get_users_by_ids(user_ids)
        
        # Create a mapping for fast lookup
        user_map = {user.id: user for user in users}
        
        # Return users in the same order as requested IDs
        return [user_map.get(user_id) for user_id in user_ids]

class PostDataLoader(DataLoader):
    """Batch load posts"""
    
    def __init__(self, post_service):
        super().__init__()
        self.post_service = post_service
    
    async def batch_load_fn(self, post_ids: List[int]) -> List[Post]:
        posts = await self.post_service.get_posts_by_ids(post_ids)
        post_map = {post.id: post for post in posts}
        return [post_map.get(post_id) for post_id in post_ids]

class CommentsByPostDataLoader(DataLoader):
    """Batch load comments by post IDs"""
    
    def __init__(self, comment_service):
        super().__init__()
        self.comment_service = comment_service
    
    async def batch_load_fn(self, post_ids: List[int]) -> List[List[Comment]]:
        """Load comments for multiple posts"""
        
        # Single query to get all comments for all posts
        all_comments = await self.comment_service.get_comments_by_post_ids(post_ids)
        
        # Group comments by post_id
        comments_by_post = {}
        for comment in all_comments:
            if comment.post_id not in comments_by_post:
                comments_by_post[comment.post_id] = []
            comments_by_post[comment.post_id].append(comment)
        
        # Return in requested order
        return [comments_by_post.get(post_id, []) for post_id in post_ids]

# Context factory with dataloaders
def create_graphql_context(request, user_service, post_service, comment_service):
    """Create GraphQL context with dataloaders"""
    
    return {
        "request": request,
        "user_service": user_service,
        "post_service": post_service,
        "comment_service": comment_service,
        
        # DataLoaders for performance
        "user_loader": UserDataLoader(user_service),
        "post_loader": PostDataLoader(post_service),
        "comments_by_post_loader": CommentsByPostDataLoader(comment_service),
        
        # Authentication context
        "current_user": getattr(request, 'user', None)
    }

# Update resolvers to use dataloaders
@strawberry.type
class OptimizedPost:
    id: int
    title: str
    content: str
    author_id: int
    
    @strawberry.field
    async def author(self, info) -> User:
        """Use dataloader to prevent N+1 queries"""
        user_loader = info.context["user_loader"]
        return await user_loader.load(self.author_id)
    
    @strawberry.field
    async def comments(self, info) -> List[Comment]:
        """Use dataloader for comments"""
        comments_loader = info.context["comments_by_post_loader"]
        return await comments_loader.load(self.id)
```

**Query Complexity Analysis:**

```python
# graphql_security.py
import strawberry
from strawberry.extensions import Extension
from typing import Dict, Any

class QueryComplexityAnalyzer(Extension):
    """Prevent overly complex GraphQL queries"""
    
    def __init__(self, max_complexity: int = 1000, max_depth: int = 10):
        self.max_complexity = max_complexity
        self.max_depth = max_depth
    
    async def on_request_start(self):
        """Analyze query before execution"""
        
        query = self.execution_context.query
        
        # Calculate query depth
        depth = self._calculate_query_depth(query)
        if depth > self.max_depth:
            raise Exception(f"Query depth {depth} exceeds maximum allowed depth {self.max_depth}")
        
        # Calculate query complexity
        complexity = self._calculate_query_complexity(query)
        if complexity > self.max_complexity:
            raise Exception(f"Query complexity {complexity} exceeds maximum allowed complexity {self.max_complexity}")
    
    def _calculate_query_depth(self, query) -> int:
        """Calculate maximum depth of GraphQL query"""
        # Implementation would parse the query AST
        # This is a simplified version
        return query.count('{') + query.count('(')
    
    def _calculate_query_complexity(self, query) -> int:
        """Calculate complexity score based on field costs"""
        
        # Define field costs
        field_costs = {
            'posts': 10,      # Expensive list query
            'users': 8,       # User list
            'comments': 5,    # Comments
            'author': 2,      # Single relation
            'user': 1,        # Single field
        }
        
        complexity = 0
        
        # Simple complexity calculation (production would use proper AST parsing)
        for field, cost in field_costs.items():
            if field in query:
                complexity += cost
        
        return complexity

class QueryDepthLimiter(Extension):
    """Limit query depth to prevent deeply nested queries"""
    
    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth
    
    def on_validate(self):
        """Validate query depth during GraphQL validation phase"""
        
        # This would integrate with GraphQL validation
        pass

# Rate limiting for GraphQL
class GraphQLRateLimit(Extension):
    """Rate limit GraphQL queries"""
    
    def __init__(self, redis_client, requests_per_minute: int = 60):
        self.redis = redis_client
        self.requests_per_minute = requests_per_minute
    
    async def on_request_start(self):
        """Check rate limit before executing query"""
        
        # Get client identifier
        request = self.execution_context.context["request"]
        client_id = request.client.host
        
        # Check rate limit
        key = f"graphql_rate_limit:{client_id}"
        current_requests = await self.redis.incr(key)
        
        if current_requests == 1:
            await self.redis.expire(key, 60)  # 1 minute window
        
        if current_requests > self.requests_per_minute:
            raise Exception("Rate limit exceeded. Please try again later.")
```

---

### 4️⃣ FastAPI Integration (10 minutes)

**Complete GraphQL FastAPI Setup:**

```python
# main.py - GraphQL FastAPI integration
from fastapi import FastAPI, Depends, HTTPException, Request
from strawberry.fastapi import GraphQLRouter
import strawberry
from contextlib import asynccontextmanager

# Create GraphQL schema
@strawberry.type
class Query:
    # Include all query resolvers
    pass

@strawberry.type  
class Mutation:
    # Include all mutation resolvers
    pass

@strawberry.type
class Subscription:
    # Include all subscription resolvers
    pass

# Create schema with security extensions
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    extensions=[
        QueryComplexityAnalyzer(max_complexity=500, max_depth=8),
        GraphQLRateLimit(redis_client, requests_per_minute=100)
    ]
)

# Authentication dependency
async def get_current_user_optional(request: Request):
    """Get current user for GraphQL context (optional)"""
    
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    
    token = auth_header.split(" ")[1]
    
    try:
        # Validate JWT token
        payload = auth_handler.verify_token(token)
        user_id = payload.get("sub")
        
        # Get user from database
        # user = await user_service.get_user_by_id(user_id)
        
        # Simulate user
        return {
            "id": int(user_id),
            "username": payload.get("username")
        }
        
    except Exception:
        return None

# GraphQL context provider
async def get_context(
    request: Request,
    current_user = Depends(get_current_user_optional)
):
    """Provide context for GraphQL resolvers"""
    
    return {
        "request": request,
        "current_user": current_user,
        "user_service": user_service,
        "post_service": post_service,
        "comment_service": comment_service,
        
        # DataLoaders for performance
        "user_loader": UserDataLoader(user_service),
        "post_loader": PostDataLoader(post_service),
        "comments_by_post_loader": CommentsByPostDataLoader(comment_service),
    }

# Create GraphQL router
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    debug=True  # Disable in production
)

# FastAPI app
app = FastAPI(title="Blog API with GraphQL")

# Mount GraphQL
app.include_router(graphql_app, prefix="/graphql")

# GraphQL Playground (development only)
@app.get("/graphql-playground")
async def graphql_playground():
    """GraphQL Playground for development"""
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset=utf-8/>
        <meta name="viewport" content="user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, minimal-ui">
        <title>GraphQL Playground</title>
        <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
        <link rel="shortcut icon" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png" />
        <script src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
    </head>
    <body>
        <div id="root">
            <style>
                body { background-color: rgb(23, 42, 58); font-family: Open Sans, sans-serif; height: 90vh; }
                #root { height: 100%; width: 100%; display: flex; align-items: center; justify-content: center; }
                .loading { font-size: 32px; font-weight: 200; color: rgba(255, 255, 255, .6); margin-left: 20px; }
                img { width: 78px; height: 78px; }
                .title { font-weight: 400; }
            </style>
            <img src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/logo.png" alt="">
            <div class="loading"> Loading
                <span class="title">GraphQL Playground</span>
            </div>
        </div>
        <script>window.addEventListener('load', function (event) {
            GraphQLPlayground.init(document.getElementById('root'), {
                endpoint: '/graphql'
            })
        })</script>
    </body>
    </html>
    """

# Example REST to GraphQL migration endpoint
@app.get("/api/v1/posts/{post_id}")
async def get_post_rest(post_id: int):
    """REST endpoint - compare with GraphQL"""
    
    # Fixed response structure - can't customize fields
    post = await post_service.get_post_by_id(post_id)
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Always returns all fields
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "excerpt": post.excerpt,
        "author_id": post.author_id,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
        "published": post.published,
        "tags": post.tags
    }

# GraphQL comparison
"""
GraphQL Query (flexible):

query GetPost($id: Int!) {
  post(id: $id) {
    title
    content
    author {
      name
      avatar_url
    }
    comments {
      content
      author {
        name
      }
    }
  }
}

Benefits:
- Single request for post + author + comments
- Only fetch needed fields
- Type safety
- Self-documenting
"""

# Error handling for GraphQL
from strawberry.types import ExecutionResult

@app.middleware("http")
async def graphql_error_handler(request: Request, call_next):
    """Handle GraphQL errors and logging"""
    
    response = await call_next(request)
    
    # Log GraphQL errors for monitoring
    if hasattr(response, 'body') and b'"errors"' in response.body:
        logger.warning(f"GraphQL errors in request to {request.url}")
    
    return response
```

**GraphQL Client Usage Examples:**

```javascript
// Frontend GraphQL usage examples
const QUERIES = {
  // Simple query
  GET_POSTS: `
    query GetPosts($first: Int, $search: String) {
      posts(first: $first, search: $search) {
        edges {
          node {
            id
            title
            excerpt
            author {
              displayName
              avatarUrl
            }
            createdAt
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  `,
  
  // Complex nested query
  GET_POST_DETAIL: `
    query GetPostDetail($id: Int!) {
      post(id: $id) {
        id
        title
        content
        tags
        wordCount
        author {
          displayName
          bio
          avatarUrl
        }
        comments {
          id
          content
          createdAt
          author {
            displayName
          }
          replies {
            id
            content
            author {
              displayName
            }
          }
        }
      }
    }
  `,
  
  // Mutation
  CREATE_POST: `
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        post {
          id
          title
          published
        }
        errors {
          field
          message
        }
      }
    }
  `,
  
  // Subscription
  SUBSCRIBE_COMMENTS: `
    subscription SubscribeToComments($postId: Int!) {
      postComments(postId: $postId) {
        id
        content
        author {
          displayName
        }
      }
    }
  `
};

// Using with fetch
async function fetchPosts() {
  const response = await fetch('/graphql', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + localStorage.getItem('token')
    },
    body: JSON.stringify({
      query: QUERIES.GET_POSTS,
      variables: { first: 10 }
    })
  });
  
  const result = await response.json();
  
  if (result.errors) {
    console.error('GraphQL errors:', result.errors);
  } else {
    console.log('Posts:', result.data.posts);
  }
}

// Using with Apollo Client or urql would be even simpler
```

---

### 🏠 Homework: Build GraphQL API

**Task:** Convert your REST blog API to GraphQL

```python
# Create a complete GraphQL API with:
# 1. Schema with Users, Posts, Comments, and Tags
# 2. Queries with filtering, pagination, and search
# 3. Mutations for CRUD operations
# 4. Subscriptions for real-time updates
# 5. DataLoaders for N+1 query prevention
# 6. Authentication and authorization
# 7. Query complexity analysis and rate limiting
# 8. Error handling and validation

# Schema Requirements:
# - User management (register, login, profile)
# - Post management (create, edit, publish, delete)
# - Comment system (nested comments, replies)
# - Tag system (popular tags, filtering)
# - Real-time notifications

# Performance Requirements:
# - Efficient data fetching (no N+1 queries)
# - Query complexity limits
# - Rate limiting
# - Caching strategies

# Bonus Features:
# - File upload mutations
# - Advanced search with filters
# - Analytics queries (post views, user activity)
# - Admin queries for moderation
```

---

### 📝 Key Takeaways

✅ GraphQL = Query language for flexible data fetching
✅ Schema & Resolvers = Define API structure and data sources
✅ DataLoaders = Solve N+1 query performance problems
✅ Security = Query limits, authentication, and validation
✅ Real-time = Subscriptions for live updates

---

<a name="hour-38"></a>
## 📅 Hour 38: Microservices & API Gateway Concepts

### 🎯 Learning Objectives
- Understand microservices architecture patterns
- Implement service-to-service communication
- Build API Gateway with routing and middleware
- Handle service discovery and load balancing
- Implement distributed system patterns (Circuit Breaker, Retry, etc.)

### 📖 What to Teach

**"Today we break our monolith into microservices and learn to orchestrate distributed systems!"**

---

### 1️⃣ Microservices Architecture Overview (10 minutes)

**Monolith vs Microservices:**

```python
# MONOLITH ARCHITECTURE
"""
┌─────────────────────────────────────────┐
│           Blog Application              │
│  ┌─────────┐ ┌─────────┐ ┌───────────┐ │
│  │  Users  │ │  Posts  │ │ Comments  │ │
│  │ Service │ │ Service │ │  Service  │ │
│  └─────────┘ └─────────┘ └───────────┘ │
│              │                          │
│      ┌───────────────────┐             │
│      │    Database       │             │
│      │   (PostgreSQL)    │             │
│      └───────────────────┘             │
└─────────────────────────────────────────┘

Monolith Challenges:
❌ Single point of failure
❌ Difficult to scale individual components
❌ Technology lock-in
❌ Large team coordination issues
❌ Deployment of entire application required
❌ Database bottlenecks
"""

# MICROSERVICES ARCHITECTURE
"""
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ User Service │    │ Post Service │    │Comment Service│
│              │    │              │    │              │
│ ┌──────────┐ │    │ ┌──────────┐ │    │ ┌──────────┐ │
│ │Users DB  │ │    │ │Posts DB  │ │    │ │Comments DB│ │
│ └──────────┘ │    │ └──────────┘ │    │ └──────────┘ │
└──────────────┘    └──────────────┘    └──────────────┘
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             │
              ┌─────────────────────────────┐
              │       API Gateway           │
              │   (Routing, Auth, etc.)     │
              └─────────────────────────────┘
                             │
              ┌─────────────────────────────┐
              │      Load Balancer          │
              └─────────────────────────────┘

Microservices Benefits:
✅ Independent deployment and scaling
✅ Technology diversity
✅ Team autonomy
✅ Fault isolation
✅ Better resource utilization

Microservices Challenges:
⚠️ Network complexity
⚠️ Data consistency issues
⚠️ Service discovery
⚠️ Monitoring and debugging
⚠️ Increased operational overhead
"""

# When to use Microservices
microservices_decision_matrix = {
    "Team Size": "Multiple teams (3+ teams)",
    "Application Complexity": "High complexity with distinct domains",
    "Scalability Needs": "Different scaling requirements per component",
    "Technology Diversity": "Need different tech stacks",
    "Deployment Frequency": "Frequent, independent deployments",
    "Fault Tolerance": "Need service isolation",
    
    "Stay with Monolith if": {
        "Small team": "< 10 developers",
        "Simple application": "CRUD with minimal business logic",
        "Uniform scaling": "All components scale together",
        "Rapid prototyping": "MVP or early-stage product",
        "Limited ops experience": "No DevOps/infrastructure expertise"
    }
}
```

**Service Decomposition Strategies:**

```python
# Domain-Driven Design (DDD) approach to service boundaries
class BlogDomainAnalysis:
    """Analyze blog domain to identify service boundaries"""
    
    def __init__(self):
        self.bounded_contexts = {
            "User Management": {
                "entities": ["User", "Profile", "Preferences"],
                "operations": ["register", "login", "update_profile"],
                "data": "user_database",
                "team": "auth_team"
            },
            
            "Content Management": {
                "entities": ["Post", "Draft", "Category", "Tag"],
                "operations": ["create_post", "publish", "edit", "search"],
                "data": "content_database", 
                "team": "content_team"
            },
            
            "Engagement": {
                "entities": ["Comment", "Like", "Share", "View"],
                "operations": ["comment", "like", "track_view"],
                "data": "engagement_database",
                "team": "engagement_team"
            },
            
            "Notification": {
                "entities": ["Notification", "EmailTemplate", "Preference"],
                "operations": ["send_notification", "email", "push"],
                "data": "notification_database",
                "team": "notification_team"
            },
            
            "Analytics": {
                "entities": ["Event", "Metric", "Report"],
                "operations": ["track_event", "generate_report"],
                "data": "analytics_database",
                "team": "analytics_team"
            }
        }
    
    def get_service_dependencies(self) -> dict:
        """Map service dependencies"""
        
        return {
            "content_service": {
                "depends_on": ["user_service"],  # Need author info
                "consumed_by": ["engagement_service", "notification_service"]
            },
            
            "engagement_service": {
                "depends_on": ["user_service", "content_service"],
                "consumed_by": ["notification_service", "analytics_service"]
            },
            
            "notification_service": {
                "depends_on": ["user_service", "content_service", "engagement_service"],
                "consumed_by": []  # Leaf service
            },
            
            "user_service": {
                "depends_on": [],  # Core service
                "consumed_by": ["content_service", "engagement_service", "notification_service"]
            },
            
            "analytics_service": {
                "depends_on": ["user_service", "content_service", "engagement_service"],
                "consumed_by": []  # Leaf service
            }
        }

# Service sizing guidelines
service_sizing_guide = {
    "team_size": "6-8 developers max per service",
    "codebase": "Can be rewritten in 2-4 weeks",
    "database": "Single service owns its data",
    "deployment": "Independent deployment pipeline",
    "monitoring": "Separate metrics and logging",
    "api_surface": "Well-defined, stable interface"
}
```

---

### 2️⃣ Service-to-Service Communication (15 minutes)

**HTTP API Communication:**

```python
# service_client.py
import httpx
import asyncio
from typing import Dict, Any, Optional, List
import logging
from datetime import datetime, timedelta
import json
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class ServiceClient:
    """Base class for service-to-service HTTP communication"""
    
    def __init__(
        self, 
        base_url: str, 
        service_name: str,
        timeout: int = 30,
        retries: int = 3
    ):
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.timeout = timeout
        self.retries = retries
        
        # Create HTTP client with connection pooling
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(timeout),
            limits=httpx.Limits(max_keepalive_connections=20, max_connections=100)
        )
        
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Dict[Any, Any]:
        """Make HTTP request with retry logic"""
        
        url = f"{self.base_url}{endpoint}"
        
        # Add service identification headers
        request_headers = {
            "User-Agent": f"ServiceClient/{self.service_name}",
            "X-Service-Name": self.service_name,
            "Content-Type": "application/json"
        }
        
        if headers:
            request_headers.update(headers)
        
        try:
            logger.info(f"🔄 {method} {url} - Service: {self.service_name}")
            
            response = await self.client.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=request_headers
            )
            
            # Log response time for monitoring
            response_time = response.elapsed.total_seconds()
            logger.info(f"✅ {method} {url} - {response.status_code} - {response_time:.3f}s")
            
            # Handle different response codes
            if response.status_code == 404:
                return None
            
            elif response.status_code >= 500:
                # Server error - should retry
                response.raise_for_status()
            
            elif response.status_code >= 400:
                # Client error - don't retry
                error_msg = f"Client error: {response.status_code}"
                try:
                    error_detail = response.json()
                    error_msg += f" - {error_detail}"
                except:
                    error_msg += f" - {response.text}"
                
                raise ValueError(error_msg)
            
            return response.json()
            
        except httpx.TimeoutException:
            logger.error(f"⏱️ Timeout calling {self.service_name} - {url}")
            raise
        
        except httpx.ConnectError:
            logger.error(f"🔌 Connection error to {self.service_name} - {url}")
            raise
        
        except Exception as e:
            logger.error(f"❌ Error calling {self.service_name} - {url}: {str(e)}")
            raise
    
    async def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """GET request"""
        return await self._make_request("GET", endpoint, params=params)
    
    async def post(self, endpoint: str, data: Dict) -> Dict:
        """POST request"""
        return await self._make_request("POST", endpoint, data=data)
    
    async def put(self, endpoint: str, data: Dict) -> Dict:
        """PUT request"""
        return await self._make_request("PUT", endpoint, data=data)
    
    async def delete(self, endpoint: str) -> bool:
        """DELETE request"""
        result = await self._make_request("DELETE", endpoint)
        return result is not None

class UserServiceClient(ServiceClient):
    """Client for User Service API"""
    
    def __init__(self, base_url: str = "http://user-service:8000"):
        super().__init__(base_url, "user-service")
    
    async def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user by ID"""
        return await self.get(f"/api/v1/users/{user_id}")
    
    async def get_users_by_ids(self, user_ids: List[int]) -> List[Dict]:
        """Batch get users by IDs"""
        response = await self.post("/api/v1/users/batch", {"user_ids": user_ids})
        return response.get("users", [])
    
    async def validate_user_token(self, token: str) -> Optional[Dict]:
        """Validate user authentication token"""
        return await self.post("/api/v1/auth/validate", {"token": token})

class ContentServiceClient(ServiceClient):
    """Client for Content Service API"""
    
    def __init__(self, base_url: str = "http://content-service:8000"):
        super().__init__(base_url, "content-service")
    
    async def get_post(self, post_id: int) -> Optional[Dict]:
        """Get post by ID"""
        return await self.get(f"/api/v1/posts/{post_id}")
    
    async def create_post(self, post_data: Dict, author_id: int) -> Dict:
        """Create new post"""
        return await self.post("/api/v1/posts", {
            **post_data,
            "author_id": author_id
        })
    
    async def get_posts_by_author(self, author_id: int, limit: int = 10) -> List[Dict]:
        """Get posts by author"""
        response = await self.get(f"/api/v1/posts", params={
            "author_id": author_id,
            "limit": limit
        })
        return response.get("posts", [])

class NotificationServiceClient(ServiceClient):
    """Client for Notification Service API"""
    
    def __init__(self, base_url: str = "http://notification-service:8000"):
        super().__init__(base_url, "notification-service")
    
    async def send_notification(
        self, 
        user_id: int, 
        notification_type: str, 
        data: Dict
    ) -> Dict:
        """Send notification to user"""
        return await self.post("/api/v1/notifications", {
            "user_id": user_id,
            "type": notification_type,
            "data": data
        })
    
    async def send_email(
        self, 
        to_email: str, 
        subject: str, 
        template: str, 
        variables: Dict
    ) -> Dict:
        """Send email notification"""
        return await self.post("/api/v1/notifications/email", {
            "to_email": to_email,
            "subject": subject,
            "template": template,
            "variables": variables
        })

# Service registry for dependency injection
class ServiceRegistry:
    """Registry for service clients"""
    
    def __init__(self):
        self._clients = {}
    
    def register_service(self, name: str, client: ServiceClient):
        """Register a service client"""
        self._clients[name] = client
    
    def get_service(self, name: str) -> ServiceClient:
        """Get service client by name"""
        if name not in self._clients:
            raise ValueError(f"Service '{name}' not registered")
        return self._clients[name]
    
    async def health_check_all(self) -> Dict[str, Any]:
        """Check health of all registered services"""
        
        health_results = {}
        
        for service_name, client in self._clients.items():
            try:
                # Try to call health endpoint
                start_time = datetime.now()
                health_data = await client.get("/health")
                response_time = (datetime.now() - start_time).total_seconds()
                
                health_results[service_name] = {
                    "status": "healthy",
                    "response_time": response_time,
                    "details": health_data
                }
                
            except Exception as e:
                health_results[service_name] = {
                    "status": "unhealthy", 
                    "error": str(e),
                    "response_time": None
                }
        
        return health_results

# Initialize service registry
service_registry = ServiceRegistry()

# Register services
async def setup_service_clients():
    """Setup service clients"""
    
    service_registry.register_service("users", UserServiceClient())
    service_registry.register_service("content", ContentServiceClient()) 
    service_registry.register_service("notifications", NotificationServiceClient())
```

**Event-Driven Communication:**

```python
# event_system.py
import json
import asyncio
from typing import Dict, Any, Callable, List
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid
import aioredis
from enum import Enum

class EventType(Enum):
    """Domain events for microservices communication"""
    
    USER_REGISTERED = "user.registered"
    USER_UPDATED = "user.updated"
    POST_CREATED = "post.created"
    POST_PUBLISHED = "post.published"
    COMMENT_CREATED = "comment.created"
    NOTIFICATION_SENT = "notification.sent"

@dataclass
class DomainEvent:
    """Base domain event"""
    
    event_id: str
    event_type: EventType
    aggregate_id: str
    data: Dict[str, Any]
    timestamp: datetime
    version: int = 1
    
    @classmethod
    def create(cls, event_type: EventType, aggregate_id: str, data: Dict[str, Any]):
        """Create new domain event"""
        return cls(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            aggregate_id=aggregate_id,
            data=data,
            timestamp=datetime.utcnow()
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            **asdict(self),
            "event_type": self.event_type.value,
            "timestamp": self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DomainEvent":
        """Create from dictionary"""
        return cls(
            event_id=data["event_id"],
            event_type=EventType(data["event_type"]),
            aggregate_id=data["aggregate_id"],
            data=data["data"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            version=data.get("version", 1)
        )

class EventBus:
    """Event bus for microservices communication using Redis"""
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_url = redis_url
        self.redis = None
        self.subscribers = {}
        self.running = False
    
    async def connect(self):
        """Connect to Redis"""
        self.redis = await aioredis.from_url(self.redis_url)
    
    async def disconnect(self):
        """Disconnect from Redis"""
        if self.redis:
            await self.redis.close()
    
    async def publish_event(self, event: DomainEvent):
        """Publish domain event"""
        
        if not self.redis:
            await self.connect()
        
        # Serialize event
        event_data = json.dumps(event.to_dict())
        
        # Publish to Redis streams
        stream_name = f"events:{event.event_type.value}"
        
        await self.redis.xadd(stream_name, event_data)
        
        logger.info(f"📤 Published event: {event.event_type.value} - {event.event_id}")
    
    async def subscribe_to_events(
        self, 
        event_types: List[EventType], 
        handler: Callable[[DomainEvent], None],
        consumer_group: str = "default"
    ):
        """Subscribe to domain events"""
        
        if not self.redis:
            await self.connect()
        
        # Create consumer group for each event type
        for event_type in event_types:
            stream_name = f"events:{event_type.value}"
            
            try:
                await self.redis.xgroup_create(stream_name, consumer_group, id="0", mkstream=True)
            except Exception:
                # Group already exists
                pass
        
        # Store handler
        for event_type in event_types:
            if event_type not in self.subscribers:
                self.subscribers[event_type] = []
            self.subscribers[event_type].append(handler)
        
        logger.info(f"📥 Subscribed to events: {[et.value for et in event_types]}")
    
    async def start_consuming(self, consumer_name: str = None):
        """Start consuming events"""
        
        if not consumer_name:
            consumer_name = f"consumer-{uuid.uuid4().hex[:8]}"
        
        self.running = True
        
        while self.running:
            try:
                # Check each subscribed event type
                for event_type in self.subscribers.keys():
                    stream_name = f"events:{event_type.value}"
                    
                    # Read from stream
                    messages = await self.redis.xreadgroup(
                        "default",
                        consumer_name,
                        {stream_name: ">"},
                        count=10,
                        block=1000  # 1 second timeout
                    )
                    
                    # Process messages
                    for stream, msgs in messages:
                        for msg_id, fields in msgs:
                            try:
                                # Parse event
                                event_data = json.loads(fields[b'data'].decode())
                                event = DomainEvent.from_dict(event_data)
                                
                                # Call handlers
                                handlers = self.subscribers.get(event.event_type, [])
                                for handler in handlers:
                                    try:
                                        await handler(event)
                                    except Exception as e:
                                        logger.error(f"❌ Event handler error: {str(e)}")
                                
                                # Acknowledge message
                                await self.redis.xack(stream_name, "default", msg_id)
                                
                            except Exception as e:
                                logger.error(f"❌ Error processing event: {str(e)}")
                
            except Exception as e:
                logger.error(f"❌ Event consumption error: {str(e)}")
                await asyncio.sleep(5)  # Wait before retry
    
    def stop_consuming(self):
        """Stop consuming events"""
        self.running = False

# Event handlers for different services
class ContentServiceEventHandler:
    """Handle events in content service"""
    
    def __init__(self, content_service, notification_client):
        self.content_service = content_service
        self.notification_client = notification_client
    
    async def handle_user_registered(self, event: DomainEvent):
        """Handle user registration event"""
        
        user_id = event.data["user_id"]
        username = event.data["username"]
        
        logger.info(f"👤 New user registered: {username} (ID: {user_id})")
        
        # Send welcome notification
        await self.notification_client.send_notification(
            user_id=user_id,
            notification_type="welcome",
            data={
                "username": username,
                "message": "Welcome to our blog platform!"
            }
        )
    
    async def handle_post_published(self, event: DomainEvent):
        """Handle post publication event"""
        
        post_id = event.data["post_id"]
        author_id = event.data["author_id"]
        title = event.data["title"]
        
        logger.info(f"📝 Post published: {title} (ID: {post_id})")
        
        # Notify followers (simplified)
        followers = await self.content_service.get_author_followers(author_id)
        
        for follower_id in followers:
            await self.notification_client.send_notification(
                user_id=follower_id,
                notification_type="new_post",
                data={
                    "post_id": post_id,
                    "title": title,
                    "author_id": author_id
                }
            )

# Event publishing examples
class PostService:
    """Content service that publishes domain events"""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
    
    async def create_post(self, title: str, content: str, author_id: int) -> Dict:
        """Create post and publish event"""
        
        # Create post in database
        post_data = {
            "id": 123,  # From database
            "title": title,
            "content": content,
            "author_id": author_id,
            "created_at": datetime.utcnow().isoformat()
        }
        
        # Publish domain event
        event = DomainEvent.create(
            event_type=EventType.POST_CREATED,
            aggregate_id=str(post_data["id"]),
            data=post_data
        )
        
        await self.event_bus.publish_event(event)
        
        return post_data
    
    async def publish_post(self, post_id: int) -> bool:
        """Publish post and emit event"""
        
        # Update post status in database
        # post = update_post_status(post_id, "published")
        
        # Publish domain event
        event = DomainEvent.create(
            event_type=EventType.POST_PUBLISHED,
            aggregate_id=str(post_id),
            data={
                "post_id": post_id,
                "author_id": 1,  # From database
                "title": "Sample Post",  # From database
                "published_at": datetime.utcnow().isoformat()
            }
        )
        
        await self.event_bus.publish_event(event)
        
        return True
```

---

### 3️⃣ API Gateway Implementation (15 minutes)

**API Gateway with FastAPI:**

```python
# api_gateway.py
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import httpx
import asyncio
from typing import Dict, Any, Optional
import time
import logging
from urllib.parse import urljoin
import json

logger = logging.getLogger(__name__)

class APIGateway:
    """API Gateway for microservices routing"""
    
    def __init__(self):
        self.app = FastAPI(title="API Gateway", version="1.0.0")
        self.service_registry = {}
        self.load_balancers = {}
        self.circuit_breakers = {}
        
        # HTTP client for service communication
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0),
            limits=httpx.Limits(max_keepalive_connections=100, max_connections=200)
        )
        
        self._setup_middleware()
        self._setup_routes()
    
    def _setup_middleware(self):
        """Setup gateway middleware"""
        
        # CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Configure for production
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Request/Response logging
        @self.app.middleware("http")
        async def log_requests(request: Request, call_next):
            start_time = time.time()
            
            response = await call_next(request)
            
            process_time = time.time() - start_time
            logger.info(
                f"🚪 Gateway: {request.method} {request.url.path} - "
                f"{response.status_code} - {process_time:.3f}s"
            )
            
            return response
    
    def register_service(
        self, 
        name: str, 
        instances: list, 
        health_endpoint: str = "/health"
    ):
        """Register a microservice with multiple instances"""
        
        self.service_registry[name] = {
            "instances": instances,
            "health_endpoint": health_endpoint,
            "healthy_instances": instances.copy()
        }
        
        # Initialize load balancer
        self.load_balancers[name] = RoundRobinLoadBalancer(instances)
        
        # Initialize circuit breaker
        self.circuit_breakers[name] = CircuitBreaker(
            failure_threshold=5,
            timeout=60,
            expected_exception=httpx.RequestError
        )
        
        logger.info(f"📝 Registered service: {name} with {len(instances)} instances")
    
    def _setup_routes(self):
        """Setup gateway routes"""
        
        # Health check endpoint
        @self.app.get("/health")
        async def gateway_health():
            """Gateway health check"""
            
            service_health = {}
            
            for service_name in self.service_registry.keys():
                try:
                    healthy_count = len(self.service_registry[service_name]["healthy_instances"])
                    total_count = len(self.service_registry[service_name]["instances"])
                    
                    service_health[service_name] = {
                        "healthy": healthy_count,
                        "total": total_count,
                        "status": "healthy" if healthy_count > 0 else "unhealthy"
                    }
                except Exception as e:
                    service_health[service_name] = {
                        "status": "error",
                        "error": str(e)
                    }
            
            return {
                "gateway": "healthy",
                "services": service_health,
                "timestamp": time.time()
            }
        
        # Route all API requests
        @self.app.api_route(
            "/api/{service_name}/{path:path}",
            methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
        )
        async def route_to_service(
            service_name: str,
            path: str,
            request: Request
        ):
            """Route requests to appropriate microservice"""
            
            if service_name not in self.service_registry:
                raise HTTPException(
                    status_code=404,
                    detail=f"Service '{service_name}' not found"
                )
            
            # Get healthy service instance
            try:
                service_url = self.load_balancers[service_name].get_instance()
                if not service_url:
                    raise HTTPException(
                        status_code=503,
                        detail=f"No healthy instances available for service '{service_name}'"
                    )
                
                # Use circuit breaker
                circuit_breaker = self.circuit_breakers[service_name]
                
                return await circuit_breaker.call(
                    self._forward_request,
                    service_url,
                    path,
                    request
                )
                
            except Exception as e:
                logger.error(f"❌ Error routing to {service_name}: {str(e)}")
                raise HTTPException(status_code=502, detail=str(e))
    
    async def _forward_request(
        self,
        service_url: str,
        path: str,
        request: Request
    ) -> Response:
        """Forward request to microservice"""
        
        # Build target URL
        target_url = urljoin(service_url, f"/api/{path}")
        
        # Get request data
        body = await request.body()
        
        # Forward headers (filter out hop-by-hop headers)
        forward_headers = {}
        for name, value in request.headers.items():
            if name.lower() not in ['host', 'content-length', 'connection']:
                forward_headers[name] = value
        
        # Add gateway headers
        forward_headers['X-Gateway'] = 'APIGateway/1.0'
        forward_headers['X-Forwarded-For'] = request.client.host
        
        try:
            # Make request to microservice
            response = await self.client.request(
                method=request.method,
                url=target_url,
                content=body,
                headers=forward_headers,
                params=dict(request.query_params)
            )
            
            # Return response
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
            
        except httpx.TimeoutException:
            logger.error(f"⏱️ Timeout calling service: {target_url}")
            raise HTTPException(status_code=504, detail="Gateway timeout")
        
        except httpx.RequestError as e:
            logger.error(f"🔌 Request error: {target_url} - {str(e)}")
            raise HTTPException(status_code=502, detail="Bad Gateway")
    
    async def start_health_checks(self):
        """Start background health checking"""
        
        asyncio.create_task(self._health_check_loop())
    
    async def _health_check_loop(self):
        """Continuously check service health"""
        
        while True:
            try:
                for service_name, config in self.service_registry.items():
                    healthy_instances = []
                    
                    for instance_url in config["instances"]:
                        if await self._check_instance_health(
                            instance_url, 
                            config["health_endpoint"]
                        ):
                            healthy_instances.append(instance_url)
                    
                    # Update healthy instances
                    self.service_registry[service_name]["healthy_instances"] = healthy_instances
                    self.load_balancers[service_name].update_instances(healthy_instances)
                    
                    logger.debug(f"🏥 {service_name}: {len(healthy_instances)}/{len(config['instances'])} healthy")
                
            except Exception as e:
                logger.error(f"❌ Health check error: {str(e)}")
            
            # Check every 30 seconds
            await asyncio.sleep(30)
    
    async def _check_instance_health(self, instance_url: str, health_endpoint: str) -> bool:
        """Check if service instance is healthy"""
        
        try:
            health_url = urljoin(instance_url, health_endpoint)
            response = await self.client.get(health_url, timeout=5.0)
            return response.status_code == 200
            
        except Exception:
            return False

class RoundRobinLoadBalancer:
    """Simple round-robin load balancer"""
    
    def __init__(self, instances: list):
        self.instances = instances.copy()
        self.current_index = 0
    
    def get_instance(self) -> Optional[str]:
        """Get next instance using round-robin"""
        
        if not self.instances:
            return None
        
        instance = self.instances[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.instances)
        
        return instance
    
    def update_instances(self, instances: list):
        """Update available instances"""
        self.instances = instances.copy()
        if self.instances:
            self.current_index = self.current_index % len(self.instances)
        else:
            self.current_index = 0

class CircuitBreaker:
    """Circuit breaker pattern implementation"""
    
    def __init__(
        self, 
        failure_threshold: int = 5,
        timeout: int = 60,
        expected_exception: type = Exception
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open
    
    async def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        
        if self.state == "open":
            if self._should_attempt_reset():
                self.state = "half-open"
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
            
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if circuit breaker should attempt to reset"""
        
        if self.last_failure_time is None:
            return False
        
        return time.time() - self.last_failure_time >= self.timeout
    
    def _on_success(self):
        """Handle successful call"""
        self.failure_count = 0
        self.state = "closed"
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "open"

# Gateway setup
gateway = APIGateway()

# Register services
gateway.register_service("users", [
    "http://user-service-1:8000",
    "http://user-service-2:8000"
])

gateway.register_service("posts", [
    "http://content-service-1:8000",
    "http://content-service-2:8000"
])

gateway.register_service("notifications", [
    "http://notification-service:8000"
])

# Start the gateway
if __name__ == "__main__":
    import uvicorn
    
    # Start health checks
    asyncio.create_task(gateway.start_health_checks())
    
    # Run gateway
    uvicorn.run(gateway.app, host="0.0.0.0", port=8080)
```

**Service Discovery with Consul:**

```python
# service_discovery.py
import consul
import asyncio
import json
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class ConsulServiceDiscovery:
    """Service discovery using HashiCorp Consul"""
    
    def __init__(self, consul_host: str = "localhost", consul_port: int = 8500):
        self.consul = consul.Consul(host=consul_host, port=consul_port)
    
    async def register_service(
        self,
        service_name: str,
        service_id: str,
        address: str,
        port: int,
        health_check_url: str = None,
        tags: List[str] = None
    ):
        """Register service with Consul"""
        
        check = None
        if health_check_url:
            check = consul.Check.http(health_check_url, interval="10s", timeout="3s")
        
        try:
            self.consul.agent.service.register(
                name=service_name,
                service_id=service_id,
                address=address,
                port=port,
                tags=tags or [],
                check=check
            )
            
            logger.info(f"📝 Registered service: {service_name} ({service_id}) at {address}:{port}")
            
        except Exception as e:
            logger.error(f"❌ Failed to register service {service_name}: {str(e)}")
            raise
    
    async def deregister_service(self, service_id: str):
        """Deregister service from Consul"""
        
        try:
            self.consul.agent.service.deregister(service_id)
            logger.info(f"🗑️ Deregistered service: {service_id}")
            
        except Exception as e:
            logger.error(f"❌ Failed to deregister service {service_id}: {str(e)}")
    
    async def discover_services(self, service_name: str) -> List[Dict[str, Any]]:
        """Discover healthy service instances"""
        
        try:
            _, services = self.consul.health.service(service_name, passing=True)
            
            instances = []
            for service in services:
                service_info = service['Service']
                instances.append({
                    'id': service_info['ID'],
                    'address': service_info['Address'],
                    'port': service_info['Port'],
                    'tags': service_info['Tags'],
                    'url': f"http://{service_info['Address']}:{service_info['Port']}"
                })
            
            logger.debug(f"🔍 Found {len(instances)} instances of {service_name}")
            return instances
            
        except Exception as e:
            logger.error(f"❌ Failed to discover service {service_name}: {str(e)}")
            return []
    
    async def watch_service(
        self, 
        service_name: str, 
        callback: callable
    ):
        """Watch for service changes"""
        
        index = None
        
        while True:
            try:
                index, services = self.consul.health.service(
                    service_name, 
                    index=index, 
                    wait="30s"
                )
                
                # Process service changes
                healthy_instances = []
                for service in services:
                    if service['Checks'][0]['Status'] == 'passing':
                        service_info = service['Service']
                        healthy_instances.append({
                            'id': service_info['ID'],
                            'url': f"http://{service_info['Address']}:{service_info['Port']}"
                        })
                
                # Call callback with updated instances
                await callback(service_name, healthy_instances)
                
            except Exception as e:
                logger.error(f"❌ Error watching service {service_name}: {str(e)}")
                await asyncio.sleep(10)

# Enhanced API Gateway with service discovery
class DiscoveryAPIGateway(APIGateway):
    """API Gateway with dynamic service discovery"""
    
    def __init__(self, consul_host: str = "localhost"):
        super().__init__()
        self.service_discovery = ConsulServiceDiscovery(consul_host)
        self.watched_services = set()
    
    async def register_and_watch_service(self, service_name: str):
        """Register service for discovery and start watching"""
        
        if service_name in self.watched_services:
            return
        
        self.watched_services.add(service_name)
        
        # Start watching service
        asyncio.create_task(
            self.service_discovery.watch_service(
                service_name,
                self._on_service_change
            )
        )
        
        logger.info(f"👁️ Started watching service: {service_name}")
    
    async def _on_service_change(self, service_name: str, instances: List[Dict]):
        """Handle service instance changes"""
        
        urls = [instance['url'] for instance in instances]
        
        # Update service registry
        if service_name not in self.service_registry:
            self.service_registry[service_name] = {
                "instances": urls,
                "health_endpoint": "/health",
                "healthy_instances": urls
            }
            self.load_balancers[service_name] = RoundRobinLoadBalancer(urls)
        else:
            self.service_registry[service_name]["instances"] = urls
            self.service_registry[service_name]["healthy_instances"] = urls
            self.load_balancers[service_name].update_instances(urls)
        
        logger.info(f"🔄 Updated {service_name} instances: {len(urls)} available")
```

---

### 4️⃣ Distributed System Patterns (10 minutes)

**Resilience Patterns:**

```python
# distributed_patterns.py
import asyncio
import time
from typing import Any, Callable, Optional
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class RetryStrategy(Enum):
    FIXED_DELAY = "fixed"
    EXPONENTIAL_BACKOFF = "exponential"
    LINEAR_BACKOFF = "linear"

@dataclass
class RetryConfig:
    max_attempts: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    strategy: RetryStrategy = RetryStrategy.EXPONENTIAL_BACKOFF
    backoff_multiplier: float = 2.0

class RetryHandler:
    """Configurable retry handler with different strategies"""
    
    def __init__(self, config: RetryConfig):
        self.config = config
    
    async def execute_with_retry(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Any:
        """Execute function with retry logic"""
        
        last_exception = None
        
        for attempt in range(self.config.max_attempts):
            try:
                return await func(*args, **kwargs)
                
            except Exception as e:
                last_exception = e
                
                if attempt < self.config.max_attempts - 1:
                    delay = self._calculate_delay(attempt)
                    
                    logger.warning(
                        f"⚠️ Attempt {attempt + 1} failed: {str(e)}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    
                    await asyncio.sleep(delay)
                else:
                    logger.error(f"❌ All {self.config.max_attempts} attempts failed")
        
        raise last_exception
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate delay based on retry strategy"""
        
        if self.config.strategy == RetryStrategy.FIXED_DELAY:
            return self.config.base_delay
        
        elif self.config.strategy == RetryStrategy.LINEAR_BACKOFF:
            delay = self.config.base_delay * (attempt + 1)
        
        elif self.config.strategy == RetryStrategy.EXPONENTIAL_BACKOFF:
            delay = self.config.base_delay * (self.config.backoff_multiplier ** attempt)
        
        else:
            delay = self.config.base_delay
        
        return min(delay, self.config.max_delay)

class BulkheadPattern:
    """Bulkhead pattern for resource isolation"""
    
    def __init__(self, name: str, max_concurrent: int = 10):
        self.name = name
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.active_requests = 0
        self.total_requests = 0
        self.failed_requests = 0
    
    async def execute(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with bulkhead protection"""
        
        async with self.semaphore:
            self.active_requests += 1
            self.total_requests += 1
            
            try:
                result = await func(*args, **kwargs)
                return result
                
            except Exception as e:
                self.failed_requests += 1
                raise e
            
            finally:
                self.active_requests -= 1
    
    def get_stats(self) -> dict:
        """Get bulkhead statistics"""
        
        return {
            "name": self.name,
            "active_requests": self.active_requests,
            "total_requests": self.total_requests,
            "failed_requests": self.failed_requests,
            "success_rate": (
                (self.total_requests - self.failed_requests) / self.total_requests
                if self.total_requests > 0 else 0
            )
        }

class TimeoutHandler:
    """Timeout handling for distributed calls"""
    
    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout
    
    async def execute_with_timeout(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Any:
        """Execute function with timeout"""
        
        try:
            return await asyncio.wait_for(func(*args, **kwargs), timeout=self.timeout)
            
        except asyncio.TimeoutError:
            logger.error(f"⏱️ Operation timed out after {self.timeout}s")
            raise TimeoutError(f"Operation timed out after {self.timeout}s")

class DistributedServiceCall:
    """Combined service call with all resilience patterns"""
    
    def __init__(
        self,
        service_name: str,
        retry_config: Optional[RetryConfig] = None,
        timeout: float = 30.0,
        bulkhead_limit: int = 10
    ):
        self.service_name = service_name
        self.retry_handler = RetryHandler(retry_config or RetryConfig())
        self.timeout_handler = TimeoutHandler(timeout)
        self.bulkhead = BulkheadPattern(service_name, bulkhead_limit)
    
    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """Make resilient service call"""
        
        async def wrapped_call():
            return await self.timeout_handler.execute_with_timeout(func, *args, **kwargs)
        
        async def bulkhead_call():
            return await self.bulkhead.execute(wrapped_call)
        
        return await self.retry_handler.execute_with_retry(bulkhead_call)

# Saga Pattern for distributed transactions
class SagaStep:
    """Single step in a saga"""
    
    def __init__(
        self,
        name: str,
        action: Callable,
        compensation: Callable,
        *args,
        **kwargs
    ):
        self.name = name
        self.action = action
        self.compensation = compensation
        self.args = args
        self.kwargs = kwargs
        self.completed = False
        self.result = None

class SagaOrchestrator:
    """Orchestrator for saga pattern"""
    
    def __init__(self, saga_name: str):
        self.saga_name = saga_name
        self.steps = []
        self.completed_steps = []
    
    def add_step(
        self,
        name: str,
        action: Callable,
        compensation: Callable,
        *args,
        **kwargs
    ):
        """Add step to saga"""
        
        step = SagaStep(name, action, compensation, *args, **kwargs)
        self.steps.append(step)
    
    async def execute(self) -> dict:
        """Execute saga with compensation on failure"""
        
        logger.info(f"🎭 Starting saga: {self.saga_name}")
        
        try:
            # Execute all steps
            for step in self.steps:
                logger.info(f"⚡ Executing step: {step.name}")
                
                step.result = await step.action(*step.args, **step.kwargs)
                step.completed = True
                self.completed_steps.append(step)
                
                logger.info(f"✅ Completed step: {step.name}")
            
            logger.info(f"🎉 Saga completed successfully: {self.saga_name}")
            
            return {
                "status": "success",
                "saga_name": self.saga_name,
                "completed_steps": len(self.completed_steps),
                "results": [step.result for step in self.completed_steps]
            }
            
        except Exception as e:
            logger.error(f"❌ Saga failed: {self.saga_name} - {str(e)}")
            
            # Compensate completed steps in reverse order
            await self._compensate()
            
            return {
                "status": "failed",
                "saga_name": self.saga_name,
                "error": str(e),
                "compensated_steps": len(self.completed_steps)
            }
    
    async def _compensate(self):
        """Run compensation for completed steps"""
        
        logger.info(f"🔄 Starting compensation for: {self.saga_name}")
        
        # Compensate in reverse order
        for step in reversed(self.completed_steps):
            try:
                logger.info(f"↩️ Compensating step: {step.name}")
                await step.compensation(*step.args, **step.kwargs)
                logger.info(f"✅ Compensated step: {step.name}")
                
            except Exception as e:
                logger.error(f"❌ Compensation failed for step {step.name}: {str(e)}")
                # Continue with other compensations

# Example: Blog post creation saga
async def create_blog_post_saga(post_data: dict, author_id: int) -> dict:
    """Create blog post with distributed transaction"""
    
    saga = SagaOrchestrator("create_blog_post")
    
    # Step 1: Create post in content service
    saga.add_step(
        "create_post",
        content_service.create_post,
        content_service.delete_post,
        post_data, author_id
    )
    
    # Step 2: Update author statistics
    saga.add_step(
        "update_author_stats",
        user_service.increment_post_count,
        user_service.decrement_post_count,
        author_id
    )
    
    # Step 3: Send notifications
    saga.add_step(
        "send_notifications",
        notification_service.notify_followers,
        notification_service.cancel_notifications,
        author_id, "new_post"
    )
    
    # Step 4: Index for search
    saga.add_step(
        "index_post",
        search_service.index_post,
        search_service.remove_from_index,
        post_data
    )
    
    return await saga.execute()
```

---

### 🏠 Homework: Build Microservices Architecture

**Task:** Refactor your blog application into microservices

```python
# Create microservices architecture with:
# 1. User Service (authentication, profiles, preferences)
# 2. Content Service (posts, drafts, categories)
# 3. Engagement Service (comments, likes, shares)
# 4. Notification Service (email, push, in-app)
# 5. API Gateway (routing, load balancing, auth)

# Implementation Requirements:
# - Service-to-service HTTP communication
# - Event-driven communication with Redis/RabbitMQ
# - API Gateway with circuit breakers
# - Service discovery (Consul or custom)
# - Distributed tracing and logging
# - Health checks and monitoring
# - Database per service pattern

# Resilience Patterns:
# - Circuit breaker for service calls
# - Retry with exponential backoff
# - Bulkhead for resource isolation
# - Timeout handling
# - Saga pattern for distributed transactions

# Bonus Features:
# - Service mesh with Istio/Linkerd
# - Container orchestration with Docker Compose
# - API versioning strategy
# - Performance monitoring and metrics
```

---

### 📝 Key Takeaways

✅ Microservices = Independent, scalable service architecture
✅ Service Communication = HTTP APIs + event-driven messaging
✅ API Gateway = Single entry point with routing and security
✅ Service Discovery = Dynamic service location and health
✅ Resilience Patterns = Circuit breakers, retries, and timeouts

---

<a name="hour-39"></a>
## 📅 Hour 39: Observability (Logging, Metrics, Tracing)

### 🎯 Learning Objectives
- Implement structured logging with correlation IDs
- Set up metrics collection and monitoring dashboards
- Add distributed tracing for microservices
- Create alerting and incident response systems
- Build comprehensive observability for production systems

### 📖 What to Teach

**"Today we add eyes and ears to our applications - because you can't manage what you can't measure!"**

---

### 1️⃣ Structured Logging Implementation (15 minutes)

**Advanced Logging Setup:**

```python
# observability/logging_config.py
import logging
import json
import sys
import traceback
from datetime import datetime
from typing import Dict, Any, Optional
from contextvars import ContextVar
import uuid
from functools import wraps
import asyncio

# Context variables for request correlation
correlation_id: ContextVar[str] = ContextVar('correlation_id', default='')
user_id: ContextVar[str] = ContextVar('user_id', default='')
request_path: ContextVar[str] = ContextVar('request_path', default='')

class StructuredLogger:
    """Structured logging with correlation IDs and context"""
    
    def __init__(self, service_name: str, environment: str = "development"):
        self.service_name = service_name
        self.environment = environment
        self.logger = logging.getLogger(service_name)
        
        # Configure structured logging
        self._setup_logger()
    
    def _setup_logger(self):
        """Setup structured JSON logging"""
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Create console handler with structured formatter
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter(self.service_name, self.environment))
        
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        
        # Prevent duplicate logs
        self.logger.propagate = False
    
    def info(self, message: str, **kwargs):
        """Log info message with context"""
        self._log(logging.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message with context"""
        self._log(logging.WARNING, message, **kwargs)
    
    def error(self, message: str, exception: Exception = None, **kwargs):
        """Log error message with exception details"""
        
        extra_data = kwargs.copy()
        
        if exception:
            extra_data.update({
                "exception_type": type(exception).__name__,
                "exception_message": str(exception),
                "exception_traceback": traceback.format_exc()
            })
        
        self._log(logging.ERROR, message, **extra_data)
    
    def debug(self, message: str, **kwargs):
        """Log debug message with context"""
        self._log(logging.DEBUG, message, **kwargs)
    
    def _log(self, level: int, message: str, **kwargs):
        """Internal log method with context injection"""
        
        # Build log context
        log_context = {
            "correlation_id": correlation_id.get(),
            "user_id": user_id.get(),
            "request_path": request_path.get(),
            **kwargs
        }
        
        # Remove empty context values
        log_context = {k: v for k, v in log_context.items() if v}
        
        self.logger.log(level, message, extra={"context": log_context})

class StructuredFormatter(logging.Formatter):
    """JSON formatter for structured logs"""
    
    def __init__(self, service_name: str, environment: str):
        super().__init__()
        self.service_name = service_name
        self.environment = environment
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON"""
        
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "service": self.service_name,
            "environment": self.environment,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add context if available
        if hasattr(record, 'context'):
            log_entry.update(record.context)
        
        # Add exception info if present
        if record.exc_info:
            log_entry["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": self.formatException(record.exc_info)
            }
        
        return json.dumps(log_entry, ensure_ascii=False)

# Request correlation middleware
from fastapi import Request, Response
import time

class CorrelationMiddleware:
    """Middleware to add correlation ID to requests"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            # Generate or extract correlation ID
            headers = dict(scope.get("headers", []))
            correlation_header = headers.get(b"x-correlation-id")
            
            if correlation_header:
                corr_id = correlation_header.decode()
            else:
                corr_id = str(uuid.uuid4())
            
            # Set context variables
            correlation_id.set(corr_id)
            request_path.set(scope.get("path", ""))
            
            # Add correlation ID to response headers
            async def send_wrapper(message):
                if message["type"] == "http.response.start":
                    headers = message.get("headers", [])
                    headers.append([b"x-correlation-id", corr_id.encode()])
                    message["headers"] = headers
                await send(message)
            
            await self.app(scope, receive, send_wrapper)
        else:
            await self.app(scope, receive, send)

# Initialize structured logger
logger = StructuredLogger("blog-api", environment="production")

# Logging decorators
def log_function_call(func):
    """Decorator to log function calls with performance metrics"""
    
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        
        logger.info(
            f"🚀 Function call started: {func.__name__}",
            function=func.__name__,
            module=func.__module__,
            args_count=len(args),
            kwargs_keys=list(kwargs.keys())
        )
        
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            
            logger.info(
                f"✅ Function call completed: {func.__name__}",
                function=func.__name__,
                duration_ms=round(duration * 1000, 2),
                success=True
            )
            
            return result
            
        except Exception as e:
            duration = time.time() - start_time
            
            logger.error(
                f"❌ Function call failed: {func.__name__}",
                function=func.__name__,
                duration_ms=round(duration * 1000, 2),
                success=False,
                exception=e
            )
            
            raise
    
    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        
        logger.info(f"🚀 Function call started: {func.__name__}", function=func.__name__)
        
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            
            logger.info(
                f"✅ Function call completed: {func.__name__}",
                function=func.__name__,
                duration_ms=round(duration * 1000, 2)
            )
            
            return result
            
        except Exception as e:
            duration = time.time() - start_time
            
            logger.error(
                f"❌ Function call failed: {func.__name__}",
                function=func.__name__,
                duration_ms=round(duration * 1000, 2),
                exception=e
            )
            
            raise
    
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

# Database query logging
class DatabaseLogger:
    """Database query logging with performance tracking"""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.slow_query_threshold = 1.0  # 1 second
    
    def log_query(self, query: str, params: Dict = None, duration: float = None):
        """Log database query with performance metrics"""
        
        log_data = {
            "database": self.db_name,
            "query": query[:200] + "..." if len(query) > 200 else query,
            "param_count": len(params) if params else 0
        }
        
        if duration:
            log_data["duration_ms"] = round(duration * 1000, 2)
            
            if duration > self.slow_query_threshold:
                logger.warning("🐌 Slow database query detected", **log_data)
            else:
                logger.info("🗃️ Database query executed", **log_data)
        else:
            logger.info("🗃️ Database query started", **log_data)

# Usage examples
@log_function_call
async def get_user_posts(user_id: int) -> List[Dict]:
    """Get posts for user with logging"""
    
    db_logger = DatabaseLogger("blog_db")
    
    # Set user context
    user_id.set(str(user_id))
    
    logger.info(f"🔍 Fetching posts for user", user_id=user_id)
    
    # Simulate database query
    query = "SELECT * FROM posts WHERE author_id = $1 ORDER BY created_at DESC"
    start_time = time.time()
    
    db_logger.log_query(query, {"author_id": user_id})
    
    try:
        # Simulate query execution
        await asyncio.sleep(0.1)
        posts = [{"id": 1, "title": "Sample Post"}]  # Mock data
        
        duration = time.time() - start_time
        db_logger.log_query(query, {"author_id": user_id}, duration)
        
        logger.info(f"📚 Found {len(posts)} posts for user", post_count=len(posts))
        
        return posts
        
    except Exception as e:
        logger.error("❌ Failed to fetch user posts", user_id=user_id, exception=e)
        raise

# Error boundary for unhandled exceptions
class ErrorHandler:
    """Global error handler with structured logging"""
    
    def __init__(self):
        self.logger = logger
    
    async def handle_http_exception(self, request: Request, exc: Exception):
        """Handle HTTP exceptions with detailed logging"""
        
        # Extract request info
        request_info = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "client_ip": request.client.host
        }
        
        # Log error with context
        self.logger.error(
            f"🚨 HTTP Exception: {type(exc).__name__}",
            exception_type=type(exc).__name__,
            exception_message=str(exc),
            request_info=request_info,
            exception=exc
        )
        
        # Return appropriate error response
        return {
            "error": "Internal server error",
            "correlation_id": correlation_id.get(),
            "timestamp": datetime.utcnow().isoformat()
        }

# Log aggregation for ELK stack or similar
class LogAggregator:
    """Send logs to external aggregation service"""
    
    def __init__(self, elasticsearch_url: str = None):
        self.elasticsearch_url = elasticsearch_url
    
    async def send_logs(self, log_entries: List[Dict]):
        """Send structured logs to Elasticsearch"""
        
        if not self.elasticsearch_url:
            return
        
        try:
            # In production, use proper Elasticsearch client
            # This is a simplified example
            logger.debug(f"📤 Sending {len(log_entries)} logs to Elasticsearch")
            
        except Exception as e:
            # Don't fail the application due to logging issues
            logger.error("❌ Failed to send logs to aggregator", exception=e)
```

---

### 2️⃣ Metrics Collection and Monitoring (15 minutes)

**Prometheus Metrics Setup:**

```python
# observability/metrics.py
from prometheus_client import Counter, Histogram, Gauge, Summary, CollectorRegistry, generate_latest
import time
from typing import Dict, Any
from functools import wraps
import asyncio
import psutil
import threading

class ApplicationMetrics:
    """Comprehensive application metrics collection"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.registry = CollectorRegistry()
        
        # HTTP Metrics
        self.http_requests_total = Counter(
            'http_requests_total',
            'Total HTTP requests',
            ['method', 'endpoint', 'status_code'],
            registry=self.registry
        )
        
        self.http_request_duration_seconds = Histogram(
            'http_request_duration_seconds',
            'HTTP request duration in seconds',
            ['method', 'endpoint'],
            buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],
            registry=self.registry
        )
        
        # Database Metrics
        self.db_queries_total = Counter(
            'db_queries_total',
            'Total database queries',
            ['operation', 'table', 'status'],
            registry=self.registry
        )
        
        self.db_query_duration_seconds = Histogram(
            'db_query_duration_seconds', 
            'Database query duration in seconds',
            ['operation', 'table'],
            buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0],
            registry=self.registry
        )
        
        # Business Metrics
        self.active_users = Gauge(
            'active_users_total',
            'Number of currently active users',
            registry=self.registry
        )
        
        self.posts_created_total = Counter(
            'posts_created_total',
            'Total posts created',
            ['category', 'published'],
            registry=self.registry
        )
        
        self.comments_created_total = Counter(
            'comments_created_total', 
            'Total comments created',
            registry=self.registry
        )
        
        # System Metrics
        self.memory_usage_bytes = Gauge(
            'memory_usage_bytes',
            'Memory usage in bytes',
            registry=self.registry
        )
        
        self.cpu_usage_percent = Gauge(
            'cpu_usage_percent',
            'CPU usage percentage',
            registry=self.registry
        )
        
        # Cache Metrics
        self.cache_operations_total = Counter(
            'cache_operations_total',
            'Total cache operations',
            ['operation', 'cache_name', 'result'],
            registry=self.registry
        )
        
        # Queue Metrics
        self.queue_messages_total = Counter(
            'queue_messages_total',
            'Total queue messages',
            ['queue_name', 'status'],
            registry=self.registry
        )
        
        self.queue_size = Gauge(
            'queue_size',
            'Current queue size',
            ['queue_name'],
            registry=self.registry
        )
        
        # Start system metrics collection
        self._start_system_metrics_collection()
    
    def record_http_request(
        self, 
        method: str, 
        endpoint: str, 
        status_code: int, 
        duration: float
    ):
        """Record HTTP request metrics"""
        
        self.http_requests_total.labels(
            method=method,
            endpoint=endpoint,
            status_code=str(status_code)
        ).inc()
        
        self.http_request_duration_seconds.labels(
            method=method,
            endpoint=endpoint
        ).observe(duration)
    
    def record_db_query(
        self,
        operation: str,
        table: str,
        duration: float,
        success: bool = True
    ):
        """Record database query metrics"""
        
        status = "success" if success else "error"
        
        self.db_queries_total.labels(
            operation=operation,
            table=table,
            status=status
        ).inc()
        
        self.db_query_duration_seconds.labels(
            operation=operation,
            table=table
        ).observe(duration)
    
    def record_post_created(self, category: str, published: bool):
        """Record post creation metric"""
        
        self.posts_created_total.labels(
            category=category,
            published=str(published).lower()
        ).inc()
    
    def record_comment_created(self):
        """Record comment creation metric"""
        
        self.comments_created_total.inc()
    
    def record_cache_operation(
        self,
        operation: str,
        cache_name: str,
        hit: bool
    ):
        """Record cache operation metrics"""
        
        result = "hit" if hit else "miss"
        
        self.cache_operations_total.labels(
            operation=operation,
            cache_name=cache_name,
            result=result
        ).inc()
    
    def record_queue_message(
        self,
        queue_name: str,
        status: str
    ):
        """Record queue message metrics"""
        
        self.queue_messages_total.labels(
            queue_name=queue_name,
            status=status
        ).inc()
    
    def set_queue_size(self, queue_name: str, size: int):
        """Set current queue size"""
        
        self.queue_size.labels(queue_name=queue_name).set(size)
    
    def set_active_users(self, count: int):
        """Set active user count"""
        
        self.active_users.set(count)
    
    def _start_system_metrics_collection(self):
        """Start background thread for system metrics"""
        
        def collect_system_metrics():
            while True:
                try:
                    # Memory usage
                    memory_info = psutil.virtual_memory()
                    self.memory_usage_bytes.set(memory_info.used)
                    
                    # CPU usage
                    cpu_percent = psutil.cpu_percent(interval=1)
                    self.cpu_usage_percent.set(cpu_percent)
                    
                except Exception as e:
                    logger.error("❌ Failed to collect system metrics", exception=e)
                
                time.sleep(30)  # Collect every 30 seconds
        
        thread = threading.Thread(target=collect_system_metrics, daemon=True)
        thread.start()
    
    def get_metrics(self) -> str:
        """Get metrics in Prometheus format"""
        
        return generate_latest(self.registry).decode('utf-8')

# Metrics middleware
class MetricsMiddleware:
    """FastAPI middleware for metrics collection"""
    
    def __init__(self, app, metrics: ApplicationMetrics):
        self.app = app
        self.metrics = metrics
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            start_time = time.time()
            
            # Extract request info
            method = scope["method"]
            path = scope["path"]
            
            # Create response wrapper to capture status code
            status_code = 200
            
            async def send_wrapper(message):
                nonlocal status_code
                if message["type"] == "http.response.start":
                    status_code = message["status"]
                await send(message)
            
            try:
                await self.app(scope, receive, send_wrapper)
            finally:
                # Record metrics
                duration = time.time() - start_time
                self.metrics.record_http_request(method, path, status_code, duration)
        else:
            await self.app(scope, receive, send)

# Metrics decorators
def track_database_query(operation: str, table: str):
    """Decorator to track database queries"""
    
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                raise
            finally:
                duration = time.time() - start_time
                metrics.record_db_query(operation, table, duration, success)
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                raise
            finally:
                duration = time.time() - start_time
                metrics.record_db_query(operation, table, duration, success)
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator

# Initialize metrics
metrics = ApplicationMetrics("blog-api")

# Usage examples
@track_database_query("SELECT", "posts")
async def get_posts_from_db(limit: int = 10):
    """Example database query with metrics tracking"""
    
    # Simulate database query
    await asyncio.sleep(0.1)
    return [{"id": 1, "title": "Sample Post"}]

# Business logic with metrics
class PostService:
    """Post service with metrics tracking"""
    
    def __init__(self, metrics: ApplicationMetrics):
        self.metrics = metrics
    
    async def create_post(
        self,
        title: str,
        content: str,
        category: str,
        published: bool = False
    ):
        """Create post with metrics"""
        
        # Create post logic here
        post = {
            "id": 123,
            "title": title,
            "content": content,
            "category": category,
            "published": published
        }
        
        # Record metrics
        self.metrics.record_post_created(category, published)
        
        return post

# Metrics endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/metrics")
async def get_metrics():
    """Prometheus metrics endpoint"""
    
    from fastapi import Response
    
    metrics_data = metrics.get_metrics()
    
    return Response(
        content=metrics_data,
        media_type="text/plain; version=0.0.4; charset=utf-8"
    )

# Health check with metrics
@app.get("/health")
async def health_check():
    """Health check endpoint with metrics"""
    
    health_data = {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "blog-api",
        "version": "1.0.0"
    }
    
    # You could add metrics about health check frequency
    metrics.http_requests_total.labels(
        method="GET",
        endpoint="/health", 
        status_code="200"
    ).inc()
    
    return health_data

# Custom business metrics
class BusinessMetricsCollector:
    """Collect business-specific metrics"""
    
    def __init__(self, metrics: ApplicationMetrics):
        self.metrics = metrics
    
    async def collect_user_metrics(self):
        """Collect user-related metrics"""
        
        # Count active users (example with Redis)
        try:
            # active_users = await redis_client.scard("active_users")
            active_users = 42  # Mock data
            
            self.metrics.set_active_users(active_users)
            
        except Exception as e:
            logger.error("❌ Failed to collect user metrics", exception=e)
    
    async def collect_queue_metrics(self):
        """Collect queue metrics"""
        
        try:
            # Example queue sizes
            queue_sizes = {
                "email_queue": 15,
                "image_processing_queue": 8,
                "notification_queue": 3
            }
            
            for queue_name, size in queue_sizes.items():
                self.metrics.set_queue_size(queue_name, size)
                
        except Exception as e:
            logger.error("❌ Failed to collect queue metrics", exception=e)

# Periodic metrics collection
async def start_metrics_collection():
    """Start periodic business metrics collection"""
    
    collector = BusinessMetricsCollector(metrics)
    
    while True:
        try:
            await collector.collect_user_metrics()
            await collector.collect_queue_metrics()
            
        except Exception as e:
            logger.error("❌ Error in metrics collection", exception=e)
        
        # Collect every 60 seconds
        await asyncio.sleep(60)
```

**Grafana Dashboard Configuration:**

```json
{
  "dashboard": {
    "id": null,
    "title": "Blog API Dashboard",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{endpoint}}"
          }
        ]
      },
      {
        "title": "Response Time",
        "type": "graph", 
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          },
          {
            "expr": "histogram_quantile(0.50, rate(http_request_duration_seconds_bucket[5m]))", 
            "legendFormat": "50th percentile"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "singlestat",
        "targets": [
          {
            "expr": "rate(http_requests_total{status_code=~\"5..\"}[5m]) / rate(http_requests_total[5m]) * 100",
            "legendFormat": "Error Rate %"
          }
        ]
      },
      {
        "title": "Active Users",
        "type": "singlestat",
        "targets": [
          {
            "expr": "active_users_total",
            "legendFormat": "Active Users"
          }
        ]
      },
      {
        "title": "Database Query Performance",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(db_query_duration_seconds_bucket[5m]))",
            "legendFormat": "{{operation}} {{table}}"
          }
        ]
      }
    ]
  }
}
```

---

### 3️⃣ Distributed Tracing (10 minutes)

**OpenTelemetry Integration:**

```python
# observability/tracing.py
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import asyncio
from typing import Dict, Any, Optional
from functools import wraps

class DistributedTracing:
    """Distributed tracing setup with OpenTelemetry"""
    
    def __init__(
        self, 
        service_name: str,
        jaeger_endpoint: str = "http://localhost:14268/api/traces"
    ):
        self.service_name = service_name
        self.jaeger_endpoint = jaeger_endpoint
        
        # Setup tracing
        self._setup_tracer()
    
    def _setup_tracer(self):
        """Configure OpenTelemetry tracer"""
        
        # Create tracer provider
        trace.set_tracer_provider(TracerProvider())
        
        # Configure Jaeger exporter
        jaeger_exporter = JaegerExporter(
            agent_host_name="localhost",
            agent_port=6831,
            collector_endpoint=self.jaeger_endpoint,
        )
        
        # Create span processor
        span_processor = BatchSpanProcessor(jaeger_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
        
        # Get tracer
        self.tracer = trace.get_tracer(self.service_name)
    
    def instrument_app(self, app):
        """Instrument FastAPI application"""
        
        # Auto-instrument FastAPI
        FastAPIInstrumentor.instrument_app(app)
        
        # Auto-instrument database
        SQLAlchemyInstrumentor().instrument()
        
        # Auto-instrument Redis
        RedisInstrumentor().instrument()
        
        # Auto-instrument HTTP requests
        RequestsInstrumentor().instrument()
    
    def create_span(
        self,
        name: str,
        attributes: Optional[Dict[str, Any]] = None
    ):
        """Create a new span"""
        
        span = self.tracer.start_span(name)
        
        if attributes:
            for key, value in attributes.items():
                span.set_attribute(key, str(value))
        
        return span
    
    def trace_function(
        self,
        span_name: str = None,
        attributes: Optional[Dict[str, Any]] = None
    ):
        """Decorator to trace function execution"""
        
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                name = span_name or f"{func.__module__}.{func.__name__}"
                
                with self.tracer.start_as_current_span(name) as span:
                    # Add function attributes
                    span.set_attribute("function.name", func.__name__)
                    span.set_attribute("function.module", func.__module__)
                    
                    # Add custom attributes
                    if attributes:
                        for key, value in attributes.items():
                            span.set_attribute(key, str(value))
                    
                    try:
                        result = await func(*args, **kwargs)
                        span.set_attribute("function.success", True)
                        return result
                        
                    except Exception as e:
                        span.set_attribute("function.success", False)
                        span.set_attribute("function.error", str(e))
                        span.record_exception(e)
                        raise
            
            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                name = span_name or f"{func.__module__}.{func.__name__}"
                
                with self.tracer.start_as_current_span(name) as span:
                    span.set_attribute("function.name", func.__name__)
                    span.set_attribute("function.module", func.__module__)
                    
                    if attributes:
                        for key, value in attributes.items():
                            span.set_attribute(key, str(value))
                    
                    try:
                        result = func(*args, **kwargs)
                        span.set_attribute("function.success", True)
                        return result
                        
                    except Exception as e:
                        span.set_attribute("function.success", False)
                        span.set_attribute("function.error", str(e))
                        span.record_exception(e)
                        raise
            
            if asyncio.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper
        
        return decorator

# Initialize tracing
tracing = DistributedTracing("blog-api")

# Service-to-service tracing
class TracedServiceClient:
    """HTTP client with tracing support"""
    
    def __init__(self, service_name: str, base_url: str, tracer):
        self.service_name = service_name
        self.base_url = base_url
        self.tracer = tracer
    
    async def make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None
    ) -> Dict[Any, Any]:
        """Make HTTP request with tracing"""
        
        with self.tracer.start_as_current_span(f"http_client_{self.service_name}") as span:
            # Add HTTP attributes
            span.set_attribute("http.method", method)
            span.set_attribute("http.url", f"{self.base_url}{endpoint}")
            span.set_attribute("service.name", self.service_name)
            
            try:
                # Make HTTP request (using httpx or similar)
                # response = await httpx.request(method, f"{self.base_url}{endpoint}", json=data)
                
                # Mock response for example
                await asyncio.sleep(0.1)
                response_data = {"status": "success"}
                
                span.set_attribute("http.status_code", 200)
                span.set_attribute("http.response_size", len(str(response_data)))
                
                return response_data
                
            except Exception as e:
                span.set_attribute("http.status_code", 500)
                span.record_exception(e)
                raise

# Database tracing
class TracedDatabase:
    """Database operations with tracing"""
    
    def __init__(self, tracer):
        self.tracer = tracer
    
    @tracing.trace_function("db.query", {"component": "database"})
    async def execute_query(
        self,
        query: str,
        params: Optional[Dict] = None
    ) -> List[Dict]:
        """Execute database query with tracing"""
        
        # Current span is automatically available
        current_span = trace.get_current_span()
        
        # Add database-specific attributes
        current_span.set_attribute("db.statement", query)
        current_span.set_attribute("db.operation", query.split()[0].upper())
        
        if params:
            current_span.set_attribute("db.params_count", len(params))
        
        # Simulate query execution
        await asyncio.sleep(0.05)
        
        result = [{"id": 1, "title": "Sample"}]
        current_span.set_attribute("db.rows_affected", len(result))
        
        return result

# Business logic with tracing
class TracedPostService:
    """Post service with comprehensive tracing"""
    
    def __init__(self, tracer):
        self.tracer = tracer
        self.db = TracedDatabase(tracer)
        self.user_service = TracedServiceClient("user-service", "http://user-service:8000", tracer)
    
    @tracing.trace_function("post.create", {"operation": "create_post"})
    async def create_post(
        self,
        title: str,
        content: str,
        author_id: int
    ) -> Dict[str, Any]:
        """Create post with distributed tracing"""
        
        current_span = trace.get_current_span()
        
        # Add business context
        current_span.set_attribute("post.title", title)
        current_span.set_attribute("post.author_id", author_id)
        current_span.set_attribute("post.content_length", len(content))
        
        try:
            # Step 1: Validate author exists
            with self.tracer.start_as_current_span("post.validate_author") as span:
                span.set_attribute("user.id", author_id)
                
                author = await self.user_service.make_request(
                    "GET",
                    f"/api/v1/users/{author_id}"
                )
                
                span.set_attribute("user.found", author is not None)
            
            # Step 2: Create post in database
            with self.tracer.start_as_current_span("post.save_to_db") as span:
                query = "INSERT INTO posts (title, content, author_id) VALUES ($1, $2, $3) RETURNING id"
                
                result = await self.db.execute_query(
                    query,
                    {"title": title, "content": content, "author_id": author_id}
                )
                
                post_id = result[0]["id"] if result else None
                span.set_attribute("post.id", post_id)
            
            # Step 3: Send notifications
            with self.tracer.start_as_current_span("post.send_notifications") as span:
                notification_data = {
                    "type": "new_post",
                    "post_id": post_id,
                    "author_id": author_id
                }
                
                # Simulate notification sending
                await asyncio.sleep(0.02)
                
                span.set_attribute("notifications.sent", True)
            
            # Success
            current_span.set_attribute("post.creation_success", True)
            
            return {
                "id": post_id,
                "title": title,
                "author_id": author_id,
                "status": "created"
            }
            
        except Exception as e:
            current_span.set_attribute("post.creation_success", False)
            current_span.record_exception(e)
            raise

# Custom span context manager
class TraceContext:
    """Context manager for custom spans"""
    
    def __init__(self, tracer, span_name: str, **attributes):
        self.tracer = tracer
        self.span_name = span_name
        self.attributes = attributes
        self.span = None
    
    async def __aenter__(self):
        self.span = self.tracer.start_span(self.span_name)
        
        for key, value in self.attributes.items():
            self.span.set_attribute(key, str(value))
        
        return self.span
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.span.record_exception(exc_val)
            self.span.set_attribute("error", True)
        else:
            self.span.set_attribute("success", True)
        
        self.span.end()

# Usage examples
async def complex_business_operation(user_id: int, data: Dict):
    """Example of complex operation with tracing"""
    
    async with TraceContext(
        tracing.tracer,
        "complex_business_operation",
        user_id=user_id,
        operation_type="complex"
    ) as span:
        
        # Step 1: Validate user
        async with TraceContext(tracing.tracer, "validate_user", user_id=user_id):
            # Validation logic
            await asyncio.sleep(0.01)
        
        # Step 2: Process data
        async with TraceContext(tracing.tracer, "process_data", data_size=len(data)):
            # Processing logic
            await asyncio.sleep(0.05)
        
        # Step 3: Save results
        async with TraceContext(tracing.tracer, "save_results"):
            # Save logic
            await asyncio.sleep(0.02)
        
        span.set_attribute("operation_completed", True)
        return {"status": "success"}
```

---

### 4️⃣ Alerting and Incident Response (10 minutes)

**Comprehensive Alerting System:**

```python
# observability/alerting.py
import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import aiohttp
import logging

logger = logging.getLogger(__name__)

class AlertSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"
    CRITICAL = "critical"

class AlertStatus(Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    ACKNOWLEDGED = "acknowledged"

@dataclass
class Alert:
    """Alert data structure"""
    
    id: str
    title: str
    description: str
    severity: AlertSeverity
    status: AlertStatus
    service: str
    created_at: datetime
    updated_at: datetime
    labels: Dict[str, str]
    annotations: Dict[str, str]
    resolved_at: Optional[datetime] = None

class AlertManager:
    """Centralized alert management"""
    
    def __init__(self):
        self.active_alerts: Dict[str, Alert] = {}
        self.alert_handlers = []
        self.notification_channels = []
    
    def add_notification_channel(self, channel):
        """Add notification channel (Slack, email, etc.)"""
        self.notification_channels.append(channel)
    
    def add_alert_handler(self, handler):
        """Add custom alert handler"""
        self.alert_handlers.append(handler)
    
    async def create_alert(
        self,
        alert_id: str,
        title: str,
        description: str,
        severity: AlertSeverity,
        service: str,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None
    ) -> Alert:
        """Create new alert"""
        
        alert = Alert(
            id=alert_id,
            title=title,
            description=description,
            severity=severity,
            status=AlertStatus.ACTIVE,
            service=service,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            labels=labels or {},
            annotations=annotations or {}
        )
        
        self.active_alerts[alert_id] = alert
        
        logger.warning(f"🚨 Alert created: {title} ({severity.value})")
        
        # Send notifications
        await self._send_notifications(alert, "created")
        
        # Run custom handlers
        for handler in self.alert_handlers:
            try:
                await handler.on_alert_created(alert)
            except Exception as e:
                logger.error(f"❌ Alert handler error: {str(e)}")
        
        return alert
    
    async def resolve_alert(self, alert_id: str) -> bool:
        """Resolve an active alert"""
        
        if alert_id not in self.active_alerts:
            return False
        
        alert = self.active_alerts[alert_id]
        alert.status = AlertStatus.RESOLVED
        alert.resolved_at = datetime.utcnow()
        alert.updated_at = datetime.utcnow()
        
        logger.info(f"✅ Alert resolved: {alert.title}")
        
        # Send notifications
        await self._send_notifications(alert, "resolved")
        
        # Remove from active alerts
        del self.active_alerts[alert_id]
        
        return True
    
    async def _send_notifications(self, alert: Alert, action: str):
        """Send alert notifications to all channels"""
        
        for channel in self.notification_channels:
            try:
                await channel.send_alert(alert, action)
            except Exception as e:
                logger.error(f"❌ Notification failed: {str(e)}")

class SlackNotificationChannel:
    """Slack notification channel"""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    async def send_alert(self, alert: Alert, action: str):
        """Send alert to Slack"""
        
        color_map = {
            AlertSeverity.LOW: "#36a64f",
            AlertSeverity.MEDIUM: "#ffaa00", 
            AlertSeverity.HIGH: "#ff6600",
            AlertSeverity.CRITICAL: "#ff0000"
        }
        
        emoji_map = {
            "created": "🚨",
            "resolved": "✅",
            "acknowledged": "👀"
        }
        
        message = {
            "attachments": [
                {
                    "color": color_map.get(alert.severity, "#cccccc"),
                    "title": f"{emoji_map.get(action, '⚠️')} Alert {action.title()}: {alert.title}",
                    "text": alert.description,
                    "fields": [
                        {
                            "title": "Service",
                            "value": alert.service,
                            "short": True
                        },
                        {
                            "title": "Severity", 
                            "value": alert.severity.value.upper(),
                            "short": True
                        },
                        {
                            "title": "Time",
                            "value": alert.created_at.isoformat(),
                            "short": True
                        }
                    ]
                }
            ]
        }
        
        # Add labels and annotations
        if alert.labels:
            message["attachments"][0]["fields"].append({
                "title": "Labels",
                "value": ", ".join([f"{k}={v}" for k, v in alert.labels.items()]),
                "short": False
            })
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.webhook_url, json=message) as response:
                if response.status != 200:
                    raise Exception(f"Slack notification failed: {response.status}")

class EmailNotificationChannel:
    """Email notification channel"""
    
    def __init__(self, smtp_config: Dict[str, Any]):
        self.smtp_config = smtp_config
    
    async def send_alert(self, alert: Alert, action: str):
        """Send alert via email"""
        
        subject = f"[{alert.severity.value.upper()}] {alert.title}"
        
        body = f"""
Alert {action}: {alert.title}

Description: {alert.description}
Service: {alert.service}
Severity: {alert.severity.value}
Time: {alert.created_at.isoformat()}

Labels: {', '.join([f"{k}={v}" for k, v in alert.labels.items()])}

--
Automated Alert System
"""
        
        # Implementation would use actual SMTP client
        logger.info(f"📧 Email alert sent: {subject}")

class HealthChecker:
    """System health monitoring with alerting"""
    
    def __init__(self, alert_manager: AlertManager):
        self.alert_manager = alert_manager
        self.checks = {}
        self.check_interval = 60  # seconds
        self.running = False
    
    def add_health_check(
        self,
        name: str,
        check_func: callable,
        threshold: float = 0.8,
        severity: AlertSeverity = AlertSeverity.HIGH
    ):
        """Add health check"""
        
        self.checks[name] = {
            "func": check_func,
            "threshold": threshold,
            "severity": severity,
            "last_status": None,
            "consecutive_failures": 0
        }
    
    async def start_monitoring(self):
        """Start health monitoring loop"""
        
        self.running = True
        
        while self.running:
            try:
                for name, check_config in self.checks.items():
                    await self._run_health_check(name, check_config)
                
            except Exception as e:
                logger.error(f"❌ Health check error: {str(e)}")
            
            await asyncio.sleep(self.check_interval)
    
    async def _run_health_check(self, name: str, config: Dict):
        """Run individual health check"""
        
        try:
            # Run check function
            result = await config["func"]()
            
            is_healthy = result >= config["threshold"]
            
            if not is_healthy:
                config["consecutive_failures"] += 1
                
                # Create alert after 3 consecutive failures
                if config["consecutive_failures"] >= 3:
                    alert_id = f"health_check_{name}"
                    
                    if alert_id not in self.alert_manager.active_alerts:
                        await self.alert_manager.create_alert(
                            alert_id=alert_id,
                            title=f"Health Check Failed: {name}",
                            description=f"Health check '{name}' failed with value {result:.2f} (threshold: {config['threshold']})",
                            severity=config["severity"],
                            service="health-monitor",
                            labels={
                                "check_name": name,
                                "value": str(result),
                                "threshold": str(config["threshold"])
                            }
                        )
            else:
                config["consecutive_failures"] = 0
                
                # Resolve alert if it exists
                alert_id = f"health_check_{name}"
                await self.alert_manager.resolve_alert(alert_id)
            
            config["last_status"] = is_healthy
            
        except Exception as e:
            logger.error(f"❌ Health check '{name}' failed: {str(e)}")
            config["consecutive_failures"] += 1

# Metric-based alerting
class MetricAlerter:
    """Create alerts based on metrics thresholds"""
    
    def __init__(self, alert_manager: AlertManager, metrics: ApplicationMetrics):
        self.alert_manager = alert_manager
        self.metrics = metrics
        self.thresholds = {}
    
    def add_threshold(
        self,
        metric_name: str,
        threshold_value: float,
        comparison: str = "greater",  # "greater", "less", "equal"
        severity: AlertSeverity = AlertSeverity.MEDIUM,
        duration: int = 300  # seconds
    ):
        """Add metric threshold for alerting"""
        
        self.thresholds[metric_name] = {
            "value": threshold_value,
            "comparison": comparison,
            "severity": severity,
            "duration": duration,
            "triggered_at": None
        }
    
    async def check_thresholds(self):
        """Check all metric thresholds"""
        
        for metric_name, config in self.thresholds.items():
            try:
                # Get current metric value (simplified)
                current_value = await self._get_metric_value(metric_name)
                
                if current_value is None:
                    continue
                
                # Check threshold
                threshold_exceeded = self._check_threshold(
                    current_value,
                    config["value"],
                    config["comparison"]
                )
                
                alert_id = f"metric_threshold_{metric_name}"
                
                if threshold_exceeded:
                    if not config["triggered_at"]:
                        config["triggered_at"] = datetime.utcnow()
                    
                    # Check if duration exceeded
                    elif (datetime.utcnow() - config["triggered_at"]).seconds >= config["duration"]:
                        
                        if alert_id not in self.alert_manager.active_alerts:
                            await self.alert_manager.create_alert(
                                alert_id=alert_id,
                                title=f"Metric Threshold Exceeded: {metric_name}",
                                description=f"Metric {metric_name} = {current_value} {config['comparison']} {config['value']} for {config['duration']}s",
                                severity=config["severity"],
                                service="metric-monitor",
                                labels={
                                    "metric": metric_name,
                                    "current_value": str(current_value),
                                    "threshold": str(config["value"]),
                                    "comparison": config["comparison"]
                                }
                            )
                else:
                    config["triggered_at"] = None
                    await self.alert_manager.resolve_alert(alert_id)
                    
            except Exception as e:
                logger.error(f"❌ Threshold check failed for {metric_name}: {str(e)}")
    
    def _check_threshold(self, value: float, threshold: float, comparison: str) -> bool:
        """Check if value exceeds threshold"""
        
        if comparison == "greater":
            return value > threshold
        elif comparison == "less":
            return value < threshold
        elif comparison == "equal":
            return abs(value - threshold) < 0.001
        
        return False
    
    async def _get_metric_value(self, metric_name: str) -> Optional[float]:
        """Get current metric value"""
        
        # This would integrate with actual metrics collection
        # For example purposes, return mock values
        metric_values = {
            "error_rate": 0.05,  # 5% error rate
            "response_time_p95": 2.5,  # 2.5 seconds
            "cpu_usage": 75.0,  # 75% CPU
            "memory_usage": 80.0  # 80% memory
        }
        
        return metric_values.get(metric_name)

# Initialize alerting system
alert_manager = AlertManager()

# Setup notification channels
slack_channel = SlackNotificationChannel("https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK")
alert_manager.add_notification_channel(slack_channel)

# Setup health monitoring
async def database_health_check() -> float:
    """Check database health"""
    try:
        # Simulate database ping
        await asyncio.sleep(0.01)
        return 1.0  # Healthy
    except:
        return 0.0  # Unhealthy

async def api_response_time_check() -> float:
    """Check API response time"""
    # Return percentage of requests under threshold
    return 0.85  # 85% under threshold

health_checker = HealthChecker(alert_manager)
health_checker.add_health_check("database", database_health_check, threshold=0.9)
health_checker.add_health_check("api_response_time", api_response_time_check, threshold=0.8)

# Setup metric alerting
metric_alerter = MetricAlerter(alert_manager, metrics)
metric_alerter.add_threshold("error_rate", 0.1, "greater", AlertSeverity.HIGH)
metric_alerter.add_threshold("response_time_p95", 5.0, "greater", AlertSeverity.MEDIUM)
```

---

### 🏠 Homework: Complete Observability Stack

**Task:** Implement comprehensive observability for your blog application

```python
# Build a complete observability solution with:
# 1. Structured logging with correlation IDs
# 2. Comprehensive metrics collection (business + system)
# 3. Distributed tracing across microservices
# 4. Real-time alerting with multiple channels
# 5. Health monitoring and SLA tracking
# 6. Performance monitoring and optimization
# 7. Error tracking and incident response
# 8. Custom dashboards and reporting

# Technical Requirements:
# - ELK/EFK stack for log aggregation
# - Prometheus + Grafana for metrics
# - Jaeger/Zipkin for distributed tracing  
# - AlertManager for alerting
# - Custom business metrics
# - SLI/SLO monitoring

# Monitoring Scope:
# - API performance and errors
# - Database query performance
# - Cache hit rates and performance
# - Queue sizes and processing times
# - User behavior and engagement
# - Infrastructure metrics
# - Business KPIs

# Bonus Features:
# - Anomaly detection with ML
# - Predictive alerting
# - Automated incident response
# - Performance regression detection
```

---

### 📝 Key Takeaways

✅ Structured Logging = JSON logs with correlation IDs and context
✅ Metrics Collection = Prometheus metrics for performance monitoring
✅ Distributed Tracing = OpenTelemetry for request flow visibility
✅ Alerting = Multi-channel notifications for incidents
✅ Observability = Complete visibility into system behavior

---

<a name="hour-40"></a>
## 🧪 Hour 40: Testing & CI for Backend

### 🎯 Learning Objectives
- Implement comprehensive testing strategies (unit, integration, e2e)
- Build automated testing pipelines with pytest
- Set up continuous integration with GitHub Actions
- Create test environments and data management
- Implement code coverage and quality gates
- Deploy with confidence using automated testing

### 📖 What to Teach

**"The final hour - where we build unbreakable systems through testing and automation!"**

---

### 1️⃣ Comprehensive Testing Framework (15 minutes)

**Advanced Testing Setup with pytest:**

```python
# tests/conftest.py
import pytest
import asyncio
import asyncpg
from fastapi.testclient import TestClient
from httpx import AsyncClient
import redis.asyncio as redis
from unittest.mock import AsyncMock, MagicMock
import tempfile
import os
from typing import AsyncGenerator, Generator
import uuid

# Import your application
from app.main import create_app
from app.database import get_database
from app.cache import get_redis
from app.auth import get_current_user
from app.config import Settings

# Test settings
@pytest.fixture(scope="session")
def test_settings() -> Settings:
    """Test configuration"""
    return Settings(
        database_url="postgresql://test_user:test_pass@localhost:5433/test_blog",
        redis_url="redis://localhost:6380/1",
        secret_key="test_secret_key_for_testing_only",
        environment="testing"
    )

# Database fixtures
@pytest.fixture(scope="session")
async def test_db_pool(test_settings):
    """Create test database connection pool"""
    
    pool = await asyncpg.create_pool(test_settings.database_url)
    
    # Create test schema
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                username VARCHAR(100) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER REFERENCES users(id),
                published BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                post_id INTEGER REFERENCES posts(id),
                author_id INTEGER REFERENCES users(id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    
    yield pool
    
    # Cleanup
    async with pool.acquire() as conn:
        await conn.execute("DROP TABLE IF EXISTS comments CASCADE")
        await conn.execute("DROP TABLE IF EXISTS posts CASCADE") 
        await conn.execute("DROP TABLE IF EXISTS users CASCADE")
    
    await pool.close()

@pytest.fixture
async def db_conn(test_db_pool):
    """Get database connection for test"""
    
    async with test_db_pool.acquire() as conn:
        # Start transaction
        tx = conn.transaction()
        await tx.start()
        
        yield conn
        
        # Rollback transaction (cleanup)
        await tx.rollback()

# Redis fixtures
@pytest.fixture(scope="session")
async def test_redis_client(test_settings):
    """Create test Redis client"""
    
    client = redis.from_url(test_settings.redis_url)
    
    yield client
    
    # Cleanup
    await client.flushdb()
    await client.aclose()

@pytest.fixture
async def redis_conn(test_redis_client):
    """Get Redis connection for test"""
    
    # Clear before test
    await test_redis_client.flushdb()
    
    yield test_redis_client
    
    # Clear after test
    await test_redis_client.flushdb()

# Application fixtures
@pytest.fixture
async def app(test_settings, test_db_pool, test_redis_client):
    """Create test FastAPI application"""
    
    app = create_app(test_settings)
    
    # Override dependencies
    app.dependency_overrides[get_database] = lambda: test_db_pool
    app.dependency_overrides[get_redis] = lambda: test_redis_client
    
    yield app
    
    # Cleanup overrides
    app.dependency_overrides.clear()

@pytest.fixture
async def client(app) -> AsyncGenerator[AsyncClient, None]:
    """Create async HTTP client"""
    
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.fixture
def sync_client(app) -> Generator[TestClient, None, None]:
    """Create synchronous HTTP client"""
    
    with TestClient(app) as client:
        yield client

# User fixtures
@pytest.fixture
async def test_user(db_conn):
    """Create test user"""
    
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "hashed_password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj.qK5XQ5zGO"  # "testpass123"
    }
    
    result = await db_conn.fetchrow("""
        INSERT INTO users (email, username, hashed_password) 
        VALUES ($1, $2, $3) 
        RETURNING id, email, username, is_active, created_at
    """, user_data["email"], user_data["username"], user_data["hashed_password"])
    
    return dict(result)

@pytest.fixture
async def authenticated_user(test_user, app):
    """Create authenticated user for testing"""
    
    # Mock authentication
    async def mock_get_current_user():
        return test_user
    
    app.dependency_overrides[get_current_user] = mock_get_current_user
    
    return test_user

@pytest.fixture
async def test_post(test_user, db_conn):
    """Create test post"""
    
    post_data = {
        "title": "Test Post Title",
        "content": "This is test post content for testing purposes.",
        "author_id": test_user["id"],
        "published": True
    }
    
    result = await db_conn.fetchrow("""
        INSERT INTO posts (title, content, author_id, published) 
        VALUES ($1, $2, $3, $4) 
        RETURNING id, title, content, author_id, published, created_at
    """, post_data["title"], post_data["content"], post_data["author_id"], post_data["published"])
    
    return dict(result)

# Mock fixtures
@pytest.fixture
def mock_email_service():
    """Mock email service"""
    
    mock = AsyncMock()
    mock.send_email.return_value = True
    return mock

@pytest.fixture 
def mock_file_storage():
    """Mock file storage service"""
    
    mock = AsyncMock()
    mock.upload_file.return_value = "https://example.com/file.jpg"
    mock.delete_file.return_value = True
    return mock

# Test data factories
class UserFactory:
    """Factory for creating test users"""
    
    @staticmethod
    def build(**kwargs):
        """Build user data"""
        
        defaults = {
            "email": f"user_{uuid.uuid4()}@example.com",
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "testpass123",
            "is_active": True
        }
        
        return {**defaults, **kwargs}
    
    @staticmethod
    async def create(db_conn, **kwargs):
        """Create user in database"""
        
        user_data = UserFactory.build(**kwargs)
        
        # Hash password
        from app.auth import get_password_hash
        hashed_password = get_password_hash(user_data.pop("password"))
        
        result = await db_conn.fetchrow("""
            INSERT INTO users (email, username, hashed_password, is_active) 
            VALUES ($1, $2, $3, $4) 
            RETURNING id, email, username, is_active, created_at
        """, user_data["email"], user_data["username"], hashed_password, user_data["is_active"])
        
        return dict(result)

class PostFactory:
    """Factory for creating test posts"""
    
    @staticmethod
    def build(author_id: int, **kwargs):
        """Build post data"""
        
        defaults = {
            "title": f"Test Post {uuid.uuid4().hex[:8]}",
            "content": "This is test content for the post.",
            "author_id": author_id,
            "published": False
        }
        
        return {**defaults, **kwargs}
    
    @staticmethod
    async def create(db_conn, author_id: int, **kwargs):
        """Create post in database"""
        
        post_data = PostFactory.build(author_id, **kwargs)
        
        result = await db_conn.fetchrow("""
            INSERT INTO posts (title, content, author_id, published) 
            VALUES ($1, $2, $3, $4) 
            RETURNING id, title, content, author_id, published, created_at, updated_at
        """, post_data["title"], post_data["content"], post_data["author_id"], post_data["published"])
        
        return dict(result)

# Helper functions
def assert_response_data(response, expected_data: dict):
    """Assert response contains expected data"""
    
    response_data = response.json()
    
    for key, value in expected_data.items():
        assert key in response_data
        assert response_data[key] == value

async def create_test_data(db_conn, num_users=5, posts_per_user=3):
    """Create test data for integration tests"""
    
    users = []
    posts = []
    
    for i in range(num_users):
        user = await UserFactory.create(db_conn)
        users.append(user)
        
        for j in range(posts_per_user):
            post = await PostFactory.create(db_conn, user["id"], published=True)
            posts.append(post)
    
    return users, posts

# Event loop configuration
@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Performance testing helpers
@pytest.fixture
def performance_tracker():
    """Track test performance"""
    
    class PerformanceTracker:
        def __init__(self):
            self.start_time = None
            self.measurements = {}
        
        def start(self, name: str):
            import time
            self.start_time = time.time()
        
        def stop(self, name: str):
            import time
            if self.start_time:
                duration = time.time() - self.start_time
                self.measurements[name] = duration
                return duration
            return None
        
        def assert_duration_under(self, name: str, max_duration: float):
            assert name in self.measurements
            assert self.measurements[name] < max_duration, \
                f"Operation {name} took {self.measurements[name]:.3f}s, expected < {max_duration}s"
    
    return PerformanceTracker()
```

**Unit Tests:**

```python
# tests/unit/test_auth.py
import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from app.auth import (
    create_access_token, 
    verify_token, 
    get_password_hash, 
    verify_password,
    authenticate_user
)
from app.models import User

class TestAuthentication:
    """Test authentication functions"""
    
    def test_password_hashing(self):
        """Test password hashing and verification"""
        
        password = "testpassword123"
        
        # Test hashing
        hashed = get_password_hash(password)
        assert hashed != password
        assert len(hashed) > 50
        
        # Test verification
        assert verify_password(password, hashed) is True
        assert verify_password("wrongpassword", hashed) is False
    
    def test_create_access_token(self):
        """Test JWT token creation"""
        
        data = {"sub": "testuser", "user_id": 123}
        token = create_access_token(data, expires_delta=None)
        
        assert isinstance(token, str)
        assert len(token) > 100
        
        # Verify token contains expected data
        payload = verify_token(token)
        assert payload["sub"] == "testuser"
        assert payload["user_id"] == 123
    
    def test_verify_token_valid(self):
        """Test token verification with valid token"""
        
        data = {"sub": "testuser", "user_id": 123}
        token = create_access_token(data)
        
        payload = verify_token(token)
        assert payload["sub"] == "testuser"
        assert payload["user_id"] == 123
    
    def test_verify_token_invalid(self):
        """Test token verification with invalid token"""
        
        with pytest.raises(HTTPException) as exc_info:
            verify_token("invalid_token")
        
        assert exc_info.value.status_code == 401
    
    @pytest.mark.asyncio
    async def test_authenticate_user_success(self, db_conn):
        """Test successful user authentication"""
        
        # Create test user
        hashed_password = get_password_hash("testpass123")
        
        await db_conn.execute("""
            INSERT INTO users (email, username, hashed_password) 
            VALUES ($1, $2, $3)
        """, "test@example.com", "testuser", hashed_password)
        
        # Test authentication
        with patch('app.auth.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {
                "id": 1,
                "username": "testuser",
                "email": "test@example.com",
                "hashed_password": hashed_password,
                "is_active": True
            }
            
            user = await authenticate_user(db_conn, "testuser", "testpass123")
            assert user is not None
            assert user["username"] == "testuser"
    
    @pytest.mark.asyncio
    async def test_authenticate_user_failure(self, db_conn):
        """Test failed user authentication"""
        
        with patch('app.auth.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = None
            
            user = await authenticate_user(db_conn, "nonexistent", "password")
            assert user is None

# tests/unit/test_models.py
import pytest
from pydantic import ValidationError
from app.schemas import UserCreate, PostCreate, UserResponse

class TestSchemas:
    """Test Pydantic schemas"""
    
    def test_user_create_valid(self):
        """Test valid user creation schema"""
        
        user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123"
        }
        
        user = UserCreate(**user_data)
        assert user.email == "test@example.com"
        assert user.username == "testuser"
        assert user.password == "testpass123"
    
    def test_user_create_invalid_email(self):
        """Test invalid email validation"""
        
        with pytest.raises(ValidationError):
            UserCreate(
                email="invalid_email",
                username="testuser",
                password="testpass123"
            )
    
    def test_user_create_short_password(self):
        """Test short password validation"""
        
        with pytest.raises(ValidationError):
            UserCreate(
                email="test@example.com",
                username="testuser", 
                password="123"  # Too short
            )
    
    def test_post_create_valid(self):
        """Test valid post creation schema"""
        
        post_data = {
            "title": "Test Post",
            "content": "This is test content that is long enough.",
            "published": True
        }
        
        post = PostCreate(**post_data)
        assert post.title == "Test Post"
        assert post.published is True
    
    def test_post_create_title_too_short(self):
        """Test post title validation"""
        
        with pytest.raises(ValidationError):
            PostCreate(
                title="Hi",  # Too short
                content="This is test content that is long enough.",
                published=False
            )

# tests/unit/test_services.py
import pytest
from unittest.mock import AsyncMock, patch
from app.services import PostService, UserService
from app.exceptions import NotFoundError, ValidationError

class TestPostService:
    """Test post service business logic"""
    
    @pytest.fixture
    def post_service(self):
        return PostService()
    
    @pytest.mark.asyncio
    async def test_create_post_success(self, post_service):
        """Test successful post creation"""
        
        with patch.object(post_service, 'db') as mock_db:
            mock_db.fetchrow.return_value = {
                "id": 1,
                "title": "Test Post",
                "content": "Test content",
                "author_id": 1,
                "published": False
            }
            
            post_data = {
                "title": "Test Post",
                "content": "Test content",
                "published": False
            }
            
            result = await post_service.create_post(1, post_data)
            
            assert result["title"] == "Test Post"
            assert result["author_id"] == 1
            mock_db.fetchrow.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_post_not_found(self, post_service):
        """Test getting non-existent post"""
        
        with patch.object(post_service, 'db') as mock_db:
            mock_db.fetchrow.return_value = None
            
            with pytest.raises(NotFoundError):
                await post_service.get_post(999)
    
    @pytest.mark.asyncio
    async def test_update_post_unauthorized(self, post_service):
        """Test updating post by non-owner"""
        
        with patch.object(post_service, 'db') as mock_db:
            mock_db.fetchrow.return_value = {
                "id": 1,
                "author_id": 2  # Different author
            }
            
            with pytest.raises(ValidationError):
                await post_service.update_post(1, 1, {"title": "New Title"})
```

**Integration Tests:**

```python
# tests/integration/test_api.py
import pytest
from httpx import AsyncClient
from app.schemas import UserCreate, PostCreate

class TestUserAPI:
    """Test user API endpoints"""
    
    @pytest.mark.asyncio
    async def test_create_user(self, client: AsyncClient):
        """Test user registration"""
        
        user_data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpass123"
        }
        
        response = await client.post("/api/v1/users/", json=user_data)
        
        assert response.status_code == 201
        
        data = response.json()
        assert data["email"] == user_data["email"]
        assert data["username"] == user_data["username"]
        assert "id" in data
        assert "hashed_password" not in data  # Should not return password
    
    @pytest.mark.asyncio
    async def test_create_user_duplicate_email(self, client: AsyncClient, test_user):
        """Test creating user with duplicate email"""
        
        user_data = {
            "email": test_user["email"],  # Duplicate email
            "username": "different_username",
            "password": "newpass123"
        }
        
        response = await client.post("/api/v1/users/", json=user_data)
        
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]
    
    @pytest.mark.asyncio
    async def test_login_user(self, client: AsyncClient, test_user):
        """Test user login"""
        
        login_data = {
            "username": test_user["username"],
            "password": "testpass123"
        }
        
        response = await client.post("/api/v1/auth/login", data=login_data)
        
        assert response.status_code == 200
        
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    @pytest.mark.asyncio
    async def test_get_current_user(self, client: AsyncClient, authenticated_user):
        """Test getting current user profile"""
        
        response = await client.get("/api/v1/users/me")
        
        assert response.status_code == 200
        
        data = response.json()
        assert data["id"] == authenticated_user["id"]
        assert data["username"] == authenticated_user["username"]

class TestPostAPI:
    """Test post API endpoints"""
    
    @pytest.mark.asyncio
    async def test_create_post(self, client: AsyncClient, authenticated_user):
        """Test creating a new post"""
        
        post_data = {
            "title": "Integration Test Post",
            "content": "This is content for integration testing.",
            "published": True
        }
        
        response = await client.post("/api/v1/posts/", json=post_data)
        
        assert response.status_code == 201
        
        data = response.json()
        assert data["title"] == post_data["title"]
        assert data["content"] == post_data["content"]
        assert data["author_id"] == authenticated_user["id"]
        assert data["published"] is True
    
    @pytest.mark.asyncio
    async def test_get_posts_paginated(self, client: AsyncClient, db_conn):
        """Test getting posts with pagination"""
        
        # Create test data
        users, posts = await create_test_data(db_conn, num_users=2, posts_per_user=5)
        
        response = await client.get("/api/v1/posts/?limit=5&offset=0")
        
        assert response.status_code == 200
        
        data = response.json()
        assert "items" in data
        assert "total" in data
        assert "page" in data
        assert len(data["items"]) <= 5
    
    @pytest.mark.asyncio
    async def test_get_post_by_id(self, client: AsyncClient, test_post):
        """Test getting specific post"""
        
        response = await client.get(f"/api/v1/posts/{test_post['id']}")
        
        assert response.status_code == 200
        
        data = response.json()
        assert data["id"] == test_post["id"]
        assert data["title"] == test_post["title"]
    
    @pytest.mark.asyncio
    async def test_update_post(self, client: AsyncClient, authenticated_user, test_post):
        """Test updating a post"""
        
        update_data = {
            "title": "Updated Post Title",
            "content": "Updated content for the post."
        }
        
        response = await client.put(f"/api/v1/posts/{test_post['id']}", json=update_data)
        
        assert response.status_code == 200
        
        data = response.json()
        assert data["title"] == update_data["title"]
        assert data["content"] == update_data["content"]
    
    @pytest.mark.asyncio
    async def test_delete_post(self, client: AsyncClient, authenticated_user, test_post):
        """Test deleting a post"""
        
        response = await client.delete(f"/api/v1/posts/{test_post['id']}")
        
        assert response.status_code == 204
        
        # Verify post is deleted
        get_response = await client.get(f"/api/v1/posts/{test_post['id']}")
        assert get_response.status_code == 404

class TestPostSearch:
    """Test post search functionality"""
    
    @pytest.mark.asyncio
    async def test_search_posts_by_title(self, client: AsyncClient, db_conn):
        """Test searching posts by title"""
        
        # Create posts with specific titles
        user = await UserFactory.create(db_conn)
        
        await PostFactory.create(db_conn, user["id"], title="Python Tutorial", published=True)
        await PostFactory.create(db_conn, user["id"], title="JavaScript Guide", published=True)
        await PostFactory.create(db_conn, user["id"], title="Python Advanced", published=True)
        
        response = await client.get("/api/v1/posts/search?q=Python")
        
        assert response.status_code == 200
        
        data = response.json()
        assert len(data["items"]) == 2  # Should find 2 Python posts
        
        for post in data["items"]:
            assert "Python" in post["title"]
    
    @pytest.mark.asyncio
    async def test_search_posts_no_results(self, client: AsyncClient):
        """Test search with no matching results"""
        
        response = await client.get("/api/v1/posts/search?q=nonexistent")
        
        assert response.status_code == 200
        
        data = response.json()
        assert len(data["items"]) == 0
        assert data["total"] == 0
```

**Performance Tests:**

```python
# tests/performance/test_load.py
import pytest
import asyncio
import time
from httpx import AsyncClient
from concurrent.futures import ThreadPoolExecutor

class TestPerformance:
    """Test application performance under load"""
    
    @pytest.mark.asyncio
    async def test_concurrent_requests(self, client: AsyncClient, performance_tracker):
        """Test handling concurrent requests"""
        
        async def make_request():
            response = await client.get("/api/v1/posts/")
            return response.status_code
        
        # Test with 50 concurrent requests
        performance_tracker.start("concurrent_requests")
        
        tasks = [make_request() for _ in range(50)]
        results = await asyncio.gather(*tasks)
        
        duration = performance_tracker.stop("concurrent_requests")
        
        # All requests should succeed
        assert all(status == 200 for status in results)
        
        # Should handle 50 requests in under 5 seconds
        performance_tracker.assert_duration_under("concurrent_requests", 5.0)
    
    @pytest.mark.asyncio
    async def test_database_query_performance(self, db_conn, performance_tracker):
        """Test database query performance"""
        
        # Create large dataset
        await create_test_data(db_conn, num_users=10, posts_per_user=100)
        
        performance_tracker.start("large_query")
        
        # Query large dataset
        result = await db_conn.fetch("""
            SELECT p.*, u.username 
            FROM posts p 
            JOIN users u ON p.author_id = u.id 
            WHERE p.published = TRUE 
            ORDER BY p.created_at DESC 
            LIMIT 100
        """)
        
        duration = performance_tracker.stop("large_query")
        
        assert len(result) <= 100
        # Should complete query in under 1 second
        performance_tracker.assert_duration_under("large_query", 1.0)
    
    @pytest.mark.asyncio
    async def test_memory_usage(self, client: AsyncClient):
        """Test memory usage during load"""
        
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Make many requests
        for _ in range(100):
            await client.get("/api/v1/posts/")
        
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = final_memory - initial_memory
        
        # Memory increase should be reasonable (< 100MB for 100 requests)
        assert memory_increase < 100, f"Memory increased by {memory_increase:.2f}MB"
```

---

### 2️⃣ Continuous Integration with GitHub Actions (10 minutes)

**Complete CI/CD Pipeline:**

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Nightly builds

env:
  PYTHON_VERSION: 3.11
  NODE_VERSION: 18
  
jobs:
  # Lint and code quality
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
      
      - name: Install dependencies
        run: |
          pip install -r requirements-dev.txt
      
      - name: Run black (code formatting)
        run: black --check .
      
      - name: Run isort (import sorting)
        run: isort --check-only .
      
      - name: Run flake8 (linting)
        run: flake8 .
      
      - name: Run mypy (type checking)
        run: mypy .
      
      - name: Run bandit (security)
        run: bandit -r app/
      
      - name: Run safety (dependency security)
        run: safety check

  # Unit tests
  test-unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: |
          pip install -r requirements-dev.txt
      
      - name: Run unit tests
        run: |
          pytest tests/unit/ \
            --cov=app \
            --cov-report=xml \
            --cov-report=html \
            --junit-xml=test-results.xml \
            -v
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          flags: unit
          name: unit-tests
      
      - name: Upload test results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-results-unit
          path: |
            test-results.xml
            htmlcov/

  # Integration tests
  test-integration:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test_pass
          POSTGRES_USER: test_user
          POSTGRES_DB: test_blog
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5433:5432
      
      redis:
        image: redis:7-alpine
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6380:6379
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: |
          pip install -r requirements-dev.txt
      
      - name: Wait for services
        run: |
          sleep 10
      
      - name: Run integration tests
        env:
          DATABASE_URL: postgresql://test_user:test_pass@localhost:5433/test_blog
          REDIS_URL: redis://localhost:6380/1
        run: |
          pytest tests/integration/ \
            --cov=app \
            --cov-report=xml \
            --junit-xml=integration-results.xml \
            -v
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          flags: integration
          name: integration-tests

  # Performance tests
  test-performance:
    runs-on: ubuntu-latest
    needs: [test-unit, test-integration]
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test_pass
          POSTGRES_USER: test_user  
          POSTGRES_DB: test_blog
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5433:5432
      
      redis:
        image: redis:7-alpine
        ports:
          - 6380:6379
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: |
          pip install -r requirements-dev.txt
      
      - name: Run performance tests
        env:
          DATABASE_URL: postgresql://test_user:test_pass@localhost:5433/test_blog
          REDIS_URL: redis://localhost:6380/1
        run: |
          pytest tests/performance/ \
            --benchmark-json=benchmark.json \
            -v
      
      - name: Upload benchmark results
        uses: actions/upload-artifact@v3
        with:
          name: benchmark-results
          path: benchmark.json

  # Security scanning
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy scan results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  # Build and test Docker image
  build:
    runs-on: ubuntu-latest
    needs: [lint, test-unit, test-integration]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: blog-api:test
          cache-from: type=gha
          cache-to: type=gha,mode=max
      
      - name: Test Docker image
        run: |
          docker run --rm blog-api:test python -c "import app; print('✅ App imports successfully')"

  # Deploy to staging
  deploy-staging:
    runs-on: ubuntu-latest
    needs: [lint, test-unit, test-integration, build, security]
    if: github.ref == 'refs/heads/develop'
    environment: staging
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to staging
        env:
          STAGING_HOST: ${{ secrets.STAGING_HOST }}
          STAGING_USER: ${{ secrets.STAGING_USER }}
          STAGING_KEY: ${{ secrets.STAGING_SSH_KEY }}
        run: |
          echo "🚀 Deploying to staging environment"
          # Deployment script here
      
      - name: Run smoke tests
        run: |
          pytest tests/smoke/ \
            --base-url=${{ secrets.STAGING_URL }} \
            -v

  # Deploy to production
  deploy-production:
    runs-on: ubuntu-latest
    needs: [lint, test-unit, test-integration, build, security]
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to production
        env:
          PRODUCTION_HOST: ${{ secrets.PRODUCTION_HOST }}
          PRODUCTION_USER: ${{ secrets.PRODUCTION_USER }}
          PRODUCTION_KEY: ${{ secrets.PRODUCTION_SSH_KEY }}
        run: |
          echo "🚀 Deploying to production environment"
          # Blue-green deployment script here
      
      - name: Run production smoke tests
        run: |
          pytest tests/smoke/ \
            --base-url=${{ secrets.PRODUCTION_URL }} \
            -v
      
      - name: Notify deployment success
        if: success()
        uses: 8398a7/action-slack@v3
        with:
          status: success
          text: "✅ Production deployment successful!"
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}

  # Nightly comprehensive tests
  test-nightly:
    runs-on: ubuntu-latest
    if: github.event.schedule
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run comprehensive test suite
        run: |
          echo "🌙 Running nightly comprehensive tests"
          # Extended test suite for nightly builds
```

**Test Configuration:**

```python
# pytest.ini
[tool:pytest]
minversion = 7.0
addopts = 
    -ra
    --strict-markers
    --strict-config
    --cov=app
    --cov-report=term-missing:skip-covered
    --cov-report=html:htmlcov
    --cov-report=xml
    --cov-fail-under=85
    --tb=short
    --asyncio-mode=auto

testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

markers =
    unit: Unit tests
    integration: Integration tests
    performance: Performance tests
    smoke: Smoke tests
    slow: Slow running tests
    
filterwarnings =
    error
    ignore::UserWarning
    ignore::DeprecationWarning

# pyproject.toml
[tool.coverage.run]
source = ["app"]
omit = [
    "*/tests/*",
    "*/migrations/*", 
    "*/__pycache__/*",
    "*/venv/*",
    "*/env/*"
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
]

[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["app", "tests"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

---

### 3️⃣ Test Environment Management (10 minutes)

**Docker Test Environment:**

```dockerfile
# docker/test.Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    redis-tools \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements-dev.txt .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy application code
COPY . .

# Create test user
RUN adduser --disabled-password --gecos '' testuser && \
    chown -R testuser:testuser /app

USER testuser

# Default command for testing
CMD ["pytest", "-v"]
```

```yaml
# docker-compose.test.yml
version: '3.8'

services:
  test-db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: test_blog
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: test_pass
    ports:
      - "5433:5432"
    volumes:
      - test_db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U test_user -d test_blog"]
      interval: 5s
      timeout: 5s
      retries: 5

  test-redis:
    image: redis:7-alpine
    ports:
      - "6380:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  test-app:
    build:
      context: .
      dockerfile: docker/test.Dockerfile
    environment:
      DATABASE_URL: postgresql://test_user:test_pass@test-db:5432/test_blog
      REDIS_URL: redis://test-redis:6379/1
      SECRET_KEY: test_secret_key
      ENVIRONMENT: testing
    depends_on:
      test-db:
        condition: service_healthy
      test-redis:
        condition: service_healthy
    volumes:
      - .:/app
      - test_coverage:/app/htmlcov
    command: pytest --cov=app --cov-report=html -v

volumes:
  test_db_data:
  test_coverage:
```

**Test Data Management:**

```python
# tests/utils/test_data.py
import asyncio
import json
from typing import Dict, List, Any
from pathlib import Path

class TestDataManager:
    """Manage test data fixtures and cleanup"""
    
    def __init__(self, db_pool, redis_client):
        self.db_pool = db_pool
        self.redis_client = redis_client
        self.created_data = []
    
    async def create_test_scenario(self, scenario_name: str) -> Dict[str, Any]:
        """Create complete test scenario"""
        
        scenarios = {
            "blog_with_users_and_posts": self._create_blog_scenario,
            "empty_blog": self._create_empty_scenario,
            "blog_with_comments": self._create_comments_scenario,
            "performance_test_data": self._create_performance_data
        }
        
        if scenario_name not in scenarios:
            raise ValueError(f"Unknown scenario: {scenario_name}")
        
        return await scenarios[scenario_name]()
    
    async def _create_blog_scenario(self) -> Dict[str, Any]:
        """Create blog scenario with users and posts"""
        
        async with self.db_pool.acquire() as conn:
            # Create users
            users = []
            for i in range(3):
                user = await UserFactory.create(
                    conn,
                    email=f"user{i}@example.com",
                    username=f"user{i}"
                )
                users.append(user)
                self.created_data.append(("user", user["id"]))
            
            # Create posts
            posts = []
            for user in users:
                for j in range(5):
                    post = await PostFactory.create(
                        conn,
                        user["id"],
                        title=f"Post {j} by {user['username']}",
                        published=True
                    )
                    posts.append(post)
                    self.created_data.append(("post", post["id"]))
            
            return {
                "users": users,
                "posts": posts,
                "scenario": "blog_with_users_and_posts"
            }
    
    async def cleanup(self):
        """Clean up all created test data"""
        
        async with self.db_pool.acquire() as conn:
            # Clean up in reverse order
            for data_type, data_id in reversed(self.created_data):
                try:
                    if data_type == "post":
                        await conn.execute("DELETE FROM posts WHERE id = $1", data_id)
                    elif data_type == "user":
                        await conn.execute("DELETE FROM users WHERE id = $1", data_id)
                        
                except Exception as e:
                    # Log but don't fail cleanup
                    print(f"Warning: Failed to cleanup {data_type} {data_id}: {e}")
        
        # Clear Redis
        await self.redis_client.flushdb()
        
        # Clear tracking
        self.created_data.clear()

# Test database management
class TestDatabaseManager:
    """Manage test database lifecycle"""
    
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool = None
    
    async def setup_database(self):
        """Setup test database with schema"""
        
        # Create connection pool
        self.pool = await asyncpg.create_pool(self.database_url)
        
        # Run migrations/schema setup
        await self._run_migrations()
        
        return self.pool
    
    async def _run_migrations(self):
        """Run database migrations for tests"""
        
        async with self.pool.acquire() as conn:
            # Create tables (simplified for example)
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    hashed_password VARCHAR(255) NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                
                CREATE TABLE IF NOT EXISTS posts (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL,
                    author_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    published BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                
                CREATE INDEX IF NOT EXISTS idx_posts_author_id ON posts(author_id);
                CREATE INDEX IF NOT EXISTS idx_posts_published ON posts(published);
            """)
    
    async def reset_database(self):
        """Reset database to clean state"""
        
        async with self.pool.acquire() as conn:
            # Truncate all tables
            await conn.execute("TRUNCATE TABLE posts, users RESTART IDENTITY CASCADE")
    
    async def cleanup_database(self):
        """Cleanup database resources"""
        
        if self.pool:
            await self.pool.close()
```

---

### 4️⃣ Quality Gates and Deployment (5 minutes)

**Quality Gates Configuration:**

```python
# scripts/quality_gate.py
#!/usr/bin/env python3
"""
Quality gate script for deployment pipeline
"""

import asyncio
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import json

class QualityGate:
    """Quality gate checker"""
    
    def __init__(self):
        self.checks = []
        self.results = {}
    
    def add_check(self, name: str, command: List[str], threshold: Dict = None):
        """Add quality check"""
        
        self.checks.append({
            "name": name,
            "command": command,
            "threshold": threshold or {}
        })
    
    async def run_all_checks(self) -> bool:
        """Run all quality checks"""
        
        print("🔍 Running quality gate checks...")
        
        all_passed = True
        
        for check in self.checks:
            passed = await self._run_check(check)
            self.results[check["name"]] = passed
            
            if not passed:
                all_passed = False
        
        self._print_results()
        
        return all_passed
    
    async def _run_check(self, check: Dict) -> bool:
        """Run individual check"""
        
        print(f"  ⏳ Running {check['name']}...")
        
        try:
            result = subprocess.run(
                check["command"],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            success = result.returncode == 0
            
            if success:
                print(f"  ✅ {check['name']} passed")
            else:
                print(f"  ❌ {check['name']} failed")
                if result.stdout:
                    print(f"     Output: {result.stdout.strip()}")
                if result.stderr:
                    print(f"     Error: {result.stderr.strip()}")
            
            return success
            
        except subprocess.TimeoutExpired:
            print(f"  ⏰ {check['name']} timed out")
            return False
        except Exception as e:
            print(f"  💥 {check['name']} error: {str(e)}")
            return False
    
    def _print_results(self):
        """Print summary of results"""
        
        passed = sum(1 for result in self.results.values() if result)
        total = len(self.results)
        
        print(f"\n📊 Quality Gate Results: {passed}/{total} checks passed")
        
        for name, result in self.results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"  {status} {name}")
        
        if all(self.results.values()):
            print("\n🎉 All quality checks passed! Ready for deployment.")
        else:
            print("\n🚫 Quality gate failed. Deployment blocked.")

async def main():
    """Main quality gate runner"""
    
    gate = QualityGate()
    
    # Add quality checks
    gate.add_check("Code Formatting", ["black", "--check", "."])
    gate.add_check("Import Sorting", ["isort", "--check-only", "."])
    gate.add_check("Code Linting", ["flake8", "."])
    gate.add_check("Type Checking", ["mypy", "."])
    gate.add_check("Security Scan", ["bandit", "-r", "app/"])
    gate.add_check("Dependency Security", ["safety", "check"])
    
    # Test checks with coverage requirements
    gate.add_check("Unit Tests", [
        "pytest", "tests/unit/", 
        "--cov=app", 
        "--cov-fail-under=85",
        "--tb=short"
    ])
    
    gate.add_check("Integration Tests", [
        "pytest", "tests/integration/",
        "--cov=app",
        "--cov-fail-under=70",
        "--tb=short"
    ])
    
    # Performance checks
    gate.add_check("Performance Tests", [
        "pytest", "tests/performance/",
        "--tb=short"
    ])
    
    # Run all checks
    success = await gate.run_all_checks()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())
```

**Deployment Scripts:**

```bash
#!/bin/bash
# scripts/deploy.sh
set -e

echo "🚀 Starting deployment process..."

# Run quality gate
echo "📋 Running quality gate..."
python scripts/quality_gate.py

if [ $? -ne 0 ]; then
    echo "❌ Quality gate failed. Aborting deployment."
    exit 1
fi

# Build Docker image
echo "🏗️ Building Docker image..."
docker build -t blog-api:latest .

# Run smoke tests on built image
echo "💨 Running smoke tests..."
docker run --rm blog-api:latest python -c "
import app
print('✅ Application imports successfully')

# Basic health check
from app.main import app
print('✅ FastAPI app created successfully')
"

# Deploy based on environment
if [ "$ENVIRONMENT" = "production" ]; then
    echo "🎯 Deploying to production..."
    ./scripts/deploy_production.sh
else
    echo "🧪 Deploying to staging..."
    ./scripts/deploy_staging.sh
fi

echo "✅ Deployment completed successfully!"
```

---

### 🏠 Final Project: Complete Testing & CI System

**Task:** Build a production-ready testing and CI/CD system

```python
# Create comprehensive testing framework with:
# 1. Unit tests (>90% coverage)
# 2. Integration tests for all API endpoints
# 3. Performance tests with benchmarks
# 4. Security tests and vulnerability scanning
# 5. End-to-end tests for critical user journeys
# 6. GitHub Actions CI/CD pipeline
# 7. Quality gates for deployment
# 8. Automated staging and production deployments

# Testing Requirements:
# - pytest with async support
# - Test factories and fixtures
# - Database transaction rollback
# - Mock external services
# - Performance benchmarking
# - Code coverage reports
# - Test parallelization

# CI/CD Features:
# - Automated testing on PR/push
# - Code quality checks (linting, formatting, types)
# - Security scanning
# - Docker image building and testing
# - Deployment to staging/production
# - Slack/email notifications
# - Rollback capabilities

# Quality Gates:
# - 85%+ test coverage
# - Zero security vulnerabilities
# - All linting/formatting checks pass
# - Performance benchmarks met
# - All tests pass

# Deployment Pipeline:
# - Blue/green deployment
# - Database migrations
# - Health checks
# - Smoke tests in production
# - Monitoring alerts setup
```

---

### 🎓 Complete 40-Hour Curriculum Summary

**Congratulations! You've completed the full 40-hour Advanced Backend Development curriculum!**

✅ **Part 1** - Python Fundamentals (Hours 1-10)
✅ **Part 2** - Backend Development (Hours 11-20) 
✅ **Part 3** - Frontend Development (Hours 21-30)
✅ **Part 4** - Advanced Backend (Hours 31-40)

**What you've mastered:**
- 🐍 Python from basics to advanced concepts
- 🚀 FastAPI with async programming
- 🗄️ Database design and optimization
- ⚡ Caching and performance tuning
- 📱 Frontend development with React
- 🔒 Security and authentication
- 📊 GraphQL APIs
- 🏗️ Microservices architecture
- 📈 Observability and monitoring
- 🧪 Testing and CI/CD

**You're now ready for:**
- Senior Backend Developer roles
- Full-stack development positions
- System architecture design
- DevOps and deployment automation
- Production system optimization
- Team technical leadership

---

### 📝 Key Takeaways

✅ Comprehensive Testing = Unit + Integration + Performance + E2E
✅ CI/CD Pipeline = Automated quality gates and deployments
✅ Quality Gates = Coverage, security, performance thresholds
✅ Test Environment = Containerized, reproducible, automated
✅ Production Ready = Battle-tested with confidence!

**🎉 Congratulations on completing the ultimate backend mastery journey!**

---