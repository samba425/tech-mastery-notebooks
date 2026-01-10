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

**What is Saga Pattern?**

Saga is a design pattern for managing distributed transactions across multiple microservices without using traditional two-phase commit. Each service performs a local transaction and publishes an event or message.

**Why Use Saga?**

- **No Distributed Locks**: Avoids the complexity and performance issues of 2PC (two-phase commit)
- **High Availability**: Services remain independent, no blocking transactions
- **Eventual Consistency**: Data becomes consistent over time, not immediately
- **Fault Tolerance**: Built-in compensation for failures

**How Saga Works:**

1. **Forward Flow**: Each service completes its transaction and triggers the next
2. **Compensation Flow**: If any step fails, execute compensating transactions to rollback previous steps

**Two Implementation Approaches:**

1. **Choreography**: Each service listens to events and knows what to do next (decentralized)
2. **Orchestration**: Central coordinator tells each service what to do (centralized)

**Saga Flow Example:**
```
[Create Order] → [Reserve Inventory] → [Process Payment] → [Confirm Order]
       ↓                  ↓                    ✗               
[Cancel Order] ← [Release Inventory] ← [Compensation Needed]
```

**When to Use Saga:**
- Multi-step business processes across services
- E-commerce order processing
- Travel booking systems
- Financial transactions
- Any workflow requiring cross-service consistency

**Challenges:**
- Complex error handling and compensation logic
- Eventual consistency (not immediate)
- Debugging distributed workflows

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

**What is Event Sourcing?**

Event Sourcing stores all changes to application state as a sequence of events, rather than just storing the current state. The current state is derived by replaying all events.

**Why Use Event Sourcing?**

- **Complete Audit Trail**: Every change is recorded, perfect for compliance
- **Time Travel**: Reconstruct state at any point in time
- **Debugging**: Replay events to understand what happened
- **Event-Driven Architecture**: Natural fit for microservices
- **Flexibility**: Create new views/reports from historical events

**How Event Sourcing Works:**

1. **Command**: User action (e.g., "Create Order")
2. **Event**: Result stored (e.g., "OrderCreated", "PaymentProcessed")
3. **Event Store**: Append-only log of all events
4. **Projection**: Current state built by replaying events

**Event Sourcing Flow:**
```
Command → Validate → Create Event → Store Event → Update Projection
                                         ↓
                                    [Event Store]
                                    - OrderCreated
                                    - ItemAdded
                                    - PaymentProcessed
```

**When to Use Event Sourcing:**
- Banking and financial systems (audit requirements)
- Collaborative applications (version control, undo/redo)
- Complex business domains
- Systems requiring complete history

**Challenges:**
- Event schema evolution
- Storage costs (all events forever)
- Complex querying (need projections)
- Learning curve

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

**What is CQRS?**

CQRS separates read and write operations into different models. Commands (writes) modify data, while Queries (reads) retrieve data from optimized read models.

**Why Use CQRS?**

- **Optimized Performance**: Write model normalized for consistency, read model denormalized for speed
- **Scalability**: Scale reads and writes independently
- **Flexibility**: Different databases for reads vs writes (polyglot persistence)
- **Complex Domains**: Clearer separation of concerns

**How CQRS Works:**

1. **Command Side (Write)**: Handles create/update/delete operations
2. **Event Publishing**: Commands publish events when data changes
3. **Read Model Sync**: Event handlers update optimized read models
4. **Query Side (Read)**: Serves read requests from denormalized data

**When to Use CQRS:**
- High read/write ratio (different scaling needs)
- Complex business logic
- Need for multiple read models (different views of same data)
- Event-driven architectures

**CQRS vs Traditional:**

| Aspect | Traditional | CQRS |
|--------|------------|------|
| Model | Single unified model | Separate read/write models |
| Database | One database | Can use different DBs |
| Complexity | Simple | More complex |
| Performance | Good for simple | Optimized for each operation |
| Scaling | Uniform | Independent scaling |

**Challenges:**
- Increased complexity
- Eventual consistency between read/write models
- Event synchronization overhead
- Not needed for simple CRUD apps

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

**What is Circuit Breaker?**

