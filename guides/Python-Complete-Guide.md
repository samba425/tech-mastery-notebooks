# 🐍 Python Complete Mastery Guide

> **Complete Python Reference for Interview Preparation and Skill Mastery**  
> From Beginner to Expert Level - All Concepts Covered

---

## 📚 Table of Contents

1. [Python Fundamentals](#1-python-fundamentals)
2. [Data Structures](#2-data-structures)
3. [Control Flow](#3-control-flow)
4. [Functions](#4-functions)
5. [Object-Oriented Programming](#5-object-oriented-programming)
6. [Advanced Features](#6-advanced-features)
7. [Modules and Packages](#7-modules-and-packages)
8. [File Operations](#8-file-operations)
9. [Algorithm Implementations](#9-algorithm-implementations)
10. [Concurrency & Parallelism](#10-concurrency--parallelism)
11. [Data Science Fundamentals](#11-data-science-fundamentals)
12. [Web Development Basics](#12-web-development-basics)
13. [Testing & Code Quality](#13-testing--code-quality)
14. [Advanced Python Features](#14-advanced-python-features)
15. [Best Practices](#15-best-practices)

---

## 1. Python Fundamentals

### Variables and Data Types

```python
# Basic data types
integer_var = 42
float_var = 3.14159
string_var = "Hello, Python!"
boolean_var = True
none_var = None

# Type checking
print(type(integer_var))  # <class 'int'>
print(isinstance(string_var, str))  # True
```

### Type Conversions

```python
# String to number
age = int("25")
price = float("99.99")

# Number to string
count_str = str(100)

# Boolean conversions
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False
print(bool("hi")) # True
```

### String Operations

```python
text = "Python Programming"

# Basic operations
print(f"Length: {len(text)}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Split: {text.split()}")

# String methods
print(text.startswith("Python"))  # True
print(text.endswith("ing"))       # True
print(text.find("Program"))       # 7
print(text.replace("Python", "Advanced Python"))
```

### String Formatting

```python
name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"Hello, {name}! You are {age} years old."

# format() method
message = "Hello, {}! You are {} years old.".format(name, age)

# % formatting (older style)
message = "Hello, %s! You are %d years old." % (name, age)
```

---

## 2. Data Structures

### Lists - Ordered, Mutable Collections

```python
# List creation and operations
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Accessing elements
first_fruit = fruits[0]      # "apple"
last_fruit = fruits[-1]      # "cherry"
subset = fruits[1:3]         # ["banana", "cherry"]

# List methods
fruits.append("date")        # Add to end
fruits.insert(1, "orange")  # Insert at index
removed = fruits.pop()       # Remove and return last
fruits.remove("banana")     # Remove specific item
fruits.sort()               # Sort in place
```

### List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
```

### Tuples - Ordered, Immutable Collections

```python
# Tuple creation
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Tuple unpacking
x, y = coordinates
r, g, b = colors

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

### Dictionaries - Key-Value Pairs

```python
# Dictionary creation
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
name = person["name"]           # KeyError if key doesn't exist
age = person.get("age", 0)      # Returns 0 if key doesn't exist

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

# Adding/updating
person["email"] = "alice@example.com"
person.update({"phone": "123-456-7890"})
```

### Dictionary Comprehensions

```python
# Basic dict comprehension
squares_dict = {x: x**2 for x in range(1, 6)}

# With condition
even_squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
```

### Sets - Unique Collections

```python
# Set creation
numbers = {1, 2, 3, 4, 5}
unique_chars = set("hello")  # {'h', 'e', 'l', 'o'}

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2         # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2   # {3, 4}
difference = set1 - set2     # {1, 2}
symmetric_diff = set1 ^ set2 # {1, 2, 5, 6}
```

---

## 3. Control Flow

### Conditional Statements

```python
# Basic if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator
status = "pass" if score >= 60 else "fail"

# Multiple conditions
if score >= 80 and score < 90:
    print("Good job!")
```

### Loops

```python
# For loops
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# Enumerate for index and value
for index, fruit in enumerate(["apple", "banana", "cherry"]):
    print(f"{index}: {fruit}")

# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip to next iteration
    if i == 7:
        break     # Exit loop
    print(i)
```

### Advanced Iteration

```python
# Zip for parallel iteration
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Loop with else (executes if loop completes normally)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")
```

---

## 4. Functions

### Basic Function Definition

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

# Function calls
message = greet("Alice")
result = add_numbers(5, 3)
```

### Function Parameters

```python
# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Keyword arguments
print(greet("Alice"))                    # "Hello, Alice!"
print(greet("Bob", greeting="Hi"))       # "Hi, Bob!"
print(greet(greeting="Hey", name="Charlie"))  # "Hey, Charlie!"

# Variable arguments
def sum_all(*args):
    return sum(args)

def create_profile(**kwargs):
    return kwargs

result = sum_all(1, 2, 3, 4, 5)  # 15
profile = create_profile(name="Alice", age=30, city="NYC")
```

### Lambda Functions

```python
# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

### Higher-Order Functions

```python
def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list."""
    return [operation(num) for num in numbers]

# Using with lambda
doubled = apply_operation([1, 2, 3, 4], lambda x: x * 2)

# Function as return value
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
```

---

## 5. Object-Oriented Programming

### Basic Classes

```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name    # Instance variable
        self.age = age      # Instance variable
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        self.age += 1

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())  # "Hi, I'm Alice and I'm 25 years old."
person1.have_birthday()
print(person1.age)  # 26
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # "Buddy says Woof!"
print(cat.speak())  # "Whiskers says Meow!"
```

### Special Methods (Magic Methods)

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return (self.title == other.title and 
                self.author == other.author)

book = Book("1984", "George Orwell", 328)
print(str(book))    # "1984 by George Orwell"
print(len(book))    # 328
```

### Method Types

```python
class Calculator:
    pi = 3.14159
    
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        """Instance method"""
        return a + b
    
    @classmethod
    def get_pi(cls):
        """Class method - operates on the class"""
        return cls.pi
    
    @staticmethod
    def multiply(a, b):
        """Static method - independent function"""
        return a * b

calc = Calculator("MyCal")
print(calc.add(2, 3))           # 5 (instance method)
print(Calculator.get_pi())      # 3.14159 (class method)
print(Calculator.multiply(4, 5)) # 20 (static method)
```

---

## 6. Advanced Features

### Decorators

```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints "Hello, Alice!" three times
```

### Generators

```python
def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

# Using generator
counter = count_up_to(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5

# Generator expressions
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Context Managers

```python
# Using with statement
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
# File is automatically closed

# Custom context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.4f} seconds")

with Timer():
    import time
    time.sleep(1)
# Output: Elapsed time: 1.0001 seconds

# Using contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print(f"Opening {filename}")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing {filename}")
        f.close()
```

---

## 7. Modules and Packages

### Importing Modules

```python
# Different import styles
import math
from math import pi, sqrt
from datetime import datetime as dt
import json as js

# Using imported modules
print(math.pi)      # 3.141592653589793
print(sqrt(16))     # 4.0
print(dt.now())     # Current datetime

# Standard library modules
import os
import sys
import random
from collections import defaultdict, Counter
```

### Creating Custom Modules

```python
# my_module.py
def calculate_area(radius):
    """Calculate area of a circle."""
    import math
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Calculate circumference of a circle."""
    import math
    return 2 * math.pi * radius

PI = 3.14159

# main.py
import my_module

area = my_module.calculate_area(5)
circumference = my_module.calculate_circumference(5)
```

### Package Structure

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
```

```python
# Importing from packages
from my_package import module1
from my_package.subpackage import submodule
```

---

## 8. File Operations

### Reading Files

```python
# Reading entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Reading line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Reading all lines into a list
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### Writing Files

```python
# Writing to file (overwrites existing)
with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a new line.\n")

# Appending to file
with open('output.txt', 'a') as f:
    f.write("This is appended.\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### Working with JSON

```python
import json

# Writing JSON
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"]
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Reading JSON
with open('data.json', 'r') as f:
    loaded_data = json.load(f)

# JSON strings
json_string = json.dumps(data, indent=2)
parsed_data = json.loads(json_string)
```

---

## 9. Algorithm Implementations

### Sorting Algorithms

```python
def bubble_sort(arr):
    """Bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Search Algorithms

```python
def binary_search(arr, target):
    """Binary search implementation."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

def linear_search(arr, target):
    """Linear search implementation."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  # Not found
```

### Dynamic Programming

```python
def fibonacci_dp(n, memo={}):
    """Fibonacci with memoization."""
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)
    return memo[n]

def knapsack(weights, values, capacity):
    """0/1 Knapsack problem."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

---

## 10. Concurrency & Parallelism

### Threading

```python
import threading
import time

def worker_function(name, duration):
    """Simulate work in a thread."""
    print(f"Worker {name} starting...")
    time.sleep(duration)
    print(f"Worker {name} finished")

# Creating and starting threads
threads = []
for i in range(3):
    thread = threading.Thread(
        target=worker_function, 
        args=(f"Thread-{i}", 1)
    )
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Thread-safe operations
class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value
```

### Asyncio

```python
import asyncio

async def fetch_data(url, delay):
    """Simulate async data fetching."""
    print(f"Starting to fetch {url}")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Finished fetching {url}")
    return f"Data from {url}"

async def main():
    """Run multiple async operations concurrently."""
    tasks = [
        fetch_data("url1", 1),
        fetch_data("url2", 2),
        fetch_data("url3", 1.5)
    ]
    
    results = await asyncio.gather(*tasks)
    return results

# Run async code
# results = asyncio.run(main())
```

### Multiprocessing

```python
import multiprocessing

def cpu_intensive_task(n):
    """CPU intensive task for multiprocessing."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def parallel_processing():
    """Use multiprocessing for CPU-bound tasks."""
    with multiprocessing.Pool() as pool:
        tasks = [1000000] * 4
        results = pool.map(cpu_intensive_task, tasks)
    return results

# Thread vs Process pools
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def concurrent_execution():
    # Thread pool for I/O-bound tasks
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(fetch_data, f"url{i}", 1) for i in range(4)]
        thread_results = [f.result() for f in futures]
    
    # Process pool for CPU-bound tasks
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_intensive_task, 100000) for _ in range(4)]
        process_results = [f.result() for f in futures]
    
    return thread_results, process_results
```

---

## 11. Data Science Fundamentals

### NumPy Basics

```python
import numpy as np

# Array creation
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Array operations
squared = arr ** 2
normalized = (arr - arr.mean()) / arr.std()

# Mathematical functions
print(f"Sum: {np.sum(arr)}")
print(f"Mean: {np.mean(arr)}")
print(f"Standard deviation: {np.std(arr)}")

# Array manipulation
reshaped = arr.reshape(-1, 1)  # Column vector
concatenated = np.concatenate([arr, arr])

# Linear algebra
dot_product = np.dot(arr, arr)
matrix_det = np.linalg.det(matrix[:2, :])  # 2x2 matrix determinant
```

### Pandas Basics

```python
import pandas as pd

# DataFrame creation
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000],
    'department': ['Engineering', 'Marketing', 'Engineering', 'Sales']
}
df = pd.DataFrame(data)

# Data selection
print(df['name'])  # Single column
print(df[['name', 'age']])  # Multiple columns
print(df[df['age'] > 28])  # Filtering

# Data manipulation
df['age_group'] = df['age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
sorted_df = df.sort_values('salary', ascending=False)

# Grouping and aggregation
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'max'],
    'age': 'mean'
})

# Data cleaning
df_with_nulls = df.copy()
df_with_nulls.loc[0, 'salary'] = np.nan
cleaned_df = df_with_nulls.fillna(df_with_nulls.mean())
```

---

## 12. Web Development Basics

### Flask Framework

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Python Web Development!"

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        users = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
        return jsonify({"users": users})
    
    elif request.method == 'POST':
        user_data = request.get_json()
        new_user = {
            "id": 3,
            "name": user_data.get('name'),
            "email": user_data.get('email')
        }
        return jsonify({"message": "User created", "user": new_user}), 201

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = {"id": user_id, "name": "Sample User", "email": "user@example.com"}
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
```

### Database Integration

```python
import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.init_db()
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
        finally:
            conn.close()
    
    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    
    def create_user(self, name, email):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_all_users(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
```

---

## 13. Testing & Code Quality

### Unit Testing with unittest

```python
import unittest
from unittest.mock import Mock, patch

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def get_random_number(self):
        import random
        return random.randint(1, 100)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    @patch('random.randint')
    def test_get_random_number_mocked(self, mock_randint):
        """Test with mocked random function."""
        mock_randint.return_value = 42
        result = self.calc.get_random_number()
        self.assertEqual(result, 42)
        mock_randint.assert_called_once_with(1, 100)

if __name__ == '__main__':
    unittest.main()
```

### Pytest Framework

```python
import pytest

# Fixtures
@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def calculator():
    """Fixture providing calculator instance."""
    return Calculator()

# Test functions
def test_list_operations(sample_data):
    """Test basic list operations."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15
    assert max(sample_data) == 5

def test_calculator_add(calculator):
    """Test calculator addition."""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(calculator, a, b, expected):
    """Test addition with multiple parameter sets."""
    assert calculator.add(a, b) == expected

# Test classes
class TestCalculatorAdvanced:
    def test_multiple_operations(self, calculator):
        """Test multiple operations in sequence."""
        result1 = calculator.add(2, 3)
        result2 = calculator.divide(result1, 5)
        assert result2 == 1.0
```

---

## 14. Advanced Python Features

### Metaclasses

```python
class SingletonMeta(type):
    """Metaclass that creates singleton instances."""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_string = "Database connected"
    
    def query(self, sql):
        return f"Executing: {sql}"

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance
```

### Descriptors

```python
class Validated:
    """Descriptor for validated attributes."""
    
    def __init__(self, validator, name=None):
        self.validator = validator
        self.name = name
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        obj.__dict__[self.name] = value

class Person:
    name = Validated(lambda x: isinstance(x, str) and len(x) > 0)
    age = Validated(lambda x: isinstance(x, int) and 0 <= x <= 150)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
# person.age = -5  # Would raise ValueError
```

### Protocol and Type Hints

```python
from typing import Protocol, TypeVar, Generic
from abc import ABC, abstractmethod

# Protocol for structural typing
class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render_shape(shape: Drawable) -> str:
    return shape.draw()

# Generic types
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()
```

---

## 15. Best Practices

### Code Organization

```python
# Use meaningful variable names
user_age = 25  # Good
a = 25         # Bad

# Follow PEP 8 naming conventions
class UserManager:     # CapitalizedWords for classes
    def get_user(self):  # lowercase_with_underscores for functions
        pass

USER_CONSTANT = "value"  # UPPER_CASE for constants

# Use type hints
def calculate_area(radius: float) -> float:
    return 3.14159 * radius ** 2

# Docstrings for documentation
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Error Handling

```python
# Specific exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(f"Invalid value: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exceptions occurred")
finally:
    print("This always executes")

# Custom exceptions
class ValidationError(Exception):
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "age")
    if age < 0:
        raise ValidationError("Age cannot be negative", "age")
```

### Performance Tips

```python
# Use list comprehensions instead of loops
# Good
squares = [x**2 for x in range(1000)]

# Less efficient
squares = []
for x in range(1000):
    squares.append(x**2)

# Use join for string concatenation
# Good
words = ["Hello", "World", "Python"]
sentence = " ".join(words)

# Less efficient
sentence = ""
for word in words:
    sentence += word + " "

# Use enumerate instead of range(len())
# Good
for i, item in enumerate(items):
    print(f"{i}: {item}")

# Less pythonic
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

---

## 🚀 Next Steps for Mastery

1. **Practice Coding Challenges**
   - LeetCode, HackerRank, CodeSignal
   - Focus on algorithms and data structures

2. **Build Real Projects**
   - Web applications with Django/Flask
   - Data analysis projects with pandas
   - Automation scripts

3. **Advanced Topics**
   - Async programming with asyncio
   - Design patterns implementation
   - Performance optimization

4. **Testing and Quality**
   - Test-driven development (TDD)
   - Code coverage analysis
   - Static type checking with mypy

5. **Open Source Contribution**
   - Contribute to Python packages
   - Create your own packages
   - Learn collaborative development

---

## 📖 Key Python Concepts Summary

| Category | Key Topics |
|----------|------------|
| **Fundamentals** | Variables, data types, string operations |
| **Data Structures** | Lists, dicts, sets, tuples, comprehensions |
| **Control Flow** | Conditionals, loops, iteration patterns |
| **Functions** | Parameters, lambdas, decorators, generators |
| **OOP** | Classes, inheritance, special methods |
| **Advanced** | Context managers, metaclasses, descriptors |
| **Concurrency** | Threading, asyncio, multiprocessing |
| **Testing** | unittest, pytest, mocking |
| **Best Practices** | PEP 8, type hints, error handling |

---

> **🎉 Congratulations!** You now have a complete Python reference covering all concepts from beginner to expert level. This guide prepares you for any Python interview, project, or advanced development work.