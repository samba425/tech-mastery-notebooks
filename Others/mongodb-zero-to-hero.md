# MongoDB: Zero to Hero Guide
## Complete NoSQL Database Mastery

---

## 📚 Table of Contents

1. [Introduction to MongoDB](#introduction)
2. [Installation & Setup](#setup)
3. [MongoDB Basics](#basics)
4. [CRUD Operations](#crud)
5. [Query Operators](#operators)
6. [Data Modeling](#modeling)
7. [Aggregation Framework](#aggregation)
8. [Indexing & Performance](#indexing)
9. [Transactions](#transactions)
10. [Mongoose ODM](#mongoose)
11. [Security & Authentication](#security)
12. [Replication & Sharding](#scaling)
13. [Backup & Recovery](#backup)
14. [Best Practices](#best-practices)
15. [Real-World Projects](#projects)

---

## 🎯 Introduction to MongoDB {#introduction}

### What is MongoDB?

**MongoDB** is a NoSQL document database that stores data in flexible, JSON-like documents.

```
┌─────────────────────────────────────┐
│    Relational Database (SQL)        │
├─────────────────────────────────────┤
│  Tables with rows and columns       │
│  Fixed schema                       │
│  SQL queries                        │
│  Joins required                     │
└─────────────────────────────────────┘
                 vs
┌─────────────────────────────────────┐
│    MongoDB (NoSQL)                  │
├─────────────────────────────────────┤
│  Collections with documents         │
│  Flexible schema                    │
│  JSON-like queries                  │
│  Embedded documents                 │
└─────────────────────────────────────┘
```

### Why MongoDB?

- ✅ **Flexible Schema** - No predefined structure
- ✅ **Scalable** - Horizontal scaling with sharding
- ✅ **High Performance** - Fast read/write operations
- ✅ **Rich Queries** - Powerful query language
- ✅ **Document-Based** - Natural data representation

### Document Structure

```javascript
// SQL Table
┌────┬──────┬───────────────────┬─────┐
│ id │ name │ email             │ age │
├────┼──────┼───────────────────┼─────┤
│ 1  │ John │ john@example.com  │ 30  │
└────┴──────┴───────────────────┴─────┘

// MongoDB Document
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John",
  email: "john@example.com",
  age: 30,
  address: {           // Embedded document
    street: "123 Main St",
    city: "New York"
  },
  hobbies: ["reading", "coding"]  // Array
}
```

### MongoDB Architecture

```
┌─────────────────────────────────────┐
│         Application                 │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      MongoDB Driver                 │
│  (Node.js, Python, Java, etc.)     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      MongoDB Server                 │
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐   │
│  │  Database 1                 │   │
│  │  ├── Collection 1           │   │
│  │  │   ├── Document 1         │   │
│  │  │   └── Document 2         │   │
│  │  └── Collection 2           │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  Database 2                 │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## 🔧 Installation & Setup {#setup}

### Install MongoDB

**macOS (using Homebrew)**

```bash
# Install MongoDB Community Edition
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB service
brew services start mongodb-community

# Stop MongoDB service
brew services stop mongodb-community
```

**Windows**

1. Download from https://www.mongodb.com/try/download/community
2. Run installer
3. MongoDB runs as Windows service automatically

**Linux (Ubuntu)**

```bash
# Import public key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Create list file
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Install MongoDB
sudo apt-get update
sudo apt-get install -y mongodb-org

# Start MongoDB
sudo systemctl start mongod
```

### Verify Installation

```bash
# Check MongoDB version
mongod --version

# Connect to MongoDB shell
mongosh

# In mongosh
> db.version()
> show dbs
```

### MongoDB Compass (GUI)

Download from: https://www.mongodb.com/products/compass

---

## 📖 MongoDB Basics {#basics}

### Database & Collections

```javascript
// Show all databases
show dbs

// Create/Switch to database
use myDatabase

// Current database
db

// Create collection
db.createCollection("users")

// Show collections
show collections

// Drop collection
db.users.drop()

// Drop database
db.dropDatabase()
```

### Documents

```javascript
// A document is like a JSON object
{
  _id: ObjectId("..."),        // Unique identifier (auto-generated)
  name: "John Doe",            // String
  age: 30,                     // Number
  email: "john@example.com",   // String
  isActive: true,              // Boolean
  createdAt: new Date(),       // Date
  address: {                   // Embedded document
    street: "123 Main St",
    city: "New York",
    zipCode: "10001"
  },
  tags: ["developer", "writer"], // Array
  skills: [                    // Array of objects
    { name: "JavaScript", level: "expert" },
    { name: "Python", level: "intermediate" }
  ]
}
```

### Data Types

```javascript
// String
{ name: "John Doe" }

// Number (Integer or Float)
{ age: 30, price: 99.99 }

// Boolean
{ isActive: true }

// Date
{ createdAt: new Date() }

// Array
{ tags: ["tag1", "tag2"] }

// Object/Embedded Document
{ address: { city: "NYC" } }

// ObjectId
{ _id: ObjectId("507f1f77bcf86cd799439011") }

// Null
{ middleName: null }
```

---

## ✏️ CRUD Operations {#crud}

### Create (Insert)

**Insert One**

```javascript
// Insert single document
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  createdAt: new Date()
})

// Returns
{
  acknowledged: true,
  insertedId: ObjectId("507f1f77bcf86cd799439011")
}
```

**Insert Many**

```javascript
// Insert multiple documents
db.users.insertMany([
  {
    name: "Jane Smith",
    email: "jane@example.com",
    age: 25
  },
  {
    name: "Bob Johnson",
    email: "bob@example.com",
    age: 35
  }
])

// Returns
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("..."),
    '1': ObjectId("...")
  }
}
```

### Read (Find)

**Find All**

```javascript
// Get all documents
db.users.find()

// Pretty print
db.users.find().pretty()
```

**Find with Filter**

```javascript
// Find by exact match
db.users.find({ name: "John Doe" })

// Find by age
db.users.find({ age: 30 })

// Find with multiple conditions (AND)
db.users.find({
  age: 30,
  isActive: true
})
```

**Find One**

```javascript
// Get first matching document
db.users.findOne({ email: "john@example.com" })

// Find by _id
db.users.findOne({ _id: ObjectId("507f1f77bcf86cd799439011") })
```

**Projection (Select Fields)**

```javascript
// Only return name and email (exclude _id)
db.users.find(
  { age: 30 },
  { name: 1, email: 1, _id: 0 }
)

// Exclude specific fields
db.users.find(
  {},
  { password: 0 }
)
```

**Limit & Skip**

```javascript
// Limit results
db.users.find().limit(5)

// Skip results (pagination)
db.users.find().skip(10).limit(5)

// Page 1: skip(0).limit(10)
// Page 2: skip(10).limit(10)
// Page 3: skip(20).limit(10)
```

**Sort**

```javascript
// Sort ascending (1)
db.users.find().sort({ age: 1 })

// Sort descending (-1)
db.users.find().sort({ age: -1 })

// Multiple sort fields
db.users.find().sort({ age: -1, name: 1 })
```

**Count**

```javascript
// Count all documents
db.users.countDocuments()

// Count with filter
db.users.countDocuments({ age: { $gte: 30 } })
```

### Update

**Update One**

```javascript
// Update single document
db.users.updateOne(
  { email: "john@example.com" },    // Filter
  { $set: { age: 31 } }             // Update
)

// Returns
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1
}
```

**Update Many**

```javascript
// Update multiple documents
db.users.updateMany(
  { age: { $lt: 18 } },           // Filter: age < 18
  { $set: { isMinor: true } }     // Update
)
```

**Update Operators**

```javascript
// $set - Set field value
db.users.updateOne(
  { _id: ObjectId("...") },
  { $set: { name: "John Smith", age: 32 } }
)

// $unset - Remove field
db.users.updateOne(
  { _id: ObjectId("...") },
  { $unset: { middleName: "" } }
)

// $inc - Increment number
db.users.updateOne(
  { _id: ObjectId("...") },
  { $inc: { age: 1 } }           // Increase age by 1
)

// $mul - Multiply
db.users.updateOne(
  { _id: ObjectId("...") },
  { $mul: { price: 1.1 } }       // Increase price by 10%
)

// $rename - Rename field
db.users.updateOne(
  { _id: ObjectId("...") },
  { $rename: { "name": "fullName" } }
)

// $min - Update if new value is less
db.users.updateOne(
  { _id: ObjectId("...") },
  { $min: { lowestScore: 75 } }
)

// $max - Update if new value is greater
db.users.updateOne(
  { _id: ObjectId("...") },
  { $max: { highestScore: 95 } }
)

// $currentDate - Set to current date
db.users.updateOne(
  { _id: ObjectId("...") },
  { $currentDate: { lastModified: true } }
)
```

**Array Update Operators**

```javascript
// $push - Add to array
db.users.updateOne(
  { _id: ObjectId("...") },
  { $push: { hobbies: "swimming" } }
)

// $push with $each (multiple items)
db.users.updateOne(
  { _id: ObjectId("...") },
  { $push: { hobbies: { $each: ["reading", "coding"] } } }
)

// $pull - Remove from array
db.users.updateOne(
  { _id: ObjectId("...") },
  { $pull: { hobbies: "swimming" } }
)

// $addToSet - Add to array if not exists
db.users.updateOne(
  { _id: ObjectId("...") },
  { $addToSet: { tags: "developer" } }
)

// $pop - Remove first (-1) or last (1) element
db.users.updateOne(
  { _id: ObjectId("...") },
  { $pop: { hobbies: 1 } }        // Remove last
)
```

**Replace One**

```javascript
// Replace entire document (except _id)
db.users.replaceOne(
  { email: "john@example.com" },
  {
    name: "John Smith",
    email: "john@example.com",
    age: 32,
    city: "Boston"
  }
)
```

**Upsert (Update or Insert)**

```javascript
// Insert if not found, update if found
db.users.updateOne(
  { email: "new@example.com" },
  { $set: { name: "New User", age: 25 } },
  { upsert: true }
)
```

### Delete

**Delete One**

```javascript
// Delete single document
db.users.deleteOne({ email: "john@example.com" })

// Returns
{
  acknowledged: true,
  deletedCount: 1
}
```

**Delete Many**

```javascript
// Delete multiple documents
db.users.deleteMany({ age: { $lt: 18 } })

// Delete all documents
db.users.deleteMany({})
```

---

## 🔍 Query Operators {#operators}

### Comparison Operators

```javascript
// $eq - Equal
db.users.find({ age: { $eq: 30 } })
// Same as: db.users.find({ age: 30 })

// $ne - Not equal
db.users.find({ age: { $ne: 30 } })

// $gt - Greater than
db.users.find({ age: { $gt: 30 } })

// $gte - Greater than or equal
db.users.find({ age: { $gte: 30 } })

// $lt - Less than
db.users.find({ age: { $lt: 30 } })

// $lte - Less than or equal
db.users.find({ age: { $lte: 30 } })

// $in - In array
db.users.find({ age: { $in: [25, 30, 35] } })

// $nin - Not in array
db.users.find({ age: { $nin: [25, 30, 35] } })

// Range query
db.users.find({ age: { $gte: 25, $lte: 35 } })
```

### Logical Operators

```javascript
// $and - All conditions must be true
db.users.find({
  $and: [
    { age: { $gte: 25 } },
    { age: { $lte: 35 } }
  ]
})

// $or - At least one condition must be true
db.users.find({
  $or: [
    { age: { $lt: 18 } },
    { age: { $gt: 65 } }
  ]
})

// $not - Negation
db.users.find({
  age: { $not: { $gte: 30 } }
})

// $nor - None of the conditions should be true
db.users.find({
  $nor: [
    { age: { $lt: 18 } },
    { isActive: false }
  ]
})

// Complex query
db.users.find({
  $and: [
    { age: { $gte: 18 } },
    {
      $or: [
        { city: "New York" },
        { city: "Boston" }
      ]
    }
  ]
})
```

### Element Operators

```javascript
// $exists - Field exists
db.users.find({ middleName: { $exists: true } })

// $type - Field type
db.users.find({ age: { $type: "number" } })
db.users.find({ age: { $type: "string" } })

// Type codes
// "double" = 1, "string" = 2, "object" = 3, "array" = 4
// "bool" = 8, "date" = 9, "null" = 10
```

### Array Operators

```javascript
// $all - Array contains all elements
db.users.find({
  hobbies: { $all: ["reading", "coding"] }
})

// $elemMatch - Array element matches all conditions
db.users.find({
  skills: {
    $elemMatch: {
      name: "JavaScript",
      level: "expert"
    }
  }
})

// $size - Array size
db.users.find({
  hobbies: { $size: 3 }
})

// Array element by index
db.users.find({ "hobbies.0": "reading" })
```

### String Operators

```javascript
// $regex - Regular expression
db.users.find({
  name: { $regex: /john/i }     // Case-insensitive
})

// Search by pattern
db.users.find({
  email: { $regex: /@gmail\.com$/ }
})

// Starts with
db.users.find({
  name: { $regex: /^J/ }
})

// Contains
db.users.find({
  name: { $regex: /Doe/ }
})
```

---

## 📐 Data Modeling {#modeling}

### Schema Design Patterns

**Embedded Documents (One-to-Few)**

```javascript
// User with embedded address (1-to-1)
{
  _id: ObjectId("..."),
  name: "John Doe",
  email: "john@example.com",
  address: {                    // Embedded
    street: "123 Main St",
    city: "New York",
    zipCode: "10001"
  }
}

// User with embedded posts (1-to-few)
{
  _id: ObjectId("..."),
  name: "John Doe",
  posts: [                      // Embedded array
    {
      title: "First Post",
      content: "Hello World",
      date: new Date()
    },
    {
      title: "Second Post",
      content: "MongoDB is great",
      date: new Date()
    }
  ]
}
```

**References (One-to-Many)**

```javascript
// Author document
{
  _id: ObjectId("author123"),
  name: "John Doe",
  email: "john@example.com"
}

// Book documents (many)
{
  _id: ObjectId("book1"),
  title: "MongoDB Basics",
  authorId: ObjectId("author123"),   // Reference
  pages: 300
}

{
  _id: ObjectId("book2"),
  title: "Advanced MongoDB",
  authorId: ObjectId("author123"),   // Reference
  pages: 500
}

// Query
const author = db.authors.findOne({ _id: ObjectId("author123") })
const books = db.books.find({ authorId: author._id })
```

**Hybrid Approach**

```javascript
// Store most-used fields embedded, reference for complete data
{
  _id: ObjectId("..."),
  title: "Great Product",
  author: {                      // Embedded (frequently accessed)
    id: ObjectId("author123"),
    name: "John Doe"
  },
  comments: [                    // Only IDs
    ObjectId("comment1"),
    ObjectId("comment2")
  ]
}
```

### Relationships Diagram

```
Embedded (1-to-Few)
┌─────────────────┐
│  User           │
│  ├─ name        │
│  └─ address     │ ◄─── Embedded
│     ├─ street   │
│     └─ city     │
└─────────────────┘

Referenced (1-to-Many)
┌─────────────────┐         ┌─────────────────┐
│  Author         │         │  Book           │
│  ├─ _id         │ ◄─────┐ │  ├─ title       │
│  └─ name        │       └─│  └─ authorId    │
└─────────────────┘         └─────────────────┘
                            └─────────────────┘
                            └─────────────────┘
```

### Schema Validation

```javascript
// Create collection with validation
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "age"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        email: {
          bsonType: "string",
          pattern: "^.+@.+$",
          description: "must be a valid email"
        },
        age: {
          bsonType: "int",
          minimum: 18,
          maximum: 120,
          description: "must be an integer between 18 and 120"
        },
        hobbies: {
          bsonType: "array",
          items: {
            bsonType: "string"
          }
        }
      }
    }
  }
})
```

---

## 📊 Aggregation Framework {#aggregation}

### What is Aggregation?

Aggregation is a pipeline of stages that process documents.

```
Documents ──▶ Stage 1 ──▶ Stage 2 ──▶ Stage 3 ──▶ Result
              $match      $group      $sort
```

### Basic Aggregation

```javascript
// Simple aggregation
db.orders.aggregate([
  { $match: { status: "completed" } },      // Filter
  { $group: {                               // Group
      _id: "$customerId",
      totalAmount: { $sum: "$amount" }
    }
  },
  { $sort: { totalAmount: -1 } }            // Sort
])
```

### Common Pipeline Stages

**$match - Filter Documents**

```javascript
db.orders.aggregate([
  {
    $match: {
      status: "completed",
      amount: { $gte: 100 }
    }
  }
])
```

**$group - Group Documents**

```javascript
// Count documents by category
db.products.aggregate([
  {
    $group: {
      _id: "$category",               // Group by field
      count: { $sum: 1 },             // Count
      avgPrice: { $avg: "$price" },   // Average
      maxPrice: { $max: "$price" },   // Maximum
      minPrice: { $min: "$price" }    // Minimum
    }
  }
])

// Example result:
[
  { _id: "Electronics", count: 50, avgPrice: 299.99, maxPrice: 999, minPrice: 49.99 },
  { _id: "Books", count: 100, avgPrice: 19.99, maxPrice: 49.99, minPrice: 9.99 }
]
```

**$project - Shape Output**

```javascript
db.users.aggregate([
  {
    $project: {
      _id: 0,                          // Exclude _id
      name: 1,                         // Include name
      email: 1,                        // Include email
      ageGroup: {                      // Computed field
        $cond: {
          if: { $gte: ["$age", 18] },
          then: "Adult",
          else: "Minor"
        }
      }
    }
  }
])
```

**$sort - Sort Results**

```javascript
db.users.aggregate([
  { $sort: { age: -1, name: 1 } }     // Sort by age desc, name asc
])
```

**$limit & $skip - Pagination**

```javascript
db.users.aggregate([
  { $sort: { createdAt: -1 } },
  { $skip: 20 },
  { $limit: 10 }
])
```

**$lookup - Join Collections**

```javascript
// Left outer join
db.orders.aggregate([
  {
    $lookup: {
      from: "users",              // Collection to join
      localField: "userId",       // Field from orders
      foreignField: "_id",        // Field from users
      as: "userDetails"           // Output array field
    }
  }
])

// Result:
{
  _id: ObjectId("..."),
  userId: ObjectId("user123"),
  amount: 100,
  userDetails: [                  // Joined data
    {
      _id: ObjectId("user123"),
      name: "John Doe",
      email: "john@example.com"
    }
  ]
}
```

**$unwind - Deconstruct Array**

```javascript
// Document with array
{
  _id: 1,
  name: "John",
  hobbies: ["reading", "coding", "gaming"]
}

// Unwind
db.users.aggregate([
  { $unwind: "$hobbies" }
])

// Result: Creates separate document for each array element
[
  { _id: 1, name: "John", hobbies: "reading" },
  { _id: 1, name: "John", hobbies: "coding" },
  { _id: 1, name: "John", hobbies: "gaming" }
]
```

### Real-World Examples

**Sales Report**

```javascript
db.orders.aggregate([
  // Filter by date range
  {
    $match: {
      orderDate: {
        $gte: new Date("2024-01-01"),
        $lt: new Date("2025-01-01")
      }
    }
  },
  // Group by month
  {
    $group: {
      _id: {
        year: { $year: "$orderDate" },
        month: { $month: "$orderDate" }
      },
      totalSales: { $sum: "$amount" },
      orderCount: { $sum: 1 },
      avgOrderValue: { $avg: "$amount" }
    }
  },
  // Sort by month
  {
    $sort: { "_id.year": 1, "_id.month": 1 }
  },
  // Format output
  {
    $project: {
      _id: 0,
      period: {
        $concat: [
          { $toString: "$_id.year" },
          "-",
          { $toString: "$_id.month" }
        ]
      },
      totalSales: 1,
      orderCount: 1,
      avgOrderValue: { $round: ["$avgOrderValue", 2] }
    }
  }
])
```

**User Analytics**

```javascript
db.users.aggregate([
  // Add computed fields
  {
    $addFields: {
      accountAge: {
        $dateDiff: {
          startDate: "$createdAt",
          endDate: "$$NOW",
          unit: "day"
        }
      }
    }
  },
  // Group by age range
  {
    $bucket: {
      groupBy: "$age",
      boundaries: [0, 18, 30, 50, 100],
      default: "Other",
      output: {
        count: { $sum: 1 },
        users: { $push: "$name" }
      }
    }
  }
])
```

---

## ⚡ Indexing & Performance {#indexing}

### What is an Index?

Indexes improve query performance by creating a sorted data structure.

```
Without Index (Collection Scan)
┌─────┬─────┬─────┬─────┬─────┐
│ Doc1│ Doc2│ Doc3│ Doc4│ Doc5│  ◄── Search all documents
└─────┴─────┴─────┴─────┴─────┘

With Index (Index Scan)
┌───────────────┐
│  Index (age)  │
├───────────────┤
│ 25 → Doc2     │
│ 30 → Doc1     │  ◄── Jump directly
│ 35 → Doc4     │
│ 40 → Doc3     │
│ 45 → Doc5     │
└───────────────┘
```

### Create Index

```javascript
// Single field index
db.users.createIndex({ email: 1 })     // Ascending
db.users.createIndex({ age: -1 })      // Descending

// Compound index (multiple fields)
db.users.createIndex({ age: 1, name: 1 })

// Unique index
db.users.createIndex({ email: 1 }, { unique: true })

// Text index (for text search)
db.articles.createIndex({ title: "text", content: "text" })

// TTL index (auto-delete after time)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }  // Delete after 1 hour
)
```

### View Indexes

```javascript
// List all indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")

// Drop all indexes (except _id)
db.users.dropIndexes()
```

### Explain Query

```javascript
// Analyze query performance
db.users.find({ email: "john@example.com" }).explain("executionStats")

// Key metrics:
// - executionTimeMillis: Query time
// - totalDocsExamined: Documents scanned
// - totalKeysExamined: Index entries scanned
// - executionStages.stage: IXSCAN (index) or COLLSCAN (full scan)
```

### Index Best Practices

```javascript
// ✅ Good: Index on frequently queried fields
db.users.createIndex({ email: 1 })

// ✅ Good: Compound index for common queries
db.orders.createIndex({ userId: 1, status: 1 })

// ✅ Good: Index on sort fields
db.products.createIndex({ price: -1 })

// ❌ Bad: Too many indexes (slows writes)
// ❌ Bad: Index on fields that change frequently
// ❌ Bad: Index on low-cardinality fields (few unique values)
```

---

## 🔄 Transactions {#transactions}

### ACID Transactions

MongoDB supports multi-document ACID transactions.

```javascript
const session = db.getMongo().startSession()
session.startTransaction()

try {
  // Transfer money between accounts
  const accounts = session.getDatabase("mydb").accounts
  
  // Withdraw from account 1
  accounts.updateOne(
    { _id: "account1" },
    { $inc: { balance: -100 } },
    { session }
  )
  
  // Deposit to account 2
  accounts.updateOne(
    { _id: "account2" },
    { $inc: { balance: 100 } },
    { session }
  )
  
  // Commit transaction
  session.commitTransaction()
  print("Transaction successful")
  
} catch (error) {
  // Rollback on error
  session.abortTransaction()
  print("Transaction failed:", error)
  
} finally {
  session.endSession()
}
```

---

## 🐘 Mongoose ODM {#mongoose}

### What is Mongoose?

Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js.

**Install**

```bash
npm install mongoose
```

### Connection

```javascript
const mongoose = require('mongoose')

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/myapp')
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Connection error:', err))
```

### Schema & Model

```javascript
const mongoose = require('mongoose')

// Define schema
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: 3,
    maxlength: 50
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    match: [/^\S+@\S+\.\S+$/, 'Please enter a valid email']
  },
  age: {
    type: Number,
    min: 18,
    max: 120
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
}, {
  timestamps: true  // Auto-add createdAt and updatedAt
})

// Create model
const User = mongoose.model('User', userSchema)

module.exports = User
```

### CRUD with Mongoose

```javascript
const User = require('./models/User')

// CREATE
const createUser = async () => {
  const user = new User({
    name: 'John Doe',
    email: 'john@example.com',
    age: 30
  })
  
  await user.save()
  // Or: await User.create({ name: 'John', email: '...' })
}

// READ
const getUsers = async () => {
  const users = await User.find()
  const john = await User.findOne({ email: 'john@example.com' })
  const userById = await User.findById('507f1f77bcf86cd799439011')
}

// UPDATE
const updateUser = async () => {
  const user = await User.findByIdAndUpdate(
    '507f1f77bcf86cd799439011',
    { age: 31 },
    { new: true, runValidators: true }
  )
}

// DELETE
const deleteUser = async () => {
  await User.findByIdAndDelete('507f1f77bcf86cd799439011')
  await User.deleteMany({ age: { $lt: 18 } })
}
```

### Middleware (Hooks)

```javascript
const bcrypt = require('bcryptjs')

// Pre-save hook
userSchema.pre('save', async function(next) {
  // Only hash if password is modified
  if (!this.isModified('password')) return next()
  
  // Hash password
  this.password = await bcrypt.hash(this.password, 10)
  next()
})

// Post-save hook
userSchema.post('save', function(doc, next) {
  console.log(`New user created: ${doc.name}`)
  next()
})
```

### Virtual Properties

```javascript
// Virtual property (not stored in DB)
userSchema.virtual('fullName').get(function() {
  return `${this.firstName} ${this.lastName}`
})

// Use in document
const user = await User.findById(id)
console.log(user.fullName)  // "John Doe"
```

### Instance Methods

```javascript
// Add custom method
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password)
}