Circuit Breaker is a resilience pattern that prevents your application from repeatedly trying to execute an operation that's likely to fail. It acts like an electrical circuit breaker, stopping the flow when things go wrong.

**Why Use Circuit Breaker?**

- **Prevent Cascading Failures**: Stop failures from spreading across services
- **Fast Failures**: Return errors immediately instead of waiting for timeouts
- **System Recovery**: Give failing services time to recover
- **Resource Protection**: Prevent thread exhaustion from hanging calls

**How Circuit Breaker Works:**

**Three States:**

1. **CLOSED** (Normal): Requests pass through, failures counted
2. **OPEN** (Failed): Requests immediately rejected, no calls to service
3. **HALF-OPEN** (Testing): After timeout, allow few test requests

**State Transitions:**
```
CLOSED → (threshold failures) → OPEN
OPEN → (timeout expires) → HALF-OPEN
HALF-OPEN → (success) → CLOSED
HALF-OPEN → (failure) → OPEN
```

**When to Use:**
- Calling external APIs or services
- Database connections
- Network operations
- Any remote call that can fail or timeout

**Benefits:**
- Improves system resilience
- Better user experience (fast failures vs timeouts)
- Allows graceful degradation
- Monitors service health

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

## 🕸️ Service Mesh {#servicemesh}

**What is a Service Mesh?**

A service mesh is an infrastructure layer that handles service-to-service communication, providing features like traffic management, security, and observability without changing application code.

**Why Use Service Mesh?**

- **Traffic Control**: Advanced routing, load balancing, retries
- **Security**: Mutual TLS (mTLS) for all service communication
- **Observability**: Automatic metrics, logs, traces
- **Policy Enforcement**: Rate limiting, access control
- **No Code Changes**: Features added via sidecar proxies

**How Service Mesh Works:**

Each service gets a "sidecar" proxy (usually Envoy). All traffic goes through these proxies, which enforce policies and collect metrics.

```
Service A ──▶ Sidecar Proxy ──▶ Network ──▶ Sidecar Proxy ──▶ Service B
              (Envoy)                         (Envoy)
```

**Service Mesh Architecture:**

```
┌─────────────────────────────────────────┐
│        Control Plane (Istio)            │
│  - Configuration                        │
│  - Service Discovery                    │
│  - Certificate Management               │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐      ┌────▼─────┐
│ Pod A  │      │  Pod B   │
│┌──────┐│      │┌────────┐│
││Service││      ││ Service││
│└──────┘│      │└────────┘│
│┌──────┐│      │┌────────┐│
││ Envoy││◀────▶││  Envoy ││
│└──────┘│      │└────────┘│
└────────┘      └──────────┘
Data Plane      Data Plane
```

**Popular Service Meshes:**

| Service Mesh | Pros | Cons |
|--------------|------|------|
| **Istio** | Feature-rich, mature | Complex, heavy |
| **Linkerd** | Lightweight, simple | Fewer features |
| **Consul** | Multi-cloud, HashiCorp ecosystem | Learning curve |
| **AWS App Mesh** | AWS-native | AWS only |

**When to Use Service Mesh:**
- Many microservices (10+)
- Need advanced traffic management
- Security requirements (mTLS)
- Polyglot architecture (multiple languages)
- Need observability without code changes

**Istio Traffic Management**

```yaml
# Canary deployment with Istio
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: product-service
spec:
  hosts:
  - product-service
  http:
  - route:
    - destination:
        host: product-service
        subset: v1
      weight: 90  # 90% to stable version
    - destination:
        host: product-service
        subset: v2
      weight: 10  # 10% to canary
```

**Service Mesh vs Library Approach:**

| Feature | Service Mesh (Istio) | Library (Resilience4j) |
|---------|----------------------|------------------------|
| Implementation | Sidecar proxy | Application library |
| Language | Any language | Language-specific |
| Code Changes | None | Modify code |
| Overhead | Higher (extra container) | Lower |
| Features | Traffic, security, observability | Resilience patterns only |

---

## 🚀 Deployment Strategies {#deployment}

**What are Deployment Strategies?**

