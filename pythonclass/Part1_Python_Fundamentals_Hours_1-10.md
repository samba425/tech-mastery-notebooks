# Part 1: Python Fundamentals & Core Programming
## Hours 1-10 (Backend Foundation)

**Duration:** 10 hours total  
**Target:** Complete beginners  
**Format:** 1 hour per session  
**Style:** Read and teach directly, copy-paste examples for students

---

## 📚 TABLE OF CONTENTS

- [Hour 1: Python Intro & Environment](#hour-1)
- [Hour 2: Variables, Types, Operators](#hour-2)
- [Hour 3: Flow Control](#hour-3)
- [Hour 4: Loops & Comprehensions](#hour-4)
- [Hour 5: Functions & Scoping](#hour-5)
- [Hour 6: Data Structures - Lists & Tuples](#hour-6)
- [Hour 7: Data Structures - Dicts & Sets](#hour-7)
- [Hour 8: File I/O & Exceptions](#hour-8)
- [Hour 9: Modules, Packages & Virtualenvs](#hour-9)
- [Hour 10: Debugging & Testing Basics](#hour-10)

---

<a name="hour-1"></a>
## 📅 Hour 1: Python Intro & Environment

### 🎯 Learning Objectives
- Understand Python ecosystem
- Install Python correctly
- Create virtual environments
- Run Python scripts
- Use REPL and VS Code

### 📖 What to Teach (Read This to Students)

**"Today we'll set up Python on your computer. Think of this like installing a new app - we need the right tools before we start cooking!"**

---

### 1️⃣ What is Python Ecosystem? (10 minutes)

**Explain:**

"Python ecosystem is like a complete kitchen:
- **Python (language)** = The oven/stove (main tool)
- **pip (package manager)** = Grocery store (get ingredients/libraries)
- **Virtual environment** = Your own personal kitchen (isolated workspace)
- **Libraries/Packages** = Recipe ingredients (pre-made code)
- **IDE (VS Code)** = Kitchen counter (where you work)"

**Show this diagram on board:**
```
Python Ecosystem
├── Python Interpreter (runs your code)
├── pip (installs packages)
├── venv (creates isolated environments)
├── Standard Library (built-in tools)
└── Third-party packages (extra tools from community)
```

---

### 2️⃣ Installing Python (15 minutes)

**Step-by-step (show on screen):**

```bash
# Step 1: Check if Python is already installed
python3 --version
# or
python --version

# Expected output:
# Python 3.12.0 (or similar)
```

**If not installed:**

**For macOS:**
```bash
# Using Homebrew (recommended)
brew install python3
```

**For Windows:**
1. Go to python.org
2. Download latest Python 3.x
3. ✅ **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"

**For Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Verify installation:**
```bash
python3 --version
pip3 --version
```

---

### 3️⃣ Create Virtual Environment (15 minutes)

**Explain to Students:**

"Virtual environment is like having a separate kitchen for each recipe. Your mom's kitchen ingredients won't mix with your cooking experiments!"

**Why Virtual Environments?**
- Different projects need different versions of packages
- Avoid conflicts between projects
- Clean and organized
- Easy to share project requirements

**Demo - Create venv:**

```bash
# Create a project folder
mkdir my_python_project
cd my_python_project

# Create virtual environment named 'venv'
python3 -m venv venv

# Your folder now looks like:
# my_python_project/
#   └── venv/  (isolated Python environment)
```

**Activate Virtual Environment:**

**macOS/Linux:**
```bash
source venv/bin/activate

# You'll see (venv) in your terminal:
# (venv) username@computer:~/my_python_project$
```

**Windows:**
```bash
venv\Scripts\activate

# You'll see:
# (venv) C:\Users\username\my_python_project>
```

**Deactivate (when done):**
```bash
deactivate
```

---

### 4️⃣ First Python Script (10 minutes)

**Create hello.py file:**

```python
# hello.py - My first Python program

print("Hello, World!")
print("Welcome to Python programming!")

# Get user input
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

# Do some math
age = int(input("How old are you? "))
print(f"In 10 years, you'll be {age + 10} years old!")
```

**Run the script:**

```bash
# Make sure venv is activated
python hello.py

# Or explicitly use python3
python3 hello.py
```

**Expected interaction:**
```
Hello, World!
Welcome to Python programming!
What's your name? John
Nice to meet you, John!
How old are you? 25
In 10 years, you'll be 35 years old!
```

---

### 5️⃣ Python REPL (Interactive Mode) (5 minutes)

**Explain:**

"REPL = Read-Eval-Print-Loop. It's like having a conversation with Python - ask a question, get an answer immediately!"

**Open REPL:**
```bash
python3
# or just
python
```

**Try these in REPL:**
```python
>>> 2 + 2
4

>>> print("Hello")
Hello

>>> name = "Python"
>>> name
'Python'

>>> 5 * 10
50

>>> exit()  # To quit REPL
```

**REPL is great for:**
- Quick calculations
- Testing small code snippets
- Learning syntax
- Debugging

---

### 6️⃣ VS Code Setup (5 minutes)

**Install VS Code:**
1. Download from code.visualstudio.com
2. Install Python extension (by Microsoft)

**Open project in VS Code:**
```bash
code .
# Opens current folder in VS Code
```

**Run Python in VS Code:**
1. Open hello.py
2. Click "Run Python File" (▶️ button top-right)
3. Or press: Ctrl+Alt+N (Windows) / Cmd+Option+N (Mac)

**VS Code Features to Show:**
- Syntax highlighting (colors!)
- Auto-completion
- Error detection
- Terminal integration

---

### 💻 Live Activity (Copy-Paste for Students)

**Activity: Create and Run Your First Script**

```python
# activity1_greeting.py

print("=" * 50)
print("WELCOME TO PYTHON PROGRAMMING")
print("=" * 50)

# Get user information
name = input("\nEnter your name: ")
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")

# Display greeting
print("\n" + "=" * 50)
print(f"Hello {name}!")
print(f"You're from {city}")
print(f"Your hobby is {hobby}")
print("=" * 50)
print("\nHappy coding! 🐍")
```

**Students should:**
1. Create this file
2. Save as `activity1_greeting.py`
3. Run it
4. See personalized output

---

### 🏠 Homework

**Task:** Write a script that:
1. Asks for user's name
2. Asks for their favorite color
3. Asks for their age
4. Prints a personalized greeting with all info

**Template (give students this):**

```python
# homework1_greeting.py

# TODO: Get user's name
name = input("Enter your name: ")

# TODO: Get user's favorite color
# (Write code here)

# TODO: Get user's age
# (Write code here)

# TODO: Print greeting
print(f"Hello {name}!")
# (Add more print statements)
```

**Expected output:**
```
Enter your name: Alice
Enter your favorite color: Blue
Enter your age: 22

Hello Alice!
Your favorite color is Blue
You are 22 years old
Welcome to Python programming!
```

---

### 📝 Key Takeaways (Tell Students)

✅ Python is installed and working
✅ Virtual environments keep projects separate
✅ `python filename.py` runs scripts
✅ REPL is for quick testing
✅ VS Code makes coding easier

---

### 🎯 Next Hour Preview

"Next class: Variables and data types - the building blocks of programming!"

---

<a name="hour-2"></a>
## 📅 Hour 2: Variables, Types, Operators

### 🎯 Learning Objectives
- Understand variables and data types
- Work with numbers, strings, booleans
- Type conversions
- String formatting (f-strings)
- Build a simple calculator

### 📖 What to Teach

**"Today we learn about variables - think of them as labeled boxes where we store information!"**

---

### 1️⃣ Variables Basics (10 minutes)

**Explain with Real-Life Example:**

"Imagine you have boxes at home:
- Box labeled 'Keys' → stores your car keys
- Box labeled 'Money' → stores cash
- Box labeled 'Photos' → stores pictures

In Python:
- Variable named 'username' → stores name
- Variable named 'age' → stores age
- Variable named 'price' → stores price"

**Basic Variable Syntax:**

```python
# Creating variables (like labeling boxes)
name = "John"
age = 25
price = 99.99
is_student = True

# Using variables
print(name)        # John
print(age)         # 25
print(price)       # 99.99
print(is_student)  # True
```

**Variable Naming Rules:**

```python
# ✅ GOOD variable names
user_name = "Alice"
total_price = 150
first_name = "Bob"
age2 = 30

# ❌ BAD variable names (will cause errors)
# 2age = 25        # Can't start with number
# user-name = "x"  # Can't use hyphens
# first name = "y" # Can't have spaces
# class = "A"      # Can't use reserved words
```

---

### 2️⃣ Data Types (15 minutes)

**Show 4 Main Types:**

```python
# 1. Numbers (int) - whole numbers
age = 25
quantity = 100
year = 2025

# 2. Numbers (float) - decimal numbers
price = 99.99
temperature = 36.5
pi = 3.14159

# 3. Strings (str) - text
name = "Alice"
city = "Mumbai"
message = 'Hello World'  # Single or double quotes

# 4. Booleans (bool) - True/False
is_active = True
is_logged_in = False
has_permission = True
```

**Check Type:**

```python
# type() function tells you the type
age = 25
print(type(age))  # <class 'int'>

price = 99.99
print(type(price))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>

is_active = True
print(type(is_active))  # <class 'bool'>
```

---

### 3️⃣ Type Conversion (10 minutes)

**Explain:**

"Sometimes we need to convert one type to another - like converting kilograms to pounds!"

```python
# String to Integer
age_str = "25"
age_int = int(age_str)
print(age_int + 5)  # 30

# String to Float
price_str = "99.99"
price_float = float(price_str)
print(price_float * 2)  # 199.98

# Integer to String
age = 25
age_str = str(age)
print("Age: " + age_str)  # Age: 25

# Float to Integer (removes decimal)
price = 99.99
price_int = int(price)
print(price_int)  # 99 (not 100!)
```

**Common Mistake to Show:**

```python
# ❌ This causes error
age = "25"
result = age + 5  # TypeError: can only concatenate str

# ✅ Convert first
age = "25"
result = int(age) + 5  # 30 ✓
```

---

### 4️⃣ Operators (10 minutes)

**Arithmetic Operators:**

```python
# Basic math
a = 10
b = 3

print(a + b)   # 13 (Addition)
print(a - b)   # 7  (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.333... (Division)
print(a // b)  # 3  (Floor Division - no decimal)
print(a % b)   # 1  (Remainder/Modulo)
print(a ** b)  # 1000 (Power: 10^3)
```

**Comparison Operators:**

```python
age = 25

print(age == 25)  # True (equal to)
print(age != 20)  # True (not equal to)
print(age > 18)   # True (greater than)
print(age < 30)   # True (less than)
print(age >= 25)  # True (greater or equal)
print(age <= 30)  # True (less or equal)
```

**Assignment Shortcuts:**

```python
# Regular way
count = 10
count = count + 5
print(count)  # 15

# Shortcut way
count = 10
count += 5    # Same as count = count + 5
print(count)  # 15

# Other shortcuts
count -= 3    # count = count - 3
count *= 2    # count = count * 2
count /= 2    # count = count / 2
```

---

### 5️⃣ String Formatting (10 minutes)

**Old Way (Don't Use):**

```python
name = "Alice"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")
# Messy and error-prone!
```

**Modern Way - f-strings (Use This!):**

```python
name = "Alice"
age = 25
city = "Mumbai"

# f-string (f before quotes)
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city}")

# Multiple variables in one line
print(f"Hi, I'm {name}, {age} years old, from {city}")
```

**f-strings with Expressions:**

```python
price = 100
quantity = 5

print(f"Total: ₹{price * quantity}")  # Total: ₹500

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # Pi is approximately 3.14

# Calculations inside
age = 25
print(f"In 10 years, I'll be {age + 10}")  # In 10 years, I'll be 35
```

---

### 💻 Live Activity: Build a Calculator

**Copy-Paste This for Students:**

```python
# activity2_calculator.py

print("=" * 40)
print("SIMPLE CALCULATOR")
print("=" * 40)

# Get two numbers from user
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Perform all operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print("\n" + "=" * 40)
print("RESULTS:")
print("=" * 40)
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(f"{num1} ÷ {num2} = {division:.2f}")
print("=" * 40)
```

**Test with students:**
```
Enter first number: 10
Enter second number: 3

RESULTS:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 × 3.0 = 30.0
10.0 ÷ 3.0 = 3.33
```

---

### 🏠 Homework: Unit Converter (km ↔ miles)

**Give students this template:**

```python
# homework2_unit_converter.py

print("KM ↔ MILES CONVERTER")
print("=" * 40)

# Show menu
print("\n1. Kilometers to Miles")
print("2. Miles to Kilometers")

choice = input("\nEnter choice (1 or 2): ")

if choice == "1":
    # TODO: Get km from user
    km = float(input("Enter kilometers: "))
    
    # TODO: Convert to miles (1 km = 0.621371 miles)
    miles = km * 0.621371
    
    # TODO: Print result
    print(f"{km} km = {miles:.2f} miles")

elif choice == "2":
    # TODO: Get miles from user
    miles = float(input("Enter miles: "))
    
    # TODO: Convert to km (1 mile = 1.60934 km)
    km = miles * 1.60934
    
    # TODO: Print result
    print(f"{miles} miles = {km:.2f} km")

else:
    print("Invalid choice!")
```

**Expected Output:**
```
KM ↔ MILES CONVERTER
========================================

1. Kilometers to Miles
2. Miles to Kilometers

Enter choice (1 or 2): 1
Enter kilometers: 100
100.0 km = 62.14 miles
```

---

### 📝 Key Takeaways

✅ Variables store data (like labeled boxes)
✅ 4 main types: int, float, str, bool
✅ Use `int()`, `float()`, `str()` to convert
✅ f-strings make formatting easy
✅ Operators: +, -, *, /, //, %, **

---

<a name="hour-3"></a>
## 📅 Hour 3: Flow Control (If/Elif/Else)

### 🎯 Learning Objectives
- Understand conditional statements
- Use if/elif/else properly
- Learn about truthiness
- Handle short-circuiting
- Build age-based access program

### 📖 What to Teach

**"Today we learn how to make decisions in code - like a traffic light that decides when to stop or go!"**

---

### 1️⃣ If Statements Basics (15 minutes)

**Real-Life Analogy:**

"Think of an ATM machine:
- IF balance >= withdrawal amount → Give money
- IF balance < withdrawal amount → Show error"

**Basic Syntax:**

```python
# Simple if statement
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("Program continues...")
```

**Important: Indentation!**

```python
# ✅ CORRECT - indented
if age >= 18:
    print("Adult")  # This runs only if True

# ❌ WRONG - not indented
if age >= 18:
print("Adult")  # ERROR!
```

---

### 2️⃣ If-Else (10 minutes)

**Explain:**

"If-else is like a fork in the road - you go one way or the other, never both!"

```python
age = 16

if age >= 18:
    print("✅ You can vote")
else:
    print("❌ Too young to vote")
    print(f"Wait {18 - age} more years")
```

**Real-World Example - Ticket Pricing:**

```python
age = int(input("Enter your age: "))

if age < 12:
    price = 50
    print(f"Child ticket: ₹{price}")
else:
    price = 100
    print(f"Adult ticket: ₹{price}")
```

---

### 3️⃣ If-Elif-Else (Multiple Conditions) (10 minutes)

**Explain:**

"When you have more than 2 options - like choosing ice cream flavor!"

```python
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade: {grade}")
```

**Important: Order Matters!**

```python
# ✅ CORRECT - check highest first
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"

# ❌ WRONG - check lowest first
if marks >= 60:    # This catches 90 too!
    grade = "D"
elif marks >= 90:  # Never reached!
    grade = "A"
```

---

### 4️⃣ Comparison Operators (5 minutes)

```python
age = 25

# Equality
if age == 25:
    print("Exactly 25")

# Not equal
if age != 30:
    print("Not 30")

# Greater/Less
if age > 18:
    print("Adult")

if age < 65:
    print("Not senior")

# Greater/Less or equal
if age >= 25:
    print("25 or older")

if age <= 30:
    print("30 or younger")
```

---

### 5️⃣ Logical Operators (10 minutes)

**AND - Both must be True:**

```python
age = 25
has_license = True

# Both conditions must be True
if age >= 18 and has_license:
    print("✅ You can drive")
else:
    print("❌ Cannot drive")
```

**OR - At least one must be True:**

```python
day = "Saturday"

# Either condition can be True
if day == "Saturday" or day == "Sunday":
    print("It's weekend! 🎉")
else:
    print("It's a weekday 😴")
```

**NOT - Reverse the condition:**

```python
is_raining = False

if not is_raining:
    print("Go outside! ☀️")
else:
    print("Stay inside 🌧️")
```

**Combining Multiple Conditions:**

```python
age = 25
income = 50000
has_job = True

# Complex condition
if (age >= 21 and age <= 65) and (income > 30000 or has_job):
    print("✅ Loan approved")
else:
    print("❌ Loan denied")
```

---

### 6️⃣ Truthiness (5 minutes)

**What Python considers False:**

```python
# These are all "Falsy" (treated as False)
if 0:
    print("Won't print")  # 0 is False

if "":
    print("Won't print")  # Empty string is False

if None:
    print("Won't print")  # None is False

if []:
    print("Won't print")  # Empty list is False

# These are all "Truthy" (treated as True)
if 1:
    print("Will print")  # Any non-zero number is True

if "hello":
    print("Will print")  # Any non-empty string is True

if [1, 2, 3]:
    print("Will print")  # Any non-empty list is True
```

**Practical Use:**

```python
name = input("Enter your name: ")

if name:  # Checks if name is not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name!")
```

---

### 7️⃣ Short-Circuiting (5 minutes)

**Explain:**

"Python is smart - it stops checking as soon as it knows the answer!"

```python
# AND short-circuit
age = 15
has_license = True

# Python checks age first
# Since age >= 18 is False, it doesn't even check has_license
if age >= 18 and has_license:
    print("Can drive")

# OR short-circuit
day = "Saturday"

# Python checks first condition
# Since it's True, it doesn't check second condition
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

**Practical Benefit:**

```python
# Avoid errors with short-circuit
x = 0

# Without short-circuit (would cause error)
# if x != 0 and 10 / x > 2:  # Division by zero!

# With short-circuit (safe!)
if x != 0 and 10 / x > 2:  # Stops at x != 0, never divides
    print("Safe!")
```

---

### 💻 Live Activity: Age-Based Access Program

**Copy-Paste for Students:**

```python
# activity3_access_control.py

print("=" * 50)
print("CINEMA TICKET SYSTEM")
print("=" * 50)

# Get user information
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower()

print("\n" + "=" * 50)

# Check access based on age
if age < 13:
    # Children
    ticket_price = 100
    movie_type = "Children's movies only"
    access = "✅ ALLOWED"
    
elif age >= 13 and age < 18:
    # Teens
    if has_id == "yes":
        ticket_price = 150
        movie_type = "PG-13 and below"
        access = "✅ ALLOWED with ID"
    else:
        ticket_price = 0
        movie_type = "None"
        access = "❌ NEED ID"
        
elif age >= 18:
    # Adults
    ticket_price = 200
    movie_type = "All movies"
    access = "✅ ALLOWED"
    
else:
    # Invalid age
    ticket_price = 0
    movie_type = "None"
    access = "❌ INVALID AGE"

# Display results
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Status: {access}")
print(f"Ticket Price: ₹{ticket_price}")
print(f"Can Watch: {movie_type}")
print("=" * 50)
```

**Test Cases:**
```
Test 1: Age 10 → Child ticket ₹100
Test 2: Age 15 with ID → Teen ticket ₹150
Test 3: Age 15 without ID → Access denied
Test 4: Age 25 → Adult ticket ₹200
```

---

### 🏠 Homework: Grade Calculator

**Give students this template:**

```python
# homework3_grade_calculator.py

print("GRADE CALCULATOR")
print("=" * 40)

# Get student information
name = input("\nEnter student name: ")
marks = int(input("Enter marks (0-100): "))

# TODO: Validate marks (0-100)
if marks < 0 or marks > 100:
    print("❌ Invalid marks! Must be 0-100")
else:
    # TODO: Calculate grade
    # A: 90-100
    # B: 80-89
    # C: 70-79
    # D: 60-69
    # F: 0-59
    
    if marks >= 90:
        grade = "A"
        remarks = "Excellent!"
    elif marks >= 80:
        grade = "B"
        remarks = "Very Good!"
    # TODO: Add remaining conditions
    
    # TODO: Check if passed (>= 60)
    if marks >= 60:
        status = "PASSED ✅"
    else:
        status = "FAILED ❌"
    
    # Display results
    print("\n" + "=" * 40)
    print(f"Student: {name}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Remarks: {remarks}")
    print(f"Status: {status}")
    print("=" * 40)
```

**Expected Output:**
```
GRADE CALCULATOR
========================================

Enter student name: Alice
Enter marks (0-100): 85

========================================
Student: Alice
Marks: 85/100
Grade: B
Remarks: Very Good!
Status: PASSED ✅
========================================
```

---

### 📝 Key Takeaways

✅ if/elif/else for decisions
✅ Indentation is CRITICAL
✅ and/or/not for combining conditions
✅ Empty values are "Falsy"
✅ Short-circuiting prevents errors

---

**[Continue to Hour 4 in next section...]**

---

## 📚 Quick Reference Card (Give to Students)

```python
# IF STATEMENT SYNTAX

# Single condition
if condition:
    # code

# Two options
if condition:
    # code
else:
    # code

# Multiple options
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code

# COMPARISON OPERATORS
==   # Equal to
!=   # Not equal to
>    # Greater than
<    # Less than
>=   # Greater or equal
<=   # Less or equal

# LOGICAL OPERATORS
and  # Both must be True
or   # At least one True
not  # Reverse the result

# FALSY VALUES (treated as False)
0, "", None, [], {}, False

# TRUTHY VALUES (treated as True)
Any non-zero number, non-empty string, True
```

---

**📌 Note for Teacher:**
"Make sure students practice indentation! It's the #1 error for beginners. Use 4 spaces, not tabs!"

---

<a name="hour-4"></a>
## 📅 Hour 4: Loops & Comprehensions

### 🎯 Learning Objectives
- Master for and while loops
- Use range() effectively
- Understand break and continue
- Write list/dict comprehensions
- Build a prime number sieve

### 📖 What to Teach

**"Loops let us repeat tasks - like washing dishes one by one!"**

---

### 1️⃣ For Loops (15 minutes)

**Real-Life Analogy:**

"For loop = Going through each dish in the sink and washing it, one at a time"

**Basic For Loop:**

```python
# Loop through a list
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(f"I love {fruit}")

# Output:
# I love apple
# I love banana
# I love mango
# I love orange
```

**Loop with Index:**

```python
# Using enumerate to get index
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. mango
```

**Range Function:**

```python
# Range creates a sequence of numbers

# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step) - with custom step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Countdown
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

### 2️⃣ While Loops (10 minutes)

**Explain:**

"While loop = Keep washing dishes WHILE there are dishes in the sink"

```python
# Basic while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Must increment, or loop forever!

# Output: Count: 1, Count: 2, ..., Count: 5
```

**User Input Loop:**

```python
# Keep asking until correct password
password = ""

while password != "python123":
    password = input("Enter password: ")
    
    if password != "python123":
        print("Wrong password! Try again.")

print("Access granted!")
```

**Infinite Loop (be careful!):**

```python
# This runs forever - need break to stop
while True:
    user_input = input("Enter 'quit' to exit: ")
    
    if user_input == 'quit':
        break
    
    print(f"You entered: {user_input}")

print("Goodbye!")
```

---

### 3️⃣ Break and Continue (10 minutes)

**Break (exit loop early):**

```python
# Find first number divisible by 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Found it: {i}")
        break  # Exit loop immediately

# Output: Found it: 7
```

**Continue (skip to next iteration):**

```python
# Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    
    print(i)

# Output: 1, 3, 5, 7, 9
```

**Real-World Example:**

```python
# Process valid emails only
emails = ["alice@email.com", "invalid", "bob@email.com", "", "charlie@email.com"]

for email in emails:
    # Skip invalid emails
    if "@" not in email or len(email) == 0:
        print(f"Skipping invalid: {email}")
        continue
    
    # Process valid email
    print(f"Sending to: {email}")
```

---

### 4️⃣ Nested Loops (10 minutes)

**Multiplication Table:**

```python
# Print multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Blank line after each number
```

**Pattern Printing:**

```python
# Print a triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line

# Output:
# *
# **
# ***
# ****
# *****
```

---

### 5️⃣ List Comprehensions (15 minutes)

**Explain:**

"List comprehension = Create a new list in ONE line!"

**Basic Syntax:**

```python
# Traditional way
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension way (SAME RESULT!)
squares = [i ** 2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**With Condition:**

```python
# Get only even numbers
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Get squares of odd numbers
odd_squares = [i ** 2 for i in range(1, 11) if i % 2 != 0]
print(odd_squares)  # [1, 9, 25, 49, 81]
```

**Transform Strings:**

```python
names = ["alice", "bob", "charlie"]

# Capitalize all names
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Get lengths
lengths = [len(name) for name in names]
print(lengths)  # [5, 3, 7]
```

**Dictionary Comprehension:**

```python
# Create dict from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

name_age_dict = {name: age for name, age in zip(names, ages)}
print(name_age_dict)
# {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Square numbers
squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### 💻 Live Activity: Prime Number Sieve

**Create: hour4_prime_sieve.py**

```python
"""
Prime Number Sieve
Find all prime numbers up to a given number
"""

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    
    # Check divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def sieve_of_eratosthenes(limit):
    """Find all primes up to limit using Sieve algorithm"""
    # Create list of True values
    is_prime_list = [True] * (limit + 1)
    is_prime_list[0] = is_prime_list[1] = False  # 0 and 1 not prime
    
    # Start from 2
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime_list[i]:
            # Mark all multiples as not prime
            for j in range(i * i, limit + 1, i):
                is_prime_list[j] = False
    
    # Get all prime numbers (using list comprehension!)
    primes = [i for i in range(limit + 1) if is_prime_list[i]]
    return primes

# Demo
print("=== Prime Number Finder ===\n")

# Method 1: Check individual numbers
print("Checking individual numbers:")
for num in [2, 10, 17, 25, 29]:
    if is_prime(num):
        print(f"{num} is PRIME")
    else:
        print(f"{num} is NOT prime")

print()

# Method 2: Find all primes up to 50
print("All primes up to 50:")
primes = sieve_of_eratosthenes(50)
print(primes)

print()

# Method 3: Print in a nice format
print("Primes up to 100:")
primes_100 = sieve_of_eratosthenes(100)
for i, prime in enumerate(primes_100, 1):
    print(f"{prime:3}", end="  ")
    if i % 10 == 0:  # New line every 10 numbers
        print()
```

**Run this and show output to students!**

---

### 🏠 Homework: Pattern Printer & Number Games

**Task 1: Pattern Printer**

```python
# homework4_patterns.py

def print_right_triangle(height):
    """
    Print right-angled triangle
    *
    **
    ***
    ****
    """
    # TODO: Use nested loops
    pass

def print_pyramid(height):
    """
    Print centered pyramid
       *
      ***
     *****
    *******
    """
    # TODO: Use nested loops with spaces
    pass

def print_diamond(size):
    """
    Print diamond shape
       *
      ***
     *****
      ***
       *
    """
    # TODO: Combine two triangles
    pass

# Test your functions
print_right_triangle(5)
print()
print_pyramid(4)
print()
print_diamond(5)
```

**Task 2: Number Games**

```python
# homework4_number_games.py

# 1. FizzBuzz
# Print numbers 1-100
# If divisible by 3: print "Fizz"
# If divisible by 5: print "Buzz"
# If divisible by both: print "FizzBuzz"
# Otherwise: print the number

for i in range(1, 101):
    # TODO: Complete this
    pass

# 2. Sum of digits
# Input: 12345
# Output: 1 + 2 + 3 + 4 + 5 = 15

number = 12345
# TODO: Calculate sum of digits

# 3. Reverse a number
# Input: 12345
# Output: 54321

number = 12345
# TODO: Reverse the number

# 4. Find perfect numbers
# A perfect number = sum of its divisors (excluding itself)
# Example: 6 = 1 + 2 + 3
# Find all perfect numbers up to 1000

# TODO: Write the logic
```

---

### 📝 Key Takeaways

✅ `for` loop = iterate over items
✅ `while` loop = repeat while condition true
✅ `break` = exit loop early
✅ `continue` = skip to next iteration
✅ List comprehension = `[expression for item in iterable if condition]`
✅ `range(start, stop, step)` creates number sequences
✅ Nested loops = loop inside loop

---

<a name="hour-5"></a>
## 📅 Hour 5: Functions & Scoping

### 🎯 Learning Objectives
- Define and call functions
- Use parameters and return values
- Understand default arguments
- Master *args and **kwargs
- Learn variable scoping
- Write recursive functions

### 📖 What to Teach

**"Functions are like recipes - write once, use many times!"**

---

### 1️⃣ Basic Functions (15 minutes)

**Simple Function:**

```python
# Define function
def greet():
    print("Hello, World!")

# Call function
greet()  # Output: Hello, World!
```

**Function with Parameters:**

```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")   # Hello, Alice!
greet_person("Bob")     # Hello, Bob!
```

**Multiple Parameters:**

```python
def introduce(name, age, city):
    print(f"I am {name}, {age} years old, from {city}")

introduce("Alice", 25, "Mumbai")
# Output: I am Alice, 25 years old, from Mumbai
```

**Return Values:**

```python
def add(a, b):
    result = a + b
    return result

# Use the returned value
sum_result = add(5, 3)
print(sum_result)  # 8

# Use directly
print(add(10, 20))  # 30
```

**Multiple Return Values:**

```python
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    product = a * b
    return sum_result, diff_result, product

# Unpack results
s, d, p = calculate(10, 5)
print(f"Sum: {s}, Diff: {d}, Product: {p}")
# Output: Sum: 15, Diff: 5, Product: 50
```

---

### 2️⃣ Default Arguments (10 minutes)

**Basic Default:**

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Namaste") # Namaste, Charlie!
```

**Real-World Example:**

```python
def calculate_price(price, tax_rate=0.18, discount=0):
    """Calculate final price with tax and discount"""
    price_with_tax = price + (price * tax_rate)
    final_price = price_with_tax - discount
    return final_price

# Use default tax rate
print(calculate_price(1000))  # 1180.0

# Custom tax rate
print(calculate_price(1000, tax_rate=0.10))  # 1100.0

# With discount
print(calculate_price(1000, discount=100))  # 1080.0
```

---

### 3️⃣ *args and **kwargs (15 minutes)

***args (variable positional arguments):**

```python
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all(5))                 # 5
```

****kwargs (variable keyword arguments):**

```python
def print_info(**info):
    """Print any number of key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Mumbai")
# Output:
# name: Alice
# age: 25
# city: Mumbai
```

**Combining All:**

```python
def create_profile(name, age, *hobbies, **other_info):
    """Create user profile with flexible arguments"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    print("Hobbies:")
    for hobby in hobbies:
        print(f"  - {hobby}")
    
    print("Additional Info:")
    for key, value in other_info.items():
        print(f"  {key}: {value}")

# Call with various arguments
create_profile(
    "Alice", 
    25, 
    "Reading", "Coding", "Gaming",
    city="Mumbai",
    occupation="Developer",
    email="alice@email.com"
)
```

---

### 4️⃣ Variable Scoping (10 minutes)

**Local vs Global:**

```python
# Global variable
count = 0

def increment():
    # Local variable (new variable, doesn't change global)
    count = 1
    print(f"Inside function: {count}")

increment()  # Inside function: 1
print(f"Outside function: {count}")  # Outside function: 0
```

**Using Global Keyword:**

```python
count = 0

def increment():
    global count  # Now we can modify global variable
    count += 1
    print(f"Inside function: {count}")

increment()  # Inside function: 1
increment()  # Inside function: 2
print(f"Outside function: {count}")  # Outside function: 2
```

**Best Practice (return instead of global):**

```python
count = 0

def increment(current_count):
    return current_count + 1

# Better approach
count = increment(count)
print(count)  # 1
count = increment(count)
print(count)  # 2
```

---

### 5️⃣ Recursion (10 minutes)

**Explain:**

"Recursion = A function calling itself. Like a mirror reflecting a mirror!"

**Factorial (Classic Example):**

```python
# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # 120

# Recursive approach
def factorial_recursive(n):
    # Base case (stop condition)
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 120

# How it works:
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1  ← Base case reached!
# Then: 2 * 1 = 2, 3 * 2 = 6, 4 * 6 = 24, 5 * 24 = 120
```

**Fibonacci:**

```python
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

---

### 💻 Live Activity: Calculator with Functions

**Create: hour5_calculator.py**

```python
"""
Advanced Calculator with Functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def square_root(n):
    """Calculate square root"""
    return n ** 0.5

def percentage(value, percent):
    """Calculate percentage of a value"""
    return (value * percent) / 100

def factorial(n):
    """Calculate factorial (recursive)"""
    if n < 0:
        return "Error: Negative numbers don't have factorials!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_bmi(weight, height):
    """Calculate BMI (Body Mass Index)"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

def display_menu():
    """Display calculator menu"""
    print("\n=== ADVANCED CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Factorial")
    print("9. BMI Calculator")
    print("0. Exit")
    print("=" * 27)

def main():
    """Main calculator program"""
    while True:
        display_menu()
        choice = input("Enter choice (0-9): ")
        
        if choice == '0':
            print("Thank you! Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {add(a, b)}")
            elif choice == '2':
                print(f"Result: {subtract(a, b)}")
            elif choice == '3':
                print(f"Result: {multiply(a, b)}")
            elif choice == '4':
                print(f"Result: {divide(a, b)}")
            elif choice == '5':
                print(f"Result: {power(a, b)}")
        
        elif choice == '6':
            n = float(input("Enter number: "))
            print(f"Result: {square_root(n)}")
        
        elif choice == '7':
            value = float(input("Enter value: "))
            percent = float(input("Enter percentage: "))
            print(f"{percent}% of {value} = {percentage(value, percent)}")
        
        elif choice == '8':
            n = int(input("Enter number: "))
            print(f"Result: {factorial(n)}")
        
        elif choice == '9':
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            bmi, category = calculate_bmi(weight, height)
            print(f"BMI: {bmi:.2f} ({category})")
        
        else:
            print("Invalid choice!")

# Run calculator
if __name__ == "__main__":
    main()
```

**Demo this to students - show all calculator functions!**

---

### 🏠 Homework: Function Practice

```python
# homework5_functions.py

# 1. Temperature Converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # Formula: F = (C × 9/5) + 32
    # TODO: Complete this
    pass

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # Formula: C = (F - 32) × 5/9
    # TODO: Complete this
    pass

# 2. Palindrome Checker
def is_palindrome(text):
    """Check if text is a palindrome"""
    # Example: "radar" is palindrome
    # TODO: Complete this
    pass

# 3. List Statistics
def calculate_stats(numbers):
    """Return min, max, average, median of list"""
    # Return multiple values as tuple
    # TODO: Complete this
    pass

# 4. Password Validator
def is_valid_password(password):
    """
    Check if password is valid:
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains at least one number
    - Contains at least one special character
    """
    # TODO: Complete this
    pass

# 5. Fibonacci with Memoization (Advanced)
def fibonacci_memo(n, memo={}):
    """
    Calculate Fibonacci with memoization (caching)
    Much faster than simple recursion!
    """
    # TODO: Complete this
    pass

# Test your functions
print(celsius_to_fahrenheit(0))    # Should be 32
print(is_palindrome("radar"))       # Should be True
print(calculate_stats([1,2,3,4,5])) # Should return stats
print(is_valid_password("Pass@123")) # Should be True
```

---

### 📝 Key Takeaways

✅ Functions = reusable code blocks
✅ `def function_name(parameters):` syntax
✅ `return` sends value back
✅ Default arguments: `def func(x=10):`
✅ `*args` = variable positional arguments
✅ `**kwargs` = variable keyword arguments
✅ Scope: local variables vs global variables
✅ Recursion = function calling itself

---

<a name="hour-6"></a>
## 📅 Hour 6: Data Structures - Lists & Tuples

### 🎯 Learning Objectives
- Master list operations
- Use list methods effectively
- Understand list slicing
- Learn when to use tuples
- Build a todo list app with JSON

### 📖 What to Teach

**"Lists are like shopping lists - you can add, remove, and change items!"**

---

### 1️⃣ List Basics (10 minutes)

**Creating Lists:**

```python
# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "mango", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]

# Using list() constructor
my_list = list()
char_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']
```

**Accessing Elements:**

```python
fruits = ["apple", "banana", "mango", "orange"]

# Index starts at 0
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[3])   # orange

# Negative indexing (from end)
print(fruits[-1])  # orange (last item)
print(fruits[-2])  # mango (second from end)
```

---

### 2️⃣ List Methods (15 minutes)

**Adding Items:**

```python
fruits = ["apple", "banana"]

# append() - add at end
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']

# insert() - add at specific position
fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  # ['apple', 'orange', 'banana', 'mango']

# extend() - add multiple items
fruits.extend(["grape", "kiwi"])
print(fruits)  # ['apple', 'orange', 'banana', 'mango', 'grape', 'kiwi']
```

**Removing Items:**

```python
fruits = ["apple", "banana", "mango", "banana", "orange"]

# remove() - remove first occurrence
fruits.remove("banana")
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# pop() - remove by index and return it
last_fruit = fruits.pop()  # Remove last
print(last_fruit)  # orange
print(fruits)  # ['apple', 'mango', 'banana']

first_fruit = fruits.pop(0)  # Remove first
print(first_fruit)  # apple
print(fruits)  # ['mango', 'banana']

# clear() - remove all items
fruits.clear()
print(fruits)  # []
```

**Finding and Counting:**

```python
fruits = ["apple", "banana", "mango", "banana", "orange"]

# index() - find position
pos = fruits.index("banana")
print(pos)  # 1 (first occurrence)

# count() - count occurrences
banana_count = fruits.count("banana")
print(banana_count)  # 2

# in operator - check if exists
if "mango" in fruits:
    print("We have mango!")
```

**Sorting:**

```python
numbers = [5, 2, 8, 1, 9, 3]

# sort() - sort in place
numbers.sort()
print(numbers)  # [1, 2, 3, 5, 8, 9]

# sort in reverse
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 3, 2, 1]

# sorted() - return new sorted list
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 5, 8, 9]
print(numbers)  # [5, 2, 8, 1, 9, 3] (unchanged)

# Sort strings
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']
```

---

### 3️⃣ List Slicing (15 minutes)

**Basic Slicing:**

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:stop] - from start to stop-1
print(numbers[2:5])    # [2, 3, 4]
print(numbers[0:3])    # [0, 1, 2]

# [start:] - from start to end
print(numbers[5:])     # [5, 6, 7, 8, 9]

# [:stop] - from beginning to stop-1
print(numbers[:4])     # [0, 1, 2, 3]

# [:] - copy entire list
copy = numbers[:]
print(copy)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Step Parameter:**

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:stop:step]
print(numbers[0:10:2])  # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1:10:2])  # [1, 3, 5, 7, 9] (odd numbers)
print(numbers[::3])     # [0, 3, 6, 9] (every 3rd)

# Reverse list
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

**Practical Examples:**

```python
text = "Hello, World!"

# Get first 5 characters
print(text[:5])  # Hello

# Get last 6 characters
print(text[-6:])  # World!

# Reverse string
print(text[::-1])  # !dlroW ,olleH

# Every other character
print(text[::2])  # Hlo ol!
```

---

### 4️⃣ Tuples (10 minutes)

**Explain:**

"Tuple = Immutable list (cannot be changed after creation). Like a sealed package!"

**Creating Tuples:**

```python
# Empty tuple
empty = ()

# Single item (need comma!)
single = (5,)

# Multiple items
coordinates = (10, 20)
rgb_color = (255, 0, 128)
person = ("Alice", 25, "Mumbai")
```

**Accessing Tuples:**

```python
coordinates = (10, 20, 30)

print(coordinates[0])  # 10
print(coordinates[1])  # 20

# Unpacking
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")
```

**When to Use Tuples:**

```python
# Return multiple values from function
def get_user():
    return ("Alice", 25, "alice@email.com")

name, age, email = get_user()

# Dictionary keys (tuples can be keys, lists cannot)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

# Immutable data (cannot be accidentally changed)
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

---

### 10 💻 Live Activity: Todo List App with JSON

**Create: hour6_todo_app.py**

```python
"""
Advanced Todo List Application
Save/load todos from JSON file
"""

import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task, priority="medium"):
        """Add a new todo"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✅ Added: {task}")
    
    def list_todos(self, show_all=True):
        """List all todos"""
        if not self.todos:
            print("No todos yet!")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Task':<30} {'Priority':<10} {'Status':<10}")
        print("="*60)
        
        for todo in self.todos:
            if not show_all and todo['completed']:
                continue
            
            status = "✓ Done" if todo['completed'] else "○ Pending"
            print(f"{todo['id']:<5} {todo['task']:<30} {todo['priority']:<10} {status:<10}")
        
        print("="*60 + "\n")
    
    def complete_todo(self, todo_id):
        """Mark todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✅ Completed: {todo['task']}")
                return
        print(f"❌ Todo {todo_id} not found!")
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                deleted_task = self.todos.pop(i)
                # Re-number remaining todos
                for j, t in enumerate(self.todos):
                    t['id'] = j + 1
                self.save_todos()
                print(f"🗑️ Deleted: {deleted_task['task']}")
                return
        print(f"❌ Todo {todo_id} not found!")
    
    def search_todos(self, keyword):
        """Search todos by keyword"""
        results = [t for t in self.todos if keyword.lower() in t['task'].lower()]
        
        if not results:
            print(f"No todos found with '{keyword}'")
            return
        
        print(f"\n🔍 Search results for '{keyword}':")
        for todo in results:
            status = "✓" if todo['completed'] else "○"
            print(f"  {status} [{todo['id']}] {todo['task']}")
    
    def get_stats(self):
        """Show todo statistics"""
        total = len(self.todos)
        completed = sum(1 for t in self.todos if t['completed'])
        pending = total - completed
        
        print("\n📊 Todo Statistics:")
        print(f"  Total: {total}")
        print(f"  Completed: {completed}")
        print(f"  Pending: {pending}")
        
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"  Completion Rate: {completion_rate:.1f}%")

def show_menu():
    """Display menu"""
    print("\n" + "="*40)
    print("        TODO LIST APPLICATION")
    print("="*40)
    print("1. Add Todo")
    print("2. List All Todos")
    print("3. List Pending Todos")
    print("4. Complete Todo")
    print("5. Delete Todo")
    print("6. Search Todos")
    print("7. Show Statistics")
    print("0. Exit")
    print("="*40)

def main():
    """Main program"""
    app = TodoApp()
    
    while True:
        show_menu()
        choice = input("Enter choice (0-7): ")
        
        if choice == '0':
            print("Goodbye! Stay productive! 🚀")
            break
        
        elif choice == '1':
            task = input("Enter task: ")
            priority = input("Priority (high/medium/low) [medium]: ").lower() or "medium"
            app.add_todo(task, priority)
        
        elif choice == '2':
            app.list_todos(show_all=True)
        
        elif choice == '3':
            app.list_todos(show_all=False)
        
        elif choice == '4':
            app.list_todos(show_all=False)
            todo_id = int(input("Enter todo ID to complete: "))
            app.complete_todo(todo_id)
        
        elif choice == '5':
            app.list_todos()
            todo_id = int(input("Enter todo ID to delete: "))
            app.delete_todo(todo_id)
        
        elif choice == '6':
            keyword = input("Enter search keyword: ")
            app.search_todos(keyword)
        
        elif choice == '7':
            app.get_stats()
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
```

**Demo this complete app to students!**

---

### 🏠 Homework: List & Tuple Practice

```python
# homework6_lists_tuples.py

# 1. List Operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# TODO: Remove duplicates (create new list with unique values)
# TODO: Find second largest number
# TODO: Create two lists: even numbers and odd numbers
# TODO: Sort in descending order

# 2. Matrix Operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# TODO: Print diagonal elements (1, 5, 9)
# TODO: Sum of each row
# TODO: Sum of each column
# TODO: Transpose matrix (swap rows and columns)

# 3. Student Records (List of Tuples)
students = [
    ("Alice", 85, "A"),
    ("Bob", 70, "B"),
    ("Charlie", 95, "A"),
    ("David", 60, "C"),
    ("Eve", 88, "A")
]

# TODO: Find student with highest marks
# TODO: Count students with grade 'A'
# TODO: Calculate average marks
# TODO: Sort students by marks (descending)

# 4. Shopping Cart
cart = []

# TODO: Add items as tuples (name, price, quantity)
# TODO: Calculate total cost
# TODO: Apply 10% discount if total > 1000
# TODO: Display bill in nice format
```

---

### 📝 Key Takeaways

✅ Lists = mutable, ordered collections
✅ `append()`, `insert()`, `extend()` = add items
✅ `remove()`, `pop()`, `clear()` = remove items
✅ Slicing: `list[start:stop:step]`
✅ Tuples = immutable lists
✅ Use tuples for fixed data, lists for changing data

---

<a name="hour-7"></a>
## 📅 Hour 7: Data Structures - Dictionaries & Sets

### 🎯 Learning Objectives
- Master dictionary operations
- Use dict methods effectively
- Understand sets and set operations
- Work with nested dictionaries
- Build a word frequency counter

### 📖 What to Teach

**"Dictionaries are like phone books - find information by name (key), not position!"**

---

### 1️⃣ Dictionary Basics (15 minutes)

**Creating Dictionaries:**

```python
# Empty dictionary
my_dict = {}
my_dict = dict()

# Dictionary with data
person = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai",
    "email": "alice@email.com"
}

# Mixed types
data = {
    "name": "Bob",
    "age": 30,
    "scores": [85, 90, 88],
    "is_active": True
}
```

**Accessing Values:**

```python
person = {"name": "Alice", "age": 25, "city": "Mumbai"}

# Using bracket notation
print(person["name"])  # Alice
print(person["age"])   # 25

# Using get() method (safer - returns None if key doesn't exist)
print(person.get("name"))    # Alice
print(person.get("phone"))   # None (no error!)
print(person.get("phone", "Not available"))  # Not available
```

**Adding/Updating Values:**

```python
person = {"name": "Alice", "age": 25}

# Add new key
person["city"] = "Mumbai"
person["email"] = "alice@email.com"

# Update existing key
person["age"] = 26

print(person)
# {'name': 'Alice', 'age': 26, 'city': 'Mumbai', 'email': 'alice@email.com'}
```

**Removing Values:**

```python
person = {"name": "Alice", "age": 25, "city": "Mumbai"}

# pop() - remove and return value
age = person.pop("age")
print(age)  # 25
print(person)  # {'name': 'Alice', 'city': 'Mumbai'}

# del - delete key
del person["city"]
print(person)  # {'name': 'Alice'}

# clear() - remove all items
person.clear()
print(person)  # {}
```

---

### 2️⃣ Dictionary Methods (15 minutes)

**Keys, Values, Items:**

```python
person = {"name": "Alice", "age": 25, "city": "Mumbai"}

# Get all keys
keys = person.keys()
print(list(keys))  # ['name', 'age', 'city']

# Get all values
values = person.values()
print(list(values))  # ['Alice', 25, 'Mumbai']

# Get all key-value pairs
items = person.items()
print(list(items))  # [('name', 'Alice'), ('age', 25), ('city', 'Mumbai')]
```

**Looping Through Dictionaries:**

```python
person = {"name": "Alice", "age": 25, "city": "Mumbai"}

# Loop through keys
for key in person:
    print(key)

# Loop through keys (explicit)
for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs (MOST COMMON)
for key, value in person.items():
    print(f"{key}: {value}")
```

**Update and Merge:**

```python
person = {"name": "Alice", "age": 25}
additional_info = {"city": "Mumbai", "email": "alice@email.com"}

# Update dictionary with another dict
person.update(additional_info)
print(person)
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai', 'email': 'alice@email.com'}

# Merge using ** operator (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

### 3️⃣ Nested Dictionaries (10 minutes)

**Dictionary of Dictionaries:**

```python
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "city": "Mumbai"
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "city": "Delhi"
    },
    "user3": {
        "name": "Charlie",
        "age": 35,
        "city": "Bangalore"
    }
}

# Access nested values
print(users["user1"]["name"])  # Alice
print(users["user2"]["age"])   # 30

# Loop through nested dict
for user_id, user_info in users.items():
    print(f"\n{user_id}:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")
```

**List of Dictionaries:**

```python
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 20, "grade": "A"}
]

# Loop through list of dicts
for student in students:
    print(f"{student['name']}: Grade {student['grade']}")

# Find students with grade A
a_students = [s for s in students if s['grade'] == 'A']
print(a_students)
```

---

### 4️⃣ Sets (10 minutes)

**Explain:**

"Set = Collection of unique items (no duplicates). Like a bag of unique marbles!"

**Creating Sets:**

```python
# Empty set (must use set(), not {})
empty_set = set()

# Set with items
fruits = {"apple", "banana", "mango"}
numbers = {1, 2, 3, 4, 5}

# From list (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

**Set Operations:**

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all items from both sets)
union = set1 | set2
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (common items)
intersection = set1 & set2
print(intersection)  # {4, 5}

# Difference (in set1 but not in set2)
difference = set1 - set2
print(difference)  # {1, 2, 3}

# Symmetric difference (in either but not both)
sym_diff = set1 ^ set2
print(sym_diff)  # {1, 2, 3, 6, 7, 8}
```

**Set Methods:**

```python
fruits = {"apple", "banana", "mango"}

# Add item
fruits.add("orange")
print(fruits)  # {'apple', 'banana', 'mango', 'orange'}

# Remove item (error if doesn't exist)
fruits.remove("banana")

# Discard (no error if doesn't exist)
fruits.discard("grape")  # No error

# Check membership
if "apple" in fruits:
    print("We have apples!")
```

---

### 💻 Live Activity: Word Frequency Counter

**Create: hour7_word_frequency.py**

```python
"""
Word Frequency Counter
Count word occurrences in text
"""

import string
from collections import Counter

def clean_text(text):
    """Remove punctuation and convert to lowercase"""
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    return text

def count_words_manual(text):
    """Count words manually using dictionary"""
    text = clean_text(text)
    words = text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def count_words_get(text):
    """Count words using dict.get()"""
    text = clean_text(text)
    words = text.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def count_words_counter(text):
    """Count words using Counter"""
    text = clean_text(text)
    words = text.split()
    return Counter(words)

def display_frequency(word_count, top_n=10):
    """Display word frequency"""
    print(f"\n{'Word':<20} {'Count':<10}")
    print("=" * 30)
    
    # Sort by frequency (descending)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in sorted_words[:top_n]:
        print(f"{word:<20} {count:<10}")

def get_statistics(word_count):
    """Get text statistics"""
    total_words = sum(word_count.values())
    unique_words = len(word_count)
    
    if unique_words > 0:
        most_common = max(word_count.items(), key=lambda x: x[1])
        avg_frequency = total_words / unique_words
    else:
        most_common = ("", 0)
        avg_frequency = 0
    
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_common": most_common,
        "avg_frequency": avg_frequency
    }

# Sample text
sample_text = """
Python is an amazing programming language. Python is easy to learn and 
Python is widely used in data science, web development, and automation.
Learning Python opens many career opportunities. Python Python Python!
"""

print("=== WORD FREQUENCY COUNTER ===\n")

# Method 1: Manual counting
print("Method 1: Manual Dictionary")
word_count = count_words_manual(sample_text)
display_frequency(word_count)

# Method 2: Using get()
print("\nMethod 2: Using dict.get()")
word_count = count_words_get(sample_text)
display_frequency(word_count)

# Method 3: Using Counter
print("\nMethod 3: Using Counter")
word_count = count_words_counter(sample_text)
display_frequency(word_count)

# Statistics
print("\n=== TEXT STATISTICS ===")
stats = get_statistics(word_count)
print(f"Total words: {stats['total_words']}")
print(f"Unique words: {stats['unique_words']}")
print(f"Most common word: '{stats['most_common'][0]}' ({stats['most_common'][1]} times)")
print(f"Average frequency: {stats['avg_frequency']:.2f}")

# Interactive mode
print("\n" + "="*50)
print("Enter your own text to analyze (or 'quit' to exit):")
print("="*50)

while True:
    user_text = input("\nEnter text: ")
    
    if user_text.lower() == 'quit':
        break
    
    if not user_text.strip():
        print("Please enter some text!")
        continue
    
    word_count = count_words_counter(user_text)
    print("\nTop 10 words:")
    display_frequency(word_count, top_n=10)
    
    stats = get_statistics(word_count)
    print(f"\nTotal words: {stats['total_words']}, Unique: {stats['unique_words']}")
```

**Demo this and let students try different texts!**

---

### 🏠 Homework: Dictionary & Set Practice

```python
# homework7_dicts_sets.py

# 1. Contact Book
contacts = {}

# TODO: Add at least 5 contacts with name, phone, email
# TODO: Search contact by name
# TODO: Update contact details
# TODO: Delete a contact
# TODO: List all contacts sorted by name

# 2. Student Grade Manager
students = {
    "Alice": {"math": 85, "science": 90, "english": 88},
    "Bob": {"math": 70, "science": 75, "english": 80},
    "Charlie": {"math": 95, "science": 92, "english": 89}
}

# TODO: Calculate average grade for each student
# TODO: Find student with highest average
# TODO: Find which subject has highest average across all students
# TODO: Add new student
# TODO: Update a grade

# 3. Set Operations - User Permissions
admin_users = {"alice", "bob", "charlie"}
active_users = {"bob", "charlie", "david", "eve"}
premium_users = {"alice", "david"}

# TODO: Find users who are both admin and active
# TODO: Find users who are admin but not active
# TODO: Find all types of users (union of all sets)
# TODO: Find users who are active but not premium

# 4. Word Analysis
text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the lazy cat sleeps under the warm sun"

# TODO: Find common words between both texts
# TODO: Find words unique to text1
# TODO: Find words unique to text2
# TODO: Find all unique words from both texts

# 5. Inventory Management (Nested Dictionaries)
inventory = {
    "laptop": {"price": 50000, "stock": 10, "category": "electronics"},
    "mouse": {"price": 500, "stock": 50, "category": "electronics"},
    "notebook": {"price": 50, "stock": 100, "category": "stationery"},
    "pen": {"price": 10, "stock": 500, "category": "stationery"}
}

# TODO: Calculate total inventory value
# TODO: Find items with low stock (< 20)
# TODO: Group items by category
# TODO: Apply 10% discount to all electronics
```

---

### 📝 Key Takeaways

✅ Dictionaries = key-value pairs
✅ Access: `dict["key"]` or `dict.get("key")`
✅ Loop: `for key, value in dict.items():`
✅ Sets = unique items only
✅ Set operations: union `|`, intersection `&`, difference `-`
✅ Use Counter for frequency counting

---

<a name="hour-8"></a>
## 📅 Hour 8: File I/O & Exception Handling

### 🎯 Learning Objectives
- Read and write files
- Use context managers (with statement)
- Handle exceptions gracefully
- Work with CSV and JSON files
- Build a log file analyzer

### 📖 What to Teach

**"Files are like notebooks - we can read from them and write to them!"**

---

### 1️⃣ Reading Files (15 minutes)

**Basic File Reading:**

```python
# Method 1: Manual open/close
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # IMPORTANT: Must close file!

# Method 2: Context manager (RECOMMENDED)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed when with block ends!
```

**Reading Methods:**

```python
# read() - read entire file as string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# readline() - read one line
with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

# readlines() - read all lines as list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes \n

# Loop through file (MOST EFFICIENT)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### 2️⃣ Writing Files (15 minutes)

**Write Mode (overwrites file):**

```python
# Write mode - creates new file or overwrites existing
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

**Append Mode (adds to end of file):**

```python
# Append mode - adds to existing file
with open("output.txt", "a") as file:
    file.write("This is appended\n")
    file.write("Another appended line\n")
```

**File Modes Summary:**

```python
# "r"  - Read (default, file must exist)
# "w"  - Write (creates new or overwrites)
# "a"  - Append (adds to end)
# "r+" - Read and write
# "b"  - Binary mode (e.g., "rb", "wb" for images)
```

---

### 3️⃣ Exception Handling (15 minutes)

**Try-Except Basics:**

```python
# Without exception handling (program crashes)
# number = int("hello")  # ValueError!

# With exception handling
try:
    number = int("hello")
    print(number)
except ValueError:
    print("That's not a valid number!")

print("Program continues...")
```

**Multiple Exceptions:**

```python
try:
    # Attempt to read file
    with open("nonexistent.txt", "r") as file:
        content = file.read()
    
    # Attempt to divide
    result = 10 / 0
    
except FileNotFoundError:
    print("File not found!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Try-Except-Else-Finally:**

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    
except ValueError:
    print("Invalid input! Please enter a number.")
    
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
else:
    # Runs if NO exception occurred
    print(f"Result: {result}")
    
finally:
    # ALWAYS runs (cleanup code)
    print("Execution completed")
```

**Raising Exceptions:**

```python
def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = 2025
    
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future!")
    
    if birth_year < 1900:
        raise ValueError("Birth year seems too old!")
    
    age = current_year - birth_year
    return age

try:
    age = calculate_age(2030)
except ValueError as e:
    print(f"Error: {e}")
```

---

### 4️⃣ Working with CSV Files (10 minutes)

**Reading CSV:**

```python
import csv

# Read CSV file
with open("students.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    # Skip header
    header = next(csv_reader)
    print(f"Columns: {header}")
    
    # Read rows
    for row in csv_reader:
        print(row)

# Read as dictionary
with open("students.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(f"{row['name']}: {row['grade']}")
```

**Writing CSV:**

```python
import csv

# Write CSV file
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 20, "A"]
]

with open("students.csv", "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(students)

# Write from dictionary
students_dict = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"}
]

with open("students.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerows(students_dict)
```

---

### 5️⃣ Working with JSON Files (5 minutes)

**Reading JSON:**

```python
import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Parse JSON string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data["name"])  # Alice
```

**Writing JSON:**

```python
import json

# Write to JSON file
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"],
    "address": {
        "city": "Mumbai",
        "country": "India"
    }
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
```

---

### 💻 Live Activity: Log File Analyzer

**Create: hour8_log_analyzer.py**

```python
"""
Log File Analyzer
Analyze server log files for errors and statistics
"""

import re
from datetime import datetime
from collections import Counter

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = []
    
    def read_logs(self):
        """Read and parse log file"""
        try:
            with open(self.log_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        log_entry = self.parse_log_line(line)
                        if log_entry:
                            self.logs.append(log_entry)
            
            print(f"✅ Successfully read {len(self.logs)} log entries")
            
        except FileNotFoundError:
            print(f"❌ Error: File '{self.log_file}' not found!")
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    
    def parse_log_line(self, line):
        """Parse a single log line"""
        # Example format: 2025-12-15 10:30:45 [ERROR] Database connection failed
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (.*)'
        match = re.match(pattern, line)
        
        if match:
            timestamp, level, message = match.groups()
            return {
                "timestamp": timestamp,
                "level": level,
                "message": message
            }
        return None
    
    def count_by_level(self):
        """Count logs by level (ERROR, INFO, WARNING, etc.)"""
        levels = [log["level"] for log in self.logs]
        level_counts = Counter(levels)
        
        print("\n" + "="*50)
        print("LOG LEVELS SUMMARY")
        print("="*50)
        
        for level, count in level_counts.most_common():
            print(f"{level:<15} {count:>5}")
        
        return level_counts
    
    def find_errors(self):
        """Find all error messages"""
        errors = [log for log in self.logs if log["level"] == "ERROR"]
        
        print("\n" + "="*50)
        print(f"ERRORS FOUND: {len(errors)}")
        print("="*50)
        
        for i, error in enumerate(errors, 1):
            print(f"\n{i}. {error['timestamp']}")
            print(f"   Message: {error['message']}")
        
        return errors
    
    def search_logs(self, keyword):
        """Search logs by keyword"""
        results = [
            log for log in self.logs 
            if keyword.lower() in log["message"].lower()
        ]
        
        print("\n" + "="*50)
        print(f"SEARCH RESULTS FOR '{keyword}': {len(results)} found")
        print("="*50)
        
        for log in results:
            print(f"{log['timestamp']} [{log['level']}] {log['message']}")
        
        return results
    
    def get_statistics(self):
        """Get log statistics"""
        total = len(self.logs)
        
        if total == 0:
            print("No logs to analyze!")
            return
        
        levels = Counter(log["level"] for log in self.logs)
        error_count = levels.get("ERROR", 0)
        warning_count = levels.get("WARNING", 0)
        info_count = levels.get("INFO", 0)
        
        print("\n" + "="*50)
        print("LOG STATISTICS")
        print("="*50)
        print(f"Total logs:     {total}")
        print(f"Errors:         {error_count} ({error_count/total*100:.1f}%)")
        print(f"Warnings:       {warning_count} ({warning_count/total*100:.1f}%)")
        print(f"Info:           {info_count} ({info_count/total*100:.1f}%)")
        
        # Time range
        if self.logs:
            first_log = self.logs[0]["timestamp"]
            last_log = self.logs[-1]["timestamp"]
            print(f"\nTime range:")
            print(f"  From: {first_log}")
            print(f"  To:   {last_log}")
    
    def export_errors_to_file(self, output_file="errors.txt"):
        """Export errors to a separate file"""
        errors = [log for log in self.logs if log["level"] == "ERROR"]
        
        try:
            with open(output_file, "w") as file:
                file.write("="*60 + "\n")
                file.write(f"ERROR REPORT - Generated on {datetime.now()}\n")
                file.write("="*60 + "\n\n")
                
                for i, error in enumerate(errors, 1):
                    file.write(f"{i}. {error['timestamp']}\n")
                    file.write(f"   {error['message']}\n\n")
            
            print(f"\n✅ Errors exported to '{output_file}'")
            
        except Exception as e:
            print(f"❌ Error exporting: {e}")

# Create sample log file
def create_sample_log():
    """Create a sample log file for testing"""
    sample_logs = [
        "2025-12-15 10:30:45 [INFO] Server started successfully",
        "2025-12-15 10:31:12 [INFO] User 'alice' logged in",
        "2025-12-15 10:32:00 [WARNING] High memory usage detected",
        "2025-12-15 10:33:15 [ERROR] Database connection failed",
        "2025-12-15 10:33:20 [INFO] Retrying database connection",
        "2025-12-15 10:33:25 [ERROR] Database connection timeout",
        "2025-12-15 10:35:00 [INFO] User 'bob' logged in",
        "2025-12-15 10:36:45 [WARNING] Slow query detected",
        "2025-12-15 10:37:30 [ERROR] File not found: /data/users.csv",
        "2025-12-15 10:38:00 [INFO] System backup started",
        "2025-12-15 10:40:15 [INFO] System backup completed",
    ]
    
    with open("server.log", "w") as file:
        for log in sample_logs:
            file.write(log + "\n")
    
    print("✅ Sample log file 'server.log' created")

# Demo
print("=== LOG FILE ANALYZER ===\n")

# Create sample log file
create_sample_log()

# Analyze logs
analyzer = LogAnalyzer("server.log")
analyzer.read_logs()

# Show statistics
analyzer.get_statistics()

# Count by level
analyzer.count_by_level()

# Find errors
analyzer.find_errors()

# Search logs
analyzer.search_logs("database")

# Export errors
analyzer.export_errors_to_file()
```

**Demo this complete analyzer!**

---

### 🏠 Homework: File Processing Tasks

```python
# homework8_file_processing.py

# 1. File Statistics
def file_stats(filename):
    """
    Return statistics about a text file:
    - Number of lines
    - Number of words
    - Number of characters
    - Average words per line
    """
    # TODO: Implement this
    pass

# 2. CSV Student Processor
def process_students_csv(input_file, output_file):
    """
    Read students.csv, calculate average grade,
    add new column with letter grade (A/B/C/D/F)
    Write to output_file
    """
    # TODO: Implement this
    pass

# 3. JSON Contact Merger
def merge_contacts(file1, file2, output_file):
    """
    Read two JSON files with contacts,
    merge them (remove duplicates),
    sort by name,
    write to output_file
    """
    # TODO: Implement this
    pass

# 4. Log Filter
def filter_logs(input_file, level, output_file):
    """
    Read log file, filter by level (ERROR/WARNING/INFO),
    write matching logs to output_file
    """
    # TODO: Implement this
    pass

# 5. Configuration File Reader
def read_config(config_file):
    """
    Read a config file (key=value format)
    Return as dictionary
    
    Example config.txt:
    host=localhost
    port=5000
    debug=True
    """
    # TODO: Implement this
    pass
```

---

### 📝 Key Takeaways

✅ Use `with open()` for automatic file closing
✅ Modes: `r` (read), `w` (write), `a` (append)
✅ `try-except` handles errors gracefully
✅ `finally` block always executes
✅ CSV module for CSV files
✅ JSON module for JSON files

---

<a name="hour-9"></a>
## 📅 Hour 9: Modules, Packages & Virtual Environments

### 🎯 Learning Objectives
- Understand modules and packages
- Import and use modules
- Create your own modules
- Use pip to install packages
- Create virtual environments
- Build a package structure

### 📖 What to Teach

**"Modules are like toolboxes - we can use tools made by others!"**

---

### 1️⃣ Importing Modules (15 minutes)

**Built-in Modules:**

```python
# Import entire module
import math
print(math.pi)          # 3.14159...
print(math.sqrt(16))    # 4.0

# Import specific items
from math import pi, sqrt
print(pi)       # 3.14159...
print(sqrt(16)) # 4.0

# Import with alias
import datetime as dt
now = dt.datetime.now()
print(now)

# Import all (NOT RECOMMENDED)
from math import *
print(cos(0))  # Works but pollutes namespace
```

**Common Built-in Modules:**

```python
# datetime - Date and time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Now: {now}")
print(f"Tomorrow: {tomorrow}")

# random - Random numbers
import random
print(random.randint(1, 10))      # Random int 1-10
print(random.choice(['a','b','c']))  # Random choice
numbers = [1,2,3,4,5]
random.shuffle(numbers)            # Shuffle list
print(numbers)

# os - Operating system
import os
print(os.getcwd())          # Current directory
print(os.listdir('.'))      # List files
os.makedirs('new_folder', exist_ok=True)  # Create folder

# sys - System-specific
import sys
print(sys.version)          # Python version
print(sys.platform)         # Platform name
```

---

### 2️⃣ Creating Your Own Modules (15 minutes)

**Simple Module:**

**Create: my_math.py**

```python
"""
My Math Module
Custom mathematical functions
"""

PI = 3.14159

def square(x):
    """Return square of x"""
    return x ** 2

def cube(x):
    """Return cube of x"""
    return x ** 3

def circle_area(radius):
    """Calculate circle area"""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate circle circumference"""
    return 2 * PI * radius

# Test code (only runs when executed directly)
if __name__ == "__main__":
    print("Testing my_math module")
    print(f"Square of 5: {square(5)}")
    print(f"Circle area (radius=10): {circle_area(10)}")
```

**Using Your Module:**

**Create: main.py**

```python
# Import your module
import my_math

print(my_math.square(5))         # 25
print(my_math.cube(3))           # 27
print(my_math.circle_area(10))   # 314.159

# Or import specific items
from my_math import square, cube
print(square(4))  # 16
print(cube(2))    # 8
```

---

### 3️⃣ Packages (15 minutes)

**Package Structure:**

```
my_package/
├── __init__.py
├── math_utils.py
├── string_utils.py
└── helpers/
    ├── __init__.py
    └── validators.py
```

**Create: my_package/__init__.py**

```python
"""
My Package
Collection of utility functions
"""

__version__ = "1.0.0"

# Import from submodules for easy access
from .math_utils import square, cube
from .string_utils import capitalize_words

__all__ = ['square', 'cube', 'capitalize_words']
```

**Create: my_package/math_utils.py**

```python
"""Math utilities"""

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def power(base, exponent):
    return base ** exponent
```

**Create: my_package/string_utils.py**

```python
"""String utilities"""

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in text"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
```

**Create: my_package/helpers/__init__.py**

```python
"""Helper functions"""

from .validators import is_email, is_phone

__all__ = ['is_email', 'is_phone']
```

**Create: my_package/helpers/validators.py**

```python
"""Validation functions"""

import re

def is_email(email):
    """Check if string is valid email"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_phone(phone):
    """Check if string is valid phone (10 digits)"""
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, phone))
```

**Using Your Package:**

```python
# Import from package
from my_package import square, cube, capitalize_words
from my_package.helpers import is_email, is_phone

print(square(5))                # 25
print(capitalize_words("hello world"))  # Hello World
print(is_email("test@example.com"))     # True
print(is_phone("1234567890"))           # True
```

---

### 4️⃣ Virtual Environments (10 minutes)

**Why Virtual Environments?**

"Each project has its own isolated Python environment - like separate toolboxes!"

**Creating Virtual Environment:**

```bash
# Create virtual environment
python -m venv myenv

# Activate (macOS/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate
```

**Installing Packages with pip:**

```bash
# Install single package
pip install requests

# Install specific version
pip install flask==2.0.1

# Install from requirements.txt
pip install -r requirements.txt

# List installed packages
pip list

# Show package info
pip show requests

# Uninstall package
pip uninstall requests

# Freeze requirements
pip freeze > requirements.txt
```

**requirements.txt example:**

```txt
flask==2.3.0
requests==2.31.0
python-dotenv==1.0.0
```

---

### 5️⃣ Popular Python Packages (5 minutes)

**Commonly Used Packages:**

```python
# requests - HTTP requests
import requests
response = requests.get("https://api.github.com")
data = response.json()

# python-dotenv - Environment variables
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")

# pillow - Image processing
from PIL import Image
img = Image.open("photo.jpg")
img.thumbnail((200, 200))
img.save("thumbnail.jpg")

# pandas - Data analysis
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())

# matplotlib - Plotting
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()
```

---

### 💻 Live Activity: Create a Utilities Package

**Project Structure:**

```
utils_package/
├── __init__.py
├── file_utils.py
├── text_utils.py
├── number_utils.py
└── setup.py
```

**Create: utils_package/__init__.py**

```python
"""
Utils Package
Collection of utility functions for common tasks
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .file_utils import read_json, write_json, read_csv
from .text_utils import clean_text, word_count, find_urls
from .number_utils import is_prime, fibonacci, factorial

__all__ = [
    'read_json', 'write_json', 'read_csv',
    'clean_text', 'word_count', 'find_urls',
    'is_prime', 'fibonacci', 'factorial'
]
```

**Create: utils_package/file_utils.py**

```python
"""File utility functions"""

import json
import csv

def read_json(filename):
    """Read JSON file and return data"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'")
        return None

def write_json(filename, data, indent=2):
    """Write data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as e:
        print(f"Error writing JSON: {e}")
        return False

def read_csv(filename):
    """Read CSV file and return list of dictionaries"""
    try:
        with open(filename, 'r') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
```

**Create: utils_package/text_utils.py**

```python
"""Text utility functions"""

import re
import string

def clean_text(text):
    """Remove punctuation and extra spaces"""
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces
    text = ' '.join(text.split())
    return text.lower()

def word_count(text):
    """Count words in text"""
    words = clean_text(text).split()
    return len(words)

def find_urls(text):
    """Find all URLs in text"""
    url_pattern = r'https?://(?:www\.)?[\w\.-]+\.\w+'
    return re.findall(url_pattern, text)

def truncate(text, length, suffix='...'):
    """Truncate text to specified length"""
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix
```

**Create: utils_package/number_utils.py**

```python
"""Number utility functions"""

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def factorial(n):
    """Calculate factorial"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    """Calculate Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)
```

**Create: test_utils.py (to test the package)**

```python
"""Test the utils package"""

from utils_package import (
    read_json, write_json,
    clean_text, word_count, find_urls,
    is_prime, fibonacci, factorial
)

print("=== TESTING UTILS PACKAGE ===\n")

# Test file utils
print("1. File Utils:")
test_data = {"name": "Alice", "age": 25}
write_json("test.json", test_data)
loaded_data = read_json("test.json")
print(f"   Saved and loaded: {loaded_data}")

# Test text utils
print("\n2. Text Utils:")
text = "  Hello,  World!  This is Python.  "
print(f"   Original: '{text}'")
print(f"   Cleaned: '{clean_text(text)}'")
print(f"   Word count: {word_count(text)}")

text_with_urls = "Visit https://python.org and http://github.com"
print(f"   URLs found: {find_urls(text_with_urls)}")

# Test number utils
print("\n3. Number Utils:")
print(f"   Is 17 prime? {is_prime(17)}")
print(f"   Is 20 prime? {is_prime(20)}")
print(f"   First 10 Fibonacci: {fibonacci(10)}")
print(f"   Factorial of 5: {factorial(5)}")

print("\n✅ All tests completed!")
```

---

### 🏠 Homework: Build Your Own Package

```python
# Create a package called 'my_tools' with:

# 1. validators.py
# - is_email(email)
# - is_url(url)
# - is_phone(phone)
# - is_strong_password(password)

# 2. converters.py
# - celsius_to_fahrenheit(temp)
# - fahrenheit_to_celsius(temp)
# - kg_to_pounds(weight)
# - meters_to_feet(distance)

# 3. formatters.py
# - format_currency(amount, symbol='₹')
# - format_date(date, format='DD-MM-YYYY')
# - format_phone(phone)
# - format_bytes(size)

# Create __init__.py that imports all functions
# Create setup.py for package installation
# Write test file to verify all functions work
```

---

### 📝 Key Takeaways

✅ Modules = single .py files
✅ Packages = folders with __init__.py
✅ `import module` or `from module import function`
✅ Virtual environments = isolated Python installations
✅ `pip install package` to add external packages
✅ `requirements.txt` tracks dependencies

---

<a name="hour-10"></a>
## 📅 Hour 10: Debugging & Testing Basics

### 🎯 Learning Objectives
- Use VS Code debugger
- Set breakpoints and inspect variables
- Write unit tests with pytest
- Understand test-driven development (TDD)
- Achieve code coverage
- Build tested calculator module

### 📖 What to Teach

**"Testing = Making sure our code works correctly before shipping!"**

---

### 1️⃣ Debugging with VS Code (15 minutes)

**Print Debugging (Basic):**

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    print(f"DEBUG: total={total}, count={count}")  # Debug print
    average = total / count
    return average

result = calculate_average([10, 20, 30])
print(f"Average: {result}")
```

**VS Code Debugger:**

"Show students how to:"

1. **Set Breakpoint** - Click left of line number (red dot appears)
2. **Start Debugging** - Press F5 or click "Run and Debug"
3. **Step Over** - F10 (execute current line)
4. **Step Into** - F11 (enter function)
5. **Step Out** - Shift+F11 (exit function)
6. **Continue** - F5 (run to next breakpoint)

**Example for Debugging:**

```python
def factorial(n):
    if n == 0:
        return 1  # Set breakpoint here
    return n * factorial(n - 1)  # Set breakpoint here

result = factorial(5)
print(result)
```

"Set breakpoints, run debugger, inspect variables in 'Variables' panel!"

---

### 2️⃣ Assert Statements (10 minutes)

**Basic Assertions:**

```python
def divide(a, b):
    assert b != 0, "Cannot divide by zero!"
    return a / b

# Works fine
print(divide(10, 2))  # 5.0

# Raises AssertionError
print(divide(10, 0))  # AssertionError: Cannot divide by zero!
```

**Testing with Assertions:**

```python
def square(x):
    return x ** 2

# Test cases
assert square(2) == 4, "2² should be 4"
assert square(3) == 9, "3² should be 9"
assert square(0) == 0, "0² should be 0"
assert square(-5) == 25, "(-5)² should be 25"

print("All tests passed!")
```

---

### 3️⃣ Unit Testing with pytest (20 minutes)

**Installing pytest:**

```bash
pip install pytest
```

**Simple Test Example:**

**Create: calculator.py**

```python
"""Simple calculator module"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Raise base to exponent"""
    return base ** exponent
```

**Create: test_calculator.py**

```python
"""Tests for calculator module"""

import pytest
from calculator import add, subtract, multiply, divide, power

def test_add():
    """Test addition"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction"""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    """Test multiplication"""
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Test division"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ValueError):
        divide(10, 0)

def test_power():
    """Test power function"""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
```

**Running Tests:**

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_calculator.py

# Run specific test
pytest test_calculator.py::test_add
```

---

### 4️⃣ Test Fixtures and Parametrize (10 minutes)

**Test Fixtures (Setup/Teardown):**

```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    """Test using fixture"""
    assert sum(sample_data) == 15

def test_length(sample_data):
    """Test using same fixture"""
    assert len(sample_data) == 5
```

**Parametrize (Test Multiple Inputs):**

```python
import pytest
from calculator import add, multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 5, 15),
    (100, 200, 300)
])
def test_add_parametrized(a, b, expected):
    """Test add with multiple inputs"""
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 3, -6),
    (10, 10, 100)
])
def test_multiply_parametrized(a, b, expected):
    """Test multiply with multiple inputs"""
    assert multiply(a, b) == expected
```

---

### 5️⃣ Code Coverage (5 minutes)

**Install pytest-cov:**

```bash
pip install pytest-cov
```

**Run Tests with Coverage:**

```bash
# Show coverage in terminal
pytest --cov=calculator

# Generate HTML coverage report
pytest --cov=calculator --cov-report=html

# Open htmlcov/index.html in browser
```

**Coverage Output:**

```
----------- coverage: platform darwin, python 3.11.0 -----------
Name            Stmts   Miss  Cover
-----------------------------------
calculator.py      12      0   100%
-----------------------------------
TOTAL              12      0   100%
```

---

### 💻 Live Activity: Complete Tested Module

**Create: string_processor.py**

```python
"""
String Processing Module with Full Test Coverage
"""

def reverse_string(text):
    """Reverse a string"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]

def is_palindrome(text):
    """Check if string is palindrome"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def word_count(text):
    """Count words in text"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text.strip():
        return 0
    
    return len(text.split())

def capitalize_words(text):
    """Capitalize first letter of each word"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ' '.join(word.capitalize() for word in text.split())

def count_vowels(text):
    """Count vowels in text"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_duplicates(text):
    """Remove duplicate characters from string"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def find_longest_word(text):
    """Find longest word in text"""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text.strip():
        return ""
    
    words = text.split()
    return max(words, key=len)
```

**Create: test_string_processor.py**

```python
"""Comprehensive tests for string_processor module"""

import pytest
from string_processor import (
    reverse_string,
    is_palindrome,
    word_count,
    capitalize_words,
    count_vowels,
    remove_duplicates,
    find_longest_word
)

# Test reverse_string
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_reverse_string_invalid_input():
    with pytest.raises(TypeError):
        reverse_string(123)

# Test is_palindrome
@pytest.mark.parametrize("text, expected", [
    ("radar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("racecar", True),
    ("python", False),
    ("", True)
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected

def test_is_palindrome_invalid_input():
    with pytest.raises(TypeError):
        is_palindrome(123)

# Test word_count
@pytest.mark.parametrize("text, expected", [
    ("hello world", 2),
    ("Python is awesome", 3),
    ("", 0),
    ("   ", 0),
    ("one", 1)
])
def test_word_count(text, expected):
    assert word_count(text) == expected

def test_word_count_invalid_input():
    with pytest.raises(TypeError):
        word_count(123)

# Test capitalize_words
@pytest.mark.parametrize("text, expected", [
    ("hello world", "Hello World"),
    ("python is great", "Python Is Great"),
    ("ALREADY CAPS", "Already Caps"),
    ("", "")
])
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected

# Test count_vowels
@pytest.mark.parametrize("text, expected", [
    ("hello", 2),
    ("Python", 1),
    ("aeiou", 5),
    ("AEIOU", 5),
    ("xyz", 0),
    ("", 0)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected

# Test remove_duplicates
@pytest.mark.parametrize("text, expected", [
    ("hello", "helo"),
    ("aabbcc", "abc"),
    ("Python", "Python"),
    ("", "")
])
def test_remove_duplicates(text, expected):
    assert remove_duplicates(text) == expected

# Test find_longest_word
@pytest.mark.parametrize("text, expected", [
    ("hello world", "hello"),
    ("Python is awesome", "awesome"),
    ("a bb ccc", "ccc"),
    ("one", "one"),
    ("", "")
])
def test_find_longest_word(text, expected):
    assert find_longest_word(text) == expected

# Test fixture example
@pytest.fixture
def sample_texts():
    """Provide sample texts for testing"""
    return [
        "hello world",
        "Python is great",
        "Testing is important"
    ]

def test_multiple_texts(sample_texts):
    """Test with fixture data"""
    for text in sample_texts:
        assert word_count(text) > 0
        assert isinstance(reverse_string(text), str)
```

**Run Tests:**

```bash
# Run all tests
pytest test_string_processor.py -v

# With coverage
pytest test_string_processor.py --cov=string_processor --cov-report=term-missing
```

---

### 🏠 Homework: Write Tests for Your Code

```python
# homework10_testing.py

# 1. Create a module 'math_operations.py' with:
# - factorial(n)
# - is_prime(n)
# - fibonacci(n)
# - gcd(a, b)
# - lcm(a, b)

# 2. Write comprehensive tests 'test_math_operations.py' with:
# - At least 3 test cases per function
# - Test edge cases (0, negative numbers, etc.)
# - Use parametrize for multiple inputs
# - Achieve 100% code coverage

# 3. Create 'user_validator.py' with:
# - validate_email(email)
# - validate_phone(phone)
# - validate_password(password)
# - validate_age(age)

# 4. Write tests 'test_user_validator.py' with:
# - Test valid inputs
# - Test invalid inputs
# - Test edge cases
# - Use fixtures for test data

# 5. Run coverage report and fix any untested code
```

---

### 📝 Key Takeaways

✅ Use VS Code debugger with breakpoints
✅ Write tests with pytest
✅ Test functions with different inputs
✅ Use `@pytest.mark.parametrize` for multiple cases
✅ Check coverage with `pytest --cov`
✅ Aim for 100% code coverage
✅ Test edge cases and error conditions

---

## 🎉 Part 1 Complete!

**You've learned:**
- Hours 1-3: Python basics, variables, if-else
- Hours 4-5: Loops, functions, recursion
- Hours 6-7: Lists, tuples, dicts, sets
- Hours 8: File I/O and exception handling
- Hour 9: Modules, packages, virtual environments
- Hour 10: Debugging and testing

**Next:** Part 2 - Backend Development (OOP, databases, Flask, APIs)



