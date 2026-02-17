# Flutter & Dart Complete Guide: Zero to Hero 🚀

## 📋 Course Overview

**Duration:** 12-16 weeks (120+ hours)  
**Level:** Beginner to Advanced  
**Prerequisites:** Basic programming knowledge (any language)  
**Outcome:** Build production-ready Flutter applications  

---

## 🎯 Learning Path Structure

```
📚 COMPLETE FLUTTER MASTERY ROADMAP

Phase 1: Foundation (Weeks 1-3)
├─ Dart Language Fundamentals
├─ Flutter Environment Setup
├─ Widget Basics & Layouts
└─ First Flutter App

Phase 2: Core Development (Weeks 4-8)
├─ State Management (Provider, Bloc, Riverpod)
├─ Navigation & Routing
├─ HTTP & APIs Integration
├─ Local Data Storage
└─ Platform-Specific Features

Phase 3: Advanced Topics (Weeks 9-12)
├─ Custom Animations & UI
├─ Architecture Patterns (Clean, MVVM, MVC)
├─ Testing (Unit, Widget, Integration)
├─ Performance Optimization
└─ App Store Deployment

Phase 4: Expert Level (Weeks 13-16)
├─ Advanced State Management
├─ Custom Packages & Plugins
├─ CI/CD & DevOps
├─ Microservices Integration
└─ Portfolio Projects
```

---

## 🌟 Part 1: Dart Language Mastery (Week 1)

### 📚 Learning Objectives
By the end of this week, you will:
- Understand Dart's role in Flutter ecosystem
- Master Dart syntax, data types, and control structures
- Implement object-oriented programming concepts
- Handle asynchronous programming with Futures and Streams
- Build confidence in Dart problem-solving

---

### 1.1 Understanding Dart: The Foundation

#### 🤔 What is Dart and Why Does It Matter?

**Dart is Google's programming language** designed specifically for building user interfaces. Think of it as the **blueprint language** for Flutter apps - just like how architects use specific drawing standards to design buildings, Flutter uses Dart to design mobile apps.

#### 🎯 Why Dart for Flutter? (Theory Deep Dive)

**1. Compilation Strategy - Best of Both Worlds**

```
🔄 DART'S DUAL COMPILATION APPROACH

Development Time (JIT - Just In Time):
┌─────────────────────────────────────────┐
│  Your Dart Code                         │
│       ↓                                 │
│  Dart VM interprets code instantly      │ ← Hot Reload Magic!
│       ↓                                 │
│  See changes immediately in app         │
└─────────────────────────────────────────┘

Production Time (AOT - Ahead Of Time):
┌─────────────────────────────────────────┐
│  Your Dart Code                         │
│       ↓                                 │
│  Compiled to native machine code        │ ← Fast Performance!
│       ↓                                 │
│  Optimized app runs directly on device  │
└─────────────────────────────────────────┘
```

**Key Insight:** This dual approach means you get **instant feedback** during development (like Python) but **high performance** in production (like C++).

**2. Memory Management - Automatic and Efficient**

**Concept:** Unlike languages like C++ where you manually manage memory, Dart uses **Garbage Collection**.

**Real-world analogy:** Think of memory management like a restaurant:
- **Manual (C++):** You have to clean each table yourself after customers leave
- **Garbage Collection (Dart):** A cleaning service automatically cleans tables when customers leave

**3. Single-Threading Model - Simplicity**

**Concept:** Dart runs on a single thread with an **event loop**, similar to JavaScript.

```
📊 EVENT LOOP VISUALIZATION

┌─────────────────────────────────────────┐
│             EVENT LOOP                  │
├─────────────────────────────────────────┤
│  1. Execute current task                │
│  2. Check for completed async operations │
│  3. Handle UI events (taps, scrolls)    │
│  4. Run scheduled callbacks             │
│  5. Repeat...                          │
└─────────────────────────────────────────┘
```

**Why This Matters:** No complex thread synchronization = fewer bugs and easier debugging.

**4. Type Safety with Flexibility**

**Concept:** Dart offers **gradual typing** - you can be strict when you want precision, flexible when you need speed.

**Example of Progressive Typing:**
```dart
// Flexible - for rapid prototyping
var userAge = 25; // Dart infers this is an int

// Strict - for production code  
int calculateAge(DateTime birthDate) {
  // Compiler guarantees age is always an integer
  return DateTime.now().year - birthDate.year;
}
```

---

### 1.2 Dart Language Concepts (Theory + Practice)

#### 🏗️ Variables and Data Types - Building Blocks of Programs

**Theoretical Foundation:**
Variables are like **labeled containers** that store data. In Dart, every variable has a **type** that determines what kind of data it can hold and what operations you can perform on it.

**Mental Model:** Think of variables like different types of containers:
- `String` = Text box (can hold letters, words, sentences)
- `int` = Number box (can hold whole numbers)  
- `double` = Decimal box (can hold decimal numbers)
- `bool` = Switch (can be ON/true or OFF/false)

#### 📝 Variable Declaration Patterns

```dart
// PATTERN 1: Type Inference (Let Dart figure it out)
void typeInferenceExample() {
  var studentName = 'Alice';        // Dart knows: String
  var studentAge = 20;              // Dart knows: int
  var studentGPA = 3.85;            // Dart knows: double
  var isEnrolled = true;            // Dart knows: bool
  
  print('Student: $studentName, Age: $studentAge, GPA: $studentGPA');
  // Why use var? Quick prototyping, cleaner code when type is obvious
}

// PATTERN 2: Explicit Typing (Tell Dart exactly what you want)
void explicitTypingExample() {
  String courseName = 'Computer Science';   // Explicit String
  int creditHours = 3;                     // Explicit int
  double tuitionCost = 15000.50;           // Explicit double
  bool isOnline = false;                   // Explicit bool
  
  // Why use explicit types? 
  // 1. Documentation (other developers know your intent)
  // 2. Error prevention (compiler catches type mismatches)
  // 3. Better IDE support (autocomplete, refactoring)
}

// PATTERN 3: Late Initialization (I'll set this value later)
void lateInitializationExample() {
  late String universityName;     // Promise: "I'll initialize this before using it"
  late int establishedYear;
  
  // Later in the code...
  if (DateTime.now().month >= 9) {
    universityName = 'Fall University';
    establishedYear = 1995;
  } else {
    universityName = 'Spring University'; 
    establishedYear = 2000;
  }
  
  print('$universityName established in $establishedYear');
  // Why use late? Conditional initialization, expensive operations
}

// PATTERN 4: Nullable Types (This might be empty/null)
void nullSafetyExample() {
  String? optionalMessage;          // Can be String or null
  int? optionalCount;               // Can be int or null
  
  // Safe handling of nullable values
  if (optionalMessage != null) {
    print('Message length: ${optionalMessage.length}');
  }
  
  // Null-aware operators (shorthand)
  print('Message: ${optionalMessage ?? 'No message'}');  // Use default if null
  print('Count: ${optionalCount?.toString() ?? 'Unknown'}');  // Safe call
  
  // Why nullable types? Represent absence of data, prevent null crashes
}

// PATTERN 5: Constants (Values that never change)
void constantsExample() {
  // Runtime constant (calculated when program runs)
  final DateTime appStartTime = DateTime.now();
  final String deviceModel = getDeviceModel(); // Can call functions
  
  // Compile-time constant (known when code compiles)
  const double pi = 3.14159;                   // Mathematical constant
  const String appVersion = '1.0.0';           // Fixed value
  const int maxRetries = 3;                    // Configuration constant
  
  // Why use constants?
  // - Performance (no recalculation)
  // - Safety (prevent accidental changes)
  // - Clarity (indicate unchanging values)
}

String getDeviceModel() {
  return 'iPhone 15'; // Placeholder implementation
}
```

#### 🎯 Key Learning Points:

1. **Type Inference (`var`)** - Let Dart be smart, but only when the type is obvious
2. **Explicit Types** - Use for function parameters, class fields, and when clarity matters  
3. **Late Variables** - For conditional initialization or expensive calculations
4. **Nullable Types (`?`)** - Explicitly handle cases where data might be missing
5. **Constants (`final`/`const`)** - Prevent bugs and improve performance

#### Setting Up Dart Environment

```bash
# Install Dart SDK
# macOS
brew tap dart-lang/dart
brew install dart

# Windows
choco install dart-sdk

# Linux
sudo apt-get update
sudo apt-get install dart

# Verify installation
dart --version
```

### 1.2 Dart Syntax Deep Dive

#### Variables and Data Types

```dart
// Variables and Type Inference
void main() {
  // Type inference
  var name = 'Flutter Developer'; // String
  var age = 25; // int
  var salary = 75000.50; // double
  var isActive = true; // bool
  
  // Explicit typing
  String company = 'Google';
  int experience = 3;
  double rating = 4.8;
  bool isRemote = true;
  
  // Late variables (initialized later)
  late String description;
  description = 'Mobile App Developer';
  
  // Final and const
  final currentYear = DateTime.now().year; // Runtime constant
  const pi = 3.14159; // Compile-time constant
  
  // Nullable types (Null Safety)
  String? nullableName; // Can be null
  String nonNullableName = 'John'; // Cannot be null
  
  print('Developer: $name');
  print('Experience: $experience years');
  print('Rating: ${rating.toStringAsFixed(1)}');
}
```

#### 📚 Collections and Generics - Organizing Data Efficiently

**Theoretical Foundation:**
Collections are **containers that hold multiple items**. Think of them as different types of organizers:
- **Lists** = Ordered shelves (items have positions: 1st, 2nd, 3rd...)
- **Maps** = Filing cabinets with labels (find items by their label/key)
- **Sets** = Unique item containers (no duplicates allowed)

**Generics** are like **type templates** - they let you specify what type of data a collection holds, providing type safety and better performance.

#### 📋 Lists - Ordered Collections (Like Arrays)

**Concept:** Lists maintain **order** and allow **duplicates**. Each item has an **index** (position).

```dart
// Understanding Lists Through Real-World Example: Student Grades
void listsDeepDive() {
  // CONCEPT: Type-safe list - only String fruits allowed
  List<String> fruits = ['apple', 'banana', 'orange'];
  
  // WHY GENERICS? Compare these two approaches:
  
  // ❌ Without generics (old way - error-prone)
  List dynamicList = ['apple', 123, true]; // Mixed types - confusing!
  // var firstItem = dynamicList[0]; // What type is this? String? int? bool?
  
  // ✅ With generics (modern way - type-safe)
  List<String> fruitList = ['apple', 'banana', 'orange']; // Only strings!
  String firstFruit = fruitList[0]; // Guaranteed to be a String!
  
  // CORE LIST OPERATIONS - Think of managing a queue of customers
  
  // 1. Adding items (customers join the queue)
  fruits.add('grape');              // Add to end (most common)
  fruits.insert(0, 'mango');        // Insert at specific position
  fruits.addAll(['kiwi', 'peach']); // Add multiple items
  
  // 2. Removing items (customers leave the queue)
  fruits.remove('banana');          // Remove by value
  fruits.removeAt(1);              // Remove by position
  fruits.removeLast();             // Remove last item
  
  // 3. Accessing items (check who's in queue)
  print('First fruit: ${fruits.first}');      // Safe access to first
  print('Last fruit: ${fruits.last}');        // Safe access to last
  print('Fruit at index 2: ${fruits[2]}');    // Direct index access
  print('Total fruits: ${fruits.length}');     // Count of items
  
  // 4. Checking contents (is customer in queue?)
  bool hasApple = fruits.contains('apple');
  int appleIndex = fruits.indexOf('apple'); // Returns -1 if not found
  
  print('Has apple: $hasApple, Apple at index: $appleIndex');
  
  // ITERATION PATTERNS - Different ways to process each item
  
  // Pattern 1: For-each (when you need the value only)
  print('\n--- Processing each fruit ---');
  for (String fruit in fruits) {
    print('Processing: $fruit');
  }
  
  // Pattern 2: Indexed loop (when you need position and value)
  print('\n--- Processing with positions ---');
  for (int i = 0; i < fruits.length; i++) {
    print('Position $i: ${fruits[i]}');
  }
  
  // Pattern 3: forEach with function (functional style)
  print('\n--- Functional processing ---');
  fruits.forEach((fruit) {
    print('Fruit: ${fruit.toUpperCase()}');
  });
  
  // FUNCTIONAL PROGRAMMING METHODS - Transform data elegantly
  
  // map() - Transform each item (like Excel formulas)
  List<String> upperFruits = fruits
      .map((fruit) => fruit.toUpperCase()) // Transform each fruit
      .toList(); // Convert back to list
  
  // where() - Filter items (like database WHERE clause)
  List<String> longFruits = fruits
      .where((fruit) => fruit.length > 5) // Keep only long names
      .toList();
  
  // reduce() - Combine all items into single result
  String allFruits = fruits.reduce((value, element) => value + ', ' + element);
  
  // Advanced: Chaining operations (like Excel formulas)
  List<String> processedFruits = fruits
      .where((fruit) => fruit.length > 4)    // Filter: only long names
      .map((fruit) => fruit.toUpperCase())   // Transform: to uppercase
      .toList();                             // Convert: to list
  
  print('Original: $fruits');
  print('Uppercase: $upperFruits');
  print('Long fruits: $longFruits');
  print('All combined: $allFruits');
  print('Processed: $processedFruits');
}

// PRACTICAL EXAMPLE: Managing a Shopping Cart
void shoppingCartExample() {
  List<String> cart = [];
  
  // Customer adds items
  void addToCart(String item) {
    cart.add(item);
    print('Added $item to cart. Total items: ${cart.length}');
  }
  
  // Customer removes items
  void removeFromCart(String item) {
    if (cart.contains(item)) {
      cart.remove(item);
      print('Removed $item from cart');
    } else {
      print('$item not found in cart');
    }
  }
  
  // View cart contents
  void viewCart() {
    if (cart.isEmpty) {
      print('Cart is empty');
      return;
    }
    
    print('Shopping Cart Contents:');
    for (int i = 0; i < cart.length; i++) {
      print('${i + 1}. ${cart[i]}');
    }
  }
  
  // Simulate shopping
  addToCart('Laptop');
  addToCart('Mouse');
  addToCart('Keyboard');
  viewCart();
  removeFromCart('Mouse');
  viewCart();
}
```

#### 🗂️ Maps - Key-Value Pairs (Like Dictionaries)

**Concept:** Maps store **key-value pairs**. Think of a real dictionary where you look up a **word (key)** to find its **meaning (value)**.

