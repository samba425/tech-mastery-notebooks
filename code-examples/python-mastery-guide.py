#!/usr/bin/env python3
"""
🐍 PYTHON MASTERY GUIDE - COMPLETE REFERENCE FOR INTERVIEWS & MASTERY
===================================================================

This comprehensive guide covers all Python concepts from basics to advanced topics.
Perfect for interview preparation, skill assessment, and continuous learning.

Author: Tech Mastery Notebooks
Date: November 2025
Level: Beginner to Expert
"""

# ===============================================================
# 1. PYTHON FUNDAMENTALS - BUILDING BLOCKS
# ===============================================================
print("🔥 PYTHON FUNDAMENTALS")
print("=" * 50)

# Variables and Data Types
print("\n📊 VARIABLES AND DATA TYPES:")

# Basic data types
integer_var = 42
float_var = 3.14159
string_var = "Hello, Python!"
boolean_var = True
none_var = None

print(f"Integer: {integer_var} (type: {type(integer_var).__name__})")
print(f"Float: {float_var} (type: {type(float_var).__name__})")
print(f"String: '{string_var}' (type: {type(string_var).__name__})")
print(f"Boolean: {boolean_var} (type: {type(boolean_var).__name__})")
print(f"None: {none_var} (type: {type(none_var).__name__})")

# Type conversion examples
print(f"\nType Conversions:")
print(f"int('123'): {int('123')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(42): '{str(42)}'")
print(f"bool(1): {bool(1)}, bool(0): {bool(0)}")

# String operations
print("\n🔤 STRING OPERATIONS:")
text = "Python Programming"
print(f"Original: '{text}'")
print(f"Length: {len(text)}")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Split: {text.split()}")
print(f"Replace: '{text.replace('Python', 'Advanced Python')}'")
print(f"Find: {text.find('Programming')}")
print(f"Starts with 'Python': {text.startswith('Python')}")

# String formatting
person_name = "Alice"
person_age = 30
print(f"\n🔤 STRING FORMATTING:")
print(f"f-string: 'Hello, {person_name}! You are {person_age} years old.'")
print("format(): 'Hello, {}! You are {} years old.'".format(person_name, person_age))
print("% formatting: 'Hello, %s! You are %d years old.'" % (person_name, person_age))

# ===============================================================
# 2. DATA STRUCTURES - COLLECTIONS AND CONTAINERS
# ===============================================================
print("\n\n🔥 DATA STRUCTURES")
print("=" * 50)

# Lists - Ordered, mutable collections
print("\n📋 LISTS:")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Original list: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# List methods
fruits.append("elderberry")
print(f"After append: {fruits}")
fruits.insert(2, "coconut")
print(f"After insert: {fruits}")
removed = fruits.pop()
print(f"After pop: {fruits}, removed: {removed}")
fruits.sort()
print(f"After sort: {fruits}")

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"\nList Comprehensions:")
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# Tuples - Ordered, immutable collections
print("\n📦 TUPLES:")
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")
print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Tuple unpacking: x={coordinates[0]}, y={coordinates[1]}")
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Named tuple: {p}, x={p.x}, y={p.y}")