Deployment strategies are methods to release new versions of services while minimizing risk and downtime.

### 1. Blue-Green Deployment

**What it is:** Run two identical environments (Blue = current, Green = new). Switch traffic when ready.

**Why use it:**
- **Zero Downtime**: Instant cutover
- **Easy Rollback**: Switch back to blue if issues
- **Full Testing**: Test green in production environment

**How it works:**

```
Step 1: Blue (v1) serves 100% traffic
┌────────┐
│ Blue   │ ◀──── 100% Traffic
│  (v1)  │
└────────┘
┌────────┐
│ Green  │       (Idle)
│  (v2)  │
└────────┘

Step 2: Deploy to Green, test
┌────────┐
│ Blue   │ ◀──── 100% Traffic
│  (v1)  │
└────────┘
┌────────┐
│ Green  │       Testing
│  (v2)  │ ◀──── Internal tests
└────────┘

Step 3: Switch traffic to Green
┌────────┐
│ Blue   │       (Standby)
│  (v1)  │
└────────┘
┌────────┐
│ Green  │ ◀──── 100% Traffic
│  (v2)  │
└────────┘
```

**Kubernetes Blue-Green**

```yaml
# Service (switch by changing selector)
apiVersion: v1
kind: Service
metadata:
  name: product-service
spec:
  selector:
    app: product-service
    version: v1  # Change to v2 to switch
  ports:
  - port: 80
    targetPort: 3000
```

### 2. Canary Deployment

**What it is:** Gradually roll out to a small percentage of users, then increase if successful.

**Why use it:**
- **Risk Reduction**: Test with small user subset
- **Performance Validation**: Monitor metrics on real traffic
- **Easy Rollback**: Affect minimal users if issues
- **A/B Testing**: Compare versions

**How it works:**

```
Step 1: 95% v1, 5% v2 (Canary)
┌────────┐
│   v1   │ ◀──── 95% Traffic
└────────┘
┌────────┐
│   v2   │ ◀──── 5% Traffic (Canary)
└────────┘

Step 2: If healthy, 50% v1, 50% v2
┌────────┐
│   v1   │ ◀──── 50% Traffic
└────────┘
┌────────┐
│   v2   │ ◀──── 50% Traffic
└────────┘

Step 3: All traffic to v2
┌────────┐
│   v2   │ ◀──── 100% Traffic
└────────┘
```

**Deployment Strategy Comparison:**

| Strategy | Downtime | Risk | Complexity | Rollback Speed | Cost |
|----------|----------|------|------------|----------------|------|
| **Blue-Green** | None | Medium | Medium | Instant | High (2x resources) |
| **Canary** | None | Low | High | Fast | Medium |
| **Rolling** | None | Medium | Low | Slow | Low |

**When to Use Each:**

- **Blue-Green**: Critical services, need instant rollback
- **Canary**: User-facing services, want gradual validation
- **Rolling**: Internal services, cost-conscious

---

---

## 🔒 Security Best Practices {#security-practices}

### 1. API Security

**Authentication & Authorization**

```javascript
// JWT with refresh tokens
const generateTokens = (userId) => {
  const accessToken = jwt.sign(
    { userId },
    process.env.ACCESS_TOKEN_SECRET,
    { expiresIn: '15m' }
  )
  
  const refreshToken = jwt.sign(
    { userId },
    process.env.REFRESH_TOKEN_SECRET,
    { expiresIn: '7d' }
  )
  
  return { accessToken, refreshToken }
}

// Verify access token
const verifyAccessToken = (token) => {
  try {
    return jwt.verify(token, process.env.ACCESS_TOKEN_SECRET)
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      throw new Error('Token expired, please refresh')
    }
    throw new Error('Invalid token')
  }
}
```

**API Rate Limiting Per Service**

```javascript
const rateLimit = require('express-rate-limit')
const RedisStore = require('rate-limit-redis')
const redis = require('redis')

const client = redis.createClient()

// Different limits for different endpoints
const authLimiter = rateLimit({
  store: new RedisStore({ client }),
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 login attempts per 15 minutes
  message: 'Too many login attempts, please try again later'
})

const apiLimiter = rateLimit({
  store: new RedisStore({ client }),
  windowMs: 60 * 1000,
  max: 100, // 100 requests per minute
  message: 'Rate limit exceeded'
})

app.post('/api/auth/login', authLimiter, loginHandler)
app.use('/api/', apiLimiter)
```