```dart
// Understanding Maps: Student Records System
void mapsDeepDive() {
  // CONCEPT: Maps are like databases - store related information
  Map<String, int> studentGrades = {
    'Alice': 95,   // Key: 'Alice', Value: 95
    'Bob': 87,     // Key: 'Bob', Value: 87
    'Charlie': 92  // Key: 'Charlie', Value: 92
  };
  
  // WHY USE MAPS? Compare with Lists:
  
  // ❌ Using Lists (inefficient for lookups)
  List<String> names = ['Alice', 'Bob', 'Charlie'];
  List<int> grades = [95, 87, 92];
  // To find Alice's grade: search names, remember index, use index in grades
  
  // ✅ Using Maps (efficient, clear relationship)
  // To find Alice's grade: studentGrades['Alice'] - done!
  
  // CORE MAP OPERATIONS
  
  // 1. Adding/Updating entries
  studentGrades['David'] = 88;      // Add new entry
  studentGrades['Alice'] = 98;      // Update existing entry
  
  // 2. Accessing values
  int? aliceGrade = studentGrades['Alice'];         // Safe access (nullable)
  int bobGrade = studentGrades['Bob'] ?? 0;         // With default value
  int charlieGrade = studentGrades['Charlie']!;     // Force unwrap (use carefully!)
  
  print('Alice: $aliceGrade, Bob: $bobGrade, Charlie: $charlieGrade');
  
  // 3. Checking existence
  bool hasStudent = studentGrades.containsKey('Eve');
  bool hasGrade = studentGrades.containsValue(100);
  
  // 4. Removing entries
  studentGrades.remove('Bob');      // Remove Bob's record
  
  // ITERATION PATTERNS FOR MAPS
  
  // Pattern 1: Keys only
  print('\n--- All Students ---');
  for (String name in studentGrades.keys) {
    print('Student: $name');
  }
  
  // Pattern 2: Values only  
  print('\n--- All Grades ---');
  for (int grade in studentGrades.values) {
    print('Grade: $grade');
  }
  
  // Pattern 3: Key-value pairs (most common)
  print('\n--- Student Records ---');
  for (String name in studentGrades.keys) {
    print('$name scored ${studentGrades[name]}');
  }
  
  // Pattern 4: Modern approach with entries
  studentGrades.forEach((name, grade) {
    String performance = grade >= 90 ? 'Excellent' : 
                        grade >= 80 ? 'Good' : 'Needs Improvement';
    print('$name ($grade): $performance');
  });
  
  // ADVANCED MAP OPERATIONS
  
  // Filter high performers
  Map<String, int> highPerformers = Map.fromEntries(
    studentGrades.entries.where((entry) => entry.value >= 90)
  );
  
  // Calculate statistics
  List<int> allGrades = studentGrades.values.toList();
  double averageGrade = allGrades.reduce((a, b) => a + b) / allGrades.length;
  int highestGrade = allGrades.reduce((a, b) => a > b ? a : b);
  
  print('\nStatistics:');
  print('Average grade: ${averageGrade.toStringAsFixed(1)}');
  print('Highest grade: $highestGrade');
  print('High performers: $highPerformers');
}
```

#### 🎯 Sets - Unique Collections (No Duplicates)

**Concept:** Sets are like **exclusive clubs** - each member can only appear once. They automatically prevent duplicates and are perfect for tracking unique items.

```dart
// Understanding Sets: Managing Unique Skills
void setsDeepDive() {
  // CONCEPT: Sets automatically eliminate duplicates
  Set<String> developerSkills = {'Flutter', 'Dart', 'Firebase'};
  
  // WHY USE SETS? Compare with Lists:
  
  // ❌ Using Lists (allows duplicates, manual checking needed)
  List<String> skillsList = ['Flutter', 'Dart', 'Flutter', 'Firebase'];
  print('Skills list: $skillsList'); // Shows: [Flutter, Dart, Flutter, Firebase]
  
  // ✅ Using Sets (automatic duplicate prevention)  
  Set<String> skillsSet = {'Flutter', 'Dart', 'Flutter', 'Firebase'};
  print('Skills set: $skillsSet'); // Shows: {Flutter, Dart, Firebase}
  
  // CORE SET OPERATIONS
  
  // 1. Adding skills (duplicates ignored automatically)
  developerSkills.add('Provider');      // New skill - added
  developerSkills.add('Flutter');       // Duplicate - ignored silently
  developerSkills.addAll(['Riverpod', 'HTTP', 'Dart']); // Multiple adds
  
  print('Current skills: $developerSkills');
  
  // 2. Checking skills
  bool knowsFlutter = developerSkills.contains('Flutter');
  bool knowsReact = developerSkills.contains('React');
  
  print('Knows Flutter: $knowsFlutter');
  print('Knows React: $knowsReact');
  
  // 3. SET THEORY OPERATIONS (Mathematical operations)
  Set<String> webSkills = {'React', 'Vue', 'JavaScript', 'Flutter'};
  Set<String> mobileSkills = {'Flutter', 'React Native', 'Swift', 'Kotlin'};
  
  // Union (Combined skills - all unique skills from both sets)
  Set<String> allSkills = developerSkills.union(webSkills);
  print('All skills (Union): $allSkills');
  
  // Intersection (Common skills - skills present in both sets)
  Set<String> commonSkills = developerSkills.intersection(webSkills);
  print('Common skills (Intersection): $commonSkills');
  
  // Difference (Unique to first set - skills in first but not second)
  Set<String> uniqueToMobile = mobileSkills.difference(webSkills);
  print('Unique to mobile (Difference): $uniqueToMobile');
  
  // 4. Set size and emptiness
  print('Total unique skills: ${developerSkills.length}');
  print('Has any skills: ${developerSkills.isNotEmpty}');
  
  // PRACTICAL EXAMPLE: User Role Management
  manageUserRoles();
}

void manageUserRoles() {
  // Real-world scenario: Managing user permissions
  Set<String> adminRoles = {'read', 'write', 'delete', 'manage_users'};
  Set<String> editorRoles = {'read', 'write'};
  Set<String> viewerRoles = {'read'};
  
  // Check what extra permissions admin has over editor
  Set<String> adminOnlyPermissions = adminRoles.difference(editorRoles);
  print('Admin-only permissions: $adminOnlyPermissions');
  
  // Check common permissions between admin and editor
  Set<String> commonPermissions = adminRoles.intersection(editorRoles);
  print('Common permissions: $commonPermissions');
  
  // Grant new permission to all roles
  void grantPermissionToAll(String permission) {
    adminRoles.add(permission);
    editorRoles.add(permission);
    viewerRoles.add(permission);
    print('Granted "$permission" to all users');
  }
  
  grantPermissionToAll('view_analytics');
  
  print('Updated admin roles: $adminRoles');
  print('Updated editor roles: $editorRoles');
  print('Updated viewer roles: $viewerRoles');
}
```

#### 🔧 Functions and Methods - Reusable Code Blocks

**Theoretical Foundation:**
Functions are like **recipes** - they take ingredients (parameters), follow steps (code), and produce a result (return value). They help you **avoid repetition** and **organize code logically**.

**Key Concepts:**
1. **Parameters** = Ingredients you provide to the function
2. **Return Value** = Result the function gives back
3. **Side Effects** = Other things the function does (like printing, saving files)

```dart
// Understanding Functions: Building a Calculator
void functionsDeepDive() {
  // BASIC FUNCTION ANATOMY
  
  // Function signature breakdown:
  // [return_type] [function_name]([parameter_type] [parameter_name]) { ... }
  
  int addNumbers(int a, int b) {
    // Function body - the recipe steps
    int result = a + b;
    return result; // Return the ingredient/result
  }
  
  // PARAMETER PATTERNS - Different ways to pass data
  
  // 1. POSITIONAL PARAMETERS (order matters)
  String greetUser(String name, int age) {
    return 'Hello $name, you are $age years old';
  }
  
  // Usage: order matters!
  print(greetUser('Alice', 25)); // ✅ Correct
  // print(greetUser(25, 'Alice')); // ❌ Error - wrong order
  
  // 2. OPTIONAL POSITIONAL PARAMETERS (can be skipped)
  String greetWithOptional(String name, [int age = 0, String title = 'User']) {
    if (age > 0) {
      return 'Hello $title $name, you are $age years old';
    }
    return 'Hello $title $name';
  }
  
  // Usage examples:
  print(greetWithOptional('Bob'));                    // Uses defaults
  print(greetWithOptional('Carol', 30));              // Provides age
  print(greetWithOptional('David', 35, 'Dr.'));       // Provides all
  
  // 3. NAMED PARAMETERS (self-documenting, order doesn't matter)
  String greetWithNamed({
    required String name,        // Must be provided
    int age = 0,                // Optional with default
    String title = 'User',      // Optional with default
    bool isVip = false          // Optional with default
  }) {
    String greeting = isVip ? 'Welcome VIP' : 'Hello';
    return '$greeting $title $name' + (age > 0 ? ', age $age' : '');
  }
  
  // Usage: clear and flexible!
  print(greetWithNamed(name: 'Emma'));
  print(greetWithNamed(name: 'Frank', age: 28, isVip: true));
  print(greetWithNamed(age: 45, name: 'Grace', title: 'Dr.')); // Order doesn't matter!
  
  // 4. FUNCTION TYPES AND VARIABLES
  
  // Functions are "first-class citizens" - you can store them in variables!
  
  // Store function in variable
  int Function(int, int) mathOperation = addNumbers;
  print('5 + 3 = ${mathOperation(5, 3)}');
  
  // Change the operation
  mathOperation = multiplyNumbers;
  print('5 * 3 = ${mathOperation(5, 3)}');
  
  // 5. ARROW FUNCTIONS (shorthand for simple functions)
  
  // Traditional function
  int square(int number) {
    return number * number;
  }
  
  // Arrow function (same thing, shorter)
  int squareArrow(int number) => number * number;
  
  // Boolean checks are perfect for arrow functions
  bool isEven(int number) => number % 2 == 0;
  bool isAdult(int age) => age >= 18;
  bool isEmpty(String text) => text.length == 0;
  
  print('4 squared: ${square(4)}');
  print('4 squared (arrow): ${squareArrow(4)}');
  print('Is 8 even? ${isEven(8)}');
  print('Is 15 adult? ${isAdult(15)}');
  
  // DEMONSTRATION: Function composition and reusability
  demonstrateCalculator();
}

int multiplyNumbers(int a, int b) => a * b;

// PRACTICAL EXAMPLE: Building a modular calculator
void demonstrateCalculator() {
  print('\n--- Calculator Demo ---');
  
  // Define operations as functions
  double add(double a, double b) => a + b;
  double subtract(double a, double b) => a - b;
  double multiply(double a, double b) => a * b;
  double divide(double a, double b) {
    if (b == 0) {
      print('Error: Cannot divide by zero!');
      return 0;
    }
    return a / b;
  }
  
  // Higher-order function - takes other functions as parameters!
  double calculate(double a, double b, double Function(double, double) operation) {
    return operation(a, b);
  }
  
  // Usage - very flexible!
  double x = 10, y = 5;
  
  print('$x + $y = ${calculate(x, y, add)}');
  print('$x - $y = ${calculate(x, y, subtract)}');  
  print('$x * $y = ${calculate(x, y, multiply)}');
  print('$x / $y = ${calculate(x, y, divide)}');
  
  // You can even create operations on the fly!
  print('$x ^ $y = ${calculate(x, y, (a, b) => math.pow(a, b).toDouble())}');
}

// Import for math operations
import 'dart:math' as math;

// ADVANCED: Function closures (functions that remember variables)
void demonstrateClosures() {
  print('\n--- Closures Demo ---');
  
  // Create a function that "remembers" a multiplier
  Function createMultiplier(int multiplier) {
    // This inner function "closes over" the multiplier variable
    return (int number) => number * multiplier;
  }
  
  // Create specialized functions
  var doubler = createMultiplier(2);     // Function that doubles
  var tripler = createMultiplier(3);     // Function that triples
  
  print('Double 5: ${doubler(5)}');      // 10
  print('Triple 5: ${tripler(5)}');      // 15
  
  // Each function remembers its own multiplier!
  var tenTimes = createMultiplier(10);
  print('Ten times 5: ${tenTimes(5)}');  // 50
}
```

#### 🎯 Function Best Practices & Patterns

```dart
void functionBestPractices() {
  // ✅ GOOD: Descriptive names that explain what the function does
  bool validateEmail(String email) => email.contains('@');
  double calculateTax(double amount, double rate) => amount * rate;
  
  // ❌ BAD: Cryptic names
  bool check(String s) => s.contains('@');
  double calc(double a, double r) => a * r;
  
  // ✅ GOOD: Single responsibility (function does one thing well)
  String formatCurrency(double amount) {
    return '\$${amount.toStringAsFixed(2)}';
  }
  
  bool isValidPrice(double price) {
    return price > 0;
  }
  
  // ❌ BAD: Multiple responsibilities
  String processPrice(double price) {
    // Validation AND formatting in one function - confusing!
    if (price <= 0) return 'Invalid';
    return '\$${price.toStringAsFixed(2)}';
  }
  
  // ✅ GOOD: Use named parameters for clarity
  void sendEmail({
    required String to,
    required String subject,
    required String body,
    List<String> attachments = const [],
    bool isUrgent = false,
  }) {
    print('Sending email to $to: $subject');
    // Implementation
  }
  
  // Usage is self-documenting:
  sendEmail(
    to: 'user@example.com',
    subject: 'Welcome!',
    body: 'Welcome to our app',
    isUrgent: true,
  );
}
```

#### Functions and Methods

```dart
// Function basics
String greetUser(String name, {int age = 0, bool isVip = false}) {
  if (isVip) {
    return 'Welcome VIP $name, age $age!';
  }
  return 'Hello $name, age $age!';
}

// Arrow functions
int square(int number) => number * number;
bool isEven(int number) => number % 2 == 0;

// Higher-order functions
List<T> filterList<T>(List<T> list, bool Function(T) predicate) {
  return list.where(predicate).toList();
}

// Function examples
void functionsExample() {
  // Function calls
  print(greetUser('Alice', age: 25, isVip: true));
  print(greetUser('Bob', age: 30));
  
  // Arrow function calls
  print('Square of 5: ${square(5)}');
  print('Is 8 even? ${isEven(8)}');
  
  // Higher-order function
  List<int> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  var evenNumbers = filterList(numbers, isEven);
  var largeNumbers = filterList(numbers, (n) => n > 5);
  
  print('Even numbers: $evenNumbers');
  print('Large numbers: $largeNumbers');
}
```

### 1.3 Object-Oriented Programming in Dart

#### Classes and Objects

```dart
// Basic class
class Student {
  // Properties
  String name;
  int age;
  List<String> subjects;
  
  // Constructor
  Student(this.name, this.age, this.subjects);
  
  // Named constructor
  Student.withDefaults(this.name) : age = 18, subjects = [];
  
  // Methods
  void addSubject(String subject) {
    subjects.add(subject);
  }
  
  void displayInfo() {
    print('Student: $name');
    print('Age: $age');
    print('Subjects: ${subjects.join(', ')}');
  }
  
  // Getters and setters
  double get averageSubjects => subjects.length.toDouble();
  
  set studentAge(int newAge) {
    if (newAge > 0) {
      age = newAge;
    }
  }
  
  // Override toString
  @override
  String toString() => 'Student(name: $name, age: $age)';
}

// Advanced class features
class BankAccount {
  String _accountNumber; // Private property (underscore)
  double _balance;
  
  BankAccount(this._accountNumber, this._balance);
  
  // Getter for private property
  String get accountNumber => _accountNumber;
  double get balance => _balance;
  
  // Methods
  void deposit(double amount) {
    if (amount > 0) {
      _balance += amount;
      print('Deposited: \$${amount.toStringAsFixed(2)}');
    }
  }
  
  bool withdraw(double amount) {
    if (amount > 0 && amount <= _balance) {
      _balance -= amount;
      print('Withdrawn: \$${amount.toStringAsFixed(2)}');
      return true;
    }
    print('Insufficient funds or invalid amount');
    return false;
  }
  
  void displayBalance() {
    print('Account: $_accountNumber, Balance: \$${_balance.toStringAsFixed(2)}');
  }
}
```

#### Inheritance and Polymorphism

```dart
// Base class
abstract class Vehicle {
  String brand;
  String model;
  int year;
  
  Vehicle(this.brand, this.model, this.year);
  
  // Abstract method (must be implemented by subclasses)
  void startEngine();
  
  // Concrete method
  void displayInfo() {
    print('$year $brand $model');
  }
  
  // Virtual method (can be overridden)
  void honk() {
    print('Beep beep!');
  }
}

// Inheritance
class Car extends Vehicle {
  int numberOfDoors;
  
  Car(String brand, String model, int year, this.numberOfDoors) 
      : super(brand, model, year);
  
  @override
  void startEngine() {
    print('$brand $model engine started with key');
  }
  
  @override
  void honk() {
    print('Car horn: HONK HONK!');
  }
  
  void openTrunk() {
    print('Trunk opened');
  }
}

class Motorcycle extends Vehicle {
  bool hasSidecar;
  
  Motorcycle(String brand, String model, int year, this.hasSidecar) 
      : super(brand, model, year);
  
  @override
  void startEngine() {
    print('$brand $model engine started with button');
  }
  
  @override
  void honk() {
    print('Motorcycle horn: beep beep!');
  }
  
  void doWheelie() {
    print('Doing a wheelie!');
  }
}

// Polymorphism example
void vehicleDemo() {
  List<Vehicle> vehicles = [
    Car('Toyota', 'Camry', 2023, 4),
    Motorcycle('Harley', 'Davidson', 2023, false),
    Car('Tesla', 'Model S', 2023, 4),
  ];
  
  // Polymorphic behavior
  for (Vehicle vehicle in vehicles) {
    vehicle.displayInfo();
    vehicle.startEngine();
    vehicle.honk();
    print('---');
  }
}
```