// Use method
const user = await User.findOne({ email: 'john@example.com' })
const isMatch = await user.comparePassword('password123')
```

### Static Methods

```javascript
// Add static method
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email: email.toLowerCase() })
}

// Use static method
const user = await User.findByEmail('JOHN@EXAMPLE.COM')
```

### Population (References)

```javascript
// Author schema
const authorSchema = new mongoose.Schema({
  name: String,
  email: String
})

// Book schema with reference
const bookSchema = new mongoose.Schema({
  title: String,
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Author'
  }
})

const Author = mongoose.model('Author', authorSchema)
const Book = mongoose.model('Book', bookSchema)

// Create with reference
const author = await Author.create({ name: 'John Doe' })
const book = await Book.create({
  title: 'MongoDB Guide',
  author: author._id
})

// Populate reference
const bookWithAuthor = await Book.findById(book._id).populate('author')
console.log(bookWithAuthor.author.name)  // "John Doe"
```

---

## 🔒 Security & Authentication {#security}

### Enable Authentication

```bash
# Start MongoDB with auth
mongod --auth --dbpath /data/db

# Create admin user
use admin
db.createUser({
  user: "admin",
  pwd: "securePassword",
  roles: ["root"]
})

# Authenticate
db.auth("admin", "securePassword")
```

### User Management

```javascript
// Create database user
use myDatabase
db.createUser({
  user: "appUser",
  pwd: "appPassword",
  roles: [
    { role: "readWrite", db: "myDatabase" }
  ]
})

