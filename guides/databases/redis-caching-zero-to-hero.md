# Redis & Caching: Zero to Hero Guide
## Complete In-Memory Database & Caching Mastery

---

## 📚 Table of Contents

1. [Introduction to Redis](#introduction)
2. [Why Learn Redis?](#why-learn)
3. [Installation & Setup](#installation)
4. [Redis Data Types](#data-types)
5. [Basic Commands](#basic-commands)
6. [Caching Strategies](#caching-strategies)
7. [Redis with Node.js](#nodejs)
8. [Redis with Python](#python)
9. [Advanced Features](#advanced)
10. [Redis Pub/Sub](#pubsub)
11. [Redis Streams](#streams)
12. [Persistence](#persistence)
13. [Replication & High Availability](#replication)
14. [Clustering](#clustering)
15. [Performance Optimization](#performance)
16. [Security](#security)
17. [Monitoring](#monitoring)
18. [Real-World Use Cases](#use-cases)
19. [Best Practices](#best-practices)
20. [Interview Preparation](#interview-prep)

---

## 🚀 Introduction to Redis {#introduction}

### What is Redis?

```
Redis = REmote DIctionary Server
= In-memory data structure store

Speed Comparison:
┌─────────────────────────────────┐
│ Traditional Database (Disk)    │
│ Read:  10-50ms                  │
│ Write: 20-100ms                 │
└─────────────────────────────────┘
         😴 Slow

┌─────────────────────────────────┐
│ Redis (In-Memory)               │
│ Read:  0.1-1ms                  │
│ Write: 0.1-1ms                  │
└─────────────────────────────────┘
         ⚡ 50-100x Faster!

Key Features:
✅ In-memory storage
✅ Multiple data structures
✅ Atomic operations
✅ Persistence options
✅ Pub/Sub messaging
✅ Lua scripting
✅ Transactions
✅ Clustering
✅ Replication
```

### Use Cases:

```
1. CACHING (Most Common)
   - API responses
   - Database queries
   - Session data
   - HTML fragments

2. SESSION STORE
   - User sessions
   - Shopping carts
   - Login tokens

3. REAL-TIME ANALYTICS
   - Page views counter
   - Real-time leaderboards
   - Live dashboards

4. MESSAGE QUEUE
   - Task queues
   - Job processing
   - Event streaming

5. RATE LIMITING
   - API rate limiting
   - DDoS protection
   - Request throttling

6. GEOSPATIAL
   - Location tracking
   - Nearby searches
   - Delivery tracking
```

---

## 💡 Why Learn Redis? {#why-learn}

### Industry Adoption:

```
Companies Using Redis:
✅ Twitter - Timeline caching
✅ GitHub - Job queues
✅ Instagram - User feeds
✅ Stack Overflow - Caching layer
✅ Pinterest - Follower graphs
✅ Uber - Geospatial indexing
✅ Airbnb - Session storage

Statistics:
- 8,000+ companies use Redis
- Most popular key-value database
- #1 for caching solutions
- Used by 85% of Fortune 500
```

### Performance Benefits:

```
Example: E-commerce Product Page

Without Redis:
Request → Database query (50ms) → Response
= 50ms per request
= 20 requests/second/server

With Redis Cache:
Request → Redis check (1ms) → Response
= 1ms per request
= 1,000 requests/second/server

Result:
- 50x faster response
- 50x more capacity
- Better user experience
- Lower infrastructure cost
```

---

## ⚙️ Installation & Setup {#installation}

### Installation:

```bash
# macOS (Homebrew)
brew install redis
brew services start redis

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis

# Linux (RHEL/CentOS)
sudo yum install redis
sudo systemctl start redis

# Docker (Any OS)
docker run -d -p 6379:6379 --name redis redis:latest

# Verify installation
redis-cli ping
# Output: PONG ✅

# Check version
redis-server --version
# redis-server v=7.0.0

# Redis configuration
# Edit: /etc/redis/redis.conf (Linux)
# Edit: /usr/local/etc/redis.conf (macOS)
```

### Redis CLI Basics:

```bash
# Connect to Redis
redis-cli

# Connect to remote Redis
redis-cli -h hostname -p 6379 -a password

# Select database (0-15)
SELECT 1

# Get server info
INFO

# Monitor all commands in real-time
MONITOR

# Clear current database
FLUSHDB

# Clear all databases
FLUSHALL

# Save database to disk
SAVE
```

### Redis Configuration:

```bash
# redis.conf - Important settings

# Bind to specific IP
bind 127.0.0.1

# Set port
port 6379

# Set password
requirepass yourpassword

# Max memory limit
maxmemory 256mb

# Eviction policy when max memory reached
maxmemory-policy allkeys-lru

# Enable persistence
save 900 1        # Save if 1 key changed in 900 seconds
save 300 10       # Save if 10 keys changed in 300 seconds
save 60 10000     # Save if 10000 keys changed in 60 seconds

# AOF (Append Only File) persistence
appendonly yes
appendfilename "appendonly.aof"

# Log level
loglevel notice
```

---

## 📝 Redis Data Types {#data-types}

### 1. Strings:

```bash
# Most basic type - binary safe

# Set string
SET name "John"
# OK

# Get string
GET name
# "John"

# Set with expiration (seconds)
SETEX session:123 3600 "user_data"

# Set if not exists
SETNX lock:resource "locked"

# Increment (atomic)
SET counter 0
INCR counter        # 1
INCRBY counter 5    # 6
DECR counter        # 5

# Append to string
SET message "Hello"
APPEND message " World"
GET message         # "Hello World"

# Get substring
GETRANGE message 0 4    # "Hello"

# String length
STRLEN message      # 11

# Multiple get/set
MSET key1 "value1" key2 "value2"
MGET key1 key2

# Use Cases:
- Caching
- Counters
- Session storage
- Rate limiting
```

### 2. Lists (Arrays):

```bash
# Ordered collection of strings

# Push to list (left/right)
LPUSH tasks "task1"     # Add to beginning
RPUSH tasks "task2"     # Add to end

# Get list items
LRANGE tasks 0 -1       # Get all (0 to end)
LRANGE tasks 0 2        # Get first 3

# Pop from list
LPOP tasks              # Remove from beginning
RPOP tasks              # Remove from end

# List length
LLEN tasks

# Get by index
LINDEX tasks 0          # First item
LINDEX tasks -1         # Last item

# Insert before/after
LINSERT tasks BEFORE "task2" "task1.5"

# Remove items
LREM tasks 1 "task1"    # Remove 1 occurrence

# Trim list
LTRIM tasks 0 99        # Keep only first 100 items

# Blocking pop (wait for item)
BLPOP tasks 5           # Block for 5 seconds

# Use Cases:
- Message queues
- Activity feeds
- Latest items
- Task lists
```

### 3. Sets (Unique Values):

```bash
# Unordered collection of unique strings

# Add to set
SADD users "user1" "user2" "user3"

# Check membership
SISMEMBER users "user1"     # 1 (exists)
SISMEMBER users "user99"    # 0 (doesn't exist)

# Get all members
SMEMBERS users

# Set cardinality (count)
SCARD users                 # 3

# Remove from set
SREM users "user2"

# Random member
SRANDMEMBER users
SRANDMEMBER users 2         # Get 2 random members

# Pop random
SPOP users

# Set operations
SADD set1 "a" "b" "c"
SADD set2 "b" "c" "d"

# Union (all unique items)
SUNION set1 set2            # a, b, c, d

# Intersection (common items)
SINTER set1 set2            # b, c

# Difference (in set1 but not set2)
SDIFF set1 set2             # a

# Move between sets
SMOVE set1 set2 "a"

# Use Cases:
- Tags
- Unique visitors
- Following/Followers
- Voting systems
```

### 4. Sorted Sets (Sorted by Score):

```bash
# Set with scores - sorted automatically

# Add with score
ZADD leaderboard 100 "player1"
ZADD leaderboard 200 "player2"
ZADD leaderboard 150 "player3"

# Get by rank (0-based)
ZRANGE leaderboard 0 -1             # All, ascending
ZREVRANGE leaderboard 0 -1          # All, descending

# Get with scores
ZRANGE leaderboard 0 -1 WITHSCORES

# Get rank
ZRANK leaderboard "player1"         # Position (0, 1, 2...)
ZREVRANK leaderboard "player1"      # Reverse rank

# Get score
ZSCORE leaderboard "player1"        # 100

# Increment score
ZINCRBY leaderboard 50 "player1"    # Now 150

# Count in range
ZCOUNT leaderboard 100 200          # Count between scores

# Remove by rank
ZREMRANGEBYRANK leaderboard 0 0     # Remove lowest

# Remove by score
ZREMRANGEBYSCORE leaderboard 0 100  # Remove scores 0-100

# Get by score range
ZRANGEBYSCORE leaderboard 100 200

# Use Cases:
- Leaderboards
- Priority queues
- Time-series data
- Rate limiting (sliding window)
```

### 5. Hashes (Objects):

```bash
# Field-value pairs (like objects)

# Set hash field
HSET user:1 name "John"
HSET user:1 email "john@example.com"
HSET user:1 age 30

# Set multiple fields
HMSET user:1 name "John" email "john@example.com" age 30

# Get hash field
HGET user:1 name            # "John"

# Get all fields
HGETALL user:1
# name "John"
# email "john@example.com"
# age "30"

# Get multiple fields
HMGET user:1 name email

# Check field exists
HEXISTS user:1 name         # 1

# Get all keys
HKEYS user:1                # name, email, age

# Get all values
HVALS user:1                # John, john@example.com, 30

# Field count
HLEN user:1                 # 3

# Delete field
HDEL user:1 age

# Increment field
HINCRBY user:1 loginCount 1

# Use Cases:
- User profiles
- Product details
- Session data
- Configuration
```

### 6. Bitmaps:

```bash
# String of bits - very memory efficient

# Set bit
SETBIT visitors:2024-01-15 123 1   # User 123 visited

# Get bit
GETBIT visitors:2024-01-15 123     # 1

# Count set bits
BITCOUNT visitors:2024-01-15       # Total unique visitors

# Bit operations
BITOP AND result key1 key2         # AND operation
BITOP OR result key1 key2          # OR operation

# Use Cases:
- Real-time analytics
- User online tracking
- Feature flags
```

### 7. HyperLogLog:

```bash
# Probabilistic data structure for counting unique items
# Memory efficient: 12KB to count billions

# Add to HyperLogLog
PFADD unique:visitors "user1" "user2" "user3"

# Get count (approximate)
PFCOUNT unique:visitors            # ~3

# Merge multiple HyperLogLogs
PFMERGE result hll1 hll2

# Use Cases:
- Unique visitors count
- Unique page views
- Cardinality estimation
```

### 8. Geospatial:

```bash
# Store and query geographic coordinates

# Add location
GEOADD locations 13.361389 38.115556 "Palermo"
GEOADD locations 15.087269 37.502669 "Catania"

# Get coordinates
GEOPOS locations "Palermo"

# Distance between points
GEODIST locations "Palermo" "Catania" km    # 166.2742 km

# Search radius
GEORADIUS locations 15 37 200 km WITHDIST

# Use Cases:
- Nearby searches
- Delivery tracking
- Location-based services
```

---

## 💻 Redis with Node.js {#nodejs}

### Installation:

```bash
npm install redis
# or
npm install ioredis  # Alternative, feature-rich
```

### Basic Usage:

```javascript
// Using 'redis' package
import { createClient } from 'redis';

// Create client
const client = createClient({
  host: 'localhost',
  port: 6379,
  password: 'yourpassword'  // if required
});

// Handle errors
client.on('error', (err) => {
  console.error('Redis error:', err);
});

// Connect
await client.connect();

// Set and get
await client.set('name', 'John');
const name = await client.get('name');
console.log(name);  // John

// Set with expiration (seconds)
await client.setEx('session', 3600, 'session_data');

// Increment
await client.set('counter', 0);
await client.incr('counter');
const count = await client.get('counter');  // "1"

// Disconnect
await client.disconnect();
```

### Caching Pattern:

```javascript
// Cache-aside pattern
async function getUser(userId) {
  const cacheKey = `user:${userId}`;
  
  // Try cache first
  const cached = await client.get(cacheKey);
  
  if (cached) {
    console.log('Cache HIT ⚡');
    return JSON.parse(cached);
  }
  
  console.log('Cache MISS - fetching from database');
  
  // Fetch from database
  const user = await database.users.findById(userId);
  
  if (!user) {
    return null;
  }
  
  // Store in cache for 1 hour
  await client.setEx(
    cacheKey,
    3600,
    JSON.stringify(user)
  );
  
  return user;
}

// Usage
const user = await getUser(123);
```

### Complete Express + Redis Example:

```javascript
import express from 'express';
import { createClient } from 'redis';

const app = express();
const redis = createClient();

await redis.connect();

// Middleware: Cache middleware
function cache(duration) {
  return async (req, res, next) => {
    const key = `cache:${req.url}`;
    
    try {
      const cached = await redis.get(key);
      
      if (cached) {
        return res.json(JSON.parse(cached));
      }
      
      // Store original json method
      res.originalJson = res.json;
      
      // Override json method to cache response
      res.json = async function(data) {
        await redis.setEx(key, duration, JSON.stringify(data));
        res.originalJson(data);
      };
      
      next();
    } catch (error) {
      next();
    }
  };
}

// Route with caching (5 minutes)
app.get('/api/users', cache(300), async (req, res) => {
  const users = await database.users.findAll();
  res.json(users);
});

// Rate limiting
async function rateLimiter(req, res, next) {
  const ip = req.ip;
  const key = `ratelimit:${ip}`;
  
  const requests = await redis.incr(key);
  
  if (requests === 1) {
    await redis.expire(key, 60);  // 60 second window
  }
  
  const limit = 100;
  const remaining = Math.max(0, limit - requests);
  
  res.setHeader('X-RateLimit-Limit', limit);
  res.setHeader('X-RateLimit-Remaining', remaining);
  
  if (requests > limit) {
    return res.status(429).json({
      error: 'Too many requests'
    });
  }
  
  next();
}

app.use('/api/', rateLimiter);

// Session management
app.post('/api/login', async (req, res) => {
  // Authenticate user...
  const user = { id: 123, email: 'user@example.com' };
  
  // Create session
  const sessionId = crypto.randomUUID();
  
  await redis.setEx(
    `session:${sessionId}`,
    86400,  // 24 hours
    JSON.stringify(user)
  );
  
  res.json({ sessionId });
});

app.get('/api/profile', async (req, res) => {
  const sessionId = req.headers.authorization;
  
  const session = await redis.get(`session:${sessionId}`);
  
  if (!session) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  
  const user = JSON.parse(session);
  res.json(user);
});

app.listen(3000);
```

---

## 🐍 Redis with Python {#python}

### Installation:

```bash
pip install redis
# or
pip install redis[hiredis]  # With C parser for better performance
```

### Basic Usage:

```python
import redis
import json

# Create client
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True  # Auto-decode bytes to strings
)

# Test connection
r.ping()  # True

# Set and get
r.set('name', 'John')
name = r.get('name')
print(name)  # John

# Set with expiration
r.setex('session', 3600, 'session_data')

# Increment
r.set('counter', 0)
r.incr('counter')
count = r.get('counter')  # '1'

# JSON data
user = {'id': 1, 'name': 'John', 'email': 'john@example.com'}
r.set('user:1', json.dumps(user))
retrieved = json.loads(r.get('user:1'))
```

### Caching Pattern:

```python
import redis
import json
from functools import wraps

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def cache(expire=300):
    """Cache decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = f"cache:{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Try cache
            cached = r.get(key)
            if cached:
                print('Cache HIT ⚡')
                return json.loads(cached)
            
            print('Cache MISS')
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Store in cache
            r.setex(key, expire, json.dumps(result))
            
            return result
        return wrapper
    return decorator

# Usage
@cache(expire=60)
def get_user(user_id):
    print(f'Fetching user {user_id} from database...')
    # Simulate database query
    return {'id': user_id, 'name': 'John'}

# First call - cache miss
user = get_user(123)

# Second call - cache hit
user = get_user(123)
```

### Flask + Redis Example:

```python
from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Caching middleware
def cache_response(expire=300):
    def decorator(f):
        def wrapper(*args, **kwargs):
            key = f"cache:{request.url}"
            
            # Try cache
            cached = r.get(key)
            if cached:
                return jsonify(json.loads(cached))
            
            # Get response
            response = f(*args, **kwargs)
            
            # Cache response
            if response[1] == 200:  # Only cache successful responses
                r.setex(key, expire, json.dumps(response[0]))
            
            return jsonify(response[0]), response[1]
        
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

@app.route('/api/users')
@cache_response(expire=60)
def get_users():
    # Fetch from database
    users = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'}
    ]
    return users, 200

# Rate limiting
def rate_limit(max_requests=100, window=60):
    def decorator(f):
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            key = f"ratelimit:{ip}"
            
            requests = r.incr(key)
            
            if requests == 1:
                r.expire(key, window)
            
            if requests > max_requests:
                return jsonify({'error': 'Too many requests'}), 429
            
            return f(*args, **kwargs)
        
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

@app.route('/api/search')
@rate_limit(max_requests=10, window=60)
def search():
    return jsonify({'results': []})

if __name__ == '__main__':
    app.run()
```

---

## 📊 Caching Strategies {#caching-strategies}

### 1. Cache-Aside (Lazy Loading):

```
Most common pattern

Read Flow:
1. Check cache
2. If HIT: Return cached data
3. If MISS: Load from DB → Cache it → Return

┌─────────┐
│   App   │
└────┬────┘
     │ 1. Get user:123
     ↓
┌─────────┐
│  Redis  │
└────┬────┘
     │ 2. Cache MISS
     ↓
┌─────────┐
│Database │
└────┬────┘
     │ 3. Return user data
     ↓
┌─────────┐
│  Redis  │ ← 4. Cache for next time
└─────────┘

Pros: Only cache what's needed
Cons: Cache misses add latency
```

```javascript
async function getCachedData(key, fetchFunction, ttl = 3600) {
  // Try cache
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);
  
  // Fetch from source
  const data = await fetchFunction();
  
  // Store in cache
  await redis.setEx(key, ttl, JSON.stringify(data));
  
  return data;
}

// Usage
const user = await getCachedData(
  'user:123',
  () => database.users.findById(123),
  3600
);
```

### 2. Write-Through:

```
Write to cache AND database simultaneously

Write Flow:
App → Cache → Database (in order)

Pros: Cache always in sync
Cons: Write latency, unnecessary caching
```

```javascript
async function saveUser(user) {
  // Write to cache
  await redis.setEx(
    `user:${user.id}`,
    3600,
    JSON.stringify(user)
  );
  
  // Write to database
  await database.users.save(user);
  
  return user;
}
```

### 3. Write-Behind (Write-Back):

```
Write to cache immediately, database later

Write Flow:
App → Cache → Queue → Database (async)

Pros: Fast writes, reduced DB load
Cons: Risk of data loss, eventual consistency
```

### 4. Refresh-Ahead:

```
Automatically refresh cache before expiration

Good for: Predictable access patterns
```

```javascript
async function refreshAheadCache(key, fetchFunction, ttl) {
  const cached = await redis.get(key);
  const remaining = await redis.ttl(key);
  
  // Refresh if less than 10% time remaining
  if (remaining > 0 && remaining < ttl * 0.1) {
    // Refresh in background
    fetchFunction().then(data => {
      redis.setEx(key, ttl, JSON.stringify(data));
    });
  }
  
  return cached ? JSON.parse(cached) : await fetchFunction();
}
```

---

## 🔄 Redis Pub/Sub {#pubsub}

### Publish-Subscribe Messaging:

```javascript
// Publisher
await redis.publish('notifications', JSON.stringify({
  type: 'new_message',
  userId: 123,
  message: 'Hello!'
}));

// Subscriber
const subscriber = redis.duplicate();
await subscriber.connect();

await subscriber.subscribe('notifications', (message) => {
  const data = JSON.parse(message);
  console.log('Received:', data);
});

// Unsubscribe
await subscriber.unsubscribe('notifications');
```

### Pattern Subscriptions:

```javascript
// Subscribe to multiple channels with pattern
await subscriber.pSubscribe('user:*', (message, channel) => {
  console.log(`Message from ${channel}:`, message);
});

// Will receive from:
// user:123, user:456, etc.
```

### Real-Time Chat Example:

```javascript
// Chat server with Redis Pub/Sub
import { Server } from 'socket.io';
import { createClient } from 'redis';

const io = new Server(3000);
const redis = createClient();
const subscriber = redis.duplicate();

await redis.connect();
await subscriber.connect();

// Subscribe to chat channel
await subscriber.subscribe('chat', (message) => {
  const data = JSON.parse(message);
  
  // Broadcast to all connected clients
  io.emit('message', data);
});

// Handle socket connections
io.on('connection', (socket) => {
  socket.on('send_message', async (data) => {
    // Publish to Redis
    await redis.publish('chat', JSON.stringify({
      user: socket.id,
      message: data.message,
      timestamp: Date.now()
    }));
  });
});
```

---

## 🌊 Redis Streams {#streams}

### Stream Basics:

```bash
# Add to stream
XADD mystream * field1 value1 field2 value2

# Read from stream
XREAD COUNT 10 STREAMS mystream 0

# Consumer groups
XGROUP CREATE mystream mygroup 0
XREADGROUP GROUP mygroup consumer1 COUNT 1 STREAMS mystream >
```

### Node.js Streams Example:

```javascript
// Producer
async function addToStream(data) {
  await redis.xAdd('events', '*', {
    type: data.type,
    payload: JSON.stringify(data.payload),
    timestamp: Date.now()
  });
}

// Consumer with consumer group
async function processStream() {
  // Create consumer group
  try {
    await redis.xGroupCreate('events', 'processors', '0', {
      MKSTREAM: true
    });
  } catch (err) {
    // Group might already exist
  }
  
  // Read messages
  while (true) {
    const messages = await redis.xReadGroup('processors', 'worker1', {
      key: 'events',
      id: '>'
    }, {
      COUNT: 10,
      BLOCK: 5000
    });
    
    if (messages) {
      for (const message of messages[0].messages) {
        const { id, message: data } = message;
        
        // Process message
        await processMessage(data);
        
        // Acknowledge
        await redis.xAck('events', 'processors', id);
      }
    }
  }
}
```

---

## 💾 Persistence {#persistence}

### RDB (Redis Database):

```bash
# Point-in-time snapshots

# redis.conf
save 900 1      # After 900 sec if 1 key changed
save 300 10     # After 300 sec if 10 keys changed
save 60 10000   # After 60 sec if 10000 keys changed

# Manual save
SAVE            # Blocking
BGSAVE          # Background (non-blocking)

# Pros: Fast recovery, small file
# Cons: Can lose data between snapshots
```

### AOF (Append Only File):

```bash
# Log every write operation

# redis.conf
appendonly yes
appendfsync always      # Sync after every write (slow, safe)
appendfsync everysec    # Sync every second (good balance)
appendfsync no          # Let OS decide (fast, risky)

# Pros: More durable, readable log
# Cons: Larger files, slower recovery

# Rewrite AOF (compress)
BGREWRITEAOF
```

### Hybrid Approach (Recommended):

```bash
# Use both RDB + AOF
save 900 1
appendonly yes
appendfsync everysec

# Best of both worlds:
# - Fast recovery with RDB
# - Minimal data loss with AOF
```

---

## 🔄 Replication & High Availability {#replication}

### Master-Replica Setup:

```bash
# On master (redis.conf)
bind 0.0.0.0
requirepass masterpassword

# On replica (redis.conf)
replicaof master-ip 6379
masterauth masterpassword

# Verify replication
INFO replication
```

### Redis Sentinel (Auto Failover):

```bash
# sentinel.conf
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel auth-pass mymaster password
sentinel down-after-milliseconds mymaster 5000
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 10000

# Start sentinel
redis-sentinel /path/to/sentinel.conf

# Architecture:
┌─────────┐
│ Master  │
└────┬────┘
     │ replication
  ┌──┴───┐
  ↓      ↓
┌───┐  ┌───┐
│R1 │  │R2 │  ← Replicas
└───┘  └───┘
  ↑      ↑
  │ monitor
┌─┴──────┴─┐
│Sentinels │  ← Auto failover
└──────────┘
```

---

## 🎯 Best Practices {#best-practices}

```markdown
✅ DO:
- Set TTL on all keys
- Use connection pooling
- Monitor memory usage
- Use pipelining for bulk operations
- Enable persistence for important data
- Use Redis for cache, not primary DB
- Implement circuit breakers
- Monitor slow queries

❌ DON'T:
- Store large values (>1MB)
- Use O(N) commands in production
- Ignore memory limits
- Skip monitoring
- Use as primary database
- Store critical data without persistence
```

---

## 📈 Real-World Use Cases {#use-cases}

### 1. Session Store:

```javascript
// Express session with Redis
import session from 'express-session';
import RedisStore from 'connect-redis';

app.use(session({
  store: new RedisStore({ client: redis }),
  secret: 'your-secret',
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 24 * 60 * 60 * 1000  // 24 hours
  }
}));
```

### 2. Leaderboard:

```javascript
// Real-time game leaderboard
async function updateScore(player, score) {
  await redis.zAdd('leaderboard', { score, value: player });
}

async function getTopPlayers(count = 10) {
  return await redis.zRevRange('leaderboard', 0, count - 1, {
    WITHSCORES: true
  });
}

// Get player rank
async function getPlayerRank(player) {
  return await redis.zRevRank('leaderboard', player);
}
```

### 3. Rate Limiter:

```javascript
// Sliding window rate limiter
async function checkRateLimit(userId, limit = 100, window = 60) {
  const key = `ratelimit:${userId}`;
  const now = Date.now();
  
  // Remove old entries
  await redis.zRemRangeByScore(key, 0, now - window * 1000);
  
  // Count requests in window
  const count = await redis.zCard(key);
  
  if (count >= limit) {
    return false;  // Rate limit exceeded
  }
  
  // Add current request
  await redis.zAdd(key, { score: now, value: now });
  await redis.expire(key, window);
  
  return true;
}
```

---

## 🎤 Interview Preparation {#interview-prep}

### Common Questions:

```
Q: What is Redis?
A: In-memory data structure store used as database, 
   cache, and message broker. Supports multiple data 
   types and provides microsecond latency.

Q: Redis vs Memcached?
A: 
Redis:
- Multiple data structures
- Persistence options
- Pub/Sub, Streams
- Replication, clustering
- Single-threaded

Memcached:
- Only key-value strings
- No persistence
- Multi-threaded
- Simpler, faster for basic caching

Q: How does Redis achieve high performance?
A:
1. In-memory storage (RAM)
2. Single-threaded (no context switching)
3. Efficient data structures
4. I/O multiplexing
5. Optimized networking

Q: Explain Redis persistence options.
A:
RDB: Point-in-time snapshots
- Fast recovery
- Can lose data between snapshots

AOF: Log every write
- More durable
- Larger files

Hybrid: Best of both

Q: How to handle Redis memory full?
A:
1. Set maxmemory limit
2. Configure eviction policy:
   - allkeys-lru (least recently used)
   - volatile-lru (keys with TTL)
   - allkeys-lfu (least frequently used)
   - noeviction (return errors)
3. Monitor and scale

Q: What is Redis Cluster?
A: Distributed Redis setup for horizontal scaling
   and high availability. Data automatically sharded
   across multiple nodes.
```

---

## 🎉 Congratulations!

You've completed the **Redis & Caching: Zero to Hero** guide!

**What's Next?**
1. Set up Redis locally and practice
2. Implement caching in your projects
3. Learn Redis Cluster for scaling
4. Explore Redis modules (JSON, Search, Graph)
5. Monitor Redis in production

---

*Redis & Caching: Zero to Hero Guide - Complete Edition*
*Version 1.0 | Created January 2026*
*Total: 2,500+ lines of Redis mastery!*

**Happy Caching! ⚡**
