# Python Complete Learning Guide: Zero to Hero 🐍

> A comprehensive guide covering Python fundamentals through advanced topics with practical examples

## 📚 Table of Contents

1. [Python Fundamentals](#1-python-fundamentals)
2. [Virtual Environments & Package Management](#2-virtual-environments--package-management)
   - [Traditional Virtual Environments (venv)](#21-traditional-virtual-environments-venv)
   - [UV - Modern Python Package Manager](#22-uv---modern-python-package-manager)
3. [Data Types](#3-data-types)
4. [Conditionals](#4-conditionals)
5. [Loops & Control Flow](#5-loops--control-flow)
   - [Walrus Operator](#55-walrus-operator)
6. [Functions](#6-functions)
7. [Modules & Packages](#7-modules--packages)
8. [List Comprehensions](#8-list-comprehensions)
9. [Generators](#9-generators)
10. [Decorators](#10-decorators)
11. [Object-Oriented Programming](#11-object-oriented-programming)
12. [Exception Handling](#12-exception-handling)
13. [File I/O & Data Persistence](#13-file-io--data-persistence)
14. [Threading & Concurrency](#14-threading--concurrency)
   - [GIL Deep Dive](#147-gil-global-interpreter-lock)
   - [Advanced Multiprocessing](#148-advanced-multiprocessing)
15. [Async Programming](#15-async-programming)
16. [Pydantic & Data Validation](#16-pydantic--data-validation)
   - [Advanced Pydantic](#164-advanced-pydantic-features)
17. [Mini Projects & Real-World Applications](#17-mini-projects--real-world-applications)

---

## 1. Python Fundamentals

### 1.1 Variables and Memory Management

Python uses dynamic typing and reference counting for memory management. Understanding how Python handles variables is crucial.

**Concept: Variable Assignment and Identity**

```python
# Variables point to objects in memory
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

# Each value has a unique ID in memory
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
```

**Key Points:**
- Variables are references to objects
- `id()` function returns the memory address
- Small integers (-5 to 256) are cached by Python for efficiency

### 1.2 Basic Data Types

```python
# Numbers
integer_num = 42
float_num = 3.14
complex_num = 3 + 4j

# Strings
name = "Python"
multiline = """This is a
multiline string"""

# Boolean
is_active = True
is_complete = False

# None
empty_value = None
```

---

## 2. Virtual Environments & Package Management

### 2.1 Traditional Virtual Environments (venv)

#### Why Virtual Environments?

Virtual environments isolate project dependencies, preventing version conflicts between different projects.

**Creating and Using Virtual Environments:**

```bash
# Create virtual environment
python -m venv myenv

# Activate (macOS/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages
pip install requests pandas

# Deactivate
deactivate

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

**Best Practices:**
- One virtual environment per project
- Always activate before installing packages
- Keep requirements.txt updated
- Add venv folder to .gitignore

---

### 2.2 UV - Modern Python Package Manager

#### What is UV?

**UV** is an extremely fast Python package and project manager, written in Rust. It's designed to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, and `virtualenv` with a single, unified tool.

**Key Features:**
- ⚡ **10-100x faster** than pip
- 🔒 **Built-in dependency resolution** with lockfiles
- 🐍 **Python version management** (like pyenv)
- 📦 **Project scaffolding** and management
- 🚀 **Zero configuration** required
- 🔄 **Compatible with pip** ecosystem

#### Installation

```bash
# Install UV (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install UV (Windows)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install via pip (alternative)
pip install uv

# Verify installation
uv --version
```

#### Quick Start with UV

**1. Creating a New Project:**

```bash
# Create a new Python project
uv init my-project
cd my-project

# Project structure created:
# my-project/
# ├── .python-version
# ├── pyproject.toml
# ├── README.md
# └── hello.py
```

**2. Managing Python Versions:**

```bash
# Install specific Python version
uv python install 3.12

# Use specific Python version for project
uv python pin 3.12

# List available Python versions
uv python list

# List installed Python versions
uv python list --only-installed
```

**3. Adding Dependencies:**

```bash
# Add a package
uv add requests

# Add development dependency
uv add --dev pytest

# Add specific version
uv add "numpy>=1.24,<2.0"

# Add from requirements.txt
uv add -r requirements.txt
```

**4. Running Commands:**

```bash
# Run Python script
uv run python script.py

# Run Python module
uv run -m pytest

# Run with specific Python version
uv run --python 3.12 python script.py
```

#### UV vs Traditional Tools

| Feature | pip | poetry | uv |
|---------|-----|--------|-----|
| Speed | Slow | Medium | **Very Fast** |
| Dependency Resolution | Basic | Good | **Excellent** |
| Lockfile | No | Yes | **Yes** |
| Python Version Management | No | No | **Yes** |
| Project Management | No | Yes | **Yes** |
| Installation Time (100 packages) | ~60s | ~30s | **~3s** |

#### Practical Examples

**Example 1: Data Science Project with UV**

```bash
# Create new data science project
uv init data-analysis
cd data-analysis

# Install Python 3.11
uv python install 3.11
uv python pin 3.11

# Add data science packages
uv add pandas numpy matplotlib seaborn scikit-learn jupyter

# Add dev tools
uv add --dev black ruff pytest

# Run Jupyter notebook
uv run jupyter notebook
```

**Example 2: Web Application with UV**

```bash
# Create new web project
uv init flask-app
cd flask-app

# Add Flask and dependencies
uv add flask flask-sqlalchemy python-dotenv

# Add development dependencies
uv add --dev pytest pytest-flask black

# Create app.py
cat > app.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from UV-powered Flask!"

if __name__ == '__main__':
    app.run(debug=True)
EOF

# Run the application
uv run python app.py
```

**Example 3: Microservice with FastAPI**

```bash
# Initialize project
uv init fastapi-service
cd fastapi-service

# Add dependencies
uv add fastapi uvicorn pydantic

# Create main.py
cat > main.py << 'EOF'
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "FastAPI with UV"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.name, "price": item.price}
EOF

# Run the service
uv run uvicorn main:app --reload
```

#### UV Commands Cheat Sheet

```bash
# Project Management
uv init <project>           # Create new project
uv add <package>            # Add dependency
uv remove <package>         # Remove dependency
uv sync                     # Sync dependencies with lockfile
uv lock                     # Update lockfile

# Python Version Management
uv python install <version> # Install Python version
uv python pin <version>     # Pin Python version for project
uv python list              # List available versions

# Running Code
uv run <command>            # Run command in project environment
uv run python <script>      # Run Python script
uv run -m <module>          # Run Python module

# Package Installation
uv pip install <package>    # Install package (pip-compatible)
uv pip list                 # List installed packages
uv pip freeze               # Export installed packages
uv pip uninstall <package>  # Uninstall package

# Virtual Environments
uv venv                     # Create virtual environment
uv venv --python 3.12       # Create with specific Python version

# Tool Management
uv tool install <tool>      # Install CLI tool globally
uv tool run <tool>          # Run tool without installing
uv tool list                # List installed tools
```

#### Working with pyproject.toml

UV uses `pyproject.toml` for project configuration:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.7.0",
    "ruff>=0.0.285",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.4.0",
]

[tool.ruff]
line-length = 88
target-version = "py311"
```

#### Migrating from pip to UV

```bash
# If you have requirements.txt
uv init my-project
cd my-project
uv add -r requirements.txt

# If you have poetry
uv init my-project
cd my-project
# UV automatically reads pyproject.toml
uv sync

# If you have pipenv
uv init my-project
cd my-project
# Convert Pipfile to pyproject.toml (manual step)
uv sync
```

#### UV Best Practices

**1. Use UV for New Projects:**
```bash
# Start fresh with UV
uv init my-new-project
cd my-new-project
uv add <dependencies>
```

**2. Pin Python Versions:**
```bash
# Ensure consistent Python version across team
uv python pin 3.12
# This creates .python-version file
```

**3. Use Lockfiles for Reproducibility:**
```bash
# Lockfile ensures exact versions
uv lock
# Commit uv.lock to version control
```

**4. Separate Dev Dependencies:**
```bash
# Production dependencies
uv add requests pandas

# Development dependencies
uv add --dev pytest black ruff mypy
```

**5. Use UV Run for Scripts:**
```bash
# Instead of activating virtual env
# Old way:
source .venv/bin/activate
python script.py

# UV way:
uv run python script.py
```

#### UV Tools - Global CLI Tools

```bash
# Install CLI tools globally (like pipx)
uv tool install ruff        # Linter
uv tool install black       # Formatter
uv tool install httpie      # HTTP client

# Run without installing
uv tool run httpie https://api.github.com

# List installed tools
uv tool list

# Update a tool
uv tool upgrade ruff
```

#### Performance Comparison

**Installing 50 packages:**

```bash
# Traditional pip
time pip install -r requirements.txt
# Real: 45.2 seconds

# poetry
time poetry install
# Real: 28.5 seconds

# UV
time uv sync
# Real: 2.1 seconds  ⚡
```

#### Troubleshooting UV

```bash
# Clear cache
uv cache clean

# Verbose output
uv add requests -v

# Force reinstall
uv sync --reinstall

# Check UV configuration
uv config list

# Update UV itself
uv self update
```

#### Real-World Example: Complete Project Setup

```bash
# 1. Create project structure
uv init ml-sentiment-analysis
cd ml-sentiment-analysis

# 2. Set Python version
uv python install 3.11
uv python pin 3.11

# 3. Add ML dependencies
uv add transformers torch scikit-learn pandas numpy

# 4. Add development tools
uv add --dev jupyter pytest black ruff mypy

# 5. Create project structure
mkdir -p src/models src/utils tests data notebooks

# 6. Create sample code
cat > src/sentiment.py << 'EOF'
from transformers import pipeline

def analyze_sentiment(text: str) -> dict:
    """Analyze sentiment of text using transformers."""
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    return {
        "text": text,
        "sentiment": result["label"],
        "confidence": result["score"]
    }

if __name__ == "__main__":
    result = analyze_sentiment("UV is amazing!")
    print(f"Sentiment: {result['sentiment']} ({result['confidence']:.2%})")
EOF

# 7. Run the code
uv run python src/sentiment.py

# 8. Create Jupyter notebook
cat > notebooks/exploration.ipynb << 'EOF'
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.sentiment import analyze_sentiment\n",
    "analyze_sentiment('Python with UV is fast!')"
   ]
  }
 ]
}
EOF

# 9. Start Jupyter
uv run jupyter notebook
```

#### When to Use UV vs Traditional Tools

**Use UV when:**
- ✅ Starting new projects
- ✅ Speed is important (large dependencies)
- ✅ Need Python version management
- ✅ Want modern dependency resolution
- ✅ Working on team projects (lockfiles)

**Stick with pip/venv when:**
- ⚠️ Working on legacy projects
- ⚠️ Company policy requires traditional tools
- ⚠️ Very simple scripts with no dependencies
- ⚠️ Teaching Python basics to beginners

---

## 3. Data Types

### 3.1 Strings

**String Operations:**

```python
# String creation
text = "Hello, Python!"

# String methods
upper_text = text.upper()          # "HELLO, PYTHON!"
lower_text = text.lower()          # "hello, python!"
title_text = text.title()          # "Hello, Python!"

# String slicing
first_five = text[:5]              # "Hello"
last_seven = text[-7:]             # "Python!"

# String formatting
name = "Alice"
age = 30
formatted = f"{name} is {age} years old"

# String methods
text.startswith("Hello")           # True
text.endswith("!")                 # True
text.replace("Python", "World")    # "Hello, World!"
text.split(", ")                   # ["Hello", "Python!"]
```

### 3.2 Lists

**List Operations:**

```python
# List creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# List methods
fruits.append("orange")            # Add to end
fruits.insert(1, "mango")          # Insert at position
fruits.remove("banana")            # Remove by value
popped = fruits.pop()              # Remove and return last item

# List operations
combined = fruits + numbers        # Concatenation
repeated = fruits * 2              # Repetition
length = len(fruits)               # Length

# List slicing
first_two = fruits[:2]
last_two = fruits[-2:]
reversed_list = fruits[::-1]

# List comprehension (covered later)
squares = [x**2 for x in range(5)]
```

### 3.3 Tuples

**Immutable Sequences:**

```python
# Tuple creation
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_element = (42,)             # Note the comma!

# Tuple unpacking
x, y = coordinates
r, g, b = colors

# Tuple methods
index = colors.index("green")      # 1
count = colors.count("red")        # 1

# Why use tuples?
# - Immutable (cannot be changed)
# - Faster than lists
# - Can be used as dictionary keys
# - Indicate data shouldn't change
```

### 3.4 Dictionaries

**Key-Value Pairs:**

```python
# Dictionary creation
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"]
}

# Accessing values
name = student["name"]
age = student.get("age")           # Safer - returns None if key missing
courses = student.get("courses", [])  # With default value

# Dictionary methods
student["grade"] = "A"             # Add new key-value
student.update({"semester": 3})    # Update multiple values

keys = student.keys()              # Get all keys
values = student.values()          # Get all values
items = student.items()            # Get all key-value pairs

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 3.5 Sets

**Unique Collections:**

```python
# Set creation
fruits_set = {"apple", "banana", "cherry"}
numbers_set = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} - duplicates removed

# Set operations
fruits_set.add("orange")
fruits_set.remove("banana")
fruits_set.discard("mango")        # Won't raise error if not found

# Set mathematical operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2                # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2         # {3, 4}
difference = set1 - set2           # {1, 2}
symmetric_diff = set1 ^ set2       # {1, 2, 5, 6}
```

---

## 4. Conditionals

### 4.1 If-Else Statements

**Basic Conditionals:**

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# If-else
score = 85
if score >= 90:
    print("Grade: A")
else:
    print("Grade: B or lower")

# If-elif-else
temperature = 25
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
else:
    print("It's cold")
```

### 4.2 Comparison Operators

```python
# Comparison operators
x = 10
y = 20

x == y    # Equal to
x != y    # Not equal to
x > y     # Greater than
x < y     # Less than
x >= y    # Greater than or equal to
x <= y    # Less than or equal to

# Logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or not has_license:
    print("Cannot drive")
```

### 4.3 Ternary Operator

```python
# Ternary operator (conditional expression)
age = 20
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

### 4.4 Match-Case (Python 3.10+)

```python
# Pattern matching (Python 3.10+)
def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(get_day_type("Monday"))  # Weekday
```

---

## 5. Loops & Control Flow

### 5.1 For Loops

**Iterating Over Sequences:**

```python
# Loop over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop over range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):     # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Loop over dictionary
student = {"name": "Alice", "age": 22}

# Loop over keys
for key in student:
    print(key)

# Loop over values
for value in student.values():
    print(value)

# Loop over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

### 5.2 While Loops

**Condition-Based Iteration:**

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# While with continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
```

### 5.3 Loop Control Statements

```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue - skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4

# Else clause - executes if loop completes normally
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")
```

### 5.4 Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # New line after each row

# 2D list iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

---

### 5.5 Walrus Operator (`:=`) - Python 3.8+

**Assignment Expressions:**

The walrus operator (`:=`) allows you to assign values to variables as part of an expression. It's called the "walrus operator" because `:=` looks like a walrus lying on its side!

```python
# Without walrus operator
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")

# With walrus operator - more concise
value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")
```

**Use Cases:**

**1. In Conditionals:**

```python
# Check user input and use it immediately
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")
```

**2. In While Loops:**

```python
# Reading input until valid
flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors:", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You chose {flavor} chai")
```

**3. In List Comprehensions:**

```python
# Process and filter in one step
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate squares but only keep those > 25
large_squares = [square for n in numbers if (square := n**2) > 25]
print(large_squares)  # [36, 49, 64, 81, 100]
```

**4. File Processing:**

```python
# Read file line by line
with open('data.txt', 'r') as file:
    while (line := file.readline()):
        print(line.strip())
```

**5. Reducing Function Calls:**

```python
# Without walrus - function called twice
def expensive_computation(x):
    print(f"Computing for {x}")
    return x ** 2 + x * 3

if expensive_computation(5) > 20:
    result = expensive_computation(5)  # Called again!
    print(result)

# With walrus - function called once
if (result := expensive_computation(5)) > 20:
    print(result)
```

**Best Practices:**
- ✅ Use when it improves readability
- ✅ Great for input validation loops
- ✅ Useful in comprehensions with filtering
- ❌ Don't overuse - can make code harder to read
- ❌ Avoid in complex expressions

---

## 6. Functions

### 6.1 Function Basics

**Eliminating Code Duplication:**

```python
# Without functions (duplication)
print("Aman ordered masala chai!")
print("Hitesh ordered Ginger chai!")
print("Jia ordered Tulsi chai!")

# With functions (reusable)
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")

print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
```

### 6.2 Function Parameters

**Different Parameter Types:**

```python
# Positional parameters
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")  # Hello, Alice!

# Default parameters
def power(base, exponent=2):
    return base ** exponent

power(3)       # 9 (3^2)
power(3, 3)    # 27 (3^3)

# Keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet(pet_name="Willie", animal_type="dog")

# *args - variable positional arguments
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - variable keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

### 6.3 Return Values

```python
# Single return value
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# Multiple return values
def get_user():
    return "Alice", 30, "New York"

name, age, city = get_user()

# Return None
def greet(name):
    print(f"Hello, {name}")
    # Implicitly returns None

result = greet("Bob")  # result is None
```

### 6.4 Function Scopes

**Local, Nonlocal, and Global Scopes:**

```python
# Global scope
global_var = "I'm global"

def outer():
    # Enclosing scope
    outer_var = "I'm in outer"
    
    def inner():
        # Local scope
        inner_var = "I'm in inner"
        print(global_var)  # Accessible
        print(outer_var)   # Accessible
        print(inner_var)   # Accessible
    
    inner()

# Using global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# Using nonlocal keyword
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

### 6.5 Lambda Functions

```python
# Lambda function (anonymous function)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda in sorted()
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

sorted_students = sorted(students, key=lambda s: s["grade"])

# Lambda in filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Lambda in map()
squared = list(map(lambda x: x ** 2, numbers))
```

### 6.6 Built-in Functions

**Commonly Used Built-in Functions:**

```python
# Type conversion
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
list("abc")     # ['a', 'b', 'c']

# Math functions
abs(-5)         # 5
max(1, 5, 3)    # 5
min(1, 5, 3)    # 1
round(3.7)      # 4
pow(2, 3)       # 8

# Sequence functions
len([1, 2, 3])              # 3
sum([1, 2, 3])              # 6
sorted([3, 1, 2])           # [1, 2, 3]
reversed([1, 2, 3])         # [3, 2, 1] (iterator)
enumerate(["a", "b", "c"])  # [(0, 'a'), (1, 'b'), (2, 'c')]
zip([1, 2], ["a", "b"])     # [(1, 'a'), (2, 'b')]

# Type checking
type(42)                    # <class 'int'>
isinstance(42, int)         # True

# Input/Output
input("Enter name: ")       # Get user input
print("Hello")              # Print to console
```

---

## 7. Modules & Packages

### 7.1 What are Modules?

A **module** is a Python file containing definitions and statements. Modules help organize code into reusable components.

**Creating a Simple Module:**

```python
# math_utils.py
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

PI = 3.14159

class Calculator:
    def multiply(self, a, b):
        return a * b
```

### 7.2 Importing Modules

**Different Ways to Import:**

```python
# 1. Import entire module
import math_utils
result = math_utils.add(5, 3)
print(math_utils.PI)

# 2. Import specific items
from math_utils import add, subtract
result = add(5, 3)

# 3. Import with alias
import math_utils as mu
result = mu.add(5, 3)

# 4. Import everything (not recommended)
from math_utils import *
result = add(5, 3)  # Can cause naming conflicts

# 5. Import specific items with alias
from math_utils import add as addition
result = addition(5, 3)
```

### 7.3 Built-in Modules

**Commonly Used Built-in Modules:**

```python
# Math module
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
print(math.ceil(4.3))     # 5
print(math.floor(4.7))    # 4

# Random module
import random
print(random.randint(1, 10))           # Random integer
print(random.choice(['a', 'b', 'c']))  # Random choice
print(random.random())                 # Random float [0.0, 1.0)

# Datetime module
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
tomorrow = now + timedelta(days=1)

# OS module
import os
print(os.getcwd())                # Current directory
print(os.listdir('.'))            # List files
os.makedirs('new_folder', exist_ok=True)

# JSON module
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)

# Collections module
from collections import Counter, defaultdict, deque
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counts)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

### 7.4 Creating Packages

A **package** is a directory containing Python modules and a special `__init__.py` file.

**Package Structure:**

```
chai_business/
├── __init__.py
├── main.py
├── recipes/
│   ├── __init__.py
│   └── flavors.py
└── utils/
    ├── __init__.py
    └── discounts.py
```

**Example Package Implementation:**

**File: `chai_business/recipes/flavors.py`**
```python
def masala_chai():
    return "Masala chai with spices"

def ginger_chai():
    return "Ginger chai - fresh and spicy"

def elaichi_chai():
    return "Elaichi chai with cardamom"

SPECIALTY_FLAVORS = ["masala", "ginger", "elaichi"]
```

**File: `chai_business/recipes/__init__.py`**
```python
# Make specific functions available at package level
from .flavors import masala_chai, ginger_chai

# Package-level variable
__version__ = "1.0.0"
```

**File: `chai_business/utils/discounts.py`**
```python
def apply_discount(price, discount_percent):
    """Apply percentage discount to price"""
    return price * (1 - discount_percent / 100)

def bulk_discount(quantity, unit_price):
    """Calculate bulk order discount"""
    if quantity >= 10:
        return apply_discount(unit_price * quantity, 10)
    return unit_price * quantity
```

**File: `chai_business/main.py`**
```python
# Different import styles
import recipes.flavors
from recipes.flavors import elaichi_chai, ginger_chai
from utils.discounts import apply_discount

# Using imported functions
print(recipes.flavors.masala_chai())
print(ginger_chai())

# Calculate discounted price
original_price = 50
discounted = apply_discount(original_price, 15)
print(f"Price after 15% discount: ${discounted}")
```

### 7.5 The `__init__.py` File

The `__init__.py` file can be empty or contain initialization code for the package.

```python
# chai_business/__init__.py

# Import commonly used items
from .recipes.flavors import masala_chai, ginger_chai
from .utils.discounts import apply_discount

# Package metadata
__version__ = "1.0.0"
__author__ = "Chai Master"
__all__ = ["masala_chai", "ginger_chai", "apply_discount"]

# Package-level initialization
print(f"Chai Business Package v{__version__} initialized")

# Package-level constants
DEFAULT_PRICE = 50
AVAILABLE_SIZES = ["small", "medium", "large"]
```

**Using the package:**

```python
import chai_business

print(chai_business.__version__)
print(chai_business.masala_chai())
print(chai_business.DEFAULT_PRICE)
```

### 7.6 Relative vs Absolute Imports

```python
# Absolute imports (recommended)
from chai_business.recipes.flavors import masala_chai
from chai_business.utils.discounts import apply_discount

# Relative imports (within package)
# In chai_business/recipes/flavors.py
from ..utils.discounts import apply_discount  # Go up one level
from .special_recipes import premium_chai     # Same level
```

### 7.7 Module Search Path

Python searches for modules in this order:

```python
import sys

# View module search paths
print(sys.path)

# Add custom path
sys.path.append('/path/to/my/modules')

# First location searched
# 1. Current directory
# 2. PYTHONPATH environment variable
# 3. Installation-dependent default paths
```

### 7.8 Checking Module Location

```python
import math
import requests

# Find where module is located
print(math.__file__)        # Built-in module location
print(requests.__file__)    # Third-party module location

# Check if module has attribute
print(hasattr(math, 'sqrt'))  # True
print(dir(math))              # List all attributes
```

### 7.9 Reloading Modules

```python
import importlib
import my_module

# Reload module after changes (useful in development)
importlib.reload(my_module)
```

### 7.10 Best Practices

```python
# ✅ Good: Specific imports at top of file
from datetime import datetime, timedelta
from collections import Counter

# ✅ Good: Group imports
# Standard library imports
import os
import sys
import json

# Third-party imports
import requests
import pandas as pd

# Local application imports
from my_package import my_module

# ❌ Avoid: Wildcard imports
from module import *  # Can cause naming conflicts

# ❌ Avoid: Import inside functions (usually)
def my_function():
    import heavy_module  # Only do if absolutely necessary
```

---

## 8. List Comprehensions

### 8.1 List Comprehensions

**Concise List Creation:**

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Real-world example: Filtering tea menu
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
# ['Iced Lemon Tea', 'Iced Peach Tea']

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With if-else
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

### 8.2 Set Comprehensions

```python
# Set comprehension
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3]}
# {1, 4, 9}

# With condition
even_set = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

### 8.3 Dictionary Comprehensions

```python
# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person = {k: v for k, v in zip(keys, values)}
# {'name': 'Alice', 'age': 30, 'city': 'New York'}

# With condition
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
passed = {name: grade for name, grade in students.items() if grade >= 80}
# {'Alice': 85, 'Bob': 92}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

### 8.4 Generator Expressions

```python
# Generator expression (lazy evaluation)
gen = (x**2 for x in range(1000000))  # Doesn't compute immediately

# Use next() to get values
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# Memory efficient for large datasets
sum_of_squares = sum(x**2 for x in range(1000000))
```

---

## 9. Generators

### 9.1 Generator Functions

**Memory-Efficient Iteration:**

```python
# Generator function with yield
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# Iterate through generator
for cup in stall:
    print(cup)

# Or use next()
chai = serve_chai()
print(next(chai))  # Cup 1: Masala Chai
print(next(chai))  # Cup 2: Ginger Chai
print(next(chai))  # Cup 3: Elaichi Chai
# print(next(chai))  # Raises StopIteration

# Comparison with regular function
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]  # All in memory at once

def get_chai_gen():
    yield "Cup 1"  # One at a time
    yield "Cup 2"
    yield "Cup 3"
```

### 8.2 Infinite Generators

```python
# Infinite generator
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 8.3 Generator Methods

```python
# send() method
def echo_generator():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")  # Received: Hello
gen.send("World")  # Received: World

# close() method
def my_generator():
    try:
        while True:
            yield "Value"
    except GeneratorExit:
        print("Generator closed")

gen = my_generator()
print(next(gen))  # Value
gen.close()       # Generator closed
# print(next(gen))  # Raises StopIteration
```

### 8.4 Generator Use Cases

```python
# Reading large files
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Processing data in chunks
def process_in_chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

data = list(range(100))
for chunk in process_in_chunks(data, 10):
    print(f"Processing chunk: {chunk}")

# Pipeline processing
def numbers():
    for i in range(10):
        yield i

def square(numbers):
    for n in numbers:
        yield n ** 2

def add_ten(numbers):
    for n in numbers:
        yield n + 10

pipeline = add_ten(square(numbers()))
print(list(pipeline))  # [10, 11, 14, 19, 26, 35, 46, 59, 74, 91]
```

---

## 10. Decorators

### 10.1 Basic Decorators

**Function Wrappers:**

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

greet()
# Output:
# Before function runs
# Hello from decorators class from chaicode
# After function runs

print(greet.__name__)  # greet (preserved by @wraps)
```

### 9.2 Decorators with Arguments

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### 9.3 Logging Decorator

```python
import logging
from functools import wraps
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        start_time = datetime.now()
        
        result = func(*args, **kwargs)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        logging.info(f"{func.__name__} completed in {execution_time:.4f}s")
        
        return result
    return wrapper

@log_execution
def process_data(data):
    # Simulate processing
    import time
    time.sleep(1)
    return f"Processed {len(data)} items"

result = process_data([1, 2, 3, 4, 5])
```

### 9.4 Authentication Decorator

```python
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulate authentication check
        is_authenticated = kwargs.get('authenticated', False)
        
        if not is_authenticated:
            raise PermissionError("Authentication required")
        
        return func(*args, **kwargs)
    return wrapper

@require_auth
def access_secret_data(authenticated=False):
    return "Secret data revealed!"

# This will raise PermissionError
# access_secret_data()

# This will work
print(access_secret_data(authenticated=True))
```

### 9.5 Class Decorators

```python
def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database initialized")

db1 = Database()  # Database initialized
db2 = Database()  # No output
print(db1 is db2)  # True
```

### 9.6 Chaining Decorators

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())  # <b><i>Hello</i></b>
```

---

## 11. Object-Oriented Programming

### 11.1 Classes and Objects

**Basic Class Definition:**

```python
class Chai:
    pass

class ChaiTime:
    pass

# Check type
print(type(Chai))  # <class 'type'>

# Create instance
ginger_tea = Chai()
print(type(ginger_tea))  # <class '__main__.Chai'>
print(type(ginger_tea) is Chai)  # True
print(type(ginger_tea) is ChaiTime)  # False
```

### 10.2 Class Attributes and Methods

```python
class Chai:
    # Class attribute (shared by all instances)
    shop_name = "Chai Paradise"
    
    def __init__(self, name, price):
        # Instance attributes
        self.name = name
        self.price = price
    
    # Instance method
    def serve(self):
        return f"Serving {self.name} chai"
    
    # Instance method with parameters
    def apply_discount(self, discount_percent):
        self.price = self.price * (1 - discount_percent / 100)
        return self.price

# Create instances
masala_chai = Chai("Masala", 50)
ginger_chai = Chai("Ginger", 45)

print(masala_chai.serve())  # Serving Masala chai
print(Chai.shop_name)  # Chai Paradise
masala_chai.apply_discount(10)
print(masala_chai.price)  # 45.0
```

### 10.3 The __init__ Method

**Object Initialization:**

```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = []  # Default empty list
    
    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
    
    def introduce(self):
        hobbies_str = ", ".join(self.hobbies) if self.hobbies else "none"
        return f"Hi, I'm {self.name}, {self.age} years old from {self.city}. Hobbies: {hobbies_str}"

alice = Person("Alice", 30, "New York")
alice.add_hobby("Reading")
alice.add_hobby("Coding")
print(alice.introduce())
```

### 10.4 Inheritance

**Code Reusability:**

```python
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def info(self):
        return f"I am {self.name}"

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed
    
    def speak(self):  # Override parent method
        return "Woof!"
    
    def info(self):
        return f"{super().info()} and I'm a {self.breed}"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
print(dog.info())   # I am Buddy and I'm a Golden Retriever
```

### 10.5 Composition vs Inheritance

```python
# Composition - "has-a" relationship
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  # Composition
    
    def start(self):
        return f"{self.model}: {self.engine.start()}"

car = Car("Tesla", 450)
print(car.start())  # Tesla: Engine started

# When to use:
# Inheritance: "is-a" relationship (Dog is an Animal)
# Composition: "has-a" relationship (Car has an Engine)
```

### 10.6 Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B (follows MRO)
print(D.__mro__)   # Shows method resolution order
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

### 10.7 Static Methods and Class Methods

```python
class MathOperations:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't access instance or class"""
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        """Class method - has access to class attributes"""
        return cls.pi * radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor"""
        return cls.circle_area(diameter / 2)

# Usage
print(MathOperations.add(5, 3))          # 8
print(MathOperations.circle_area(5))     # 78.53975
print(MathOperations.from_diameter(10))  # 78.53975
```

### 10.8 Property Decorators

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Usage
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 86
print(temp.celsius)      # 30.0

# temp.celsius = -300  # Raises ValueError
```

### 10.9 Special Methods (Magic Methods)

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for users"""
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of the book"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Less than comparison (for sorting)"""
        return self.pages < other.pages

book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)

print(book1)           # Python Guide by John Doe
print(repr(book1))     # Book('Python Guide', 'John Doe', 300)
print(len(book1))      # 300
print(book1 == book2)  # False
print(book1 < book2)   # True
```

---

## 12. Exception Handling

### 12.1 Try-Except Blocks

**Handling Errors Gracefully:**

```python
# Basic exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 11.2 Multiple Exception Handling

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid type")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Execution completed")

divide_numbers(10, 2)
divide_numbers(10, 0)
```

### 11.3 Raising Exceptions

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
```

### 11.4 Custom Exceptions

```python
class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds: Balance ${balance}, attempted withdrawal ${amount}"
        super().__init__(message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)  # Insufficient funds: Balance $100, attempted withdrawal $150
```

### 11.5 Context Managers

```python
# File handling with context manager
with open('data.txt', 'w') as file:
    file.write("Hello, World!")
# File automatically closed

# Custom context manager
class DatabaseConnection:
    def __enter__(self):
        print("Opening database connection")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False  # Don't suppress exceptions
    
    def query(self, sql):
        print(f"Executing: {sql}")

# Usage
with DatabaseConnection() as db:
    db.query("SELECT * FROM users")
```

---

## 13. File I/O & Data Persistence

### 13.1 Reading Files

**Basic File Reading:**

```python
# Read entire file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Read first N lines
with open('data.txt', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()
```

### 13.2 Writing Files

```python
# Write mode (overwrites existing file)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Append mode (adds to existing file)
with open('output.txt', 'a') as file:
    file.write("Appended line\n")
```

### 13.3 File Modes

```python
# 'r'  - Read (default)
# 'w'  - Write (overwrites)
# 'a'  - Append
# 'x'  - Exclusive creation (fails if exists)
# 'b'  - Binary mode
# 't'  - Text mode (default)
# '+'  - Read and write

# Examples
with open('data.txt', 'r') as f:     # Read text
    pass

with open('image.jpg', 'rb') as f:   # Read binary
    pass

with open('data.txt', 'r+') as f:    # Read and write
    pass

with open('new.txt', 'x') as f:      # Create new (error if exists)
    pass
```

### 13.4 Working with CSV Files

```python
import csv

# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'San Francisco'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Using DictWriter
with open('people.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 30, 'City': 'New York'})
    writer.writerow({'Name': 'Bob', 'Age': 25, 'City': 'SF'})

# Using DictReader
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")
```

### 13.5 Working with JSON Files

```python
import json

# Write JSON
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding"],
    "active": True
}

# Write to file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Read from file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Pretty print JSON
print(json.dumps(data, indent=2, sort_keys=True))

# Write multiple JSON objects
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

with open('people.json', 'w') as file:
    json.dump(people, file, indent=2)
```

### 13.6 Binary Files

```python
# Writing binary data
data = bytes([65, 66, 67, 68, 69])  # ABCDE in ASCII

with open('data.bin', 'wb') as file:
    file.write(data)

# Reading binary data
with open('data.bin', 'rb') as file:
    binary_data = file.read()
    print(binary_data)  # b'ABCDE'

# Copy binary file (like images)
with open('source.jpg', 'rb') as source:
    with open('destination.jpg', 'wb') as dest:
        dest.write(source.read())
```

### 13.7 File and Directory Operations

```python
import os
import shutil
from pathlib import Path

# Check if file exists
if os.path.exists('data.txt'):
    print("File exists")

# Check if it's a file or directory
print(os.path.isfile('data.txt'))
print(os.path.isdir('my_folder'))

# Get file size
size = os.path.getsize('data.txt')
print(f"File size: {size} bytes")

# Create directory
os.makedirs('new_folder/subfolder', exist_ok=True)

# List directory contents
files = os.listdir('.')
for file in files:
    print(file)

# Walk through directory tree
for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))

# Copy file
shutil.copy('source.txt', 'destination.txt')

# Move/rename file
shutil.move('old_name.txt', 'new_name.txt')

# Delete file
os.remove('file_to_delete.txt')

# Delete directory
shutil.rmtree('folder_to_delete')
```

### 13.8 Using Pathlib (Modern Approach)

```python
from pathlib import Path

# Create Path object
path = Path('data/files/document.txt')

# Create parent directories
path.parent.mkdir(parents=True, exist_ok=True)

# Write to file
path.write_text("Hello, World!")

# Read from file
content = path.read_text()

# Check existence
if path.exists():
    print("File exists")

# Get file information
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")
print(f"Parent: {path.parent}")

# Iterate over directory
data_dir = Path('data')
for file in data_dir.glob('*.txt'):
    print(file)

# Recursive glob
for file in data_dir.rglob('*.py'):
    print(file)

# Join paths
new_path = Path('data') / 'files' / 'document.txt'
```

### 13.9 Temporary Files

```python
import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
    temp.write("Temporary data")
    temp_path = temp.name
    print(f"Temp file created at: {temp_path}")

# Create temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temp directory: {temp_dir}")
    # Directory and contents deleted automatically
```

### 13.10 File Handling with Exception Safety

```python
def process_order_file(filename):
    """Process chai orders from file with proper error handling"""
    try:
        with open(filename, 'r') as file:
            orders = []
            for line_num, line in enumerate(file, 1):
                try:
                    # Parse order: "chai_type,quantity,price"
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        raise ValueError(f"Invalid format at line {line_num}")
                    
                    chai_type, quantity, price = parts
                    orders.append({
                        'type': chai_type,
                        'quantity': int(quantity),
                        'price': float(price)
                    })
                except ValueError as e:
                    print(f"Error processing line {line_num}: {e}")
                    continue
            
            return orders
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Usage
orders = process_order_file('chai_orders.txt')
print(f"Processed {len(orders)} orders")
```

### 13.11 Working with Large Files

```python
# Reading large files efficiently
def process_large_file(filename):
    """Process large file line by line"""
    with open(filename, 'r') as file:
        for line in file:
            # Process one line at a time
            # Memory efficient - doesn't load entire file
            process_line(line.strip())

# Reading in chunks
def read_in_chunks(filename, chunk_size=1024):
    """Read file in chunks"""
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_in_chunks('large_file.bin'):
    process_chunk(chunk)
```

### 13.12 File Locking (Multi-process Safety)

```python
import fcntl  # Unix/Linux only

def write_with_lock(filename, data):
    """Write to file with exclusive lock"""
    with open(filename, 'a') as file:
        # Acquire exclusive lock
        fcntl.flock(file.fileno(), fcntl.LOCK_EX)
        try:
            file.write(data)
        finally:
            # Release lock
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
```

### 13.13 Practical Example: Log File Manager

```python
from datetime import datetime
from pathlib import Path

class LogManager:
    def __init__(self, log_file='app.log'):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def log(self, level, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        with open(self.log_file, 'a') as file:
            file.write(log_entry)
    
    def info(self, message):
        self.log('INFO', message)
    
    def error(self, message):
        self.log('ERROR', message)
    
    def warning(self, message):
        self.log('WARNING', message)
    
    def read_logs(self, level=None):
        """Read logs, optionally filter by level"""
        if not self.log_file.exists():
            return []
        
        logs = []
        with open(self.log_file, 'r') as file:
            for line in file:
                if level is None or f"] {level}:" in line:
                    logs.append(line.strip())
        return logs
    
    def clear_logs(self):
        """Clear all logs"""
        self.log_file.write_text("")

# Usage
logger = LogManager('logs/chai_shop.log')
logger.info("Chai shop opened")
logger.warning("Low stock on masala chai")
logger.error("Payment system down")

# Read all errors
errors = logger.read_logs(level='ERROR')
for error in errors:
    print(error)
```

---

## 14. Threading & Concurrency

### 14.1 Basic Threading

**Concurrent Execution:**

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

# Sequential execution
print("Sequential:")
print_numbers()
print_letters()

# Concurrent execution
print("\nConcurrent:")
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()  # Wait for thread1 to complete
thread2.join()  # Wait for thread2 to complete

print("Both threads completed")
```

### 12.2 Thread with Arguments

```python
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    time.sleep(1)

# Create threads with arguments
threads = []
users = ["Alice", "Bob", "Charlie"]

for user in users:
    thread = threading.Thread(target=greet_user, args=(user,), kwargs={"greeting": "Hi"})
    threads.append(thread)
    thread.start()

# Wait for all threads
for thread in threads:
    thread.join()
```

### 12.3 Daemon Threads

```python
def background_worker():
    while True:
        print("Working in background...")
        time.sleep(2)

# Daemon thread - terminates when main program exits
daemon_thread = threading.Thread(target=background_worker, daemon=True)
daemon_thread.start()

time.sleep(5)
print("Main program ending")
# Daemon thread will automatically terminate
```

### 12.4 Race Conditions

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

# Race condition - multiple threads accessing shared resource
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter: {counter}")  # May not be 200000 due to race condition
```

### 12.5 Thread Synchronization with Locks

```python
import threading

counter = 0
lock = threading.Lock()

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock:  # Acquire lock
            counter += 1
        # Lock automatically released

# No race condition - synchronized access
thread1 = threading.Thread(target=increment_with_lock)
thread2 = threading.Thread(target=increment_with_lock)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter: {counter}")  # Will be exactly 200000
```

### 12.6 Deadlock

```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        print("Task 1 acquired lock1")
        time.sleep(0.1)
        with lock2:
            print("Task 1 acquired lock2")

def task2():
    with lock2:
        print("Task 2 acquired lock2")
        time.sleep(0.1)
        with lock1:
            print("Task 2 acquired lock1")

# This can cause deadlock
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### 12.7 Thread-Safe Queue

```python
from queue import Queue
import threading
import time

def producer(queue, items):
    for item in items:
        print(f"Producing: {item}")
        queue.put(item)
        time.sleep(0.5)
    queue.put(None)  # Signal completion

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming: {item}")
        time.sleep(1)
        queue.task_done()

# Thread-safe queue
q = Queue()

producer_thread = threading.Thread(target=producer, args=(q, range(5)))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
```

---

### 14.7 GIL (Global Interpreter Lock)

**Understanding the GIL:**

The **Global Interpreter Lock (GIL)** is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This has important implications for multi-threaded programs.

**GIL with Threading (CPU-bound tasks):**

```python
import threading
import time

def brew_chai():
    """CPU-intensive task"""
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

# Threading with GIL
thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time with threading: {end - start:.2f} seconds")
# Result: ~10-12 seconds (NOT faster due to GIL!)
```

**GIL with Multiprocessing (CPU-bound tasks):**

```python
import multiprocessing
import time

def brew_chai(name):
    """CPU-intensive task"""
    print(f"{name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{name} finished brewing...")

# Multiprocessing bypasses GIL
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=brew_chai, args=("Barista-1",))
    process2 = multiprocessing.Process(target=brew_chai, args=("Barista-2",))
    
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    
    print(f"Total time with multiprocessing: {end - start:.2f} seconds")
    # Result: ~5-6 seconds (MUCH faster - true parallelism!)
```

**When GIL Matters:**

```python
# ❌ GIL impacts CPU-bound tasks with threading
import threading

def cpu_intensive():
    total = sum(i * i for i in range(10_000_000))
    return total

# Threading doesn't help here (GIL bottleneck)
threads = [threading.Thread(target=cpu_intensive) for _ in range(4)]
# Won't be faster than single-threaded

# ✅ GIL doesn't impact I/O-bound tasks with threading
import threading
import time

def io_intensive():
    time.sleep(2)  # Simulates I/O (network, disk, etc.)
    return "Done"

# Threading works great here!
threads = [threading.Thread(target=io_intensive) for _ in range(4)]
# Will complete in ~2 seconds instead of 8
```

**GIL Decision Chart:**

```python
"""
Task Type              | Best Choice         | Reason
-----------------------|---------------------|---------------------------
CPU-bound              | multiprocessing     | Bypasses GIL
I/O-bound (blocking)   | threading           | GIL released during I/O
I/O-bound (async)      | asyncio             | Lightweight, efficient
Mixed workload         | ProcessPoolExecutor | Combines benefits
"""
```

---

### 14.8 Advanced Multiprocessing

**Process Basics:**

```python
import multiprocessing
import os

def worker(name):
    """Simple worker process"""
    print(f"{name}: Process ID {os.getpid()}")
    print(f"{name}: Parent Process ID {os.getppid()}")

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(f"Worker-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

**Process Pool:**

```python
from multiprocessing import Pool
import time

def square(n):
    """Calculate square (simulates work)"""
    time.sleep(0.1)
    return n * n

if __name__ == '__main__':
    numbers = list(range(20))
    
    # Sequential
    start = time.time()
    results_seq = [square(n) for n in numbers]
    print(f"Sequential: {time.time() - start:.2f}s")
    
    # Parallel with Pool
    start = time.time()
    with Pool(processes=4) as pool:
        results_parallel = pool.map(square, numbers)
    print(f"Parallel: {time.time() - start:.2f}s")
    
    print(f"Results: {results_parallel}")
```

**Process Queue (Inter-process Communication):**

```python
from multiprocessing import Process, Queue

def producer(queue):
    """Produce items"""
    for i in range(5):
        item = f"Item-{i}"
        queue.put(item)
        print(f"Produced: {item}")
    queue.put(None)  # Signal completion

def consumer(queue):
    """Consume items"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")

if __name__ == '__main__':
    q = Queue()
    
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

**Shared Memory with Value and Array:**

```python
from multiprocessing import Process, Value, Array
import time

def increment_counter(counter, arr, index):
    """Increment shared counter and modify array"""
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1
    
    arr[index] = counter.value

if __name__ == '__main__':
    # Shared value
    counter = Value('i', 0)  # 'i' = integer
    
    # Shared array
    arr = Array('i', [0, 0, 0, 0])
    
    processes = []
    for i in range(4):
        p = Process(target=increment_counter, args=(counter, arr, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Final counter value: {counter.value}")
    print(f"Array values: {list(arr)}")
```

**Process Pool with map, starmap, and apply_async:**

```python
from multiprocessing import Pool

def add(a, b):
    return a + b

def power(base, exp):
    return base ** exp

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        # map: single argument
        results = pool.map(lambda x: x**2, [1, 2, 3, 4, 5])
        print(f"map results: {results}")
        
        # starmap: multiple arguments
        args = [(2, 3), (3, 4), (4, 5)]
        results = pool.starmap(power, args)
        print(f"starmap results: {results}")
        
        # apply_async: asynchronous execution
        result = pool.apply_async(add, (5, 3))
        print(f"apply_async result: {result.get()}")
        
        # Multiple async tasks
        results = []
        for i in range(5):
            result = pool.apply_async(lambda x: x**2, (i,))
            results.append(result)
        
        # Get all results
        final_results = [r.get() for r in results]
        print(f"Multiple async results: {final_results}")
```

**ProcessPoolExecutor (Modern Approach):**

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def process_task(n):
    """Simulate heavy processing"""
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    numbers = list(range(10))
    
    # Using ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as executor:
        # Submit tasks
        futures = [executor.submit(process_task, n) for n in numbers]
        
        # Process results as they complete
        for future in as_completed(futures):
            result = future.result()
            print(f"Result: {result}")
    
    # Using map (simpler for simple cases)
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_task, numbers))
        print(f"All results: {results}")
```

**Practical Example: Parallel Data Processing:**

```python
from multiprocessing import Pool
import time

def process_chunk(data_chunk):
    """Process a chunk of data"""
    # Simulate data processing
    processed = [x * 2 for x in data_chunk]
    time.sleep(0.1)  # Simulate processing time
    return sum(processed)

def parallel_data_processing(data, num_processes=4):
    """Split data and process in parallel"""
    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    return sum(results)

if __name__ == '__main__':
    # Large dataset
    large_data = list(range(1000))
    
    # Sequential processing
    start = time.time()
    seq_result = sum(process_chunk(large_data))
    print(f"Sequential: {time.time() - start:.2f}s, Result: {seq_result}")
    
    # Parallel processing
    start = time.time()
    par_result = parallel_data_processing(large_data, num_processes=4)
    print(f"Parallel: {time.time() - start:.2f}s, Result: {par_result}")
```

**Best Practices:**

```python
# ✅ Always use if __name__ == '__main__':
if __name__ == '__main__':
    # Multiprocessing code here
    pass

# ✅ Use Pool for many similar tasks
with Pool(processes=4) as pool:
    results = pool.map(func, data)

# ✅ Use Queue for inter-process communication
from multiprocessing import Queue
q = Queue()

# ✅ Use Value/Array for shared state
from multiprocessing import Value
counter = Value('i', 0)

# ❌ Avoid sharing complex objects (use Manager instead)
from multiprocessing import Manager
manager = Manager()
shared_dict = manager.dict()
```

---

## 15. Async Programming

### 15.1 Basic Async/Await

**Asynchronous Execution:**

```python
import asyncio

async def brew_chai(name):
    print(f"Start brewing {name}")
    await asyncio.sleep(2)  # Simulate brewing time
    print(f"{name} is ready!")
    return f"Cup of {name}"

async def main():
    # Sequential execution
    result1 = await brew_chai("Masala Chai")
    result2 = await brew_chai("Ginger Chai")
    print(result1, result2)

# Run async function
asyncio.run(main())
```

### 13.2 Concurrent Async Tasks

```python
import asyncio

async def brew_chai(name):
    print(f"Start brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} is ready!")
    return f"Cup of {name}"

async def main():
    # Concurrent execution with gather
    results = await asyncio.gather(
        brew_chai("Masala Chai"),
        brew_chai("Ginger Chai"),
        brew_chai("Elaichi Chai")
    )
    print(results)

asyncio.run(main())
```

### 13.3 Async with Tasks

```python
import asyncio

async def brew_chai(name, brewing_time):
    print(f"Start brewing {name}")
    await asyncio.sleep(brewing_time)
    print(f"{name} is ready!")
    return f"Cup of {name}"

async def main():
    # Create tasks
    task1 = asyncio.create_task(brew_chai("Masala Chai", 3))
    task2 = asyncio.create_task(brew_chai("Ginger Chai", 2))
    task3 = asyncio.create_task(brew_chai("Elaichi Chai", 1))
    
    # Do other work while tasks run
    print("Tasks created, doing other work...")
    await asyncio.sleep(0.5)
    print("Still doing work...")
    
    # Wait for tasks to complete
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(f"Results: {result1}, {result2}, {result3}")

asyncio.run(main())
```

### 13.4 Async Context Managers

```python
import asyncio

class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Opening async database connection")
        await asyncio.sleep(1)  # Simulate connection time
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing async database connection")
        await asyncio.sleep(0.5)  # Simulate cleanup
        return False
    
    async def query(self, sql):
        print(f"Executing: {sql}")
        await asyncio.sleep(1)
        return f"Results for: {sql}"

async def main():
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

asyncio.run(main())
```

### 13.5 Async Iteration

```python
import asyncio

class AsyncRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(0.5)  # Simulate async operation
        value = self.current
        self.current += 1
        return value

async def main():
    async for number in AsyncRange(1, 5):
        print(f"Number: {number}")

asyncio.run(main())
```

### 13.6 Threading vs Async

```python
# Threading - for I/O-bound tasks with blocking operations
import threading
import time

def blocking_io():
    time.sleep(2)  # Blocking operation
    return "Done"

threads = [threading.Thread(target=blocking_io) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Async - for I/O-bound tasks with async operations
import asyncio

async def async_io():
    await asyncio.sleep(2)  # Non-blocking operation
    return "Done"

async def main():
    await asyncio.gather(*[async_io() for _ in range(3)])

asyncio.run(main())

# When to use:
# Threading: CPU-bound tasks, blocking I/O, legacy libraries
# Async: I/O-bound tasks, many concurrent operations, modern libraries
```

### 13.7 Process vs Thread

```python
import multiprocessing
import threading
import time

def cpu_bound_task():
    # Simulate CPU-intensive work
    total = sum(i * i for i in range(10000000))
    return total

# Using threads (not efficient for CPU-bound)
start = time.time()
threads = [threading.Thread(target=cpu_bound_task) for _ in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"Threading time: {time.time() - start:.2f}s")

# Using processes (efficient for CPU-bound)
start = time.time()
processes = [multiprocessing.Process(target=cpu_bound_task) for _ in range(4)]
for process in processes:
    process.start()
for process in processes:
    process.join()
print(f"Multiprocessing time: {time.time() - start:.2f}s")

# Use processes for CPU-bound tasks
# Use threads/async for I/O-bound tasks
```

---

## 16. Pydantic & Data Validation

### 16.1 Basic Pydantic Models

**Type Validation and Data Classes:**

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)

# Create instance
user = User(id=1, name="Alice", email="alice@example.com", age=30)
print(user)
# id=1 name='Alice' email='alice@example.com' age=30 created_at=datetime(...)

# Type validation
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except Exception as e:
    print(f"Validation error: {e}")
```

### 16.2 Field Validation

```python
from pydantic import BaseModel, Field, validator, EmailStr

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0, le=1000000)
    quantity: int = Field(default=0, ge=0)
    tags: List[str] = Field(default_factory=list)
    
    @validator('name')
    def name_must_not_contain_special_chars(cls, v):
        if not v.replace(' ', '').isalnum():
            raise ValueError('Name must contain only alphanumeric characters')
        return v.title()
    
    @validator('price')
    def price_must_be_reasonable(cls, v):
        if v > 100000:
            raise ValueError('Price seems unreasonably high')
        return round(v, 2)

# Valid product
product = Product(name="laptop", price=999.999, quantity=10)
print(product)
# name='Laptop' price=1000.0 quantity=10 tags=[]

# Invalid product
try:
    invalid = Product(name="$pecial", price=-10)
except Exception as e:
    print(f"Validation error: {e}")
```

### 16.3 Nested Models

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    country: str
    zipcode: str

class Person(BaseModel):
    name: str
    age: int
    addresses: List[Address]

# Create nested model
person = Person(
    name="Alice",
    age=30,
    addresses=[
        {"street": "123 Main St", "city": "New York", "country": "USA", "zipcode": "10001"},
        {"street": "456 Oak Ave", "city": "Boston", "country": "USA", "zipcode": "02101"}
    ]
)

print(person.json(indent=2))
```

### 16.4 Config and Advanced Features

```python
from pydantic import BaseModel, Field
from datetime import datetime

class Article(BaseModel):
    title: str
    content: str
    published: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    tags: List[str] = []
    
    class Config:
        # Allow arbitrary types
        arbitrary_types_allowed = True
        # Validate on assignment
        validate_assignment = True
        # Use enum values
        use_enum_values = True
        # JSON encoders
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

article = Article(
    title="Python Pydantic Guide",
    content="Learn Pydantic for data validation",
    tags=["python", "pydantic"]
)

# Export to dict/JSON
print(article.dict())
print(article.json())

# Update with validation
article.published = True  # Validates on assignment
```

### 16.5 Advanced Pydantic Features

#### Computed Fields
```python
from pydantic import BaseModel, computed_field
from typing import Optional

class ChaiOrder(BaseModel):
    chai_type: str
    quantity: int
    price_per_cup: float
    discount_percent: Optional[float] = 0.0
    
    @computed_field
    @property
    def subtotal(self) -> float:
        """Calculate subtotal before discount"""
        return self.quantity * self.price_per_cup
    
    @computed_field
    @property
    def discount_amount(self) -> float:
        """Calculate discount amount"""
        return self.subtotal * (self.discount_percent / 100)
    
    @computed_field
    @property
    def total(self) -> float:
        """Calculate final total after discount"""
        return self.subtotal - self.discount_amount

# Usage
order = ChaiOrder(
    chai_type="Masala Chai",
    quantity=5,
    price_per_cup=50.0,
    discount_percent=10.0
)

print(f"Subtotal: ₹{order.subtotal}")
print(f"Discount: ₹{order.discount_amount}")
print(f"Total: ₹{order.total}")
```

#### Model Serialization
```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class ChaiShopStats(BaseModel):
    shop_name: str = Field(..., description="Name of the chai shop")
    location: str
    opening_time: datetime
    daily_sales: List[float]
    rating: Optional[float] = None
    
    class Config:
        # Customize JSON serialization
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create instance
stats = ChaiShopStats(
    shop_name="Chai Paradise",
    location="Mumbai",
    opening_time=datetime(2024, 1, 1, 8, 0),
    daily_sales=[5000.0, 6000.0, 5500.0],
    rating=4.5
)

# Export to dict (for Python usage)
dict_data = stats.model_dump()
print("Dict format:", dict_data)

# Export to JSON string (for API/storage)
json_data = stats.model_dump_json(indent=2)
print("JSON format:", json_data)

# Export with exclusions
json_without_rating = stats.model_dump_json(exclude={'rating'})
print("Without rating:", json_without_rating)

# Export only specific fields
json_minimal = stats.model_dump_json(include={'shop_name', 'location'})
print("Minimal:", json_minimal)
```

#### Self-Referencing Models
```python
from pydantic import BaseModel
from typing import Optional, List

class ChaiCategory(BaseModel):
    name: str
    description: str
    parent: Optional['ChaiCategory'] = None
    subcategories: List['ChaiCategory'] = []
    
# Must call model_rebuild() for self-referencing models
ChaiCategory.model_rebuild()

# Create hierarchical structure
hot_beverages = ChaiCategory(
    name="Hot Beverages",
    description="All hot drinks"
)

chai_category = ChaiCategory(
    name="Chai Varieties",
    description="Different types of chai",
    parent=hot_beverages
)

masala_chai = ChaiCategory(
    name="Masala Chai",
    description="Spiced tea with milk",
    parent=chai_category
)

# Build hierarchy
chai_category.subcategories = [masala_chai]
hot_beverages.subcategories = [chai_category]

print(hot_beverages.model_dump_json(indent=2))
```

#### Advanced Validators
```python
from pydantic import BaseModel, field_validator, model_validator
from typing import List

class ChaiRecipe(BaseModel):
    name: str
    ingredients: List[str]
    preparation_time: int  # in minutes
    serving_size: int
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError('Recipe name must be at least 3 characters')
        if not v[0].isupper():
            raise ValueError('Recipe name must start with capital letter')
        return v
    
    @field_validator('ingredients')
    @classmethod
    def validate_ingredients(cls, v):
        if len(v) < 2:
            raise ValueError('Recipe must have at least 2 ingredients')
        # Check for duplicates
        if len(v) != len(set(v)):
            raise ValueError('Duplicate ingredients not allowed')
        return v
    
    @model_validator(mode='after')
    def validate_recipe(self):
        # Cross-field validation
        if self.preparation_time > 60 and self.serving_size < 4:
            raise ValueError('Long preparation time should serve more people')
        return self

# Valid recipe
recipe = ChaiRecipe(
    name="Classic Masala Chai",
    ingredients=["Tea leaves", "Milk", "Ginger", "Cardamom", "Sugar"],
    preparation_time=15,
    serving_size=4
)
print(recipe.model_dump())

# Invalid examples
try:
    bad_recipe = ChaiRecipe(
        name="Chai",  # Too short
        ingredients=["Tea"],  # Too few
        preparation_time=90,
        serving_size=1
    )
except Exception as e:
    print(f"Validation error: {e}")
```

---

## 17. Mini Projects & Real-World Applications

### 17.1 Chai Shop Inventory Manager

```python
from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
import json

@dataclass
class ChaiItem:
    name: str
    quantity: int
    price: float
    last_restocked: datetime
    
    def needs_restock(self, threshold: int = 10) -> bool:
        return self.quantity < threshold

class InventoryManager:
    def __init__(self):
        self.inventory: Dict[str, ChaiItem] = {}
    
    def add_item(self, name: str, quantity: int, price: float):
        """Add or update inventory item"""
        if name in self.inventory:
            self.inventory[name].quantity += quantity
            self.inventory[name].last_restocked = datetime.now()
        else:
            self.inventory[name] = ChaiItem(
                name=name,
                quantity=quantity,
                price=price,
                last_restocked=datetime.now()
            )
    
    def sell_item(self, name: str, quantity: int) -> bool:
        """Process sale and update inventory"""
        if name not in self.inventory:
            print(f"Item '{name}' not found in inventory")
            return False
        
        if self.inventory[name].quantity < quantity:
            print(f"Insufficient stock for '{name}'")
            return False
        
        self.inventory[name].quantity -= quantity
        return True
    
    def get_restock_list(self) -> List[str]:
        """Get list of items that need restocking"""
        return [
            item.name 
            for item in self.inventory.values() 
            if item.needs_restock()
        ]
    
    def get_total_value(self) -> float:
        """Calculate total inventory value"""
        return sum(
            item.quantity * item.price 
            for item in self.inventory.values()
        )
    
    def generate_report(self) -> str:
        """Generate inventory report"""
        report = ["=== Chai Shop Inventory Report ===\n"]
        report.append(f"Total Items: {len(self.inventory)}\n")
        report.append(f"Total Value: ₹{self.get_total_value():.2f}\n")
        report.append("\nItems needing restock:")
        
        restock_items = self.get_restock_list()
        if restock_items:
            for item in restock_items:
                report.append(f"  - {item}")
        else:
            report.append("  None")
        
        return "\n".join(report)

# Usage Example
manager = InventoryManager()

# Add initial inventory
manager.add_item("Tea Leaves", 50, 200.0)
manager.add_item("Milk", 30, 60.0)
manager.add_item("Sugar", 25, 40.0)
manager.add_item("Cardamom", 8, 500.0)  # Low stock
manager.add_item("Ginger", 15, 80.0)

# Process some sales
manager.sell_item("Tea Leaves", 10)
manager.sell_item("Milk", 5)
manager.sell_item("Cardamom", 3)

# Generate report
print(manager.generate_report())
```

### 17.2 Data Processing Pipeline

```python
from typing import Callable, List, Any
from functools import reduce

class DataPipeline:
    """Functional programming approach to data transformation"""
    
    def __init__(self, data: List[Any]):
        self.data = data
    
    def map(self, func: Callable) -> 'DataPipeline':
        """Transform each element"""
        self.data = list(map(func, self.data))
        return self
    
    def filter(self, predicate: Callable) -> 'DataPipeline':
        """Filter elements based on condition"""
        self.data = list(filter(predicate, self.data))
        return self
    
    def reduce(self, func: Callable, initial=None):
        """Reduce to single value"""
        if initial is None:
            return reduce(func, self.data)
        return reduce(func, self.data, initial)
    
    def sort(self, key: Callable = None, reverse: bool = False) -> 'DataPipeline':
        """Sort the data"""
        self.data = sorted(self.data, key=key, reverse=reverse)
        return self
    
    def get(self) -> List[Any]:
        """Get final result"""
        return self.data

# Example: Process chai sales data
sales_data = [
    {"item": "Masala Chai", "quantity": 45, "price": 50},
    {"item": "Ginger Chai", "quantity": 30, "price": 55},
    {"item": "Cardamom Chai", "quantity": 25, "price": 60},
    {"item": "Plain Chai", "quantity": 60, "price": 40},
    {"item": "Kulhad Chai", "quantity": 20, "price": 45},
]

# Process pipeline
result = (DataPipeline(sales_data)
    .filter(lambda x: x['quantity'] > 25)  # High sales items
    .map(lambda x: {**x, 'revenue': x['quantity'] * x['price']})  # Add revenue
    .sort(key=lambda x: x['revenue'], reverse=True)  # Sort by revenue
    .get())

print("Top selling chai items by revenue:")
for item in result:
    print(f"{item['item']}: ₹{item['revenue']} ({item['quantity']} cups)")

# Calculate total revenue
total_revenue = (DataPipeline(sales_data)
    .map(lambda x: x['quantity'] * x['price'])
    .reduce(lambda a, b: a + b))

print(f"\nTotal Revenue: ₹{total_revenue}")
```

### 17.3 Custom Logger with Context

```python
import logging
from datetime import datetime
from contextlib import contextmanager
from typing import Optional
import sys

class ChaiShopLogger:
    """Custom logger for chai shop operations"""
    
    def __init__(self, name: str, log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
        # File handler (if specified)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_format = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'
            )
            file_handler.setFormatter(file_format)
            self.logger.addHandler(file_handler)
    
    @contextmanager
    def operation(self, operation_name: str):
        """Context manager for tracking operations"""
        start_time = datetime.now()
        self.logger.info(f"Starting: {operation_name}")
        
        try:
            yield
            duration = (datetime.now() - start_time).total_seconds()
            self.logger.info(f"Completed: {operation_name} (took {duration:.2f}s)")
        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            self.logger.error(
                f"Failed: {operation_name} after {duration:.2f}s - Error: {str(e)}"
            )
            raise
    
    def log_sale(self, item: str, quantity: int, amount: float):
        """Log a sale transaction"""
        self.logger.info(f"SALE: {quantity}x {item} = ₹{amount:.2f}")
    
    def log_restock(self, item: str, quantity: int):
        """Log inventory restock"""
        self.logger.info(f"RESTOCK: Added {quantity} units of {item}")

# Usage Example
logger = ChaiShopLogger("ChaiShop", "chai_shop.log")

with logger.operation("Morning Sales"):
    logger.log_sale("Masala Chai", 5, 250.0)
    logger.log_sale("Ginger Chai", 3, 165.0)
    
with logger.operation("Inventory Restock"):
    logger.log_restock("Tea Leaves", 100)
    logger.log_restock("Milk", 50)

# Simulate error
try:
    with logger.operation("Invalid Operation"):
        raise ValueError("Insufficient funds")
except ValueError:
    pass
```

### 17.4 Simple Web Scraper (Concept)

```python
from typing import List, Dict
import re
from dataclasses import dataclass

@dataclass
class ChaiRecipeData:
    name: str
    ingredients: List[str]
    instructions: List[str]
    prep_time: int

class RecipeParser:
    """Parse chai recipe data from text"""
    
    @staticmethod
    def extract_ingredients(text: str) -> List[str]:
        """Extract ingredients from text"""
        # Simple pattern matching
        lines = text.split('\n')
        ingredients = []
        
        for line in lines:
            # Look for lines with measurements or ingredient keywords
            if any(word in line.lower() for word in ['cup', 'tsp', 'tbsp', 'ml', 'gram']):
                ingredients.append(line.strip())
        
        return ingredients
    
    @staticmethod
    def extract_time(text: str) -> int:
        """Extract preparation time in minutes"""
        # Match patterns like "15 minutes", "1 hour", etc.
        time_pattern = r'(\d+)\s*(minute|min|hour|hr)'
        matches = re.findall(time_pattern, text.lower())
        
        total_minutes = 0
        for value, unit in matches:
            if unit in ['hour', 'hr']:
                total_minutes += int(value) * 60
            else:
                total_minutes += int(value)
        
        return total_minutes
    
    @staticmethod
    def parse_recipe(text: str, recipe_name: str) -> ChaiRecipeData:
        """Parse complete recipe from text"""
        ingredients = RecipeParser.extract_ingredients(text)
        prep_time = RecipeParser.extract_time(text)
        
        # Extract instructions (lines starting with numbers)
        instruction_pattern = r'^\d+\.\s*(.+)$'
        instructions = []
        for line in text.split('\n'):
            match = re.match(instruction_pattern, line.strip())
            if match:
                instructions.append(match.group(1))
        
        return ChaiRecipeData(
            name=recipe_name,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )

# Example Usage
sample_recipe = """
Masala Chai Recipe

Ingredients:
- 2 cups water
- 1 cup milk
- 2 tsp tea leaves
- 1 tsp grated ginger
- 4-5 cardamom pods
- 2 tsp sugar

Preparation Time: 15 minutes

Instructions:
1. Boil water with ginger and cardamom
2. Add tea leaves and simmer for 3 minutes
3. Add milk and bring to boil
4. Add sugar and strain
5. Serve hot
"""

recipe = RecipeParser.parse_recipe(sample_recipe, "Masala Chai")
print(f"Recipe: {recipe.name}")
print(f"Prep Time: {recipe.prep_time} minutes")
print(f"Ingredients: {len(recipe.ingredients)} items")
print(f"Steps: {len(recipe.instructions)}")
```

---

## 📖 Practice Challenges

### Challenge 1: List Processing
Create a function that takes a list of numbers and returns:
- Sum of even numbers
- Product of odd numbers
- Count of zeros

### Challenge 2: String Manipulation
Write a program that:
- Reverses words in a sentence
- Counts vowels and consonants
- Converts to title case

### Challenge 3: File Processing
Create a program that:
- Reads a CSV file
- Filters data based on criteria
- Writes results to new file

### Challenge 4: API Client
Build an async API client that:
- Fetches data from multiple endpoints concurrently
- Handles errors gracefully
- Validates response data with Pydantic

### Challenge 5: Class Design
Design a library management system with:
- Book class with properties
- Library class with inventory management
- Member class with borrowing history
- Exception handling for edge cases

---

## 🎯 Best Practices Summary

### 1. **Code Organization**
- Follow PEP 8 style guide
- Use meaningful variable names
- Keep functions small and focused
- Add docstrings to functions and classes

### 2. **Error Handling**
- Use try-except blocks appropriately
- Create custom exceptions for domain-specific errors
- Always clean up resources (use context managers)

### 3. **Performance**
- Use generators for large datasets
- Leverage list comprehensions for readability
- Use appropriate data structures (set for membership tests, dict for lookups)

### 4. **Concurrency**
- Use async for I/O-bound tasks
- Use multiprocessing for CPU-bound tasks
- Always protect shared resources with locks

### 5. **Type Hints**
- Use type hints for better code documentation
- Use Pydantic for runtime validation
- Leverage IDE autocomplete features

---

## 🚀 Next Steps

1. **Practice Regularly**: Solve coding challenges on platforms like LeetCode, HackerRank
2. **Build Projects**: Apply concepts in real-world projects
3. **Read Documentation**: Explore official Python documentation
4. **Contribute to Open Source**: Learn from production code
5. **Stay Updated**: Follow Python Enhancement Proposals (PEPs)

---

## 📚 Additional Resources

- **Official Python Documentation**: https://docs.python.org/3/
- **Python Package Index (PyPI)**: https://pypi.org/
- **Real Python**: https://realpython.com/
- **Python Weekly**: https://www.pythonweekly.com/
- **PEP 8 Style Guide**: https://pep8.org/

---

**Happy Learning! 🎉**

*This guide covers fundamental to advanced Python concepts with practical examples. Practice each concept, build projects, and keep coding!*