# Dictionaries - Key-value pairs
print("\n📚 DICTIONARIES:")
student = {
    "name": "Bob",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age', 'Unknown')}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Dictionary comprehensions
numbers_dict = {x: x**2 for x in range(1, 6)}
print(f"Dict comprehension: {numbers_dict}")

# Sets - Unique elements
print("\n🎯 SETS:")
colors = {"red", "green", "blue", "red"}  # Duplicates removed
print(f"Colors set: {colors}")

more_colors = {"blue", "yellow", "purple"}
print(f"More colors: {more_colors}")
print(f"Union: {colors | more_colors}")
print(f"Intersection: {colors & more_colors}")
print(f"Difference: {colors - more_colors}")

# ===============================================================
# 3. CONTROL FLOW - LOGIC AND LOOPS
# ===============================================================
print("\n\n🔥 CONTROL FLOW")
print("=" * 50)

# Conditional statements
print("\n🚦 CONDITIONAL STATEMENTS:")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Ternary operator
status = "Pass" if score >= 60 else "Fail"
print(f"Status: {status}")

# Loops
print("\n🔄 LOOPS:")

# For loops
print("For loop with range:")
for i in range(5):
    print(f"  Iteration {i}")

print("For loop with list:")
for fruit in ["apple", "banana", "cherry"]:
    print(f"  Fruit: {fruit}")

print("For loop with enumerate:")
for index, fruit in enumerate(["apple", "banana", "cherry"]):
    print(f"  {index}: {fruit}")

print("For loop with zip:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age_val in zip(names, ages):
    print(f"  {name} is {age_val} years old")

# While loops
print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1

# Loop control
print("\nLoop control (break and continue):")
for i in range(10):
    if i == 3:
        continue  # Skip iteration
    if i == 7:
        break     # Exit loop
    print(f"  Number: {i}")

# ===============================================================
# 4. FUNCTIONS - REUSABLE CODE BLOCKS
# ===============================================================
print("\n\n🔥 FUNCTIONS")
print("=" * 50)

# Basic functions
def greet(name, greeting="Hello"):
    """Simple greeting function with default parameter."""
    return f"{greeting}, {name}!"

print(f"Function call: {greet('Alice')}")
print(f"With custom greeting: {greet('Bob', 'Hi')}")

# Functions with multiple return values
def calculate_stats(numbers):
    """Calculate basic statistics for a list of numbers."""
    if not numbers:
        return 0, 0, 0
    
    total = sum(numbers)
    avg = total / len(numbers)
    maximum = max(numbers)
    
    return total, avg, maximum

nums = [1, 2, 3, 4, 5]
total, average, max_val = calculate_stats(nums)
print(f"\nStats for {nums}:")
print(f"Total: {total}, Average: {average:.2f}, Max: {max_val}")

# Variable arguments
def flexible_function(*args, **kwargs):
    """Function that accepts any number of arguments."""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function(1, 2, 3, name="Alice", years=30)

# Lambda functions
square = lambda x: x**2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nLambda examples:")
print(f"Squared: {squared}")
print(f"Even numbers: {filtered}")

# Higher-order functions
def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list."""
    return [operation(num) for num in numbers]

doubled = apply_operation([1, 2, 3], lambda x: x * 2)
print(f"Doubled: {doubled}")

# ===============================================================
# 5. OBJECT-ORIENTED PROGRAMMING - CLASSES AND OBJECTS
# ===============================================================
print("\n\n🔥 OBJECT-ORIENTED PROGRAMMING")
print("=" * 50)

# Basic class definition
class Person:
    """A simple Person class demonstrating OOP concepts."""
    
    # Class variable
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Initialize a Person instance."""
        self.name = name        # Instance variable
        self.age = age         # Instance variable
        self._id = id(self)    # Private-ish variable
    
    def introduce(self):
        """Instance method."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Method that modifies instance state."""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."
    
    @classmethod
    def get_species(cls):
        """Class method."""
        return cls.species
    
    @staticmethod
    def is_adult(age):
        """Static method."""
        return age >= 18
    
    def __str__(self):
        """String representation."""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Person('{self.name}', {self.age})"

# Using the class
print("\n👤 PERSON CLASS DEMO:")
alice = Person("Alice", 25)
bob = Person("Bob", 17)

print(f"Alice: {alice}")
print(f"Alice introduction: {alice.introduce()}")
print(f"Alice birthday: {alice.have_birthday()}")
print(f"Species: {Person.get_species()}")
print(f"Is Alice adult? {Person.is_adult(alice.age)}")
print(f"Is Bob adult? {Person.is_adult(bob.age)}")

# Inheritance
class Student(Person):
    """Student class inheriting from Person."""
    
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record."""
        self.grades.append(grade)
    
    def get_gpa(self):
        """Calculate GPA."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def introduce(self):
        """Override parent method."""
        base_intro = super().introduce()
        return f"{base_intro} I'm studying {self.major}."

print("\n🎓 INHERITANCE DEMO:")
charlie = Student("Charlie", 20, "S12345", "Computer Science")
charlie.add_grade(3.7)
charlie.add_grade(3.9)
charlie.add_grade(3.5)

print(f"Charlie: {charlie.introduce()}")
print(f"Charlie's GPA: {charlie.get_gpa():.2f}")

# Multiple inheritance and mixins
class Printable:
    """Mixin for printable functionality."""
    
    def print_info(self):
        """Print object information."""
        print(f"Object info: {self}")

class Employee(Person, Printable):
    """Employee class with multiple inheritance."""
    
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def get_annual_salary(self):
        return self.salary * 12

print("\n💼 MULTIPLE INHERITANCE DEMO:")
dave = Employee("Dave", 35, "E67890", 5000)
print(f"Dave's annual salary: ${dave.get_annual_salary():,}")
dave.print_info()

# ===============================================================
# 6. ERROR HANDLING - EXCEPTIONS AND DEBUGGING
# ===============================================================
print("\n\n🔥 ERROR HANDLING")
print("=" * 50)

# Basic exception handling
def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types!"
    except Exception as e:
        return f"Unexpected error: {e}"
    finally:
        print("  Division operation completed.")

print("\n⚠️ EXCEPTION HANDLING DEMO:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# Custom exceptions
class ValidationError(Exception):
    """Custom exception for validation errors."""
    
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

def validate_age(age):
    """Validate age with custom exception."""
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "TYPE_ERROR")
    if age < 0:
        raise ValidationError("Age cannot be negative", "VALUE_ERROR")
    if age > 150:
        raise ValidationError("Age seems unrealistic", "RANGE_ERROR")
    return True

print("\n🔍 CUSTOM EXCEPTIONS:")
try:
    validate_age(25)
    print("Age 25: Valid")
    validate_age(-5)
except ValidationError as e:
    print(f"Validation error: {e} (Code: {e.code})")

# Context managers
class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Using context manager would require actual file operations
print("\nContext managers ensure proper resource cleanup!")

# ===============================================================
# 7. ADVANCED FEATURES - DECORATORS, GENERATORS, AND MORE
# ===============================================================
print("\n\n🔥 ADVANCED FEATURES")
print("=" * 50)

# Decorators
def timing_decorator(func):
    """Decorator to measure function execution time."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start) * 1000:.2f} ms")
        return result
    return wrapper

def cache_decorator(func):
    """Simple caching decorator."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"Cache miss for {args}, result cached")
        return result
    return wrapper

@timing_decorator
@cache_decorator
def fibonacci(n):
    """Calculate fibonacci number with caching."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n⚡ DECORATORS DEMO:")
print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(10) again: {fibonacci(10)}")

# Generators
def fibonacci_generator(limit):
    """Generator for fibonacci sequence."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("\n🔄 GENERATORS DEMO:")
fib_gen = fibonacci_generator(10)
fib_sequence = list(fib_gen)
print(f"Fibonacci sequence: {fib_sequence}")

# Generator expression
squares_gen = (x**2 for x in range(10))
even_squares = [x for x in squares_gen if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Iterators
class CountUp:
    """Custom iterator class."""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

print("\n🔢 CUSTOM ITERATOR:")
counter = CountUp(1, 5)
for num in counter:
    print(f"Count: {num}")

# ===============================================================
# 8. MODULES AND PACKAGES - CODE ORGANIZATION
# ===============================================================
print("\n\n🔥 MODULES AND PACKAGES")
print("=" * 50)

# Standard library modules
import math
import random
import datetime
from collections import defaultdict, Counter
import json

print("\n📦 STANDARD LIBRARY DEMO:")

# Math module
print(f"Math constants: π = {math.pi:.4f}, e = {math.e:.4f}")
print(f"Math functions: sqrt(16) = {math.sqrt(16)}, sin(π/2) = {math.sin(math.pi/2):.1f}")

# Random module
random.seed(42)  # For reproducible results
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
print(f"Random sample: {random.sample(range(1, 11), 3)}")

# Datetime module
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Tomorrow: {(now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')}")

# Collections
word_count = Counter("hello world")
print(f"Character count: {dict(word_count)}")

grouped_data = defaultdict(list)
for name, category in [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit")]:
    grouped_data[category].append(name)
print(f"Grouped data: {dict(grouped_data)}")

# JSON handling
data = {"name": "Alice", "age": 30, "skills": ["Python", "ML", "Data Science"]}
json_string = json.dumps(data, indent=2)
print(f"JSON serialization:\n{json_string}")

parsed_data = json.loads(json_string)
print(f"JSON parsing: {parsed_data}")

# ===============================================================
# 9. FILE OPERATIONS - READING AND WRITING DATA
# ===============================================================
print("\n\n🔥 FILE OPERATIONS")
print("=" * 50)

# File operations (simulated)
print("\n📁 FILE OPERATIONS CONCEPTS:")
print("Reading files:")
print("  with open('file.txt', 'r') as f:")
print("      content = f.read()  # Read entire file")
print("      lines = f.readlines()  # Read all lines")
print("      for line in f:  # Iterate line by line")

print("\nWriting files:")
print("  with open('file.txt', 'w') as f:")
print("      f.write('Hello, World!')  # Write string")
print("      f.writelines(['line1\\n', 'line2\\n'])  # Write multiple lines")

print("\nFile modes:")
modes = {
    'r': 'Read only (default)',
    'w': 'Write (overwrites existing)',
    'a': 'Append',
    'r+': 'Read and write',
    'x': 'Exclusive creation',
    'b': 'Binary mode (add to other modes)',
    't': 'Text mode (default)'
}
for mode, description in modes.items():
    print(f"  '{mode}': {description}")

# ===============================================================
# 10. ALGORITHM IMPLEMENTATIONS - COMMON PATTERNS
# ===============================================================
print("\n\n🔥 ALGORITHM IMPLEMENTATIONS")
print("=" * 50)

# Sorting algorithms
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

# Search algorithms
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
    
    return -1

print("\n🔍 ALGORITHMS DEMO:")
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted_list}")
print(f"Bubble sort: {bubble_sort(unsorted_list.copy())}")
print(f"Quick sort: {quick_sort(unsorted_list.copy())}")

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(sorted_list, target)
print(f"Binary search for {target} in {sorted_list}: index {result}")

# Dynamic programming
def fibonacci_dp(n, memo={}):
    """Fibonacci with memoization."""
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)
    return memo[n]

print(f"Fibonacci(20) with DP: {fibonacci_dp(20)}")

# ===============================================================
# 11. BEST PRACTICES AND PATTERNS
# ===============================================================
print("\n\n🔥 BEST PRACTICES AND PATTERNS")
print("=" * 50)

# Design patterns
class Singleton:
    """Singleton pattern implementation."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

print("\n🏗️ DESIGN PATTERNS:")
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")

# Context manager pattern
from contextlib import contextmanager

@contextmanager
def timer_context():
    """Context manager for timing code execution."""
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution time: {(end - start) * 1000:.2f} ms")

print("\n⏱️ CONTEXT MANAGER PATTERN:")
with timer_context():
    # Simulate some work
    sum(range(100000))
    print("Computation completed")

# ===============================================================
# 12. TESTING AND DEBUGGING
# ===============================================================
print("\n\n🔥 TESTING AND DEBUGGING")
print("=" * 50)

# Unit testing concepts
def add_numbers(a, b):
    """Simple function to demonstrate testing."""
    return a + b

def divide_numbers(a, b):
    """Division function with error handling."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("\n🧪 TESTING CONCEPTS:")
print("Unit test structure:")
print("  import unittest")
print("  ")
print("  class TestMathFunctions(unittest.TestCase):")
print("      def test_add_positive_numbers(self):")
print("          self.assertEqual(add_numbers(2, 3), 5)")
print("      ")
print("      def test_divide_by_zero(self):")
print("          with self.assertRaises(ValueError):")
print("              divide_numbers(5, 0)")

# Debugging techniques
print("\n🐛 DEBUGGING TECHNIQUES:")
debugging_tips = [
    "Use print() statements for simple debugging",
    "Use logging module for production debugging",
    "Use pdb (Python Debugger) for interactive debugging",
    "Use assert statements for development checks",
    "Use try-except blocks to catch and handle errors",
    "Use IDE debugger for step-by-step execution",
    "Write unit tests to catch bugs early"
]

for i, tip in enumerate(debugging_tips, 1):
    print(f"  {i}. {tip}")

# ===============================================================
# 13. CONCURRENCY AND PARALLEL PROCESSING
# ===============================================================
print("\n\n🔥 CONCURRENCY AND PARALLEL PROCESSING")
print("=" * 50)

import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threading
print("\n🧵 THREADING:")

def worker_function(name, duration):
    """Simulate work in a thread."""
    print(f"  Worker {name} starting...")
    time.sleep(duration)
    print(f"  Worker {name} finished after {duration}s")
    return f"Result from {name}"

def threading_demo():
    """Demonstrate threading."""
    print("Threading example:")
    threads = []
    
    # Create and start threads
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
    
    print("All threads completed!")

threading_demo()

# Thread-safe operations
print("\n🔒 THREAD-SAFE OPERATIONS:")

class ThreadSafeCounter:
    """Thread-safe counter using locks."""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value

# Asyncio
print("\n⚡ ASYNCIO (ASYNC/AWAIT):")

async def async_task(name, delay):
    """Async task simulation."""
    print(f"  Async task {name} starting...")
    await asyncio.sleep(delay)
    print(f"  Async task {name} completed after {delay}s")
    return f"Result from {name}"

async def asyncio_demo():
    """Demonstrate asyncio."""
    print("Asyncio example:")
    
    # Run tasks concurrently
    tasks = [
        async_task("Task-1", 1),
        async_task("Task-2", 2),
        async_task("Task-3", 1.5)
    ]
    
    results = await asyncio.gather(*tasks)
    print(f"All async tasks completed: {results}")

# Run asyncio demo
print("Running async demo...")
try:
    asyncio.run(asyncio_demo())
except RuntimeError:
    print("Asyncio demo completed (runtime environment limitation)")

# Multiprocessing concepts
print("\n🚀 MULTIPROCESSING CONCEPTS:")

def cpu_intensive_task(n):
    """CPU-intensive task for multiprocessing."""
    total = 0
    for i in range(n * 1000000):
        total += i * i
    return total

def multiprocessing_demo():
    """Demonstrate multiprocessing concepts."""
    print("Multiprocessing example (concept):")
    print("  # Create processes")
    print("  processes = []")
    print("  for i in range(4):")
    print("      p = multiprocessing.Process(target=cpu_intensive_task, args=(100,))")
    print("      processes.append(p)")
    print("      p.start()")
    print("  ")
    print("  # Wait for completion")
    print("  for p in processes:")
    print("      p.join()")

multiprocessing_demo()

# Concurrent.futures
print("\n🎯 CONCURRENT.FUTURES:")

def demonstrate_executors():
    """Demonstrate ThreadPoolExecutor and ProcessPoolExecutor."""
    print("Executor patterns:")
    
    # ThreadPoolExecutor example
    print("  # ThreadPoolExecutor")
    print("  with ThreadPoolExecutor(max_workers=4) as executor:")
    print("      futures = [executor.submit(worker_function, f'Worker-{i}', 1) for i in range(4)]")
    print("      results = [future.result() for future in futures]")
    
    # ProcessPoolExecutor example  
    print("  ")
    print("  # ProcessPoolExecutor")
    print("  with ProcessPoolExecutor(max_workers=4) as executor:")
    print("      futures = [executor.submit(cpu_intensive_task, 100) for _ in range(4)]")
    print("      results = [future.result() for future in futures]")

demonstrate_executors()

# ===============================================================
# 14. DATA SCIENCE FOUNDATIONS
# ===============================================================
print("\n\n🔥 DATA SCIENCE FOUNDATIONS")
print("=" * 50)

# NumPy concepts
print("\n🔢 NUMPY FUNDAMENTALS:")

numpy_concepts = """
import numpy as np

# Array creation
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
random_array = np.random.rand(3, 3)

# Array operations
result = arr * 2
dot_product = np.dot(matrix, matrix)
element_wise = matrix * matrix

# Mathematical functions
sqrt_arr = np.sqrt(arr)
mean_val = np.mean(arr)
std_val = np.std(arr)

# Array slicing and indexing
subset = arr[1:4]
matrix_row = matrix[0, :]
matrix_col = matrix[:, 1]

# Broadcasting
broadcast_result = arr + 10
"""

print(numpy_concepts)

# Pandas concepts
print("\n📊 PANDAS FUNDAMENTALS:")

pandas_concepts = """
import pandas as pd

# DataFrame creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Data exploration
print(df.head())
print(df.info())
print(df.describe())

# Data selection
names = df['Name']
adults = df[df['Age'] > 25]
subset = df.loc[0:1, ['Name', 'Age']]

# Data manipulation
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
grouped = df.groupby('City')['Age'].mean()
sorted_df = df.sort_values('Age', ascending=False)

# Data cleaning
df_clean = df.dropna()
df_filled = df.fillna(0)

# File operations
df.to_csv('data.csv', index=False)
loaded_df = pd.read_csv('data.csv')
"""

print(pandas_concepts)

# Data visualization concepts
print("\n📈 DATA VISUALIZATION:")

visualization_concepts = """
import matplotlib.pyplot as plt
import seaborn as sns

# Basic plotting
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# Multiple plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot([1, 2, 3], [1, 4, 2])
axes[0, 1].bar(['A', 'B', 'C'], [1, 3, 2])
axes[1, 0].hist([1, 2, 2, 3, 3, 3], bins=3)
axes[1, 1].scatter([1, 2, 3], [1, 4, 2])

# Seaborn for statistical plots
sns.boxplot(data=df, x='City', y='Age')
sns.heatmap(correlation_matrix, annot=True)
sns.pairplot(df)
"""

print(visualization_concepts)

# ===============================================================
# 15. WEB DEVELOPMENT WITH PYTHON
# ===============================================================
print("\n\n🔥 WEB DEVELOPMENT WITH PYTHON")
print("=" * 50)

# Flask fundamentals
print("\n🌶️ FLASK FUNDAMENTALS:")

flask_concepts = """
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return '<h1>Welcome to Flask!</h1>'

# Route with parameters
@app.route('/user/<name>')
def user_profile(name):
    return f'<h1>Hello, {name}!</h1>'

# HTTP methods
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return jsonify({'message': 'Data retrieved'})
    elif request.method == 'POST':
        data = request.json
        return jsonify({'received': data})

# Template rendering
@app.route('/dashboard')
def dashboard():
    user_data = {'name': 'Alice', 'score': 95}
    return render_template('dashboard.html', user=user_data)

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Database integration (conceptual)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
"""

print(flask_concepts)

# Django fundamentals
print("\n🎯 DJANGO FUNDAMENTALS:")

django_concepts = """
# Django project structure
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        urls.py

# Models (models.py)
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

# Views (views.py)
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html', {'title': 'Django App'})

@csrf_exempt
def api_users(request):
    if request.method == 'GET':
        users = User.objects.all().values()
        return JsonResponse({'users': list(users)})

# URLs (urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/users/', views.api_users, name='api_users'),
]

# Settings configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Commands
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser
"""

print(django_concepts)

# REST API concepts
print("\n🔌 REST API CONCEPTS:")

rest_api_concepts = """
# RESTful API design principles
GET    /api/users/        # Get all users
GET    /api/users/123/    # Get specific user
POST   /api/users/        # Create new user
PUT    /api/users/123/    # Update user
DELETE /api/users/123/    # Delete user

# Status codes
200 OK                    # Success
201 Created              # Resource created
400 Bad Request          # Client error
401 Unauthorized         # Authentication required
404 Not Found           # Resource not found
500 Internal Server Error # Server error

# Django REST Framework example
from rest_framework import serializers, viewsets
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

print(rest_api_concepts)

# ===============================================================
# 16. TESTING AND QUALITY ASSURANCE
# ===============================================================
print("\n\n🔥 TESTING AND QUALITY ASSURANCE")
print("=" * 50)

# Unit testing with unittest
print("\n🧪 UNIT TESTING:")

unittest_example = """
import unittest
from unittest.mock import patch, MagicMock

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def fetch_data(self):
        # Simulates external API call
        import requests
        response = requests.get('https://api.example.com/data')
        return response.json()

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_divide_normal(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Mock external API call
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': 'test'}
        mock_get.return_value = mock_response
        
        result = self.calc.fetch_data()
        self.assertEqual(result, {'data': 'test'})
        mock_get.assert_called_once_with('https://api.example.com/data')

if __name__ == '__main__':
    unittest.main()
"""

print(unittest_example)

# Pytest concepts
print("\n⚡ PYTEST CONCEPTS:")

pytest_example = """
# test_calculator.py
import pytest
from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError):
            calc.divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        assert calc.add(a, b) == expected
    
    @pytest.fixture(scope="module")
    def database():
        # Setup expensive resource
        db = create_test_database()
        yield db
        # Cleanup
        db.close()

# Running tests
# pytest test_calculator.py
# pytest -v  # verbose output
# pytest --cov=calculator  # coverage report
# pytest -x  # stop on first failure
"""

print(pytest_example)

# Code quality tools
print("\n📏 CODE QUALITY TOOLS:")

quality_tools = """
# Linting with flake8
flake8 myfile.py
# E302 expected 2 blank lines, found 1
# W291 trailing whitespace

# Type checking with mypy
from typing import List, Optional

def process_items(items: List[str]) -> Optional[str]:
    if not items:
        return None
    return items[0].upper()

# Running mypy
# mypy myfile.py

# Code formatting with black
# black myfile.py

# Import sorting with isort
# isort myfile.py

# Security checking with bandit
# bandit -r myproject/

# Pre-commit hooks (.pre-commit-config.yaml)
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
"""

print(quality_tools)

# ===============================================================
# 17. ADVANCED PYTHON FEATURES
# ===============================================================
print("\n\n🔥 ADVANCED PYTHON FEATURES")
print("=" * 50)

# Metaclasses
print("\n🧬 METACLASSES:")

metaclass_example = """
class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Modify class creation
        attrs['class_id'] = f"ID_{name}_{id(cls)}"
        return super().__new__(cls, name, bases, attrs)
    
    def __call__(cls, *args, **kwargs):
        # Modify instance creation
        instance = super().__call__(*args, **kwargs)
        print(f"Created instance of {cls.__name__}")
        return instance

class MyClass(metaclass=MetaClass):
    def __init__(self, value):
        self.value = value

# Usage
obj = MyClass(42)
print(obj.class_id)  # ID_MyClass_...
"""

print(metaclass_example)

# Descriptors
print("\n🎛️ DESCRIPTORS:")

descriptor_example = """
class ValidatedAttribute:
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Person:
    age = ValidatedAttribute('age', lambda x: isinstance(x, int) and x >= 0)
    name = ValidatedAttribute('name', lambda x: isinstance(x, str) and len(x) > 0)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 25)
# person.age = -5  # Would raise ValueError
"""

print(descriptor_example)

# Context managers
print("\n🔧 ADVANCED CONTEXT MANAGERS:")

context_manager_example = """
from contextlib import contextmanager
import sqlite3

@contextmanager
def database_transaction(db_path):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# Usage
with database_transaction('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

# Class-based context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions
"""

print(context_manager_example)

# ===============================================================
# PYTHON MASTERY SUMMARY
# ===============================================================
print("\n" + "=" * 60)
print("🏆 PYTHON MASTERY SUMMARY")
print("=" * 60)

python_concepts = {
    "Fundamentals": [
        "Variables and data types",
        "String operations and formatting",
        "Type conversion and checking"
    ],
    "Data Structures": [
        "Lists, tuples, dictionaries, sets",
        "List/dict/set comprehensions",
        "Collections module (Counter, defaultdict)"
    ],
    "Control Flow": [
        "Conditional statements (if/elif/else)",
        "Loops (for/while) and loop control",
        "Iteration techniques (enumerate, zip)"
    ],
    "Functions": [
        "Function definition and parameters",
        "Lambda functions and higher-order functions",
        "Variable arguments (*args, **kwargs)"
    ],
    "OOP": [
        "Classes, objects, and inheritance",
        "Method types (instance, class, static)",
        "Special methods (__str__, __repr__, etc.)"
    ],
    "Advanced": [
        "Decorators and generators",
        "Context managers and iterators",
        "Error handling and custom exceptions"
    ],
    "Modules": [
        "Standard library usage",
        "Import statements and packages",
        "File operations and JSON handling"
    ],
    "Algorithms": [
        "Sorting and searching algorithms",
        "Dynamic programming concepts",
        "Algorithm complexity analysis"
    ],
    "Concurrency": [
        "Threading and multiprocessing",
        "Asyncio and async/await patterns",
        "Thread-safe operations and locks"
    ],
    "Data Science": [
        "NumPy fundamentals and operations",
        "Pandas DataFrame manipulation",
        "Data visualization with matplotlib/seaborn"
    ],
    "Web Development": [
        "Flask framework basics",
        "Django MVC architecture",
        "REST API design and implementation"
    ],
    "Testing": [
        "Unit testing with unittest and pytest",
        "Mocking and test fixtures",
        "Code quality tools (flake8, mypy, black)"
    ],
    "Advanced Features": [
        "Metaclasses and descriptors",
        "Advanced context managers",
        "Memory management and optimization"
    ],
    "Best Practices": [
        "Design patterns (Singleton, Factory)",
        "Code organization and structure",
        "Performance optimization techniques"
    ]
}

print("\n📚 TOPICS MASTERED:")
for category, topics in python_concepts.items():
    print(f"\n✅ {category}:")
    for topic in topics:
        print(f"    - {topic}")

print("\n💼 INTERVIEW READINESS:")
interview_topics = [
    "Data structure operations and time complexity",
    "Algorithm implementation from scratch", 
    "Object-oriented programming principles",
    "Error handling and edge cases",
    "Code optimization and best practices",
    "Design patterns and software architecture",
    "Testing strategies and debugging skills"
]

for topic in interview_topics:
    print(f"🎯 {topic}")

# ===============================================================
# 13. DATA SCIENCE FUNDAMENTALS - NUMPY AND PANDAS
# ===============================================================
print("\n\n🔥 DATA SCIENCE WITH PYTHON")
print("=" * 50)

# NumPy fundamentals
try:
    import numpy as np
    
    print("\n📊 NUMPY FUNDAMENTALS:")
    
    # Array creation
    arr = np.array([1, 2, 3, 4, 5])
    matrix = np.array([[1, 2], [3, 4], [5, 6]])
    
    print(f"1D Array: {arr}")
    print(f"2D Matrix:\n{matrix}")
    print(f"Array shape: {arr.shape}, Matrix shape: {matrix.shape}")
    
    # Mathematical operations
    print(f"Square: {arr ** 2}")
    print(f"Sum: {np.sum(arr)}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Standard deviation: {np.std(arr):.2f}")
    
    # Array manipulation
    reshaped = arr.reshape(-1, 1)
    print(f"Reshaped to column vector:\n{reshaped}")
    
    # Linear algebra
    dot_product = np.dot(arr, arr)
    print(f"Dot product with itself: {dot_product}")
    
except ImportError:
    print("📊 NumPy not installed. Install with: pip install numpy")

# Pandas fundamentals
try:
    import pandas as pd
    
    print("\n📈 PANDAS FUNDAMENTALS:")
    
    # DataFrame creation
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 28],
        'salary': [50000, 60000, 70000, 55000],
        'department': ['Engineering', 'Marketing', 'Engineering', 'Sales']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # Data selection and filtering
    print(f"\nAges column:\n{df['age']}")
    print(f"\nEngineering employees:\n{df[df['department'] == 'Engineering']}")
    print(f"\nHigh earners (>55k):\n{df[df['salary'] > 55000]}")
    
    # Grouping and aggregation
    dept_stats = df.groupby('department').agg({
        'salary': ['mean', 'max'],
        'age': 'mean'
    })
    print(f"\nDepartment statistics:\n{dept_stats}")
    
    # Data manipulation
    df_sorted = df.sort_values('salary', ascending=False)
    print(f"\nSorted by salary:\n{df_sorted}")
    
except ImportError:
    print("📈 Pandas not installed. Install with: pip install pandas")

# ===============================================================
# 14. WEB DEVELOPMENT BASICS - FLASK AND APIs
# ===============================================================
print("\n\n🔥 WEB DEVELOPMENT WITH PYTHON")
print("=" * 50)

print("\n🌐 FLASK WEB FRAMEWORK:")

# Flask application structure
flask_app_code = '''
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Python Web Development!"

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        # Return all users
        users = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
        return jsonify({"users": users})
    
    elif request.method == 'POST':
        # Create new user
        user_data = request.get_json()
        new_user = {
            "id": 3,
            "name": user_data.get('name'),
            "email": user_data.get('email')
        }
        return jsonify({"message": "User created", "user": new_user}), 201

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    # Get specific user
    user = {"id": user_id, "name": "Sample User", "email": "user@example.com"}
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
'''

print("Flask application structure:")
print(flask_app_code)

# Database integration concepts
print("\n💾 DATABASE INTEGRATION:")

db_integration_code = '''
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
'''

print("Database manager class:")
print(db_integration_code)

# ===============================================================
# 15. TESTING AND CODE QUALITY
# ===============================================================
print("\n\n🔥 TESTING AND CODE QUALITY")
print("=" * 50)

print("\n🧪 UNIT TESTING WITH UNITTEST:")

unittest_example = '''
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
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)
    
    def test_divide_success(self):
        """Test successful division."""
        result = self.calc.divide(10, 2)
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
'''

print("Complete unittest example:")
print(unittest_example)

print("\n� PYTEST FUNDAMENTALS:")

pytest_example = '''
import pytest
from unittest.mock import Mock

# Pytest fixtures
@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def calculator():
    """Fixture providing calculator instance."""
    return Calculator()

# Pytest test functions
def test_list_operations(sample_data):
    """Test basic list operations."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15
    assert max(sample_data) == 5

def test_calculator_add(calculator):
    """Test calculator addition."""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_calculator_divide_by_zero(calculator):
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

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
'''

print("Pytest example with fixtures and parametrization:")
print(pytest_example)

# ===============================================================
# 16. ADVANCED PYTHON FEATURES
# ===============================================================
print("\n\n🔥 ADVANCED PYTHON FEATURES")
print("=" * 50)

print("\n🎭 METACLASSES:")

# Metaclass example
metaclass_example = '''
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
'''

print("Singleton metaclass example:")
print(metaclass_example)

print("\n🔧 DESCRIPTORS:")

# Descriptor example
descriptor_example = '''
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
'''

print("Descriptor for data validation:")
print(descriptor_example)

print("\n🎯 CONTEXT MANAGERS:")

# Context manager example
context_manager_example = '''
import time
from contextlib import contextmanager

class Timer:
    """Context manager for timing code execution."""
    
    def __init__(self, name="Operation"):
        self.name = name
    
    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"{self.name} completed in {duration:.4f} seconds")
        
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

@contextmanager
def file_manager(filename, mode):
    """Generator-based context manager."""
    print(f"Opening {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        file.close()

# Usage
with Timer("Data processing"):
    time.sleep(0.1)  # Simulate work
'''

print("Context manager for timing:")
print(context_manager_example)

print("\n�🚀 NEXT STEPS:")
next_steps = [
    "Practice coding challenges on LeetCode/HackerRank",
    "Build projects using web frameworks (Django/Flask)",
    "Learn data science libraries (pandas, numpy, sklearn)",
    "Explore async programming with asyncio",
    "Study system design and scalability patterns",
    "Contribute to open-source Python projects",
    "Master testing frameworks and TDD practices",
    "Learn advanced features like metaclasses and descriptors",
    "Practice with real-world project architectures",
    "Explore performance optimization techniques"
]

for step in next_steps:
    print(f"📈 {step}")

print("\n" + "=" * 60)
print("🎉 COMPLETE PYTHON MASTERY ACHIEVED!")
print("💪 Ready for Senior/Lead Python Developer roles!")
print("🏆 Interview-ready with 15+ years of concepts covered!")
print("=" * 60)