#### Mixins and Interfaces

```dart
// Mixin - adds functionality to classes
mixin Flyable {
  void fly() {
    print('Flying high in the sky!');
  }
  
  void land() {
    print('Landing safely');
  }
}

mixin Swimmable {
  void swim() {
    print('Swimming in the water');
  }
  
  void dive() {
    print('Diving deep');
  }
}

// Interface (implicit interface)
abstract class Drawable {
  void draw();
  void erase();
}

// Class using mixins and implementing interface
class Duck extends Animal with Flyable, Swimmable implements Drawable {
  Duck(String name) : super(name);
  
  @override
  void makeSound() {
    print('Quack quack!');
  }
  
  @override
  void draw() {
    print('Drawing a duck');
  }
  
  @override
  void erase() {
    print('Erasing the duck');
  }
}

class Animal {
  String name;
  
  Animal(this.name);
  
  void makeSound() {
    print('Some animal sound');
  }
}

// Usage example
void mixinExample() {
  Duck duck = Duck('Donald');
  
  duck.makeSound(); // From Animal
  duck.fly();       // From Flyable mixin
  duck.swim();      // From Swimmable mixin
  duck.draw();      // From Drawable interface
}
```

### 1.4 Asynchronous Programming

#### Futures and async/await

```dart
// Future basics
Future<String> fetchUserData(String userId) async {
  // Simulate network delay
  await Future.delayed(Duration(seconds: 2));
  
  // Simulate API response
  if (userId == 'valid_user') {
    return 'User data: John Doe, john@example.com';
  } else {
    throw Exception('User not found');
  }
}

// Error handling with try-catch
Future<void> getUserInfo() async {
  try {
    print('Fetching user data...');
    String userData = await fetchUserData('valid_user');
    print(userData);
  } catch (e) {
    print('Error: $e');
  } finally {
    print('Fetch operation completed');
  }
}

// Multiple async operations
Future<Map<String, dynamic>> fetchUserProfile(String userId) async {
  try {
    // Parallel execution
    List<Future> futures = [
      fetchUserData(userId),
      fetchUserPreferences(userId),
      fetchUserActivity(userId),
    ];
    
    List<dynamic> results = await Future.wait(futures);
    
    return {
      'userData': results[0],
      'preferences': results[1],
      'activity': results[2],
    };
  } catch (e) {
    throw Exception('Failed to fetch user profile: $e');
  }
}

Future<List<String>> fetchUserPreferences(String userId) async {
  await Future.delayed(Duration(seconds: 1));
  return ['Dark Mode', 'Notifications On', 'Auto-sync'];
}

Future<List<String>> fetchUserActivity(String userId) async {
  await Future.delayed(Duration(seconds: 1));
  return ['Login: 2024-01-01', 'Purchase: 2024-01-05', 'Update: 2024-01-10'];
}
```

#### Streams and Stream Controllers

```dart
import 'dart:async';

// Stream basics
Stream<int> numberStream() async* {
  for (int i = 1; i <= 5; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

// Stream controller
class ChatService {
  final StreamController<String> _messageController = StreamController<String>();
  
  Stream<String> get messages => _messageController.stream;
  
  void sendMessage(String message) {
    _messageController.add(message);
  }
  
  void sendError(String error) {
    _messageController.addError(error);
  }
  
  void dispose() {
    _messageController.close();
  }
}

// Stream usage examples
void streamExamples() async {
  // Basic stream listening
  print('Starting number stream:');
  await for (int number in numberStream()) {
    print('Received: $number');
  }
  
  // Stream controller example
  ChatService chatService = ChatService();
  
  // Listen to messages
  chatService.messages.listen(
    (message) => print('New message: $message'),
    onError: (error) => print('Error: $error'),
    onDone: () => print('Chat ended'),
  );
  
  // Send messages
  chatService.sendMessage('Hello!');
  chatService.sendMessage('How are you?');
  chatService.sendError('Connection lost');
  
  // Clean up
  await Future.delayed(Duration(seconds: 1));
  chatService.dispose();
}
```

---

## 🎨 Part 2: Flutter Fundamentals (Week 2)

### 2.1 Flutter Architecture Overview

```
🏗️ FLUTTER ARCHITECTURE DIAGRAM

┌─────────────────────────────────────────────────────────┐
│                    FLUTTER FRAMEWORK                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐    ┌─────────────────┐            │
│  │   DART APP      │    │    FRAMEWORK    │            │
│  │                 │    │                 │            │
│  │  - Your Code    │◄──►│  - Widgets      │            │
│  │  - Business     │    │  - Rendering    │            │
│  │    Logic        │    │  - Animation    │            │
│  │  - State Mgmt   │    │  - Gestures     │            │
│  └─────────────────┘    └─────────────────┘            │
│           │                       │                    │
│           ▼                       ▼                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │              ENGINE (C++)                       │   │
│  │                                                 │   │
│  │  - Skia Graphics   - Dart Runtime              │   │
│  │  - Text Layout     - Garbage Collection        │   │
│  │  - File I/O        - Thread Management         │   │
│  │  - Network I/O     - Plugin Architecture       │   │
│  └─────────────────────────────────────────────────┘   │
│                           │                            │
└───────────────────────────┼────────────────────────────┘
                           │
┌───────────────────────────▼────────────────────────────┐
│                PLATFORM (iOS/Android)                  │
├─────────────────────────────────────────────────────────┤
│  - Operating System Services                           │
│  - Native UI Components (when needed)                  │
│  - Platform Channels for Native Integration            │
│  - Hardware Access (Camera, GPS, etc.)                 │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Flutter Installation and Setup

#### Complete Development Environment Setup

```bash
# 1. Install Flutter SDK

# macOS
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:`pwd`/flutter/bin"

# Add to ~/.zshrc or ~/.bash_profile
echo 'export PATH="$PATH:/path/to/flutter/bin"' >> ~/.zshrc

# Windows (PowerShell)
# Download Flutter SDK from https://flutter.dev
# Extract to C:\src\flutter
# Add C:\src\flutter\bin to PATH

# 2. Install dependencies

# Android Studio (Required for Android development)
# Download from: https://developer.android.com/studio

# Xcode (Required for iOS development - macOS only)
# Download from Mac App Store

# VS Code with Flutter extensions
code --install-extension dart-code.flutter
code --install-extension dart-code.dart-code

# 3. Verify installation
flutter doctor

# 4. Create first project
flutter create my_first_app
cd my_first_app
flutter run
```

#### Project Structure Deep Dive

```
📁 my_first_app/
├── 📁 android/              # Android-specific code and configuration
│   ├── 📁 app/
│   │   ├── 📄 build.gradle   # Android build configuration
│   │   └── 📁 src/main/
│   │       ├── 📄 AndroidManifest.xml
│   │       └── 📁 kotlin/     # Native Android code
├── 📁 ios/                  # iOS-specific code and configuration
│   ├── 📄 Podfile           # iOS dependencies
│   └── 📁 Runner/
│       ├── 📄 Info.plist     # iOS app configuration
│       └── 📄 AppDelegate.swift
├── 📁 lib/                  # Main Dart code
│   └── 📄 main.dart         # App entry point
├── 📁 test/                 # Unit and widget tests
├── 📁 assets/               # Images, fonts, other assets
├── 📄 pubspec.yaml          # Project dependencies and metadata
├── 📄 analysis_options.yaml # Dart analysis configuration
└── 📄 README.md
```

### 2.3 Your First Flutter App - Deep Dive

```dart
// lib/main.dart - Complete beginner app with explanations
import 'package:flutter/material.dart';

// Entry point of the Flutter app
void main() {
  runApp(MyApp()); // Starts the app with MyApp widget
}

// Root widget of the application
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // App configuration
      title: 'My First Flutter App',
      debugShowCheckedModeBanner: false,
      
      // App theme
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      
      // Home screen
      home: HomeScreen(),
    );
  }
}