// Grant roles
db.grantRolesToUser("appUser", [
  { role: "dbAdmin", db: "myDatabase" }
])

// Revoke roles
db.revokeRolesFromUser("appUser", [
  { role: "dbAdmin", db: "myDatabase" }
])
```

### Connection with Auth

```javascript
// Mongoose connection with auth
mongoose.connect('mongodb://appUser:appPassword@localhost:27017/myDatabase')
```

### Encryption

```javascript
// Field-level encryption
const encryptedSchema = new mongoose.Schema({
  ssn: {
    type: String,
    encrypt: true  // Requires mongoose-encryption
  }
})
```

---

## 📈 Replication & Sharding {#scaling}

### Replication (High Availability)

```
┌─────────────┐
│   Primary   │ ◄──── Writes
└──────┬──────┘
       │
       ├──────► Secondary 1  ◄──── Reads
       │
       └──────► Secondary 2  ◄──── Reads
```

**Replica Set Benefits:**
- High availability
- Data redundancy
- Automatic failover
- Read scaling

### Sharding (Horizontal Scaling)

```
            ┌──────────────┐
            │   MongoDB    │
            │    Router    │
            └──────┬───────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
    ┌───▼───┐  ┌───▼───┐  ┌───▼───┐
    │Shard 1│  │Shard 2│  │Shard 3│
    │ A - H │  │ I - P │  │ Q - Z │
    └───────┘  └───────┘  └───────┘