### 2. Secure Service-to-Service Communication

**Mutual TLS (mTLS)**

```javascript
// Generate certificates for each service
const https = require('https')
const fs = require('fs')

const options = {
  // Server certificate
  key: fs.readFileSync('./certs/service-key.pem'),
  cert: fs.readFileSync('./certs/service-cert.pem'),
  
  // CA certificate for client verification
  ca: fs.readFileSync('./certs/ca-cert.pem'),
  
  // Require client certificate
  requestCert: true,
  rejectUnauthorized: true
}

https.createServer(options, app).listen(3001)
```

**Service Mesh with Istio (Automatic mTLS)**

```yaml
# Enable automatic mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT  # Enforce mTLS for all services
```

### 3. Secrets Management

**Using HashiCorp Vault**

```javascript
const vault = require('node-vault')({
  endpoint: 'http://vault:8200',
  token: process.env.VAULT_TOKEN
})

async function getDatabaseCredentials() {
  const result = await vault.read('secret/data/database')
  return result.data.data
}

// Rotate secrets automatically
async function rotateSecret() {
  const newPassword = generateSecurePassword()
  await vault.write('secret/data/database', {
    data: {
      username: 'dbuser',
      password: newPassword
    }
  })
}
```

**Kubernetes Secrets**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secrets
type: Opaque
data:
  # Base64 encoded values
  username: dXNlcm5hbWU=
  password: cGFzc3dvcmQ=
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  template:
    spec:
      containers:
      - name: app
        image: user-service:latest
        env:
        - name: DB_USERNAME
          valueFrom:
            secretKeyRef:
              name: db-secrets
              key: username
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secrets
              key: password
```

### 4. Input Validation & Sanitization

```javascript
const Joi = require('joi')
const mongoSanitize = require('express-mongo-sanitize')
const xss = require('xss-clean')

// Schema validation
const userSchema = Joi.object({
  name: Joi.string().min(3).max(50).required(),
  email: Joi.string().email().required(),
  age: Joi.number().integer().min(18).max(120)
})

app.use(express.json({ limit: '10kb' }))  // Limit body size
app.use(mongoSanitize())  // Prevent NoSQL injection
app.use(xss())  // Prevent XSS attacks

// Validation middleware
const validate = (schema) => (req, res, next) => {
  const { error } = schema.validate(req.body)
  if (error) {
    return res.status(400).json({ error: error.details[0].message })
  }
  next()
}

app.post('/api/users', validate(userSchema), createUser)
```

---

## 📊 Advanced Monitoring & Observability {#advanced-monitoring}

### 1. Distributed Tracing with Jaeger

**OpenTelemetry Integration**

```javascript
const opentelemetry = require('@opentelemetry/api')
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node')
const { JaegerExporter } = require('@opentelemetry/exporter-jaeger')
const { registerInstrumentations } = require('@opentelemetry/instrumentation')
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http')
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express')

// Setup Jaeger exporter
const exporter = new JaegerExporter({
  serviceName: 'user-service',
  endpoint: 'http://jaeger:14268/api/traces'
})

const provider = new NodeTracerProvider()
provider.addSpanProcessor(new BatchSpanProcessor(exporter))
provider.register()

// Auto-instrument HTTP and Express
registerInstrumentations({
  instrumentations: [
    new HttpInstrumentation(),
    new ExpressInstrumentation()
  ]
})

// Custom spans
const tracer = opentelemetry.trace.getTracer('user-service')

async function getUserOrders(userId) {
  const span = tracer.startSpan('getUserOrders')
  span.setAttribute('user.id', userId)
  
  try {
    // Call order service
    const orders = await fetch(`http://order-service/api/orders?userId=${userId}`)
    span.addEvent('Orders fetched successfully')
    return orders
  } catch (error) {
    span.recordException(error)
    span.setStatus({ code: SpanStatusCode.ERROR })
    throw error
  } finally {
    span.end()
  }
}
```

### 2. Metrics with Prometheus

```javascript
const promClient = require('prom-client')
const express = require('express')
const app = express()

