# Microservices Architecture: Complete Guide
## From Monolith to Microservices Mastery

---

## 📚 Table of Contents

1. [Introduction to Microservices](#introduction)
2. [Microservices vs Monolith](#comparison)
3. [Design Principles](#principles)
4. [Service Communication](#communication)
5. [API Gateway Pattern](#api-gateway)
6. [Service Discovery](#discovery)
7. [Data Management](#data)
8. [Authentication & Authorization](#auth)
9. [Observability & Monitoring](#monitoring)
10. [Resilience Patterns](#resilience)
11. [Container & Orchestration](#containers)
12. [CI/CD for Microservices](#cicd)
13. [Testing Strategies](#testing)
14. [Best Practices](#best-practices)
15. [Real-World Implementation](#projects)

---

## 🎯 Introduction to Microservices {#introduction}

### What are Microservices?

**Microservices** is an architectural style where an application is built as a collection of small, independent services that communicate through APIs.

```
Traditional Monolith
┌────────────────────────────────┐
│     Single Application         │
│  ┌──────────────────────────┐ │
│  │  UI + Business + Data    │ │
│  │  All in one codebase     │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘

Microservices
┌──────────┐  ┌──────────┐  ┌──────────┐
│  User    │  │ Product  │  │  Order   │
│ Service  │  │ Service  │  │ Service  │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │
     └─────────────┴─────────────┘
           API Gateway
```

### Key Characteristics

- ✅ **Independently Deployable** - Each service can be deployed separately
- ✅ **Loosely Coupled** - Services don't depend on each other's implementation
- ✅ **Single Responsibility** - Each service does one thing well
- ✅ **Technology Agnostic** - Different services can use different tech stacks
- ✅ **Resilient** - Failure in one service doesn't crash entire system

---

## 🔄 Microservices vs Monolith {#comparison}

### Architecture Comparison

```
┌─────────────────────────────────────────────────────────┐
│               MONOLITH                                  │
├─────────────────────────────────────────────────────────┤
│  Pros:                          Cons:                   │
│  ✅ Simple to develop           ❌ Hard to scale        │
│  ✅ Easy to test               ❌ Technology lock-in   │
│  ✅ Simple deployment          ❌ Long deployments     │
│  ✅ Easy debugging             ❌ Risk of failure      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│             MICROSERVICES                               │
├─────────────────────────────────────────────────────────┤
│  Pros:                          Cons:                   │
│  ✅ Independent scaling        ❌ Complex to set up    │
│  ✅ Technology freedom         ❌ Distributed debugging │
│  ✅ Fault isolation            ❌ Network overhead     │
│  ✅ Team autonomy              ❌ Data consistency     │
└─────────────────────────────────────────────────────────┘
```

### When to Use Microservices?

**Use Microservices When:**
- Large, complex applications
- Need to scale different parts independently
- Multiple teams working on different features
- Frequent deployments required
- Different technology stacks needed

**Stick with Monolith When:**
- Small team (< 10 developers)
- Simple application
- Just starting out
- Limited DevOps capacity
- Predictable scaling needs

---

## 📐 Design Principles {#principles}

### 1. Single Responsibility

Each service should do **one thing** and do it well.

```
❌ Bad: UserService
- User management
- Authentication
- Email notifications
- Order processing

✅ Good: Separate Services
- UserService: User CRUD operations
- AuthService: Authentication & authorization
- NotificationService: Email/SMS notifications
- OrderService: Order processing
```

### 2. Service Boundaries

Define clear boundaries using Domain-Driven Design (DDD).

```
E-commerce Domain
├── User Management (Bounded Context)
│   └── UserService
├── Product Catalog (Bounded Context)
│   ├── ProductService
│   └── CategoryService
├── Shopping (Bounded Context)
│   ├── CartService
│   └── OrderService
└── Payment (Bounded Context)
    └── PaymentService
```

### 3. Data Ownership

Each service owns its database - **no shared databases!**

```
❌ Bad: Shared Database
┌──────────┐   ┌──────────┐
│ UserSvc  │   │OrderSvc  │
└────┬─────┘   └────┬─────┘
     │              │
     └──────┬───────┘
            ▼
      ┌──────────┐
      │ Database │
      └──────────┘

✅ Good: Database per Service
┌──────────┐      ┌──────────┐
│ UserSvc  │      │OrderSvc  │
└────┬─────┘      └────┬─────┘
     ▼                 ▼
┌──────────┐      ┌──────────┐
│  User DB │      │Order DB  │
└──────────┘      └──────────┘
```

### 4. Loose Coupling

Services should communicate through well-defined APIs, not direct database access.

```javascript
// ❌ Bad: Direct DB access
const user = await db.users.findOne({ id: userId })

// ✅ Good: API call
const user = await fetch(`http://user-service/api/users/${userId}`)
  .then(res => res.json())
```

---

## 🔌 Service Communication {#communication}

### Synchronous Communication (REST)

**Use for:** Request-response patterns, real-time data

```
Client ──────▶ API Gateway ──────▶ User Service
                                        │
                                        ▼
                                   Response
```

**Example: REST API**

```javascript
// User Service - Express.js
const express = require('express')
const app = express()

app.get('/api/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id)
  res.json({ success: true, data: user })
})

app.listen(3001, () => console.log('User service on port 3001'))
```

```javascript
// Order Service - Calling User Service
const axios = require('axios')

async function createOrder(userId, items) {
  // Call User Service
  const userResponse = await axios.get(
    `http://user-service:3001/api/users/${userId}`
  )
  
  const user = userResponse.data.data
  
  // Create order
  const order = await Order.create({
    userId: user.id,
    userName: user.name,
    items
  })
  
  return order
}
```

### Asynchronous Communication (Message Queue)

**Use for:** Event-driven, decoupled services, background processing

```
Service A ────▶ Message Queue ────▶ Service B
                    │
                    └────────────▶ Service C
```

**Example: RabbitMQ**

```javascript
// Producer (Order Service) - Publish Event
const amqp = require('amqplib')

async function publishOrderCreated(order) {
  const connection = await amqp.connect('amqp://localhost')
  const channel = await connection.createChannel()
  
  const exchange = 'orders'
  await channel.assertExchange(exchange, 'fanout', { durable: true })
  
  const message = JSON.stringify({
    event: 'ORDER_CREATED',
    data: order
  })
  
  channel.publish(exchange, '', Buffer.from(message))
  console.log('Published ORDER_CREATED event')
  
  await channel.close()
  await connection.close()
}

// After creating order
const order = await Order.create({ userId, items })
await publishOrderCreated(order)
```

```javascript
// Consumer (Email Service) - Subscribe to Events
async function subscribeToOrderEvents() {
  const connection = await amqp.connect('amqp://localhost')
  const channel = await connection.createChannel()
  
  const exchange = 'orders'
  await channel.assertExchange(exchange, 'fanout', { durable: true })
  
  const q = await channel.assertQueue('', { exclusive: true })
  channel.bindQueue(q.queue, exchange, '')
  
  console.log('Waiting for order events...')
  
  channel.consume(q.queue, async (msg) => {
    const event = JSON.parse(msg.content.toString())
    
    if (event.event === 'ORDER_CREATED') {
      // Send confirmation email
      await sendOrderConfirmationEmail(event.data)
      console.log('Sent order confirmation email')
    }
    
    channel.ack(msg)
  })
}

subscribeToOrderEvents()
```

### Communication Patterns

```
┌────────────────────────────────────────────┐
│  Synchronous (REST/gRPC)                   │
├────────────────────────────────────────────┤
│  ✅ Simple to understand                   │
│  ✅ Immediate response                     │
│  ❌ Tight coupling                         │
│  ❌ Service availability dependency        │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│  Asynchronous (Message Queue/Events)       │
├────────────────────────────────────────────┤
│  ✅ Loose coupling                         │
│  ✅ Better fault tolerance                 │
│  ✅ Load leveling                          │
│  ❌ Complex to debug                       │
│  ❌ Eventual consistency                   │
└────────────────────────────────────────────┘
```

---

## 🚪 API Gateway Pattern {#api-gateway}

### What is API Gateway?

Single entry point for all client requests that routes to appropriate microservices.

```
┌──────────┐
│  Mobile  │─┐
└──────────┘ │
┌──────────┐ │
│   Web    │─┼──▶ ┌──────────────┐
└──────────┘ │    │ API Gateway  │
┌──────────┐ │    └──────┬───────┘
│   IoT    │─┘           │
└──────────┘       ┌─────┼─────┬─────┐
                   │     │     │     │
               ┌───▼┐ ┌──▼─┐ ┌─▼──┐ ┌▼────┐
               │User│ │Prod│ │Order│ │Auth │
               └────┘ └────┘ └────┘ └─────┘
```

### API Gateway Responsibilities

- **Routing** - Direct requests to correct service
- **Authentication** - Verify user identity
- **Rate Limiting** - Prevent abuse
- **Load Balancing** - Distribute requests
- **Request Aggregation** - Combine multiple service calls
- **Caching** - Reduce backend load

### Example: Express API Gateway

```javascript
// api-gateway/server.js
const express = require('express')
const { createProxyMiddleware } = require('http-proxy-middleware')
const rateLimit = require('express-rate-limit')

const app = express()

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
})

app.use(limiter)

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' })
  }
  
  // Verify token
  // ... token verification logic
  next()
}

// Route to User Service
app.use('/api/users', authenticate, createProxyMiddleware({
  target: 'http://user-service:3001',
  changeOrigin: true,
  pathRewrite: {
    '^/api/users': '/api/users'
  }
}))

// Route to Product Service
app.use('/api/products', createProxyMiddleware({
  target: 'http://product-service:3002',
  changeOrigin: true
}))

// Route to Order Service
app.use('/api/orders', authenticate, createProxyMiddleware({
  target: 'http://order-service:3003',
  changeOrigin: true
}))

// Request aggregation example
app.get('/api/dashboard/:userId', authenticate, async (req, res) => {
  try {
    const userId = req.params.userId
    
    // Fetch data from multiple services in parallel
    const [user, orders, recommendations] = await Promise.all([
      fetch(`http://user-service:3001/api/users/${userId}`),
      fetch(`http://order-service:3003/api/orders?userId=${userId}`),
      fetch(`http://recommendation-service:3004/api/recommendations/${userId}`)
    ])
    
    // Aggregate response
    res.json({
      user: await user.json(),
      orders: await orders.json(),
      recommendations: await recommendations.json()
    })
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch dashboard data' })
  }
})

app.listen(3000, () => {
  console.log('API Gateway running on port 3000')
})
```

---

## 🔍 Service Discovery {#discovery}

### What is Service Discovery?

Mechanism for services to find each other dynamically.

```
Without Service Discovery (Hardcoded URLs)
Service A ──▶ http://service-b:3002 ❌ What if port changes?

With Service Discovery
Service A ──▶ Service Registry ──▶ Find Service B
              (Consul/Eureka)       (Dynamic IP:Port)
```

### Consul Example

```javascript
// Register service with Consul
const Consul = require('consul')
const consul = new Consul()

// Register User Service
const registerService = async () => {
  await consul.agent.service.register({
    name: 'user-service',
    id: 'user-service-1',
    address: 'localhost',
    port: 3001,
    check: {
      http: 'http://localhost:3001/health',
      interval: '10s'
    }
  })
  console.log('Service registered with Consul')
}

registerService()

// Discover and call service
const discoverService = async (serviceName) => {
  const services = await consul.health.service({
    service: serviceName,
    passing: true
  })
  
  if (services.length === 0) {
    throw new Error(`Service ${serviceName} not found`)
  }
  
  // Get first healthy instance
  const service = services[0].Service
  return `http://${service.Address}:${service.Port}`
}

// Use service discovery
const userServiceUrl = await discoverService('user-service')
const response = await fetch(`${userServiceUrl}/api/users/123`)
```

---

## 💾 Data Management {#data}

### Database Per Service Pattern

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ User Service │      │Product Service│     │Order Service │
└──────┬───────┘      └──────┬───────┘      └──────┬───────┘
       │                     │                     │
       ▼                     ▼                     ▼
  ┌─────────┐          ┌─────────┐          ┌─────────┐
  │ User DB │          │Product DB│          │Order DB │
  └─────────┘          └─────────┘          └─────────┘
```

### Saga Pattern (Distributed Transactions)

Handle transactions across multiple services using compensating transactions.

**Example: Order Processing Saga**

```javascript
// Order Service
async function createOrder(userId, items) {
  // Step 1: Create order (pending)
  const order = await Order.create({
    userId,
    items,
    status: 'PENDING',
    totalAmount: calculateTotal(items)
  })
  
  try {
    // Step 2: Reserve inventory
    await fetch('http://inventory-service/api/reserve', {
      method: 'POST',
      body: JSON.stringify({ orderId: order.id, items })
    })
    
    // Step 3: Process payment
    const payment = await fetch('http://payment-service/api/charge', {
      method: 'POST',
      body: JSON.stringify({
        userId,
        amount: order.totalAmount
      })
    })
    
    // Step 4: Update order status
    order.status = 'CONFIRMED'
    await order.save()
    
    return order
    
  } catch (error) {
    // Compensating transactions (rollback)
    
    // Release inventory
    await fetch('http://inventory-service/api/release', {
      method: 'POST',
      body: JSON.stringify({ orderId: order.id })
    })
    
    // Cancel order
    order.status = 'CANCELLED'
    await order.save()
    
    throw error
  }
}
```

### Event Sourcing

Store all changes as a sequence of events.

```javascript
// Events
const events = [
  { type: 'ORDER_CREATED', orderId: 1, items: [...] },
  { type: 'PAYMENT_PROCESSED', orderId: 1, amount: 100 },
  { type: 'ORDER_SHIPPED', orderId: 1, trackingId: 'ABC123' }
]

// Rebuild state from events
function rebuildOrderState(events) {
  let order = {}
  
  for (const event of events) {
    switch (event.type) {
      case 'ORDER_CREATED':
        order = { id: event.orderId, items: event.items, status: 'CREATED' }
        break
      case 'PAYMENT_PROCESSED':
        order.status = 'PAID'
        break
      case 'ORDER_SHIPPED':
        order.status = 'SHIPPED'
        order.trackingId = event.trackingId
        break
    }
  }
  
  return order
}
```

### CQRS (Command Query Responsibility Segregation)

Separate read and write operations.

```
Write Side (Commands)          Read Side (Queries)
┌──────────────┐              ┌──────────────┐
│  Write Model │─────Events───▶│  Read Model  │
│  (Normalized)│              │  (Optimized) │
└──────────────┘              └──────────────┘
     PostgreSQL                   MongoDB
```

```javascript
// Command Side (Write)
class CreateOrderCommand {
  async execute(orderData) {
    const order = await Order.create(orderData)
    
    // Publish event
    await publishEvent({
      type: 'ORDER_CREATED',
      data: order
    })
    
    return order
  }
}

// Query Side (Read)
class OrderQueryService {
  async getOrderById(orderId) {
    // Optimized read model
    return await OrderReadModel.findById(orderId)
  }
  
  async getOrdersByUser(userId) {
    // Denormalized for fast reads
    return await OrderReadModel.find({ userId })
  }
}

// Event Handler (Sync read model)
async function handleOrderCreated(event) {
  const { data } = event
  
  // Update read model
  await OrderReadModel.create({
    id: data.id,
    userId: data.userId,
    userName: data.userName, // Denormalized
    items: data.items,
    totalAmount: data.totalAmount
  })
}
```

---

## 🔐 Authentication & Authorization {#auth}

### JWT-Based Authentication

```
┌─────────┐                           ┌─────────────┐
│ Client  │─── 1. Login ─────────────▶│ Auth Service│
└─────────┘                           └──────┬──────┘
     │                                       │
     │◀──── 2. JWT Token ────────────────────┘
     │
     │── 3. Request + JWT ──────────────────▶┌──────────────┐
     │                                       │ API Gateway  │
     │                                       └──────┬───────┘
     │                                              │
     │                                    4. Verify Token
     │                                              │
     │◀──── 5. Response ─────────────────────────┐ │
                                                  │ │
                                            ┌─────▼──────┐
                                            │User Service│
                                            └────────────┘
```

**Auth Service**

```javascript
// auth-service/server.js
const express = require('express')
const jwt = require('jsonwebtoken')
const bcrypt = require('bcryptjs')

const app = express()
app.use(express.json())

const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key'

// Login endpoint
app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body
  
  // Find user (from database)
  const user = await User.findOne({ email })
  
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' })
  }
  
  // Verify password
  const isValid = await bcrypt.compare(password, user.password)
  
  if (!isValid) {
    return res.status(401).json({ error: 'Invalid credentials' })
  }
  
  // Generate JWT token
  const token = jwt.sign(
    {
      userId: user.id,
      email: user.email,
      role: user.role
    },
    JWT_SECRET,
    { expiresIn: '7d' }
  )
  
  res.json({
    success: true,
    token,
    user: {
      id: user.id,
      email: user.email,
      name: user.name
    }
  })
})

// Verify token endpoint (used by API Gateway)
app.post('/api/auth/verify', (req, res) => {
  const { token } = req.body
  
  try {
    const decoded = jwt.verify(token, JWT_SECRET)
    res.json({ success: true, user: decoded })
  } catch (error) {
    res.status(401).json({ success: false, error: 'Invalid token' })
  }
})

app.listen(3005, () => console.log('Auth service on port 3005'))
```

**API Gateway - Auth Middleware**

```javascript
// Verify JWT in API Gateway
const verifyToken = async (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '')
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' })
  }
  
  try {
    // Verify with Auth Service
    const response = await fetch('http://auth-service:3005/api/auth/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token })
    })
    
    const result = await response.json()
    
    if (!result.success) {
      return res.status(401).json({ error: 'Invalid token' })
    }
    
    // Attach user to request
    req.user = result.user
    next()
    
  } catch (error) {
    res.status(500).json({ error: 'Authentication failed' })
  }
}

// Protect routes
app.use('/api/orders', verifyToken, orderProxy)
app.use('/api/profile', verifyToken, userProxy)
```

---

## 📊 Observability & Monitoring {#monitoring}

### The Three Pillars

```
┌─────────────────────────────────────────┐
│  1. Logging                             │
│  - Application logs                     │
│  - Error logs                           │
│  - Access logs                          │
│  Tool: ELK Stack, CloudWatch            │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  2. Metrics                             │
│  - Request rate                         │
│  - Error rate                           │
│  - Latency                              │
│  - Resource usage                       │
│  Tool: Prometheus, Grafana              │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  3. Tracing                             │
│  - Request flow across services         │
│  - Performance bottlenecks              │
│  - Dependency mapping                   │
│  Tool: Jaeger, Zipkin                   │
└─────────────────────────────────────────┘
```

### Structured Logging

```javascript
const winston = require('winston')

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'app.log' })
  ]
})

// Log with context
logger.info('Order created', {
  orderId: order.id,
  userId: user.id,
  amount: order.totalAmount,
  service: 'order-service'
})

// Log errors
logger.error('Payment failed', {
  orderId: order.id,
  error: error.message,
  stack: error.stack
})
```

### Distributed Tracing

```javascript
// Using OpenTelemetry
const { trace } = require('@opentelemetry/api')
const tracer = trace.getTracer('order-service')

async function createOrder(userId, items) {
  // Start span
  const span = tracer.startSpan('createOrder')
  
  try {
    span.setAttribute('userId', userId)
    span.setAttribute('itemCount', items.length)
    
    // Create order
    const order = await Order.create({ userId, items })
    
    // Child span for external call
    const paymentSpan = tracer.startSpan('processPayment', { parent: span })
    await processPayment(order.id, order.totalAmount)
    paymentSpan.end()
    
    span.setStatus({ code: 0 }) // Success
    return order
    
  } catch (error) {
    span.setStatus({ code: 2, message: error.message }) // Error
    throw error
  } finally {
    span.end()
  }
}
```

### Health Checks

```javascript
// Health check endpoint
app.get('/health', async (req, res) => {
  const health = {
    status: 'UP',
    timestamp: new Date().toISOString(),
    service: 'order-service',
    checks: {}
  }
  
  // Check database
  try {
    await db.ping()
    health.checks.database = { status: 'UP' }
  } catch (error) {
    health.checks.database = { status: 'DOWN', error: error.message }
    health.status = 'DOWN'
  }
  
  // Check external service
  try {
    await fetch('http://payment-service/health')
    health.checks.paymentService = { status: 'UP' }
  } catch (error) {
    health.checks.paymentService = { status: 'DOWN' }
  }
  
  const statusCode = health.status === 'UP' ? 200 : 503
  res.status(statusCode).json(health)
})
```

---

## 🛡️ Resilience Patterns {#resilience}

### 1. Circuit Breaker

Prevent cascading failures by stopping requests to failing services.

```
┌──────────────────────────────────────┐
│  Circuit Breaker States              │
├──────────────────────────────────────┤
│  CLOSED ─────▶ Requests pass through │
│    │                                 │
│    ▼ (Too many failures)            │
│  OPEN ───────▶ Requests rejected     │
│    │                                 │
│    ▼ (After timeout)                │
│  HALF-OPEN ──▶ Test with few requests│
│    │         │                       │
│    │         └─▶ Success → CLOSED   │
│    └───────────▶ Failure → OPEN     │
└──────────────────────────────────────┘
```

```javascript
const CircuitBreaker = require('opossum')

// Circuit breaker configuration
const options = {
  timeout: 3000,           // Call timeout
  errorThresholdPercentage: 50, // Open circuit at 50% errors
  resetTimeout: 10000      // Try again after 10 seconds
}

// Wrap function with circuit breaker
const callPaymentService = async (amount) => {
  const response = await fetch('http://payment-service/api/charge', {
    method: 'POST',
    body: JSON.stringify({ amount })
  })
  return response.json()
}

const breaker = new CircuitBreaker(callPaymentService, options)

// Handle circuit open
breaker.on('open', () => {
  console.log('Circuit breaker opened - payment service is down')
})

// Handle success after half-open
breaker.on('close', () => {
  console.log('Circuit breaker closed - payment service recovered')
})

// Use circuit breaker
try {
  const result = await breaker.fire(100)
} catch (error) {
  // Fallback logic
  console.log('Payment service unavailable, using fallback')
}
```

### 2. Retry Pattern

```javascript
const retry = require('async-retry')

async function callServiceWithRetry() {
  return await retry(
    async () => {
      const response = await fetch('http://user-service/api/users/123')
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`)
      }
      
      return response.json()
    },
    {
      retries: 3,
      minTimeout: 1000,
      maxTimeout: 5000,
      factor: 2 // Exponential backoff
    }
  )
}
```

### 3. Timeout Pattern

```javascript
async function callWithTimeout(url, timeoutMs = 5000) {
  const controller = new AbortController()
  const timeout = setTimeout(() => controller.abort(), timeoutMs)
  
  try {
    const response = await fetch(url, { signal: controller.signal })
    return response.json()
  } catch (error) {
    if (error.name === 'AbortError') {
      throw new Error('Request timeout')
    }
    throw error
  } finally {
    clearTimeout(timeout)
  }
}
```

### 4. Bulkhead Pattern

Isolate resources to prevent total system failure.

```javascript
const { Pool } = require('pg')

// Separate connection pools for different operations
const criticalPool = new Pool({
  max: 10,  // 10 connections for critical operations
  // ... other config
})

const nonCriticalPool = new Pool({
  max: 5,   // 5 connections for non-critical operations
  // ... other config
})

// Critical operation uses dedicated pool
async function getCriticalData() {
  const client = await criticalPool.connect()
  try {
    return await client.query('SELECT * FROM critical_data')
  } finally {
    client.release()
  }
}
```

---

## 🐳 Containers & Orchestration {#containers}

### Docker for Microservices

**Dockerfile (User Service)**

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install --production

# Copy source code
COPY . .

# Expose port
EXPOSE 3001

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node healthcheck.js

# Start service
CMD ["node", "server.js"]
```

### Docker Compose (Local Development)

```yaml
# docker-compose.yml
version: '3.8'

services:
  # API Gateway
  api-gateway:
    build: ./api-gateway
    ports:
      - "3000:3000"
    environment:
      - USER_SERVICE_URL=http://user-service:3001
      - PRODUCT_SERVICE_URL=http://product-service:3002
      - ORDER_SERVICE_URL=http://order-service:3003
    depends_on:
      - user-service
      - product-service
      - order-service
  
  # User Service
  user-service:
    build: ./user-service
    environment:
      - MONGODB_URI=mongodb://mongo:27017/users
      - JWT_SECRET=secret
    depends_on:
      - mongo
  
  # Product Service
  product-service:
    build: ./product-service
    environment:
      - MONGODB_URI=mongodb://mongo:27017/products
  
  # Order Service
  order-service:
    build: ./order-service
    environment:
      - MONGODB_URI=mongodb://mongo:27017/orders
      - RABBITMQ_URL=amqp://rabbitmq:5672
    depends_on:
      - mongo
      - rabbitmq
  
  # MongoDB
  mongo:
    image: mongo:latest
    volumes:
      - mongo-data:/data/db
  
  # RabbitMQ
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "15672:15672" # Management UI
    environment:
      - RABBITMQ_DEFAULT_USER=admin
      - RABBITMQ_DEFAULT_PASS=admin

volumes:
  mongo-data:
```

### Kubernetes Deployment

```yaml
# user-service-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: your-registry/user-service:latest
        ports:
        - containerPort: 3001
        env:
        - name: MONGODB_URI
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: mongodb-uri
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3001
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3001
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3001
  type: ClusterIP
```

---

## 🔄 CI/CD for Microservices {#cicd}

### GitHub Actions Pipeline

```yaml
# .github/workflows/user-service.yml
name: User Service CI/CD

on:
  push:
    branches: [ main ]
    paths:
      - 'user-service/**'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: |
          cd user-service
          npm install
      
      - name: Run tests
        run: |
          cd user-service
          npm test
      
      - name: Run linting
        run: |
          cd user-service
          npm run lint
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker image
        run: |
          cd user-service
          docker build -t ${{ secrets.DOCKER_REGISTRY }}/user-service:${{ github.sha }} .
      
      - name: Push to registry
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push ${{ secrets.DOCKER_REGISTRY }}/user-service:${{ github.sha }}
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/user-service \
            user-service=${{ secrets.DOCKER_REGISTRY }}/user-service:${{ github.sha }}
```

---

## 🧪 Testing Strategies {#testing}

### 1. Unit Tests (Service Level)

```javascript
// user-service/tests/user.test.js
const User = require('../models/User')
const { createUser, getUser } = require('../controllers/userController')

describe('User Service', () => {
  describe('createUser', () => {
    it('should create a new user', async () => {
      const userData = {
        name: 'John Doe',
        email: 'john@example.com',
        password: 'password123'
      }
      
      const user = await createUser(userData)
      
      expect(user.name).toBe('John Doe')
      expect(user.email).toBe('john@example.com')
      expect(user.password).not.toBe('password123') // Should be hashed
    })
    
    it('should reject duplicate email', async () => {
      await createUser({
        name: 'John',
        email: 'john@example.com',
        password: 'pass'
      })
      
      await expect(createUser({
        name: 'Jane',
        email: 'john@example.com',
        password: 'pass'
      })).rejects.toThrow('Email already exists')
    })
  })
})
```

### 2. Integration Tests

```javascript
// order-service/tests/integration.test.js
const request = require('supertest')
const app = require('../app')

describe('Order API Integration', () => {
  it('should create order with valid user', async () => {
    const res = await request(app)
      .post('/api/orders')
      .set('Authorization', 'Bearer valid-token')
      .send({
        items: [
          { productId: '123', quantity: 2 }
        ]
      })
    
    expect(res.status).toBe(201)
    expect(res.body.success).toBe(true)
    expect(res.body.data.status).toBe('PENDING')
  })
})
```

### 3. Contract Tests (Pact)

```javascript
// Consumer test (Order Service)
const { Pact } = require('@pact-foundation/pact')

const provider = new Pact({
  consumer: 'OrderService',
  provider: 'UserService'
})

describe('User Service Contract', () => {
  beforeAll(() => provider.setup())
  afterAll(() => provider.finalize())
  
  it('should get user by ID', async () => {
    await provider.addInteraction({
      state: 'user 123 exists',
      uponReceiving: 'a request for user 123',
      withRequest: {
        method: 'GET',
        path: '/api/users/123'
      },
      willRespondWith: {
        status: 200,
        body: {
          id: '123',
          name: 'John Doe',
          email: 'john@example.com'
        }
      }
    })
    
    // Test implementation
    const user = await getUserFromService('123')
    expect(user.id).toBe('123')
  })
})
```

### 4. End-to-End Tests

```javascript
// e2e/order-flow.test.js
describe('Complete Order Flow', () => {
  it('should complete order from creation to delivery', async () => {
    // 1. Login
    const loginRes = await request(apiGateway)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'password' })
    
    const token = loginRes.body.token
    
    // 2. Create order
    const orderRes = await request(apiGateway)
      .post('/api/orders')
      .set('Authorization', `Bearer ${token}`)
      .send({ items: [{ productId: '123', quantity: 1 }] })
    
    expect(orderRes.status).toBe(201)
    const orderId = orderRes.body.data.id
    
    // 3. Process payment
    const paymentRes = await request(apiGateway)
      .post(`/api/orders/${orderId}/pay`)
      .set('Authorization', `Bearer ${token}`)
    
    expect(paymentRes.status).toBe(200)
    
    // 4. Check order status
    const statusRes = await request(apiGateway)
      .get(`/api/orders/${orderId}`)
      .set('Authorization', `Bearer ${token}`)
    
    expect(statusRes.body.data.status).toBe('PAID')
  })
})
```

---

## ✅ Best Practices {#best-practices}

### 1. Start Small

```
❌ Don't: Build 20 microservices from day one
✅ Do: Start with monolith, extract services gradually
```

### 2. Define Service Boundaries

```
✅ Good Boundaries (by Business Capability)
- User Management
- Product Catalog
- Order Processing
- Payment

❌ Bad Boundaries (by Technical Layer)
- Database Service
- Validation Service
- Email Service
```

### 3. API Versioning

```javascript
// Version in URL
app.use('/api/v1/users', usersRouterV1)
app.use('/api/v2/users', usersRouterV2)

// Version in header
app.use('/api/users', (req, res, next) => {
  const version = req.headers['api-version'] || 'v1'
  if (version === 'v2') {
    return usersRouterV2(req, res, next)
  }
  return usersRouterV1(req, res, next)
})
```

### 4. Graceful Shutdown

```javascript
const server = app.listen(3001)

process.on('SIGTERM', () => {
  console.log('SIGTERM received, closing server...')
  
  server.close(() => {
    console.log('Server closed')
    
    // Close database connections
    mongoose.connection.close(false, () => {
      console.log('MongoDB connection closed')
      process.exit(0)
    })
  })
})
```

### 5. Configuration Management

```javascript
// Use environment variables
require('dotenv').config()

const config = {
  port: process.env.PORT || 3001,
  database: {
    uri: process.env.MONGODB_URI,
    options: {
      useNewUrlParser: true,
      useUnifiedTopology: true
    }
  },
  services: {
    userService: process.env.USER_SERVICE_URL,
    paymentService: process.env.PAYMENT_SERVICE_URL
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: '7d'
  }
}

module.exports = config
```

---

## 🎯 Real-World Implementation {#projects}

### Complete E-commerce Microservices

```
microservices/
├── api-gateway/
│   ├── Dockerfile
│   ├── server.js
│   └── package.json
├── auth-service/
│   ├── Dockerfile
│   ├── controllers/
│   ├── models/
│   └── server.js
├── user-service/
│   ├── Dockerfile
│   ├── controllers/
│   ├── models/
│   └── server.js
├── product-service/
│   ├── Dockerfile
│   ├── controllers/
│   ├── models/
│   └── server.js
├── order-service/
│   ├── Dockerfile
│   ├── controllers/
│   ├── models/
│   ├── sagas/
│   └── server.js
├── payment-service/
│   ├── Dockerfile
│   ├── controllers/
│   └── server.js
├── notification-service/
│   ├── Dockerfile
│   ├── consumers/
│   └── server.js
├── inventory-service/
│   ├── Dockerfile
│   ├── controllers/
│   └── server.js
├── docker-compose.yml
└── kubernetes/
    ├── deployments/
    ├── services/
    └── ingress.yaml
```

---

## 🏆 Congratulations!

You've completed the Microservices Architecture guide! You now know:

- ✅ Microservices patterns and principles
- ✅ Service communication (sync & async)
- ✅ API Gateway and service discovery
- ✅ Data management strategies
- ✅ Resilience and fault tolerance
- ✅ Container orchestration
- ✅ Testing microservices
- ✅ Production deployment

**Next Steps:**
- Build a real microservices project
- Learn Kubernetes in depth
- Study event-driven architecture
- Explore service mesh (Istio)

Happy coding! 🚀
