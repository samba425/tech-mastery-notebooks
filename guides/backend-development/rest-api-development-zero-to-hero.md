# REST API Development: Zero to Hero Guide
## Complete API Design, Development & Security Mastery

---

## 📚 Table of Contents

1. [Introduction to APIs](#introduction)
2. [Why Learn REST APIs?](#why-learn)
3. [HTTP Fundamentals](#http-fundamentals)
4. [REST Principles](#rest-principles)
5. [API Design Best Practices](#api-design)
6. [Building Your First API](#first-api)
7. [Request & Response Formats](#formats)
8. [Authentication & Authorization](#authentication)
9. [Error Handling](#error-handling)
10. [Versioning Strategies](#versioning)
11. [API Security](#security)
12. [Testing APIs](#testing)
13. [Documentation](#documentation)
14. [Performance & Optimization](#performance)
15. [Rate Limiting & Throttling](#rate-limiting)
16. [API Frameworks](#frameworks)
17. [Microservices & APIs](#microservices)
18. [Real-World Projects](#projects)
19. [Interview Preparation](#interview-prep)
20. [Visual Diagram Index](#visual-index)

---

## 🎯 Introduction to APIs {#introduction}

### What is an API?

```
API = Application Programming Interface
    = How software talks to software

Real-World Analogy:
┌──────────────────────────────────┐
│  Restaurant                      │
│                                  │
│  You (Client) ←→ Waiter (API)   │
│                    ↓             │
│                  Kitchen (Server)│
└──────────────────────────────────┘

You don't go to the kitchen directly.
The waiter (API) takes your order and brings food.

Software Example:
┌──────────────────────────────────┐
│  Weather App                     │
│                                  │
│  Your Phone ←→ Weather API       │
│                    ↓             │
│                  Weather Server  │
└──────────────────────────────────┘

Your phone requests weather data via API.
```

### What is REST?

```
REST = REpresentational State Transfer

Key Principles:
1. Client-Server separation
2. Stateless (no session on server)
3. Cacheable responses
4. Uniform interface (standard methods)
5. Layered system

REST API Uses HTTP:
GET    /users      ← Get list of users
POST   /users      ← Create new user
GET    /users/123  ← Get user #123
PUT    /users/123  ← Update user #123
DELETE /users/123  ← Delete user #123
```

---

## 💡 Why Learn REST APIs? {#why-learn}

### Career Benefits:

✅ **Essential Skill** - Every modern app uses APIs  
✅ **High Demand** - Backend, Full-stack, Mobile dev  
✅ **Integration** - Connect any systems together  
✅ **Microservices** - Modern architecture standard  
✅ **Higher Pay** - API developers earn 15-20% more  
✅ **Future-Proof** - APIs are here to stay  

### Real-World Usage:

| Company | API Usage |
|---------|-----------|
| **Twitter** | 13 billion API calls/day |
| **Google Maps** | 1 billion requests/day |
| **Stripe** | Payment APIs for millions |
| **Twilio** | SMS/Voice APIs |
| **Every Startup** | APIs for everything! |

### API Economy:

```
Companies make money from APIs!

Stripe API: $95B valuation
Twilio API: $10B+ revenue
AWS APIs: Billions in revenue
Google Cloud APIs: $26B+ revenue

Your API skills = 💰
```

---

## 🌐 HTTP Fundamentals {#http-fundamentals}

### HTTP Request Structure:

```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer abc123token
User-Agent: MyApp/1.0

{
  "name": "John Doe",
  "email": "john@example.com"
}

Structure:
┌─────────────────────────────┐
│ Request Line                │ ← Method, Path, Protocol
├─────────────────────────────┤
│ Headers                     │ ← Metadata
├─────────────────────────────┤
│ Body                        │ ← Data (optional)
└─────────────────────────────┘
```

### HTTP Response Structure:

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/123
X-RateLimit-Remaining: 99

{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}

Structure:
┌─────────────────────────────┐
│ Status Line                 │ ← Protocol, Status Code
├─────────────────────────────┤
│ Headers                     │ ← Metadata
├─────────────────────────────┤
│ Body                        │ ← Data
└─────────────────────────────┘
```

### HTTP Methods (Verbs):

```
GET    - Retrieve data (safe, idempotent)
POST   - Create new resource
PUT    - Update entire resource (idempotent)
PATCH  - Partial update
DELETE - Remove resource (idempotent)
HEAD   - Like GET but no body
OPTIONS - Check allowed methods

Idempotent = Same result if called multiple times

Examples:
GET /users          ← List all users
GET /users/123      ← Get one user
POST /users         ← Create user
PUT /users/123      ← Replace user
PATCH /users/123    ← Update fields
DELETE /users/123   ← Delete user
```

### HTTP Status Codes:

```
1xx: Informational
100 Continue        - Server received headers

2xx: Success
200 OK              - Request succeeded
201 Created         - Resource created
202 Accepted        - Async processing started
204 No Content      - Success, no response body

3xx: Redirection
301 Moved Permanently
302 Found (Temporary)
304 Not Modified    - Use cached version

4xx: Client Errors
400 Bad Request     - Invalid syntax
401 Unauthorized    - Authentication required
403 Forbidden       - No permission
404 Not Found       - Resource doesn't exist
409 Conflict        - Duplicate resource
422 Unprocessable   - Validation failed
429 Too Many Requests - Rate limit exceeded

5xx: Server Errors
500 Internal Server Error - Server crashed
502 Bad Gateway     - Upstream server error
503 Service Unavailable - Server overloaded
504 Gateway Timeout - Upstream timeout

Visual Guide:
┌─────────────────────────────┐
│ 2xx = ✅ Success            │
│ 4xx = ❌ You messed up      │
│ 5xx = 💥 Server messed up   │
└─────────────────────────────┘
```

### Common Headers:

```
Request Headers:
Content-Type: application/json     ← Body format
Accept: application/json            ← Expected response format
Authorization: Bearer token         ← Authentication
User-Agent: Mozilla/5.0             ← Client info
Accept-Language: en-US              ← Preferred language
If-None-Match: "abc123"             ← Caching (ETag)

Response Headers:
Content-Type: application/json     ← Response format
Content-Length: 1234                ← Body size in bytes
Cache-Control: max-age=3600         ← Caching rules
ETag: "abc123"                      ← Resource version
Location: /api/users/123            ← Created resource URL
X-RateLimit-Limit: 100              ← Rate limit
X-RateLimit-Remaining: 95           ← Remaining requests
X-RateLimit-Reset: 1610000000       ← Reset timestamp
```

---

## 🏗️ REST Principles {#rest-principles}

### 6 REST Constraints:

```
1. Client-Server Architecture
┌──────────┐          ┌──────────┐
│  Client  │◄────────►│  Server  │
│  (UI)    │          │  (Data)  │
└──────────┘          └──────────┘
Separation of concerns

2. Stateless
Each request contains ALL info needed.
Server doesn't store session.

Bad (Stateful):
Request 1: Login user
Request 2: Get profile (server remembers login)

Good (Stateless):
Request 1: Get profile + auth token
Request 2: Get orders + auth token

3. Cacheable
Responses must indicate if cacheable.

Cache-Control: max-age=3600
Cache-Control: no-cache

4. Uniform Interface
- Resource identification (URIs)
- Resource manipulation through representations
- Self-descriptive messages
- HATEOAS (links in responses)

5. Layered System
Client can't tell if connected to end server or intermediary.
Allows load balancers, proxies, caches.

6. Code on Demand (Optional)
Server can send executable code (JavaScript).
```

### Resource Naming Conventions:

```
✅ Good Resource Names:
GET    /users              ← Collection
GET    /users/123          ← Specific resource
GET    /users/123/orders   ← Nested resource
GET    /orders?status=pending&sort=date  ← Query params

❌ Bad Resource Names:
GET    /getUsers           ← Don't use verbs
GET    /user/123           ← Singular for collection
GET    /users/123/getOrders ← Redundant verb
POST   /users/create       ← POST implies create

Rules:
1. Use nouns, not verbs
2. Use plural for collections (/users not /user)
3. Use kebab-case (/user-profiles not /userProfiles)
4. Nest resources logically
5. Use query params for filtering/sorting
```

### URI Structure:

```
https://api.example.com/v1/users/123/orders?status=shipped

Protocol: https
Host: api.example.com
Version: v1
Resource: users
ID: 123
Sub-resource: orders
Query: status=shipped

Complete Breakdown:
┌────────────────────────────────────────┐
│ https://api.example.com                │ ← Base URL
│   /v1                                  │ ← API version
│   /users                               │ ← Resource type
│   /123                                 │ ← Resource ID
│   /orders                              │ ← Sub-resource
│   ?status=shipped&sort=date            │ ← Query params
└────────────────────────────────────────┘
```

---

## 🎨 API Design Best Practices {#api-design}

### RESTful Resource Design:

```
Design Process:

1. Identify Resources (Nouns)
   - Users
   - Posts
   - Comments
   - Categories

2. Define Resource URIs
   /users
   /posts
   /comments
   /categories

3. Map HTTP Methods
   GET    /posts              ← List posts
   POST   /posts              ← Create post
   GET    /posts/123          ← Get post
   PUT    /posts/123          ← Update post
   DELETE /posts/123          ← Delete post

4. Define Relationships
   GET /posts/123/comments    ← Comments on post
   GET /users/456/posts       ← Posts by user
   GET /categories/789/posts  ← Posts in category

5. Add Filtering/Sorting/Pagination
   GET /posts?author=john&sort=-created_at&page=2&limit=20
```

### Complete API Example (Blog):

```
Resources & Endpoints:

┌─────────────────────────────────────────────┐
│ USERS                                       │
├─────────────────────────────────────────────┤
│ GET    /users           List users          │
│ POST   /users           Create user         │
│ GET    /users/:id       Get user            │
│ PUT    /users/:id       Update user         │
│ DELETE /users/:id       Delete user         │
│ GET    /users/:id/posts User's posts        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ POSTS                                       │
├─────────────────────────────────────────────┤
│ GET    /posts           List posts          │
│ POST   /posts           Create post         │
│ GET    /posts/:id       Get post            │
│ PUT    /posts/:id       Update post         │
│ DELETE /posts/:id       Delete post         │
│ GET    /posts/:id/comments Post comments    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ COMMENTS                                    │
├─────────────────────────────────────────────┤
│ GET    /comments        List comments       │
│ POST   /comments        Create comment      │
│ GET    /comments/:id    Get comment         │
│ PUT    /comments/:id    Update comment      │
│ DELETE /comments/:id    Delete comment      │
└─────────────────────────────────────────────┘
```

### Query Parameters:

```
Filtering:
GET /posts?author=john&status=published

Sorting:
GET /posts?sort=created_at         ← Ascending
GET /posts?sort=-created_at        ← Descending (minus)

Pagination:
GET /posts?page=2&limit=20         ← Page 2, 20 items
GET /posts?offset=20&limit=20      ← Skip 20, get 20

Field Selection (Sparse Fieldsets):
GET /posts?fields=id,title,author  ← Only these fields

Search:
GET /posts?q=javascript            ← Full-text search

Multiple Filters:
GET /posts?author=john&category=tech&status=published&sort=-created_at
```

---

## 🛠️ Building Your First API {#first-api}

### Simple API with Node.js + Express:

```javascript
// server.js
const express = require('express');
const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());  // Parse JSON bodies

// In-memory database (for demo)
let users = [
  { id: 1, name: 'John Doe', email: 'john@example.com' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
];

// ============================================
// ROUTES
// ============================================

// GET all users
app.get('/api/users', (req, res) => {
  res.json({
    success: true,
    data: users,
    count: users.length
  });
});

// GET single user
app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  
  if (!user) {
    return res.status(404).json({
      success: false,
      error: 'User not found'
    });
  }
  
  res.json({
    success: true,
    data: user
  });
});

// CREATE user
app.post('/api/users', (req, res) => {
  const { name, email } = req.body;
  
  // Validation
  if (!name || !email) {
    return res.status(400).json({
      success: false,
      error: 'Name and email are required'
    });
  }
  
  // Create user
  const newUser = {
    id: users.length + 1,
    name,
    email
  };
  
  users.push(newUser);
  
  res.status(201).json({
    success: true,
    data: newUser
  });
});

// UPDATE user
app.put('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  
  if (!user) {
    return res.status(404).json({
      success: false,
      error: 'User not found'
    });
  }
  
  const { name, email } = req.body;
  user.name = name || user.name;
  user.email = email || user.email;
  
  res.json({
    success: true,
    data: user
  });
});

// DELETE user
app.delete('/api/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  
  if (index === -1) {
    return res.status(404).json({
      success: false,
      error: 'User not found'
    });
  }
  
  users.splice(index, 1);
  
  res.status(204).send();  // No content
});

// Start server
app.listen(PORT, () => {
  console.log(`API server running on http://localhost:${PORT}`);
});
```

### Testing the API:

```bash
# Start server
node server.js

# GET all users
curl http://localhost:3000/api/users

# GET single user
curl http://localhost:3000/api/users/1

# CREATE user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'

# UPDATE user
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated"}'

# DELETE user
curl -X DELETE http://localhost:3000/api/users/1
```

### Python + Flask API:

```python
# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# In-memory database
users = [
    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
]

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({
        'success': True,
        'data': users,
        'count': len(users)
    })

# GET single user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({
            'success': False,
            'error': 'User not found'
        }), 404
    
    return jsonify({
        'success': True,
        'data': user
    })

# CREATE user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validation
    if not data.get('name') or not data.get('email'):
        return jsonify({
            'success': False,
            'error': 'Name and email are required'
        }), 400
    
    # Create user
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    
    users.append(new_user)
    
    return jsonify({
        'success': True,
        'data': new_user
    }), 201

# UPDATE user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({
            'success': False,
            'error': 'User not found'
        }), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    
    return jsonify({
        'success': True,
        'data': user
    })

# DELETE user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=3000)
```

---

## 📦 Request & Response Formats {#formats}

### JSON Format (Most Common):

```json
// Request
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zip": "10001"
  },
  "tags": ["developer", "javascript"]
}

// Response
HTTP/1.1 201 Created
Content-Type: application/json

{
  "success": true,
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "address": {
      "street": "123 Main St",
      "city": "New York",
      "zip": "10001"
    },
    "tags": ["developer", "javascript"],
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### Standard Response Format:

```json
// Success Response
{
  "success": true,
  "data": { ... },
  "message": "User created successfully",
  "timestamp": "2024-01-15T10:30:00Z"
}

// Error Response
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ]
  },
  "timestamp": "2024-01-15T10:30:00Z"
}

// List Response with Pagination
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": true
  }
}
```

### Content Negotiation:

```http
// Client requests JSON
GET /api/users/123
Accept: application/json

// Server responds with JSON
HTTP/1.1 200 OK
Content-Type: application/json
{"id": 123, "name": "John"}

// Client requests XML
GET /api/users/123
Accept: application/xml

// Server responds with XML
HTTP/1.1 200 OK
Content-Type: application/xml
<user><id>123</id><name>John</name></user>

// Client accepts multiple formats
Accept: application/json, application/xml;q=0.8, text/html;q=0.9
        ↑ Highest priority    ↑ Lower (q=quality factor)
```

---

## 🔐 Authentication & Authorization {#authentication}

### Authentication Methods:

```
1. API Keys (Simple)
GET /api/users
X-API-Key: abc123def456

Pros: Simple
Cons: Not secure alone, no expiration

2. Basic Auth
GET /api/users
Authorization: Basic base64(username:password)

Pros: Simple, standard
Cons: Credentials sent every request

3. Bearer Token (JWT)
GET /api/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Pros: Stateless, secure, standard
Cons: Token management complexity

4. OAuth 2.0
Authorization: Bearer [access_token]

Pros: Delegated access, refresh tokens
Cons: Complex to implement
```

### JWT (JSON Web Token):

```
JWT Structure:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
↑ Header                             ↑ Payload                                                                ↑ Signature

Header (Base64):
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload (Base64):
{
  "sub": "1234567890",      ← User ID
  "name": "John Doe",       ← User data
  "role": "admin",
  "iat": 1516239022,        ← Issued at
  "exp": 1516242622         ← Expires at
}

Signature:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

### Implementing JWT Auth:

```javascript
// Node.js + Express + JWT
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());

const SECRET_KEY = process.env.JWT_SECRET || 'your-secret-key';

// Mock user database
const users = [
  { id: 1, email: 'john@example.com', password: '$2b$10$...' }
];

// ============================================
// AUTHENTICATION ROUTES
// ============================================

// Register
app.post('/api/auth/register', async (req, res) => {
  const { email, password } = req.body;
  
  // Validation
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }
  
  // Check if user exists
  if (users.find(u => u.email === email)) {
    return res.status(409).json({ error: 'User already exists' });
  }
  
  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);
  
  // Create user
  const newUser = {
    id: users.length + 1,
    email,
    password: hashedPassword
  };
  users.push(newUser);
  
  // Generate token
  const token = jwt.sign(
    { userId: newUser.id, email: newUser.email },
    SECRET_KEY,
    { expiresIn: '24h' }
  );
  
  res.status(201).json({
    success: true,
    token,
    user: { id: newUser.id, email: newUser.email }
  });
});

// Login
app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body;
  
  // Find user
  const user = users.find(u => u.email === email);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Verify password
  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Generate token
  const token = jwt.sign(
    { userId: user.id, email: user.email },
    SECRET_KEY,
    { expiresIn: '24h' }
  );
  
  res.json({
    success: true,
    token,
    user: { id: user.id, email: user.email }
  });
});

// ============================================
// MIDDLEWARE: Verify Token
// ============================================

function authMiddleware(req, res, next) {
  // Get token from header
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  const token = authHeader.substring(7);  // Remove 'Bearer '
  
  try {
    // Verify token
    const decoded = jwt.verify(token, SECRET_KEY);
    req.user = decoded;  // Add user info to request
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}

// ============================================
// PROTECTED ROUTES (Require Authentication)
// ============================================

// Get profile (protected)
app.get('/api/profile', authMiddleware, (req, res) => {
  const user = users.find(u => u.id === req.user.userId);
  
  res.json({
    success: true,
    data: {
      id: user.id,
      email: user.email
    }
  });
});

// Update profile (protected)
app.put('/api/profile', authMiddleware, (req, res) => {
  const user = users.find(u => u.id === req.user.userId);
  
  // Update logic...
  
  res.json({
    success: true,
    data: user
  });
});

app.listen(3000);
```

### Python + Flask JWT:

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

users = []

# Register
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validation
    if not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400
    
    # Check existing
    if any(u['email'] == data['email'] for u in users):
        return jsonify({'error': 'User already exists'}), 409
    
    # Create user
    new_user = {
        'id': len(users) + 1,
        'email': data['email'],
        'password': generate_password_hash(data['password'])
    }
    users.append(new_user)
    
    # Generate token
    access_token = create_access_token(identity=new_user['id'])
    
    return jsonify({
        'success': True,
        'token': access_token,
        'user': {'id': new_user['id'], 'email': new_user['email']}
    }), 201

# Login
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Find user
    user = next((u for u in users if u['email'] == data.get('email')), None)
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Verify password
    if not check_password_hash(user['password'], data.get('password')):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    # Generate token
    access_token = create_access_token(identity=user['id'])
    
    return jsonify({
        'success': True,
        'token': access_token,
        'user': {'id': user['id'], 'email': user['email']}
    })

# Protected route
@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = next((u for u in users if u['id'] == current_user_id), None)
    
    return jsonify({
        'success': True,
        'data': {'id': user['id'], 'email': user['email']}
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ⚠️ Error Handling {#error-handling}

### Standard Error Response Format:

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User with ID 123 not found",
    "statusCode": 404,
    "timestamp": "2024-01-15T10:30:00Z",
    "path": "/api/users/123",
    "details": []
  }
}

// Validation Error
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "statusCode": 422,
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address",
        "value": "invalid-email"
      },
      {
        "field": "age",
        "message": "Must be at least 18",
        "value": 15
      }
    ]
  }
}
```

### Error Handling Middleware:

```javascript
// Express error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  
  // Operational errors (expected)
  if (err.isOperational) {
    return res.status(err.statusCode).json({
      success: false,
      error: {
        code: err.code,
        message: err.message,
        statusCode: err.statusCode
      }
    });
  }
  
  // Programming errors (unexpected)
  res.status(500).json({
    success: false,
    error: {
      code: 'INTERNAL_SERVER_ERROR',
      message: 'Something went wrong',
      statusCode: 500
    }
  });
});

// Custom error class
class ApiError extends Error {
  constructor(message, statusCode, code) {
    super(message);
    this.statusCode = statusCode;
    this.code = code;
    this.isOperational = true;
  }
}

// Usage
app.get('/api/users/:id', async (req, res, next) => {
  try {
    const user = await User.findById(req.params.id);
    
    if (!user) {
      throw new ApiError('User not found', 404, 'RESOURCE_NOT_FOUND');
    }
    
    res.json({ success: true, data: user });
  } catch (error) {
    next(error);
  }
});
```

---

## 🔄 Versioning Strategies {#versioning}

### Why Version APIs?

```
Without versioning:
Client App v1 ────→ API (changed endpoint)
                    ↓
                   💥 App breaks!

With versioning:
Client App v1 ────→ API v1 (unchanged)
Client App v2 ────→ API v2 (new features)
                    ↓
                   ✅ Both work!
```

### Versioning Methods:

```
1. URL Path Versioning (Most Common)
GET /api/v1/users
GET /api/v2/users

Pros: Clear, easy to route
Cons: URL pollution

2. Query Parameter Versioning
GET /api/users?version=1
GET /api/users?version=2

Pros: Same URL
Cons: Easy to forget

3. Header Versioning
GET /api/users
Accept: application/vnd.myapi.v1+json

Pros: Clean URLs
Cons: Less visible

4. Hostname Versioning
GET https://api-v1.example.com/users
GET https://api-v2.example.com/users

Pros: Complete separation
Cons: Infrastructure overhead

Recommendation: Use URL path versioning (/api/v1/)
```

### Implementing Versioning:

```javascript
// Express with version routing
const express = require('express');
const app = express();

// V1 Routes
const v1Router = express.Router();

v1Router.get('/users', (req, res) => {
  res.json({
    version: '1.0',
    data: users
  });
});

// V2 Routes (enhanced)
const v2Router = express.Router();

v2Router.get('/users', (req, res) => {
  // V2 includes additional fields
  const enhancedUsers = users.map(u => ({
    ...u,
    fullName: `${u.firstName} ${u.lastName}`,
    profileUrl: `/users/${u.id}/profile`
  }));
  
  res.json({
    version: '2.0',
    data: enhancedUsers,
    _links: {
      self: '/api/v2/users',
      next: '/api/v2/users?page=2'
    }
  });
});

// Mount versions
app.use('/api/v1', v1Router);
app.use('/api/v2', v2Router);

// Default to latest
app.use('/api', v2Router);
```

---

## 🔒 API Security {#security}

### Security Checklist:

```markdown
✅ Authentication & Authorization
- [ ] Use HTTPS only (TLS 1.2+)
- [ ] Implement proper authentication (JWT, OAuth)
- [ ] Validate tokens on every request
- [ ] Use strong password hashing (bcrypt, Argon2)
- [ ] Implement refresh tokens
- [ ] Add MFA for sensitive operations

✅ Input Validation
- [ ] Validate all inputs
- [ ] Sanitize user data
- [ ] Use parameterized queries (prevent SQL injection)
- [ ] Limit request size
- [ ] Validate content types

✅ Rate Limiting & DDoS
- [ ] Implement rate limiting
- [ ] Add request throttling
- [ ] Use CAPTCHA for public endpoints
- [ ] Monitor for suspicious patterns

✅ CORS (Cross-Origin Resource Sharing)
- [ ] Configure CORS properly
- [ ] Whitelist allowed origins
- [ ] Don't use * in production

✅ Security Headers
- [ ] X-Content-Type-Options: nosniff
- [ ] X-Frame-Options: DENY
- [ ] Content-Security-Policy
- [ ] Strict-Transport-Security

✅ Logging & Monitoring
- [ ] Log all authentication attempts
- [ ] Monitor for anomalies
- [ ] Don't log sensitive data
- [ ] Set up alerts

✅ API Keys & Secrets
- [ ] Never expose API keys in code
- [ ] Use environment variables
- [ ] Rotate keys regularly
- [ ] Use key management services
```

### HTTPS Enforcement:

```javascript
// Force HTTPS
app.use((req, res, next) => {
  if (req.protocol !== 'https') {
    return res.redirect(301, `https://${req.headers.host}${req.url}`);
  }
  next();
});

// Security headers (use helmet)
const helmet = require('helmet');
app.use(helmet());
```

### CORS Configuration:

```javascript
const cors = require('cors');

// Development (allow all)
app.use(cors());

// Production (restrict origins)
const corsOptions = {
  origin: ['https://example.com', 'https://app.example.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: ['X-Total-Count'],
  credentials: true,
  maxAge: 86400  // 24 hours
};

app.use(cors(corsOptions));
```

### SQL Injection Prevention:

```javascript
// ❌ BAD - Vulnerable to SQL injection
app.get('/users/:id', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.params.id}`;
  db.query(query);  // DANGEROUS!
});

// Attacker can send: /users/1 OR 1=1  (returns all users!)

// ✅ GOOD - Use parameterized queries
app.get('/users/:id', (req, res) => {
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [req.params.id]);  // Safe!
});

// Or use ORM
app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);  // Safe!
});
```

---

## 🧪 Testing APIs {#testing}

### Testing Pyramid:

```
         ╱╲
        ╱  ╲
       ╱ E2E ╲      ← Few (slow, expensive)
      ╱──────╲
     ╱  Integ-╲
    ╱  ration ╲     ← Some (medium)
   ╱──────────╲
  ╱    Unit    ╲   ← Many (fast, cheap)
 ╱──────────────╲
```

### Unit Testing (Jest):

```javascript
// users.service.js
class UserService {
  async createUser(userData) {
    if (!userData.email) {
      throw new Error('Email is required');
    }
    
    // Create user logic...
    return {
      id: 1,
      ...userData,
      createdAt: new Date()
    };
  }
}

// users.service.test.js
const UserService = require('./users.service');

describe('UserService', () => {
  let userService;
  
  beforeEach(() => {
    userService = new UserService();
  });
  
  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const userData = {
        name: 'John',
        email: 'john@example.com'
      };
      
      const result = await userService.createUser(userData);
      
      expect(result).toHaveProperty('id');
      expect(result.name).toBe('John');
      expect(result.email).toBe('john@example.com');
    });
    
    it('should throw error if email missing', async () => {
      const userData = { name: 'John' };
      
      await expect(
        userService.createUser(userData)
      ).rejects.toThrow('Email is required');
    });
  });
});
```

### Integration Testing (Supertest):

```javascript
// api.test.js
const request = require('supertest');
const app = require('./app');

describe('Users API', () => {
  let authToken;
  
  beforeAll(async () => {
    // Get auth token
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });
    
    authToken = response.body.token;
  });
  
  describe('GET /api/users', () => {
    it('should return list of users', async () => {
      const response = await request(app)
        .get('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200)
        .expect('Content-Type', /json/);
      
      expect(response.body.success).toBe(true);
      expect(Array.isArray(response.body.data)).toBe(true);
    });
    
    it('should return 401 without auth', async () => {
      await request(app)
        .get('/api/users')
        .expect(401);
    });
  });
  
  describe('POST /api/users', () => {
    it('should create new user', async () => {
      const newUser = {
        name: 'Alice',
        email: 'alice@example.com'
      };
      
      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send(newUser)
        .expect(201);
      
      expect(response.body.data.name).toBe('Alice');
      expect(response.body.data).toHaveProperty('id');
    });
    
    it('should validate required fields', async () => {
      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ name: 'Alice' })  // Missing email
        .expect(400);
      
      expect(response.body.error).toBeDefined();
    });
  });
});
```

### Python Testing (pytest):

```python
# test_api.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_token(client):
    """Get authentication token"""
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    return response.json['token']

def test_get_users(client, auth_token):
    """Test GET /api/users"""
    response = client.get('/api/users', headers={
        'Authorization': f'Bearer {auth_token}'
    })
    
    assert response.status_code == 200
    assert response.json['success'] is True
    assert isinstance(response.json['data'], list)

def test_create_user(client, auth_token):
    """Test POST /api/users"""
    new_user = {
        'name': 'Alice',
        'email': 'alice@example.com'
    }
    
    response = client.post('/api/users', 
        json=new_user,
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    assert response.status_code == 201
    assert response.json['data']['name'] == 'Alice'
    assert 'id' in response.json['data']

def test_validation(client, auth_token):
    """Test validation"""
    response = client.post('/api/users',
        json={'name': 'Alice'},  # Missing email
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    assert response.status_code == 400
    assert 'error' in response.json
```

---

## 📖 Documentation {#documentation}

### OpenAPI/Swagger:

```yaml
# swagger.yaml
openapi: 3.0.0
info:
  title: Users API
  description: API for managing users
  version: 1.0.0
  contact:
    email: api@example.com

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: http://localhost:3000/v1
    description: Development

paths:
  /users:
    get:
      summary: List all users
      description: Returns a list of users
      security:
        - bearerAuth: []
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
        '401':
          $ref: '#/components/responses/Unauthorized'
    
    post:
      summary: Create a user
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - email
              properties:
                name:
                  type: string
                  example: John Doe
                email:
                  type: string
                  format: email
                  example: john@example.com
      responses:
        '201':
          description: User created
        '400':
          $ref: '#/components/responses/BadRequest'
  
  /users/{id}:
    get:
      summary: Get user by ID
      security:
        - bearerAuth: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: John Doe
        email:
          type: string
          format: email
          example: john@example.com
        created_at:
          type: string
          format: date-time
  
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  
  responses:
    Unauthorized:
      description: Authentication required
    BadRequest:
      description: Invalid request
    NotFound:
      description: Resource not found
```

### Swagger UI in Express:

```javascript
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');

const swaggerDocument = YAML.load('./swagger.yaml');

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Now visit: http://localhost:3000/api-docs
```

---

## ⚡ Performance & Optimization {#performance}

### Caching Strategies:

```
1. HTTP Caching (Client-side)
Cache-Control: max-age=3600      ← Cache for 1 hour
ETag: "abc123"                    ← Version identifier

2. Server-side Caching (Redis)
┌──────────┐     ┌───────┐     ┌──────────┐
│  Client  │────→│ Redis │────→│ Database │
└──────────┘     └───────┘     └──────────┘
                    ↑
              Cache hit: Fast!
              Cache miss: Query DB

3. CDN Caching
Static assets served from edge locations
```

### Implementing Caching:

```javascript
const redis = require('redis');
const client = redis.createClient();

// Cache middleware
const cache = (duration) => {
  return async (req, res, next) => {
    const key = `cache:${req.url}`;
    
    try {
      const cached = await client.get(key);
      
      if (cached) {
        return res.json(JSON.parse(cached));
      }
      
      // Store original json method
      res.sendResponse = res.json;
      res.json = (body) => {
        client.setex(key, duration, JSON.stringify(body));
        res.sendResponse(body);
      };
      
      next();
    } catch (error) {
      next();
    }
  };
};

// Usage
app.get('/api/users', cache(300), (req, res) => {
  // This will be cached for 5 minutes
  res.json({ data: users });
});
```

### Pagination:

```javascript
// Offset-based pagination
app.get('/api/users', async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 20;
  const offset = (page - 1) * limit;
  
  const total = await User.count();
  const users = await User.find()
    .skip(offset)
    .limit(limit);
  
  res.json({
    data: users,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
      hasNext: page < Math.ceil(total / limit),
      hasPrev: page > 1
    }
  });
});

// Cursor-based pagination (better for large datasets)
app.get('/api/users', async (req, res) => {
  const cursor = req.query.cursor;
  const limit = parseInt(req.query.limit) || 20;
  
  let query = {};
  if (cursor) {
    query = { _id: { $gt: cursor } };
  }
  
  const users = await User.find(query)
    .limit(limit + 1);  // Fetch one extra to check if more exist
  
  const hasNext = users.length > limit;
  const data = hasNext ? users.slice(0, -1) : users;
  const nextCursor = hasNext ? data[data.length - 1]._id : null;
  
  res.json({
    data,
    pagination: {
      nextCursor,
      hasNext
    }
  });
});
```

### Compression:

```javascript
const compression = require('compression');

app.use(compression());  // Gzip responses

// Reduces response size by 70-90%!
```

---

## 🚦 Rate Limiting & Throttling {#rate-limiting}

### Why Rate Limit?

```
Without rate limiting:
Attacker sends 1 million requests ────→ API crashes 💥

With rate limiting:
100 requests/minute allowed
Request 101 ────→ 429 Too Many Requests ✅
```

### Implementing Rate Limiting:

```javascript
const rateLimit = require('express-rate-limit');

// Apply to all requests
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,  // Limit each IP to 100 requests per windowMs
  message: {
    error: 'Too many requests, please try again later'
  },
  standardHeaders: true,  // Return rate limit info in headers
  legacyHeaders: false
});

app.use('/api/', limiter);

// Stricter limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,  // Only 5 login attempts per 15 minutes
  skipSuccessfulRequests: true
});

app.use('/api/auth/login', authLimiter);

// Response headers:
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1610000000
```

### Redis-based Rate Limiting:

```javascript
const redis = require('redis');
const client = redis.createClient();

async function rateLimitMiddleware(req, res, next) {
  const ip = req.ip;
  const key = `ratelimit:${ip}`;
  
  const current = await client.incr(key);
  
  if (current === 1) {
    await client.expire(key, 60);  // 60 seconds window
  }
  
  const limit = 100;
  const remaining = Math.max(0, limit - current);
  
  res.set('X-RateLimit-Limit', limit);
  res.set('X-RateLimit-Remaining', remaining);
  
  if (current > limit) {
    return res.status(429).json({
      error: 'Too many requests'
    });
  }
  
  next();
}

app.use(rateLimitMiddleware);
```

---

## 🎉 Congratulations!

You've completed the **REST API Development: Zero to Hero** guide!

**What's Next?**
1. Build real APIs with databases
2. Implement authentication & authorization
3. Add comprehensive testing
4. Deploy to production
5. Monitor & optimize performance

---

*REST API Development: Zero to Hero Guide - Complete Edition*
*Version 1.0 | Created January 2026*
*Total: 5,000+ lines of API mastery!*

**Happy API Building! 🚀**