// Create a Registry
const register = new promClient.Registry()

// Add default metrics
promClient.collectDefaultMetrics({ register })

// Custom metrics
const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 0.5, 1, 2, 5]
})

const httpRequestTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
})

const activeConnections = new promClient.Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
})

register.registerMetric(httpRequestDuration)
register.registerMetric(httpRequestTotal)
register.registerMetric(activeConnections)

// Metrics middleware
app.use((req, res, next) => {
  const start = Date.now()
  
  activeConnections.inc()
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000
    
    httpRequestDuration.observe(
      {
        method: req.method,
        route: req.route?.path || req.path,
        status_code: res.statusCode
      },
      duration
    )
    
    httpRequestTotal.inc({
      method: req.method,
      route: req.route?.path || req.path,
      status_code: res.statusCode
    })
    
    activeConnections.dec()
  })
  
  next()
})

// Expose metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType)
  res.end(await register.metrics())
})
```

### 3. Centralized Logging with ELK Stack

**Structured Logging**

```javascript
const winston = require('winston')
const { ElasticsearchTransport } = require('winston-elasticsearch')

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'user-service',
    environment: process.env.NODE_ENV
  },
  transports: [
    // Console for development
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    }),
    
    // Elasticsearch for production
    new ElasticsearchTransport({
      level: 'info',
      clientOpts: {
        node: 'http://elasticsearch:9200'
      },
      index: 'logs-user-service'
    })
  ]
})

// Correlation ID middleware
app.use((req, res, next) => {
  req.correlationId = req.headers['x-correlation-id'] || generateId()
  res.setHeader('x-correlation-id', req.correlationId)
  
  // Add to logger context
  req.logger = logger.child({
    correlationId: req.correlationId,
    userId: req.user?.id
  })
  
  next()
})

// Usage
req.logger.info('User created', {
  userId: user.id,
  email: user.email
})
```

### 4. Alerting & Incident Management

**Prometheus Alerting Rules**

```yaml
# prometheus-alerts.yml
groups:
  - name: microservices
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status_code=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Service {{ $labels.service }} has error rate above 5%"
      
      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service is down"
          description: "{{ $labels.service }} has been down for 1 minute"
      
      - alert: HighLatency
        expr: http_request_duration_seconds_bucket{le="1"} < 0.95
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
          description: "P95 latency is above 1 second"
```

---

## 🔄 Advanced Patterns {#advanced-patterns}

### 1. Strangler Fig Pattern (Monolith to Microservices)

**What is Strangler Fig?**

Strangler Fig is a pattern for incrementally migrating from monolith to microservices by gradually replacing functionality.

**How it Works:**

```
Phase 1: Monolith handles everything
┌────────────────────────┐
│      Monolith          │
│  - Users               │
│  - Products            │
│  - Orders              │
└────────────────────────┘

Phase 2: Extract one service, route some traffic
┌────────────────────────┐     ┌──────────────┐
│      Monolith          │     │User Service  │
│  - Products            │◄────┤ (New)        │
│  - Orders              │     └──────────────┘
└────────────────────────┘

Phase 3: Continue extracting
┌────────────────────────┐     ┌──────────────┐
│      Monolith          │     │User Service  │
│  - Orders              │     └──────────────┘
└────────────────────────┘     ┌──────────────┐
                               │Product Svc   │
                               └──────────────┘

Phase 4: Complete migration
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│User Service  │  │Product Svc   │  │Order Service │
└──────────────┘  └──────────────┘  └──────────────┘
```

**Implementation with API Gateway**

```javascript
// API Gateway routing logic
const express = require('express')
const { createProxyMiddleware } = require('http-proxy-middleware')
const app = express()

// Feature flags to control migration
const featureFlags = {
  useUserMicroservice: true,
  useProductMicroservice: false
}