// Home screen widget
class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _counter = 0;
  String _message = 'Welcome to Flutter!';

  void _incrementCounter() {
    setState(() {
      _counter++;
      _message = _counter == 0 
          ? 'Welcome to Flutter!'
          : 'You have pressed the button $_counter time${_counter == 1 ? '' : 's'}';
    });
  }

  void _resetCounter() {
    setState(() {
      _counter = 0;
      _message = 'Counter reset!';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // App bar
      appBar: AppBar(
        title: Text('My First Flutter App'),
        backgroundColor: Colors.blue,
        centerTitle: true,
      ),
      
      // Main content
      body: Center(
        child: Padding(
          padding: EdgeInsets.all(20.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Welcome message
              Text(
                _message,
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.w500,
                ),
                textAlign: TextAlign.center,
              ),
              
              SizedBox(height: 30),
              
              // Counter display
              Container(
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.blue.shade50,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: Colors.blue.shade200),
                ),
                child: Text(
                  '$_counter',
                  style: TextStyle(
                    fontSize: 48,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue.shade800,
                  ),
                ),
              ),
              
              SizedBox(height: 30),
              
              // Buttons row
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  // Reset button
                  ElevatedButton.icon(
                    onPressed: _counter > 0 ? _resetCounter : null,
                    icon: Icon(Icons.refresh),
                    label: Text('Reset'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.red,
                      foregroundColor: Colors.white,
                    ),
                  ),
                  
                  // Increment button
                  ElevatedButton.icon(
                    onPressed: _incrementCounter,
                    icon: Icon(Icons.add),
                    label: Text('Add'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green,
                      foregroundColor: Colors.white,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
      
      // Floating action button
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
```

### 2.4 Widget System Deep Dive

#### Understanding the Widget Tree

```
🌳 WIDGET TREE VISUALIZATION

MaterialApp
└── HomeScreen (Scaffold)
    ├── AppBar
    │   └── Text ("My First Flutter App")
    ├── Body (Center)
    │   └── Padding
    │       └── Column
    │           ├── Text (message)
    │           ├── SizedBox (spacer)
    │           ├── Container
    │           │   └── Text (counter)
    │           ├── SizedBox (spacer)
    │           └── Row
    │               ├── ElevatedButton (Reset)
    │               └── ElevatedButton (Add)
    └── FloatingActionButton
```

#### Core Widget Categories

```dart
// 1. LAYOUT WIDGETS - Structure your UI

// Container - Box model widget
Widget containerExample() {
  return Container(
    width: 200,
    height: 100,
    padding: EdgeInsets.all(16),
    margin: EdgeInsets.symmetric(vertical: 8),
    decoration: BoxDecoration(
      color: Colors.blue.shade100,
      borderRadius: BorderRadius.circular(8),
      boxShadow: [
        BoxShadow(
          color: Colors.grey.withOpacity(0.5),
          spreadRadius: 2,
          blurRadius: 5,
          offset: Offset(0, 3),
        ),
      ],
    ),
    child: Text('Styled Container'),
  );
}

// Row - Horizontal layout
Widget rowExample() {
  return Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    crossAxisAlignment: CrossAxisAlignment.center,
    children: [
      Icon(Icons.star, color: Colors.yellow),
      Text('Rating'),
      Text('4.5'),
      Icon(Icons.thumb_up, color: Colors.green),
    ],
  );
}

// Column - Vertical layout
Widget columnExample() {
  return Column(
    mainAxisAlignment: MainAxisAlignment.start,
    crossAxisAlignment: CrossAxisAlignment.stretch,
    children: [
      Text('Title', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
      SizedBox(height: 8),
      Text('Subtitle', style: TextStyle(fontSize: 16, color: Colors.grey)),
      SizedBox(height: 16),
      ElevatedButton(onPressed: () {}, child: Text('Action')),
    ],
  );
}

// Stack - Overlapping widgets
Widget stackExample() {
  return Stack(
    alignment: Alignment.center,
    children: [
      Container(
        width: 200,
        height: 200,
        color: Colors.blue,
      ),
      Container(
        width: 150,
        height: 150,
        color: Colors.red.withOpacity(0.7),
      ),
      Text(
        'Stacked Text',
        style: TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
      ),
    ],
  );
}
```

```dart
// 2. INPUT WIDGETS - User interaction

class InputWidgetsDemo extends StatefulWidget {
  @override
  _InputWidgetsDemoState createState() => _InputWidgetsDemoState();
}

class _InputWidgetsDemoState extends State<InputWidgetsDemo> {
  final TextEditingController _textController = TextEditingController();
  bool _switchValue = false;
  bool _checkboxValue = false;
  double _sliderValue = 50.0;
  String _radioValue = 'Option 1';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Input Widgets Demo')),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Text input
            TextField(
              controller: _textController,
              decoration: InputDecoration(
                labelText: 'Enter your name',
                hintText: 'John Doe',
                prefixIcon: Icon(Icons.person),
                border: OutlineInputBorder(),
              ),
            ),
            
            SizedBox(height: 16),
            
            // Switch
            SwitchListTile(
              title: Text('Enable notifications'),
              value: _switchValue,
              onChanged: (bool value) {
                setState(() {
                  _switchValue = value;
                });
              },
            ),
            
            // Checkbox
            CheckboxListTile(
              title: Text('I agree to terms and conditions'),
              value: _checkboxValue,
              onChanged: (bool? value) {
                setState(() {
                  _checkboxValue = value ?? false;
                });
              },
            ),
            
            // Slider
            Text('Volume: ${_sliderValue.round()}'),
            Slider(
              value: _sliderValue,
              min: 0,
              max: 100,
              divisions: 10,
              label: _sliderValue.round().toString(),
              onChanged: (double value) {
                setState(() {
                  _sliderValue = value;
                });
              },
            ),
            
            // Radio buttons
            Text('Choose an option:'),
            RadioListTile<String>(
              title: Text('Option 1'),
              value: 'Option 1',
              groupValue: _radioValue,
              onChanged: (String? value) {
                setState(() {
                  _radioValue = value!;
                });
              },
            ),
            
            RadioListTile<String>(
              title: Text('Option 2'),
              value: 'Option 2',
              groupValue: _radioValue,
              onChanged: (String? value) {
                setState(() {
                  _radioValue = value!;
                });
              },
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _textController.dispose();
    super.dispose();
  }
}
```

```dart
// 3. DISPLAY WIDGETS - Show information

class DisplayWidgetsDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Display Widgets Demo')),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Text variations
            Text('Default Text'),
            Text(
              'Styled Text',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.blue,
                decoration: TextDecoration.underline,
              ),
            ),
            
            SizedBox(height: 16),
            
            // RichText for mixed styling
            RichText(
              text: TextSpan(
                style: TextStyle(color: Colors.black),
                children: [
                  TextSpan(text: 'This is '),
                  TextSpan(
                    text: 'bold text',
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  TextSpan(text: ' and this is '),
                  TextSpan(
                    text: 'colored text',
                    style: TextStyle(color: Colors.red),
                  ),
                ],
              ),
            ),
            
            SizedBox(height: 16),
            
            // Images
            Text('Image Examples:', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            
            // Network image
            ClipRRect(
              borderRadius: BorderRadius.circular(8),
              child: Image.network(
                'https://picsum.photos/200/100',
                width: 200,
                height: 100,
                fit: BoxFit.cover,
                loadingBuilder: (context, child, loadingProgress) {
                  if (loadingProgress == null) return child;
                  return Container(
                    width: 200,
                    height: 100,
                    child: Center(
                      child: CircularProgressIndicator(
                        value: loadingProgress.expectedTotalBytes != null
                            ? loadingProgress.cumulativeBytesLoaded /
                                loadingProgress.expectedTotalBytes!
                            : null,
                      ),
                    ),
                  );
                },
                errorBuilder: (context, error, stackTrace) {
                  return Container(
                    width: 200,
                    height: 100,
                    color: Colors.grey.shade300,
                    child: Icon(Icons.error),
                  );
                },
              ),
            ),
            
            SizedBox(height: 16),
            
            // Icons
            Text('Icon Examples:', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Row(
              children: [
                Icon(Icons.home, size: 30, color: Colors.blue),
                SizedBox(width: 8),
                Icon(Icons.favorite, size: 30, color: Colors.red),
                SizedBox(width: 8),
                Icon(Icons.star, size: 30, color: Colors.yellow),
                SizedBox(width: 8),
                Icon(Icons.settings, size: 30, color: Colors.grey),
              ],
            ),
            
            SizedBox(height: 16),
            
            // Cards
            Card(
              elevation: 4,
              child: ListTile(
                leading: CircleAvatar(
                  backgroundImage: NetworkImage('https://picsum.photos/50/50'),
                ),
                title: Text('Card Title'),
                subtitle: Text('This is a card with elevation and shadow'),
                trailing: Icon(Icons.arrow_forward_ios),
                onTap: () {
                  print('Card tapped');
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

## 🚀 Part 3: Layouts and UI Design (Week 3)

### 3.1 Advanced Layout Techniques

#### Responsive Design Patterns

```dart
// Responsive layout builder
class ResponsiveWidget extends StatelessWidget {
  final Widget mobile;
  final Widget? tablet;
  final Widget desktop;

  const ResponsiveWidget({
    Key? key,
    required this.mobile,
    this.tablet,
    required this.desktop,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth < 600) {
          return mobile;
        } else if (constraints.maxWidth < 1024) {
          return tablet ?? mobile;
        } else {
          return desktop;
        }
      },
    );
  }
}

// Responsive home page example
class ResponsiveHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ResponsiveWidget(
        mobile: _buildMobileLayout(),
        tablet: _buildTabletLayout(),
        desktop: _buildDesktopLayout(),
      ),
    );
  }

  Widget _buildMobileLayout() {
    return SingleChildScrollView(
      child: Column(
        children: [
          _buildHeader(),
          _buildContent(),
          _buildSidebar(),
          _buildFooter(),
        ],
      ),
    );
  }

  Widget _buildTabletLayout() {
    return Row(
      children: [
        Expanded(
          flex: 2,
          child: Column(
            children: [
              _buildHeader(),
              Expanded(child: _buildContent()),
              _buildFooter(),
            ],
          ),
        ),
        Expanded(
          flex: 1,
          child: _buildSidebar(),
        ),
      ],
    );
  }

  Widget _buildDesktopLayout() {
    return Column(
      children: [
        _buildHeader(),
        Expanded(
          child: Row(
            children: [
              Expanded(flex: 3, child: _buildContent()),
              Expanded(flex: 1, child: _buildSidebar()),
            ],
          ),
        ),
        _buildFooter(),
      ],
    );
  }

  Widget _buildHeader() {
    return Container(
      height: 80,
      color: Colors.blue,
      child: Center(
        child: Text(
          'Header',
          style: TextStyle(color: Colors.white, fontSize: 24),
        ),
      ),
    );
  }

  Widget _buildContent() {
    return Container(
      padding: EdgeInsets.all(16),
      child: Column(
        children: List.generate(10, (index) => 
          Card(
            child: ListTile(
              title: Text('Content Item ${index + 1}'),
              subtitle: Text('This is content item number ${index + 1}'),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildSidebar() {
    return Container(
      color: Colors.grey.shade200,
      padding: EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Sidebar', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 16),
          ...List.generate(5, (index) => 
            Padding(
              padding: EdgeInsets.symmetric(vertical: 4),
              child: Text('Sidebar item ${index + 1}'),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFooter() {
    return Container(
      height: 60,
      color: Colors.grey.shade800,
      child: Center(
        child: Text(
          'Footer',
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}
```

### 3.2 Custom Widgets and Reusability

```dart
// Custom reusable button widget
class CustomButton extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final Color? backgroundColor;
  final Color? textColor;
  final IconData? icon;
  final bool isLoading;
  final ButtonSize size;

  const CustomButton({
    Key? key,
    required this.text,
    required this.onPressed,
    this.backgroundColor,
    this.textColor,
    this.icon,
    this.isLoading = false,
    this.size = ButtonSize.medium,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: isLoading ? null : onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: backgroundColor ?? Theme.of(context).primaryColor,
        foregroundColor: textColor ?? Colors.white,
        padding: _getPadding(),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8),
        ),
      ),
      child: isLoading 
          ? SizedBox(
              width: 16,
              height: 16,
              child: CircularProgressIndicator(strokeWidth: 2),
            )
          : Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                if (icon != null) ...[
                  Icon(icon, size: _getIconSize()),
                  SizedBox(width: 8),
                ],
                Text(text, style: TextStyle(fontSize: _getFontSize())),
              ],
            ),
    );
  }

  EdgeInsets _getPadding() {
    switch (size) {
      case ButtonSize.small:
        return EdgeInsets.symmetric(horizontal: 12, vertical: 8);
      case ButtonSize.medium:
        return EdgeInsets.symmetric(horizontal: 16, vertical: 12);
      case ButtonSize.large:
        return EdgeInsets.symmetric(horizontal: 20, vertical: 16);
    }
  }

  double _getFontSize() {
    switch (size) {
      case ButtonSize.small:
        return 12;
      case ButtonSize.medium:
        return 14;
      case ButtonSize.large:
        return 16;
    }
  }

  double _getIconSize() {
    switch (size) {
      case ButtonSize.small:
        return 16;
      case ButtonSize.medium:
        return 18;
      case ButtonSize.large:
        return 20;
    }
  }
}

enum ButtonSize { small, medium, large }

// Custom card widget
class CustomCard extends StatelessWidget {
  final String title;
  final String? subtitle;
  final Widget? child;
  final VoidCallback? onTap;
  final Color? backgroundColor;
  final double elevation;

  const CustomCard({
    Key? key,
    required this.title,
    this.subtitle,
    this.child,
    this.onTap,
    this.backgroundColor,
    this.elevation = 2,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: elevation,
      color: backgroundColor,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(8),
        child: Padding(
          padding: EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              if (subtitle != null) ...[
                SizedBox(height: 4),
                Text(
                  subtitle!,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: Colors.grey.shade600,
                  ),
                ),
              ],
              if (child != null) ...[
                SizedBox(height: 12),
                child!,
              ],
            ],
          ),
        ),
      ),
    );
  }
}

// Usage example
class CustomWidgetsDemo extends StatefulWidget {
  @override
  _CustomWidgetsDemoState createState() => _CustomWidgetsDemoState();
}

class _CustomWidgetsDemoState extends State<CustomWidgetsDemo> {
  bool _isLoading = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Custom Widgets Demo')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            // Custom buttons
            CustomButton(
              text: 'Small Button',
              size: ButtonSize.small,
              icon: Icons.star,
              onPressed: () => print('Small button pressed'),
            ),
            
            SizedBox(height: 8),
            
            CustomButton(
              text: 'Loading Button',
              isLoading: _isLoading,
              backgroundColor: Colors.green,
              onPressed: () {
                setState(() => _isLoading = !_isLoading);
                Future.delayed(Duration(seconds: 2), () {
                  setState(() => _isLoading = false);
                });
              },
            ),
            
            SizedBox(height: 16),
            
            // Custom cards
            CustomCard(
              title: 'Sample Card',
              subtitle: 'This is a custom card widget',
              onTap: () => print('Card tapped'),
              child: CustomButton(
                text: 'Card Action',
                size: ButtonSize.small,
                onPressed: () => print('Card action pressed'),
              ),
            ),
            
            SizedBox(height: 8),
            
            CustomCard(
              title: 'Another Card',
              backgroundColor: Colors.blue.shade50,
              elevation: 4,
              child: Text('Custom content inside card'),
            ),
          ],
        ),
      ),
    );
  }
}
```

### 3.3 Navigation and Routing

```dart
// Route configuration
class AppRoutes {
  static const String home = '/';
  static const String profile = '/profile';
  static const String settings = '/settings';
  static const String productDetail = '/product';

  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case home:
        return MaterialPageRoute(builder: (_) => HomeScreen());
      case profile:
        return MaterialPageRoute(builder: (_) => ProfileScreen());
      case settings:
        return MaterialPageRoute(builder: (_) => SettingsScreen());
      case productDetail:
        final args = settings.arguments as Map<String, dynamic>?;
        return MaterialPageRoute(
          builder: (_) => ProductDetailScreen(
            productId: args?['id'] ?? '',
            productName: args?['name'] ?? '',
          ),
        );
      default:
        return MaterialPageRoute(
          builder: (_) => Scaffold(
            body: Center(
              child: Text('Route not found: ${settings.name}'),
            ),
          ),
        );
    }
  }
}

// Main app with routing
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Navigation Demo',
      onGenerateRoute: AppRoutes.generateRoute,
      initialRoute: AppRoutes.home,
    );
  }
}

// Navigation examples
class NavigationDemoScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Navigation Demo')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Basic navigation
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, AppRoutes.profile);
              },
              child: Text('Go to Profile'),
            ),
            
            // Navigation with data
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(
                  context, 
                  AppRoutes.productDetail,
                  arguments: {
                    'id': '123',
                    'name': 'Sample Product',
                  },
                );
              },
              child: Text('View Product Detail'),
            ),
            
            // Navigation with result
            ElevatedButton(
              onPressed: () async {
                final result = await Navigator.push<String>(
                  context,
                  MaterialPageRoute(
                    builder: (context) => DataInputScreen(),
                  ),
                );
                
                if (result != null) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text('Received: $result')),
                  );
                }
              },
              child: Text('Get Data from Screen'),
            ),
            
            // Replace current screen
            ElevatedButton(
              onPressed: () {
                Navigator.pushReplacementNamed(context, AppRoutes.settings);
              },
              child: Text('Replace with Settings'),
            ),
            
            // Clear stack and navigate
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamedAndRemoveUntil(
                  context,
                  AppRoutes.home,
                  (route) => false,
                );
              },
              child: Text('Go to Home (Clear Stack)'),
            ),
          ],
        ),
      ),
    );
  }
}

// Screen that returns data
class DataInputScreen extends StatefulWidget {
  @override
  _DataInputScreenState createState() => _DataInputScreenState();
}

class _DataInputScreenState extends State<DataInputScreen> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Enter Data'),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(context, _controller.text);
            },
            child: Text('Done', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(
                labelText: 'Enter some data',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context, _controller.text);
              },
              child: Text('Return Data'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

---

## 📊 Part 4: State Management (Weeks 4-5)

### 4.1 State Management Overview

```
🔄 STATE MANAGEMENT HIERARCHY

┌─────────────────────────────────────────────────────────┐
│               FLUTTER STATE MANAGEMENT                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📊 SIMPLE STATE (Built-in)                           │
│  ├─ setState() → Local widget state                    │
│  ├─ InheritedWidget → Share state down tree           │
│  └─ ValueNotifier → Simple reactive state             │
│                                                         │
│  🏗️ MEDIUM COMPLEXITY                                 │
│  ├─ Provider → Google-recommended, easy to learn       │
│  ├─ Riverpod → Modern evolution of Provider           │
│  └─ GetX → All-in-one solution                        │
│                                                         │
│  🏢 ENTERPRISE LEVEL                                   │
│  ├─ Bloc/Cubit → Predictable state management         │
│  ├─ Redux → Unidirectional data flow                  │
│  └─ MobX → Reactive state management                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Provider State Management

#### Setting up Provider

```yaml
# pubspec.yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.5
```

#### Counter App with Provider

```dart
// 1. Create a state model
import 'package:flutter/foundation.dart';

class CounterModel extends ChangeNotifier {
  int _count = 0;
  
  int get count => _count;
  
  void increment() {
    _count++;
    notifyListeners(); // Notify widgets to rebuild
  }
  
  void decrement() {
    if (_count > 0) {
      _count--;
      notifyListeners();
    }
  }
  
  void reset() {
    _count = 0;
    notifyListeners();
  }
}

// 2. Provide the state to widget tree
import 'package:provider/provider.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => CounterModel(),
      child: MaterialApp(
        title: 'Provider Counter App',
        home: CounterScreen(),
      ),
    );
  }
}

// 3. Consume the state in widgets
class CounterScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Provider Counter')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Counter Value:',
              style: TextStyle(fontSize: 18),
            ),
            
            // Consumer rebuilds only when count changes
            Consumer<CounterModel>(
              builder: (context, counterModel, child) {
                return Text(
                  '${counterModel.count}',
                  style: TextStyle(
                    fontSize: 48,
                    fontWeight: FontWeight.bold,
                    color: counterModel.count > 10 ? Colors.red : Colors.blue,
                  ),
                );
              },
            ),
            
            SizedBox(height: 20),
            
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  onPressed: () {
                    context.read<CounterModel>().decrement();
                  },
                  child: Text('Decrement'),
                ),
                
                ElevatedButton(
                  onPressed: () {
                    context.read<CounterModel>().increment();
                  },
                  child: Text('Increment'),
                ),
                
                ElevatedButton(
                  onPressed: () {
                    context.read<CounterModel>().reset();
                  },
                  child: Text('Reset'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

// Alternative way to consume state
class CounterDisplayWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // watch() rebuilds widget when state changes
    final counterModel = context.watch<CounterModel>();
    
    return Text(
      'Count: ${counterModel.count}',
      style: TextStyle(fontSize: 24),
    );
  }
}
```

#### Shopping Cart Example with Provider

```dart
// Models
class Product {
  final String id;
  final String name;
  final double price;
  final String imageUrl;
  
  Product({
    required this.id,
    required this.name,
    required this.price,
    required this.imageUrl,
  });
}

class CartItem {
  final Product product;
  int quantity;
  
  CartItem({required this.product, this.quantity = 1});
  
  double get totalPrice => product.price * quantity;
}

// Cart state management
class CartModel extends ChangeNotifier {
  final List<CartItem> _items = [];
  
  List<CartItem> get items => List.unmodifiable(_items);
  
  int get itemCount => _items.fold(0, (sum, item) => sum + item.quantity);
  
  double get totalAmount => _items.fold(0.0, (sum, item) => sum + item.totalPrice);
  
  void addItem(Product product) {
    final existingItemIndex = _items.indexWhere(
      (item) => item.product.id == product.id,
    );
    
    if (existingItemIndex >= 0) {
      _items[existingItemIndex].quantity++;
    } else {
      _items.add(CartItem(product: product));
    }
    
    notifyListeners();
  }
  
  void removeItem(String productId) {
    _items.removeWhere((item) => item.product.id == productId);
    notifyListeners();
  }
  
  void updateQuantity(String productId, int quantity) {
    final itemIndex = _items.indexWhere(
      (item) => item.product.id == productId,
    );
    
    if (itemIndex >= 0) {
      if (quantity <= 0) {
        _items.removeAt(itemIndex);
      } else {
        _items[itemIndex].quantity = quantity;
      }
      notifyListeners();
    }
  }
  
  void clearCart() {
    _items.clear();
    notifyListeners();
  }
}

// Products state management
class ProductsModel extends ChangeNotifier {
  final List<Product> _products = [
    Product(
      id: '1',
      name: 'Smartphone',
      price: 699.99,
      imageUrl: 'https://picsum.photos/200/200?random=1',
    ),
    Product(
      id: '2',
      name: 'Laptop',
      price: 1299.99,
      imageUrl: 'https://picsum.photos/200/200?random=2',
    ),
    Product(
      id: '3',
      name: 'Headphones',
      price: 199.99,
      imageUrl: 'https://picsum.photos/200/200?random=3',
    ),
  ];
  
  List<Product> get products => List.unmodifiable(_products);
  
  Product? findById(String id) {
    try {
      return _products.firstWhere((product) => product.id == id);
    } catch (error) {
      return null;
    }
  }
}

// Main app with multiple providers
class ShoppingApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => ProductsModel()),
        ChangeNotifierProvider(create: (context) => CartModel()),
      ],
      child: MaterialApp(
        title: 'Shopping Cart App',
        home: ProductsScreen(),
      ),
    );
  }
}

// Products screen
class ProductsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final productsModel = context.watch<ProductsModel>();
    
    return Scaffold(
      appBar: AppBar(
        title: Text('Products'),
        actions: [
          Consumer<CartModel>(
            builder: (context, cartModel, child) {
              return Stack(
                children: [
                  IconButton(
                    icon: Icon(Icons.shopping_cart),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => CartScreen()),
                      );
                    },
                  ),
                  if (cartModel.itemCount > 0)
                    Positioned(
                      right: 8,
                      top: 8,
                      child: Container(
                        padding: EdgeInsets.all(2),
                        decoration: BoxDecoration(
                          color: Colors.red,
                          borderRadius: BorderRadius.circular(10),
                        ),
                        constraints: BoxConstraints(
                          minWidth: 16,
                          minHeight: 16,
                        ),
                        child: Text(
                          '${cartModel.itemCount}',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 12,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ),
                ],
              );
            },
          ),
        ],
      ),
      body: GridView.builder(
        padding: EdgeInsets.all(16),
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 0.7,
          crossAxisSpacing: 16,
          mainAxisSpacing: 16,
        ),
        itemCount: productsModel.products.length,
        itemBuilder: (context, index) {
          final product = productsModel.products[index];
          return ProductCard(product: product);
        },
      ),
    );
  }
}

// Product card widget
class ProductCard extends StatelessWidget {
  final Product product;
  
  const ProductCard({Key? key, required this.product}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Image.network(
              product.imageUrl,
              fit: BoxFit.cover,
              width: double.infinity,
            ),
          ),
          Padding(
            padding: EdgeInsets.all(8),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  product.name,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
                SizedBox(height: 4),
                Text(
                  '\$${product.price.toStringAsFixed(2)}',
                  style: TextStyle(
                    color: Colors.green,
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 8),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      context.read<CartModel>().addItem(product);
                      
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text('${product.name} added to cart'),
                          duration: Duration(seconds: 1),
                        ),
                      );
                    },
                    child: Text('Add to Cart'),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// Cart screen
class CartScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
        actions: [
          Consumer<CartModel>(
            builder: (context, cartModel, child) {
              return TextButton(
                onPressed: cartModel.items.isEmpty ? null : () {
                  cartModel.clearCart();
                },
                child: Text(
                  'Clear',
                  style: TextStyle(color: Colors.white),
                ),
              );
            },
          ),
        ],
      ),
      body: Consumer<CartModel>(
        builder: (context, cartModel, child) {
          if (cartModel.items.isEmpty) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.shopping_cart_outlined, size: 64, color: Colors.grey),
                  SizedBox(height: 16),
                  Text(
                    'Your cart is empty',
                    style: TextStyle(fontSize: 18, color: Colors.grey),
                  ),
                ],
              ),
            );
          }
          
          return Column(
            children: [
              Expanded(
                child: ListView.builder(
                  itemCount: cartModel.items.length,
                  itemBuilder: (context, index) {
                    final item = cartModel.items[index];
                    return CartItemWidget(item: item);
                  },
                ),
              ),
              Container(
                padding: EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.grey.shade100,
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(16),
                    topRight: Radius.circular(16),
                  ),
                ),
                child: Column(
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(
                          'Total: ',
                          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                        ),
                        Text(
                          '\$${cartModel.totalAmount.toStringAsFixed(2)}',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.green,
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: 16),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {
                          // Implement checkout logic
                          showDialog(
                            context: context,
                            builder: (context) => AlertDialog(
                              title: Text('Checkout'),
                              content: Text('Order placed successfully!'),
                              actions: [
                                TextButton(
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                    cartModel.clearCart();
                                    Navigator.of(context).pop();
                                  },
                                  child: Text('OK'),
                                ),
                              ],
                            ),
                          );
                        },
                        child: Text('Checkout'),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}

// Cart item widget
class CartItemWidget extends StatelessWidget {
  final CartItem item;
  
  const CartItemWidget({Key? key, required this.item}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      child: Padding(
        padding: EdgeInsets.all(8),
        child: Row(
          children: [
            Image.network(
              item.product.imageUrl,
              width: 60,
              height: 60,
              fit: BoxFit.cover,
            ),
            SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    item.product.name,
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 4),
                  Text(
                    '\$${item.product.price.toStringAsFixed(2)} each',
                    style: TextStyle(color: Colors.grey.shade600),
                  ),
                  SizedBox(height: 4),
                  Text(
                    'Total: \$${item.totalPrice.toStringAsFixed(2)}',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.green,
                    ),
                  ),
                ],
              ),
            ),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(
                  onPressed: item.quantity > 1 ? () {
                    context.read<CartModel>().updateQuantity(
                      item.product.id,
                      item.quantity - 1,
                    );
                  } : null,
                  icon: Icon(Icons.remove),
                ),
                Text('${item.quantity}', style: TextStyle(fontSize: 16)),
                IconButton(
                  onPressed: () {
                    context.read<CartModel>().updateQuantity(
                      item.product.id,
                      item.quantity + 1,
                    );
                  },
                  icon: Icon(Icons.add),
                ),
              ],
            ),
            IconButton(
              onPressed: () {
                context.read<CartModel>().removeItem(item.product.id);
              },
              icon: Icon(Icons.delete, color: Colors.red),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

## 🌐 Part 5: APIs and Data Integration (Week 6)

### 5.1 HTTP Requests with Dio

```yaml
# pubspec.yaml
dependencies:
  dio: ^5.3.2
  json_annotation: ^4.8.1

dev_dependencies:
  json_serializable: ^6.7.1
  build_runner: ^2.4.7
```

#### API Service Architecture

```dart
// API service layer
import 'package:dio/dio.dart';

class ApiService {
  static final ApiService _instance = ApiService._internal();
  late Dio _dio;
  
  factory ApiService() => _instance;
  
  ApiService._internal() {
    _dio = Dio();
    _dio.options.baseUrl = 'https://api.example.com/v1';
    _dio.options.connectTimeout = Duration(seconds: 10);
    _dio.options.receiveTimeout = Duration(seconds: 10);
    
    // Request interceptor
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) {
          print('REQUEST: ${options.method} ${options.path}');
          // Add auth token if available
          final token = getStoredToken();
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          handler.next(options);
        },
        onResponse: (response, handler) {
          print('RESPONSE: ${response.statusCode}');
          handler.next(response);
        },
        onError: (error, handler) {
          print('ERROR: ${error.message}');
          handler.next(error);
        },
      ),
    );
  }
  
  String? getStoredToken() {
    // Implement token storage logic
    return null;
  }
  
  // Generic GET request
  Future<T> get<T>(
    String path, {
    Map<String, dynamic>? queryParameters,
    T Function(dynamic)? fromJson,
  }) async {
    try {
      final response = await _dio.get(path, queryParameters: queryParameters);
      if (fromJson != null) {
        return fromJson(response.data);
      }
      return response.data as T;
    } catch (e) {
      throw _handleError(e);
    }
  }
  
  // Generic POST request
  Future<T> post<T>(
    String path, {
    dynamic data,
    T Function(dynamic)? fromJson,
  }) async {
    try {
      final response = await _dio.post(path, data: data);
      if (fromJson != null) {
        return fromJson(response.data);
      }
      return response.data as T;
    } catch (e) {
      throw _handleError(e);
    }
  }
  
  Exception _handleError(dynamic error) {
    if (error is DioException) {
      switch (error.type) {
        case DioExceptionType.connectionTimeout:
          return Exception('Connection timeout');
        case DioExceptionType.receiveTimeout:
          return Exception('Receive timeout');
        case DioExceptionType.badResponse:
          return Exception('Server error: ${error.response?.statusCode}');
        default:
          return Exception('Network error: ${error.message}');
      }
    }
    return Exception('Unknown error: $error');
  }
}
```

### 5.2 Data Models with JSON Serialization

```dart
// User model with JSON serialization
import 'package:json_annotation/json_annotation.dart';

part 'user.g.dart'; // Generated file

@JsonSerializable()
class User {
  final String id;
  final String name;
  final String email;
  final String? avatar;
  final DateTime createdAt;
  final List<String> roles;
  
  User({
    required this.id,
    required this.name,
    required this.email,
    this.avatar,
    required this.createdAt,
    required this.roles,
  });
  
  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}

// Generate JSON serialization code:
// flutter packages pub run build_runner build

// Repository pattern for API calls
class UserRepository {
  final ApiService _apiService = ApiService();
  
  Future<List<User>> getUsers({int page = 1, int limit = 20}) async {
    try {
      final response = await _apiService.get<Map<String, dynamic>>(
        '/users',
        queryParameters: {'page': page, 'limit': limit},
      );
      
      final List<dynamic> usersJson = response['data'];
      return usersJson.map((json) => User.fromJson(json)).toList();
    } catch (e) {
      throw Exception('Failed to fetch users: $e');
    }
  }
  
  Future<User> getUserById(String id) async {
    try {
      final response = await _apiService.get<Map<String, dynamic>>('/users/$id');
      return User.fromJson(response['data']);
    } catch (e) {
      throw Exception('Failed to fetch user: $e');
    }
  }
  
  Future<User> createUser(CreateUserRequest request) async {
    try {
      final response = await _apiService.post<Map<String, dynamic>>(
        '/users',
        data: request.toJson(),
      );
      return User.fromJson(response['data']);
    } catch (e) {
      throw Exception('Failed to create user: $e');
    }
  }
  
  Future<User> updateUser(String id, UpdateUserRequest request) async {
    try {
      final response = await _apiService.post<Map<String, dynamic>>(
        '/users/$id',
        data: request.toJson(),
      );
      return User.fromJson(response['data']);
    } catch (e) {
      throw Exception('Failed to update user: $e');
    }
  }
}

@JsonSerializable()
class CreateUserRequest {
  final String name;
  final String email;
  final String password;
  
  CreateUserRequest({
    required this.name,
    required this.email,
    required this.password,
  });
  
  Map<String, dynamic> toJson() => _$CreateUserRequestToJson(this);
}
```

### 5.3 State Management with API Integration

```dart
// Users state management with API
class UsersModel extends ChangeNotifier {
  final UserRepository _userRepository = UserRepository();
  
  List<User> _users = [];
  bool _isLoading = false;
  String? _error;
  int _currentPage = 1;
  bool _hasMoreData = true;
  
  // Getters
  List<User> get users => List.unmodifiable(_users);
  bool get isLoading => _isLoading;
  String? get error => _error;
  bool get hasMoreData => _hasMoreData;
  
  // Load initial users
  Future<void> loadUsers() async {
    if (_isLoading) return;
    
    _setLoading(true);
    _error = null;
    
    try {
      final newUsers = await _userRepository.getUsers(page: 1);
      _users = newUsers;
      _currentPage = 1;
      _hasMoreData = newUsers.length == 20; // Assuming 20 is the page size
    } catch (e) {
      _error = e.toString();
    } finally {
      _setLoading(false);
    }
  }
  
  // Load more users (pagination)
  Future<void> loadMoreUsers() async {
    if (_isLoading || !_hasMoreData) return;
    
    _setLoading(true);
    
    try {
      final newUsers = await _userRepository.getUsers(page: _currentPage + 1);
      if (newUsers.isNotEmpty) {
        _users.addAll(newUsers);
        _currentPage++;
        _hasMoreData = newUsers.length == 20;
      } else {
        _hasMoreData = false;
      }
    } catch (e) {
      _error = e.toString();
    } finally {
      _setLoading(false);
    }
  }
  
  // Add new user
  Future<bool> addUser(CreateUserRequest request) async {
    try {
      final newUser = await _userRepository.createUser(request);
      _users.insert(0, newUser);
      notifyListeners();
      return true;
    } catch (e) {
      _error = e.toString();
      notifyListeners();
      return false;
    }
  }
  
  // Update user
  Future<bool> updateUser(String id, UpdateUserRequest request) async {
    try {
      final updatedUser = await _userRepository.updateUser(id, request);
      final index = _users.indexWhere((user) => user.id == id);
      if (index >= 0) {
        _users[index] = updatedUser;
        notifyListeners();
      }
      return true;
    } catch (e) {
      _error = e.toString();
      notifyListeners();
      return false;
    }
  }
  
  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }
  
  void clearError() {
    _error = null;
    notifyListeners();
  }
}

// Users screen with infinite scroll
class UsersScreen extends StatefulWidget {
  @override
  _UsersScreenState createState() => _UsersScreenState();
}

class _UsersScreenState extends State<UsersScreen> {
  final ScrollController _scrollController = ScrollController();
  
  @override
  void initState() {
    super.initState();
    
    // Load initial data
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<UsersModel>().loadUsers();
    });
    
    // Setup infinite scroll
    _scrollController.addListener(_onScroll);
  }
  
  void _onScroll() {
    if (_scrollController.position.pixels == _scrollController.position.maxScrollExtent) {
      context.read<UsersModel>().loadMoreUsers();
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Users'),
        actions: [
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AddUserScreen()),
              );
            },
          ),
        ],
      ),
      body: Consumer<UsersModel>(
        builder: (context, usersModel, child) {
          if (usersModel.isLoading && usersModel.users.isEmpty) {
            return Center(child: CircularProgressIndicator());
          }
          
          if (usersModel.error != null && usersModel.users.isEmpty) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.error_outline, size: 64, color: Colors.red),
                  SizedBox(height: 16),
                  Text('Error: ${usersModel.error}'),
                  SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: () {
                      usersModel.clearError();
                      usersModel.loadUsers();
                    },
                    child: Text('Retry'),
                  ),
                ],
              ),
            );
          }
          
          return RefreshIndicator(
            onRefresh: usersModel.loadUsers,
            child: ListView.builder(
              controller: _scrollController,
              itemCount: usersModel.users.length + (usersModel.hasMoreData ? 1 : 0),
              itemBuilder: (context, index) {
                if (index == usersModel.users.length) {
                  return Center(
                    child: Padding(
                      padding: EdgeInsets.all(16),
                      child: CircularProgressIndicator(),
                    ),
                  );
                }
                
                final user = usersModel.users[index];
                return UserListTile(user: user);
              },
            ),
          );
        },
      ),
    );
  }
  
  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }
}
```

---

## 🏗️ Part 6: Architecture Patterns (Week 7)

### 6.1 Clean Architecture in Flutter

```
🏛️ CLEAN ARCHITECTURE LAYERS

┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                     │
├─────────────────────────────────────────────────────────┤
│  📱 UI (Widgets)    🎭 State (Provider/Bloc)           │
│  ├─ Screens         ├─ State Management                 │
│  ├─ Widgets         ├─ UI Logic                        │
│  └─ Navigation      └─ Validation                      │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                   DOMAIN LAYER                          │
├─────────────────────────────────────────────────────────┤
│  🏗️ Use Cases      📋 Entities      🔌 Repository      │
│  ├─ Business Logic  ├─ Core Models   ├─ Interfaces     │
│  ├─ App Services    ├─ Value Objects ├─ Contracts      │
│  └─ Validation      └─ Domain Rules  └─ Abstractions   │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                    DATA LAYER                           │
├─────────────────────────────────────────────────────────┤
│  🌐 Remote Data     💾 Local Data    🔌 Implementations │
│  ├─ API Services    ├─ Database      ├─ Repository Impl │
│  ├─ Network Models  ├─ Cache         ├─ Data Sources    │
│  └─ HTTP Clients    └─ Preferences   └─ Mappers         │
└─────────────────────────────────────────────────────────┘
```

#### Clean Architecture Implementation

```dart
// 1. DOMAIN LAYER

// Entities (Business objects)
class UserEntity {
  final String id;
  final String name;
  final String email;
  final DateTime createdAt;
  
  UserEntity({
    required this.id,
    required this.name,
    required this.email,
    required this.createdAt,
  });
}

