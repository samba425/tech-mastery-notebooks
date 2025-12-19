# Part 2: Backend Development with Python
## Hours 11-20 (Databases & Web APIs)

**Duration:** 10 hours total  
**Target:** Students who completed Python fundamentals  
**Format:** 1 hour per session  
**Style:** Read and teach directly, copy-paste examples

---

## 📚 TABLE OF CONTENTS

- [Hour 11: OOP Fundamentals](#hour-11)
- [Hour 12: Advanced OOP](#hour-12)
- [Hour 13: Virtual Environments & Dependencies](#hour-13)
- [Hour 14: SQL & Relational Databases](#hour-14)
- [Hour 15: ORMs (SQLAlchemy/Django ORM)](#hour-15)
- [Hour 16: NoSQL Basics (MongoDB)](#hour-16)
- [Hour 17: RESTful API Concepts](#hour-17)
- [Hour 18: Flask Part 1 (Basics)](#hour-18)
- [Hour 19: Flask Part 2 (Advanced)](#hour-19)
- [Hour 20: Authentication & Authorization](#hour-20)

---

<a name="hour-11"></a>
## 📅 Hour 11: OOP Fundamentals

### 🎯 Learning Objectives
- Understand classes and objects
- Create `__init__` constructor
- Differentiate class vs instance variables
- Build User and Post classes for a blog

### 📖 What to Teach

**"Today we learn Object-Oriented Programming (OOP) - think of it as creating blueprints for objects, like a car factory!"**

---

### 1️⃣ What is OOP? (10 minutes)

**Real-Life Analogy:**

```
Car Factory:
├── Blueprint (Class) → Design of a car
└── Actual Cars (Objects) → Individual cars made from blueprint

Each car has:
- Properties: color, brand, price (Attributes)
- Actions: start(), drive(), stop() (Methods)
```

**In Python Terms:**

```python
# Class = Blueprint
class Car:
    pass

# Objects = Individual cars
car1 = Car()  # First car
car2 = Car()  # Second car
car3 = Car()  # Third car
```

---

### 2️⃣ Creating a Simple Class (10 minutes)

**Basic Class Structure:**

```python
# Define a class (blueprint for a user)
class User:
    # Attributes (properties)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    # Methods (actions)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
    
    def greet(self):
        print(f"Hello, I'm {self.name}!")

# Create objects (individual users)
user1 = User("Alice", "alice@email.com", 25)
user2 = User("Bob", "bob@email.com", 30)

# Use methods
user1.display_info()
user1.greet()
```

**Output:**
```
Name: Alice
Email: alice@email.com
Age: 25
Hello, I'm Alice!
```

---

### 3️⃣ Understanding __init__ (Constructor) (10 minutes)

**Explain to Students:**

"`__init__` is a special method that automatically runs when you create an object. Like a setup function!"

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # self = this specific account
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account created for {account_holder}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

# __init__ is called automatically
account1 = BankAccount("Alice", 5000)  # Account created for Alice
account2 = BankAccount("Bob", 10000)   # Account created for Bob

# Use methods
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()
```

---

### 4️⃣ Class Variables vs Instance Variables (10 minutes)

**Explain the Difference:**

```python
class Employee:
    # CLASS VARIABLE (shared by all employees)
    company_name = "Tech Corp"
    total_employees = 0
    
    def __init__(self, name, salary):
        # INSTANCE VARIABLES (unique to each employee)
        self.name = name
        self.salary = salary
        Employee.total_employees += 1  # Increment class variable
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")
        print(f"Company: {Employee.company_name}")

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 70000)

# Class variable is shared
print(f"Total employees: {Employee.total_employees}")  # 3
print(f"Company: {Employee.company_name}")  # Tech Corp

# Instance variables are unique
print(f"Employee 1 salary: ₹{emp1.salary}")  # 50000
print(f"Employee 2 salary: ₹{emp2.salary}")  # 60000
```

**Visual Diagram:**

```
Employee Class
├── company_name = "Tech Corp"  (SHARED by all)
├── total_employees = 3          (SHARED by all)
│
├── emp1:
│   ├── name = "Alice"           (UNIQUE)
│   └── salary = 50000           (UNIQUE)
│
├── emp2:
│   ├── name = "Bob"             (UNIQUE)
│   └── salary = 60000           (UNIQUE)
│
└── emp3:
    ├── name = "Charlie"         (UNIQUE)
    └── salary = 70000           (UNIQUE)
```

---

### 5️⃣ Methods (Instance Methods) (10 minutes)

**Different Types of Methods:**

```python
class Calculator:
    def __init__(self, name):
        self.name = name
        self.history = []
    
    # Instance method (uses self)
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def show_history(self):
        print(f"\n{self.name}'s Calculation History:")
        for calculation in self.history:
            print(f"  - {calculation}")

# Create calculator objects
calc1 = Calculator("Alice's Calculator")
calc2 = Calculator("Bob's Calculator")

# Use methods
calc1.add(10, 5)
calc1.multiply(4, 3)
calc1.show_history()

calc2.add(100, 200)
calc2.show_history()
```

**Output:**
```
Alice's Calculator's Calculation History:
  - 10 + 5 = 15
  - 4 × 3 = 12

Bob's Calculator's Calculation History:
  - 100 + 200 = 300
```

---

### 💻 Live Activity: Blog System (User & Post Classes)

**Copy-Paste for Students:**

```python
# activity11_blog_system.py

class User:
    """Represents a blog user"""
    
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio
        self.posts = []  # List to store user's posts
    
    def create_post(self, title, content):
        """Create a new blog post"""
        post = Post(title, content, self.username)
        self.posts.append(post)
        print(f"✅ Post '{title}' created successfully!")
        return post
    
    def display_profile(self):
        """Display user profile"""
        print("\n" + "=" * 50)
        print(f"👤 User Profile")
        print("=" * 50)
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio}")
        print(f"Total Posts: {len(self.posts)}")
        print("=" * 50)
    
    def show_all_posts(self):
        """Display all posts by this user"""
        print(f"\n📝 Posts by {self.username}:")
        print("-" * 50)
        if self.posts:
            for i, post in enumerate(self.posts, 1):
                print(f"\n{i}. {post.title}")
                print(f"   {post.content[:50]}...")
        else:
            print("No posts yet.")


class Post:
    """Represents a blog post"""
    
    post_count = 0  # Class variable to track total posts
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes = 0
        self.comments = []
        Post.post_count += 1
        self.post_id = Post.post_count
    
    def like(self):
        """Like the post"""
        self.likes += 1
        print(f"❤️ Post liked! Total likes: {self.likes}")
    
    def add_comment(self, username, comment_text):
        """Add a comment to the post"""
        comment = {
            "username": username,
            "text": comment_text
        }
        self.comments.append(comment)
        print(f"💬 Comment added by {username}")
    
    def display_post(self):
        """Display post details"""
        print("\n" + "=" * 50)
        print(f"📄 Post #{self.post_id}")
        print("=" * 50)
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"\n{self.content}\n")
        print(f"❤️ Likes: {self.likes}")
        print(f"💬 Comments: {len(self.comments)}")
        
        if self.comments:
            print("\nComments:")
            for comment in self.comments:
                print(f"  - {comment['username']}: {comment['text']}")
        print("=" * 50)


# === DEMO THE SYSTEM ===

# Create users
user1 = User("alice_dev", "alice@email.com", "Python developer 🐍")
user2 = User("bob_tech", "bob@email.com", "Full-stack engineer 💻")

# Show profiles
user1.display_profile()
user2.display_profile()

# Create posts
post1 = user1.create_post(
    "Getting Started with Python",
    "Python is an amazing language for beginners. In this post, I'll show you how to get started with Python programming..."
)

post2 = user1.create_post(
    "10 Python Tips",
    "Here are my top 10 Python tips that will make you a better programmer..."
)

post3 = user2.create_post(
    "Building REST APIs with Flask",
    "Flask is a lightweight web framework for Python. Let's build a simple REST API..."
)

# Interact with posts
post1.display_post()
post1.like()
post1.like()
post1.add_comment("bob_tech", "Great post! Very helpful!")
post1.add_comment("charlie", "Thanks for sharing!")
post1.display_post()

# Show all posts by user
user1.show_all_posts()

# Show statistics
print(f"\n📊 Blog Statistics:")
print(f"Total Posts: {Post.post_count}")
print(f"Total Users: 2")
```

**Run this and show output to students!**

---

### 🏠 Homework: Add Serialization to Models

**Task:** Add methods to convert objects to dictionaries/JSON

```python
# homework11_serialization.py

import json

class User:
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio
        self.posts = []
    
    # TODO: Add this method
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            "username": self.username,
            "email": self.email,
            "bio": self.bio,
            "post_count": len(self.posts)
        }
    
    # TODO: Add this method
    def to_json(self):
        """Convert user object to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes = 0
    
    # TODO: Add this method
    def to_dict(self):
        """Convert post object to dictionary"""
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "likes": self.likes
        }
    
    # TODO: Add this method
    def to_json(self):
        """Convert post object to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


# Test the serialization
user = User("alice", "alice@email.com", "Developer")
post = Post("Python Tips", "Here are some tips...", "alice")

print("User as dict:", user.to_dict())
print("\nUser as JSON:")
print(user.to_json())

print("\nPost as dict:", post.to_dict())
print("\nPost as JSON:")
print(post.to_json())
```

**Expected Output:**
```json
User as JSON:
{
  "username": "alice",
  "email": "alice@email.com",
  "bio": "Developer",
  "post_count": 0
}

Post as JSON:
{
  "title": "Python Tips",
  "content": "Here are some tips...",
  "author": "alice",
  "likes": 0
}
```

---

### 📝 Key Takeaways

✅ Class = Blueprint, Object = Instance
✅ `__init__` = Constructor (auto-runs)
✅ `self` = refers to current instance
✅ Instance variables = unique to each object
✅ Class variables = shared by all objects
✅ Methods = functions inside classes

---

<a name="hour-14"></a>
## 📅 Hour 14: SQL & Relational Databases

### 🎯 Learning Objectives
- Understand relational databases
- Learn SQL CRUD operations
- Work with SQLite
- Create tables, insert/query data
- Design schema for a blog

### 📖 What to Teach

**"Today we learn databases - think of it as an Excel spreadsheet on steroids!"**

---

### 1️⃣ What is a Database? (10 minutes)

**Real-Life Analogy:**

```
Filing Cabinet (Database)
├── Drawer 1: Customers (Table)
│   ├── John, john@email.com, 25
│   ├── Alice, alice@email.com, 30
│   └── Bob, bob@email.com, 28
│
└── Drawer 2: Orders (Table)
    ├── Order #1, John, ₹500
    ├── Order #2, Alice, ₹1000
    └── Order #3, Bob, ₹750
```

**Relational Database Concepts:**

```
Database: blog_db
├── Table: users
│   ├── Columns: id, username, email, created_at
│   └── Rows: Individual users
│
└── Table: posts
    ├── Columns: id, title, content, author_id, created_at
    └── Rows: Individual posts
```

**Why Use Databases?**
- Store large amounts of data
- Fast searching
- Data relationships
- Data integrity
- Concurrent access
- Backup and recovery

---

### 2️⃣ SQL Basics (10 minutes)

**SQL = Structured Query Language**

"SQL is the language we use to talk to databases!"

**4 Main Operations (CRUD):**

```sql
CREATE (INSERT) - Add new data
READ (SELECT)   - Get data
UPDATE          - Modify data
DELETE          - Remove data
```

**Basic SQL Syntax:**

```sql
-- Create table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT
);

-- Insert data (CREATE)
INSERT INTO users (username, email) 
VALUES ('alice', 'alice@email.com');

-- Read data (READ)
SELECT * FROM users;

-- Update data (UPDATE)
UPDATE users 
SET email = 'newemail@email.com' 
WHERE username = 'alice';

-- Delete data (DELETE)
DELETE FROM users 
WHERE username = 'alice';
```

---

### 3️⃣ Working with SQLite in Python (15 minutes)

**SQLite Setup:**

"SQLite is built into Python - no installation needed! It's like a mini-database in a file."

```python
import sqlite3

# Connect to database (creates file if doesn't exist)
conn = sqlite3.connect('blog.db')

# Create cursor (like a pointer)
cursor = conn.cursor()

# Execute SQL
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Save changes
conn.commit()

# Close connection
conn.close()
```

---

### 4️⃣ CRUD Operations in Python (15 minutes)

**Complete Example:**

```python
# crud_demo.py

import sqlite3

class Database:
    def __init__(self, db_name='blog.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Create tables if they don't exist"""
        # Users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                bio TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Posts table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                likes INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author_id) REFERENCES users (id)
            )
        ''')
        
        self.conn.commit()
        print("✅ Tables created successfully!")
    
    # ========== CREATE ==========
    def create_user(self, username, email, bio=''):
        """Insert new user"""
        try:
            self.cursor.execute('''
                INSERT INTO users (username, email, bio)
                VALUES (?, ?, ?)
            ''', (username, email, bio))
            self.conn.commit()
            print(f"✅ User '{username}' created!")
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"❌ User '{username}' already exists!")
            return None
    
    def create_post(self, title, content, author_id):
        """Insert new post"""
        self.cursor.execute('''
            INSERT INTO posts (title, content, author_id)
            VALUES (?, ?, ?)
        ''', (title, content, author_id))
        self.conn.commit()
        print(f"✅ Post '{title}' created!")
        return self.cursor.lastrowid
    
    # ========== READ ==========
    def get_all_users(self):
        """Get all users"""
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
    
    def get_user_by_username(self, username):
        """Get user by username"""
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()
    
    def get_posts_by_author(self, author_id):
        """Get all posts by an author"""
        self.cursor.execute('''
            SELECT * FROM posts WHERE author_id = ?
        ''', (author_id,))
        return self.cursor.fetchall()
    
    # ========== UPDATE ==========
    def update_user_bio(self, username, new_bio):
        """Update user's bio"""
        self.cursor.execute('''
            UPDATE users SET bio = ? WHERE username = ?
        ''', (new_bio, username))
        self.conn.commit()
        print(f"✅ Updated bio for '{username}'")
    
    def like_post(self, post_id):
        """Increment post likes"""
        self.cursor.execute('''
            UPDATE posts SET likes = likes + 1 WHERE id = ?
        ''', (post_id,))
        self.conn.commit()
        print(f"❤️ Post #{post_id} liked!")
    
    # ========== DELETE ==========
    def delete_user(self, username):
        """Delete user"""
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.conn.commit()
        print(f"🗑️ User '{username}' deleted!")
    
    def delete_post(self, post_id):
        """Delete post"""
        self.cursor.execute('''
            DELETE FROM posts WHERE id = ?
        ''', (post_id,))
        self.conn.commit()
        print(f"🗑️ Post #{post_id} deleted!")
    
    def close(self):
        """Close database connection"""
        self.conn.close()


# ========== DEMO ==========

def demo():
    db = Database()
    
    # CREATE users
    user1_id = db.create_user('alice', 'alice@email.com', 'Python developer')
    user2_id = db.create_user('bob', 'bob@email.com', 'Full-stack engineer')
    
    # CREATE posts
    db.create_post('Python Basics', 'Learn Python...', user1_id)
    db.create_post('Web Development', 'Build websites...', user1_id)
    db.create_post('Flask Tutorial', 'Getting started...', user2_id)
    
    # READ all users
    print("\n📋 All Users:")
    users = db.get_all_users()
    for user in users:
        print(f"  ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    
    # READ specific user
    print("\n👤 User Details:")
    alice = db.get_user_by_username('alice')
    print(f"  {alice}")
    
    # READ posts by author
    print("\n📝 Alice's Posts:")
    posts = db.get_posts_by_author(user1_id)
    for post in posts:
        print(f"  ID: {post[0]}, Title: {post[1]}, Likes: {post[4]}")
    
    # UPDATE
    db.update_user_bio('alice', 'Senior Python Developer 🐍')
    
    # LIKE posts
    db.like_post(1)
    db.like_post(1)
    db.like_post(1)
    
    db.close()


if __name__ == '__main__':
    demo()
```

---

### 5️⃣ SQL Joins (10 minutes)

**Explain Joins:**

"Joins combine data from multiple tables - like matching puzzle pieces!"

```python
def get_posts_with_authors(self):
    """Get posts with author information (JOIN)"""
    self.cursor.execute('''
        SELECT 
            posts.id,
            posts.title,
            posts.content,
            posts.likes,
            users.username,
            users.email
        FROM posts
        INNER JOIN users ON posts.author_id = users.id
        ORDER BY posts.created_at DESC
    ''')
    return self.cursor.fetchall()

# Usage
posts_with_authors = db.get_posts_with_authors()
for post in posts_with_authors:
    print(f"Post: {post[1]} by {post[4]} (Likes: {post[3]})")
```

**Output:**
```
Post: Flask Tutorial by bob (Likes: 0)
Post: Web Development by alice (Likes: 0)
Post: Python Basics by alice (Likes: 3)
```

---

### 💻 Live Activity: Build Blog Database

**Students run the complete demo above and see:**
- Tables created
- Users inserted
- Posts created
- Data queried
- Records updated
- Likes incremented

---

### 🏠 Homework: Design Complete Blog Schema

**Task:** Design and implement a complete blog database schema

```sql
-- homework14_blog_schema.sql

-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    bio TEXT,
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TODO: Add posts table with these columns:
-- id, title, content, author_id, likes, views, created_at, updated_at

-- TODO: Add comments table with these columns:
-- id, post_id, user_id, content, created_at

-- TODO: Add categories table:
-- id, name, description

-- TODO: Add post_categories junction table (many-to-many):
-- post_id, category_id

-- TODO: Add follows table (user following system):
-- follower_id, following_id, created_at
```

**Implement in Python and test with sample data!**

---

### 📝 Key Takeaways

✅ SQL = language for databases
✅ CRUD = Create, Read, Update, Delete
✅ SQLite = built-in Python database
✅ Primary Key = unique identifier
✅ Foreign Key = links tables
✅ JOIN = combines tables

---

<a name="hour-12"></a>
## 📅 Hour 12: Advanced OOP

### 🎯 Learning Objectives
- Master inheritance and polymorphism
- Use magic methods (`__str__`, `__repr__`)
- Understand dataclasses
- Build payment processing system

### 📖 What to Teach

**"Inheritance = Child classes inherit from parent classes, like children inherit traits from parents!"**

---

### 1️⃣ Inheritance (15 minutes)

**Basic Inheritance:**

```python
# Parent class (base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child classes
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Call parent __init__
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def make_sound(self):  # Override parent method
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())        # Buddy is a Dog
print(dog.make_sound())  # Woof!
print(dog.fetch())       # Buddy is fetching the ball!

print(cat.info())        # Whiskers is a Cat
print(cat.make_sound())  # Meow!
print(cat.scratch())     # Whiskers is scratching the furniture!
```

**Multi-Level Inheritance:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        return f"Driving {self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return f"Charging {self.battery_capacity}kWh battery"

# Usage
tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())   # Tesla vehicle started
print(tesla.drive())   # Driving Tesla Model 3
print(tesla.charge())  # Charging 75kWh battery
```

---

### 2️⃣ Polymorphism (10 minutes)

**Explain:**

"Polymorphism = Same method name, different behavior based on object type"

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")

# Output:
# Rectangle area: 50
# Circle area: 153.93804
# Triangle area: 24.0
```

---

### 3️⃣ Magic Methods (15 minutes)

**Common Magic Methods:**

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users (print)"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """String representation for developers (debugging)"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of book (pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Check if two books are equal"""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Less than comparison (by pages)"""
        return self.pages < other.pages

# Usage
book1 = Book("Python Basics", "Alice", 300)
book2 = Book("Advanced Python", "Bob", 450)

print(book1)           # 'Python Basics' by Alice
print(repr(book1))     # Book('Python Basics', 'Alice', 300)
print(len(book1))      # 300
print(book1 == book2)  # False
print(book1 < book2)   # True (300 < 450)

# Sorting books by pages
books = [book2, book1]
books.sort()
for book in books:
    print(book)
```

**More Magic Methods:**

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"{self.owner}'s account: ₹{self.balance}"
    
    def __add__(self, amount):
        """Add money (deposit)"""
        self.balance += amount
        return self
    
    def __sub__(self, amount):
        """Subtract money (withdraw)"""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self
    
    def __call__(self):
        """Make object callable"""
        return f"Balance: ₹{self.balance}"

# Usage
account = BankAccount("Alice", 1000)
print(account)       # Alice's account: ₹1000

account + 500        # Deposit
print(account())     # Balance: ₹1500

account - 200        # Withdraw
print(account())     # Balance: ₹1300
```

---

### 4️⃣ Dataclasses (10 minutes)

**Traditional Class:**

```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, city='{self.city}')"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
```

**Using Dataclass (Simpler!):**

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

# Automatically creates __init__, __repr__, __eq__, etc.
person = Person("Alice", 25, "Mumbai")
print(person)  # Person(name='Alice', age=25, city='Mumbai')
```

**Dataclass with Defaults:**

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list = field(default_factory=list)
    
    def total_value(self):
        return self.price * self.quantity

# Usage
product = Product("Laptop", 50000, 10)
print(product)
print(f"Total value: ₹{product.total_value()}")

product2 = Product("Mouse", 500)
print(product2)
```

---

### 5️⃣ Abstract Classes (10 minutes)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processors"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        """Must be implemented by subclasses"""
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ₹{amount} via Credit Card"
    
    def refund(self, transaction_id):
        return f"Refunding transaction {transaction_id}"

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ₹{amount} via UPI"
    
    def refund(self, transaction_id):
        return f"Refunding UPI transaction {transaction_id}"

# Cannot instantiate abstract class
# processor = PaymentProcessor()  # Error!

# Can instantiate concrete classes
cc_processor = CreditCardProcessor()
print(cc_processor.process_payment(1000))

upi_processor = UPIProcessor()
print(upi_processor.process_payment(500))
```

---

### 💻 Live Activity: Payment System

**Create: hour12_payment_system.py**

```python
"""
Payment Processing System
Demonstrates inheritance, polymorphism, and magic methods
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"

@dataclass
class Transaction:
    transaction_id: str
    amount: float
    status: PaymentStatus
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

class PaymentMethod(ABC):
    """Abstract base class for payment methods"""
    
    def __init__(self):
        self.transactions = []
    
    @abstractmethod
    def process_payment(self, amount, description=""):
        """Process a payment"""
        pass
    
    @abstractmethod
    def get_fee(self, amount):
        """Calculate processing fee"""
        pass
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    def get_transaction_history(self):
        return self.transactions

class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv, expiry):
        super().__init__()
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.cvv = cvv
        self.expiry = expiry
    
    def process_payment(self, amount, description=""):
        fee = self.get_fee(amount)
        total = amount + fee
        
        # Simulate payment processing
        transaction_id = f"CC-{len(self.transactions) + 1:05d}"
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=total,
            status=PaymentStatus.SUCCESS
        )
        
        self.add_transaction(transaction)
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "fee": fee,
            "total": total,
            "message": f"Paid ₹{total} via Credit Card (****{self.card_number})"
        }
    
    def get_fee(self, amount):
        return amount * 0.02  # 2% fee

class DebitCard(PaymentMethod):
    def __init__(self, card_number, pin):
        super().__init__()
        self.card_number = card_number[-4:]
        self.pin = pin
    
    def process_payment(self, amount, description=""):
        fee = self.get_fee(amount)
        total = amount + fee
        
        transaction_id = f"DC-{len(self.transactions) + 1:05d}"
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=total,
            status=PaymentStatus.SUCCESS
        )
        
        self.add_transaction(transaction)
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "fee": fee,
            "total": total,
            "message": f"Paid ₹{total} via Debit Card (****{self.card_number})"
        }
    
    def get_fee(self, amount):
        return 0  # No fee

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        super().__init__()
        self.upi_id = upi_id
    
    def process_payment(self, amount, description=""):
        fee = self.get_fee(amount)
        total = amount + fee
        
        transaction_id = f"UPI-{len(self.transactions) + 1:05d}"
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=total,
            status=PaymentStatus.SUCCESS
        )
        
        self.add_transaction(transaction)
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "fee": fee,
            "total": total,
            "message": f"Paid ₹{total} via UPI ({self.upi_id})"
        }
    
    def get_fee(self, amount):
        return 0  # No fee

class Wallet(PaymentMethod):
    def __init__(self, balance=0):
        super().__init__()
        self.balance = balance
    
    def add_money(self, amount):
        self.balance += amount
        return f"Added ₹{amount}. New balance: ₹{self.balance}"
    
    def process_payment(self, amount, description=""):
        if self.balance < amount:
            return {
                "success": False,
                "message": f"Insufficient balance. Available: ₹{self.balance}"
            }
        
        fee = self.get_fee(amount)
        total = amount + fee
        
        self.balance -= total
        
        transaction_id = f"WALLET-{len(self.transactions) + 1:05d}"
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=total,
            status=PaymentStatus.SUCCESS
        )
        
        self.add_transaction(transaction)
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "fee": fee,
            "total": total,
            "balance": self.balance,
            "message": f"Paid ₹{total} via Wallet. Remaining: ₹{self.balance}"
        }
    
    def get_fee(self, amount):
        return 0  # No fee

class PaymentGateway:
    """Main payment gateway to handle all payment methods"""
    
    def __init__(self):
        self.payment_methods = {}
    
    def add_payment_method(self, name, payment_method):
        self.payment_methods[name] = payment_method
    
    def process_payment(self, method_name, amount, description=""):
        if method_name not in self.payment_methods:
            return {"success": False, "message": "Payment method not found"}
        
        payment_method = self.payment_methods[method_name]
        return payment_method.process_payment(amount, description)
    
    def get_all_transactions(self):
        all_transactions = []
        for name, method in self.payment_methods.items():
            for transaction in method.get_transaction_history():
                all_transactions.append({
                    "method": name,
                    "transaction": transaction
                })
        return all_transactions

# Demo
print("=== PAYMENT PROCESSING SYSTEM ===\n")

# Create payment gateway
gateway = PaymentGateway()

# Add payment methods
gateway.add_payment_method("credit_card", CreditCard("1234567890123456", "123", "12/26"))
gateway.add_payment_method("debit_card", DebitCard("9876543210987654", "1234"))
gateway.add_payment_method("upi", UPI("alice@upi"))
gateway.add_payment_method("wallet", Wallet(balance=5000))

# Process payments
print("1. Credit Card Payment:")
result = gateway.process_payment("credit_card", 1000, "Shopping")
print(result["message"])
print(f"   Fee: ₹{result['fee']}\n")

print("2. Debit Card Payment:")
result = gateway.process_payment("debit_card", 500)
print(result["message"])
print(f"   Fee: ₹{result['fee']}\n")

print("3. UPI Payment:")
result = gateway.process_payment("upi", 750)
print(result["message"])
print(f"   Fee: ₹{result['fee']}\n")

print("4. Wallet Payment:")
result = gateway.process_payment("wallet", 300)
print(result["message"])
print(f"   Fee: ₹{result['fee']}\n")

# Show transaction history
print("=== TRANSACTION HISTORY ===")
transactions = gateway.get_all_transactions()
for item in transactions:
    trans = item["transaction"]
    print(f"{item['method']}: {trans.transaction_id} - ₹{trans.amount} ({trans.status.value})")
```

---

### 🏠 Homework: E-commerce System

```python
# homework12_ecommerce.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# TODO: Create abstract Product class with:
# - name, price, stock
# - abstract method: calculate_discount()

# TODO: Create concrete product classes:
# - Electronics (10% discount)
# - Clothing (20% discount)
# - Books (15% discount)

# TODO: Create ShoppingCart class with:
# - add_item(product, quantity)
# - remove_item(product)
# - calculate_total()
# - apply_coupon(code, discount_percent)

# TODO: Create Order class with:
# - order_id, customer, items, total, status
# - Magic methods: __str__, __repr__

# TODO: Test the complete system
```

---

### 📝 Key Takeaways

✅ Inheritance = child classes extend parent
✅ `super()` calls parent method
✅ Polymorphism = same method, different behavior
✅ Magic methods = `__str__`, `__repr__`, `__eq__`, etc.
✅ Dataclasses = automatic method generation
✅ Abstract classes = templates for subclasses

---

<a name="hour-13"></a>
## 📅 Hour 13: Virtual Environments & Dependencies

### 🎯 Learning Objectives
- Master virtual environments
- Use pip effectively
- Create requirements.txt
- Understand pyproject.toml
- Use Poetry for dependency management

### 📖 What to Teach

**"Virtual environments = separate Python installations for each project!"**

---

### 1️⃣ Why Virtual Environments? (10 minutes)

**The Problem:**

```
System Python (Global):
├── Django 3.0
├── Flask 1.1
└── requests 2.25

Project A needs Django 4.0  ❌ Conflict!
Project B needs Flask 2.0   ❌ Conflict!
```

**The Solution:**

```
System Python
├── Project A (venv)
│   ├── Django 4.0 ✅
│   └── requests 2.28
└── Project B (venv)
    ├── Flask 2.0 ✅
    └── requests 2.31
```

---

### 2️⃣ Creating Virtual Environments (15 minutes)

**Using venv (Built-in):**

```bash
# Create virtual environment
python -m venv myenv

# Activate (macOS/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Verify activation (prompt shows (myenv))
which python  # Should show myenv/bin/python

# Deactivate
deactivate
```

**Project Setup Workflow:**

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate
source venv/bin/activate

# 4. Install packages
pip install flask requests

# 5. Create requirements.txt
pip freeze > requirements.txt

# 6. Work on project...

# 7. Deactivate when done
deactivate
```

---

### 3️⃣ Managing Dependencies with pip (15 minutes)

**Common pip Commands:**

```bash
# Install package
pip install requests

# Install specific version
pip install flask==2.3.0

# Install with version constraints
pip install "django>=4.0,<5.0"

# Install from requirements.txt
pip install -r requirements.txt

# Upgrade package
pip install --upgrade requests

# Uninstall package
pip uninstall requests

# List installed packages
pip list

# Show package details
pip show flask

# Search packages (deprecated, use pypi.org)
# pip search django

# Check outdated packages
pip list --outdated

# Freeze (save installed packages)
pip freeze > requirements.txt
```

**requirements.txt Example:**

```txt
# requirements.txt

# Web Framework
flask==2.3.0
flask-cors==4.0.0

# Database
sqlalchemy==2.0.0
psycopg2-binary==2.9.5

# Utilities
python-dotenv==1.0.0
requests==2.31.0

# Development only
pytest==7.4.0
black==23.7.0
```

**Development vs Production:**

```txt
# requirements-dev.txt (development)
pytest==7.4.0
black==23.7.0
flake8==6.1.0
mypy==1.5.0

# requirements-prod.txt (production)
gunicorn==21.2.0
psycopg2-binary==2.9.5
```

---

### 4️⃣ Modern Dependency Management with Poetry (10 minutes)

**Installing Poetry:**

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Or with pip
pip install poetry
```

**Using Poetry:**

```bash
# Create new project
poetry new my_project
cd my_project

# Or initialize in existing project
poetry init

# Add dependencies
poetry add flask
poetry add requests

# Add dev dependencies
poetry add --group dev pytest black

# Install all dependencies
poetry install

# Update dependencies
poetry update

# Show installed packages
poetry show

# Run script in virtual environment
poetry run python app.py

# Activate poetry shell
poetry shell
```

**pyproject.toml Example:**

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
flask = "^2.3.0"
sqlalchemy = "^2.0.0"
requests = "^2.31.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
black = "^23.7.0"
flake8 = "^6.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

### 5️⃣ Project Structure Best Practices (10 minutes)

**Standard Python Project Structure:**

```
my_project/
├── venv/                  # Virtual environment
├── src/                   # Source code
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/                 # Test files
│   ├── __init__.py
│   ├── test_models.py
│   └── test_services.py
├── docs/                  # Documentation
├── .env                   # Environment variables
├── .gitignore            # Git ignore file
├── requirements.txt      # Dependencies
├── README.md             # Project README
└── setup.py              # Package setup
```

**.gitignore for Python:**

```gitignore
# Virtual environments
venv/
env/
ENV/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
dist/
build/
*.egg-info/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# Database
*.db
*.sqlite3

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```

---

### 💻 Live Activity: Project Setup Script

**Create: hour13_project_setup.py**

```python
"""
Automated Project Setup Script
Creates a complete Python project structure
"""

import os
import sys
import subprocess
from pathlib import Path

class ProjectSetup:
    def __init__(self, project_name):
        self.project_name = project_name
        self.project_path = Path(project_name)
    
    def create_directory_structure(self):
        """Create project folders"""
        print(f"Creating project structure for '{self.project_name}'...")
        
        directories = [
            self.project_path,
            self.project_path / "src",
            self.project_path / "src" / "models",
            self.project_path / "src" / "services",
            self.project_path / "src" / "utils",
            self.project_path / "tests",
            self.project_path / "docs",
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created {directory}")
    
    def create_init_files(self):
        """Create __init__.py files"""
        print("\nCreating __init__.py files...")
        
        init_files = [
            self.project_path / "src" / "__init__.py",
            self.project_path / "src" / "models" / "__init__.py",
            self.project_path / "src" / "services" / "__init__.py",
            self.project_path / "src" / "utils" / "__init__.py",
            self.project_path / "tests" / "__init__.py",
        ]
        
        for init_file in init_files:
            init_file.touch()
            print(f"  ✓ Created {init_file}")
    
    def create_main_file(self):
        """Create main.py"""
        print("\nCreating main.py...")
        
        main_content = '''"""
Main application file
"""

def main():
    print("Hello from {}!")

if __name__ == "__main__":
    main()
'''.format(self.project_name)
        
        main_file = self.project_path / "src" / "main.py"
        main_file.write_text(main_content)
        print(f"  ✓ Created {main_file}")
    
    def create_readme(self):
        """Create README.md"""
        print("\nCreating README.md...")
        
        readme_content = f'''# {self.project_name}

## Description
Brief description of your project.

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\\Scripts\\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```

## Testing

```bash
pytest tests/
```

## License
MIT License
'''
        
        readme_file = self.project_path / "README.md"
        readme_file.write_text(readme_content)
        print(f"  ✓ Created {readme_file}")
    
    def create_requirements(self):
        """Create requirements.txt"""
        print("\nCreating requirements.txt...")
        
        requirements_content = '''# Core dependencies
requests==2.31.0
python-dotenv==1.0.0

# Development dependencies
pytest==7.4.0
black==23.7.0
flake8==6.1.0
'''
        
        req_file = self.project_path / "requirements.txt"
        req_file.write_text(requirements_content)
        print(f"  ✓ Created {req_file}")
    
    def create_gitignore(self):
        """Create .gitignore"""
        print("\nCreating .gitignore...")
        
        gitignore_content = '''# Virtual environments
venv/
env/
ENV/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env
.env.local

# Database
*.db
*.sqlite3

# IDE
.vscode/
.idea/

# OS
.DS_Store
'''
        
        gitignore_file = self.project_path / ".gitignore"
        gitignore_file.write_text(gitignore_content)
        print(f"  ✓ Created {gitignore_file}")
    
    def create_env_file(self):
        """Create .env file"""
        print("\nCreating .env file...")
        
        env_content = '''# Environment variables
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
'''
        
        env_file = self.project_path / ".env"
        env_file.write_text(env_content)
        print(f"  ✓ Created {env_file}")
    
    def create_virtual_environment(self):
        """Create virtual environment"""
        print("\nCreating virtual environment...")
        
        venv_path = self.project_path / "venv"
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)])
        print(f"  ✓ Created virtual environment at {venv_path}")
    
    def setup(self):
        """Run complete setup"""
        print(f"\n{'='*60}")
        print(f"  PROJECT SETUP: {self.project_name}")
        print(f"{'='*60}\n")
        
        self.create_directory_structure()
        self.create_init_files()
        self.create_main_file()
        self.create_readme()
        self.create_requirements()
        self.create_gitignore()
        self.create_env_file()
        self.create_virtual_environment()
        
        print(f"\n{'='*60}")
        print("  ✅ PROJECT SETUP COMPLETE!")
        print(f"{'='*60}\n")
        
        print("Next steps:")
        print(f"  1. cd {self.project_name}")
        print("  2. source venv/bin/activate")
        print("  3. pip install -r requirements.txt")
        print("  4. python src/main.py")

# Demo
if __name__ == "__main__":
    project_name = input("Enter project name: ").strip()
    
    if not project_name:
        print("Error: Project name cannot be empty!")
        sys.exit(1)
    
    setup = ProjectSetup(project_name)
    setup.setup()
```

---

### 🏠 Homework: Multi-Environment Setup

```python
# homework13_environments.py

# TODO: Create a script that sets up different environments:

# 1. Development environment
# - Install dev dependencies (pytest, black, flake8)
# - Set DEBUG=True
# - Use SQLite database

# 2. Production environment
# - Install production dependencies only
# - Set DEBUG=False
# - Use PostgreSQL database
# - Add gunicorn

# 3. Testing environment
# - Install test dependencies
# - Use in-memory database
# - Set TEST=True

# Create separate requirements files:
# - requirements-dev.txt
# - requirements-prod.txt
# - requirements-test.txt

# Write setup script that:
# - Detects current environment
# - Installs appropriate dependencies
# - Sets correct environment variables
```

---

### 📝 Key Takeaways

✅ Virtual environments isolate project dependencies
✅ `python -m venv venv` creates environment
✅ `source venv/bin/activate` activates it
✅ `pip freeze > requirements.txt` saves dependencies
✅ Poetry = modern dependency management
✅ Always use .gitignore to exclude venv/

---

<a name="hour-15"></a>
## 📅 Hour 15: ORMs - SQLAlchemy

### 🎯 Learning Objectives
- Understand Object-Relational Mapping (ORM)
- Use SQLAlchemy Core and ORM
- Define models and relationships
- Perform CRUD operations with ORM

### 📖 What to Teach

**"ORM = Write Python code instead of SQL queries!"**

---

### 1️⃣ What is ORM? (10 minutes)

**Without ORM (Raw SQL):**

```python
import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Create user
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@email.com"))
conn.commit()

# Get user
cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@email.com",))
user = cursor.fetchone()
```

**With ORM (SQLAlchemy):**

```python
from sqlalchemy.orm import Session

# Create user
user = User(name="Alice", email="alice@email.com")
session.add(user)
session.commit()

# Get user
user = session.query(User).filter_by(email="alice@email.com").first()
```

---

### 2️⃣ SQLAlchemy Setup (15 minutes)

**Install:**

```bash
pip install sqlalchemy
```

**Basic Setup:**

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create engine
engine = create_engine('sqlite:///blog.db', echo=True)

# Base class for models
Base = declarative_base()

# Define model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
```

---

### 3️⃣ CRUD Operations with ORM (20 minutes)

**Create:**

```python
# Single user
user = User(username="alice", email="alice@email.com")
session.add(user)
session.commit()

# Multiple users
users = [
    User(username="bob", email="bob@email.com"),
    User(username="charlie", email="charlie@email.com")
]
session.add_all(users)
session.commit()
```

**Read (Query):**

```python
# Get all users
users = session.query(User).all()

# Get first user
user = session.query(User).first()

# Filter by column
user = session.query(User).filter_by(username="alice").first()

# Filter with conditions
users = session.query(User).filter(User.id > 5).all()

# Order by
users = session.query(User).order_by(User.created_at.desc()).all()

# Limit
users = session.query(User).limit(10).all()

# Count
count = session.query(User).count()

# Get by primary key
user = session.query(User).get(1)
```

**Update:**

```python
# Method 1: Get and modify
user = session.query(User).filter_by(username="alice").first()
user.email = "newemail@email.com"
session.commit()

# Method 2: Update query
session.query(User).filter_by(username="alice").update({"email": "newemail@email.com"})
session.commit()
```

**Delete:**

```python
# Method 1: Get and delete
user = session.query(User).filter_by(username="alice").first()
session.delete(user)
session.commit()

# Method 2: Delete query
session.query(User).filter_by(username="alice").delete()
session.commit()
```

---

### 4️⃣ Relationships (15 minutes)

**One-to-Many Relationship:**

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    
    # Relationship
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    # Relationship
    author = relationship("User", back_populates="posts")

# Usage
user = User(username="alice")
post1 = Post(title="First Post", content="Hello World")
post2 = Post(title="Second Post", content="Another post")

user.posts.append(post1)
user.posts.append(post2)

session.add(user)
session.commit()

# Query
user = session.query(User).filter_by(username="alice").first()
for post in user.posts:
    print(post.title)
```

**Many-to-Many Relationship:**

```python
from sqlalchemy import Table

# Association table
post_tags = Table('post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    
    # Many-to-many relationship
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    
    # Many-to-many relationship
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

# Usage
post = Post(title="Python Tutorial")
tag1 = Tag(name="Python")
tag2 = Tag(name="Tutorial")

post.tags.extend([tag1, tag2])

session.add(post)
session.commit()
```

---

### 💻 Live Activity: Complete Blog ORM

**Create: hour15_blog_orm.py**

```python
"""
Complete Blog System with SQLAlchemy ORM
"""

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Setup
engine = create_engine('sqlite:///blog_orm.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Association table for many-to-many
post_tags = Table('post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

# Models
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    bio = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")
    
    def __repr__(self):
        return f"<Post(title='{self.title}')>"

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    
    def __repr__(self):
        return f"<Comment(id={self.id})>"

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
    
    def __repr__(self):
        return f"<Tag(name='{self.name}')>"

# Create tables
Base.metadata.create_all(engine)

# Helper functions
def create_user(username, email, bio=""):
    user = User(username=username, email=email, bio=bio)
    session.add(user)
    session.commit()
    return user

def create_post(author_id, title, content, tag_names=None):
    post = Post(author_id=author_id, title=title, content=content)
    
    if tag_names:
        for tag_name in tag_names:
            tag = session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            post.tags.append(tag)
    
    session.add(post)
    session.commit()
    return post

def add_comment(user_id, post_id, content):
    comment = Comment(user_id=user_id, post_id=post_id, content=content)
    session.add(comment)
    session.commit()
    return comment

def get_user_posts(username):
    user = session.query(User).filter_by(username=username).first()
    return user.posts if user else []

def get_posts_by_tag(tag_name):
    tag = session.query(Tag).filter_by(name=tag_name).first()
    return tag.posts if tag else []

def get_post_with_comments(post_id):
    post = session.query(Post).get(post_id)
    return post

def like_post(post_id):
    post = session.query(Post).get(post_id)
    if post:
        post.likes += 1
        session.commit()

def view_post(post_id):
    post = session.query(Post).get(post_id)
    if post:
        post.views += 1
        session.commit()

# Demo
print("=== BLOG ORM DEMO ===\n")

# Create users
print("1. Creating users...")
alice = create_user("alice", "alice@email.com", "Python developer")
bob = create_user("bob", "bob@email.com", "Data scientist")
print(f"   Created: {alice}, {bob}\n")

# Create posts
print("2. Creating posts...")
post1 = create_post(alice.id, "Python Basics", "Learn Python fundamentals", ["Python", "Tutorial"])
post2 = create_post(alice.id, "Advanced Python", "Deep dive into Python", ["Python", "Advanced"])
post3 = create_post(bob.id, "Data Science 101", "Introduction to data science", ["Data Science", "Tutorial"])
print(f"   Created 3 posts\n")

# Add comments
print("3. Adding comments...")
add_comment(bob.id, post1.id, "Great tutorial!")
add_comment(alice.id, post3.id, "Very informative!")
print("   Added comments\n")

# Like and view posts
print("4. Liking and viewing posts...")
like_post(post1.id)
like_post(post1.id)
view_post(post1.id)
view_post(post1.id)
view_post(post1.id)
print("   Post 1: 2 likes, 3 views\n")

# Query examples
print("5. Querying data...")

print("   Alice's posts:")
for post in get_user_posts("alice"):
    print(f"     - {post.title} ({post.likes} likes, {post.views} views)")

print("\n   Posts with 'Python' tag:")
for post in get_posts_by_tag("Python"):
    print(f"     - {post.title} by {post.author.username}")

print("\n   Post 1 with comments:")
post = get_post_with_comments(post1.id)
print(f"     Title: {post.title}")
print(f"     Comments:")
for comment in post.comments:
    print(f"       - {comment.user.username}: {comment.content}")

# Statistics
print("\n6. Statistics:")
total_users = session.query(User).count()
total_posts = session.query(Post).count()
total_comments = session.query(Comment).count()
print(f"   Users: {total_users}")
print(f"   Posts: {total_posts}")
print(f"   Comments: {total_comments}")
```

---

### 🏠 Homework: E-commerce Database

```python
# homework15_ecommerce_orm.py

# TODO: Create an e-commerce database with SQLAlchemy:

# 1. Models:
# - User (id, username, email, address, phone)
# - Product (id, name, description, price, stock, category_id)
# - Category (id, name, description)
# - Order (id, user_id, total, status, created_at)
# - OrderItem (id, order_id, product_id, quantity, price)

# 2. Relationships:
# - User has many Orders
# - Order has many OrderItems
# - Product belongs to Category
# - Product has many OrderItems

# 3. Functions:
# - create_user()
# - add_product()
# - create_order()
# - add_to_cart()
# - get_user_orders()
# - get_order_total()

# Test with sample data!
```

---

### 📝 Key Takeaways

✅ ORM = Object-Relational Mapping
✅ SQLAlchemy = Popular Python ORM
✅ Models = Python classes representing tables
✅ `session.query()` for retrieving data
✅ `relationship()` defines relationships
✅ Cascade operations automatically handle related data

---

<a name="hour-16"></a>
## 📅 Hour 16: NoSQL with MongoDB

### 🎯 Learning Objectives
- Understand NoSQL vs SQL
- Use MongoDB with Python
- Perform CRUD operations
- Work with embedded documents

### 📖 What to Teach

**"NoSQL = Flexible document storage, like JSON files in a database!"**

---

### 1️⃣ SQL vs NoSQL (10 minutes)

**SQL (Relational):**

```
users table:
id | username | email
1  | alice    | alice@email.com

posts table:
id | title    | user_id
1  | Hello    | 1
```

**NoSQL (Document):**

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "username": "alice",
  "email": "alice@email.com",
  "posts": [
    {
      "title": "Hello",
      "content": "First post",
      "created_at": "2025-12-15"
    }
  ]
}
```

**When to use NoSQL:**
- Flexible schema
- Rapid development
- Hierarchical data
- Horizontal scaling

---

### 2️⃣ MongoDB with Python (20 minutes)

**Install PyMongo:**

```bash
pip install pymongo
```

**Connect to MongoDB:**

```python
from pymongo import MongoClient
from datetime import datetime

# Connect
client = MongoClient('mongodb://localhost:27017/')

# Database
db = client['blog_db']

# Collection (like table in SQL)
users = db['users']
posts = db['posts']
```

**Insert Documents:**

```python
# Insert one
user = {
    "username": "alice",
    "email": "alice@email.com",
    "created_at": datetime.utcnow()
}
result = users.insert_one(user)
print(f"Inserted ID: {result.inserted_id}")

# Insert many
new_users = [
    {"username": "bob", "email": "bob@email.com"},
    {"username": "charlie", "email": "charlie@email.com"}
]
result = users.insert_many(new_users)
print(f"Inserted IDs: {result.inserted_ids}")
```

**Find Documents:**

```python
# Find one
user = users.find_one({"username": "alice"})
print(user)

# Find all
all_users = users.find()
for user in all_users:
    print(user)

# Find with filter
active_users = users.find({"status": "active"})

# Find with projection (select specific fields)
users_names = users.find({}, {"username": 1, "email": 1, "_id": 0})

# Count
count = users.count_documents({})
print(f"Total users: {count}")
```

**Update Documents:**

```python
# Update one
users.update_one(
    {"username": "alice"},
    {"$set": {"email": "newemail@email.com"}}
)

# Update many
users.update_many(
    {"status": "inactive"},
    {"$set": {"status": "active"}}
)

# Increment value
posts.update_one(
    {"_id": post_id},
    {"$inc": {"likes": 1}}
)

# Add to array
users.update_one(
    {"username": "alice"},
    {"$push": {"hobbies": "reading"}}
)
```

**Delete Documents:**

```python
# Delete one
users.delete_one({"username": "alice"})

# Delete many
users.delete_many({"status": "deleted"})
```

---

### 3️⃣ Embedded Documents (15 minutes)

**Embedding Posts in User:**

```python
# Insert user with embedded posts
user_with_posts = {
    "username": "alice",
    "email": "alice@email.com",
    "posts": [
        {
            "title": "First Post",
            "content": "Hello World",
            "likes": 10,
            "created_at": datetime.utcnow()
        },
        {
            "title": "Second Post",
            "content": "Another post",
            "likes": 5,
            "created_at": datetime.utcnow()
        }
    ]
}

users.insert_one(user_with_posts)

# Query embedded documents
user = users.find_one({"posts.title": "First Post"})

# Update embedded document
users.update_one(
    {"username": "alice", "posts.title": "First Post"},
    {"$inc": {"posts.$.likes": 1}}
)
```

---

### 4️⃣ Indexing and Aggregation (15 minutes)

**Create Indexes:**

```python
# Single field index
users.create_index("username")

# Unique index
users.create_index("email", unique=True)

# Compound index
posts.create_index([("author", 1), ("created_at", -1)])

# Text index for search
posts.create_index([("title", "text"), ("content", "text")])

# Text search
results = posts.find({"$text": {"$search": "python tutorial"}})
```

**Aggregation:**

```python
# Group by and count
pipeline = [
    {"$group": {"_id": "$author", "post_count": {"$sum": 1}}}
]
result = posts.aggregate(pipeline)

# Match, group, sort
pipeline = [
    {"$match": {"likes": {"$gt": 10}}},
    {"$group": {"_id": "$author", "total_likes": {"$sum": "$likes"}}},
    {"$sort": {"total_likes": -1}}
]
result = posts.aggregate(pipeline)
```

---

### 💻 Live Activity: MongoDB Blog

**Create: hour16_mongodb_blog.py**

```python
"""
MongoDB Blog System
"""

from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

class MongoBlog:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['blog_db']
        self.users = self.db['users']
        self.posts = self.db['posts']
        self.comments = self.db['comments']
        
        # Create indexes
        self.users.create_index("username", unique=True)
        self.users.create_index("email", unique=True)
        self.posts.create_index([("title", "text"), ("content", "text")])
    
    def create_user(self, username, email, bio=""):
        user = {
            "username": username,
            "email": email,
            "bio": bio,
            "created_at": datetime.utcnow()
        }
        result = self.users.insert_one(user)
        return result.inserted_id
    
    def create_post(self, author_id, title, content, tags=None):
        post = {
            "author_id": ObjectId(author_id),
            "title": title,
            "content": content,
            "tags": tags or [],
            "likes": 0,
            "views": 0,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = self.posts.insert_one(post)
        return result.inserted_id
    
    def add_comment(self, post_id, user_id, content):
        comment = {
            "post_id": ObjectId(post_id),
            "user_id": ObjectId(user_id),
            "content": content,
            "created_at": datetime.utcnow()
        }
        result = self.comments.insert_one(comment)
        return result.inserted_id
    
    def like_post(self, post_id):
        self.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"likes": 1}}
        )
    
    def view_post(self, post_id):
        self.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"views": 1}}
        )
    
    def get_user_posts(self, username):
        user = self.users.find_one({"username": username})
        if not user:
            return []
        
        posts = self.posts.find({"author_id": user["_id"]})
        return list(posts)
    
    def get_post_with_author(self, post_id):
        post = self.posts.find_one({"_id": ObjectId(post_id)})
        if not post:
            return None
        
        author = self.users.find_one({"_id": post["author_id"]})
        post["author"] = author
        return post
    
    def search_posts(self, keyword):
        posts = self.posts.find(
            {"$text": {"$search": keyword}},
            {"score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})])
        
        return list(posts)
    
    def get_popular_posts(self, limit=10):
        posts = self.posts.find().sort("likes", -1).limit(limit)
        return list(posts)
    
    def get_statistics(self):
        return {
            "total_users": self.users.count_documents({}),
            "total_posts": self.posts.count_documents({}),
            "total_comments": self.comments.count_documents({})
        }

# Demo
print("=== MONGODB BLOG DEMO ===\n")

blog = MongoBlog()

# Create users
print("1. Creating users...")
alice_id = blog.create_user("alice", "alice@email.com", "Python developer")
bob_id = blog.create_user("bob", "bob@email.com", "Data scientist")
print(f"   Created users\n")

# Create posts
print("2. Creating posts...")
post1_id = blog.create_post(alice_id, "Python Basics", "Learn Python", ["Python", "Tutorial"])
post2_id = blog.create_post(alice_id, "Advanced Python", "Deep dive", ["Python", "Advanced"])
post3_id = blog.create_post(bob_id, "Data Science", "Introduction", ["Data Science"])
print(f"   Created posts\n")

# Add comments
print("3. Adding comments...")
blog.add_comment(post1_id, bob_id, "Great tutorial!")
print("   Added comment\n")

# Like and view
print("4. Liking and viewing...")
blog.like_post(post1_id)
blog.like_post(post1_id)
blog.view_post(post1_id)
print("   Post liked and viewed\n")

# Query
print("5. Queries:")
print("   Alice's posts:")
for post in blog.get_user_posts("alice"):
    print(f"     - {post['title']}")

print("\n   Search 'Python':")
for post in blog.search_posts("Python"):
    print(f"     - {post['title']}")

# Statistics
print("\n6. Statistics:")
stats = blog.get_statistics()
for key, value in stats.items():
    print(f"   {key}: {value}")
```

---

### 🏠 Homework: MongoDB E-commerce

```python
# homework16_mongodb_ecommerce.py

# TODO: Build e-commerce system with MongoDB:

# Collections:
# - users (username, email, address, orders)
# - products (name, description, price, stock, reviews)
# - orders (user_id, items, total, status, created_at)

# Embedded documents:
# - User has embedded orders array
# - Product has embedded reviews array

# Functions:
# - create_user()
# - add_product()
# - add_review(product_id, user_id, rating, comment)
# - create_order(user_id, items)
# - get_product_avg_rating()
# - get_top_rated_products()

# Use aggregation to calculate statistics!
```

---

### 📝 Key Takeaways

✅ NoSQL = flexible document storage
✅ MongoDB stores JSON-like documents
✅ PyMongo = Python MongoDB driver
✅ Embedded documents = nested data
✅ Aggregation = complex queries
✅ Indexes = improve query performance

---

<a name="hour-17"></a>
## 📅 Hour 17: RESTful API Concepts

### 🎯 Learning Objectives
- Understand REST principles
- Learn HTTP methods (GET, POST, PUT, DELETE)
- Master status codes
- Design RESTful endpoints
- Understand JSON responses

### 📖 What to Teach

**"REST API = Way for applications to talk to each other over internet!"**

---

### 1️⃣ What is REST API? (10 minutes)

**Real-Life Analogy:**

"API = Menu at a restaurant
- You (client) look at menu (API documentation)
- You order food (make API request)
- Kitchen (server) prepares food
- Waiter brings food (API response)"

**REST Principles:**

```
1. Client-Server: Separate frontend and backend
2. Stateless: Each request has all needed info
3. Cacheable: Responses can be cached
4. Uniform Interface: Standard methods (GET, POST, etc.)
5. Layered System: Can have intermediate servers
```

---

### 2️⃣ HTTP Methods (15 minutes)

**CRUD Operations:**

```
CREATE  → POST    → Add new resource
READ    → GET     → Get resource(s)
UPDATE  → PUT     → Update entire resource
UPDATE  → PATCH   → Update part of resource
DELETE  → DELETE  → Remove resource
```

**Examples:**

```python
# GET - Retrieve data
GET /api/users           # Get all users
GET /api/users/1         # Get user with ID 1
GET /api/users/1/posts   # Get posts by user 1

# POST - Create new data
POST /api/users          # Create new user
{
    "username": "alice",
    "email": "alice@email.com"
}

# PUT - Replace entire resource
PUT /api/users/1         # Update user 1 completely
{
    "username": "alice_updated",
    "email": "newemail@email.com",
    "bio": "Updated bio"
}

# PATCH - Update specific fields
PATCH /api/users/1       # Update specific fields
{
    "email": "newemail@email.com"
}

# DELETE - Remove resource
DELETE /api/users/1      # Delete user 1
```

---

### 3️⃣ HTTP Status Codes (15 minutes)

**Status Code Categories:**

```
1xx: Informational
2xx: Success ✅
3xx: Redirection
4xx: Client Error ❌
5xx: Server Error 💥
```

**Common Status Codes:**

```python
# Success (2xx)
200 OK                  # Successful GET, PUT, PATCH
201 Created             # Successful POST
204 No Content          # Successful DELETE

# Client Errors (4xx)
400 Bad Request         # Invalid data sent
401 Unauthorized        # Not authenticated
403 Forbidden           # Not authorized
404 Not Found           # Resource doesn't exist
409 Conflict            # Duplicate/conflict

# Server Errors (5xx)
500 Internal Server Error   # Server crashed
502 Bad Gateway            # Upstream server error
503 Service Unavailable    # Server down
```

---

### 4️⃣ REST API Design (15 minutes)

**Good API Design:**

```
✅ GOOD:
GET    /api/users              # Get all users
GET    /api/users/123          # Get user 123
POST   /api/users              # Create user
PUT    /api/users/123          # Update user 123
DELETE /api/users/123          # Delete user 123

GET    /api/users/123/posts    # Get user's posts
POST   /api/users/123/posts    # Create post for user

❌ BAD:
GET    /api/getAllUsers
GET    /api/user?id=123
POST   /api/createUser
GET    /api/deleteUser/123     # Should use DELETE!
```

**API Versioning:**

```
Option 1: URL Path
/api/v1/users
/api/v2/users

Option 2: Header
GET /api/users
Accept: application/vnd.myapi.v1+json

Option 3: Query Parameter
/api/users?version=1
```

**Query Parameters:**

```python
# Filtering
GET /api/posts?author=alice&status=published

# Sorting
GET /api/posts?sort=created_at&order=desc

# Pagination
GET /api/posts?page=2&limit=10

# Search
GET /api/posts?search=python

# Fields selection
GET /api/users?fields=username,email
```

---

### 5️⃣ JSON Response Format (5 minutes)

**Standard Response:**

```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "alice",
    "email": "alice@email.com"
  },
  "message": "User retrieved successfully"
}
```

**List Response with Pagination:**

```json
{
  "success": true,
  "data": [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"}
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 50,
    "pages": 5
  }
}
```

**Error Response:**

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": {
      "email": "Must be a valid email address"
    }
  }
}
```

---

### 💻 Live Activity: API Documentation

**Create: hour17_api_design.md**

```markdown
# Blog API Documentation

## Base URL
```
https://api.myblog.com/v1
```

## Authentication
All endpoints require authentication header:
```
Authorization: Bearer YOUR_TOKEN_HERE
```

---

## Endpoints

### Users

#### Get All Users
```
GET /users
```

**Query Parameters:**
- `page` (integer): Page number (default: 1)
- `limit` (integer): Items per page (default: 10)
- `sort` (string): Sort field (default: created_at)

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "username": "alice",
      "email": "alice@email.com",
      "created_at": "2025-12-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 50
  }
}
```

---

#### Get User by ID
```
GET /users/:id
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "alice",
    "email": "alice@email.com",
    "bio": "Python developer",
    "created_at": "2025-12-15T10:30:00Z"
  }
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 1 not found"
  }
}
```

---

#### Create User
```
POST /users
```

**Request Body:**
```json
{
  "username": "alice",
  "email": "alice@email.com",
  "password": "SecurePass123"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "alice",
    "email": "alice@email.com",
    "created_at": "2025-12-15T10:30:00Z"
  },
  "message": "User created successfully"
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": {
      "email": "Email already exists",
      "password": "Password must be at least 8 characters"
    }
  }
}
```

---

#### Update User
```
PUT /users/:id
```

**Request Body:**
```json
{
  "username": "alice_updated",
  "email": "newemail@email.com",
  "bio": "Senior Python Developer"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "alice_updated",
    "email": "newemail@email.com",
    "bio": "Senior Python Developer",
    "updated_at": "2025-12-15T11:00:00Z"
  },
  "message": "User updated successfully"
}
```

---

#### Delete User
```
DELETE /users/:id
```

**Response (204 No Content)**

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 1 not found"
  }
}
```

---

### Posts

#### Get All Posts
```
GET /posts
```

**Query Parameters:**
- `author` (integer): Filter by author ID
- `tag` (string): Filter by tag
- `search` (string): Search in title/content

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Python Basics",
      "content": "Learn Python...",
      "author": {
        "id": 1,
        "username": "alice"
      },
      "tags": ["Python", "Tutorial"],
      "likes": 42,
      "created_at": "2025-12-15T10:30:00Z"
    }
  ]
}
```

---

#### Create Post
```
POST /posts
```

**Request Body:**
```json
{
  "title": "Python Basics",
  "content": "Learn Python fundamentals...",
  "tags": ["Python", "Tutorial"]
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "Python Basics",
    "content": "Learn Python fundamentals...",
    "author_id": 1,
    "tags": ["Python", "Tutorial"],
    "created_at": "2025-12-15T10:30:00Z"
  },
  "message": "Post created successfully"
}
```

---

#### Like Post
```
POST /posts/:id/like
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "likes": 43
  },
  "message": "Post liked successfully"
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Invalid input data |
| `AUTHENTICATION_ERROR` | Invalid or missing token |
| `AUTHORIZATION_ERROR` | Insufficient permissions |
| `NOT_FOUND` | Resource not found |
| `DUPLICATE_ERROR` | Resource already exists |
| `SERVER_ERROR` | Internal server error |

---

## Rate Limiting

- **Rate Limit:** 100 requests per minute
- **Headers:**
  - `X-RateLimit-Limit`: Total allowed
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Reset timestamp

**Response (429 Too Many Requests):**
```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Try again in 60 seconds"
  }
}
```
```

---

### 🏠 Homework: Design Your API

```markdown
# homework17_api_design.md

# TODO: Design a complete REST API for an e-commerce system

## Requirements:

### Resources:
1. Users (authentication, profile)
2. Products (CRUD operations)
3. Categories (product categories)
4. Cart (shopping cart)
5. Orders (purchase orders)
6. Reviews (product reviews)

### Design:
- List all endpoints
- Specify HTTP methods
- Define request/response formats
- Include error responses
- Add pagination for lists
- Include filtering/sorting
- Define status codes

### Example Format:
```
GET /api/products
POST /api/products
GET /api/products/:id
PUT /api/products/:id
DELETE /api/products/:id
POST /api/products/:id/reviews
```

Write complete API documentation!
```

---

### 📝 Key Takeaways

✅ REST = Representational State Transfer
✅ HTTP Methods: GET, POST, PUT, PATCH, DELETE
✅ Status Codes: 2xx success, 4xx client error, 5xx server error
✅ URL structure: `/api/resource/:id`
✅ JSON = standard response format
✅ Good API design = predictable and consistent

---

<a name="hour-18"></a>
## 📅 Hour 18: Flask Part 1 - Basics

### 🎯 Learning Objectives
- Set up Flask application
- Create routes and endpoints
- Handle request/response
- Use templates (Jinja2)
- Build a simple blog API

### 📖 What to Teach

**"Flask = Lightweight web framework for Python!"**

---

### 1️⃣ Flask Setup (10 minutes)

**Install Flask:**

```bash
pip install flask
```

**Basic Flask App:**

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

**Run:**

```bash
python app.py
# Visit: http://localhost:5000
```

---

### 2️⃣ Routes and Methods (15 minutes)

**Different HTTP Methods:**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return jsonify(users)

# POST request
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # Process data
    return jsonify({"message": "User created", "data": data}), 201

# GET with URL parameter
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = {"id": user_id, "name": "Alice"}
    return jsonify(user)

# PUT request
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    return jsonify({"message": f"User {user_id} updated", "data": data})

# DELETE request
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 3️⃣ Request Handling (15 minutes)

**Query Parameters:**

```python
# GET /search?q=python&page=1
@app.route('/search')
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    
    return jsonify({
        "query": query,
        "page": page,
        "results": []
    })
```

**JSON Request Body:**

```python
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Validate
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    
    # Check credentials (simplified)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401
```

**Form Data:**

```python
@app.route('/upload', methods=['POST'])
def upload():
    # Form data
    title = request.form.get('title')
    
    # File upload
    file = request.files.get('file')
    if file:
        file.save(f'uploads/{file.filename}')
        return jsonify({"message": "File uploaded"})
    
    return jsonify({"error": "No file provided"}), 400
```

---

### 4️⃣ Response Types (10 minutes)

**JSON Response:**

```python
from flask import jsonify

@app.route('/api/data')
def get_data():
    data = {"name": "Alice", "age": 25}
    return jsonify(data)
```

**Custom Status Code:**

```python
@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify({"message": "Created"}), 201
```

**HTML Response:**

```python
@app.route('/page')
def page():
    html = """
    <html>
        <body>
            <h1>Hello from Flask!</h1>
        </body>
    </html>
    """
    return html
```

**Redirect:**

```python
from flask import redirect, url_for

@app.route('/old-page')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return "This is the new page!"
```

---

### 5️⃣ Templates with Jinja2 (10 minutes)

**Project Structure:**

```
flask_app/
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/
    └── js/
```

**base.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 My App</p>
    </footer>
</body>
</html>
```

**index.html:**

```html
{% extends "base.html" %}

{% block title %}Home - My App{% endblock %}

{% block content %}
<h1>Welcome, {{ username }}!</h1>

<ul>
    {% for item in items %}
    <li>{{ item }}</li>
    {% endfor %}
</ul>

{% if show_message %}
<p>This is a message!</p>
{% endif %}
{% endblock %}
```

**Using Templates:**

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', 
                         username='Alice',
                         items=['Python', 'Flask', 'Jinja2'],
                         show_message=True)
```

---

### 💻 Live Activity: Blog API

**Create: hour18_blog_api.py**

```python
"""
Simple Blog API with Flask
"""

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory data storage
users = {}
posts = {}
comments = {}

user_id_counter = 1
post_id_counter = 1
comment_id_counter = 1

# Helper function
def find_user_by_username(username):
    for user in users.values():
        if user['username'] == username:
            return user
    return None

# Users endpoints
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({
        "success": True,
        "data": list(users.values())
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    return jsonify({
        "success": True,
        "data": user
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    global user_id_counter
    
    data = request.json
    username = data.get('username')
    email = data.get('email')
    
    # Validation
    if not username or not email:
        return jsonify({
            "success": False,
            "error": "Username and email required"
        }), 400
    
    # Check duplicate
    if find_user_by_username(username):
        return jsonify({
            "success": False,
            "error": "Username already exists"
        }), 409
    
    # Create user
    user = {
        "id": user_id_counter,
        "username": username,
        "email": email,
        "bio": data.get('bio', ''),
        "created_at": datetime.utcnow().isoformat()
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": user,
        "message": "User created successfully"
    }), 201

# Posts endpoints
@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Query parameters
    author_id = request.args.get('author_id', type=int)
    
    filtered_posts = list(posts.values())
    
    if author_id:
        filtered_posts = [p for p in filtered_posts if p['author_id'] == author_id]
    
    return jsonify({
        "success": True,
        "data": filtered_posts
    })

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = posts.get(post_id)
    if not post:
        return jsonify({
            "success": False,
            "error": "Post not found"
        }), 404
    
    # Add author info
    author = users.get(post['author_id'])
    post['author'] = author
    
    # Add comments
    post_comments = [c for c in comments.values() if c['post_id'] == post_id]
    post['comments'] = post_comments
    
    return jsonify({
        "success": True,
        "data": post
    })

@app.route('/api/posts', methods=['POST'])
def create_post():
    global post_id_counter
    
    data = request.json
    author_id = data.get('author_id')
    title = data.get('title')
    content = data.get('content')
    
    # Validation
    if not all([author_id, title, content]):
        return jsonify({
            "success": False,
            "error": "author_id, title, and content required"
        }), 400
    
    if author_id not in users:
        return jsonify({
            "success": False,
            "error": "Author not found"
        }), 404
    
    # Create post
    post = {
        "id": post_id_counter,
        "author_id": author_id,
        "title": title,
        "content": content,
        "tags": data.get('tags', []),
        "likes": 0,
        "views": 0,
        "created_at": datetime.utcnow().isoformat()
    }
    
    posts[post_id_counter] = post
    post_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": post,
        "message": "Post created successfully"
    }), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = posts.get(post_id)
    if not post:
        return jsonify({
            "success": False,
            "error": "Post not found"
        }), 404
    
    data = request.json
    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])
    post['tags'] = data.get('tags', post['tags'])
    post['updated_at'] = datetime.utcnow().isoformat()
    
    return jsonify({
        "success": True,
        "data": post,
        "message": "Post updated successfully"
    })

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if post_id not in posts:
        return jsonify({
            "success": False,
            "error": "Post not found"
        }), 404
    
    del posts[post_id]
    
    return '', 204

@app.route('/api/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    post = posts.get(post_id)
    if not post:
        return jsonify({
            "success": False,
            "error": "Post not found"
        }), 404
    
    post['likes'] += 1
    
    return jsonify({
        "success": True,
        "data": {"id": post_id, "likes": post['likes']},
        "message": "Post liked successfully"
    })

# Comments endpoints
@app.route('/api/comments', methods=['POST'])
def create_comment():
    global comment_id_counter
    
    data = request.json
    post_id = data.get('post_id')
    user_id = data.get('user_id')
    content = data.get('content')
    
    # Validation
    if not all([post_id, user_id, content]):
        return jsonify({
            "success": False,
            "error": "post_id, user_id, and content required"
        }), 400
    
    if post_id not in posts:
        return jsonify({
            "success": False,
            "error": "Post not found"
        }), 404
    
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    # Create comment
    comment = {
        "id": comment_id_counter,
        "post_id": post_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.utcnow().isoformat()
    }
    
    comments[comment_id_counter] = comment
    comment_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": comment,
        "message": "Comment created successfully"
    }), 201

# Statistics endpoint
@app.route('/api/stats', methods=['GET'])
def get_stats():
    return jsonify({
        "success": True,
        "data": {
            "total_users": len(users),
            "total_posts": len(posts),
            "total_comments": len(comments)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

**Test with curl or Postman:**

```bash
# Create user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@email.com"}'

# Create post
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"author_id":1,"title":"Hello","content":"First post"}'

# Get all posts
curl http://localhost:5000/api/posts
```

---

### 🏠 Homework: Flask TODO API

```python
# homework18_todo_api.py

# TODO: Create a TODO list API with Flask

# Endpoints:
# GET    /api/todos           - Get all todos
# POST   /api/todos           - Create todo
# GET    /api/todos/:id       - Get todo
# PUT    /api/todos/:id       - Update todo
# DELETE /api/todos/:id       - Delete todo
# PATCH  /api/todos/:id/complete - Mark as complete

# Todo structure:
# {
#   "id": 1,
#   "title": "Buy groceries",
#   "description": "Milk, bread, eggs",
#   "completed": false,
#   "priority": "high",  # low/medium/high
#   "due_date": "2025-12-20",
#   "created_at": "2025-12-15T10:30:00Z"
# }

# Add query parameters for filtering:
# - ?completed=true
# - ?priority=high
# - ?sort=due_date

# Test all endpoints!
```

---

### 📝 Key Takeaways

✅ Flask = lightweight Python web framework
✅ `@app.route()` defines endpoints
✅ `request.json` gets JSON data
✅ `jsonify()` returns JSON response
✅ Status codes indicate success/failure
✅ Templates with Jinja2 for HTML

---

<a name="hour-19"></a>
## 📅 Hour 19: Flask Part 2 - Advanced Features

### 🎯 Learning Objectives
- Use Flask Blueprints
- Handle file uploads
- Implement error handling
- Add request validation
- Use Flask extensions

### 📖 What to Teach

**"Advanced Flask = building production-ready applications!"**

---

### 1️⃣ Flask Blueprints (15 minutes)

**Why Blueprints?**

"Blueprints = Organize large apps into smaller modules"

**Project Structure:**

```
flask_app/
├── app.py
├── config.py
├── api/
│   ├── __init__.py
│   ├── users.py
│   ├── posts.py
│   └── auth.py
└── models/
    ├── __init__.py
    ├── user.py
    └── post.py
```

**api/users.py:**

```python
from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

# In-memory storage
users = {}
user_id_counter = 1

@users_bp.route('', methods=['GET'])
def get_users():
    return jsonify({"success": True, "data": list(users.values())})

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404
    return jsonify({"success": True, "data": user})

@users_bp.route('', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.json
    
    user = {
        "id": user_id_counter,
        "username": data['username'],
        "email": data['email']
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    
    return jsonify({"success": True, "data": user}), 201
```

**api/posts.py:**

```python
from flask import Blueprint, request, jsonify

posts_bp = Blueprint('posts', __name__, url_prefix='/api/posts')

posts = {}
post_id_counter = 1

@posts_bp.route('', methods=['GET'])
def get_posts():
    return jsonify({"success": True, "data": list(posts.values())})

@posts_bp.route('', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.json
    
    post = {
        "id": post_id_counter,
        "title": data['title'],
        "content": data['content'],
        "author_id": data['author_id']
    }
    
    posts[post_id_counter] = post
    post_id_counter += 1
    
    return jsonify({"success": True, "data": post}), 201
```

**app.py:**

```python
from flask import Flask
from api.users import users_bp
from api.posts import posts_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

@app.route('/')
def home():
    return {"message": "Welcome to Blog API"}

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 2️⃣ Error Handling (15 minutes)

**Global Error Handlers:**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "NOT_FOUND",
            "message": "Resource not found"
        }
    }), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "BAD_REQUEST",
            "message": "Invalid request data"
        }
    }), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "INTERNAL_ERROR",
            "message": "Something went wrong"
        }
    }), 500

@app.errorhandler(Exception)
def handle_exception(error):
    # Log the error
    app.logger.error(f"Unhandled exception: {error}")
    
    return jsonify({
        "success": False,
        "error": {
            "code": "SERVER_ERROR",
            "message": "An unexpected error occurred"
        }
    }), 500
```

**Custom Exceptions:**

```python
class ValidationError(Exception):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details or {}

class NotFoundError(Exception):
    def __init__(self, resource, resource_id):
        self.message = f"{resource} with ID {resource_id} not found"

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "VALIDATION_ERROR",
            "message": error.message,
            "details": error.details
        }
    }), 400

@app.errorhandler(NotFoundError)
def handle_not_found_error(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "NOT_FOUND",
            "message": error.message
        }
    }), 404

# Usage in routes
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFoundError("User", user_id)
    return jsonify({"success": True, "data": user})
```

---

### 3️⃣ Request Validation (15 minutes)

**Manual Validation:**

```python
from flask import request, jsonify

def validate_user_data(data):
    errors = {}
    
    # Username validation
    if 'username' not in data:
        errors['username'] = "Username is required"
    elif len(data['username']) < 3:
        errors['username'] = "Username must be at least 3 characters"
    
    # Email validation
    if 'email' not in data:
        errors['email'] = "Email is required"
    elif '@' not in data['email']:
        errors['email'] = "Invalid email format"
    
    # Password validation
    if 'password' in data:
        password = data['password']
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if not any(c.isupper() for c in password):
            errors['password'] = "Password must contain uppercase letter"
        if not any(c.isdigit() for c in password):
            errors['password'] = "Password must contain a number"
    
    return errors

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    
    # Validate
    errors = validate_user_data(data)
    if errors:
        return jsonify({
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Validation failed",
                "details": errors
            }
        }), 400
    
    # Create user...
    return jsonify({"success": True, "message": "User created"}), 201
```

**Using Flask-Pydantic (Better Way):**

```bash
pip install flask-pydantic
```

```python
from flask import Flask
from flask_pydantic import validate
from pydantic import BaseModel, EmailStr, validator

app = Flask(__name__)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    @validator('username')
    def username_min_length(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        return v
    
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain a number')
        return v

@app.route('/api/users', methods=['POST'])
@validate()
def create_user(body: UserCreate):
    # body is automatically validated!
    return {"success": True, "data": body.dict()}
```

---

### 4️⃣ File Upload (10 minutes)

```python
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Check if file is present
    if 'file' not in request.files:
        return jsonify({
            "success": False,
            "error": "No file provided"
        }), 400
    
    file = request.files['file']
    
    # Check if filename is empty
    if file.filename == '':
        return jsonify({
            "success": False,
            "error": "No file selected"
        }), 400
    
    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "error": "File type not allowed"
        }), 400
    
    # Save file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    return jsonify({
        "success": True,
        "data": {
            "filename": filename,
            "path": filepath
        },
        "message": "File uploaded successfully"
    }), 201

@app.route('/api/upload-multiple', methods=['POST'])
def upload_multiple():
    files = request.files.getlist('files')
    
    uploaded_files = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            uploaded_files.append(filename)
    
    return jsonify({
        "success": True,
        "data": {"files": uploaded_files},
        "message": f"{len(uploaded_files)} files uploaded"
    }), 201
```

---

### 5️⃣ CORS and Security (5 minutes)

**Enable CORS:**

```bash
pip install flask-cors
```

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Or specific routes
@app.route('/api/public')
@cross_origin()
def public_api():
    return {"message": "Public API"}
```

**Security Headers:**

```python
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
```

---

### 💻 Live Activity: Production-Ready Blog API

**Create: hour19_production_blog.py**

```python
"""
Production-Ready Blog API with Flask
Includes: Blueprints, Error Handling, Validation, File Upload
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
import os

# Initialize Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# In-memory storage
users = {}
posts = {}
user_id_counter = 1
post_id_counter = 1

# Pydantic models for validation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    bio: str = ""
    
    @validator('username')
    def username_validation(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v
    
    @validator('password')
    def password_validation(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int
    tags: list = []
    
    @validator('title')
    def title_validation(cls, v):
        if len(v) < 5:
            raise ValueError('Title must be at least 5 characters')
        return v
    
    @validator('content')
    def content_validation(cls, v):
        if len(v) < 10:
            raise ValueError('Content must be at least 10 characters')
        return v

# Custom exceptions
class ValidationError(Exception):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details or {}

class NotFoundError(Exception):
    def __init__(self, resource, resource_id):
        self.message = f"{resource} with ID {resource_id} not found"

class DuplicateError(Exception):
    def __init__(self, field, value):
        self.message = f"{field} '{value}' already exists"

# Error handlers
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "VALIDATION_ERROR",
            "message": error.message,
            "details": error.details
        }
    }), 400

@app.errorhandler(NotFoundError)
def handle_not_found(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "NOT_FOUND",
            "message": error.message
        }
    }), 404

@app.errorhandler(DuplicateError)
def handle_duplicate(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "DUPLICATE_ERROR",
            "message": error.message
        }
    }), 409

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": {
            "code": "NOT_FOUND",
            "message": "Endpoint not found"
        }
    }), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Internal error: {error}")
    return jsonify({
        "success": False,
        "error": {
            "code": "INTERNAL_ERROR",
            "message": "Something went wrong"
        }
    }), 500

# Helper functions
def find_user_by_username(username):
    for user in users.values():
        if user['username'] == username:
            return user
    return None

# Routes
@app.route('/')
def home():
    return jsonify({
        "message": "Blog API v1.0",
        "endpoints": {
            "users": "/api/users",
            "posts": "/api/posts",
            "upload": "/api/upload"
        }
    })

# User routes
@app.route('/api/users', methods=['POST'])
def create_user():
    global user_id_counter
    
    try:
        data = request.json
        user_data = UserCreate(**data)
    except Exception as e:
        raise ValidationError("Invalid user data", {"details": str(e)})
    
    # Check duplicate username
    if find_user_by_username(user_data.username):
        raise DuplicateError("Username", user_data.username)
    
    # Create user
    user = {
        "id": user_id_counter,
        "username": user_data.username,
        "email": user_data.email,
        "bio": user_data.bio,
        "avatar_url": None,
        "created_at": datetime.utcnow().isoformat()
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": user,
        "message": "User created successfully"
    }), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFoundError("User", user_id)
    return jsonify({"success": True, "data": user})

@app.route('/api/users/<int:user_id>/avatar', methods=['POST'])
def upload_avatar(user_id):
    user = users.get(user_id)
    if not user:
        raise NotFoundError("User", user_id)
    
    if 'avatar' not in request.files:
        raise ValidationError("No avatar file provided")
    
    file = request.files['avatar']
    
    if file.filename == '':
        raise ValidationError("No file selected")
    
    # Validate file type
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
        raise ValidationError("Invalid file type. Allowed: png, jpg, jpeg, gif")
    
    # Save file
    filename = f"avatar_{user_id}_{secure_filename(file.filename)}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Update user
    user['avatar_url'] = f"/uploads/{filename}"
    
    return jsonify({
        "success": True,
        "data": {"avatar_url": user['avatar_url']},
        "message": "Avatar uploaded successfully"
    })

# Post routes
@app.route('/api/posts', methods=['POST'])
def create_post():
    global post_id_counter
    
    try:
        data = request.json
        post_data = PostCreate(**data)
    except Exception as e:
        raise ValidationError("Invalid post data", {"details": str(e)})
    
    # Verify author exists
    if post_data.author_id not in users:
        raise NotFoundError("Author", post_data.author_id)
    
    # Create post
    post = {
        "id": post_id_counter,
        "title": post_data.title,
        "content": post_data.content,
        "author_id": post_data.author_id,
        "tags": post_data.tags,
        "likes": 0,
        "views": 0,
        "created_at": datetime.utcnow().isoformat()
    }
    
    posts[post_id_counter] = post
    post_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": post,
        "message": "Post created successfully"
    }), 201

@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Query parameters
    author_id = request.args.get('author_id', type=int)
    tag = request.args.get('tag')
    
    filtered_posts = list(posts.values())
    
    if author_id:
        filtered_posts = [p for p in filtered_posts if p['author_id'] == author_id]
    
    if tag:
        filtered_posts = [p for p in filtered_posts if tag in p['tags']]
    
    return jsonify({"success": True, "data": filtered_posts})

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = posts.get(post_id)
    if not post:
        raise NotFoundError("Post", post_id)
    
    # Increment views
    post['views'] += 1
    
    # Add author info
    author = users.get(post['author_id'])
    post['author'] = author
    
    return jsonify({"success": True, "data": post})

# Statistics
@app.route('/api/stats', methods=['GET'])
def get_stats():
    total_likes = sum(p['likes'] for p in posts.values())
    total_views = sum(p['views'] for p in posts.values())
    
    return jsonify({
        "success": True,
        "data": {
            "total_users": len(users),
            "total_posts": len(posts),
            "total_likes": total_likes,
            "total_views": total_views
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 🏠 Homework: Complete E-commerce API

```python
# homework19_ecommerce_api.py

# TODO: Build complete e-commerce API with:

# 1. Blueprints:
# - api/products.py
# - api/cart.py
# - api/orders.py
# - api/auth.py

# 2. Features:
# - Product CRUD with image upload
# - Shopping cart management
# - Order placement
# - User authentication
# - Error handling
# - Request validation (use Pydantic)
# - CORS enabled

# 3. Models:
# - Product (name, price, stock, images)
# - Cart (user_id, items)
# - Order (user_id, items, total, status)

# Test all endpoints with Postman!
```

---

### 📝 Key Takeaways

✅ Blueprints organize large apps
✅ Error handlers for consistent responses
✅ Pydantic for request validation
✅ File upload with security checks
✅ CORS for cross-origin requests
✅ Production-ready = validation + error handling + security

---

<a name="hour-20"></a>
## 📅 Hour 20: Authentication & Authorization

### 🎯 Learning Objectives
- Implement JWT authentication
- Hash passwords with bcrypt
- Create signup/login endpoints
- Protect routes with decorators
- Implement role-based access

### 📖 What to Teach

**"Authentication = Who are you? Authorization = What can you do?"**

---

### 1️⃣ Password Hashing (10 minutes)

**Install bcrypt:**

```bash
pip install bcrypt
```

**Hashing Passwords:**

```python
import bcrypt

def hash_password(password):
    """Hash a password"""
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed):
    """Verify a password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Usage
password = "MySecurePass123"
hashed = hash_password(password)
print(f"Hashed: {hashed}")

# Verify
is_valid = verify_password("MySecurePass123", hashed)
print(f"Valid: {is_valid}")  # True

is_valid = verify_password("WrongPassword", hashed)
print(f"Valid: {is_valid}")  # False
```

---

### 2️⃣ JWT Tokens (15 minutes)

**Install PyJWT:**

```bash
pip install pyjwt
```

**Creating and Verifying JWTs:**

```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-keep-this-safe"

def create_token(user_id, username):
    """Create JWT token"""
    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=24)  # Expires in 24 hours
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Usage
token = create_token(1, "alice")
print(f"Token: {token}")

# Verify
payload = verify_token(token)
print(f"Payload: {payload}")
```

---

### 3️⃣ Authentication Routes (15 minutes)

```python
from flask import Flask, request, jsonify
import bcrypt
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# In-memory storage
users = {}
user_id_counter = 1

# Helper functions
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_token(user_id, username, role='user'):
    payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")

# Signup route
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    global user_id_counter
    
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # Validation
    if not all([username, email, password]):
        return jsonify({
            "success": False,
            "error": "Username, email, and password required"
        }), 400
    
    # Check duplicate username
    for user in users.values():
        if user['username'] == username:
            return jsonify({
                "success": False,
                "error": "Username already exists"
            }), 409
    
    # Create user
    user = {
        "id": user_id_counter,
        "username": username,
        "email": email,
        "password_hash": hash_password(password),
        "role": "user",
        "created_at": datetime.utcnow().isoformat()
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    
    # Generate token
    token = create_token(user['id'], user['username'], user['role'])
    
    # Return user without password
    user_response = {k: v for k, v in user.items() if k != 'password_hash'}
    
    return jsonify({
        "success": True,
        "data": {
            "user": user_response,
            "token": token
        },
        "message": "Signup successful"
    }), 201

# Login route
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Validation
    if not username or not password:
        return jsonify({
            "success": False,
            "error": "Username and password required"
        }), 400
    
    # Find user
    user = None
    for u in users.values():
        if u['username'] == username:
            user = u
            break
    
    if not user:
        return jsonify({
            "success": False,
            "error": "Invalid credentials"
        }), 401
    
    # Verify password
    if not verify_password(password, user['password_hash']):
        return jsonify({
            "success": False,
            "error": "Invalid credentials"
        }), 401
    
    # Generate token
    token = create_token(user['id'], user['username'], user['role'])
    
    # Return user without password
    user_response = {k: v for k, v in user.items() if k != 'password_hash'}
    
    return jsonify({
        "success": True,
        "data": {
            "user": user_response,
            "token": token
        },
        "message": "Login successful"
    })
```

---

### 4️⃣ Protected Routes (15 minutes)

**Authentication Decorator:**

```python
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Get token from header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]  # "Bearer <token>"
            except IndexError:
                return jsonify({
                    "success": False,
                    "error": "Invalid token format"
                }), 401
        
        if not token:
            return jsonify({
                "success": False,
                "error": "Token is missing"
            }), 401
        
        try:
            # Verify token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(payload['user_id'])
            
            if not current_user:
                return jsonify({
                    "success": False,
                    "error": "User not found"
                }), 401
            
        except jwt.ExpiredSignatureError:
            return jsonify({
                "success": False,
                "error": "Token has expired"
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                "success": False,
                "error": "Invalid token"
            }), 401
        
        # Pass current_user to route
        return f(current_user, *args, **kwargs)
    
    return decorated

# Protected route
@app.route('/api/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    user_response = {k: v for k, v in current_user.items() if k != 'password_hash'}
    return jsonify({
        "success": True,
        "data": user_response
    })

@app.route('/api/profile', methods=['PUT'])
@token_required
def update_profile(current_user):
    data = request.json
    
    # Update user
    if 'email' in data:
        current_user['email'] = data['email']
    if 'bio' in data:
        current_user['bio'] = data.get('bio', '')
    
    user_response = {k: v for k, v in current_user.items() if k != 'password_hash'}
    
    return jsonify({
        "success": True,
        "data": user_response,
        "message": "Profile updated"
    })
```

---

### 5️⃣ Role-Based Access (5 minutes)

```python
def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user['role'] not in allowed_roles:
                return jsonify({
                    "success": False,
                    "error": "You don't have permission to access this resource"
                }), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator

# Admin-only route
@app.route('/api/admin/users', methods=['GET'])
@token_required
@role_required('admin')
def get_all_users(current_user):
    user_list = [
        {k: v for k, v in user.items() if k != 'password_hash'}
        for user in users.values()
    ]
    return jsonify({
        "success": True,
        "data": user_list
    })

# Moderator or Admin
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
@token_required
@role_required('admin', 'moderator')
def delete_post(current_user, post_id):
    # Delete post logic
    return jsonify({
        "success": True,
        "message": "Post deleted"
    })
```

---

### 💻 Live Activity: Complete Auth System

**Create: hour20_auth_system.py**

```python
"""
Complete Authentication System
Signup, Login, Protected Routes, Role-Based Access
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
CORS(app)

# Storage
users = {}
posts = {}
user_id_counter = 1
post_id_counter = 1

# Helper functions
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_token(user_id, username, role):
    payload = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")

# Decorators
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(" ")[1]
            except IndexError:
                return jsonify({"success": False, "error": "Invalid token format"}), 401
        
        if not token:
            return jsonify({"success": False, "error": "Token is missing"}), 401
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(payload['user_id'])
            
            if not current_user:
                return jsonify({"success": False, "error": "User not found"}), 401
            
        except jwt.ExpiredSignatureError:
            return jsonify({"success": False, "error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"success": False, "error": "Invalid token"}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user['role'] not in allowed_roles:
                return jsonify({
                    "success": False,
                    "error": "Insufficient permissions"
                }), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator

# Auth routes
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    global user_id_counter
    
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not all([username, email, password]):
        return jsonify({"success": False, "error": "All fields required"}), 400
    
    # Check duplicate
    for user in users.values():
        if user['username'] == username:
            return jsonify({"success": False, "error": "Username exists"}), 409
    
    # Create user
    user = {
        "id": user_id_counter,
        "username": username,
        "email": email,
        "password_hash": hash_password(password),
        "role": "user",
        "created_at": datetime.utcnow().isoformat()
    }
    
    users[user_id_counter] = user
    user_id_counter += 1
    
    token = create_token(user['id'], user['username'], user['role'])
    
    user_response = {k: v for k, v in user.items() if k != 'password_hash'}
    
    return jsonify({
        "success": True,
        "data": {"user": user_response, "token": token},
        "message": "Signup successful"
    }), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"success": False, "error": "Credentials required"}), 400
    
    user = None
    for u in users.values():
        if u['username'] == username:
            user = u
            break
    
    if not user or not verify_password(password, user['password_hash']):
        return jsonify({"success": False, "error": "Invalid credentials"}), 401
    
    token = create_token(user['id'], user['username'], user['role'])
    
    user_response = {k: v for k, v in user.items() if k != 'password_hash'}
    
    return jsonify({
        "success": True,
        "data": {"user": user_response, "token": token},
        "message": "Login successful"
    })

# Protected routes
@app.route('/api/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    user_response = {k: v for k, v in current_user.items() if k != 'password_hash'}
    return jsonify({"success": True, "data": user_response})

@app.route('/api/posts', methods=['POST'])
@token_required
def create_post(current_user):
    global post_id_counter
    
    data = request.json
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"success": False, "error": "Title and content required"}), 400
    
    post = {
        "id": post_id_counter,
        "title": title,
        "content": content,
        "author_id": current_user['id'],
        "author_username": current_user['username'],
        "created_at": datetime.utcnow().isoformat()
    }
    
    posts[post_id_counter] = post
    post_id_counter += 1
    
    return jsonify({
        "success": True,
        "data": post,
        "message": "Post created"
    }), 201

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
@token_required
def delete_post(current_user, post_id):
    post = posts.get(post_id)
    
    if not post:
        return jsonify({"success": False, "error": "Post not found"}), 404
    
    # Check ownership or admin
    if post['author_id'] != current_user['id'] and current_user['role'] != 'admin':
        return jsonify({"success": False, "error": "Not authorized"}), 403
    
    del posts[post_id]
    return jsonify({"success": True, "message": "Post deleted"})

# Admin-only routes
@app.route('/api/admin/users', methods=['GET'])
@token_required
@role_required('admin')
def get_all_users(current_user):
    user_list = [
        {k: v for k, v in user.items() if k != 'password_hash'}
        for user in users.values()
    ]
    return jsonify({"success": True, "data": user_list})

@app.route('/api/admin/users/<int:user_id>/role', methods=['PATCH'])
@token_required
@role_required('admin')
def update_user_role(current_user, user_id):
    user = users.get(user_id)
    
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404
    
    data = request.json
    new_role = data.get('role')
    
    if new_role not in ['user', 'moderator', 'admin']:
        return jsonify({"success": False, "error": "Invalid role"}), 400
    
    user['role'] = new_role
    
    return jsonify({
        "success": True,
        "message": f"User role updated to {new_role}"
    })

if __name__ == '__main__':
    # Create default admin user
    admin_password = hash_password("admin123")
    users[user_id_counter] = {
        "id": user_id_counter,
        "username": "admin",
        "email": "admin@blog.com",
        "password_hash": admin_password,
        "role": "admin",
        "created_at": datetime.utcnow().isoformat()
    }
    user_id_counter += 1
    
    print("Default admin created: username='admin', password='admin123'")
    app.run(debug=True)
```

---

### 🏠 Homework: Complete Auth System

```python
# homework20_complete_auth.py

# TODO: Enhance the authentication system with:

# 1. Refresh Tokens
# - Short-lived access token (15 minutes)
# - Long-lived refresh token (7 days)
# - /api/auth/refresh endpoint

# 2. Password Reset
# - /api/auth/forgot-password (send reset token)
# - /api/auth/reset-password (reset with token)

# 3. Email Verification
# - Send verification email on signup
# - /api/auth/verify-email endpoint

# 4. Account Management
# - Change password (requires old password)
# - Delete account
# - Account lockout after failed attempts

# 5. Advanced Security
# - Rate limiting
# - Token blacklist
# - Session management

# Implement and test all features!
```

---

### 📝 Key Takeaways

✅ bcrypt for password hashing
✅ JWT for stateless authentication
✅ Bearer token in Authorization header
✅ `@token_required` decorator for protected routes
✅ `@role_required` for authorization
✅ Never store passwords in plain text!

---

## 🎉 Part 2 Complete!

**You've learned:**
- Hours 11-12: OOP (inheritance, polymorphism, magic methods)
- Hour 13: Virtual environments & dependency management
- Hours 14-16: Databases (SQL, SQLAlchemy, MongoDB)
- Hour 17: REST API design principles
- Hours 18-19: Flask (routes, blueprints, validation, file upload)
- Hour 20: Authentication & authorization (JWT, bcrypt, protected routes)

**Next:** Part 3 - Frontend Development (React, state management, full-stack integration)





