# Node.js & Express: Zero to Hero Guide
## Complete Backend JavaScript Development Mastery

---

## 📚 Table of Contents

1. [Introduction to Node.js](#introduction)
2. [Setting Up Environment](#setup)
3. [Node.js Fundamentals](#fundamentals)
4. [Express.js Framework](#express)
5. [RESTful API Development](#rest-api)
6. [Middleware & Error Handling](#middleware)
7. [Database Integration](#database)
8. [Authentication & Authorization](#auth)
9. [File Upload & Processing](#files)
10. [Real-time with Socket.io](#realtime)
11. [Testing & Debugging](#testing)
12. [Performance & Scalability](#performance)
13. [Deployment & Production](#deployment)
14. [Best Practices](#best-practices)
15. [Real-World Projects](#projects)

---

## 🎯 Introduction to Node.js {#introduction}

### What is Node.js?

**Node.js** is a JavaScript runtime built on Chrome's V8 engine that allows you to run JavaScript on the server.

```
┌─────────────────────────────────────┐
│         Traditional Model           │
├─────────────────────────────────────┤
│  Browser (JavaScript) ──────▶ UI    │
│  Server (PHP/Java/Python) ──▶ Logic │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│         Node.js Model               │
├─────────────────────────────────────┤
│  Browser (JavaScript) ──────▶ UI    │
│  Server (JavaScript) ────────▶ Logic│
│         Same Language! ✨           │
└─────────────────────────────────────┘
```

### Why Node.js?

- ✅ **JavaScript Everywhere** - One language for frontend and backend
- ✅ **Fast & Scalable** - Non-blocking I/O, event-driven
- ✅ **NPM Ecosystem** - Largest package registry
- ✅ **Real-time** - Perfect for chat, live updates
- ✅ **Microservices** - Lightweight and modular

### Node.js Architecture

```
                    ┌─────────────────────────────────────┐
                    │     Your JavaScript Code            │
                    │  (app.js, routes, controllers)      │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │      Node.js Core Modules           │
                    ├─────────────────────────────────────┤
                    │  • fs (File System)                 │
                    │  • http (HTTP Server)               │
                    │  • path (Path Utilities)            │
                    │  • crypto (Encryption)              │
                    │  • stream (Data Streaming)          │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────┐     ┌───────────▼────────┐     ┌──────────▼─────────┐
│  V8 Engine     │     │   libuv (C++)      │     │   Node Bindings    │
│                │     │                    │     │                    │
│ • Compiles JS  │     │ • Event Loop       │     │ • C++ ←→ JS        │
│ • Optimizes    │     │ • Thread Pool      │     │ • Native Modules   │
│ • Garbage      │     │ • Async I/O        │     │                    │
│   Collection   │     │ • Timers           │     │                    │
└────────────────┘     └────────────────────┘     └────────────────────┘
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     Operating System                │
                    │  (File I/O, Network, Processes)     │
                    └─────────────────────────────────────┘

📊 Event Loop Phases:
┌───────────────────────────────────────────────────────────────┐
│                    Event Loop Cycle                           │
└───────────────────────────────────────────────────────────────┘
│
├─► 1. Timers          : Execute setTimeout() & setInterval()
│
├─► 2. Pending         : Execute I/O callbacks deferred
│
├─► 3. Idle/Prepare    : Internal use only
│
├─► 4. Poll           : Retrieve new I/O events
│                        • Execute I/O callbacks
│                        • Wait for callbacks if queue empty
│
├─► 5. Check          : Execute setImmediate() callbacks
│
├─► 6. Close          : Execute close event callbacks
│                        (e.g., socket.on('close'))
│
└─► Back to Timers (Loop continues)

Microtasks (Higher Priority):
  → process.nextTick()
  → Promise.then()
  → async/await
```

---

## 🔧 Setting Up Environment {#setup}

### Installation

**Step 1: Install Node.js**

```bash
# macOS (using Homebrew)
brew install node

# Windows (download from nodejs.org)
# Or use nvm (Node Version Manager)

# Verify installation
node --version
npm --version
```

**Step 2: Project Setup**

```bash
# Create project directory
mkdir my-express-app
cd my-express-app

# Initialize package.json
npm init -y

# Install Express
npm install express

# Install development dependencies
npm install --save-dev nodemon
```

**Project Structure**

```
my-express-app/
├── node_modules/        # Dependencies
├── src/
│   ├── controllers/     # Route handlers
│   ├── models/          # Data models
│   ├── routes/          # Route definitions
│   ├── middleware/      # Custom middleware
│   ├── utils/           # Helper functions
│   └── app.js           # App entry point
├── tests/               # Test files
├── .env                 # Environment variables
├── .gitignore          # Git ignore file
└── package.json         # Project metadata
```

---

## 📖 Node.js Fundamentals {#fundamentals}

### 1. Modules System

**CommonJS (Node.js Default)**

```javascript
// math.js - Export
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = { add, subtract };

// app.js - Import
const math = require('./math');
console.log(math.add(5, 3)); // 8
```

**ES Modules (Modern)**

```javascript
// math.mjs - Export
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

// app.mjs - Import
import { add, subtract } from './math.mjs';
console.log(add(5, 3)); // 8
```

### 2. Asynchronous Programming

**Callbacks (Old Way)**

```javascript
const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log(data);
});
```

**Promises (Better)**

```javascript
const fs = require('fs').promises;

fs.readFile('file.txt', 'utf8')
  .then(data => console.log(data))
  .catch(err => console.error('Error:', err));
```

**Async/Await (Best)**

```javascript
const fs = require('fs').promises;

async function readFileAsync() {
  try {
    const data = await fs.readFile('file.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error('Error:', err);
  }
}

readFileAsync();
```

### 3. Event Loop

```
┌───────────────────────────┐
│      Call Stack           │  ← Your synchronous code
└───────────────────────────┘
            │
            ▼
┌───────────────────────────┐
│    Node.js APIs           │  ← fs, http, timers
│  (Background threads)     │
└───────────────────────────┘
            │
            ▼
┌───────────────────────────┐
│    Callback Queue         │  ← Completed operations
└───────────────────────────┘
            │
            ▼ (When call stack is empty)
┌───────────────────────────┐
│    Event Loop             │  ← Picks callbacks
│  (Executes callbacks)     │
└───────────────────────────┘
```

**Example:**

```javascript
console.log('1. Start');

setTimeout(() => {
  console.log('2. Timeout callback');
}, 0);

Promise.resolve().then(() => {
  console.log('3. Promise callback');
});

console.log('4. End');

// Output:
// 1. Start
// 4. End
// 3. Promise callback (Microtasks execute first!)
// 2. Timeout callback
```

### 4. Built-in Modules

**File System (fs)**

```javascript
const fs = require('fs').promises;

// Read file
const content = await fs.readFile('file.txt', 'utf8');

// Write file
await fs.writeFile('output.txt', 'Hello World');

// Check if file exists
const exists = await fs.access('file.txt')
  .then(() => true)
  .catch(() => false);
```

**Path Module**

```javascript
const path = require('path');

const filePath = '/user/local/file.txt';

console.log(path.dirname(filePath));  // /user/local
console.log(path.basename(filePath)); // file.txt
console.log(path.extname(filePath));  // .txt

// Join paths (works across OS)
const fullPath = path.join(__dirname, 'uploads', 'image.jpg');
```

**HTTP Module**

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World\n');
});

server.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### 5. Streams (Efficient Data Processing)

**What are Streams?**

Streams are objects that let you read data from a source or write data to a destination in a continuous manner. Instead of reading an entire file into memory, streams process data chunk by chunk.

**Why Use Streams?**

- **Memory Efficient**: Handle large files without consuming lots of RAM
- **Time Efficient**: Start processing data before entire file is loaded
- **Composable**: Chain multiple operations together using pipes

**Types of Streams:**

1. **Readable**: Read data from source (e.g., `fs.createReadStream`, HTTP requests)
2. **Writable**: Write data to destination (e.g., `fs.createWriteStream`, HTTP responses)
3. **Duplex**: Both readable and writable (e.g., TCP sockets)
4. **Transform**: Modify data while reading/writing (e.g., compression, encryption)

**When to Use Streams:**
- Processing large files (logs, videos, databases)
- Real-time data processing
- Network communication (HTTP, WebSockets)
- File uploads/downloads

```javascript
const fs = require('fs')
const { pipeline } = require('stream')

// Read Stream (large files)
const readStream = fs.createReadStream('large-file.txt', { encoding: 'utf8' })

readStream.on('data', (chunk) => {
  console.log('Received chunk:', chunk.length, 'bytes')
})

readStream.on('end', () => {
  console.log('Finished reading')
})

readStream.on('error', (err) => {
  console.error('Error:', err)
})

// Write Stream
const writeStream = fs.createWriteStream('output.txt')

writeStream.write('Hello ')
writeStream.write('World!')
writeStream.end()

// Pipe (efficient copy)
const readStream2 = fs.createReadStream('source.txt')
const writeStream2 = fs.createWriteStream('destination.txt')

readStream2.pipe(writeStream2)

// Transform Stream (modify data)
const { Transform } = require('stream')

const upperCaseTransform = new Transform({
  transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase())
    callback()
  }
})

// Pipeline (safer than pipe)
pipeline(
  fs.createReadStream('input.txt'),
  upperCaseTransform,
  fs.createWriteStream('output.txt'),
  (err) => {
    if (err) {
      console.error('Pipeline failed:', err)
    } else {
      console.log('Pipeline succeeded')
    }
  }
)
```

**Stream Types:**
```
┌────────────────────────────────────┐
│  Readable  → Read data             │
│  Writable  → Write data            │
│  Duplex    → Read & Write          │
│  Transform → Modify data           │
└────────────────────────────────────┘
```

### 6. Buffer (Binary Data)

**What is Buffer?**

Buffer is a temporary storage area for binary data. Unlike strings (which handle text), Buffers work with raw binary data like images, videos, or network packets.

**Why Use Buffers?**

- JavaScript strings are designed for UTF-16 text, not binary data
- Buffers provide efficient low-level memory operations
- Essential for file I/O, network protocols, cryptography

**How Buffers Work:**

Buffers allocate raw memory outside V8's heap memory. This makes them:
- Faster for binary operations
- Fixed-size (can't be resized)
- Not subject to garbage collection during allocation

**When to Use Buffers:**
- Reading/writing files
- Network communication (TCP/UDP)
- Image/video processing
- Encryption/decryption
- Working with binary protocols

```javascript
// Create buffer
const buf1 = Buffer.from('Hello')
const buf2 = Buffer.alloc(10)  // 10 bytes of zeros
const buf3 = Buffer.allocUnsafe(10)  // Faster but uninitialized

// Read buffer
console.log(buf1.toString())  // 'Hello'
console.log(buf1.toString('hex'))  // '48656c6c6f'

// Write to buffer
buf2.write('Node.js')
console.log(buf2.toString())  // 'Node.js'

// Buffer operations
const buf4 = Buffer.concat([buf1, buf2])
const sliced = buf4.slice(0, 5)

// Compare buffers
console.log(buf1.equals(buf2))  // false
console.log(Buffer.compare(buf1, buf2))  // -1, 0, or 1
```

### 7. Child Processes (Run External Commands)

Execute system commands and spawn separate processes.

```javascript
const { exec, spawn, fork } = require('child_process')

// exec - Run command and get output at once
exec('ls -la', (error, stdout, stderr) => {
  if (error) {
    console.error('Error:', error)
    return
  }
  console.log('Output:', stdout)
})

// spawn - Stream output (better for large output)
const ls = spawn('ls', ['-la'])

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`)
})

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`)
})

ls.on('close', (code) => {
  console.log(`Process exited with code ${code}`)
})

// fork - Run Node.js script in separate process
const child = fork('child.js')

child.send({ hello: 'world' })

child.on('message', (msg) => {
  console.log('Message from child:', msg)
})

// child.js
process.on('message', (msg) => {
  console.log('Message from parent:', msg)
  process.send({ foo: 'bar' })
})
```

### 8. Worker Threads (True Parallelism)

**What are Worker Threads?**

Worker Threads enable true parallel JavaScript execution by creating separate V8 instances. Unlike the event loop (which is concurrent but not parallel), worker threads run code simultaneously on multiple CPU cores.

**Why Use Worker Threads?**

- **True Parallelism**: Multiple threads execute at the same time
- **CPU-Intensive Tasks**: Handle heavy computations without blocking
- **Shared Memory**: Can share data via SharedArrayBuffer (faster than IPC)
- **Better than Child Processes**: Lighter weight, faster communication

**How Worker Threads Work:**

Each worker thread has:
- Own V8 instance and event loop
- Separate memory space (isolated)
- Message-based communication with main thread
- Ability to share memory via SharedArrayBuffer

**Worker Threads vs Child Processes:**

| Feature | Worker Threads | Child Processes |
|---------|---------------|----------------|
| Memory | Shared (can use SharedArrayBuffer) | Separate |
| Startup Time | Fast (~2ms) | Slower (~30ms) |
| Communication | `postMessage()` | IPC / Streams |
| Use Case | CPU-intensive JS | External programs, isolation |
| Overhead | Lightweight | Heavier |

**When to Use Worker Threads:**
- Image/video processing
- Data encryption/hashing
- Complex calculations (ML, simulations)
- Parallel array processing
- Tasks taking >50ms on main thread

```javascript
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads')

if (isMainThread) {
  // Main thread
  console.log('Main thread running')
  
  // Create worker
  const worker = new Worker(__filename, {
    workerData: { num: 5 }
  })
  
  // Listen for messages
  worker.on('message', (result) => {
    console.log('Result from worker:', result)
  })
  
  worker.on('error', (err) => {
    console.error('Worker error:', err)
  })
  
  worker.on('exit', (code) => {
    console.log(`Worker stopped with exit code ${code}`)
  })
  
} else {
  // Worker thread
  console.log('Worker thread running')
  
  // CPU-intensive task
  function fibonacci(n) {
    if (n <= 1) return n
    return fibonacci(n - 1) + fibonacci(n - 2)
  }
  
  const result = fibonacci(workerData.num)
  
  // Send result back
  parentPort.postMessage(result)
}
```

**Worker Pool Example:**

```javascript
const { Worker } = require('worker_threads')

class WorkerPool {
  constructor(workerScript, numWorkers) {
    this.workerScript = workerScript
    this.workers = []
    this.queue = []
    
    for (let i = 0; i < numWorkers; i++) {
      this.workers.push({ worker: null, busy: false })
    }
  }
  
  runTask(data) {
    return new Promise((resolve, reject) => {
      const availableWorker = this.workers.find(w => !w.busy)
      
      if (availableWorker) {
        this.executeTask(availableWorker, data, resolve, reject)
      } else {
        this.queue.push({ data, resolve, reject })
      }
    })
  }
  
  executeTask(workerObj, data, resolve, reject) {
    workerObj.busy = true
    workerObj.worker = new Worker(this.workerScript, { workerData: data })
    
    workerObj.worker.on('message', (result) => {
      resolve(result)
      workerObj.busy = false
      workerObj.worker.terminate()
      
      // Process queue
      if (this.queue.length > 0) {
        const { data, resolve, reject } = this.queue.shift()
        this.executeTask(workerObj, data, resolve, reject)
      }
    })
    
    workerObj.worker.on('error', reject)
  }
}

// Usage
const pool = new WorkerPool('./worker.js', 4)

async function processTasks() {
  const tasks = [1, 2, 3, 4, 5, 6, 7, 8]
  const results = await Promise.all(
    tasks.map(task => pool.runTask(task))
  )
  console.log('All results:', results)
}
```

### 9. Cluster Module (Multi-Process Scaling)

**What is Cluster Module?**

The Cluster module allows you to create multiple Node.js processes (workers) that share the same server port. This enables horizontal scaling on multi-core systems.

**Why Use Cluster Module?**

- **Full CPU Utilization**: Node.js is single-threaded; clustering uses all cores
- **High Availability**: If one worker crashes, others continue serving requests
- **Load Distribution**: Master process distributes connections across workers
- **Zero-Downtime Restarts**: Restart workers one at a time

**How Clustering Works:**

1. **Master Process**: Manages worker processes, distributes incoming connections
2. **Worker Processes**: Handle actual requests, each has own event loop
3. **Load Balancing**: Master uses round-robin (default on most OS) to distribute load
4. **IPC Communication**: Workers can communicate via master process

**Cluster Architecture:**

```
                    [Master Process]
                          |
        +-----------------+-----------------+
        |                 |                 |
    [Worker 1]        [Worker 2]       [Worker 3]
      Port 3000        Port 3000         Port 3000
```

**When to Use Cluster Module:**
- Production web servers
- High-traffic APIs
- Applications needing high availability
- When you need process-level isolation (crash recovery)

**Cluster vs Worker Threads vs Child Processes:**

| Feature | Cluster | Worker Threads | Child Processes |
|---------|---------|---------------|----------------|
| Purpose | HTTP load balancing | CPU-intensive tasks | System commands |
| Shares Port | ✅ Yes | ❌ No | ❌ No |
| Memory | Separate | Shared option | Separate |
| Communication | IPC | postMessage | IPC/Streams |
| Use Case | Web servers | Parallel computing | Shell integration |

```javascript
const cluster = require('cluster')
const http = require('http')
const numCPUs = require('os').cpus().length

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`)
  
  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork()
  }
  
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`)
    console.log('Starting a new worker...')
    cluster.fork()
  })
  
  // Send message to all workers
  Object.values(cluster.workers).forEach(worker => {
    worker.send('Hello from master')
  })
  
} else {
  // Workers share the same TCP connection
  const server = http.createServer((req, res) => {
    res.writeHead(200)
    res.end(`Process ${process.pid} handled the request\n`)
  })
  
  server.listen(3000, () => {
    console.log(`Worker ${process.pid} started`)
  })
  
  // Receive messages from master
  process.on('message', (msg) => {
    console.log(`Worker ${process.pid} received:`, msg)
  })
}
```

**Cluster vs Worker Threads:**

```
┌────────────────────────────────────────────┐
│  Cluster Module                            │
├────────────────────────────────────────────┤
│  ✅ Separate processes (isolated memory)  │
│  ✅ Good for I/O-heavy workloads           │
│  ✅ Auto-restart on crash                  │
│  ❌ Higher memory usage                    │
│  ❌ IPC overhead                           │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│  Worker Threads                            │
├────────────────────────────────────────────┤
│  ✅ Shared memory (faster communication)   │
│  ✅ Good for CPU-heavy workloads           │
│  ✅ Lower memory usage                     │
│  ❌ Crash affects main thread              │
│  ❌ Limited in older Node versions         │
└────────────────────────────────────────────┘
```

### 10. Process & OS Information

```javascript
const os = require('os')
const process = require('process')

// OS Information
console.log('Platform:', os.platform())  // 'darwin', 'linux', 'win32'
console.log('CPU Architecture:', os.arch())  // 'x64', 'arm64'
console.log('CPUs:', os.cpus().length)
console.log('Total Memory:', os.totalmem() / 1024 / 1024 / 1024, 'GB')
console.log('Free Memory:', os.freemem() / 1024 / 1024 / 1024, 'GB')
console.log('Uptime:', os.uptime(), 'seconds')
console.log('Home Directory:', os.homedir())

// Process Information
console.log('Process ID:', process.pid)
console.log('Node Version:', process.version)
console.log('Current Directory:', process.cwd())
console.log('Memory Usage:', process.memoryUsage())
console.log('CPU Usage:', process.cpuUsage())
console.log('Uptime:', process.uptime(), 'seconds')

// Environment Variables
console.log('NODE_ENV:', process.env.NODE_ENV)

// Exit process
// process.exit(0)  // Success
// process.exit(1)  // Error

// Handle signals
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully...')
  server.close(() => {
    console.log('Server closed')
    process.exit(0)
  })
})
```

---

## ⚡ Express.js Framework {#express}

### What is Express?

Express is a minimal and flexible Node.js web application framework.

```
┌──────────────────────────────────────────────────────────────┐
│              Raw Node.js HTTP Server                         │
├──────────────────────────────────────────────────────────────┤
│  • Verbose code (100+ lines for simple API)                  │
│  • Manual routing with if/else                               │
│  • Manual request parsing                                    │
│  • No middleware support                                     │
│  • Complex error handling                                    │
└──────────────────────────────────────────────────────────────┘
                            ⬇️  vs  ⬇️
┌──────────────────────────────────────────────────────────────┐
│              Express Framework  ✨                           │
├──────────────────────────────────────────────────────────────┤
│  ✅ Concise code (20 lines for same API)                    │
│  ✅ Clean routing (app.get, app.post, etc.)                 │
│  ✅ Automatic parsing (JSON, URL-encoded)                   │
│  ✅ Rich middleware ecosystem (1000+ packages)              │
│  ✅ Built-in error handling                                 │
└──────────────────────────────────────────────────────────────┘

📊 Express Request-Response Cycle:
┌─────────────────────────────────────────────────────────────────┐
│                    Client Request                               │
│                (HTTP GET /api/users)                            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────▼────────────┐
                │   Express App           │
                └────────────┬────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼──────┐   ┌─────────▼────────┐   ┌─────▼──────┐
│ Middleware 1 │──▶│  Middleware 2    │──▶│ Route      │
│              │   │                  │   │ Handler    │
│ • Logging    │   │ • Authentication │   │            │
│ • CORS       │   │ • Body Parsing   │   │ Execute    │
└──────────────┘   └──────────────────┘   │ Logic      │
                                          └─────┬──────┘
                                                │
                             ┌──────────────────▼──────────────────┐
                             │      Response to Client             │
                             │  (JSON, HTML, File, Error, etc.)    │
                             └─────────────────────────────────────┘
```

### Basic Express Server

```javascript
// app.js
const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to parse JSON
app.use(express.json());

// Simple route
app.get('/', (req, res) => {
  res.send('Hello Express!');
});

// JSON response
app.get('/api/users', (req, res) => {
  res.json({
    users: [
      { id: 1, name: 'John' },
      { id: 2, name: 'Jane' }
    ]
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

### Routing

**Basic Routes**

```javascript
// GET request
app.get('/users', (req, res) => {
  res.send('Get all users');
});

// POST request
app.post('/users', (req, res) => {
  res.send('Create user');
});

// PUT request
app.put('/users/:id', (req, res) => {
  res.send(`Update user ${req.params.id}`);
});

// DELETE request
app.delete('/users/:id', (req, res) => {
  res.send(`Delete user ${req.params.id}`);
});
```

**Route Parameters**

```javascript
// URL: /users/123
app.get('/users/:id', (req, res) => {
  const userId = req.params.id;
  res.send(`User ID: ${userId}`);
});

// Multiple parameters
// URL: /users/123/posts/456
app.get('/users/:userId/posts/:postId', (req, res) => {
  const { userId, postId } = req.params;
  res.json({ userId, postId });
});
```

**Query Parameters**

```javascript
// URL: /search?query=node&limit=10
app.get('/search', (req, res) => {
  const { query, limit } = req.query;
  res.json({
    searchQuery: query,
    limit: limit || 20
  });
});
```

**Router (Modular Routes)**

```javascript
// routes/users.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.send('Get all users');
});

router.get('/:id', (req, res) => {
  res.send(`Get user ${req.params.id}`);
});

router.post('/', (req, res) => {
  res.send('Create user');
});

module.exports = router;

// app.js
const userRoutes = require('./routes/users');
app.use('/api/users', userRoutes);
```

---

## 🔌 RESTful API Development {#rest-api}

### REST Principles

```
┌──────────────────────────────────────────┐
│  Resource: /api/users                    │
├──────────────────────────────────────────┤
│  GET     /api/users       → List all     │
│  GET     /api/users/:id   → Get one      │
│  POST    /api/users       → Create       │
│  PUT     /api/users/:id   → Update (full)│
│  PATCH   /api/users/:id   → Update (part)│
│  DELETE  /api/users/:id   → Delete       │
└──────────────────────────────────────────┘
```

### Complete CRUD API Example

```javascript
// controllers/userController.js
const users = [
  { id: 1, name: 'John Doe', email: 'john@example.com' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
];

// GET all users
exports.getAllUsers = (req, res) => {
  res.json({
    success: true,
    data: users
  });
};

// GET single user
exports.getUser = (req, res) => {
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
};

// CREATE user
exports.createUser = (req, res) => {
  const { name, email } = req.body;
  
  // Validation
  if (!name || !email) {
    return res.status(400).json({
      success: false,
      error: 'Name and email are required'
    });
  }
  
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
};

// UPDATE user
exports.updateUser = (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  
  if (!user) {
    return res.status(404).json({
      success: false,
      error: 'User not found'
    });
  }
  
  const { name, email } = req.body;
  if (name) user.name = name;
  if (email) user.email = email;
  
  res.json({
    success: true,
    data: user
  });
};

// DELETE user
exports.deleteUser = (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  
  if (index === -1) {
    return res.status(404).json({
      success: false,
      error: 'User not found'
    });
  }
  
  users.splice(index, 1);
  
  res.json({
    success: true,
    message: 'User deleted successfully'
  });
};
```

```javascript
// routes/users.js
const express = require('express');
const router = express.Router();
const {
  getAllUsers,
  getUser,
  createUser,
  updateUser,
  deleteUser
} = require('../controllers/userController');

router.route('/')
  .get(getAllUsers)
  .post(createUser);

router.route('/:id')
  .get(getUser)
  .put(updateUser)
  .delete(deleteUser);

module.exports = router;
```

### Request Validation

```javascript
const { body, validationResult } = require('express-validator');

// Validation middleware
const validateUser = [
  body('name')
    .trim()
    .isLength({ min: 3 })
    .withMessage('Name must be at least 3 characters'),
  body('email')
    .isEmail()
    .withMessage('Must be a valid email'),
  body('age')
    .optional()
    .isInt({ min: 18 })
    .withMessage('Must be 18 or older')
];

// Use in route
router.post('/', validateUser, (req, res) => {
  const errors = validationResult(req);
  
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      errors: errors.array()
    });
  }
  
  // Proceed with creation
  createUser(req, res);
});
```

---

## 🔀 Middleware & Error Handling {#middleware}

### What is Middleware?

**Middleware** functions have access to `req`, `res`, and `next()`.

```
┌────────────────────────────────────────────────────────────────────┐
│                    Middleware Chain Flow                           │
└────────────────────────────────────────────────────────────────────┘

  Client Request
       │
       ▼
┌──────────────────┐
│  Middleware 1    │  ← app.use(logger)
│  (Logger)        │
│                  │
│  • Log request   │
│  • next()────────┼─────────┐
└──────────────────┘         │
                             ▼
                    ┌──────────────────┐
                    │  Middleware 2    │  ← app.use(cors())
                    │  (CORS)          │
                    │                  │
                    │  • Set headers   │
                    │  • next()────────┼─────────┐
                    └──────────────────┘         │
                                                 ▼
                                        ┌──────────────────┐
                                        │  Middleware 3    │  ← app.use(auth)
                                        │  (Auth)          │
                                        │                  │
                                        │  • Verify token  │
                                        │  • next()────────┼────┐
                                        └──────────────────┘    │
                                                                ▼
                                                       ┌──────────────────┐
                                                       │  Route Handler   │
                                                       │                  │
                                                       │  • Process req   │
                                                       │  • res.json()    │
                                                       └────────┬─────────┘
                                                                │
                                                                ▼
                                                          Client Response

🔴 Error Handling:
   Any middleware can call next(error) to skip to error handler

┌──────────────────┐
│  Middleware      │
│  if (error) {    │
│    next(error) ──┼─────────┐
│  }               │         │
└──────────────────┘         │
                             ▼
                    ┌─────────────────────┐
                    │  Error Handler      │  ← app.use((err, req, res, next))
                    │                     │
                    │  • Log error        │
                    │  • Send response    │
                    └─────────────────────┘
                             │
                             ▼
                       Error Response


📊 Middleware Types:

┌─────────────────────────────────────────────────────────┐
│                Application-Level                        │
│  app.use() - Applies to all routes                     │
│  app.use('/api', middleware) - Applies to /api/*       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Router-Level                             │
│  router.use() - Applies to specific router             │
│  router.get('/users', auth, handler)                    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Error-Handling                           │
│  app.use((err, req, res, next) => {})                  │
│  Must have 4 parameters (err, req, res, next)          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Built-in                                 │
│  express.json(), express.static(), etc.                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Third-Party                              │
│  cors, helmet, morgan, compression, etc.                │
└─────────────────────────────────────────────────────────┘
```

### Built-in Middleware

```javascript
const express = require('express');
const app = express();

// Parse JSON bodies
app.use(express.json());

// Parse URL-encoded bodies
app.use(express.urlencoded({ extended: true }));

// Serve static files
app.use(express.static('public'));
```

### Custom Middleware

```javascript
// Logger middleware
const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url} - ${new Date().toISOString()}`);
  next(); // Pass control to next middleware
};

// Auth middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization;
  
  if (!token) {
    return res.status(401).json({
      success: false,
      error: 'No token provided'
    });
  }
  
  // Verify token (simplified)
  if (token === 'valid-token') {
    req.user = { id: 1, name: 'John' };
    next();
  } else {
    return res.status(401).json({
      success: false,
      error: 'Invalid token'
    });
  }
};

// Use middleware
app.use(logger); // Apply to all routes
app.get('/protected', authenticate, (req, res) => {
  res.json({ message: `Hello ${req.user.name}` });
});
```

### Third-Party Middleware

```javascript
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const compression = require('compression');

// CORS - Allow cross-origin requests
app.use(cors());

// Helmet - Security headers
app.use(helmet());

// Morgan - HTTP request logger
app.use(morgan('dev'));

// Compression - Gzip compression
app.use(compression());
```

### Error Handling

```javascript
// Custom error class
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}

// Async error wrapper
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Use in routes
app.get('/users/:id', asyncHandler(async (req, res, next) => {
  const user = await User.findById(req.params.id);
  
  if (!user) {
    throw new AppError('User not found', 404);
  }
  
  res.json({ success: true, data: user });
}));

// Global error handler (must be last!)
app.use((err, req, res, next) => {
  err.statusCode = err.statusCode || 500;
  err.message = err.message || 'Internal Server Error';
  
  // Development error
  if (process.env.NODE_ENV === 'development') {
    res.status(err.statusCode).json({
      success: false,
      error: err.message,
      stack: err.stack
    });
  } else {
    // Production error
    res.status(err.statusCode).json({
      success: false,
      error: err.message
    });
  }
});
```

---

## 💾 Database Integration {#database}

### MongoDB with Mongoose

```
┌─────────────────────────────────────────────────────────────────┐
│                  Node.js Application Architecture               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                         Frontend                                │
│     (React, Vue, Angular, Mobile App, etc.)                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               │ HTTP Requests
                               │ (JSON Data)
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                    Express.js Server                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐│
│  │  Middleware    │───▶│    Routes      │───▶│  Controllers   ││
│  │                │    │                │    │                ││
│  │ • CORS         │    │ • /api/users   │    │ • Business     ││
│  │ • Auth         │    │ • /api/posts   │    │   Logic        ││
│  │ • Logging      │    │ • /api/orders  │    │                ││
│  └────────────────┘    └────────────────┘    └────┬───────────┘│
│                                                     │            │
└─────────────────────────────────────────────────────┼────────────┘
                                                      │
                                                      │ Mongoose ODM
                                                      │ (Object Data Modeling)
                                                      ▼
┌──────────────────────────────────────────────────────────────────┐
│                       MongoDB Database                           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │ Collection  │  │ Collection  │  │ Collection  │            │
│  │   users     │  │   posts     │  │   orders    │            │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤            │
│  │ { doc 1 }   │  │ { doc 1 }   │  │ { doc 1 }   │            │
│  │ { doc 2 }   │  │ { doc 2 }   │  │ { doc 2 }   │            │
│  │ { doc 3 }   │  │ { doc 3 }   │  │ { doc 3 }   │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘


📊 Mongoose Schema & Model Flow:

┌─────────────────────────────────────────────────────────────────┐
│  1. Define Schema (Structure + Validation)                      │
└─────────────────────────────────────────────────────────────────┘
   const userSchema = new mongoose.Schema({
     name: String,
     email: { type: String, unique: true },
     age: Number
   })
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. Add Methods & Middleware (Hooks)                            │
└─────────────────────────────────────────────────────────────────┘
   userSchema.pre('save', async function() {
     // Hash password before saving
   })
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. Create Model (Compile schema into model)                    │
└─────────────────────────────────────────────────────────────────┘
   const User = mongoose.model('User', userSchema)
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. Use Model (CRUD Operations)                                 │
└─────────────────────────────────────────────────────────────────┘
   • User.create()     → Create new document
   • User.find()       → Read documents
   • User.findById()   → Read single document
   • User.updateOne()  → Update document
   • User.deleteOne()  → Delete document


🔗 Relationships in MongoDB:

┌────────────────────────────────────────────────────────────────┐
│  Embedding (1-to-Few)  - Store related data together           │
└────────────────────────────────────────────────────────────────┘
{
  _id: 1,
  name: "John",
  addresses: [                    ← Embedded documents
    { street: "123 Main", city: "NYC" },
    { street: "456 Oak", city: "LA" }
  ]
}

┌────────────────────────────────────────────────────────────────┐
│  Referencing (1-to-Many) - Store references                    │
└────────────────────────────────────────────────────────────────┘
// User document
{
  _id: ObjectId("123"),
  name: "John"
}

// Post documents
{
  _id: ObjectId("456"),
  title: "My Post",
  author: ObjectId("123")    ← Reference to User
}
```

**Install**

```bash
npm install mongoose
```

**Connection**

```javascript
// config/database.js
const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  }
};

module.exports = connectDB;
```

**Model Definition**

```javascript
// models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: 3
  },
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    match: [/^\S+@\S+\.\S+$/, 'Please enter a valid email']
  },
  password: {
    type: String,
    required: [true, 'Password is required'],
    minlength: 6,
    select: false // Don't return password by default
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user'
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  
  const bcrypt = require('bcryptjs');
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

// Instance method
userSchema.methods.comparePassword = async function(candidatePassword) {
  const bcrypt = require('bcryptjs');
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);
```

**CRUD Operations**

```javascript
// controllers/userController.js
const User = require('../models/User');

// Create
exports.createUser = async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json({
      success: true,
      data: user
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      error: error.message
    });
  }
};

// Read all
exports.getAllUsers = async (req, res) => {
  try {
    const users = await User.find();
    res.json({
      success: true,
      count: users.length,
      data: users
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Read one
exports.getUser = async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    
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
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Update
exports.updateUser = async (req, res) => {
  try {
    const user = await User.findByIdAndUpdate(
      req.params.id,
      req.body,
      {
        new: true, // Return updated document
        runValidators: true // Run model validators
      }
    );
    
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
  } catch (error) {
    res.status(400).json({
      success: false,
      error: error.message
    });
  }
};

// Delete
exports.deleteUser = async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    
    if (!user) {
      return res.status(404).json({
        success: false,
        error: 'User not found'
      });
    }
    
    res.json({
      success: true,
      message: 'User deleted successfully'
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};
```

### Advanced Queries

```javascript
// Pagination
exports.getUsers = async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const skip = (page - 1) * limit;
  
  const users = await User.find()
    .skip(skip)
    .limit(limit)
    .sort({ createdAt: -1 });
  
  const total = await User.countDocuments();
  
  res.json({
    success: true,
    data: users,
    pagination: {
      page,
      limit,
      total,
      pages: Math.ceil(total / limit)
    }
  });
};

// Search & Filter
exports.searchUsers = async (req, res) => {
  const { name, email, role } = req.query;
  
  const query = {};
  
  if (name) {
    query.name = { $regex: name, $options: 'i' }; // Case-insensitive
  }
  
  if (email) {
    query.email = { $regex: email, $options: 'i' };
  }
  
  if (role) {
    query.role = role;
  }
  
  const users = await User.find(query);
  
  res.json({
    success: true,
    count: users.length,
    data: users
  });
};
```

---

## 🔐 Authentication & Authorization {#auth}

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           Authentication vs Authorization                                   │
└─────────────────────────────────────────────────────────────────────────────┘

Authentication: "Who are you?" - Verify identity
Authorization:  "What can you do?" - Check permissions

┌──────────────────────────────────────────────────────────────┐
│ User Login Flow (Authentication):                            │
│                                                              │
│ 1. Client                                                    │
│    │ POST /api/auth/login                                    │
│    │ {email: "user@test.com", password: "secret123"}        │
│    ▼                                                         │
│ 2. Server                                                    │
│    │ Find user by email                                      │
│    │ Compare hashed password                                 │
│    │                                                          │
│    │ ✅ Match → Generate JWT token                           │
│    │ ❌ No match → 401 Unauthorized                          │
│    ▼                                                         │
│ 3. Response                                                  │
│    {                                                         │
│      token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",      │
│      user: {id: 1, name: "John", email: "user@test.com"}    │
│    }                                                         │
│                                                              │
│ 4. Client stores token (localStorage/cookie)                │
│                                                              │
│ 5. Client includes token in future requests:                │
│    GET /api/profile                                          │
│    Headers: {                                                │
│      Authorization: "Bearer eyJhbGciOiJIUzI1NiIs..."        │
│    }                                                         │
└──────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│            JWT (JSON Web Token) Structure & Flow                            │
└─────────────────────────────────────────────────────────────────────────────┘

JWT Token Structure:
┌─────────────────────────────────────────────────────────────┐
│ eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9                       │  Header
│ .                                                            │
│ eyJpZCI6IjEyMyIsImlhdCI6MTYxNjIzOTAyMn0                     │  Payload
│ .                                                            │
│ SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c                 │  Signature
└─────────────────────────────────────────────────────────────┘
    │                       │                       │
    ▼                       ▼                       ▼
┌──────────┐        ┌──────────┐          ┌──────────┐
│  Header  │        │ Payload  │          │Signature │
│          │        │          │          │          │
│ {        │        │ {        │          │ HMACSHA256│
│  "alg":  │        │  "id":   │          │ (         │
│  "HS256",│        │  "123",  │          │  base64   │
│  "typ":  │        │  "iat":  │          │  Header + │
│  "JWT"   │        │  161623  │          │  Payload, │
│ }        │        │ }        │          │  secret   │
└──────────┘        └──────────┘          │ )         │
                                          └──────────┘

JWT Authentication Flow:
┌──────────────────────────────────────────────────────────────┐
│ 1. User Registers/Logs In                                    │
│    ┌────────┐                    ┌────────┐                  │
│    │ Client │ POST /api/login    │ Server │                  │
│    │        │──────────────────▶ │        │                  │
│    │        │ {email, password}  │        │                  │
│    └────────┘                    └────────┘                  │
│                                       │                       │
│                                       │ 1. Validate           │
│                                       │ 2. Hash password      │
│                                       │ 3. Compare hash       │
│                                       │ 4. Generate JWT       │
│                                       ▼                       │
│    ┌────────┐                    ┌────────┐                  │
│    │ Client │◀──────────────────  │ Server │                  │
│    │        │ {token, user}      │        │                  │
│    │        │                    │        │                  │
│    │ Store  │                    └────────┘                  │
│    │ in     │                                                │
│    │ Storage│                                                │
│    └────────┘                                                │
│                                                              │
│ 2. Access Protected Route                                   │
│    ┌────────┐                    ┌────────┐                  │
│    │ Client │ GET /api/profile   │ Server │                  │
│    │        │──────────────────▶ │        │                  │
│    │        │ Header:            │        │                  │
│    │        │ Authorization:     │        │                  │
│    │        │ Bearer <token>     │        │                  │
│    └────────┘                    └────────┘                  │
│                                       │                       │
│                                       │ Middleware:           │
│                                       │ 1. Extract token      │
│                                       │ 2. Verify signature   │
│                                       │ 3. Decode payload     │
│                                       │ 4. Check expiry       │
│                                       ▼                       │
│                                  ✅ Valid                     │
│                                       │                       │
│                                       │ req.user = decoded    │
│                                       │ Call next()           │
│                                       ▼                       │
│    ┌────────┐                    ┌────────┐                  │
│    │ Client │◀──────────────────  │ Server │                  │
│    │        │ {profile data}     │        │                  │
│    └────────┘                    └────────┘                  │
│                                                              │
│                                  ❌ Invalid                   │
│                                       │                       │
│                                       │ 401 Unauthorized      │
│                                       ▼                       │
│    ┌────────┐                    ┌────────┐                  │
│    │ Client │◀──────────────────  │ Server │                  │
│    │        │ {error: "Invalid"} │        │                  │
│    └────────┘                    └────────┘                  │
└──────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│          Role-Based Authorization (RBAC)                                    │
└─────────────────────────────────────────────────────────────────────────────┘

User Roles & Permissions:
┌────────────────────────────────────────────────────────────┐
│ User: {                                                    │
│   id: 123,                                                 │
│   email: "admin@test.com",                                 │
│   role: "admin"    ← Role determines permissions           │
│ }                                                          │
└────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│ Role Permission Matrix:                                         │
│                                                                 │
│ ┌────────────┬─────────┬──────────┬─────────┬────────────┐     │
│ │   Action   │  User   │ Moderator│  Admin  │ SuperAdmin │     │
│ ├────────────┼─────────┼──────────┼─────────┼────────────┤     │
│ │ Read Posts │   ✅    │    ✅    │   ✅    │     ✅     │     │
│ │Create Posts│   ✅    │    ✅    │   ✅    │     ✅     │     │
│ │Delete Own  │   ✅    │    ✅    │   ✅    │     ✅     │     │
│ │Delete Any  │   ❌    │    ✅    │   ✅    │     ✅     │     │
│ │ Ban Users  │   ❌    │    ✅    │   ✅    │     ✅     │     │
│ │Manage Roles│   ❌    │    ❌    │   ❌    │     ✅     │     │
│ │Config Sys  │   ❌    │    ❌    │   ❌    │     ✅     │     │
│ └────────────┴─────────┴──────────┴─────────┴────────────┘     │
└─────────────────────────────────────────────────────────────────┘

Authorization Middleware Flow:
┌──────────────────────────────────────────────────────────────┐
│ Request: DELETE /api/posts/456                               │
│          Authorization: Bearer <token>                       │
│                                                              │
│ 1. Authentication Middleware                                 │
│    ├─ Extract token                                          │
│    ├─ Verify signature                                       │
│    ├─ Decode: {id: 123, role: "user"}                       │
│    └─ req.user = {id: 123, role: "user"}                    │
│                                                              │
│ 2. Authorization Middleware - checkRole('admin')             │
│    ├─ Check req.user.role                                    │
│    │                                                          │
│    ├─ req.user.role = "user"                                │
│    ├─ Required role = "admin"                               │
│    │                                                          │
│    └─ ❌ "user" !== "admin"                                  │
│                                                              │
│ 3. Response: 403 Forbidden                                   │
│    {                                                         │
│      error: "Access denied. Admin role required"            │
│    }                                                         │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Resource-Based Authorization:                                │
│                                                              │
│ Request: DELETE /api/posts/456                               │
│          User: {id: 123, role: "user"}                      │
│                                                              │
│ 1. Check ownership                                           │
│    ├─ Find post by ID                                        │
│    ├─ Post: {id: 456, author: 123, title: "..."}           │
│    │                                                          │
│    ├─ req.user.id === post.author?                          │
│    └─ ✅ 123 === 123 → Authorized (owns resource)           │
│                                                              │
│ 2. Process deletion                                          │
│                                                              │
│ 3. Response: 200 OK                                          │
└──────────────────────────────────────────────────────────────┘

Session vs Token Comparison:
┌─────────────────────────────────────────────────────────────┐
│ Session-Based (Stateful):                                   │
│                                                             │
│ Client              Server                Database          │
│   │                   │                      │              │
│   │ Login             │                      │              │
│   │──────────────────▶│                      │              │
│   │                   │ Create session       │              │
│   │                   │─────────────────────▶│              │
│   │                   │ Session ID: abc123   │              │
│   │◀──────────────────│                      │              │
│   │ Cookie: abc123    │                      │              │
│   │                   │                      │              │
│   │ Request + Cookie  │                      │              │
│   │──────────────────▶│                      │              │
│   │                   │ Lookup session       │              │
│   │                   │─────────────────────▶│              │
│   │                   │ Session data         │              │
│   │                   │◀─────────────────────│              │
│   │◀──────────────────│                      │              │
│   │ Response          │                      │              │
│                                                             │
│ ✅ Can revoke sessions easily                               │
│ ❌ Server must store session data                           │
│ ❌ Harder to scale (session data in memory/database)        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Token-Based / JWT (Stateless):                             │
│                                                             │
│ Client              Server                                  │
│   │                   │                                     │
│   │ Login             │                                     │
│   │──────────────────▶│                                     │
│   │                   │ Generate JWT                        │
│   │                   │ (no database storage)               │
│   │◀──────────────────│                                     │
│   │ Token: eyJhbG...  │                                     │
│   │                   │                                     │
│   │ Request + Token   │                                     │
│   │──────────────────▶│                                     │
│   │                   │ Verify signature                    │
│   │                   │ (no database lookup)                │
│   │◀──────────────────│                                     │
│   │ Response          │                                     │
│                                                             │
│ ✅ Stateless (no server storage needed)                     │
│ ✅ Easily scalable (any server can verify)                  │
│ ✅ Works across domains (mobile apps, SPAs)                 │
│ ❌ Hard to revoke (token valid until expiry)                │
│ ❌ Larger payload (token sent with every request)           │
└─────────────────────────────────────────────────────────────┘
```

### JWT Authentication

**Install**

```bash
npm install jsonwebtoken bcryptjs
```

**Generate Token**

```javascript
// utils/generateToken.js
const jwt = require('jsonwebtoken');

const generateToken = (userId) => {
  return jwt.sign(
    { id: userId },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
};

module.exports = generateToken;
```

**Register**

```javascript
// controllers/authController.js
const User = require('../models/User');
const generateToken = require('../utils/generateToken');

exports.register = async (req, res) => {
  try {
    const { name, email, password } = req.body;
    
    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({
        success: false,
        error: 'Email already registered'
      });
    }
    
    // Create user
    const user = await User.create({
      name,
      email,
      password
    });
    
    // Generate token
    const token = generateToken(user._id);
    
    res.status(201).json({
      success: true,
      data: {
        user: {
          id: user._id,
          name: user.name,
          email: user.email
        },
        token
      }
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      error: error.message
    });
  }
};
```

**Login**

```javascript
exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;
    
    // Validate input
    if (!email || !password) {
      return res.status(400).json({
        success: false,
        error: 'Please provide email and password'
      });
    }
    
    // Find user and include password
    const user = await User.findOne({ email }).select('+password');
    
    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'Invalid credentials'
      });
    }
    
    // Check password
    const isPasswordCorrect = await user.comparePassword(password);
    
    if (!isPasswordCorrect) {
      return res.status(401).json({
        success: false,
        error: 'Invalid credentials'
      });
    }
    
    // Generate token
    const token = generateToken(user._id);
    
    res.json({
      success: true,
      data: {
        user: {
          id: user._id,
          name: user.name,
          email: user.email
        },
        token
      }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};
```

**Auth Middleware**

```javascript
// middleware/auth.js
const jwt = require('jsonwebtoken');
const User = require('../models/User');

exports.protect = async (req, res, next) => {
  try {
    let token;
    
    // Get token from header
    if (req.headers.authorization && 
        req.headers.authorization.startsWith('Bearer')) {
      token = req.headers.authorization.split(' ')[1];
    }
    
    if (!token) {
      return res.status(401).json({
        success: false,
        error: 'Not authorized to access this route'
      });
    }
    
    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    
    // Get user from token
    req.user = await User.findById(decoded.id);
    
    if (!req.user) {
      return res.status(401).json({
        success: false,
        error: 'User not found'
      });
    }
    
    next();
  } catch (error) {
    return res.status(401).json({
      success: false,
      error: 'Not authorized'
    });
  }
};

// Role-based authorization
exports.authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        success: false,
        error: `User role ${req.user.role} is not authorized`
      });
    }
    next();
  };
};
```

**Protected Routes**

```javascript
// routes/users.js
const { protect, authorize } = require('../middleware/auth');

router.get('/profile', protect, getUserProfile);
router.delete('/:id', protect, authorize('admin'), deleteUser);
```

---

## 🎨 GraphQL Basics {#graphql}

**What is GraphQL?**

GraphQL is a query language for APIs that allows clients to request exactly the data they need. Unlike REST where you get fixed data structures, GraphQL lets clients specify the exact fields they want.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     GraphQL vs REST Architecture                            │
└─────────────────────────────────────────────────────────────────────────────┘

REST API (Multiple Endpoints):
┌──────────────────────────────────────────────────────────────────────────┐
│                           Client Application                             │
└──────────────────────────────────────────────────────────────────────────┘
              │                  │                   │
              │ GET /users/1     │ GET /posts?       │ GET /comments?
              │                  │ userId=1          │ postId=5
              ▼                  ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │/users/:id    │   │/posts        │   │/comments     │
    │Endpoint      │   │Endpoint      │   │Endpoint      │
    └──────────────┘   └──────────────┘   └──────────────┘
              │                  │                   │
              ▼                  ▼                   ▼
    ┌────────────────────────────────────────────────────────┐
    │              Backend Server (Node.js)                  │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
    │  │  Users   │  │  Posts   │  │ Comments │            │
    │  │Controller│  │Controller│  │Controller│            │
    │  └──────────┘  └──────────┘  └──────────┘            │
    └────────────────────────────────────────────────────────┘
              │                  │                   │
              ▼                  ▼                   ▼
         Database           Database            Database
    
    Problems:
    ❌ 3 network requests needed
    ❌ Over-fetching (gets all user fields when only need name)
    ❌ Under-fetching (need multiple requests for related data)
    ❌ Fixed response structure

GraphQL API (Single Endpoint):
┌──────────────────────────────────────────────────────────────────────────┐
│                           Client Application                             │
│  query {                                                                 │
│    user(id: 1) {                                                        │
│      name                    ← Request only needed fields               │
│      posts {                                                            │
│        title                                                            │
│        comments { text }                                                │
│      }                                                                  │
│    }                                                                    │
│  }                                                                      │
└──────────────────────────────────────────────────────────────────────────┘
              │
              │ POST /graphql (single request)
              ▼
    ┌────────────────────────────────────────────────────────┐
    │            GraphQL Server (Apollo)                     │
    │                                                        │
    │  ┌──────────────────────────────────────────┐         │
    │  │   Schema (Type Definitions)              │         │
    │  │   type User { id, name, posts }          │         │
    │  │   type Post { id, title, comments }      │         │
    │  │   type Comment { id, text }              │         │
    │  └──────────────────────────────────────────┘         │
    │               ▼                                        │
    │  ┌──────────────────────────────────────────┐         │
    │  │   Resolvers (Data Fetching Logic)        │         │
    │  │   Query.user()                           │         │
    │  │   User.posts()                           │         │
    │  │   Post.comments()                        │         │
    │  └──────────────────────────────────────────┘         │
    └────────────────────────────────────────────────────────┘
              │
              ▼
         Database (optimized query)
    
    Benefits:
    ✅ Single request for all data
    ✅ No over-fetching (get only name, title, text)
    ✅ No under-fetching (nested data in one query)
    ✅ Client defines response structure

┌─────────────────────────────────────────────────────────────────────────────┐
│                     GraphQL Request Flow                                    │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: Client sends GraphQL query
┌──────────────────────────────────┐
│ POST /graphql                    │
│ {                                │
│   query: "                       │
│     query GetUser {              │
│       user(id: 1) {              │
│         name                     │
│         email                    │
│         posts { title }          │
│       }                          │
│     }                            │
│   "                              │
│ }                                │
└──────────────────────────────────┘
                │
                ▼
Step 2: GraphQL Server parses and validates
┌──────────────────────────────────┐
│ Parse Query                      │
│   ↓                              │
│ Validate against Schema          │
│   ↓                              │
│ Execute Resolvers                │
└──────────────────────────────────┘
                │
                ▼
Step 3: Resolvers fetch data (parallel when possible)
┌────────────────────────────────────────────┐
│ Query.user(id: 1)                         │
│   ↓                                        │
│ Find user in database                     │
│   ↓                                        │
│ User.posts(parent: user)  ← Nested        │
│   ↓                                        │
│ Find posts where author = user.id         │
└────────────────────────────────────────────┘
                │
                ▼
Step 4: Return shaped response
┌──────────────────────────────────┐
│ {                                │
│   "data": {                      │
│     "user": {                    │
│       "name": "John",            │
│       "email": "john@test.com",  │
│       "posts": [                 │
│         { "title": "Post 1" },   │
│         { "title": "Post 2" }    │
│       ]                          │
│     }                            │
│   }                              │
│ }                                │
└──────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                     GraphQL Schema & Resolvers                              │
└─────────────────────────────────────────────────────────────────────────────┘

Schema (Contract - What can be queried):
┌─────────────────────────────────────────────────────────────┐
│  type User {                                                │
│    id: ID!              ← ! means required                  │
│    name: String!                                            │
│    email: String!                                           │
│    posts: [Post!]!      ← Array of Posts                    │
│  }                                                          │
│                                                             │
│  type Query {                                               │
│    user(id: ID!): User  ← Query with parameter             │
│    users: [User!]!                                          │
│  }                                                          │
│                                                             │
│  type Mutation {                                            │
│    createUser(name: String!, email: String!): User!         │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼ Maps to
┌─────────────────────────────────────────────────────────────┐
│  Resolvers (Implementation - How to fetch):                 │
│                                                             │
│  const resolvers = {                                        │
│    Query: {                                                 │
│      user: (parent, args, context) => {                     │
│        return User.findById(args.id)                        │
│      }                                                      │
│    },                                                       │
│                                                             │
│    User: {  ← Field-level resolver                          │
│      posts: (parent) => {                                   │
│        return Post.find({ authorId: parent.id })            │
│      }                                                      │
│    },                                                       │
│                                                             │
│    Mutation: {                                              │
│      createUser: (_, { name, email }) => {                  │
│        return User.create({ name, email })                  │
│      }                                                      │
│    }                                                        │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘

Resolver Function Signature:
fieldName: (parent, args, context, info) => { ... }
           ▲       ▲      ▲         ▲
           │       │      │         └─ Query metadata
           │       │      └─ Shared context (auth, db, etc)
           │       └─ Arguments passed to field
           └─ Result from parent resolver
```

**Why Use GraphQL?**

- **No Over-fetching**: Get only what you need
- **No Under-fetching**: Get all data in one request (no multiple REST calls)
- **Strongly Typed**: Schema defines all types and operations
- **Self-Documenting**: Schema serves as documentation
- **Real-time with Subscriptions**: WebSocket-based real-time updates

**GraphQL vs REST:**

| Feature | REST | GraphQL |
|---------|------|---------|
| Endpoints | Multiple (/users, /posts, /comments) | Single (/graphql) |
| Data Fetching | Fixed response structure | Client specifies fields |
| Over-fetching | Common (get all fields) | None (request what you need) |
| Under-fetching | Multiple requests needed | Single request |
| Versioning | URL versioning (/v1/, /v2/) | Schema evolution |

**When to Use GraphQL:**
- Mobile apps (minimize data transfer)
- Complex data requirements
- Rapid frontend development
- Real-time features needed
- Multiple clients with different data needs

**Setup with Express**

```bash
npm install apollo-server-express graphql
```

**Basic GraphQL Server**

```javascript
const { ApolloServer, gql } = require('apollo-server-express')
const express = require('express')

// Type definitions (schema)
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }
  
  type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
  }
  
  type Query {
    users: [User!]!
    user(id: ID!): User
    posts: [Post!]!
  }
  
  type Mutation {
    createUser(name: String!, email: String!): User!
    createPost(title: String!, content: String!, authorId: ID!): Post!
  }
`

// Resolvers (how to fetch data)
const resolvers = {
  Query: {
    users: async () => await User.find(),
    user: async (_, { id }) => await User.findById(id),
    posts: async () => await Post.find()
  },
  
  Mutation: {
    createUser: async (_, { name, email }) => {
      const user = new User({ name, email })
      await user.save()
      return user
    },
    createPost: async (_, { title, content, authorId }) => {
      const post = new Post({ title, content, author: authorId })
      await post.save()
      return post
    }
  },
  
  // Nested resolvers
  User: {
    posts: async (parent) => await Post.find({ author: parent.id })
  },
  Post: {
    author: async (parent) => await User.findById(parent.author)
  }
}

// Create Apollo Server
const server = new ApolloServer({ typeDefs, resolvers })

const app = express()
await server.start()
server.applyMiddleware({ app })

app.listen(4000, () => {
  console.log(`Server ready at http://localhost:4000${server.graphqlPath}`)
})
```

**Example Queries**

```graphql
# Get specific user fields
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}

# Create user
mutation {
  createUser(name: "John Doe", email: "john@example.com") {
    id
    name
  }
}
```

---

## 🔄 API Versioning {#versioning}

**What is API Versioning?**

API versioning allows you to make breaking changes while maintaining backward compatibility with existing clients.

**Why Version APIs?**

- **Breaking Changes**: Modify data structures without breaking existing apps
- **Gradual Migration**: Clients update at their own pace
- **Deprecation**: Sunset old versions gracefully
- **Multiple Client Versions**: Support old mobile apps while updating backend

**Versioning Strategies:**

### 1. URL Path Versioning (Most Common)

**Pros**: Clear, easy to understand, cacheable
**Cons**: URL pollution, harder to maintain

```javascript
// V1 API
app.get('/api/v1/users', (req, res) => {
  res.json({ users: [...] })
})

// V2 API (new structure)
app.get('/api/v2/users', (req, res) => {
  res.json({
    data: { users: [...] },
    meta: { total: 100, page: 1 }
  })
})
```

### 2. Query Parameter Versioning

**Pros**: Clean URLs
**Cons**: Harder to route, not cacheable

```javascript
app.get('/api/users', (req, res) => {
  const version = req.query.version || 'v1'
  
  if (version === 'v2') {
    res.json({ data: { users: [...] }, meta: {} })
  } else {
    res.json({ users: [...] })
  }
})

// Usage: GET /api/users?version=v2
```

### 3. Header Versioning

**Pros**: Clean URLs, RESTful
**Cons**: Not visible in URL, harder to test

```javascript
app.get('/api/users', (req, res) => {
  const version = req.header('API-Version') || 'v1'
  
  if (version === 'v2') {
    res.json({ data: { users: [...] }, meta: {} })
  } else {
    res.json({ users: [...] })
  }
})

// Usage: GET /api/users
// Header: API-Version: v2
```

**Best Practices:**
- Use semantic versioning (v1, v2, not v1.1)
- Document deprecation timelines
- Monitor version usage
- Provide migration guides
- Default to latest stable version

---

## 📁 File Upload & Processing {#files}

### Using Multer

**Install**

```bash
npm install multer
```

**Configuration**

```javascript
// middleware/upload.js
const multer = require('multer');
const path = require('path');

// Storage configuration
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  }
});

// File filter
const fileFilter = (req, file, cb) => {
  const allowedTypes = /jpeg|jpg|png|pdf/;
  const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
  const mimetype = allowedTypes.test(file.mimetype);
  
  if (extname && mimetype) {
    cb(null, true);
  } else {
    cb(new Error('Only images and PDFs are allowed!'));
  }
};

// Upload configuration
const upload = multer({
  storage: storage,
  limits: {
    fileSize: 5 * 1024 * 1024 // 5MB
  },
  fileFilter: fileFilter
});

module.exports = upload;
```

**Single File Upload**

```javascript
const upload = require('../middleware/upload');

router.post('/upload', upload.single('avatar'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({
      success: false,
      error: 'Please upload a file'
    });
  }
  
  res.json({
    success: true,
    data: {
      filename: req.file.filename,
      path: req.file.path,
      size: req.file.size
    }
  });
});
```

**Multiple Files Upload**

```javascript
router.post('/upload-multiple', upload.array('photos', 5), (req, res) => {
  if (!req.files || req.files.length === 0) {
    return res.status(400).json({
      success: false,
      error: 'Please upload files'
    });
  }
  
  const files = req.files.map(file => ({
    filename: file.filename,
    path: file.path,
    size: file.size
  }));
  
  res.json({
    success: true,
    data: files
  });
});
```

---

## ⚡ Real-time with Socket.io {#realtime}

**Install**

```bash
npm install socket.io
```

**Server Setup**

```javascript
// server.js
const express = require('express');
const http = require('http');
const socketIO = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIO(server, {
  cors: {
    origin: '*'
  }
});

// Socket.io connection
io.on('connection', (socket) => {
  console.log('New client connected:', socket.id);
  
  // Join room
  socket.on('join-room', (room) => {
    socket.join(room);
    socket.to(room).emit('user-joined', socket.id);
  });
  
  // Send message
  socket.on('send-message', ({ room, message }) => {
    io.to(room).emit('receive-message', {
      user: socket.id,
      message,
      timestamp: new Date()
    });
  });
  
  // Disconnect
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

server.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

**Client (HTML)**

```html
<!DOCTYPE html>
<html>
<head>
  <script src="/socket.io/socket.io.js"></script>
</head>
<body>
  <div id="messages"></div>
  <input id="messageInput" type="text" />
  <button onclick="sendMessage()">Send</button>
  
  <script>
    const socket = io('http://localhost:3000');
    
    // Join room
    socket.emit('join-room', 'room1');
    
    // Receive messages
    socket.on('receive-message', (data) => {
      const messagesDiv = document.getElementById('messages');
      messagesDiv.innerHTML += `<p>${data.user}: ${data.message}</p>`;
    });
    
    // Send message
    function sendMessage() {
      const input = document.getElementById('messageInput');
      socket.emit('send-message', {
        room: 'room1',
        message: input.value
      });
      input.value = '';
    }
  </script>
</body>
</html>
```

---

## 🧪 Testing & Debugging {#testing}

### Unit Testing with Jest

**Install**

```bash
npm install --save-dev jest supertest
```

**Test Example**

```javascript
// tests/user.test.js
const request = require('supertest');
const app = require('../app');

describe('User API', () => {
  describe('GET /api/users', () => {
    it('should return all users', async () => {
      const res = await request(app)
        .get('/api/users')
        .expect(200);
      
      expect(res.body.success).toBe(true);
      expect(Array.isArray(res.body.data)).toBe(true);
    });
  });
  
  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const res = await request(app)
        .post('/api/users')
        .send({
          name: 'Test User',
          email: 'test@example.com',
          password: 'password123'
        })
        .expect(201);
      
      expect(res.body.success).toBe(true);
      expect(res.body.data.name).toBe('Test User');
    });
    
    it('should return error for missing fields', async () => {
      const res = await request(app)
        .post('/api/users')
        .send({
          name: 'Test User'
        })
        .expect(400);
      
      expect(res.body.success).toBe(false);
    });
  });
});
```

---

## 🚀 Performance & Scalability {#performance}

### Caching with Redis

```javascript
const redis = require('redis');
const client = redis.createClient();

// Cache middleware
const cache = async (req, res, next) => {
  const key = req.originalUrl;
  
  try {
    const data = await client.get(key);
    
    if (data) {
      return res.json(JSON.parse(data));
    }
    
    next();
  } catch (error) {
    next();
  }
};

// Use in route
app.get('/api/users', cache, async (req, res) => {
  const users = await User.find();
  
  // Cache for 1 hour
  await client.setex(req.originalUrl, 3600, JSON.stringify(users));
  
  res.json(users);
});
```

### Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests, please try again later'
});

app.use('/api/', limiter);
```

### Clustering

```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  const numCPUs = os.cpus().length;
  
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork();
  });
} else {
  require('./app');
}
```

---

## 🌐 Deployment & Production {#deployment}

### Environment Variables

```bash
# .env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://localhost:27017/myapp
JWT_SECRET=your-secret-key
```

```javascript
require('dotenv').config();

const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI;
```

### PM2 Process Manager

```bash
# Install PM2
npm install -g pm2

# Start app
pm2 start app.js --name my-app

# Monitor
pm2 monit

# Logs
pm2 logs

# Restart
pm2 restart my-app

# Stop
pm2 stop my-app
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - MONGODB_URI=mongodb://mongo:27017/myapp
    depends_on:
      - mongo
  
  mongo:
    image: mongo:latest
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

---

## ✅ Best Practices {#best-practices}

### 1. Project Structure

```
src/
├── config/           # Configuration files
├── controllers/      # Route controllers
├── models/           # Database models
├── routes/           # Route definitions
├── middleware/       # Custom middleware
├── utils/            # Helper functions
├── validators/       # Input validation
├── services/         # Business logic
└── app.js            # Express app
```

### 2. Error Handling

- Always use try-catch for async operations
- Create custom error classes
- Use centralized error handler
- Log errors properly

### 3. Security

```javascript
const helmet = require('helmet');
const mongoSanitize = require('express-mongo-sanitize');
const xss = require('xss-clean');
const hpp = require('hpp');

// Security headers
app.use(helmet());

// Prevent NoSQL injection
app.use(mongoSanitize());

// Prevent XSS attacks
app.use(xss());

// Prevent parameter pollution
app.use(hpp());
```

### 4. Performance

- Use compression
- Implement caching
- Database indexing
- Connection pooling
- Load balancing

---

## 🎯 Real-World Projects {#projects}

### Project 1: Blog API

Complete REST API with:
- User authentication
- CRUD for posts
- Comments system
- File uploads
- Pagination & search

### Project 2: E-commerce API

Features:
- Product management
- Shopping cart
- Order processing
- Payment integration
- Admin dashboard

### Project 3: Real-time Chat

Includes:
- Socket.io integration
- Private & group chats
- File sharing
- Online status
- Message history

---

## 🎓 Learning Resources

### Official Documentation
- Node.js: https://nodejs.org/docs
- Express: https://expressjs.com
- MongoDB: https://docs.mongodb.com

### Practice
- Build 5+ REST APIs
- Implement authentication
- Create real-time features
- Deploy to production

---

## 🏆 Congratulations!

You've completed the Node.js & Express Zero to Hero guide! You now have the skills to:

- ✅ Build scalable backend applications
- ✅ Create RESTful APIs
- ✅ Implement authentication & authorization
- ✅ Work with databases
- ✅ Deploy to production

**Next Steps:**
- Build real projects
- Learn TypeScript with Node.js
- Explore microservices
- Study GraphQL

Keep coding! 🚀

---

## 🔒 Advanced Security Topics {#advanced-security}

### 1. Helmet.js Security Headers

```javascript
const helmet = require('helmet')

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"]
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}))
```

### 2. Advanced Rate Limiting

```javascript
const rateLimit = require('express-rate-limit')
const RedisStore = require('rate-limit-redis')

// Different limits for different endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 attempts per 15 minutes
  message: 'Too many login attempts'
})

app.post('/api/auth/login', authLimiter, loginHandler)
```

### 3. OAuth 2.0 Integration

```javascript
const passport = require('passport')
const GoogleStrategy = require('passport-google-oauth20').Strategy

passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: '/auth/google/callback'
  },
  async (accessToken, refreshToken, profile, done) => {
    let user = await User.findOne({ googleId: profile.id })
    if (!user) {
      user = await User.create({
        googleId: profile.id,
        name: profile.displayName,
        email: profile.emails[0].value
      })
    }
    done(null, user)
  }
))

app.get('/auth/google',
  passport.authenticate('google', { scope: ['profile', 'email'] })
)
```

---

## 🚀 Performance Best Practices {#performance-best}

### 1. Response Compression

```javascript
const compression = require('compression')

app.use(compression({
  level: 6,
  threshold: 1024,
  filter: (req, res) => {
    return compression.filter(req, res)
  }
}))
```

### 2. Database Query Optimization

```javascript
// ❌ BAD: N+1 problem
const posts = await Post.find()
for (const post of posts) {
  post.author = await User.findById(post.authorId)
}

// ✅ GOOD: Use populate
const posts = await Post.find()
  .populate('author', 'name email')
  .select('title content')
  .lean()
```

### 3. Caching with Redis

```javascript
const redis = require('redis')
const client = redis.createClient()

// Cache middleware
const cache = async (req, res, next) => {
  const key = req.originalUrl
  const data = await client.get(key)
  
  if (data) {
    return res.json(JSON.parse(data))
  }
  next()
}

app.get('/api/users', cache, async (req, res) => {
  const users = await User.find()
  await client.setex(req.originalUrl, 3600, JSON.stringify(users))
  res.json(users)
})
```

---

## 📊 Production Monitoring {#monitoring}

### 1. Health Check Endpoints

```javascript
app.get('/health', async (req, res) => {
  const health = {
    status: 'UP',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    checks: {}
  }
  
  try {
    await mongoose.connection.db.admin().ping()
    health.checks.database = { status: 'UP' }
  } catch (error) {
    health.checks.database = { status: 'DOWN' }
    health.status = 'DOWN'
  }
  
  res.status(health.status === 'UP' ? 200 : 503).json(health)
})
```

### 2. Request Logging

```javascript
const winston = require('winston')

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
})

app.use((req, res, next) => {
  const start = Date.now()
  res.on('finish', () => {
    logger.info({
      method: req.method,
      url: req.originalUrl,
      status: res.statusCode,
      duration: `${Date.now() - start}ms`
    })
  })
  next()
})
```

---

## 🎯 Advanced Topics {#advanced-topics}

### 1. GraphQL with Node.js

**What is GraphQL?**
- Query language for APIs
- Request exactly what you need
- Single endpoint for all queries

```javascript
const { ApolloServer, gql } = require('apollo-server-express')

// Define schema
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }
  
  type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
  }
  
  type Query {
    users: [User!]!
    user(id: ID!): User
    posts: [Post!]!
  }
  
  type Mutation {
    createUser(name: String!, email: String!): User!
    createPost(title: String!, content: String!, authorId: ID!): Post!
  }
`

// Define resolvers
const resolvers = {
  Query: {
    users: async () => await User.find().populate('posts'),
    user: async (_, { id }) => await User.findById(id).populate('posts'),
    posts: async () => await Post.find().populate('author')
  },
  
  Mutation: {
    createUser: async (_, { name, email }) => {
      const user = new User({ name, email })
      await user.save()
      return user
    },
    createPost: async (_, { title, content, authorId }) => {
      const post = new Post({ title, content, author: authorId })
      await post.save()
      await User.findByIdAndUpdate(authorId, { $push: { posts: post._id } })
      return post
    }
  },
  
  User: {
    posts: async (parent) => await Post.find({ author: parent.id })
  },
  
  Post: {
    author: async (parent) => await User.findById(parent.author)
  }
}

// Create Apollo Server
const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    // Add user from JWT to context
    const token = req.headers.authorization || ''
    const user = getUser(token)
    return { user }
  }
})

// Apply middleware
await server.start()
server.applyMiddleware({ app, path: '/graphql' })

console.log(`🚀 GraphQL Server ready at http://localhost:4000${server.graphqlPath}`)
```

**GraphQL Queries**

```graphql
# Query: Get user with posts
query GetUserWithPosts {
  user(id: "123") {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}

# Mutation: Create user
mutation CreateUser {
  createUser(name: "John Doe", email: "john@example.com") {
    id
    name
    email
  }
}

# Query: Get all posts with author
query GetPostsWithAuthors {
  posts {
    id
    title
    author {
      name
      email
    }
  }
}
```

### 2. Microservices Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              Monolithic vs Microservices Architecture                       │
└─────────────────────────────────────────────────────────────────────────────┘

MONOLITHIC APPLICATION (Single Process):
┌────────────────────────────────────────────────────────────────────┐
│                      Frontend (React/Angular)                      │
└────────────────────────────────────────────────────────────────────┘
                              │ HTTP
                              ▼
┌────────────────────────────────────────────────────────────────────┐
│                    Load Balancer (NGINX)                           │
└────────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│   App Instance   │ │   App Instance   │ │   App Instance   │
│  ┌────────────┐  │ │  ┌────────────┐  │ │  ┌────────────┐  │
│  │   Users    │  │ │  │   Users    │  │ │  │   Users    │  │
│  │  Module    │  │ │  │  Module    │  │ │  │  Module    │  │
│  ├────────────┤  │ │  ├────────────┤  │ │  ├────────────┤  │
│  │   Orders   │  │ │  │   Orders   │  │ │  │   Orders   │  │
│  │  Module    │  │ │  │  Module    │  │ │  │  Module    │  │
│  ├────────────┤  │ │  ├────────────┤  │ │  ├────────────┤  │
│  │  Products  │  │ │  │  Products  │  │ │  │  Products  │  │
│  │  Module    │  │ │  │  Module    │  │ │  │  Module    │  │
│  ├────────────┤  │ │  ├────────────┤  │ │  ├────────────┤  │
│  │  Payments  │  │ │  │  Payments  │  │ │  │  Payments  │  │
│  └────────────┘  │ │  └────────────┘  │ │  └────────────┘  │
└──────────────────┘ └──────────────────┘ └──────────────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                  ┌────────────────────┐
                  │  Single Database   │
                  └────────────────────┘

Problems:
❌ One service fails → entire app down
❌ Must scale entire app (can't scale just one module)
❌ Tight coupling between modules
❌ Hard to update (must redeploy entire app)
❌ Technology lock-in (all modules same stack)

MICROSERVICES ARCHITECTURE (Independent Services):
┌────────────────────────────────────────────────────────────────────┐
│                      Frontend (React/Angular)                      │
└────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────────┐
│                    API Gateway (Port 3000)                         │
│  ┌────────────────────────────────────────────────────────┐       │
│  │ Routes:                                                │       │
│  │ /api/users/*    → User Service                         │       │
│  │ /api/orders/*   → Order Service                        │       │
│  │ /api/products/* → Product Service                      │       │
│  │ /api/payments/* → Payment Service                      │       │
│  └────────────────────────────────────────────────────────┘       │
└────────────────────────────────────────────────────────────────────┘
        │               │               │               │
        │ Proxy         │ Proxy         │ Proxy         │ Proxy
        ▼               ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│User Service  │ │Order Service │ │Product Svc   │ │Payment Svc   │
│Port 3001     │ │Port 3002     │ │Port 3003     │ │Port 3004     │
│              │ │              │ │              │ │              │
│ Node.js      │ │ Node.js      │ │ Python       │ │ Go           │
│ Express      │ │ Express      │ │ FastAPI      │ │ Gin          │
│              │ │              │ │              │ │              │
│ - GET /users │ │ - POST /order│ │ - GET /prods │ │ - POST /pay  │
│ - POST /auth │ │ - GET /order │ │ - PUT /prod  │ │ - GET /status│
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
        │               │               │               │
        ▼               ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Users DB    │ │  Orders DB   │ │ Products DB  │ │ Payments DB  │
│ (PostgreSQL) │ │  (MongoDB)   │ │ (PostgreSQL) │ │  (Redis)     │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘

Benefits:
✅ Independent deployment (update one service without affecting others)
✅ Fault isolation (one service fails, others keep running)
✅ Technology diversity (use best tool for each service)
✅ Independent scaling (scale only the services that need it)
✅ Smaller codebases (easier to understand and maintain)

┌─────────────────────────────────────────────────────────────────────────────┐
│          Microservices Communication Patterns                               │
└─────────────────────────────────────────────────────────────────────────────┘

1. Synchronous (HTTP/REST) - Direct Service-to-Service:
┌──────────────────────────────────────────────────────────────┐
│ User creates order:                                          │
│                                                              │
│ Client                                                       │
│   │                                                          │
│   │ POST /api/orders                                         │
│   ▼                                                          │
│ API Gateway                                                  │
│   │                                                          │
│   │ Proxy to Order Service                                  │
│   ▼                                                          │
│ Order Service (Port 3002)                                    │
│   │                                                          │
│   │ 1. Validate order                                       │
│   │ 2. Need user details ────────────────┐                  │
│   │                                      │                  │
│   │                                      ▼                  │
│   │                              User Service (3001)        │
│   │                                      │                  │
│   │                      GET /api/users/123                 │
│   │ ◄────────────────────────────────────┘                  │
│   │                      {name, email}                      │
│   │                                                          │
│   │ 3. Need product prices ──────────────┐                  │
│   │                                      │                  │
│   │                                      ▼                  │
│   │                            Product Service (3003)       │
│   │                                      │                  │
│   │                      GET /api/products                  │
│   │ ◄────────────────────────────────────┘                  │
│   │                      [{price: 99}]                      │
│   │                                                          │
│   │ 4. Process payment ──────────────────┐                  │
│   │                                      │                  │
│   │                                      ▼                  │
│   │                            Payment Service (3004)       │
│   │                                      │                  │
│   │                      POST /api/pay                      │
│   │ ◄────────────────────────────────────┘                  │
│   │                      {success: true}                    │
│   │                                                          │
│   │ 5. Create order record                                  │
│   ▼                                                          │
│ Orders Database                                              │
│                                                              │
│ Response to client: {orderId: 456, status: 'paid'}          │
└──────────────────────────────────────────────────────────────┘

Problems:
❌ Tight coupling (Order Service depends on 3 other services)
❌ Cascade failures (if User Service down, orders fail)
❌ Slow (sequential HTTP calls add latency)
❌ Hard to scale (must handle all HTTP connections)

2. Asynchronous (Message Queue) - Event-Driven:
┌──────────────────────────────────────────────────────────────┐
│ User creates order (Async):                                  │
│                                                              │
│ Client                                                       │
│   │ POST /api/orders                                         │
│   ▼                                                          │
│ Order Service                                                │
│   │                                                          │
│   │ 1. Create order (status: 'pending')                     │
│   │ 2. Publish event to queue                               │
│   ▼                                                          │
│ ┌────────────────────────────────────────────────┐           │
│ │         Message Queue (RabbitMQ/Kafka)         │           │
│ │                                                │           │
│ │  Queue: order.created                          │           │
│ │  Message: {orderId: 456, userId: 123, ...}     │           │
│ └────────────────────────────────────────────────┘           │
│          │              │              │                     │
│          │ Subscribe    │ Subscribe    │ Subscribe           │
│          ▼              ▼              ▼                     │
│  ┌──────────────┐ ┌────────────┐ ┌────────────┐             │
│  │   Email      │ │ Inventory  │ │  Payment   │             │
│  │  Service     │ │  Service   │ │  Service   │             │
│  └──────────────┘ └────────────┘ └────────────┘             │
│          │              │              │                     │
│          │              │              │                     │
│  Send    │      Reserve │      Charge  │                     │
│  confirm │       items  │      card    │                     │
│  email   │              │              │                     │
│          │              │              │                     │
│          │              │              │                     │
│          └──────────────┴──────────────┘                     │
│                         │                                    │
│                         │ All done, publish                  │
│                         ▼                                    │
│              Queue: order.completed                          │
│                         │                                    │
│                         ▼                                    │
│              Order Service updates status                    │
└──────────────────────────────────────────────────────────────┘

Benefits:
✅ Loose coupling (services don't know about each other)
✅ Fault tolerance (messages queued even if service down)
✅ Scalability (add more consumers to process faster)
✅ Async processing (fast response to client)
```

**Microservices Pattern**

```javascript
// User Service (Port 3001)
const express = require('express')
const app = express()

app.get('/api/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id)
  res.json(user)
})

app.listen(3001, () => console.log('User Service on port 3001'))

// Order Service (Port 3002)
const express = require('express')
const axios = require('axios')
const app = express()

app.post('/api/orders', async (req, res) => {
  const { userId, items } = req.body
  
  // Call User Service
  const userResponse = await axios.get(`http://localhost:3001/api/users/${userId}`)
  const user = userResponse.data
  
  // Create order
  const order = await Order.create({
    user: userId,
    items,
    total: calculateTotal(items)
  })
  
  res.status(201).json(order)
})

app.listen(3002, () => console.log('Order Service on port 3002'))

// API Gateway (Port 3000)
const express = require('express')
const { createProxyMiddleware } = require('http-proxy-middleware')
const app = express()

// Route requests to microservices
app.use('/api/users', createProxyMiddleware({ 
  target: 'http://localhost:3001',
  changeOrigin: true 
}))

app.use('/api/orders', createProxyMiddleware({ 
  target: 'http://localhost:3002',
  changeOrigin: true 
}))

app.listen(3000, () => console.log('API Gateway on port 3000'))
```

### 3. Message Queues with RabbitMQ

```javascript
const amqp = require('amqplib')

class MessageQueue {
  constructor() {
    this.connection = null
    this.channel = null
  }
  
  async connect() {
    this.connection = await amqp.connect('amqp://localhost')
    this.channel = await this.connection.createChannel()
  }
  
  async publish(queue, message) {
    await this.channel.assertQueue(queue, { durable: true })
    this.channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)), {
      persistent: true
    })
    console.log(`✉️  Message sent to ${queue}:`, message)
  }
  
  async consume(queue, callback) {
    await this.channel.assertQueue(queue, { durable: true })
    this.channel.consume(queue, async (msg) => {
      if (msg) {
        const content = JSON.parse(msg.content.toString())
        await callback(content)
        this.channel.ack(msg)
      }
    })
  }
}

// Usage: Email Service
const mq = new MessageQueue()
await mq.connect()

// Producer (API)
app.post('/api/register', async (req, res) => {
  const user = await User.create(req.body)
  
  // Send email task to queue
  await mq.publish('emails', {
    type: 'welcome',
    email: user.email,
    name: user.name
  })
  
  res.status(201).json(user)
})

// Consumer (Email Worker)
await mq.consume('emails', async (message) => {
  console.log('Processing email:', message)
  await sendEmail(message.email, message.type, { name: message.name })
})
```

### 4. Server-Sent Events (SSE)

```javascript
// Real-time notifications without WebSockets
app.get('/api/notifications/stream', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream')
  res.setHeader('Cache-Control', 'no-cache')
  res.setHeader('Connection', 'keep-alive')
  
  const userId = req.query.userId
  
  // Send initial connection message
  res.write('data: {"message": "Connected to notifications"}\n\n')
  
  // Listen for notifications
  const notificationListener = (notification) => {
    if (notification.userId === userId) {
      res.write(`data: ${JSON.stringify(notification)}\n\n`)
    }
  }
  
  eventEmitter.on('notification', notificationListener)
  
  // Cleanup on client disconnect
  req.on('close', () => {
    eventEmitter.off('notification', notificationListener)
    res.end()
  })
})

// Trigger notification
app.post('/api/notifications', async (req, res) => {
  const notification = await Notification.create(req.body)
  eventEmitter.emit('notification', notification)
  res.status(201).json(notification)
})
```

---

## 🏗️ Real-World Project: E-Commerce API {#ecommerce-project}

### Complete E-Commerce Backend

**1. Product Management**

```javascript
// models/Product.js
const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: String,
  price: { type: Number, required: true, min: 0 },
  category: { type: String, required: true },
  stock: { type: Number, default: 0 },
  images: [String],
  ratings: [{
    user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    rating: { type: Number, min: 1, max: 5 },
    comment: String,
    createdAt: { type: Date, default: Date.now }
  }],
  averageRating: { type: Number, default: 0 },
  tags: [String],
  isActive: { type: Boolean, default: true }
}, { timestamps: true })

// Virtual for total reviews
productSchema.virtual('totalReviews').get(function() {
  return this.ratings.length
})

// Calculate average rating before save
productSchema.pre('save', function(next) {
  if (this.ratings.length > 0) {
    const sum = this.ratings.reduce((acc, r) => acc + r.rating, 0)
    this.averageRating = sum / this.ratings.length
  }
  next()
})

module.exports = mongoose.model('Product', productSchema)

// routes/products.js
router.get('/products', async (req, res) => {
  const { 
    page = 1, 
    limit = 10, 
    category, 
    minPrice, 
    maxPrice, 
    search,
    sortBy = 'createdAt',
    order = 'desc'
  } = req.query
  
  // Build query
  const query = { isActive: true }
  
  if (category) query.category = category
  if (minPrice || maxPrice) {
    query.price = {}
    if (minPrice) query.price.$gte = Number(minPrice)
    if (maxPrice) query.price.$lte = Number(maxPrice)
  }
  if (search) {
    query.$or = [
      { name: { $regex: search, $options: 'i' } },
      { description: { $regex: search, $options: 'i' } },
      { tags: { $in: [new RegExp(search, 'i')] } }
    ]
  }
  
  // Execute query with pagination
  const products = await Product.find(query)
    .sort({ [sortBy]: order === 'asc' ? 1 : -1 })
    .limit(limit * 1)
    .skip((page - 1) * limit)
    .select('-__v')
  
  const count = await Product.countDocuments(query)
  
  res.json({
    products,
    totalPages: Math.ceil(count / limit),
    currentPage: page,
    total: count
  })
})

// Add product review
router.post('/products/:id/reviews', authenticate, async (req, res) => {
  const { rating, comment } = req.body
  
  const product = await Product.findById(req.params.id)
  if (!product) return res.status(404).json({ error: 'Product not found' })
  
  // Check if user already reviewed
  const existingReview = product.ratings.find(
    r => r.user.toString() === req.user.id
  )
  
  if (existingReview) {
    return res.status(400).json({ error: 'You already reviewed this product' })
  }
  
  product.ratings.push({
    user: req.user.id,
    rating,
    comment
  })
  
  await product.save()
  res.status(201).json(product)
})
```

**2. Shopping Cart**

```javascript
// models/Cart.js
const cartSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  items: [{
    product: { type: mongoose.Schema.Types.ObjectId, ref: 'Product' },
    quantity: { type: Number, required: true, min: 1 },
    price: Number
  }],
  totalAmount: { type: Number, default: 0 }
}, { timestamps: true })

cartSchema.pre('save', async function(next) {
  // Calculate total amount
  this.totalAmount = this.items.reduce((sum, item) => {
    return sum + (item.price * item.quantity)
  }, 0)
  next()
})

// routes/cart.js
router.post('/cart/items', authenticate, async (req, res) => {
  const { productId, quantity } = req.body
  
  const product = await Product.findById(productId)
  if (!product) return res.status(404).json({ error: 'Product not found' })
  
  if (product.stock < quantity) {
    return res.status(400).json({ error: 'Insufficient stock' })
  }
  
  let cart = await Cart.findOne({ user: req.user.id })
  
  if (!cart) {
    cart = new Cart({ user: req.user.id, items: [] })
  }
  
  const existingItem = cart.items.find(
    item => item.product.toString() === productId
  )
  
  if (existingItem) {
    existingItem.quantity += quantity
  } else {
    cart.items.push({
      product: productId,
      quantity,
      price: product.price
    })
  }
  
  await cart.save()
  await cart.populate('items.product')
  
  res.json(cart)
})

router.delete('/cart/items/:productId', authenticate, async (req, res) => {
  const cart = await Cart.findOne({ user: req.user.id })
  if (!cart) return res.status(404).json({ error: 'Cart not found' })
  
  cart.items = cart.items.filter(
    item => item.product.toString() !== req.params.productId
  )
  
  await cart.save()
  res.json(cart)
})
```

**3. Order Processing**

```javascript
// models/Order.js
const orderSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  items: [{
    product: { type: mongoose.Schema.Types.ObjectId, ref: 'Product' },
    quantity: Number,
    price: Number,
    name: String
  }],
  totalAmount: { type: Number, required: true },
  status: { 
    type: String, 
    enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'],
    default: 'pending'
  },
  paymentMethod: { type: String, required: true },
  paymentStatus: {
    type: String,
    enum: ['pending', 'completed', 'failed'],
    default: 'pending'
  },
  shippingAddress: {
    street: String,
    city: String,
    state: String,
    zipCode: String,
    country: String
  },
  trackingNumber: String,
  notes: String
}, { timestamps: true })

// routes/orders.js
router.post('/orders', authenticate, async (req, res) => {
  const { paymentMethod, shippingAddress } = req.body
  
  const cart = await Cart.findOne({ user: req.user.id }).populate('items.product')
  if (!cart || cart.items.length === 0) {
    return res.status(400).json({ error: 'Cart is empty' })
  }
  
  // Check stock availability
  for (const item of cart.items) {
    if (item.product.stock < item.quantity) {
      return res.status(400).json({ 
        error: `Insufficient stock for ${item.product.name}` 
      })
    }
  }
  
  // Create order
  const order = await Order.create({
    user: req.user.id,
    items: cart.items.map(item => ({
      product: item.product._id,
      quantity: item.quantity,
      price: item.price,
      name: item.product.name
    })),
    totalAmount: cart.totalAmount,
    paymentMethod,
    shippingAddress
  })
  
  // Update product stock
  for (const item of cart.items) {
    await Product.findByIdAndUpdate(item.product._id, {
      $inc: { stock: -item.quantity }
    })
  }
  
  // Clear cart
  await Cart.findByIdAndDelete(cart._id)
  
  // Send confirmation email (background job)
  await emailQueue.add('order-confirmation', {
    userId: req.user.id,
    orderId: order._id
  })
  
  res.status(201).json(order)
})

// Get order status
router.get('/orders/:id', authenticate, async (req, res) => {
  const order = await Order.findOne({
    _id: req.params.id,
    user: req.user.id
  }).populate('items.product')
  
  if (!order) return res.status(404).json({ error: 'Order not found' })
  
  res.json(order)
})

// Admin: Update order status
router.patch('/admin/orders/:id/status', [authenticate, isAdmin], async (req, res) => {
  const { status, trackingNumber } = req.body
  
  const order = await Order.findByIdAndUpdate(
    req.params.id,
    { status, trackingNumber },
    { new: true }
  )
  
  // Notify customer
  await emailQueue.add('order-update', {
    userId: order.user,
    orderId: order._id,
    status
  })
  
  res.json(order)
})
```

**4. Payment Integration (Stripe)**

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)

router.post('/payments/create-intent', authenticate, async (req, res) => {
  const { orderId } = req.body
  
  const order = await Order.findById(orderId)
  if (!order) return res.status(404).json({ error: 'Order not found' })
  
  if (order.user.toString() !== req.user.id) {
    return res.status(403).json({ error: 'Unauthorized' })
  }
  
  // Create payment intent
  const paymentIntent = await stripe.paymentIntents.create({
    amount: Math.round(order.totalAmount * 100), // Convert to cents
    currency: 'usd',
    metadata: {
      orderId: order._id.toString(),
      userId: req.user.id
    }
  })
  
  res.json({ clientSecret: paymentIntent.client_secret })
})

// Stripe webhook
router.post('/webhooks/stripe', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature']
  let event
  
  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    )
  } catch (err) {
    return res.status(400).send(`Webhook Error: ${err.message}`)
  }
  
  if (event.type === 'payment_intent.succeeded') {
    const paymentIntent = event.data.object
    const orderId = paymentIntent.metadata.orderId
    
    await Order.findByIdAndUpdate(orderId, {
      paymentStatus: 'completed',
      status: 'processing'
    })
    
    console.log(`✅ Payment succeeded for order ${orderId}`)
  }
  
  res.json({ received: true })
})
```

---

## 💡 Interview Questions & Answers {#interview}

### Beginner Level

**Q1: What is the event loop in Node.js?**

**A:** The event loop is what allows Node.js to perform non-blocking I/O operations despite JavaScript being single-threaded. It continuously checks the callback queue and executes callbacks when the call stack is empty.

```javascript
console.log('1. Start')

setTimeout(() => {
  console.log('2. Timeout')
}, 0)

Promise.resolve().then(() => {
  console.log('3. Promise')
})

console.log('4. End')

// Output:
// 1. Start
// 4. End
// 3. Promise (microtask - higher priority)
// 2. Timeout (macrotask)
```

**Q2: Difference between `require()` and `import`?**

**A:** 
- `require()`: CommonJS, synchronous, dynamic, can be called anywhere
- `import`: ES Modules, asynchronous, static, must be at top level

```javascript
// CommonJS
const express = require('express')
if (condition) {
  const module = require('./module') // ✅ Works
}

// ES Modules
import express from 'express'
if (condition) {
  import module from './module' // ❌ Error
}
// Use dynamic import instead
const module = await import('./module') // ✅ Works
```

### Intermediate Level

**Q3: How do you handle errors in async/await?**

**A:**
```javascript
// Method 1: try/catch
async function getUser(id) {
  try {
    const user = await User.findById(id)
    return user
  } catch (error) {
    logger.error('Error fetching user:', error)
    throw new Error('Failed to fetch user')
  }
}

// Method 2: Wrapper function
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next)
}

router.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id)
  res.json(user)
}))

// Method 3: Global error handler
app.use((err, req, res, next) => {
  logger.error(err.stack)
  res.status(500).json({ error: err.message })
})
```

**Q4: What are streams and why use them?**

**A:** Streams process data in chunks instead of loading everything into memory.

```javascript
const fs = require('fs')

// ❌ Bad: Loads entire file into memory
app.get('/download', (req, res) => {
  const file = fs.readFileSync('large-file.zip') // 5GB file!
  res.send(file) // Server crashes
})

// ✅ Good: Streams data in chunks
app.get('/download', (req, res) => {
  const stream = fs.createReadStream('large-file.zip')
  stream.pipe(res) // Memory efficient
})

// File processing with streams
const readStream = fs.createReadStream('input.txt')
const writeStream = fs.createWriteStream('output.txt')
const transform = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, chunk.toString().toUpperCase())
  }
})

readStream
  .pipe(transform)
  .pipe(writeStream)
  .on('finish', () => console.log('Done!'))
```

### Advanced Level

**Q5: How do you scale a Node.js application?**

**A:**

```javascript
// 1. Cluster Mode (Vertical Scaling)
const cluster = require('cluster')
const os = require('os')
const numCPUs = os.cpus().length

if (cluster.isMaster) {
  console.log(`Master ${process.pid} starting`)
  
  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork()
  }
  
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died. Starting new one...`)
    cluster.fork()
  })
} else {
  // Worker processes
  const app = express()
  // ... app setup
  app.listen(3000, () => {
    console.log(`Worker ${process.pid} started`)
  })
}

// 2. Load Balancing (Horizontal Scaling)
// Use NGINX or PM2

// PM2 Ecosystem File
module.exports = {
  apps: [{
    name: 'api',
    script: './app.js',
    instances: 'max', // Use all CPU cores
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'production'
    }
  }]
}

// 3. Caching Strategy
const NodeCache = require('node-cache')
const cache = new NodeCache({ stdTTL: 600 })

app.get('/api/products', async (req, res) => {
  const cacheKey = `products_${JSON.stringify(req.query)}`
  
  // Check cache
  let products = cache.get(cacheKey)
  
  if (!products) {
    products = await Product.find(req.query)
    cache.set(cacheKey, products)
  }
  
  res.json(products)
})

// 4. Database Connection Pooling
mongoose.connect(process.env.MONGODB_URI, {
  maxPoolSize: 10, // Maximum 10 connections
  minPoolSize: 2,
  socketTimeoutMS: 45000
})
```

**Q6: Memory leak prevention?**

**A:**
```javascript
// ❌ Memory Leak: Event listeners not removed
class UserService {
  constructor() {
    setInterval(() => {
      this.processUsers() // Keeps reference even after instance destroyed
    }, 1000)
  }
}

// ✅ Fix: Clean up resources
class UserService {
  constructor() {
    this.interval = setInterval(() => {
      this.processUsers()
    }, 1000)
  }
  
  destroy() {
    clearInterval(this.interval)
  }
}

// Monitor memory usage
setInterval(() => {
  const usage = process.memoryUsage()
  console.log({
    rss: `${Math.round(usage.rss / 1024 / 1024)}MB`,
    heapUsed: `${Math.round(usage.heapUsed / 1024 / 1024)}MB`,
    external: `${Math.round(usage.external / 1024 / 1024)}MB`
  })
}, 10000)
```

---

## 🎓 Learning Path & Resources {#learning-path}

### Month 1: Fundamentals
- ✅ JavaScript ES6+
- ✅ Node.js basics
- ✅ NPM & package management
- ✅ Async programming
- ✅ File system operations

### Month 2: Express & APIs
- ✅ Express.js
- ✅ RESTful API design
- ✅ Middleware
- ✅ Error handling
- ✅ Database integration

### Month 3: Advanced Topics
- ✅ Authentication/Authorization
- ✅ Testing (Jest, Supertest)
- ✅ WebSockets
- ✅ GraphQL
- ✅ Microservices

### Month 4: Production
- ✅ Performance optimization
- ✅ Security best practices
- ✅ Deployment (Docker, AWS)
- ✅ Monitoring & logging
- ✅ CI/CD pipelines

---

## 🚀 Next Steps

Keep building amazing things! 🚀

**Your Node.js Journey:**
1. ✅ Build 3-5 full projects
2. ✅ Contribute to open source
3. ✅ Deploy to production
4. ✅ Learn system design
5. ✅ Master DevOps

**Ready for:** Senior Backend Developer roles ($100K-$180K+)