// Repository interface (Domain layer)
abstract class UserRepository {
  Future<List<UserEntity>> getUsers();
  Future<UserEntity> getUserById(String id);
  Future<UserEntity> createUser(CreateUserEntity user);
  Future<UserEntity> updateUser(String id, UpdateUserEntity user);
  Future<void> deleteUser(String id);
}

// Use cases (Business logic)
class GetUsersUseCase {
  final UserRepository repository;
  
  GetUsersUseCase(this.repository);
  
  Future<List<UserEntity>> execute() async {
    return await repository.getUsers();
  }
}

class CreateUserUseCase {
  final UserRepository repository;
  
  CreateUserUseCase(this.repository);
  
  Future<UserEntity> execute(CreateUserEntity user) async {
    // Business logic validation
    if (user.name.isEmpty) {
      throw Exception('Name cannot be empty');
    }
    
    if (!_isValidEmail(user.email)) {
      throw Exception('Invalid email format');
    }
    
    return await repository.createUser(user);
  }
  
  bool _isValidEmail(String email) {
    return RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(email);
  }
}

// 2. DATA LAYER

// Data models (API response models)
@JsonSerializable()
class UserModel {
  final String id;
  final String name;
  final String email;
  @JsonKey(name: 'created_at')
  final String createdAt;
  
  UserModel({
    required this.id,
    required this.name,
    required this.email,
    required this.createdAt,
  });
  
  factory UserModel.fromJson(Map<String, dynamic> json) => _$UserModelFromJson(json);
  Map<String, dynamic> toJson() => _$UserModelToJson(this);
  
  // Convert to domain entity
  UserEntity toEntity() {
    return UserEntity(
      id: id,
      name: name,
      email: email,
      createdAt: DateTime.parse(createdAt),
    );
  }
}

// Repository implementation
class UserRepositoryImpl implements UserRepository {
  final ApiService _apiService;
  
  UserRepositoryImpl(this._apiService);
  
  @override
  Future<List<UserEntity>> getUsers() async {
    try {
      final response = await _apiService.get<Map<String, dynamic>>('/users');
      final List<dynamic> usersJson = response['data'];
      final userModels = usersJson.map((json) => UserModel.fromJson(json)).toList();
      return userModels.map((model) => model.toEntity()).toList();
    } catch (e) {
      throw Exception('Failed to fetch users: $e');
    }
  }
  
  @override
  Future<UserEntity> getUserById(String id) async {
    try {
      final response = await _apiService.get<Map<String, dynamic>>('/users/$id');
      final userModel = UserModel.fromJson(response['data']);
      return userModel.toEntity();
    } catch (e) {
      throw Exception('Failed to fetch user: $e');
    }
  }
  
  @override
  Future<UserEntity> createUser(CreateUserEntity user) async {
    try {
      final response = await _apiService.post<Map<String, dynamic>>(
        '/users',
        data: {
          'name': user.name,
          'email': user.email,
        },
      );
      final userModel = UserModel.fromJson(response['data']);
      return userModel.toEntity();
    } catch (e) {
      throw Exception('Failed to create user: $e');
    }
  }
  
  // Implement other methods...
}
```

---

## 🎨 Part 7: Advanced UI and Animations (Week 8)

### 7.1 Custom Animations

```dart
// Custom animation controller
class AnimatedCounterWidget extends StatefulWidget {
  final int value;
  final Duration duration;
  
  const AnimatedCounterWidget({
    Key? key,
    required this.value,
    this.duration = const Duration(milliseconds: 500),
  }) : super(key: key);
  
  @override
  _AnimatedCounterWidgetState createState() => _AnimatedCounterWidgetState();
}

class _AnimatedCounterWidgetState extends State<AnimatedCounterWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;
  int _previousValue = 0;
  
  @override
  void initState() {
    super.initState();
    
    _controller = AnimationController(
      duration: widget.duration,
      vsync: this,
    );
    
    _animation = Tween<double>(
      begin: 0,
      end: widget.value.toDouble(),
    ).animate(CurvedAnimation(
      parent: _controller,
      curve: Curves.easeInOut,
    ));
    
    _controller.forward();
  }
  
  @override
  void didUpdateWidget(AnimatedCounterWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    
    if (oldWidget.value != widget.value) {
      _previousValue = oldWidget.value;
      _animation = Tween<double>(
        begin: _previousValue.toDouble(),
        end: widget.value.toDouble(),
      ).animate(CurvedAnimation(
        parent: _controller,
        curve: Curves.easeInOut,
      ));
      
      _controller.reset();
      _controller.forward();
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Text(
          _animation.value.toInt().toString(),
          style: TextStyle(
            fontSize: 48,
            fontWeight: FontWeight.bold,
            color: Colors.blue,
          ),
        );
      },
    );
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}

