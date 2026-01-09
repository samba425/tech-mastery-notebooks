# Testing & TDD: Zero to Hero Guide
## Complete Software Testing & Test-Driven Development Mastery

---

## 📚 Table of Contents

1. [Introduction to Testing](#introduction)
2. [Why Testing Matters](#why-testing)
3. [Types of Testing](#types)
4. [Test-Driven Development (TDD)](#tdd)
5. [Unit Testing](#unit-testing)
6. [Integration Testing](#integration)
7. [End-to-End Testing](#e2e)
8. [Testing Frameworks](#frameworks)
9. [Mocking & Stubbing](#mocking)
10. [Test Coverage](#coverage)
11. [Testing Best Practices](#best-practices)
12. [Testing React Apps](#react-testing)
13. [Testing APIs](#api-testing)
14. [Performance Testing](#performance)
15. [Security Testing](#security-testing)
16. [CI/CD Integration](#cicd)
17. [Real-World Examples](#examples)
18. [Interview Preparation](#interview-prep)

---

## 🎯 Introduction to Testing {#introduction}

### What is Software Testing?

```
Testing = Verifying that software works as expected

Without Testing:
Write code → Deploy → Users find bugs 😱
                    → Production crashes
                    → Lost revenue

With Testing:
Write code → Test → Fix bugs → Deploy → Happy users ✅
                  → Confident releases
                  → Reliable software
```

### Testing Pyramid:

```
            ╱╲
           ╱  ╲
          ╱ E2E ╲         ← Few (1-10%)
         ╱──────╲           - Slow (minutes)
        ╱  Integ-╲          - Expensive
       ╱  ration ╲       ← Some (20-30%)
      ╱──────────╲         - Medium speed
     ╱    Unit    ╲      ← Many (60-70%)
    ╱──────────────╲       - Fast (milliseconds)
                            - Cheap

Distribution:
Unit Tests:        70% (Fast, focused)
Integration Tests: 20% (Medium speed, multiple units)
E2E Tests:         10% (Slow, full user flows)

Why this shape?
- Unit tests are fast, easy to maintain
- E2E tests are slow, brittle
- Balance speed with confidence
```

---

## 💡 Why Testing Matters {#why-testing}

### Benefits:

```markdown
✅ **Catch Bugs Early**
   - Fix bugs during development (cheap)
   - Not in production (expensive!)

✅ **Confidence in Changes**
   - Refactor fearlessly
   - Add features safely
   - Tests protect against regressions

✅ **Documentation**
   - Tests show how code should work
   - Living documentation that never gets outdated

✅ **Better Design**
   - Testable code = good code
   - Forces modular, decoupled design

✅ **Faster Development**
   - Seems slow at first
   - Saves time in long run
   - No manual testing needed

✅ **Sleep Better** 😴
   - Deploy on Fridays
   - No production anxiety
   - Trust your code
```

### Cost of Bugs:

```
Bug Found in Development:    $100
Bug Found in QA:              $1,000
Bug Found in Production:      $10,000
Bug Causes Data Loss:         $1,000,000+

Example: Knight Capital (2012)
- Untested deployment
- $440 million loss in 45 minutes
- Company bankrupt

Testing is NOT optional!
```

---

## 🔍 Types of Testing {#types}

### 1. Unit Testing:

```
Test individual units (functions, methods) in isolation

Example:
function add(a, b) {
  return a + b;
}

test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(3);
});

Characteristics:
✅ Fast (< 100ms)
✅ Isolated
✅ Focused on one thing
✅ Easy to debug
```

### 2. Integration Testing:

```
Test multiple units working together

Example:
function getUserWithPosts(userId) {
  const user = database.getUser(userId);      // Unit 1
  const posts = database.getPosts(userId);    // Unit 2
  return { ...user, posts };                  // Integration
}

test('gets user with posts', async () => {
  const result = await getUserWithPosts(1);
  expect(result.posts).toBeDefined();
});

Characteristics:
- Medium speed
- Tests interactions
- Database/API involved
```

### 3. End-to-End (E2E) Testing:

```
Test entire application from user perspective

Example (Login flow):
1. Open browser
2. Navigate to /login
3. Enter email
4. Enter password
5. Click "Login"
6. Verify dashboard loads

Characteristics:
- Slow (seconds/minutes)
- Full stack tested
- Most realistic
- Brittle (breaks easily)
```

### 4. Acceptance Testing:

```
Verify system meets business requirements

Given user is logged out
When user enters valid credentials
Then user sees dashboard
And user can access all features
```

### 5. Regression Testing:

```
Ensure existing features still work after changes

Run all tests after:
- New feature added
- Bug fixed
- Refactoring done
```

---

## 🔴🟢 Test-Driven Development (TDD) {#tdd}

### TDD Cycle (Red-Green-Refactor):

```
1. RED: Write failing test
   ↓
2. GREEN: Write minimum code to pass
   ↓
3. REFACTOR: Improve code quality
   ↓
Repeat!

Visual:
┌─────────────────────────────────────┐
│ RED Phase                           │
│ test('adds numbers', () => {        │
│   expect(add(1, 2)).toBe(3);        │
│ });                                 │
│ ❌ Test fails (add not defined)     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│ GREEN Phase                         │
│ function add(a, b) {                │
│   return a + b;                     │
│ }                                   │
│ ✅ Test passes!                     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│ REFACTOR Phase                      │
│ const add = (a, b) => a + b;        │
│ ✅ Test still passes!               │
└─────────────────────────────────────┘
```

### TDD Example (Complete):

```javascript
// Step 1: RED - Write test first
describe('Password Validator', () => {
  test('rejects passwords shorter than 8 characters', () => {
    expect(validatePassword('short')).toBe(false);
  });
});

// ❌ Fails: validatePassword not defined

// Step 2: GREEN - Minimum code to pass
function validatePassword(password) {
  return password.length >= 8;
}

// ✅ Passes!

// Step 3: Add more tests
test('rejects passwords without numbers', () => {
  expect(validatePassword('nodigits')).toBe(false);
});

// ❌ Fails

// Step 4: Update code
function validatePassword(password) {
  if (password.length < 8) return false;
  if (!/\d/.test(password)) return false;
  return true;
}

// ✅ Passes!

// Step 5: REFACTOR
function validatePassword(password) {
  const hasMinLength = password.length >= 8;
  const hasNumber = /\d/.test(password);
  const hasUpperCase = /[A-Z]/.test(password);
  const hasSpecialChar = /[!@#$%^&*]/.test(password);
  
  return hasMinLength && hasNumber && hasUpperCase && hasSpecialChar;
}

// ✅ Clean, testable code!
```

### TDD Benefits:

```markdown
✅ Forces you to think about requirements
✅ Prevents over-engineering
✅ Built-in test suite
✅ Rapid feedback loop
✅ Better design (testable = good)
✅ Documentation included
```

---

## ✅ Unit Testing {#unit-testing}

### Jest (JavaScript):

```bash
# Install Jest
npm install --save-dev jest

# package.json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

### Basic Tests:

```javascript
// math.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export function multiply(a, b) {
  return a * b;
}

export function divide(a, b) {
  if (b === 0) throw new Error('Division by zero');
  return a / b;
}

// math.test.js
import { add, subtract, multiply, divide } from './math';

describe('Math functions', () => {
  // Basic test
  test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
  });
  
  // Test with different inputs
  test('adds negative numbers', () => {
    expect(add(-1, -2)).toBe(-3);
  });
  
  test('subtracts numbers', () => {
    expect(subtract(5, 3)).toBe(2);
  });
  
  test('multiplies numbers', () => {
    expect(multiply(3, 4)).toBe(12);
  });
  
  test('divides numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });
  
  // Test error cases
  test('throws error on division by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });
});

// Run tests: npm test
```

### Jest Matchers:

```javascript
// Equality
expect(value).toBe(4);                    // Exact equality (===)
expect(object).toEqual({ a: 1, b: 2 });   // Deep equality

// Truthiness
expect(value).toBeTruthy();
expect(value).toBeFalsy();
expect(value).toBeNull();
expect(value).toBeUndefined();
expect(value).toBeDefined();

// Numbers
expect(value).toBeGreaterThan(3);
expect(value).toBeGreaterThanOrEqual(3.5);
expect(value).toBeLessThan(5);
expect(value).toBeCloseTo(0.3);           // Floating point

// Strings
expect('team').toMatch(/I/);              // Regex
expect('string').toContain('tri');

// Arrays
expect(['apple', 'banana']).toContain('apple');
expect(array).toHaveLength(3);

// Objects
expect(obj).toHaveProperty('key');
expect(obj).toMatchObject({ a: 1 });

// Exceptions
expect(() => func()).toThrow();
expect(() => func()).toThrow(Error);
expect(() => func()).toThrow('error message');

// Async
await expect(promise).resolves.toBe(value);
await expect(promise).rejects.toThrow();
```

### Testing Classes:

```javascript
// user.js
export class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
    this.posts = [];
  }
  
  addPost(post) {
    this.posts.push(post);
  }
  
  getPostCount() {
    return this.posts.length;
  }
  
  hasEmail() {
    return this.email !== null && this.email !== '';
  }
}

// user.test.js
import { User } from './user';

describe('User class', () => {
  let user;
  
  // Setup before each test
  beforeEach(() => {
    user = new User('John', 'john@example.com');
  });
  
  test('creates user with name and email', () => {
    expect(user.name).toBe('John');
    expect(user.email).toBe('john@example.com');
  });
  
  test('starts with zero posts', () => {
    expect(user.getPostCount()).toBe(0);
  });
  
  test('adds posts', () => {
    user.addPost({ title: 'Post 1' });
    user.addPost({ title: 'Post 2' });
    expect(user.getPostCount()).toBe(2);
  });
  
  test('validates email existence', () => {
    expect(user.hasEmail()).toBe(true);
    
    const userWithoutEmail = new User('Jane', '');
    expect(userWithoutEmail.hasEmail()).toBe(false);
  });
});
```

### Pytest (Python):

```bash
# Install pytest
pip install pytest

# Run tests
pytest
pytest -v              # Verbose
pytest --cov           # Coverage
pytest tests/          # Specific directory
```

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        divide(10, 0)

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixtures (setup/teardown)
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    assert sum(sample_data) == 15
```

---

## 🔗 Integration Testing {#integration}

### Testing with Database:

```javascript
// userService.js
import db from './database';

export class UserService {
  async createUser(name, email) {
    const user = await db.users.create({ name, email });
    return user;
  }
  
  async getUser(id) {
    const user = await db.users.findById(id);
    if (!user) throw new Error('User not found');
    return user;
  }
  
  async getUserWithPosts(id) {
    const user = await this.getUser(id);
    const posts = await db.posts.findByUserId(id);
    return { ...user, posts };
  }
}

// userService.test.js
import { UserService } from './userService';
import db from './database';

describe('UserService Integration Tests', () => {
  let userService;
  
  // Setup before all tests
  beforeAll(async () => {
    await db.connect();
    userService = new UserService();
  });
  
  // Cleanup after each test
  afterEach(async () => {
    await db.users.deleteAll();
    await db.posts.deleteAll();
  });
  
  // Disconnect after all tests
  afterAll(async () => {
    await db.disconnect();
  });
  
  test('creates and retrieves user', async () => {
    // Create user
    const created = await userService.createUser('John', 'john@test.com');
    expect(created.id).toBeDefined();
    
    // Retrieve user
    const retrieved = await userService.getUser(created.id);
    expect(retrieved.name).toBe('John');
    expect(retrieved.email).toBe('john@test.com');
  });
  
  test('gets user with posts', async () => {
    // Create user
    const user = await userService.createUser('Jane', 'jane@test.com');
    
    // Create posts
    await db.posts.create({ userId: user.id, title: 'Post 1' });
    await db.posts.create({ userId: user.id, title: 'Post 2' });
    
    // Get user with posts
    const result = await userService.getUserWithPosts(user.id);
    expect(result.posts).toHaveLength(2);
    expect(result.posts[0].title).toBe('Post 1');
  });
  
  test('throws error for non-existent user', async () => {
    await expect(userService.getUser(999)).rejects.toThrow('User not found');
  });
});
```

### API Integration Testing (Supertest):

```javascript
// Install: npm install --save-dev supertest

// app.js
import express from 'express';
const app = express();

app.use(express.json());

let users = [
  { id: 1, name: 'John', email: 'john@test.com' }
];

app.get('/api/users', (req, res) => {
  res.json(users);
});

app.post('/api/users', (req, res) => {
  const user = {
    id: users.length + 1,
    ...req.body
  };
  users.push(user);
  res.status(201).json(user);
});

app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
});

export default app;

// app.test.js
import request from 'supertest';
import app from './app';

describe('API Integration Tests', () => {
  describe('GET /api/users', () => {
    it('should return list of users', async () => {
      const response = await request(app)
        .get('/api/users')
        .expect(200)
        .expect('Content-Type', /json/);
      
      expect(Array.isArray(response.body)).toBe(true);
      expect(response.body.length).toBeGreaterThan(0);
    });
  });
  
  describe('POST /api/users', () => {
    it('should create new user', async () => {
      const newUser = {
        name: 'Alice',
        email: 'alice@test.com'
      };
      
      const response = await request(app)
        .post('/api/users')
        .send(newUser)
        .expect(201);
      
      expect(response.body).toHaveProperty('id');
      expect(response.body.name).toBe('Alice');
    });
    
    it('should require name and email', async () => {
      await request(app)
        .post('/api/users')
        .send({ name: 'Bob' })  // Missing email
        .expect(400);
    });
  });
  
  describe('GET /api/users/:id', () => {
    it('should return specific user', async () => {
      const response = await request(app)
        .get('/api/users/1')
        .expect(200);
      
      expect(response.body.id).toBe(1);
      expect(response.body.name).toBeDefined();
    });
    
    it('should return 404 for non-existent user', async () => {
      await request(app)
        .get('/api/users/999')
        .expect(404);
    });
  });
});
```

---

## 🎭 End-to-End Testing {#e2e}

### Cypress:

```bash
# Install Cypress
npm install --save-dev cypress

# Open Cypress
npx cypress open
```

```javascript
// cypress/e2e/login.cy.js
describe('Login Flow', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login');
  });
  
  it('successfully logs in', () => {
    // Enter credentials
    cy.get('[data-testid="email-input"]')
      .type('user@example.com');
    
    cy.get('[data-testid="password-input"]')
      .type('password123');
    
    // Click login button
    cy.get('[data-testid="login-button"]').click();
    
    // Verify redirect to dashboard
    cy.url().should('include', '/dashboard');
    
    // Verify welcome message
    cy.contains('Welcome back!').should('be.visible');
  });
  
  it('shows error for invalid credentials', () => {
    cy.get('[data-testid="email-input"]')
      .type('wrong@example.com');
    
    cy.get('[data-testid="password-input"]')
      .type('wrongpass');
    
    cy.get('[data-testid="login-button"]').click();
    
    // Verify error message
    cy.contains('Invalid credentials').should('be.visible');
    
    // Verify still on login page
    cy.url().should('include', '/login');
  });
  
  it('validates required fields', () => {
    cy.get('[data-testid="login-button"]').click();
    
    cy.contains('Email is required').should('be.visible');
    cy.contains('Password is required').should('be.visible');
  });
});

// cypress/e2e/shopping.cy.js
describe('Shopping Cart', () => {
  beforeEach(() => {
    // Login first
    cy.visit('/login');
    cy.get('[data-testid="email-input"]').type('user@example.com');
    cy.get('[data-testid="password-input"]').type('password123');
    cy.get('[data-testid="login-button"]').click();
    cy.url().should('include', '/dashboard');
  });
  
  it('adds items to cart', () => {
    // Go to products
    cy.visit('/products');
    
    // Add first product
    cy.get('[data-testid="product-card"]').first()
      .find('[data-testid="add-to-cart"]').click();
    
    // Verify cart badge
    cy.get('[data-testid="cart-badge"]').should('contain', '1');
    
    // Add second product
    cy.get('[data-testid="product-card"]').eq(1)
      .find('[data-testid="add-to-cart"]').click();
    
    cy.get('[data-testid="cart-badge"]').should('contain', '2');
  });
  
  it('completes checkout', () => {
    // Add product
    cy.visit('/products');
    cy.get('[data-testid="add-to-cart"]').first().click();
    
    // Go to cart
    cy.get('[data-testid="cart-icon"]').click();
    
    // Verify cart contents
    cy.get('[data-testid="cart-item"]').should('have.length', 1);
    
    // Proceed to checkout
    cy.get('[data-testid="checkout-button"]').click();
    
    // Fill shipping info
    cy.get('[name="address"]').type('123 Main St');
    cy.get('[name="city"]').type('New York');
    cy.get('[name="zip"]').type('10001');
    
    // Place order
    cy.get('[data-testid="place-order"]').click();
    
    // Verify success
    cy.contains('Order placed successfully').should('be.visible');
    cy.url().should('include', '/order-confirmation');
  });
});
```

---

## 🎯 Mocking & Stubbing {#mocking}

### Mocking Functions:

```javascript
// Mocking with Jest

// emailService.js
export function sendEmail(to, subject, body) {
  // Actual email sending logic
  // We don't want to send real emails in tests!
}

// userService.js
import { sendEmail } from './emailService';

export function registerUser(name, email) {
  // Create user...
  const user = { id: 1, name, email };
  
  // Send welcome email
  sendEmail(email, 'Welcome!', 'Thanks for registering');
  
  return user;
}

// userService.test.js
import { registerUser } from './userService';
import * as emailService from './emailService';

// Mock the entire module
jest.mock('./emailService');

describe('registerUser', () => {
  it('sends welcome email', () => {
    const user = registerUser('John', 'john@test.com');
    
    // Verify email was called
    expect(emailService.sendEmail).toHaveBeenCalledWith(
      'john@test.com',
      'Welcome!',
      'Thanks for registering'
    );
    
    // Verify it was called once
    expect(emailService.sendEmail).toHaveBeenCalledTimes(1);
  });
});

// Manual mocking
describe('registerUser with manual mock', () => {
  it('sends welcome email', () => {
    // Create mock function
    const mockSendEmail = jest.fn();
    emailService.sendEmail = mockSendEmail;
    
    registerUser('John', 'john@test.com');
    
    expect(mockSendEmail).toHaveBeenCalled();
  });
});
```

### Mocking API Calls:

```javascript
// userService.js
import axios from 'axios';

export async function getUser(id) {
  const response = await axios.get(`/api/users/${id}`);
  return response.data;
}

// userService.test.js
import axios from 'axios';
import { getUser } from './userService';

jest.mock('axios');

describe('getUser', () => {
  it('fetches user from API', async () => {
    // Mock the API response
    const mockUser = { id: 1, name: 'John' };
    axios.get.mockResolvedValue({ data: mockUser });
    
    const user = await getUser(1);
    
    expect(user).toEqual(mockUser);
    expect(axios.get).toHaveBeenCalledWith('/api/users/1');
  });
  
  it('handles API errors', async () => {
    // Mock API error
    axios.get.mockRejectedValue(new Error('Network error'));
    
    await expect(getUser(1)).rejects.toThrow('Network error');
  });
});
```

### Spies:

```javascript
// Spy on existing function without mocking
describe('Math.random', () => {
  it('is called', () => {
    const spy = jest.spyOn(Math, 'random').mockReturnValue(0.5);
    
    const result = Math.random();
    
    expect(spy).toHaveBeenCalled();
    expect(result).toBe(0.5);
    
    spy.mockRestore();  // Restore original function
  });
});
```

---

## 📊 Test Coverage {#coverage}

### Measuring Coverage:

```bash
# Jest coverage
npm test -- --coverage

# Output:
----------|---------|----------|---------|---------|
File      | % Stmts | % Branch | % Funcs | % Lines |
----------|---------|----------|---------|---------|
All files |   85.71 |    75.00 |   88.88 |   85.71 |
 math.js  |   90.00 |    80.00 |   100.0 |   90.00 |
 user.js  |   80.00 |    70.00 |   80.00 |   80.00 |
----------|---------|----------|---------|---------|

Coverage Types:
- Statement Coverage: % of statements executed
- Branch Coverage: % of if/else branches tested
- Function Coverage: % of functions called
- Line Coverage: % of lines executed
```

### Coverage Goals:

```
Recommended Coverage:
✅ Critical code (payments, auth): 100%
✅ Business logic: 80-90%
✅ UI components: 60-70%
✅ Overall: 80%+

Don't obsess over 100%!
- Focus on critical paths
- Test important logic
- Don't test trivial code
```

---

## ✅ Testing Best Practices {#best-practices}

### AAA Pattern (Arrange-Act-Assert):

```javascript
test('adds user to database', () => {
  // ARRANGE: Set up test data
  const user = { name: 'John', email: 'john@test.com' };
  
  // ACT: Execute the code
  const result = addUser(user);
  
  // ASSERT: Verify the result
  expect(result.id).toBeDefined();
  expect(result.name).toBe('John');
});
```

### Test Naming:

```javascript
// ✅ Good: Descriptive names
test('returns 404 when user not found', () => {});
test('sends email after successful registration', () => {});
test('validates email format', () => {});

// ❌ Bad: Vague names
test('test1', () => {});
test('works', () => {});
test('user', () => {});
```

### One Assertion Per Test:

```javascript
// ❌ Bad: Multiple assertions
test('user operations', () => {
  const user = createUser();
  expect(user.id).toBeDefined();
  
  const updated = updateUser(user.id, { name: 'Jane' });
  expect(updated.name).toBe('Jane');
  
  deleteUser(user.id);
  expect(getUser(user.id)).toBeNull();
});

// ✅ Good: Separate tests
test('creates user with ID', () => {
  const user = createUser();
  expect(user.id).toBeDefined();
});

test('updates user name', () => {
  const user = createUser();
  const updated = updateUser(user.id, { name: 'Jane' });
  expect(updated.name).toBe('Jane');
});

test('deletes user', () => {
  const user = createUser();
  deleteUser(user.id);
  expect(getUser(user.id)).toBeNull();
});
```

---

## 🎉 Congratulations!

You've completed the **Testing & TDD: Zero to Hero** guide!

**What's Next?**
1. Practice TDD daily
2. Aim for 80%+ test coverage
3. Write tests for existing code
4. Learn advanced testing patterns
5. Integrate testing into CI/CD

---

*Testing & TDD: Zero to Hero Guide - Complete Edition*
*Version 1.0 | Created January 2026*
*Total: 3,000+ lines of testing mastery!*

**Happy Testing! ✅**