```

---

## 💾 Backup & Recovery {#backup}

### Backup

```bash
# Backup entire database
mongodump --db myDatabase --out /backup/

# Backup specific collection
mongodump --db myDatabase --collection users --out /backup/

# Backup with authentication
mongodump --username admin --password pass --authenticationDatabase admin --db myDatabase --out /backup/
```

### Restore

```bash
# Restore database
mongorestore --db myDatabase /backup/myDatabase/

# Restore collection
mongorestore --db myDatabase --collection users /backup/myDatabase/users.bson
```

---

## ✅ Best Practices {#best-practices}

### 1. Schema Design
- Embed for 1-to-few relationships
- Reference for 1-to-many relationships
- Denormalize for performance
- Use schema validation

### 2. Indexing
- Index frequently queried fields
- Use compound indexes wisely
- Monitor index performance
- Remove unused indexes

### 3. Queries
- Use projection to limit fields
- Avoid $where operator
- Use covered queries (index-only)
- Paginate large result sets

### 4. Performance
- Use aggregation pipeline efficiently
- Enable query profiling
- Monitor slow queries
- Use connection pooling

### 5. Security
- Enable authentication
- Use role-based access control
- Encrypt sensitive data
- Regular backups

---

## 🎯 Real-World Projects {#projects}

### Project 1: E-commerce Database

```javascript
// Product Schema
const productSchema = new Schema({
  name: String,
  price: Number,
  category: String,
  inventory: Number,
  reviews: [{
    user: { type: ObjectId, ref: 'User' },
    rating: Number,
    comment: String
  }]
})