// Hero animations for page transitions
class ProductListScreen extends StatelessWidget {
  final List<Product> products = [
    Product(id: '1', name: 'Smartphone', price: 699.99, imageUrl: 'https://picsum.photos/200/200?random=1'),
    Product(id: '2', name: 'Laptop', price: 1299.99, imageUrl: 'https://picsum.photos/200/200?random=2'),
  ];
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Products')),
      body: GridView.builder(
        padding: EdgeInsets.all(16),
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 0.8,
        ),
        itemCount: products.length,
        itemBuilder: (context, index) {
          final product = products[index];
          return GestureDetector(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ProductDetailScreen(product: product),
                ),
              );
            },
            child: Card(
              child: Column(
                children: [
                  Expanded(
                    child: Hero(
                      tag: 'product-${product.id}',
                      child: Image.network(
                        product.imageUrl,
                        fit: BoxFit.cover,
                        width: double.infinity,
                      ),
                    ),
                  ),
                  Padding(
                    padding: EdgeInsets.all(8),
                    child: Column(
                      children: [
                        Text(
                          product.name,
                          style: TextStyle(fontWeight: FontWeight.bold),
                        ),
                        Text('\$${product.price}'),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class ProductDetailScreen extends StatelessWidget {
  final Product product;
  
  const ProductDetailScreen({Key? key, required this.product}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            expandedHeight: 300,
            pinned: true,
            flexibleSpace: FlexibleSpaceBar(
              background: Hero(
                tag: 'product-${product.id}',
                child: Image.network(
                  product.imageUrl,
                  fit: BoxFit.cover,
                ),
              ),
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    product.name,
                    style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 8),
                  Text(
                    '\$${product.price}',
                    style: TextStyle(fontSize: 20, color: Colors.green),
                  ),
                  SizedBox(height: 16),
                  Text(
                    'Product Description',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'This is a detailed description of the ${product.name}. '
                    'It includes all the features and benefits that make this product special.',
                    style: TextStyle(fontSize: 16),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
```

---

## 📱 Part 8: Real-World Project - Complete Social Media App

### 8.1 Project Architecture Overview

```
📱 SOCIAL MEDIA APP ARCHITECTURE

┌─────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                    │
├─────────────────────────────────────────────────────────┤
│  📱 Screens         🎭 State Management                │
│  ├─ Auth Screens    ├─ AuthProvider                     │
│  ├─ Feed Screens    ├─ PostsProvider                    │
│  ├─ Profile Screens ├─ UserProvider                     │
│  ├─ Chat Screens    ├─ ChatProvider                     │
│  └─ Camera Screens  └─ MediaProvider                    │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                   BUSINESS LOGIC                        │
├─────────────────────────────────────────────────────────┤
│  🏗️ Use Cases       📋 Entities                        │
│  ├─ Authentication  ├─ User Entity                      │
│  ├─ Post Management ├─ Post Entity                      │
│  ├─ User Management ├─ Comment Entity                   │
│  ├─ Chat System     ├─ Chat Entity                      │
│  └─ Media Upload    └─ Media Entity                     │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                     DATA LAYER                          │
├─────────────────────────────────────────────────────────┤
│  🌐 Remote Data     💾 Local Data                      │
│  ├─ REST APIs       ├─ SQLite Database                  │
│  ├─ Firebase        ├─ Shared Preferences               │
│  ├─ Cloud Storage   ├─ Secure Storage                   │
│  └─ Push Notifications └─ Cache Management              │
└─────────────────────────────────────────────────────────┘
```

### 8.2 Project Structure

```
📁 social_media_app/
├── 📁 lib/
│   ├── 📄 main.dart
│   ├── 📁 core/                    # Core utilities and constants
│   │   ├── 📁 constants/
│   │   │   ├── 📄 app_colors.dart
│   │   │   ├── 📄 app_text_styles.dart
│   │   │   └── 📄 api_constants.dart
│   │   ├── 📁 utils/
│   │   │   ├── 📄 validators.dart
│   │   │   ├── 📄 helpers.dart
│   │   │   └── 📄 extensions.dart
│   │   └── 📁 errors/
│   │       └── 📄 exceptions.dart
│   ├── 📁 data/                   # Data layer
│   │   ├── 📁 models/
│   │   │   ├── 📄 user_model.dart
│   │   │   ├── 📄 post_model.dart
│   │   │   └── 📄 comment_model.dart
│   │   ├── 📁 repositories/
│   │   │   ├── 📄 user_repository_impl.dart
│   │   │   └── 📄 post_repository_impl.dart
│   │   ├── 📁 datasources/
│   │   │   ├── 📄 remote_data_source.dart
│   │   │   └── 📄 local_data_source.dart
│   │   └── 📁 services/
│   │       ├── 📄 api_service.dart
│   │       ├── 📄 database_service.dart
│   │       └── 📄 storage_service.dart
│   ├── 📁 domain/                 # Domain layer
│   │   ├── 📁 entities/
│   │   │   ├── 📄 user_entity.dart
│   │   │   ├── 📄 post_entity.dart
│   │   │   └── 📄 comment_entity.dart
│   │   ├── 📁 repositories/
│   │   │   ├── 📄 user_repository.dart
│   │   │   └── 📄 post_repository.dart
│   │   └── 📁 usecases/
│   │       ├── 📄 auth_usecases.dart
│   │       ├── 📄 post_usecases.dart
│   │       └── 📄 user_usecases.dart
│   └── 📁 presentation/           # Presentation layer
│       ├── 📁 screens/
│       │   ├── 📁 auth/
│       │   │   ├── 📄 login_screen.dart
│       │   │   ├── 📄 register_screen.dart
│       │   │   └── 📄 forgot_password_screen.dart
│       │   ├── 📁 home/
│       │   │   ├── 📄 home_screen.dart
│       │   │   ├── 📄 feed_screen.dart
│       │   │   └── 📄 search_screen.dart
│       │   ├── 📁 profile/
│       │   │   ├── 📄 profile_screen.dart
│       │   │   └── 📄 edit_profile_screen.dart
│       │   └── 📁 posts/
│       │       ├── 📄 create_post_screen.dart
│       │       └── 📄 post_detail_screen.dart
│       ├── 📁 widgets/
│       │   ├── 📁 common/
│       │   │   ├── 📄 custom_button.dart
│       │   │   ├── 📄 loading_indicator.dart
│       │   │   └── 📄 error_widget.dart
│       │   └── 📁 post/
│       │       ├── 📄 post_card.dart
│       │       └── 📄 comment_widget.dart
│       └── 📁 providers/
│           ├── 📄 auth_provider.dart
│           ├── 📄 posts_provider.dart
│           └── 📄 user_provider.dart
```

---

## 🚀 **Complete Learning Roadmap Summary**

### **Phase 1: Foundation (Weeks 1-3) ✅**
- **Week 1:** Dart fundamentals, OOP, async programming
- **Week 2:** Flutter basics, widgets, layouts  
- **Week 3:** Advanced UI, navigation, custom widgets

### **Phase 2: Intermediate (Weeks 4-8)**
- **Week 4-5:** State management (Provider, Riverpod, Bloc)
- **Week 6:** APIs, HTTP, JSON handling
- **Week 7:** Architecture patterns, Clean Architecture
- **Week 8:** Advanced animations and custom UI

### **Phase 3: Advanced (Weeks 9-12)**
- **Week 9:** Testing (Unit, Widget, Integration)
- **Week 10:** Performance optimization, debugging
- **Week 11:** Platform integration (cameras, maps, notifications)
- **Week 12:** App store deployment, CI/CD

### **Phase 4: Expert (Weeks 13-16)**
- **Week 13:** Custom plugins and packages
- **Week 14:** Advanced architecture patterns
- **Week 15:** Production debugging and monitoring
- **Week 16:** Portfolio projects and real-world applications

## 💡 **Key Success Tips:**

1. **Build Along:** Code every example - don't just read
2. **Practice Daily:** 2-3 hours consistent daily practice  
3. **Real Projects:** Build actual apps you would use
4. **Community:** Join Flutter Discord/Reddit communities
5. **Documentation:** Read official Flutter docs regularly

---

## 🧪 Part 9: Testing Mastery (Week 9)

### 9.1 Testing Pyramid in Flutter

```
🏗️ FLUTTER TESTING PYRAMID

                    ┌─────────────┐
                    │     E2E     │ ← Few, Expensive, Slow
                    │ Integration │   (Real device testing)
                    └─────────────┘
                  ┌─────────────────┐
                  │     WIDGET      │ ← Some, Medium cost
                  │   Integration   │   (UI component testing)
                  └─────────────────┘
               ┌────────────────────────┐
               │        UNIT           │ ← Many, Fast, Cheap
               │    Business Logic     │   (Pure Dart testing)
               └────────────────────────┘
```

#### Unit Testing Examples

```dart
// test/models/user_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:your_app/models/user.dart';

void main() {
  group('User Model Tests', () {
    test('should create user from JSON', () {
      // Arrange
      final json = {
        'id': '123',
        'name': 'John Doe',
        'email': 'john@example.com',
        'created_at': '2023-01-01T00:00:00Z',
      };
      
      // Act
      final user = User.fromJson(json);
      
      // Assert
      expect(user.id, equals('123'));
      expect(user.name, equals('John Doe'));
      expect(user.email, equals('john@example.com'));
      expect(user.createdAt, isA<DateTime>());
    });
    
    test('should convert user to JSON', () {
      // Arrange
      final user = User(
        id: '123',
        name: 'John Doe',
        email: 'john@example.com',
        createdAt: DateTime.parse('2023-01-01T00:00:00Z'),
        roles: ['user'],
      );
      
      // Act
      final json = user.toJson();
      
      // Assert
      expect(json['id'], equals('123'));
      expect(json['name'], equals('John Doe'));
      expect(json['email'], equals('john@example.com'));
    });
    
    test('should validate email format', () {
      // Arrange
      const validEmail = 'test@example.com';
      const invalidEmail = 'invalid-email';
      
      // Act & Assert
      expect(User.isValidEmail(validEmail), isTrue);
      expect(User.isValidEmail(invalidEmail), isFalse);
    });
  });
}

// test/usecases/auth_usecase_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';
import 'package:mockito/annotations.dart';
import 'package:your_app/domain/repositories/auth_repository.dart';
import 'package:your_app/domain/usecases/auth_usecases.dart';

@GenerateMocks([AuthRepository])
import 'auth_usecase_test.mocks.dart';

void main() {
  late AuthUseCases authUseCases;
  late MockAuthRepository mockAuthRepository;
  
  setUp(() {
    mockAuthRepository = MockAuthRepository();
    authUseCases = AuthUseCases(mockAuthRepository);
  });
  
  group('AuthUseCases', () {
    test('should login user successfully', () async {
      // Arrange
      const email = 'test@example.com';
      const password = 'password123';
      final user = User(
        id: '123',
        name: 'Test User',
        email: email,
        createdAt: DateTime.now(),
        roles: ['user'],
      );
      
      when(mockAuthRepository.login(email, password))
          .thenAnswer((_) async => user);
      
      // Act
      final result = await authUseCases.login(email, password);
      
      // Assert
      expect(result, equals(user));
      verify(mockAuthRepository.login(email, password)).called(1);
    });
    
    test('should throw exception for invalid credentials', () async {
      // Arrange
      const email = 'test@example.com';
      const password = 'wrongpassword';
      
      when(mockAuthRepository.login(email, password))
          .thenThrow(Exception('Invalid credentials'));
      
      // Act & Assert
      expect(
        () => authUseCases.login(email, password),
        throwsA(isA<Exception>()),
      );
    });
  });
}
```

#### Widget Testing Examples

```dart
// test/widgets/counter_widget_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:your_app/models/counter_model.dart';
import 'package:your_app/widgets/counter_widget.dart';

void main() {
  group('CounterWidget Tests', () {
    testWidgets('should display initial counter value', (WidgetTester tester) async {
      // Arrange
      final counterModel = CounterModel();
      
      // Build widget
      await tester.pumpWidget(
        ChangeNotifierProvider.value(
          value: counterModel,
          child: MaterialApp(
            home: Scaffold(body: CounterWidget()),
          ),
        ),
      );
      
      // Assert
      expect(find.text('0'), findsOneWidget);
    });
    
    testWidgets('should increment counter when button is pressed', (WidgetTester tester) async {
      // Arrange
      final counterModel = CounterModel();
      
      await tester.pumpWidget(
        ChangeNotifierProvider.value(
          value: counterModel,
          child: MaterialApp(
            home: Scaffold(body: CounterWidget()),
          ),
        ),
      );
      
      // Act
      await tester.tap(find.byIcon(Icons.add));
      await tester.pump();
      
      // Assert
      expect(find.text('1'), findsOneWidget);
    });
    
    testWidgets('should show error message for invalid input', (WidgetTester tester) async {
      // Arrange
      await tester.pumpWidget(
        MaterialApp(
          home: Scaffold(body: LoginForm()),
        ),
      );
      
      // Act
      await tester.enterText(find.byKey(Key('email-field')), 'invalid-email');
      await tester.tap(find.byKey(Key('login-button')));
      await tester.pump();
      
      // Assert
      expect(find.text('Please enter a valid email'), findsOneWidget);
    });
  });
}
```

### 9.2 Integration Testing

```dart
// integration_test/app_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:your_app/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  
  group('Social Media App Integration Tests', () {
    testWidgets('complete user journey: register, login, create post', (WidgetTester tester) async {
      // Start the app
      app.main();
      await tester.pumpAndSettle();
      
      // Test registration flow
      await tester.tap(find.text('Register'));
      await tester.pumpAndSettle();
      
      await tester.enterText(find.byKey(Key('name-field')), 'Test User');
      await tester.enterText(find.byKey(Key('email-field')), 'test@example.com');
      await tester.enterText(find.byKey(Key('password-field')), 'password123');
      
      await tester.tap(find.byKey(Key('register-button')));
      await tester.pumpAndSettle(Duration(seconds: 3));
      
      // Verify registration success and navigation to home
      expect(find.byKey(Key('home-screen')), findsOneWidget);
      
      // Test post creation
      await tester.tap(find.byIcon(Icons.add));
      await tester.pumpAndSettle();
      
      await tester.enterText(find.byKey(Key('post-content-field')), 'My first post!');
      await tester.tap(find.byKey(Key('create-post-button')));
      await tester.pumpAndSettle(Duration(seconds: 2));
      
      // Verify post appears in feed
      expect(find.text('My first post!'), findsOneWidget);
      
      // Test logout
      await tester.tap(find.byKey(Key('profile-tab')));
      await tester.pumpAndSettle();
      
      await tester.tap(find.byKey(Key('logout-button')));
      await tester.pumpAndSettle();
      
      // Verify navigation back to login
      expect(find.byKey(Key('login-screen')), findsOneWidget);
    });
  });
}
```

---

## 📱 Part 10: Real-World Projects (Weeks 10-12)

### 10.1 Complete E-Commerce App

#### Project Requirements

```
🛒 E-COMMERCE APP FEATURES

Core Features:
├─ User authentication (login/register/logout)
├─ Product catalog with categories and search
├─ Shopping cart with quantity management
├─ Order placement and order history
├─ User profile and address management
├─ Payment integration (Stripe/PayPal)
├─ Push notifications for order updates
└─ Offline support with sync

Advanced Features:
├─ Product reviews and ratings
├─ Wishlist/favorites
├─ Price tracking and alerts
├─ Social sharing
├─ Dark/light theme support
├─ Multi-language support
├─ Analytics integration
└─ Crash reporting
```

#### Core Implementation

```dart
// Product catalog with search
class ProductCatalogScreen extends StatefulWidget {
  @override
  _ProductCatalogScreenState createState() => _ProductCatalogScreenState();
}

class _ProductCatalogScreenState extends State<ProductCatalogScreen> {
  final TextEditingController _searchController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  String _selectedCategory = 'All';
  
  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<ProductsProvider>().loadProducts();
    });
  }
  
  void _onScroll() {
    if (_scrollController.position.pixels == _scrollController.position.maxScrollExtent) {
      context.read<ProductsProvider>().loadMoreProducts();
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Products'),
        bottom: PreferredSize(
          preferredSize: Size.fromHeight(120),
          child: Column(
            children: [
              // Search bar
              Padding(
                padding: EdgeInsets.all(8.0),
                child: TextField(
                  controller: _searchController,
                  decoration: InputDecoration(
                    hintText: 'Search products...',
                    prefixIcon: Icon(Icons.search),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(25),
                    ),
                    filled: true,
                    fillColor: Colors.white,
                  ),
                  onChanged: (value) {
                    context.read<ProductsProvider>().searchProducts(value);
                  },
                ),
              ),
              
              // Category filter
              Container(
                height: 50,
                child: Consumer<ProductsProvider>(
                  builder: (context, provider, child) {
                    return ListView.builder(
                      scrollDirection: Axis.horizontal,
                      itemCount: provider.categories.length,
                      itemBuilder: (context, index) {
                        final category = provider.categories[index];
                        final isSelected = _selectedCategory == category;
                        
                        return Padding(
                          padding: EdgeInsets.symmetric(horizontal: 4),
                          child: FilterChip(
                            label: Text(category),
                            selected: isSelected,
                            onSelected: (selected) {
                              setState(() {
                                _selectedCategory = category;
                              });
                              provider.filterByCategory(category);
                            },
                          ),
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
      body: Consumer<ProductsProvider>(
        builder: (context, provider, child) {
          if (provider.isLoading && provider.products.isEmpty) {
            return Center(child: CircularProgressIndicator());
          }
          
          if (provider.error != null && provider.products.isEmpty) {
            return ErrorWidget(
              message: provider.error!,
              onRetry: provider.loadProducts,
            );
          }
          
          return RefreshIndicator(
            onRefresh: provider.refreshProducts,
            child: GridView.builder(
              controller: _scrollController,
              padding: EdgeInsets.all(8),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 0.7,
                crossAxisSpacing: 8,
                mainAxisSpacing: 8,
              ),
              itemCount: provider.filteredProducts.length + 
                         (provider.hasMoreData ? 1 : 0),
              itemBuilder: (context, index) {
                if (index == provider.filteredProducts.length) {
                  return Center(child: CircularProgressIndicator());
                }
                
                final product = provider.filteredProducts[index];
                return ProductCard(
                  product: product,
                  onTap: () => _navigateToProductDetail(product),
                  onAddToCart: () => _addToCart(product),
                );
              },
            ),
          );
        },
      ),
    );
  }
  
  void _navigateToProductDetail(Product product) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ProductDetailScreen(product: product),
      ),
    );
  }
  
  void _addToCart(Product product) {
    context.read<CartProvider>().addItem(product);
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('${product.name} added to cart'),
        action: SnackBarAction(
          label: 'View Cart',
          onPressed: () {
            Navigator.pushNamed(context, '/cart');
          },
        ),
      ),
    );
  }
  
  @override
  void dispose() {
    _searchController.dispose();
    _scrollController.dispose();
    super.dispose();
  }
}
```

### 10.2 Advanced Features Implementation

#### Push Notifications with Firebase

```yaml
# pubspec.yaml
dependencies:
  firebase_core: ^2.24.2
  firebase_messaging: ^14.7.9
  flutter_local_notifications: ^16.3.0
```

```dart
// Push notification service
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationService {
  static final NotificationService _instance = NotificationService._internal();
  factory NotificationService() => _instance;
  NotificationService._internal();
  
  final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;
  final FlutterLocalNotificationsPlugin _localNotifications = FlutterLocalNotificationsPlugin();
  
  Future<void> initialize() async {
    // Request permission
    NotificationSettings settings = await _firebaseMessaging.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );
    
    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      print('User granted permission');
    }
    
    // Initialize local notifications
    const AndroidInitializationSettings initializationSettingsAndroid =
        AndroidInitializationSettings('@mipmap/ic_launcher');
    
    const DarwinInitializationSettings initializationSettingsIOS =
        DarwinInitializationSettings(
          requestAlertPermission: true,
          requestBadgePermission: true,
          requestSoundPermission: true,
        );
    
    const InitializationSettings initializationSettings = InitializationSettings(
      android: initializationSettingsAndroid,
      iOS: initializationSettingsIOS,
    );
    
    await _localNotifications.initialize(
      initializationSettings,
      onDidReceiveNotificationResponse: _onNotificationTap,
    );
    
    // Handle foreground messages
    FirebaseMessaging.onMessage.listen(_handleForegroundMessage);
    
    // Handle background messages
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
    
    // Handle app opened from notification
    FirebaseMessaging.onMessageOpenedApp.listen(_handleNotificationOpenedApp);
  }
  
  Future<String?> getToken() async {
    return await _firebaseMessaging.getToken();
  }
  
  void _handleForegroundMessage(RemoteMessage message) {
    print('Received foreground message: ${message.messageId}');
    
    _showLocalNotification(
      title: message.notification?.title ?? 'New Message',
      body: message.notification?.body ?? '',
      payload: message.data.toString(),
    );
  }
  
  void _handleNotificationOpenedApp(RemoteMessage message) {
    print('App opened from notification: ${message.messageId}');
    _handleNotificationNavigation(message.data);
  }
  
  void _onNotificationTap(NotificationResponse response) {
    print('Local notification tapped: ${response.payload}');
    // Handle navigation based on payload
  }
  
  Future<void> _showLocalNotification({
    required String title,
    required String body,
    String? payload,
  }) async {
    const AndroidNotificationDetails androidDetails = AndroidNotificationDetails(
      'default_channel',
      'Default Channel',
      channelDescription: 'Default notification channel',
      importance: Importance.max,
      priority: Priority.high,
    );
    
    const DarwinNotificationDetails iOSDetails = DarwinNotificationDetails(
      presentAlert: true,
      presentBadge: true,
      presentSound: true,
    );
    
    const NotificationDetails notificationDetails = NotificationDetails(
      android: androidDetails,
      iOS: iOSDetails,
    );
    
    await _localNotifications.show(
      DateTime.now().millisecond,
      title,
      body,
      notificationDetails,
      payload: payload,
    );
  }
  
  void _handleNotificationNavigation(Map<String, dynamic> data) {
    // Implement navigation logic based on notification data
    final type = data['type'];
    final id = data['id'];
    
    switch (type) {
      case 'order_update':
        // Navigate to order details
        break;
      case 'new_message':
        // Navigate to chat
        break;
      case 'promotion':
        // Navigate to product/offer
        break;
    }
  }
}

// Background message handler (top-level function)
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp();
  print('Handling background message: ${message.messageId}');
}
```

#### Offline Support and Synchronization

```dart
// Offline data management
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseService {
  static final DatabaseService _instance = DatabaseService._internal();
  factory DatabaseService() => _instance;
  DatabaseService._internal();
  
  Database? _database;
  
  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }
  
  Future<Database> _initDatabase() async {
    final databasePath = await getDatabasesPath();
    final path = join(databasePath, 'app_database.db');
    
    return await openDatabase(
      path,
      version: 1,
      onCreate: _onCreate,
    );
  }
  
  Future<void> _onCreate(Database db, int version) async {
    // Create tables
    await db.execute('''
      CREATE TABLE users(
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        avatar TEXT,
        created_at TEXT NOT NULL,
        is_synced INTEGER DEFAULT 0
      )
    ''');
    
    await db.execute('''
      CREATE TABLE posts(
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        content TEXT NOT NULL,
        image_url TEXT,
        likes_count INTEGER DEFAULT 0,
        created_at TEXT NOT NULL,
        is_synced INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (id)
      )
    ''');
    
    await db.execute('''
      CREATE TABLE sync_queue(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        table_name TEXT NOT NULL,
        record_id TEXT NOT NULL,
        data TEXT,
        created_at TEXT NOT NULL
      )
    ''');
  }
  
  // User operations
  Future<int> insertUser(User user) async {
    final db = await database;
    return await db.insert('users', {
      'id': user.id,
      'name': user.name,
      'email': user.email,
      'avatar': user.avatar,
      'created_at': user.createdAt.toIso8601String(),
      'is_synced': 1,
    });
  }
  
  Future<List<User>> getUsers() async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query('users');
    
    return List.generate(maps.length, (i) {
      return User(
        id: maps[i]['id'],
        name: maps[i]['name'],
        email: maps[i]['email'],
        avatar: maps[i]['avatar'],
        createdAt: DateTime.parse(maps[i]['created_at']),
        roles: [], // Load from separate table if needed
      );
    });
  }
  
  // Sync operations
  Future<void> addToSyncQueue(String action, String tableName, String recordId, Map<String, dynamic>? data) async {
    final db = await database;
    await db.insert('sync_queue', {
      'action': action,
      'table_name': tableName,
      'record_id': recordId,
      'data': data != null ? json.encode(data) : null,
      'created_at': DateTime.now().toIso8601String(),
    });
  }
  
  Future<List<Map<String, dynamic>>> getPendingSyncItems() async {
    final db = await database;
    return await db.query('sync_queue', orderBy: 'created_at ASC');
  }
  
  Future<void> removeSyncItem(int id) async {
    final db = await database;
    await db.delete('sync_queue', where: 'id = ?', whereArgs: [id]);
  }
}

// Sync service
class SyncService {
  final ApiService _apiService = ApiService();
  final DatabaseService _databaseService = DatabaseService();
  
  Future<void> syncData() async {
    if (!await _hasInternetConnection()) return;
    
    final pendingItems = await _databaseService.getPendingSyncItems();
    
    for (final item in pendingItems) {
      try {
        await _processSyncItem(item);
        await _databaseService.removeSyncItem(item['id']);
      } catch (e) {
        print('Sync failed for item ${item['id']}: $e');
        // Keep item in queue for next sync
      }
    }
  }
  
  Future<void> _processSyncItem(Map<String, dynamic> item) async {
    final action = item['action'];
    final tableName = item['table_name'];
    final recordId = item['record_id'];
    final data = item['data'] != null ? json.decode(item['data']) : null;
    
    switch (action) {
      case 'CREATE':
        await _apiService.post('/$tableName', data: data);
        break;
      case 'UPDATE':
        await _apiService.post('/$tableName/$recordId', data: data);
        break;
      case 'DELETE':
        await _apiService.delete('/$tableName/$recordId');
        break;
    }
  }
  
  Future<bool> _hasInternetConnection() async {
    // Implement connectivity check
    return true; // Placeholder
  }
}
```

### 10.3 Complete Social Media App

```dart
// Social feed with real-time updates
class SocialFeedScreen extends StatefulWidget {
  @override
  _SocialFeedScreenState createState() => _SocialFeedScreenState();
}

class _SocialFeedScreenState extends State<SocialFeedScreen> {
  final RefreshController _refreshController = RefreshController();
  late StreamSubscription _postSubscription;
  
  @override
  void initState() {
    super.initState();
    _loadInitialPosts();
    _setupRealTimeUpdates();
  }
  
  void _loadInitialPosts() {
    context.read<PostsProvider>().loadPosts();
  }
  
  void _setupRealTimeUpdates() {
    // Listen to real-time post updates via WebSocket or Firebase
    _postSubscription = PostsWebSocketService().postUpdates.listen((update) {
      context.read<PostsProvider>().handleRealTimeUpdate(update);
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Feed'),
        actions: [
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () => _navigateToCreatePost(),
          ),
        ],
      ),
      body: Consumer<PostsProvider>(
        builder: (context, postsProvider, child) {
          return SmartRefresher(
            controller: _refreshController,
            enablePullDown: true,
            enablePullUp: true,
            onRefresh: () async {
              await postsProvider.refreshPosts();
              _refreshController.refreshCompleted();
            },
            onLoading: () async {
              await postsProvider.loadMorePosts();
              _refreshController.loadComplete();
            },
            child: ListView.builder(
              itemCount: postsProvider.posts.length,
              itemBuilder: (context, index) {
                final post = postsProvider.posts[index];
                return PostCard(
                  post: post,
                  onLike: () => _likePost(post),
                  onComment: () => _navigateToComments(post),
                  onShare: () => _sharePost(post),
                );
              },
            ),
          );
        },
      ),
    );
  }
  
  void _navigateToCreatePost() {
    Navigator.pushNamed(context, '/create-post');
  }
  
  void _likePost(Post post) {
    context.read<PostsProvider>().toggleLike(post.id);
  }
  
  void _navigateToComments(Post post) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => CommentsScreen(post: post),
      ),
    );
  }
  
  void _sharePost(Post post) {
    Share.share('Check out this post: ${post.content}');
  }
  
  @override
  void dispose() {
    _postSubscription.cancel();
    _refreshController.dispose();
    super.dispose();
  }
}