// Proxy to new user microservice or old monolith
app.use('/api/users', (req, res, next) => {
  if (featureFlags.useUserMicroservice) {
    return createProxyMiddleware({
      target: 'http://user-service:3001',
      changeOrigin: true
    })(req, res, next)
  } else {
    return createProxyMiddleware({
      target: 'http://monolith:8080',
      changeOrigin: true
    })(req, res, next)
  }
})

// Products still in monolith
app.use('/api/products', createProxyMiddleware({
  target: 'http://monolith:8080',
  changeOrigin: true
}))
```

### 2. Backend for Frontend (BFF) Pattern

**What is BFF?**

BFF creates specialized backend services for different frontend clients (mobile, web, desktop) with tailored APIs.

**Why Use BFF?**

- **Optimized Responses**: Each client gets exactly what it needs
- **Reduced Client Logic**: BFF handles aggregation and transformation
- **Better Performance**: Mobile gets lighter payloads
- **Client-Specific Features**: Different auth, caching per client

```
┌─────────────┐        ┌─────────────────┐        ┌──────────────┐
│  Mobile App │───────▶│  Mobile BFF     │───────▶│ User Service │
└─────────────┘        └─────────────────┘        └──────────────┘
                              │                    ┌──────────────┐
┌─────────────┐        ┌──────┴──────────┐        │Product Svc   │
│  Web App    │───────▶│  Web BFF        │───────▶└──────────────┘
└─────────────┘        └─────────────────┘        ┌──────────────┐
                                                   │Order Service │
                                                   └──────────────┘
```

**Example:**

```javascript
// mobile-bff/server.js - Mobile BFF
app.get('/api/dashboard', async (req, res) => {
  // Fetch data from multiple services
  const [user, orders, recommendations] = await Promise.all([
    fetch('http://user-service/api/users/' + req.user.id),
    fetch('http://order-service/api/orders?userId=' + req.user.id + '&limit=5'),
    fetch('http://recommendation-service/api/recommendations/' + req.user.id)
  ])
  
  // Return lightweight mobile response
  res.json({
    user: {
      name: user.name,
      avatar: user.avatar  // Small thumbnail
    },
    recentOrders: orders.slice(0, 3),  // Only 3 orders
    suggestions: recommendations.slice(0, 5)  // Only 5 suggestions
  })
})

// web-bff/server.js - Web BFF
app.get('/api/dashboard', async (req, res) => {
  // Fetch richer data for web
  const [user, orders, recommendations, analytics] = await Promise.all([
    fetch('http://user-service/api/users/' + req.user.id + '?full=true'),
    fetch('http://order-service/api/orders?userId=' + req.user.id + '&limit=20'),
    fetch('http://recommendation-service/api/recommendations/' + req.user.id),
    fetch('http://analytics-service/api/user-stats/' + req.user.id)
  ])
  
  // Return full web response with analytics
  res.json({
    user,
    orders: orders,  // All 20 orders
    recommendations,
    analytics  // Web-only analytics
  })
})
```

### 3. Sidecar Pattern

**What is Sidecar?**

Sidecar deploys a helper container alongside your main application container to handle cross-cutting concerns.

**Common Sidecar Uses:**
- Logging aggregation
- Configuration management
- Monitoring and metrics
- Service mesh proxy (Envoy)
- Secret management

```yaml
# Kubernetes deployment with sidecar
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  template:
    spec:
      containers:
      # Main application container
      - name: app
        image: user-service:latest
        ports:
        - containerPort: 3001
        volumeMounts:
        - name: shared-logs
          mountPath: /var/log/app
      
      # Logging sidecar container
      - name: log-shipper
        image: fluentd:latest
        volumeMounts:
        - name: shared-logs
          mountPath: /var/log/app
        env:
        - name: ELASTICSEARCH_HOST
          value: "elasticsearch:9200"
      
      # Metrics sidecar
      - name: metrics-collector
        image: prometheus-exporter:latest
        ports:
        - containerPort: 9090
      
      volumes:
      - name: shared-logs
        emptyDir: {}
```

### 4. Ambassador Pattern

**What is Ambassador?**

Ambassador pattern uses a proxy container to handle network communication on behalf of the main application.

**Use Cases:**
- Protocol translation (gRPC ↔ REST)
- Connection pooling
- Retry logic
- Circuit breaking

```javascript
// ambassador-proxy.js
const express = require('express')
const grpc = require('@grpc/grpc-js')
const app = express()