// Order Schema
const orderSchema = new Schema({
  user: { type: ObjectId, ref: 'User' },
  items: [{
    product: { type: ObjectId, ref: 'Product' },
    quantity: Number,
    price: Number
  }],
  totalAmount: Number,
  status: { type: String, enum: ['pending', 'shipped', 'delivered'] }
})
```

### Project 2: Social Media Platform

```javascript
// User with friends (many-to-many)
const userSchema = new Schema({
  username: String,
  friends: [{ type: ObjectId, ref: 'User' }],
  posts: [{ type: ObjectId, ref: 'Post' }]
})

// Post with comments
const postSchema = new Schema({
  author: { type: ObjectId, ref: 'User' },
  content: String,
  likes: [{ type: ObjectId, ref: 'User' }],
  comments: [{
    user: { type: ObjectId, ref: 'User' },
    text: String,
    createdAt: Date
  }]
})
```

---

## 🎓 Learning Path

### Beginner
1. ✅ Install MongoDB
2. ✅ Learn basic CRUD
3. ✅ Understand documents and collections
4. ✅ Practice query operators

### Intermediate
5. ✅ Master aggregation
6. ✅ Learn indexing
7. ✅ Use Mongoose ODM
8. ✅ Implement authentication

### Advanced
9. ✅ Design complex schemas
10. ✅ Optimize performance
11. ✅ Setup replication
12. ✅ Deploy to production

---

## 🏆 Congratulations!

You've completed the MongoDB Zero to Hero guide! You can now:

- ✅ Design flexible NoSQL schemas
- ✅ Perform complex queries and aggregations
- ✅ Optimize database performance
- ✅ Build production-ready applications
- ✅ Scale MongoDB horizontally

**Next Steps:**
- Build real-world projects
- Learn MongoDB Atlas (cloud)
- Explore advanced patterns
- Study MongoDB administration

Keep building! 🚀