// Post card widget
class PostCard extends StatelessWidget {
  final Post post;
  final VoidCallback onLike;
  final VoidCallback onComment;
  final VoidCallback onShare;
  
  const PostCard({
    Key? key,
    required this.post,
    required this.onLike,
    required this.onComment,
    required this.onShare,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // User info header
          ListTile(
            leading: CircleAvatar(
              backgroundImage: NetworkImage(post.user.avatar ?? 'https://picsum.photos/50/50'),
            ),
            title: Text(
              post.user.name,
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            subtitle: Text(_formatTime(post.createdAt)),
            trailing: PopupMenuButton(
              itemBuilder: (context) => [
                PopupMenuItem(
                  value: 'report',
                  child: Text('Report'),
                ),
                if (post.user.id == context.read<AuthProvider>().currentUser?.id)
                  PopupMenuItem(
                    value: 'delete',
                    child: Text('Delete'),
                  ),
              ],
              onSelected: (value) => _handleMenuAction(context, value),
            ),
          ),
          
          // Post content
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 16),
            child: Text(
              post.content,
              style: TextStyle(fontSize: 16),
            ),
          ),
          
          // Post image
          if (post.imageUrl != null)
            Padding(
              padding: EdgeInsets.all(8),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: Image.network(
                  post.imageUrl!,
                  width: double.infinity,
                  height: 250,
                  fit: BoxFit.cover,
                ),
              ),
            ),
          
          // Action buttons
          Padding(
            padding: EdgeInsets.all(8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _ActionButton(
                  icon: post.isLikedByCurrentUser ? Icons.favorite : Icons.favorite_border,
                  label: '${post.likesCount}',
                  color: post.isLikedByCurrentUser ? Colors.red : Colors.grey,
                  onTap: onLike,
                ),
                _ActionButton(
                  icon: Icons.comment_outlined,
                  label: '${post.commentsCount}',
                  onTap: onComment,
                ),
                _ActionButton(
                  icon: Icons.share_outlined,
                  label: 'Share',
                  onTap: onShare,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
  
  String _formatTime(DateTime dateTime) {
    final now = DateTime.now();
    final difference = now.difference(dateTime);
    
    if (difference.inMinutes < 1) return 'Just now';
    if (difference.inMinutes < 60) return '${difference.inMinutes}m ago';
    if (difference.inHours < 24) return '${difference.inHours}h ago';
    return '${difference.inDays}d ago';
  }
  
  void _handleMenuAction(BuildContext context, String action) {
    switch (action) {
      case 'report':
        // Implement report functionality
        break;
      case 'delete':
        _showDeleteConfirmation(context);
        break;
    }
  }
  
  void _showDeleteConfirmation(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Delete Post'),
          content: Text('Are you sure you want to delete this post?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                context.read<PostsProvider>().deletePost(post.id);
                Navigator.of(context).pop();
              },
              child: Text('Delete', style: TextStyle(color: Colors.red)),
            ),
          ],
        );
      },
    );
  }
}

class _ActionButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onTap;
  final Color? color;
  
  const _ActionButton({
    required this.icon,
    required this.label,
    required this.onTap,
    this.color,
  });
  
  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(20),
      child: Padding(
        padding: EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, size: 20, color: color ?? Colors.grey),
            SizedBox(width: 4),
            Text(label, style: TextStyle(color: color ?? Colors.grey)),
          ],
        ),
      ),
    );
  }
}
```

---

## 📈 Part 11: Performance Optimization (Week 13)

### 11.1 Performance Best Practices

```dart
// Optimized list rendering with lazy loading
class OptimizedListView extends StatefulWidget {
  final List<Product> products;
  
  const OptimizedListView({Key? key, required this.products}) : super(key: key);
  
  @override
  _OptimizedListViewState createState() => _OptimizedListViewState();
}

class _OptimizedListViewState extends State<OptimizedListView> {
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      // Performance optimizations
      cacheExtent: 500, // Pre-load items
      itemExtent: 100, // Fixed height for better performance
      addAutomaticKeepAlives: false, // Don't keep off-screen widgets
      addRepaintBoundaries: false, // Reduce repaint boundaries if not needed
      
      itemCount: widget.products.length,
      itemBuilder: (context, index) {
        // Use AutomaticKeepAliveClientMixin for expensive widgets
        return ProductListItem(
          key: ValueKey(widget.products[index].id),
          product: widget.products[index],
        );
      },
    );
  }
}

// Optimized image loading
class OptimizedNetworkImage extends StatelessWidget {
  final String imageUrl;
  final double? width;
  final double? height;
  final BoxFit fit;
  
  const OptimizedNetworkImage({
    Key? key,
    required this.imageUrl,
    this.width,
    this.height,
    this.fit = BoxFit.cover,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return CachedNetworkImage(
      imageUrl: imageUrl,
      width: width,
      height: height,
      fit: fit,
      
      // Optimizations
      memCacheWidth: width?.toInt(),
      memCacheHeight: height?.toInt(),
      
      // Loading states
      placeholder: (context, url) => Container(
        color: Colors.grey.shade200,
        child: Center(
          child: CircularProgressIndicator(strokeWidth: 2),
        ),
      ),
      
      errorWidget: (context, url, error) => Container(
        color: Colors.grey.shade300,
        child: Icon(Icons.error, color: Colors.red),
      ),
      
      // Fade-in animation
      fadeInDuration: Duration(milliseconds: 300),
    );
  }
}

// Memory-efficient state management
class MemoryEfficientProvider extends ChangeNotifier {
  List<Product> _products = [];
  final int _pageSize = 20;
  final Map<String, Product> _productCache = {};
  
  List<Product> get visibleProducts {
    // Only keep recent items in memory
    if (_products.length > 100) {
      _products = _products.take(50).toList();
    }
    return _products;
  }
  
  void addProducts(List<Product> newProducts) {
    _products.addAll(newProducts);
    
    // Cache frequently accessed products
    for (final product in newProducts) {
      _productCache[product.id] = product;
    }
    
    // Limit cache size
    if (_productCache.length > 200) {
      final oldestKeys = _productCache.keys.take(50).toList();
      for (final key in oldestKeys) {
        _productCache.remove(key);
      }
    }
    
    notifyListeners();
  }
  
  Product? getCachedProduct(String id) {
    return _productCache[id];
  }
  
  @override
  void dispose() {
    _products.clear();
    _productCache.clear();
    super.dispose();
  }
}
```

---

## 🚀 Part 12: Deployment and Production (Week 14)

### 12.1 App Store Deployment

#### Android Deployment (Google Play Store)

```bash
# 1. Generate release APK
flutter build apk --release

# 2. Generate App Bundle (Recommended)
flutter build appbundle --release

# 3. Sign the app
# Create keystore (one-time setup)
keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload

# Configure signing in android/app/build.gradle
```

```gradle
// android/app/build.gradle
android {
    compileSdkVersion flutter.compileSdkVersion
    
    signingConfigs {
        release {
            keyAlias keystoreProperties['keyAlias']
            keyPassword keystoreProperties['keyPassword']
            storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
            storePassword keystoreProperties['storePassword']
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            useProguard true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

#### iOS Deployment (App Store)

```bash
# 1. Build iOS release
flutter build ios --release

# 2. Archive in Xcode
open ios/Runner.xcworkspace

# 3. Use Xcode organizer to upload to App Store Connect
```

### 12.2 CI/CD Pipeline

```yaml
# .github/workflows/flutter_ci.yml
name: Flutter CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.16.0'
          
      - name: Install dependencies
        run: flutter pub get
        
      - name: Run analyzer
        run: flutter analyze
        
      - name: Run tests
        run: flutter test --coverage
        
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        
  build_android:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        
      - name: Install dependencies
        run: flutter pub get
        
      - name: Build APK
        run: flutter build apk --release
        
      - name: Build App Bundle
        run: flutter build appbundle --release
        
      - name: Upload to Play Store
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJsonPlainText: ${{ secrets.GOOGLE_PLAY_SERVICE_ACCOUNT }}
          packageName: com.yourcompany.yourapp
          releaseFiles: build/app/outputs/bundle/release/app-release.aab
          track: internal
          
  build_ios:
    needs: test
    runs-on: macos-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        
      - name: Install dependencies
        run: flutter pub get
        
      - name: Build iOS
        run: flutter build ios --release --no-codesign
        
      - name: Upload to TestFlight
        uses: apple-actions/upload-testflight-build@v1
        with:
          app-path: build/ios/iphoneos/Runner.app
          issuer-id: ${{ secrets.APPSTORE_ISSUER_ID }}
          api-key-id: ${{ secrets.APPSTORE_API_KEY_ID }}
          api-private-key: ${{ secrets.APPSTORE_API_PRIVATE_KEY }}
```

---

## 🏆 **Complete Project Portfolio**

### Project 1: Task Management App 📋
- **Features:** CRUD operations, local storage, synchronization
- **Architecture:** Clean Architecture + Provider
- **Skills:** State management, data persistence, offline support

### Project 2: E-Commerce App 🛒  
- **Features:** Product catalog, cart, checkout, payment integration
- **Architecture:** MVVM + Repository pattern
- **Skills:** API integration, complex UI, performance optimization

### Project 3: Social Media App 📱
- **Features:** Real-time chat, image sharing, push notifications
- **Architecture:** Clean Architecture + Bloc
- **Skills:** Real-time features, media handling, advanced UI

### Project 4: Fitness Tracker 💪
- **Features:** Exercise tracking, charts, wearable integration
- **Architecture:** Microservices + Provider
- **Skills:** Data visualization, device integration, health APIs

### Project 5: Restaurant Ordering 🍕
- **Features:** Menu browsing, ordering, payment, delivery tracking
- **Architecture:** Modular + Riverpod
- **Skills:** Location services, real-time tracking, payment systems

---

## 🎓 **Flutter Developer Certification Path**

### **Beginner Level (Weeks 1-4)**
✅ Build 3 simple apps  
✅ Understand widget lifecycle  
✅ Master basic state management  
✅ Complete Dart fundamentals  

### **Intermediate Level (Weeks 5-8)**
✅ Build 2 complex apps with APIs  
✅ Implement proper architecture  
✅ Add testing coverage  
✅ Handle offline scenarios  

### **Advanced Level (Weeks 9-12)**
✅ Build 1 production-ready app  
✅ Implement CI/CD pipeline  
✅ Deploy to app stores  
✅ Handle performance optimization  

### **Expert Level (Weeks 13-16)**
✅ Create custom packages  
✅ Contribute to open source  
✅ Mentor other developers  
✅ Build Flutter expertise reputation  

---

## 💼 **Career Roadmap**

### **Flutter Developer Salary Progression**
```
📈 FLUTTER DEVELOPER CAREER PATH

Junior Flutter Developer (0-1 years)
├─ Salary: $50,000 - $70,000
├─ Skills: Basic Flutter, simple apps
└─ Focus: Learning fundamentals

Mid-Level Flutter Developer (1-3 years)  
├─ Salary: $70,000 - $100,000
├─ Skills: Complex apps, state management, APIs
└─ Focus: Architecture and best practices

Senior Flutter Developer (3-5 years)
├─ Salary: $100,000 - $140,000  
├─ Skills: Performance, testing, mentoring
└─ Focus: Technical leadership

Flutter Tech Lead (5+ years)
├─ Salary: $140,000 - $180,000+
├─ Skills: Architecture design, team management
└─ Focus: Strategic technical decisions
```

### **Skill Development Checklist**

**Technical Skills:**
- [ ] ✅ Dart language mastery
- [ ] ✅ Flutter widget system
- [ ] ✅ State management (multiple patterns)
- [ ] ✅ API integration and data modeling
- [ ] ✅ Local storage and offline support
- [ ] ✅ Testing (unit, widget, integration)
- [ ] ✅ Performance optimization
- [ ] ✅ Platform integration (iOS/Android)
- [ ] ✅ CI/CD and deployment
- [ ] ✅ Custom packages and plugins

**Soft Skills:**
- [ ] ✅ Problem-solving and debugging
- [ ] ✅ Code review and mentoring
- [ ] ✅ Technical communication
- [ ] ✅ Project planning and estimation
- [ ] ✅ Cross-platform thinking

---

## 🎯 **Final Success Formula**

```
🏆 FLUTTER MASTERY = THEORY + PRACTICE + PROJECTS

Theory (25%):
├─ Read this complete guide
├─ Study official Flutter documentation  
├─ Follow Flutter YouTube channel
└─ Read Flutter development blogs

Practice (50%):  
├─ Code every example in this guide
├─ Build variations of example projects
├─ Solve coding challenges on LeetCode/HackerRank
├─ Contribute to open source Flutter packages
└─ Practice algorithm problems in Dart

Projects (25%):
├─ Build the 5 portfolio projects listed above
├─ Deploy apps to Google Play Store / App Store
├─ Get user feedback and iterate
├─ Document your development process
└─ Share your apps on social media
```

## ✅ **Ultimate Flutter Mastery Checklist**

### **Foundation Level:**
- [ ] ✅ Set up development environment (Flutter, Android Studio, Xcode)
- [ ] ✅ Master Dart language fundamentals and OOP
- [ ] ✅ Understand Flutter widget system and widget lifecycle
- [ ] ✅ Build basic UI with layouts and navigation
- [ ] ✅ Implement local state management with setState

### **Intermediate Level:**
- [ ] ✅ Master Provider/Riverpod for app-wide state management
- [ ] ✅ Integrate REST APIs with proper error handling
- [ ] ✅ Implement data persistence (SQLite, SharedPreferences)
- [ ] ✅ Handle form validation and user input
- [ ] ✅ Add offline support and data synchronization

### **Advanced Level:**
- [ ] ✅ Implement Clean Architecture or MVVM patterns
- [ ] ✅ Add comprehensive testing (unit, widget, integration)
- [ ] ✅ Optimize performance and handle large datasets
- [ ] ✅ Integrate platform-specific features (camera, location, etc.)
- [ ] ✅ Deploy apps to Google Play Store and App Store

### **Expert Level:**
- [ ] ✅ Create custom Flutter packages and plugins
- [ ] ✅ Implement advanced animations and custom painters
- [ ] ✅ Set up CI/CD pipeline with automated testing
- [ ] ✅ Handle production monitoring and crash reporting
- [ ] ✅ Mentor other developers and contribute to open source

**🎉 Congratulations! You now have a complete Flutter and Dart mastery guide that takes you from absolute beginner to expert level. Follow this systematic approach, build the projects, and you'll become a highly skilled Flutter developer ready for any mobile development challenge! 🚀**

---

*Last Updated: February 2026*  
*Flutter Version: 3.16+ Compatible*