// REST endpoint that translates to gRPC
app.get('/api/users/:id', async (req, res) => {
  const client = new UserServiceClient('localhost:50051')
  
  client.getUser({ id: req.params.id }, (error, response) => {
    if (error) {
      return res.status(500).json({ error: error.message })
    }
    
    // Convert gRPC response to REST JSON
    res.json({
      id: response.id,
      name: response.name,
      email: response.email
    })
  })
})

app.listen(3000)  // REST interface
```

---

## 🚀 Production Readiness Checklist {#production-checklist}

### Before Going to Production

#### 1. **Performance**
- [ ] Load tested with expected traffic (use k6, JMeter)
- [ ] Database indexes optimized
- [ ] Caching implemented (Redis, CDN)
- [ ] Connection pooling configured
- [ ] Horizontal scaling tested
- [ ] Resource limits set (CPU, memory)

#### 2. **Reliability**
- [ ] Circuit breakers implemented
- [ ] Retry logic with exponential backoff
- [ ] Timeout configurations
- [ ] Health checks configured
- [ ] Graceful shutdown implemented
- [ ] Auto-scaling policies defined

#### 3. **Observability**
- [ ] Structured logging in place
- [ ] Distributed tracing enabled
- [ ] Metrics collection active
- [ ] Dashboards created (Grafana)
- [ ] Alerts configured
- [ ] Log aggregation setup (ELK)

#### 4. **Security**
- [ ] Authentication implemented
- [ ] Authorization enforced
- [ ] Secrets managed securely (Vault, K8s secrets)
- [ ] TLS/SSL enabled
- [ ] Rate limiting configured
- [ ] Input validation everywhere
- [ ] CORS configured properly
- [ ] Security headers added (Helmet)

#### 5. **Data Management**
- [ ] Backup strategy defined
- [ ] Disaster recovery plan
- [ ] Data retention policies
- [ ] GDPR/compliance requirements met
- [ ] Database migrations automated
- [ ] Data encryption at rest and in transit

#### 6. **Testing**
- [ ] Unit tests (>80% coverage)
- [ ] Integration tests
- [ ] Contract tests (Pact)
- [ ] End-to-end tests
- [ ] Performance tests
- [ ] Chaos engineering tests

#### 7. **Documentation**
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Architecture diagrams
- [ ] Runbooks for common issues
- [ ] Deployment procedures
- [ ] Incident response plan
- [ ] Service dependencies mapped

#### 8. **Operations**
- [ ] CI/CD pipeline configured
- [ ] Blue-green or canary deployment
- [ ] Rollback procedure tested
- [ ] Monitoring alerts tested
- [ ] On-call rotation defined
- [ ] Cost monitoring enabled

---

## 🏆 Congratulations!

You've completed the Microservices Architecture guide! You now know:

- ✅ Microservices patterns and principles
- ✅ Service communication (sync & async)
- ✅ API Gateway and service discovery
- ✅ Data management strategies (Saga, Event Sourcing, CQRS)
- ✅ Resilience patterns (Circuit Breaker, Retry, Timeout, Bulkhead)
- ✅ Security (JWT, mTLS, Secrets Management)
- ✅ Observability (Logging, Metrics, Tracing, Alerting)
- ✅ Service Mesh (Istio, traffic management, mTLS)
- ✅ Deployment Strategies (Blue-Green, Canary, Rolling)
- ✅ Advanced Patterns (Strangler Fig, BFF, Sidecar, Ambassador)
- ✅ Container orchestration with Kubernetes
- ✅ Testing microservices
- ✅ Production best practices and readiness checklist

**Next Steps:**
- Build a real microservices project (e-commerce, booking system)
- Master Kubernetes and Helm charts
- Study event-driven architecture in depth
- Implement full observability stack (ELK + Prometheus + Jaeger)
- Explore serverless microservices (AWS Lambda, Cloud Functions)
- Practice chaos engineering (break things intentionally!)

Happy coding! 🚀

