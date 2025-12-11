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
16. [Asynchronous Programming](#16-asynchronous-programming) ⭐
17. [REST APIs & FastAPI](#17-rest-apis--fastapi) ⭐
18. [Database Operations](#18-database-operations) ⭐
19. [Testing](#19-testing) ⭐
20. [Type Hints & Static Type Checking](#20-type-hints--static-type-checking) ⭐
21. [Python Interview Topics](#21-python-interview-topics) ⭐
22. [Exception Handling & Error Management](#22-exception-handling--error-management) 🔥 NEW
23. [Regular Expressions (Regex)](#23-regular-expressions-regex) 🔥 NEW
24. [Virtual Environments & Package Management](#24-virtual-environments--package-management) 🔥 NEW
25. [Logging & Monitoring](#25-logging--monitoring) 🔥 NEW
26. [Authentication & Security](#26-authentication--security) 🔥 NEW
27. [Docker & Deployment](#27-docker--deployment) 🔥 NEW
28. [Design Patterns](#28-design-patterns) 🔥 NEW
29. [Caching & Performance Optimization](#29-caching--performance-optimization) 🔥 NEW

---

## 1. Python Fundamentals

### Variables and Data Types

Python is dynamically typed, meaning you don't need to declare variable types explicitly. Python supports several built-in data types including integers (whole numbers), floats (decimal numbers), strings (text), booleans (True/False), and None (represents absence of value). Understanding these fundamental types is crucial as they form the building blocks of all Python programs.

```python
# Basic data types
integer_var = 42
float_var = 3.14159
string_var = "Hello, Python!"
boolean_var = True
none_var = None

# Type checking
print(type(integer_var))            # <class 'int'>
print(isinstance(string_var, str))  # True
```

### Type Conversions

Type conversion (also called type casting) allows you to convert data from one type to another. Python provides built-in functions like `int()`, `float()`, `str()`, and `bool()` for explicit type conversion. Understanding type conversion is essential when working with user input, file operations, or when performing operations that require specific data types.

```python
# String to number
age = int("25")            # 25
price = float("99.99")     # 99.99

# Number to string
count_str = str(100)       # "100"

# Boolean conversions
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False (empty string is falsy)
print(bool("hi")) # True (non-empty string is truthy)
```

### String Operations

Strings in Python are immutable sequences of characters. Python provides numerous built-in string methods for manipulation, searching, and formatting. Common operations include changing case, splitting/joining, searching for substrings, and replacing text. These methods are essential for text processing and data cleaning tasks.

```python
text = "Python Programming"

# Basic operations
print(f"Length: {len(text)}")           # Length: 18
print(f"Upper: {text.upper()}")         # Upper: PYTHON PROGRAMMING
print(f"Lower: {text.lower()}")         # Lower: python programming
print(f"Split: {text.split()}")         # Split: ['Python', 'Programming']

# String methods
print(text.startswith("Python"))  # True
print(text.endswith("ing"))       # True
print(text.find("Program"))       # 7 (index where "Program" starts)
print(text.replace("Python", "Advanced Python"))  # "Advanced Python Programming"
```

### String Formatting

String formatting allows you to create dynamic strings by inserting variables and expressions into text templates. Python offers three main approaches: f-strings (most modern and readable), the `format()` method, and the older % formatting. F-strings are the recommended approach in modern Python as they are more concise and readable.

```python
name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"Hello, {name}! You are {age} years old."  # "Hello, Alice! You are 30 years old."

# format() method
message = "Hello, {}! You are {} years old.".format(name, age)  # "Hello, Alice! You are 30 years old."

# % formatting (older style)
message = "Hello, %s! You are %d years old." % (name, age)  # "Hello, Alice! You are 30 years old."
```

---

## 2. Data Structures

### Lists - Ordered, Mutable Collections

Lists are Python's most versatile data structure, storing ordered sequences of items that can be of different types. Unlike strings, lists are mutable, meaning you can modify their contents after creation. Lists support indexing, slicing, and numerous methods for adding, removing, and sorting elements, making them ideal for storing collections of data.

```python
# List creation and operations
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Accessing elements
first_fruit = fruits[0]      # "apple"
last_fruit = fruits[-1]      # "cherry"
subset = fruits[1:3]         # ["banana", "cherry"]

# List methods
fruits.append("date")        # fruits = ["apple", "banana", "cherry", "date"]
fruits.insert(1, "orange")   # fruits = ["apple", "orange", "banana", "cherry", "date"]
removed = fruits.pop()       # removed = "date", fruits = ["apple", "orange", "banana", "cherry"]
fruits.remove("banana")      # fruits = ["apple", "orange", "cherry"]
fruits.sort()                # fruits = ["apple", "cherry", "orange"]
```

### List Comprehensions

List comprehensions provide a concise way to create lists based on existing sequences or ranges. They combine the functionality of loops and conditional statements into a single, readable line of code. List comprehensions are more efficient and Pythonic than traditional for-loops for creating lists, and can include conditions and nested iterations.

```python
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]  # [[1,2,3], [2,4,6], [3,6,9]]
```

### Tuples - Ordered, Immutable Collections

Tuples are ordered collections similar to lists, but they are immutable (cannot be modified after creation). This immutability makes tuples hashable and suitable for use as dictionary keys or set elements. Tuples are commonly used to store related data (like coordinates), return multiple values from functions, and ensure data integrity by preventing accidental modifications.

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

Dictionaries are unordered collections that store data in key-value pairs, providing fast lookups by key. Each key must be unique and immutable (strings, numbers, or tuples), while values can be any data type. Dictionaries are ideal for storing structured data like user profiles, configuration settings, or creating lookup tables, offering O(1) average time complexity for access operations.

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
keys = person.keys()      # dict_keys(['name', 'age', 'city'])
values = person.values()  # dict_values(['Alice', 30, 'New York'])
items = person.items()    # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Adding/updating
person["email"] = "alice@example.com"           # Add new key-value pair
person.update({"phone": "123-456-7890"})        # Add/update multiple items
```

### Dictionary Comprehensions

Dictionary comprehensions provide a concise syntax for creating dictionaries, similar to list comprehensions. They allow you to build dictionaries from iterables or transform existing dictionaries in a single, readable expression. This feature is useful for data transformation, filtering, and creating mappings efficiently.

```python
# Basic dict comprehension
squares_dict = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}  # {'a': 1, 'b': 2, 'c': 3}
```

### Sets - Unique Collections

Sets are unordered collections of unique elements, automatically removing duplicates. They support mathematical set operations like union, intersection, and difference, making them perfect for membership testing and eliminating duplicates. Sets offer O(1) average time complexity for add, remove, and membership tests, making them highly efficient for checking if an item exists in a collection.

```python
# Set creation
numbers = {1, 2, 3, 4, 5}
unique_chars = set("hello")  # {'h', 'e', 'l', 'o'}

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2          # {1, 2, 3, 4, 5, 6} - all elements from both sets
intersection = set1 & set2   # {3, 4} - common elements
difference = set1 - set2     # {1, 2} - elements in set1 but not set2
symmetric_diff = set1 ^ set2 # {1, 2, 5, 6} - elements in either set but not both
```

---

## 3. Control Flow

### Conditional Statements

Conditional statements allow your program to make decisions and execute different code blocks based on conditions. Python uses `if`, `elif` (else if), and `else` keywords to create branches in your code logic. The ternary operator provides a concise way to write simple if-else statements in a single line, useful for assignments and return statements.

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
status = "pass" if score >= 60 else "fail"  # status = "pass" (since 85 >= 60)

# Multiple conditions
if score >= 80 and score < 90:
    print("Good job!")  # This will execute since 80 <= 85 < 90
```

### Loops

Loops allow you to execute code repeatedly, either a fixed number of times (for loops) or while a condition is true (while loops). For loops are ideal for iterating over sequences like lists, strings, or ranges, while while loops continue until a condition becomes false. Python provides `break` to exit loops early and `continue` to skip to the next iteration, giving you fine control over loop execution.

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

Python provides powerful iteration tools beyond basic loops. The `zip()` function combines multiple iterables for parallel iteration, perfect for processing related data together. Nested loops allow you to work with multi-dimensional data structures. The loop-else construct is a unique Python feature where the else block executes only if the loop completes without encountering a break statement, useful for search operations.

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

Functions are reusable blocks of code that perform specific tasks, defined using the `def` keyword. They can accept input parameters and return output values, promoting code reusability and organization. Functions should have descriptive names and docstrings explaining their purpose, helping maintain clean, readable, and maintainable code.

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

# Function calls
message = greet("Alice")    # "Hello, Alice!"
result = add_numbers(5, 3)  # 8
```

### Function Parameters

Python functions support flexible parameter handling including default values, keyword arguments, and variable-length arguments. Default parameters provide fallback values when arguments aren't supplied. `*args` collects any number of positional arguments into a tuple, while `**kwargs` collects keyword arguments into a dictionary, making functions highly adaptable to different calling scenarios.

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

Lambda functions are anonymous, single-expression functions defined using the `lambda` keyword, ideal for short operations. They're commonly used with functions like `map()`, `filter()`, and `sorted()` when you need a simple function for a brief operation. While concise, lambdas should be used judiciously—for complex logic, regular functions are more readable and maintainable.

```python
# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))          # [1, 4, 9, 16, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### Higher-Order Functions

Higher-order functions are functions that either accept other functions as arguments or return functions as results, enabling powerful functional programming patterns. They promote code reusability and abstraction by treating functions as first-class objects. Common examples include decorators, closures, and functions like `map()`, `filter()`, and `reduce()` that transform data using custom operations.

```python
def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list."""
    return [operation(num) for num in numbers]

# Using with lambda
doubled = apply_operation([1, 2, 3, 4], lambda x: x * 2)  # [2, 4, 6, 8]

# Function as return value
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)  # Returns a function that doubles
triple = create_multiplier(3)  # Returns a function that triples
print(double(5))   # 10
print(triple(5))   # 15
```

---

## 5. Object-Oriented Programming

### Basic Classes

Object-Oriented Programming (OOP) organizes code into classes that bundle data (attributes) and behavior (methods) together. Classes serve as blueprints for creating objects (instances), enabling code reusability and logical organization. The `__init__` method is a constructor that initializes object attributes when an instance is created, while instance methods operate on individual objects.

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
person1.have_birthday()     # Increments age
print(person1.age)          # 26
```

### Inheritance

Inheritance allows classes to inherit attributes and methods from parent classes, promoting code reuse and establishing hierarchical relationships. Child classes can override parent methods to provide specialized behavior while maintaining the base interface. This enables polymorphism, where different objects can be treated uniformly through their common parent class interface.

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

Special methods (also called dunder methods, from "double underscore") customize how objects behave with built-in Python operations. Methods like `__str__` and `__repr__` control string representation, `__len__` enables the `len()` function, and `__eq__` defines equality comparison. These methods allow your custom classes to integrate seamlessly with Python's syntax and built-in functions.

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
print(str(book))    # "1984 by George Orwell" (calls __str__)
print(len(book))    # 328 (calls __len__)
print(repr(book))   # Book('1984', 'George Orwell', 328) (calls __repr__)
```

### Method Types

Python classes support three types of methods: instance methods (work with instance data), class methods (work with class-level data using `@classmethod` decorator), and static methods (independent utilities using `@staticmethod` decorator). Instance methods receive `self` to access instance attributes, class methods receive `cls` to access class attributes, and static methods receive neither, acting as utility functions namespaced within the class.

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
print(calc.add(2, 3))            # 5 (instance method - uses self)
print(Calculator.get_pi())       # 3.14159 (class method - uses cls)
print(Calculator.multiply(4, 5)) # 20 (static method - independent utility)
```

### SOLID Principles in Python

The SOLID principles are five design principles that make software designs more understandable, flexible, and maintainable.

#### 1. Single Responsibility Principle (SRP)
*"A class should have only one reason to change"*

```python
# ❌ Bad - Multiple responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Database logic
        pass
    
    def send_email(self):
        # Email logic
        pass

# ✅ Good - Single responsibility per class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Database logic
        pass

class EmailService:
    def send_email(self, user, message):
        # Email logic
        pass
```

#### 2. Open/Closed Principle (OCP)
*"Classes should be open for extension, but closed for modification"*

```python
# ✅ Good - Using inheritance for extension
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class AreaCalculator:
    def total_area(self, shapes):
        return sum(shape.area() for shape in shapes)

# Adding new shapes doesn't modify existing code
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
```

#### 3. Liskov Substitution Principle (LSP)
*"Objects of a superclass should be replaceable with objects of its subclasses"*

```python
# ✅ Good - Proper inheritance
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "Flying"
    
    def fly(self):
        return "Flying high"

class WalkingBird(Bird):
    def move(self):
        return "Walking"
    
    def walk(self):
        return "Walking on ground"

class Eagle(FlyingBird):
    def fly(self):
        return "Soaring through the sky"

class Penguin(WalkingBird):
    def walk(self):
        return "Waddling on ice"

# All birds can be used interchangeably for movement
def make_bird_move(bird: Bird):
    return bird.move()

eagle = Eagle()
penguin = Penguin()
print(make_bird_move(eagle))    # "Flying"
print(make_bird_move(penguin))  # "Walking"
```

#### 4. Interface Segregation Principle (ISP)
*"Clients should not be forced to depend on interfaces they don't use"*

```python
# ❌ Bad - Fat interface
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

# ✅ Good - Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Human working"
    
    def eat(self):
        return "Human eating"

class Robot(Workable):
    def work(self):
        return "Robot working"
    # Robot doesn't need to implement eat()
```

#### 5. Dependency Inversion Principle (DIP)
*"Depend on abstractions, not concretions"*

```python
# ❌ Bad - High-level module depends on low-level module
class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"{message}\n")

class UserService:
    def __init__(self):
        self.logger = FileLogger()  # Direct dependency
    
    def create_user(self, user):
        # Create user logic
        self.logger.log(f"User {user.name} created")

# ✅ Good - Depend on abstraction
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"{message}\n")

class DatabaseLogger(Logger):
    def log(self, message):
        # Log to database
        pass

class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger  # Depends on abstraction
    
    def create_user(self, user):
        # Create user logic
        self.logger.log(f"User {user.name} created")

# Usage with dependency injection
file_logger = FileLogger()
user_service = UserService(file_logger)
```

#### SOLID Principles Summary

```python
# Example combining all SOLID principles
from abc import ABC, abstractmethod
from typing import List

# Interfaces (ISP)
class Readable(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

class Writable(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass

# Single Responsibility (SRP)
class FileReader(Readable):
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self) -> str:
        with open(self.filename, 'r') as f:
            return f.read()

class FileWriter(Writable):
    def __init__(self, filename: str):
        self.filename = filename
    
    def write(self, data: str) -> None:
        with open(self.filename, 'w') as f:
            f.write(data)

# Open/Closed Principle (OCP) & Liskov Substitution (LSP)
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: str) -> str:
        pass

class UpperCaseProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return data.upper()

class JSONProcessor(DataProcessor):
    def process(self, data: str) -> str:
        import json
        return json.dumps({"data": data})

# Dependency Inversion (DIP)
class DocumentService:
    def __init__(self, reader: Readable, writer: Writable, processor: DataProcessor):
        self.reader = reader
        self.writer = writer
        self.processor = processor
    
    def process_document(self):
        data = self.reader.read()
        processed_data = self.processor.process(data)
        self.writer.write(processed_data)

# Usage
reader = FileReader("input.txt")
writer = FileWriter("output.txt")
processor = UpperCaseProcessor()
service = DocumentService(reader, writer, processor)
service.process_document()
```

---

## 6. Advanced Features

### Decorators

Decorators are functions that modify or enhance other functions without changing their source code. They use the `@decorator_name` syntax and follow the wrapper pattern, taking a function as input and returning a modified version. Decorators are commonly used for logging, authentication, timing, caching, and input validation, making them essential for clean, maintainable code.

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

Generators are memory-efficient iterators that produce values on-the-fly using the `yield` keyword instead of storing entire sequences in memory. They maintain their state between calls, making them perfect for processing large datasets or infinite sequences. Generator expressions (similar to list comprehensions but with parentheses) provide a concise way to create generators for simple transformations.

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

Context managers handle resource management by automatically setting up and tearing down resources using the `with` statement. They implement `__enter__` and `__exit__` methods to ensure proper cleanup even if errors occur. Context managers are essential for managing files, database connections, locks, and other resources that need guaranteed cleanup, preventing resource leaks.

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

Modules are Python files containing reusable code (functions, classes, variables) that can be imported into other programs. Python's import system supports various styles: importing entire modules, specific items, or using aliases for convenience. The standard library provides numerous built-in modules for common tasks, eliminating the need to write code from scratch for many operations.

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

Packages are directories containing Python modules organized hierarchically, with an `__init__.py` file marking them as packages. Packages enable better code organization for larger projects by grouping related modules together. Subpackages create nested namespaces, making it easier to manage and maintain large codebases with logical structure and clear separation of concerns.

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

File operations in Python are handled through built-in functions and the `with` statement for automatic resource management. Python provides multiple ways to read files: `read()` loads the entire content, iterating line-by-line is memory-efficient for large files, and `readlines()` creates a list of all lines. Always use the `with` statement to ensure proper file closure even if errors occur.

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

Python supports different file writing modes: 'w' for writing (overwrites existing content), 'a' for appending (adds to end of file), and 'w+' for reading and writing. The `write()` method writes strings to files, while `writelines()` writes a list of strings. Understanding file modes prevents accidental data loss and enables proper file manipulation for various use cases.

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

JSON (JavaScript Object Notation) is a popular data interchange format used extensively in APIs and configuration files. Python's `json` module provides `dump()`/`load()` for file operations and `dumps()`/`loads()` for string operations. JSON seamlessly converts between Python dictionaries/lists and JSON format, making it essential for web development, API integration, and data storage.

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

Sorting algorithms arrange elements in a specific order (ascending/descending) and are fundamental to computer science. Different algorithms have varying time/space complexities: Bubble Sort (O(n²)) is simple but inefficient, Quick Sort (O(n log n) average) is fast and widely used, while Merge Sort (O(n log n) guaranteed) is stable and predictable. Understanding these algorithms is crucial for technical interviews and choosing optimal solutions.

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

Dynamic Programming (DP) optimizes recursive problems by storing (memoizing) previously calculated results to avoid redundant computations. This technique transforms exponential time algorithms into polynomial time solutions. DP is essential for solving optimization problems like the knapsack problem, longest common subsequence, and shortest path algorithms, making it a critical skill for technical interviews.

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

Threading allows multiple tasks to run concurrently within a single process, sharing the same memory space. Python's `threading` module is ideal for I/O-bound tasks (file operations, network requests) where threads wait for external resources. Note: Due to Python's Global Interpreter Lock (GIL), threading doesn't provide true parallelism for CPU-bound tasks, but it's perfect for improving responsiveness in I/O-heavy applications.

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

### Advanced Threading Patterns

```python
import threading
import queue
import time
from typing import Any, Callable

# Thread Pool Pattern
class ThreadPool:
    """Custom thread pool for managing worker threads."""
    
    def __init__(self, num_workers: int = 4):
        self.task_queue = queue.Queue()
        self.workers = []
        self.results = []
        self._lock = threading.Lock()
        
        # Create worker threads
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker, daemon=True)
            worker.start()
            self.workers.append(worker)
    
    def _worker(self):
        """Worker thread that processes tasks from queue."""
        while True:
            try:
                func, args, kwargs = self.task_queue.get(timeout=1)
                result = func(*args, **kwargs)
                with self._lock:
                    self.results.append(result)
                self.task_queue.task_done()
            except queue.Empty:
                continue
    
    def submit(self, func: Callable, *args, **kwargs):
        """Submit a task to the thread pool."""
        self.task_queue.put((func, args, kwargs))
    
    def wait_completion(self):
        """Wait for all tasks to complete."""
        self.task_queue.join()
        return self.results

# Usage
def download_file(url: str) -> str:
    """Simulate file download (I/O-bound)."""
    time.sleep(1)
    return f"Downloaded {url}"

pool = ThreadPool(num_workers=4)
urls = [f"https://example.com/file{i}.txt" for i in range(10)]

for url in urls:
    pool.submit(download_file, url)

results = pool.wait_completion()
print(f"Downloaded {len(results)} files")

# Producer-Consumer Pattern with Threading
class ProducerConsumer:
    """Producer-Consumer pattern using threads and queue."""
    
    def __init__(self, num_consumers: int = 3):
        self.task_queue = queue.Queue(maxsize=10)
        self.num_consumers = num_consumers
        self.stop_event = threading.Event()
    
    def producer(self, items: list):
        """Producer adds items to queue."""
        for item in items:
            self.task_queue.put(item)
            print(f"Produced: {item}")
            time.sleep(0.1)
        
        # Signal completion
        for _ in range(self.num_consumers):
            self.task_queue.put(None)  # Poison pill
    
    def consumer(self, consumer_id: int):
        """Consumer processes items from queue."""
        while True:
            item = self.task_queue.get()
            if item is None:  # Poison pill received
                break
            
            # Process item
            print(f"Consumer {consumer_id} processing: {item}")
            time.sleep(0.5)
            self.task_queue.task_done()
    
    def run(self, items: list):
        """Start producer and consumers."""
        # Start consumers
        consumers = []
        for i in range(self.num_consumers):
            t = threading.Thread(target=self.consumer, args=(i,))
            t.start()
            consumers.append(t)
        
        # Start producer
        producer_thread = threading.Thread(target=self.producer, args=(items,))
        producer_thread.start()
        
        # Wait for completion
        producer_thread.join()
        for t in consumers:
            t.join()

# Usage
pc = ProducerConsumer(num_consumers=3)
items = list(range(20))
pc.run(items)

# Thread Synchronization Primitives
class ThreadSynchronization:
    """Demonstrate various thread synchronization mechanisms."""
    
    def __init__(self):
        self.lock = threading.Lock()
        self.rlock = threading.RLock()  # Reentrant lock
        self.semaphore = threading.Semaphore(3)  # Allow 3 threads max
        self.event = threading.Event()
        self.condition = threading.Condition()
        self.barrier = threading.Barrier(3)  # Wait for 3 threads
    
    def lock_example(self):
        """Basic lock usage."""
        with self.lock:
            # Critical section - only one thread at a time
            print(f"{threading.current_thread().name} acquired lock")
            time.sleep(1)
    
    def semaphore_example(self, worker_id: int):
        """Limit concurrent access to resource."""
        with self.semaphore:
            print(f"Worker {worker_id} accessing resource")
            time.sleep(2)
            print(f"Worker {worker_id} releasing resource")
    
    def event_example_waiter(self):
        """Wait for event to be set."""
        print("Waiting for event...")
        self.event.wait()  # Block until event is set
        print("Event received! Continuing...")
    
    def event_example_setter(self):
        """Set event after delay."""
        time.sleep(2)
        print("Setting event")
        self.event.set()
    
    def condition_example_consumer(self):
        """Wait for condition to be notified."""
        with self.condition:
            print("Consumer waiting...")
            self.condition.wait()
            print("Consumer notified!")
    
    def condition_example_producer(self):
        """Notify waiting threads."""
        time.sleep(1)
        with self.condition:
            print("Producer notifying...")
            self.condition.notify_all()
    
    def barrier_example(self, worker_id: int):
        """Synchronize multiple threads at a point."""
        print(f"Worker {worker_id} reached barrier")
        self.barrier.wait()  # Wait for all threads
        print(f"Worker {worker_id} passed barrier")

# Thread-Safe Data Structures
class ThreadSafeDict:
    """Thread-safe dictionary using RLock."""
    
    def __init__(self):
        self._dict = {}
        self._lock = threading.RLock()
    
    def get(self, key: Any, default=None):
        with self._lock:
            return self._dict.get(key, default)
    
    def set(self, key: Any, value: Any):
        with self._lock:
            self._dict[key] = value
    
    def increment(self, key: Any, amount: int = 1):
        with self._lock:
            self._dict[key] = self._dict.get(key, 0) + amount
    
    def items(self):
        with self._lock:
            return list(self._dict.items())
```

### Advanced Multiprocessing

```python
import multiprocessing as mp
from multiprocessing import Process, Queue, Pipe, Manager, Pool
import os
import time

# Process Pool with Progress Tracking
def cpu_bound_task(n: int) -> tuple:
    """CPU-intensive task that returns result."""
    result = sum(i * i for i in range(n))
    return (os.getpid(), result)

def parallel_processing_with_pool():
    """Use Pool for parallel processing."""
    with mp.Pool(processes=4) as pool:
        tasks = [1000000, 2000000, 3000000, 4000000]
        
        # Map - blocks until all complete
        results = pool.map(cpu_bound_task, tasks)
        
        # Map async - non-blocking
        async_result = pool.map_async(cpu_bound_task, tasks)
        results = async_result.get()
        
        # Apply - single task
        result = pool.apply(cpu_bound_task, (1000000,))
        
        # Apply async - single task non-blocking
        async_result = pool.apply_async(cpu_bound_task, (1000000,))
        result = async_result.get()
    
    return results

# Inter-Process Communication with Queue
def producer_process(queue: Queue, items: list):
    """Producer adds items to queue."""
    for item in items:
        queue.put(item)
        print(f"Produced: {item} by PID {os.getpid()}")
        time.sleep(0.1)
    queue.put(None)  # Signal completion

def consumer_process(queue: Queue, consumer_id: int):
    """Consumer processes items from queue."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumer {consumer_id} (PID {os.getpid()}) consumed: {item}")
        time.sleep(0.2)

def multiprocess_queue_example():
    """Demonstrate multiprocessing with Queue."""
    queue = mp.Queue()
    items = list(range(10))
    
    # Start producer
    producer = Process(target=producer_process, args=(queue, items))
    producer.start()
    
    # Start consumers
    consumers = []
    for i in range(3):
        consumer = Process(target=consumer_process, args=(queue, i))
        consumer.start()
        consumers.append(consumer)
    
    # Wait for completion
    producer.join()
    for consumer in consumers:
        queue.put(None)  # Send poison pill to each consumer
    for consumer in consumers:
        consumer.join()

# Shared Memory Between Processes
def shared_memory_example():
    """Share data between processes using Manager."""
    manager = Manager()
    shared_dict = manager.dict()
    shared_list = manager.list()
    
    def worker(worker_id: int, shared_dict, shared_list):
        shared_dict[worker_id] = f"Result from worker {worker_id}"
        shared_list.append(worker_id * 10)
        print(f"Worker {worker_id} (PID {os.getpid()}) updated shared data")
    
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(i, shared_dict, shared_list))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    print("Shared dict:", dict(shared_dict))
    print("Shared list:", list(shared_list))

# Process Pool with Callback
def task_with_callback(n: int) -> int:
    """Task that will trigger callback on completion."""
    return n * n

def on_task_complete(result):
    """Callback function called when task completes."""
    print(f"Task completed with result: {result}")

def pool_with_callbacks():
    """Use callbacks with async pool."""
    with mp.Pool(processes=4) as pool:
        for i in range(10):
            pool.apply_async(
                task_with_callback,
                args=(i,),
                callback=on_task_complete
            )
        pool.close()
        pool.join()

# Process Synchronization
def process_synchronization_example():
    """Demonstrate process synchronization primitives."""
    lock = mp.Lock()
    semaphore = mp.Semaphore(2)
    event = mp.Event()
    
    def worker_with_lock(worker_id: int, lock):
        with lock:
            print(f"Worker {worker_id} acquired lock")
            time.sleep(1)
    
    def worker_with_semaphore(worker_id: int, semaphore):
        with semaphore:
            print(f"Worker {worker_id} acquired semaphore")
            time.sleep(2)
    
    # Create processes with lock
    processes = []
    for i in range(3):
        p = Process(target=worker_with_lock, args=(i, lock))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
```

### Advanced Asyncio Patterns

```python
import asyncio
import aiohttp
import aiof files
from typing import List
import time

# Async HTTP Requests with aiohttp
async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """Fetch URL asynchronously."""
    try:
        async with session.get(url, timeout=5) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def fetch_multiple_urls(urls: List[str]):
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# Async File Operations
async def read_file_async(filepath: str) -> str:
    """Read file asynchronously."""
    async with aiofiles.open(filepath, 'r') as f:
        content = await f.read()
        return content

async def write_file_async(filepath: str, content: str):
    """Write file asynchronously."""
    async with aiofiles.open(filepath, 'w') as f:
        await f.write(content)

# Async Queue for Producer-Consumer
async def async_producer(queue: asyncio.Queue, items: List[int]):
    """Async producer adds items to queue."""
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)
    await queue.put(None)  # Signal completion

async def async_consumer(queue: asyncio.Queue, consumer_id: int):
    """Async consumer processes items from queue."""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        
        print(f"Consumer {consumer_id} processing: {item}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def async_producer_consumer():
    """Run async producer-consumer pattern."""
    queue = asyncio.Queue(maxsize=5)
    items = list(range(20))
    
    # Create producer and consumers
    producer_task = asyncio.create_task(async_producer(queue, items))
    consumer_tasks = [
        asyncio.create_task(async_consumer(queue, i))
        for i in range(3)
    ]
    
    # Wait for producer to finish
    await producer_task
    
    # Signal consumers to stop
    for _ in consumer_tasks:
        await queue.put(None)
    
    # Wait for consumers
    await asyncio.gather(*consumer_tasks)

# Async Semaphore for Rate Limiting
async def rate_limited_request(semaphore: asyncio.Semaphore, url: str):
    """Make request with rate limiting."""
    async with semaphore:
        print(f"Requesting {url}")
        await asyncio.sleep(1)  # Simulate request
        return f"Response from {url}"

async def rate_limited_requests():
    """Limit concurrent requests using semaphore."""
    semaphore = asyncio.Semaphore(3)  # Max 3 concurrent requests
    urls = [f"https://api.example.com/endpoint{i}" for i in range(10)]
    
    tasks = [rate_limited_request(semaphore, url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# Async Context Managers
class AsyncDatabase:
    """Async context manager for database connection."""
    
    async def __aenter__(self):
        print("Connecting to database...")
        await asyncio.sleep(0.5)
        self.connection = "DatabaseConnection"
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.5)
        return False
    
    async def query(self, sql: str):
        print(f"Executing: {sql}")
        await asyncio.sleep(0.2)
        return ["result1", "result2"]

async def use_async_db():
    """Use async context manager."""
    async with AsyncDatabase() as db:
        results = await db.query("SELECT * FROM users")
        return results

# Async Generators
async def async_number_generator(n: int):
    """Async generator that yields numbers."""
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def consume_async_generator():
    """Consume async generator."""
    async for num in async_number_generator(10):
        print(f"Received: {num}")

# Async Task Groups (Python 3.11+)
async def task_with_timeout():
    """Task that might timeout."""
    try:
        async with asyncio.timeout(2):
            await asyncio.sleep(5)
            return "Completed"
    except asyncio.TimeoutError:
        return "Timeout"

# Async vs Sync Performance Comparison
def sync_io_task(n: int):
    """Synchronous I/O task."""
    time.sleep(0.5)
    return n * 2

async def async_io_task(n: int):
    """Asynchronous I/O task."""
    await asyncio.sleep(0.5)
    return n * 2

def compare_performance():
    """Compare sync vs async performance."""
    # Synchronous - takes 5 seconds (10 * 0.5)
    start = time.time()
    results = [sync_io_task(i) for i in range(10)]
    sync_time = time.time() - start
    print(f"Sync time: {sync_time:.2f}s")
    
    # Asynchronous - takes ~0.5 seconds (concurrent)
    start = time.time()
    results = asyncio.run(asyncio.gather(*[async_io_task(i) for i in range(10)]))
    async_time = time.time() - start
    print(f"Async time: {async_time:.2f}s")
    print(f"Speedup: {sync_time/async_time:.2f}x")

# Run async code
# asyncio.run(fetch_multiple_urls(['https://example.com'] * 5))
# asyncio.run(async_producer_consumer())
# asyncio.run(rate_limited_requests())
```

### Choosing the Right Concurrency Model

```python
"""
Python Concurrency Decision Guide:

1. THREADING - Use for I/O-bound tasks
   ✓ Network requests, file I/O, database queries
   ✓ Tasks that wait for external resources
   ✓ Need to share memory between tasks
   ✗ CPU-bound tasks (GIL limits performance)
   Example: Downloading multiple files, web scraping

2. MULTIPROCESSING - Use for CPU-bound tasks
   ✓ Heavy computations, data processing
   ✓ True parallelism needed
   ✓ Can utilize multiple CPU cores
   ✗ Higher memory overhead (separate processes)
   ✗ Slower inter-process communication
   Example: Image processing, scientific computing

3. ASYNCIO - Use for high-concurrency I/O
   ✓ Thousands of concurrent connections
   ✓ Event-driven applications
   ✓ Most efficient for I/O-bound tasks
   ✓ Single-threaded, lower overhead
   ✗ Requires async libraries (aiohttp, aiofiles)
   ✗ All code must be async-aware
   Example: Web servers, API clients, chat servers

Performance Comparison:
- Threading: Good for 10-100 concurrent I/O tasks
- Asyncio: Excellent for 1000+ concurrent I/O tasks
- Multiprocessing: Best for utilizing all CPU cores
"""

# Practical example combining all three
import asyncio
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class HybridProcessor:
    """Combine threading, multiprocessing, and asyncio."""
    
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=10)
        self.process_pool = ProcessPoolExecutor(max_workers=4)
    
    async def process_urls_async(self, urls: List[str]):
        """Use asyncio for I/O-bound URL fetching."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url(session, url) for url in urls]
            return await asyncio.gather(*tasks)
    
    async def fetch_url(self, session, url):
        async with session.get(url) as response:
            return await response.text()
    
    def process_images_parallel(self, images: List[str]):
        """Use multiprocessing for CPU-bound image processing."""
        return self.process_pool.map(self.process_image, images)
    
    @staticmethod
    def process_image(image_path: str):
        """CPU-intensive image processing."""
        # Simulate image processing
        time.sleep(2)
        return f"Processed {image_path}"
    
    def download_files_threaded(self, urls: List[str]):
        """Use threading for I/O-bound file downloads."""
        return list(self.thread_pool.map(self.download_file, urls))
    
    @staticmethod
    def download_file(url: str):
        """Simulate file download."""
        time.sleep(1)
        return f"Downloaded {url}"
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

## 16. Asynchronous Programming

### Async/Await Basics

Asynchronous programming allows concurrent execution of I/O-bound tasks without blocking, making applications more efficient. Python's `asyncio` module uses `async`/`await` keywords to write non-blocking code. This is essential for web servers, API clients, database operations, and any scenario where waiting for I/O shouldn't freeze your program.

```python
import asyncio

# Basic async function
async def fetch_data(id):
    """Simulate fetching data asynchronously."""
    print(f"Fetching data {id}...")
    await asyncio.sleep(1)  # Simulates I/O operation
    return f"Data {id}"

async def main():
    """Run multiple async tasks concurrently."""
    # Sequential execution (slower)
    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    print(f"Sequential: {result1}, {result2}")
    
    # Concurrent execution (faster)
    results = await asyncio.gather(
        fetch_data(3),
        fetch_data(4),
        fetch_data(5)
    )
    print(f"Concurrent: {results}")

# Run the async program
asyncio.run(main())
```

### Async Context Managers and Generators

```python
import asyncio
import aiohttp

# Async context manager
class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Opening database connection...")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.1)
    
    async def query(self, sql):
        await asyncio.sleep(0.1)
        return f"Results for: {sql}"

# Async generator
async def async_range(start, stop):
    """Async generator example."""
    for i in range(start, stop):
        await asyncio.sleep(0.1)
        yield i

async def demo():
    # Using async context manager
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(result)
    
    # Using async generator
    async for i in async_range(1, 5):
        print(f"Generated: {i}")

asyncio.run(demo())
```

### Async HTTP Requests

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """Fetch a single URL."""
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = [
    'https://api.github.com/users/github',
    'https://api.github.com/users/python',
]
# results = asyncio.run(fetch_multiple_urls(urls))
```

---

## 17. REST APIs & FastAPI

### FastAPI Basics

FastAPI is a modern, fast web framework for building APIs with Python. It provides automatic API documentation, type validation, and excellent performance. FastAPI uses Python type hints for automatic request/response validation and is built on Starlette and Pydantic, making it perfect for production-ready APIs.

```python
from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="My API", version="1.0.0")

# Pydantic models for request/response validation
class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=50)
    email: str
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: bool = True

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

# In-memory database (use real DB in production)
users_db: List[User] = [
    User(id=1, name="Alice", email="alice@example.com", age=30),
    User(id=2, name="Bob", email="bob@example.com", age=25),
]

# GET endpoint - List all users
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to My API"}

@app.get("/users", response_model=List[User])
async def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Get list of users with pagination."""
    return users_db[skip : skip + limit]

# GET endpoint with path parameter
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int = Path(..., gt=0)):
    """Get a specific user by ID."""
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST endpoint - Create user
@app.post("/users", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """Create a new user."""
    new_id = max([u.id for u in users_db], default=0) + 1
    new_user = User(id=new_id, **user.dict())
    users_db.append(new_user)
    return new_user

# PUT endpoint - Update user
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserCreate):
    """Update an existing user."""
    user_idx = next((i for i, u in enumerate(users_db) if u.id == user_id), None)
    if user_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = User(id=user_id, **user_update.dict())
    users_db[user_idx] = updated_user
    return updated_user

# DELETE endpoint
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user."""
    user_idx = next((i for i, u in enumerate(users_db) if u.id == user_id), None)
    if user_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_idx)
    return {"message": f"User {deleted_user.name} deleted successfully"}

# Run with: uvicorn main:app --reload
```

### FastAPI Advanced Features

```python
from fastapi import FastAPI, Depends, Header, Cookie
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import jwt

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency injection
async def get_current_user(token: str = Header(None)):
    """Dependency to get current user from token."""
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    # Decode token and get user (simplified)
    return {"user_id": 1, "username": "alice"}

# Using dependencies
@app.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    """Get current user info."""
    return current_user

# Background tasks
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    """Simulate sending email."""
    print(f"Sending email to {email}: {message}")

@app.post("/send-notification")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    """Send notification in background."""
    background_tasks.add_task(send_email, email, "Hello!")
    return {"message": "Notification sent"}

# File upload
from fastapi import File, UploadFile

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file."""
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }
```

### REST API Best Practices

```python
from enum import Enum
from fastapi import status

# Use enums for fixed choices
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

# Proper status codes
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user_properly(user: UserCreate):
    """Create user with proper status code."""
    # ... create user logic
    pass

# Error responses with detail
class ErrorResponse(BaseModel):
    detail: str
    error_code: str
    timestamp: str

@app.get("/users/{user_id}", responses={
    404: {"model": ErrorResponse},
    200: {"model": User}
})
async def get_user_with_error_handling(user_id: int):
    """Get user with proper error handling."""
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(
            status_code=404,
            detail={
                "detail": "User not found",
                "error_code": "USER_NOT_FOUND",
                "timestamp": "2025-12-11T10:00:00Z"
            }
        )
    return user
```

---

## 18. Database Operations

### SQLAlchemy ORM

SQLAlchemy is Python's most popular ORM (Object-Relational Mapping) library, allowing you to interact with databases using Python classes instead of raw SQL. It provides database abstraction, automatic migrations, relationship handling, and query building, making database operations more Pythonic and maintainable.

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

# Define models
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

# Create tables
Base.metadata.create_all(engine)

# CRUD operations
session = Session()

# Create
new_user = User(username='alice', email='alice@example.com')
session.add(new_user)
session.commit()

# Read
user = session.query(User).filter_by(username='alice').first()
all_users = session.query(User).all()

# Update
user.email = 'newemail@example.com'
session.commit()

# Delete
session.delete(user)
session.commit()

session.close()
```

### Async Database with FastAPI

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# Async engine
engine = create_async_engine('sqlite+aiosqlite:///async_example.db')
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Using in FastAPI
@app.get("/users")
async def get_users_async(db: AsyncSession = Depends(get_db)):
    """Get users asynchronously."""
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
```

---

## 19. Testing

### Pytest Basics

Testing ensures code reliability and catches bugs early. Pytest is Python's most popular testing framework, offering simple syntax, powerful fixtures, and excellent plugin ecosystem. Writing tests is crucial for maintaining code quality, enabling refactoring, and building confidence in deployments.

```python
# test_calculator.py
import pytest

# Simple test
def add(a, b):
    return a + b

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    """Test add with multiple inputs."""
    assert add(a, b) == expected

# Fixtures for setup/teardown
@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    """Test using fixture."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15

# Testing exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    """Test that division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Run with: pytest test_calculator.py
```

### Testing FastAPI

```python
from fastapi.testclient import TestClient

# test_api.py
def test_read_main():
    """Test root endpoint."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to My API"}

def test_create_user():
    """Test user creation."""
    client = TestClient(app)
    response = client.post(
        "/users",
        json={"name": "Test User", "email": "test@example.com", "age": 25}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_get_nonexistent_user():
    """Test getting user that doesn't exist."""
    client = TestClient(app)
    response = client.get("/users/99999")
    assert response.status_code == 404
```

---

## 20. Type Hints & Static Type Checking

### Type Hints

Type hints improve code readability, enable better IDE support, and catch bugs early. They don't affect runtime but help with documentation and static analysis tools like mypy. Type hints are increasingly important in modern Python development and are commonly used in professional codebases.

```python
from typing import List, Dict, Optional, Union, Callable, Tuple, Any

# Basic type hints
def greet(name: str) -> str:
    """Function with type hints."""
    return f"Hello, {name}"

# Collection types
def process_items(items: List[int]) -> int:
    """Process list of integers."""
    return sum(items)

def get_user(user_id: int) -> Dict[str, Any]:
    """Return user dictionary."""
    return {"id": user_id, "name": "Alice"}

# Optional types
def find_user(user_id: int) -> Optional[Dict]:
    """Return user or None if not found."""
    return None if user_id > 100 else {"id": user_id}

# Union types
def process_id(id: Union[int, str]) -> str:
    """Accept int or string ID."""
    return str(id)

# Callable types
def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    """Apply operation to number."""
    return operation(x)

# Generic types
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation."""
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Using generic
int_stack: Stack[int] = Stack()
int_stack.push(1)
```

---

## 21. Python Interview Topics

### Common Interview Questions

Understanding these concepts is crucial for technical interviews. They test your knowledge of Python's internals, best practices, and problem-solving abilities. These topics frequently appear in interviews for Python developer positions at all levels.

```python
# 1. What is the difference between list and tuple?
# Lists are mutable, tuples are immutable
# Tuples are faster and use less memory

# 2. Explain *args and **kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")       # Positional arguments as tuple
    print(f"Kwargs: {kwargs}")   # Keyword arguments as dict

# 3. What is a decorator?
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return result
    return wrapper

# 4. Explain list comprehension vs generator expression
list_comp = [x**2 for x in range(1000)]     # Creates list in memory
gen_exp = (x**2 for x in range(1000))       # Generates on-demand

# 5. What is the GIL (Global Interpreter Lock)?
# The GIL prevents multiple threads from executing Python bytecode
# Use multiprocessing for CPU-bound tasks, threading for I/O-bound

# 6. Shallow vs Deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)      # Copies outer list only
deep = copy.deepcopy(original)     # Copies everything recursively

# 7. What are Python's magic methods?
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# 8. Explain generators and yield
def infinite_sequence():
    num = 0
    while True:
        yield num  # Returns value and pauses execution
        num += 1

# 9. What is monkey patching?
# Modifying/extending classes at runtime
import datetime
datetime.datetime.now = lambda: "Patched!"

# 10. Context managers
class FileManager:
    def __enter__(self):
        # Setup code
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup code
        pass
```

---

## 22. Exception Handling & Error Management

### Understanding Exceptions

Exception handling is critical for writing robust, production-ready code. Proper error handling prevents crashes, provides meaningful feedback, and enables graceful degradation. Understanding Python's exception hierarchy and handling mechanisms is essential for any professional developer and frequently tested in interviews.

```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")

# Multiple exceptions
try:
    data = {"name": "Alice"}
    age = data["age"]  # KeyError
except (KeyError, ValueError) as e:
    print(f"Error: {e}")

# Exception with else clause
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {number}")  # Runs if no exception
finally:
    print("Cleanup code")
```

### Custom Exceptions

```python
# Creating custom exceptions
class ValidationError(Exception):
    """Raised when validation fails."""
    def __init__(self, message, field_name=None):
        self.message = message
        self.field_name = field_name
        super().__init__(self.message)

class DatabaseError(Exception):
    """Custom database error."""
    pass

class APIError(Exception):
    """API-specific errors."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")

# Using custom exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "age")
    if age < 0 or age > 150:
        raise ValidationError("Age must be between 0 and 150", "age")
    return True

def fetch_user_data(user_id):
    if user_id < 0:
        raise APIError(400, "Invalid user ID")
    # Fetch data logic
    return {"id": user_id, "name": "User"}

# Handling custom exceptions
try:
    validate_age("twenty")
except ValidationError as e:
    print(f"Validation failed for {e.field_name}: {e.message}")

try:
    user = fetch_user_data(-1)
except APIError as e:
    print(f"Status: {e.status_code}, Message: {e.message}")
```

### Exception Chaining and Context

```python
# Exception chaining (Python 3+)
class DataProcessingError(Exception):
    pass

def process_data(data):
    try:
        result = int(data)
    except ValueError as e:
        raise DataProcessingError("Failed to process data") from e

try:
    process_data("invalid")
except DataProcessingError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")

# Suppressing exception context
try:
    # Some operation
    raise ValueError("Original error")
except ValueError:
    raise RuntimeError("New error") from None  # Suppress original
```

### Best Practices for Exception Handling

```python
# ✅ GOOD: Specific exceptions
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    if 'file' in locals():
        file.close()

# ❌ BAD: Bare except
try:
    risky_operation()
except:  # Don't do this!
    pass

# ✅ GOOD: Context manager (automatic cleanup)
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")

# ✅ GOOD: Logging exceptions
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = complex_operation()
except Exception as e:
    logging.error(f"Operation failed: {e}", exc_info=True)
    raise  # Re-raise after logging
```

---

## 23. Regular Expressions (Regex)

### Regex Basics

Regular expressions are powerful patterns for matching and manipulating text. They're essential for data validation, text parsing, web scraping, and log analysis. Mastering regex is crucial for interviews and real-world text processing tasks.

```python
import re

# Basic pattern matching
text = "My email is john@example.com and phone is 123-456-7890"

# Search for pattern
email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
if email_match:
    print(f"Found email: {email_match.group()}")

# Find all matches
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                    "Contact: john@example.com or jane@test.org")
print(f"All emails: {emails}")

# Match phone numbers
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone = re.search(phone_pattern, text)
print(f"Phone: {phone.group()}")
```

### Common Regex Patterns

```python
import re

# Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Phone number validation (US format)
def is_valid_phone(phone):
    pattern = r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return bool(re.match(pattern, phone))

# URL validation
def is_valid_url(url):
    pattern = r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b'
    return bool(re.match(pattern, url))

# Password strength (min 8 chars, 1 upper, 1 lower, 1 digit)
def is_strong_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))

# Test validations
print(is_valid_email("user@example.com"))      # True
print(is_valid_phone("123-456-7890"))          # True
print(is_valid_url("https://www.google.com"))  # True
print(is_strong_password("SecurePass123"))     # True
```

### Advanced Regex Operations

```python
import re

# Substitution
text = "The price is $100 and discount is $20"
new_text = re.sub(r'\$(\d+)', r'USD \1', text)
print(new_text)  # "The price is USD 100 and discount is USD 20"

# Split by pattern
data = "apple,banana;orange:grape"
fruits = re.split(r'[,;:]', data)
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# Named groups
log_line = "2025-12-11 10:30:45 ERROR: Database connection failed"
pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+): (?P<message>.+)'
match = re.match(pattern, log_line)
if match:
    print(match.groupdict())
    # {'date': '2025-12-11', 'time': '10:30:45', 'level': 'ERROR', 'message': 'Database connection failed'}

# Compile patterns for reuse (more efficient)
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
text1 = "Contact: john@example.com"
text2 = "Email: jane@test.org"
print(email_pattern.findall(text1))
print(email_pattern.findall(text2))
```

### Practical Regex Examples

```python
import re

# Extract hashtags from social media text
def extract_hashtags(text):
    return re.findall(r'#\w+', text)

# Extract mentions
def extract_mentions(text):
    return re.findall(r'@\w+', text)

# Clean HTML tags
def remove_html_tags(html):
    return re.sub(r'<[^>]+>', '', html)

# Extract numbers from text
def extract_numbers(text):
    return [float(n) for n in re.findall(r'-?\d+\.?\d*', text)]

# Validate credit card (basic)
def is_valid_credit_card(card):
    # Remove spaces and dashes
    card = re.sub(r'[\s-]', '', card)
    return bool(re.match(r'^\d{13,19}$', card))

# Usage
tweet = "Check out #Python and #FastAPI! Thanks @john_doe"
print(extract_hashtags(tweet))   # ['#Python', '#FastAPI']
print(extract_mentions(tweet))   # ['@john_doe']

html = "<p>Hello <b>World</b>!</p>"
print(remove_html_tags(html))    # "Hello World!"

text = "The price is $19.99 and quantity is 5"
print(extract_numbers(text))     # [19.99, 5.0]
```

---

## 24. Virtual Environments & Package Management

### Virtual Environments

Virtual environments isolate project dependencies, preventing version conflicts between projects. Understanding virtual environments is fundamental for Python development and is one of the first questions in technical interviews about Python project setup.

```python
# Create virtual environment
# Command line:
# python -m venv myenv              # Create venv
# source myenv/bin/activate         # Activate (Mac/Linux)
# myenv\Scripts\activate           # Activate (Windows)
# deactivate                        # Deactivate

# Check active environment
import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
```

### Package Management with pip

```bash
# Install packages
pip install requests
pip install fastapi uvicorn
pip install pandas numpy matplotlib

# Install specific version
pip install django==4.2.0

# Install from requirements.txt
pip install -r requirements.txt

# Upgrade package
pip upgrade requests

# Uninstall package
pip uninstall requests

# List installed packages
pip list

# Show package info
pip show requests

# Generate requirements.txt
pip freeze > requirements.txt

# Install in development mode
pip install -e .
```

### Requirements.txt Best Practices

```python
# requirements.txt
# Production dependencies with pinned versions
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
sqlalchemy==2.0.23
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# requirements-dev.txt
# Development dependencies
-r requirements.txt  # Include production requirements
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
flake8==6.1.0
mypy==1.7.1
```

### Poetry - Modern Dependency Management

```python
# pyproject.toml (Poetry configuration)
# [tool.poetry]
# name = "my-project"
# version = "0.1.0"
# description = "My awesome project"
# authors = ["Your Name <you@example.com>"]
# 
# [tool.poetry.dependencies]
# python = "^3.9"
# fastapi = "^0.104.0"
# uvicorn = "^0.24.0"
# 
# [tool.poetry.dev-dependencies]
# pytest = "^7.4.0"
# black = "^23.11.0"

# Poetry commands:
# poetry init                 # Initialize new project
# poetry add fastapi         # Add dependency
# poetry add --dev pytest    # Add dev dependency
# poetry install             # Install all dependencies
# poetry update              # Update dependencies
# poetry run python main.py  # Run with poetry environment
```

### Environment Variables with python-dotenv

```python
# .env file (never commit to git!)
# DATABASE_URL=postgresql://user:pass@localhost/dbname
# SECRET_KEY=your-secret-key-here
# API_KEY=your-api-key
# DEBUG=True
# PORT=8000

# Loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file

# Access environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
PORT = int(os.getenv("PORT", 8000))

print(f"Database: {DATABASE_URL}")
print(f"Debug mode: {DEBUG}")

# Using with Pydantic for validation
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8000
    
    class Config:
        env_file = ".env"

settings = Settings()
print(settings.database_url)
```

---

## 25. Logging & Monitoring

### Python Logging Module

Logging is essential for debugging, monitoring, and maintaining production applications. Proper logging practices help track application behavior, diagnose issues, and understand system performance. This is a must-know topic for professional development.

```python
import logging
from datetime import datetime

# Basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Log levels (from least to most severe)
logger.debug("Detailed debugging information")
logger.info("General informational messages")
logger.warning("Warning messages")
logger.error("Error messages")
logger.critical("Critical errors")

# Example usage
def divide(a, b):
    logger.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logger.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted", exc_info=True)
        raise
```

### Advanced Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import sys

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Create formatters
detailed_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)
simple_formatter = logging.Formatter('%(levelname)s - %(message)s')

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(simple_formatter)

# File handler with rotation
file_handler = RotatingFileHandler(
    'app.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(detailed_formatter)

# Time-based rotation
timed_handler = TimedRotatingFileHandler(
    'daily.log',
    when='midnight',
    interval=1,
    backupCount=7
)
timed_handler.setFormatter(detailed_formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(timed_handler)

# Usage
logger.info("Application started")
logger.debug("Debug information")
logger.error("An error occurred")
```

### Logging in FastAPI

```python
import logging
from fastapi import FastAPI, Request
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    logger.info(f"Request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(
        f"Response: {response.status_code} - "
        f"Completed in {process_time:.4f}s"
    )
    
    return response

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}

@app.post("/users")
async def create_user(user_data: dict):
    logger.info(f"Creating user: {user_data.get('name')}")
    try:
        # Create user logic
        logger.debug(f"User data: {user_data}")
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Failed to create user: {e}", exc_info=True)
        raise
```

### Structured Logging (JSON)

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging."""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        # Add custom fields
        if hasattr(record, 'user_id'):
            log_data["user_id"] = record.user_id
        if hasattr(record, 'request_id'):
            log_data["request_id"] = record.request_id
        
        return json.dumps(log_data)

# Setup logger with JSON formatter
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage with custom fields
logger.info("User logged in", extra={"user_id": 123, "request_id": "abc-123"})
```

---

## 26. Authentication & Security

### Password Hashing

Secure password handling is critical for any application with user authentication. Never store passwords in plain text. Understanding password hashing, salting, and secure authentication is essential for web development interviews.

```python
from passlib.context import CryptContext

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

# Usage
password = "SecurePassword123!"
hashed = hash_password(password)
print(f"Hashed: {hashed}")

# Verification
is_valid = verify_password("SecurePassword123!", hashed)
print(f"Password valid: {is_valid}")

is_invalid = verify_password("WrongPassword", hashed)
print(f"Wrong password valid: {is_invalid}")
```

### JWT Authentication

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

# Configuration
SECRET_KEY = "your-secret-key-keep-it-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """Decode and validate a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return payload
    except JWTError:
        return None

# Usage
# Create token
user_data = {"sub": "john@example.com", "role": "admin"}
token = create_access_token(user_data, timedelta(minutes=30))
print(f"Token: {token}")

# Verify token
decoded = decode_access_token(token)
print(f"Decoded: {decoded}")
```

### FastAPI Authentication

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# Fake database
fake_users_db = {
    "john": {
        "username": "john",
        "email": "john@example.com",
        "full_name": "John Doe",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

def get_user(username: str):
    """Get user from database."""
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)

def authenticate_user(username: str, password: str):
    """Authenticate a user."""
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current user from token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """Get current active user."""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login endpoint to get access token."""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user info."""
    return current_user

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    """Protected endpoint requiring authentication."""
    return {"message": f"Hello {current_user.username}!"}
```

### API Security Best Practices

```python
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZIPMiddleware
import secrets

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["yourdomain.com", "*.yourdomain.com"]
)

# GZIP compression
app.add_middleware(GZIPMiddleware, minimum_size=1000)

# API Key authentication
API_KEYS = {
    "secret-key-1": "user1",
    "secret-key-2": "user2",
}

async def verify_api_key(x_api_key: str = Header(...)):
    """Verify API key."""
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return API_KEYS[x_api_key]

@app.get("/api/data")
async def get_data(user: str = Depends(verify_api_key)):
    """Protected endpoint with API key."""
    return {"data": "secret information", "user": user}

# Rate limiting (using slowapi)
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")
async def limited_endpoint(request: Request):
    """Endpoint with rate limiting."""
    return {"message": "This endpoint is rate limited"}
```

---

## 27. Docker & Deployment

### Dockerfile for Python Applications

Docker containerization is standard in modern development. Understanding how to containerize Python applications is essential for deployment and frequently asked in interviews for backend positions.

```dockerfile
# Dockerfile
# Multi-stage build for Python FastAPI application

# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose for Full Stack

```yaml
# docker-compose.yml
version: '3.8'

services:
  # FastAPI application
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./app:/app
    networks:
      - app-network

  # PostgreSQL database
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - app-network

  # Redis cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - app-network

  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - api
    networks:
      - app-network

volumes:
  postgres-data:

networks:
  app-network:
    driver: bridge
```

### Python Application with Docker Commands

```bash
# Build image
docker build -t myapp:latest .

# Run container
docker run -d -p 8000:8000 --name myapp-container myapp:latest

# View logs
docker logs myapp-container

# Execute command in container
docker exec -it myapp-container bash

# Stop and remove container
docker stop myapp-container
docker rm myapp-container

# Docker Compose commands
docker-compose up -d          # Start all services
docker-compose down           # Stop all services
docker-compose logs -f api    # View logs
docker-compose ps             # List services
docker-compose restart api    # Restart service
```

### Production-Ready FastAPI with Docker

```python
# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="My API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    logger.info("Application starting up...")
    # Initialize database connections, load models, etc.

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    logger.info("Application shutting down...")
    # Close database connections, cleanup resources

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker."""
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to My API"}

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 28. Design Patterns

### Singleton Pattern

Design patterns provide proven solutions to common programming problems. Understanding design patterns demonstrates advanced knowledge and is frequently tested in senior developer interviews. They promote code reusability, maintainability, and scalability.

```python
class Singleton:
    """Singleton pattern ensures only one instance exists."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - same instance

# Thread-safe Singleton
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Practical example: Database connection
class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection = "Connected to database"
        print("Database connection initialized")
    
    def query(self, sql):
        return f"Executing: {sql}"

# All instances share the same connection
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

### Factory Pattern

```python
from abc import ABC, abstractmethod

# Abstract product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Factory
class AnimalFactory:
    """Factory pattern creates objects without specifying exact class."""
    
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        animals = {
            "dog": Dog,
            "cat": Cat,
            "bird": Bird
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class is None:
            raise ValueError(f"Unknown animal type: {animal_type}")
        
        return animal_class()

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # "Woof!"
print(cat.speak())  # "Meow!"

# Practical example: API Client Factory
class APIClient(ABC):
    @abstractmethod
    def request(self, endpoint: str):
        pass

class RESTClient(APIClient):
    def request(self, endpoint: str):
        return f"REST request to {endpoint}"

class GraphQLClient(APIClient):
    def request(self, endpoint: str):
        return f"GraphQL query to {endpoint}"

class ClientFactory:
    @staticmethod
    def create_client(client_type: str) -> APIClient:
        clients = {
            "rest": RESTClient,
            "graphql": GraphQLClient
        }
        return clients[client_type]()
```

### Observer Pattern

```python
from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Subject (Observable)
class Subject:
    """Subject maintains list of observers and notifies them of changes."""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None
    
    def attach(self, observer: Observer):
        """Add an observer."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Remove an observer."""
        self._observers.remove(observer)
    
    def notify(self, message: str):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(message)
    
    def set_state(self, state):
        """Change state and notify observers."""
        self._state = state
        self.notify(f"State changed to: {state}")

# Concrete observers
class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"Email notification: {message}")

class SMSNotifier(Observer):
    def update(self, message: str):
        print(f"SMS notification: {message}")

class PushNotifier(Observer):
    def update(self, message: str):
        print(f"Push notification: {message}")

# Usage
subject = Subject()

email = EmailNotifier()
sms = SMSNotifier()
push = PushNotifier()

subject.attach(email)
subject.attach(sms)
subject.attach(push)

subject.set_state("Order shipped")
# Output:
# Email notification: State changed to: Order shipped
# SMS notification: State changed to: Order shipped
# Push notification: State changed to: Order shipped

subject.detach(sms)
subject.set_state("Order delivered")
# Only email and push notifiers receive this
```

### Strategy Pattern

```python
from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float):
        return f"Paid ${amount} using PayPal account {self.email}"

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float):
        return f"Paid ${amount} using Crypto wallet {self.wallet_address}"

# Context
class ShoppingCart:
    """Context uses Strategy pattern to allow different payment methods."""
    
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item: str, price: float):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(price for _, price in self.items)
        if self.payment_strategy is None:
            return "No payment method selected"
        return self.payment_strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)

# Pay with credit card
cart.set_payment_strategy(CreditCardPayment("1234567890123456", "123"))
print(cart.checkout())

# Pay with PayPal
cart.set_payment_strategy(PayPalPayment("user@example.com"))
print(cart.checkout())

# Pay with Crypto
cart.set_payment_strategy(CryptoPayment("0x1234..."))
print(cart.checkout())
```

### Decorator Pattern

```python
from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0
    
    def description(self) -> str:
        return "Simple coffee"

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def cost(self) -> float:
        return self._coffee.cost()
    
    def description(self) -> str:
        return self._coffee.description()

# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5
    
    def description(self) -> str:
        return self._coffee.description() + ", milk"

class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2
    
    def description(self) -> str:
        return self._coffee.description() + ", sugar"

class WhippedCream(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.7
    
    def description(self) -> str:
        return self._coffee.description() + ", whipped cream"

# Usage
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost()}")

# Add milk
coffee = Milk(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

# Add sugar
coffee = Sugar(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

# Add whipped cream
coffee = WhippedCream(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")
# Output: Simple coffee, milk, sugar, whipped cream: $3.4
```

---

## 29. Caching & Performance Optimization

### Function Caching with functools

Caching stores computed results to avoid redundant calculations, dramatically improving performance. Understanding caching strategies is crucial for building scalable applications and is a common topic in performance optimization interviews.

```python
from functools import lru_cache, cache
import time

# LRU Cache (Least Recently Used)
@lru_cache(maxsize=128)
def fibonacci(n):
    """Fibonacci with caching - O(n) instead of O(2^n)."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test performance
start = time.time()
result = fibonacci(35)
print(f"Result: {result}, Time: {time.time() - start:.4f}s")

# Cache info
print(fibonacci.cache_info())
# CacheInfo(hits=33, misses=36, maxsize=128, currsize=36)

# Clear cache
fibonacci.cache_clear()

# Simple cache (Python 3.9+) - unbounded
@cache
def expensive_computation(x, y):
    """Cached computation with no size limit."""
    time.sleep(1)  # Simulate expensive operation
    return x ** y

# First call: slow
print(expensive_computation(2, 10))  # Takes 1 second

# Second call: instant
print(expensive_computation(2, 10))  # Instant from cache
```

### Redis Caching

```python
import redis
import json
from functools import wraps
from typing import Callable, Any

# Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def redis_cache(expiration: int = 3600):
    """Decorator for Redis caching."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Create cache key
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Try to get from cache
            cached_result = redis_client.get(cache_key)
            if cached_result is not None:
                print(f"Cache HIT for {cache_key}")
                return json.loads(cached_result)
            
            # Compute result
            print(f"Cache MISS for {cache_key}")
            result = func(*args, **kwargs)
            
            # Store in cache
            redis_client.setex(
                cache_key,
                expiration,
                json.dumps(result)
            )
            
            return result
        return wrapper
    return decorator

@redis_cache(expiration=300)  # Cache for 5 minutes
def get_user_data(user_id: int):
    """Simulate expensive database query."""
    time.sleep(2)  # Simulate slow query
    return {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }

# First call: slow (cache miss)
user = get_user_data(123)

# Second call: fast (cache hit)
user = get_user_data(123)
```

### Caching with FastAPI

```python
from fastapi import FastAPI, Depends
from functools import lru_cache
import time

app = FastAPI()

# Cache configuration
@lru_cache()
def get_settings():
    """Cached settings - loaded once."""
    print("Loading settings...")
    return {
        "app_name": "My API",
        "admin_email": "admin@example.com",
        "items_per_page": 50
    }

@app.get("/info")
async def info(settings: dict = Depends(get_settings)):
    """Endpoint using cached settings."""
    return settings

# Response caching middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import hashlib

class CacheMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, cache_time: int = 60):
        super().__init__(app)
        self.cache = {}
        self.cache_time = cache_time
    
    async def dispatch(self, request: Request, call_next):
        # Only cache GET requests
        if request.method != "GET":
            return await call_next(request)
        
        # Create cache key
        cache_key = hashlib.md5(
            f"{request.url.path}{request.url.query}".encode()
        ).hexdigest()
        
        # Check cache
        if cache_key in self.cache:
            cached_response, timestamp = self.cache[cache_key]
            if time.time() - timestamp < self.cache_time:
                return cached_response
        
        # Get fresh response
        response = await call_next(request)
        
        # Cache response
        self.cache[cache_key] = (response, time.time())
        
        return response

# Add caching middleware
app.add_middleware(CacheMiddleware, cache_time=60)

# Manual caching for specific endpoints
cache_store = {}

@app.get("/expensive-operation")
async def expensive_operation():
    """Manually cached endpoint."""
    cache_key = "expensive_operation"
    
    # Check cache
    if cache_key in cache_store:
        cached_data, timestamp = cache_store[cache_key]
        if time.time() - timestamp < 300:  # 5 minutes
            return {"data": cached_data, "cached": True}
    
    # Perform expensive operation
    time.sleep(2)
    result = {"value": 12345, "computed": True}
    
    # Cache result
    cache_store[cache_key] = (result, time.time())
    
    return {"data": result, "cached": False}
```

### Cache Strategies and Best Practices

```python
import time
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

class CacheManager:
    """Advanced cache manager with multiple strategies."""
    
    def __init__(self):
        self.cache: Dict[str, Dict[str, Any]] = {}
    
    def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if key in self.cache:
            entry = self.cache[key]
            
            # Check expiration
            if entry["expires_at"] > datetime.now():
                entry["hits"] += 1
                entry["last_accessed"] = datetime.now()
                return entry["value"]
            else:
                # Expired
                del self.cache[key]
        
        return None
    
    def set(self, key: str, value: Any, ttl: int = 3600):
        """Set value in cache with TTL."""
        self.cache[key] = {
            "value": value,
            "created_at": datetime.now(),
            "last_accessed": datetime.now(),
            "expires_at": datetime.now() + timedelta(seconds=ttl),
            "hits": 0
        }
    
    def invalidate(self, key: str):
        """Remove key from cache."""
        if key in self.cache:
            del self.cache[key]
    
    def clear(self):
        """Clear all cache."""
        self.cache.clear()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        total_hits = sum(entry["hits"] for entry in self.cache.values())
        return {
            "total_keys": len(self.cache),
            "total_hits": total_hits,
            "keys": list(self.cache.keys())
        }

# Usage
cache = CacheManager()

# Cache with 5-minute TTL
cache.set("user:123", {"name": "Alice", "email": "alice@example.com"}, ttl=300)

# Get from cache
user = cache.get("user:123")
print(user)

# Get stats
print(cache.get_stats())

# Cache invalidation patterns

# 1. Time-based expiration (TTL)
cache.set("temp_data", "value", ttl=60)

# 2. Manual invalidation on update
def update_user(user_id, data):
    # Update database
    # ...
    # Invalidate cache
    cache.invalidate(f"user:{user_id}")

# 3. Cache warming (preload)
def warm_cache():
    """Preload frequently accessed data."""
    popular_users = [1, 2, 3, 4, 5]
    for user_id in popular_users:
        user_data = get_user_from_db(user_id)
        cache.set(f"user:{user_id}", user_data)

# 4. Cache-aside pattern
def get_user_cached(user_id):
    """Cache-aside: Check cache first, then database."""
    # Try cache first
    cached = cache.get(f"user:{user_id}")
    if cached:
        return cached
    
    # Cache miss: get from database
    user = get_user_from_db(user_id)
    
    # Store in cache
    cache.set(f"user:{user_id}", user)
    
    return user
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
| **OOP** | Classes, inheritance, special methods, SOLID principles |
| **Advanced** | Context managers, metaclasses, descriptors, async/await |
| **Web Development** | FastAPI, REST APIs, authentication, JWT |
| **Database** | SQLAlchemy ORM, async database operations |
| **Testing** | Pytest, unit testing, integration testing, mocking |
| **Concurrency** | Threading, asyncio, multiprocessing |
| **DevOps** | Docker, virtual environments, deployment |
| **Security** | Password hashing, JWT, API security, authentication |
| **Performance** | Caching strategies, Redis, optimization techniques |
| **Best Practices** | PEP 8, type hints, logging, error handling, design patterns |
| **Patterns** | Singleton, Factory, Observer, Strategy, Decorator |
| **Tools** | pip, poetry, regex, environment variables |

---

> **🎉 Congratulations!** You now have a complete Python reference covering all concepts from beginner to expert level. This guide prepares you for any Python interview, project, or advanced development work.