# 🟨 JavaScript Complete Mastery Guide

> **Complete JavaScript Reference for Interview Preparation and Modern Development**  
> From Beginner to Expert Level - All Concepts Covered

---

## 📚 Table of Contents

1. [JavaScript Fundamentals](#1-javascript-fundamentals)
2. [Data Types and Variables](#2-data-types-and-variables)
3. [Functions](#3-functions)
4. [Objects and Arrays](#4-objects-and-arrays)
5. [ES6+ Modern Features](#5-es6-modern-features)
6. [Asynchronous JavaScript](#6-asynchronous-javascript)
7. [DOM Manipulation](#7-dom-manipulation)
8. [Object-Oriented Programming](#8-object-oriented-programming)
9. [Functional Programming](#9-functional-programming)
10. [Error Handling](#10-error-handling)
11. [Node.js Backend Development](#11-nodejs-backend-development)
12. [Testing Frameworks](#12-testing-frameworks)
13. [Advanced Concepts](#13-advanced-concepts)
14. [Performance Optimization](#14-performance-optimization)
15. [Modern JavaScript Ecosystem](#15-modern-javascript-ecosystem)

---

## 1. JavaScript Fundamentals

### Variables and Declarations

```javascript
// Variable declarations
var oldStyle = "function-scoped variable";
let modernBlock = "block-scoped variable";
const constant = "immutable reference";

// Hoisting behavior
console.log(hoistedVar); // undefined (not error)
var hoistedVar = "I'm hoisted!";

// let and const are not hoisted
// console.log(notHoisted); // ReferenceError
let notHoisted = "Modern variable";
```

### Data Types

```javascript
// Primitive types
const number = 42;
const string = "Hello, JavaScript!";
const boolean = true;
const undefinedValue = undefined;
const nullValue = null;
const symbol = Symbol('unique');
const bigint = BigInt(9007199254740991);

// Type checking
console.log(typeof number);    // "number"
console.log(typeof string);    // "string"
console.log(typeof boolean);   // "boolean"
console.log(typeof undefinedValue); // "undefined"
console.log(typeof nullValue); // "object" (historical quirk)
console.log(typeof symbol);    // "symbol"
console.log(typeof bigint);    // "bigint"

// Reference types
const object = { name: "Alice", age: 30 };
const array = [1, 2, 3, 4, 5];
const func = function() { return "I'm a function!"; };

console.log(Array.isArray(array)); // true
console.log(object instanceof Object); // true
```

### Type Coercion

```javascript
// Automatic type conversion
console.log("5" + 3);      // "53" (string concatenation)
console.log("5" - 3);      // 2 (numeric subtraction)
console.log("5" * "2");    // 10 (numeric multiplication)
console.log(true + 1);     // 2 (boolean to number)

// Explicit conversion
const str = String(123);        // "123"
const num = Number("456");      // 456
const bool = Boolean(1);        // true

// Falsy values
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean(null));     // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));      // false
```

---

## 2. Data Types and Variables

### Strings

```javascript
// String creation
const singleQuotes = 'Hello, World!';
const doubleQuotes = "Hello, JavaScript!";
const templateLiteral = `Hello, ${name}!`;

// String methods
const text = "JavaScript Programming";
console.log(text.length);              // 21
console.log(text.toUpperCase());       // "JAVASCRIPT PROGRAMMING"
console.log(text.toLowerCase());       // "javascript programming"
console.log(text.slice(0, 10));       // "JavaScript"
console.log(text.substring(0, 10));    // "JavaScript"
console.log(text.indexOf("Script"));   // 4
console.log(text.includes("Program")); // true
console.log(text.split(" "));          // ["JavaScript", "Programming"]

// Template literals
const name = "Alice";
const age = 30;
const message = `Hello, my name is ${name} and I'm ${age} years old.`;

// Multi-line strings
const multiLine = `
    This is a
    multi-line
    string
`;
```

### Numbers

```javascript
// Number operations
const integer = 42;
const float = 3.14159;
const exponential = 2.5e6; // 2500000

// Math object
console.log(Math.PI);           // 3.141592653589793
console.log(Math.round(4.7));   // 5
console.log(Math.ceil(4.1));    // 5
console.log(Math.floor(4.9));   // 4
console.log(Math.max(1, 5, 3)); // 5
console.log(Math.min(1, 5, 3)); // 1
console.log(Math.random());     // Random number 0-1

// Number methods
const num = 123.456;
console.log(num.toFixed(2));     // "123.46"
console.log(num.toPrecision(4)); // "123.5"
console.log(parseInt("123px"));  // 123
console.log(parseFloat("123.45px")); // 123.45

// Number validation
console.log(Number.isNaN(NaN));      // true
console.log(Number.isFinite(123));   // true
console.log(Number.isInteger(123));  // true
```

---

## 3. Functions

### Function Declarations and Expressions

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function expression
const greetExpression = function(name) {
    return `Hello, ${name}!`;
};

// Arrow function (ES6+)
const greetArrow = (name) => `Hello, ${name}!`;
const greetArrowBlock = (name) => {
    return `Hello, ${name}!`;
};

// Single parameter (parentheses optional)
const square = x => x * x;

// No parameters
const random = () => Math.random();
```

### Function Parameters

```javascript
// Default parameters
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15

// Destructuring parameters
function createUser({name, age, email}) {
    return {
        id: Date.now(),
        name,
        age,
        email,
        created: new Date()
    };
}

const userData = {name: "Alice", age: 30, email: "alice@example.com"};
const user = createUser(userData);
```

### Higher-Order Functions

```javascript
// Function that takes another function as parameter
function applyOperation(numbers, operation) {
    return numbers.map(operation);
}

const numbers = [1, 2, 3, 4, 5];
const squared = applyOperation(numbers, x => x * x);
const doubled = applyOperation(numbers, x => x * 2);

// Function that returns a function
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Currying
const curry = (fn) => {
    return function curried(...args) {
        if (args.length >= fn.length) {
            return fn.apply(this, args);
        } else {
            return function(...args2) {
                return curried.apply(this, args.concat(args2));
            };
        }
    };
};

const add = (a, b, c) => a + b + c;
const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6
```

---

## 4. Objects and Arrays

### Objects

```javascript
// Object creation
const person = {
    name: "Alice",
    age: 30,
    city: "New York",
    greet: function() {
        return `Hello, I'm ${this.name}`;
    }
};

// Accessing properties
console.log(person.name);        // "Alice"
console.log(person["age"]);      // 30

// Adding/modifying properties
person.email = "alice@example.com";
person.age = 31;

// Object methods
const keys = Object.keys(person);
const values = Object.values(person);
const entries = Object.entries(person);

// Object destructuring
const {name, age, city} = person;
const {name: personName, age: personAge} = person; // Rename variables

// Nested destructuring
const user = {
    id: 1,
    profile: {
        name: "Alice",
        preferences: {
            theme: "dark",
            language: "en"
        }
    }
};

const {profile: {name: userName, preferences: {theme}}} = user;
```

### Arrays

```javascript
// Array creation
const fruits = ["apple", "banana", "cherry"];
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "hello", true, {name: "Alice"}];

// Array methods
fruits.push("date");           // Add to end
fruits.unshift("avocado");     // Add to beginning
const last = fruits.pop();     // Remove from end
const first = fruits.shift();  // Remove from beginning

// Array iteration
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});

// Array transformation
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((total, n) => total + n, 0);

// Array searching
const foundFruit = fruits.find(fruit => fruit.startsWith('a'));
const fruitIndex = fruits.findIndex(fruit => fruit === 'banana');
const hasApple = fruits.includes('apple');

// Array destructuring
const [firstFruit, secondFruit, ...restFruits] = fruits;

// Spread operator with arrays
const moreFruits = ["grape", "orange"];
const allFruits = [...fruits, ...moreFruits];
```

### Advanced Array Methods

```javascript
// Sorting
const words = ["banana", "apple", "cherry"];
words.sort(); // Alphabetical sort

const nums = [3, 1, 4, 1, 5, 9];
nums.sort((a, b) => a - b); // Numerical sort ascending
nums.sort((a, b) => b - a); // Numerical sort descending

// Flattening
const nested = [[1, 2], [3, 4], [5, 6]];
const flattened = nested.flat();          // [1, 2, 3, 4, 5, 6]
const deepNested = [1, [2, [3, [4]]]];
const deepFlattened = deepNested.flat(3); // [1, 2, 3, 4]

// Array.from and Array.of
const arrayFromString = Array.from("hello"); // ['h', 'e', 'l', 'l', 'o']
const arrayFromRange = Array.from({length: 5}, (_, i) => i); // [0, 1, 2, 3, 4]
const arrayOf = Array.of(1, 2, 3, 4, 5); // [1, 2, 3, 4, 5]
```

---

## 5. ES6+ Modern Features

### Let, Const, and Block Scope

```javascript
// Block scope with let and const
{
    let blockScoped = "I'm block scoped";
    const alsoBlockScoped = "Me too";
    var functionScoped = "I'm function scoped";
}

// console.log(blockScoped); // ReferenceError
// console.log(alsoBlockScoped); // ReferenceError
console.log(functionScoped); // "I'm function scoped"

// Temporal dead zone
// console.log(temporalDeadZone); // ReferenceError
let temporalDeadZone = "Now I exist";
```

### Destructuring Assignment

```javascript
// Array destructuring
const colors = ["red", "green", "blue"];
const [primary, secondary, tertiary] = colors;
const [first, , third] = colors; // Skip middle element
const [head, ...tail] = colors;  // Rest elements

// Object destructuring
const person = {name: "Alice", age: 30, city: "NYC"};
const {name, age} = person;
const {name: personName} = person; // Rename
const {country = "USA"} = person;  // Default value

// Function parameter destructuring
function displayUser({name, age, email = "No email"}) {
    console.log(`${name}, ${age}, ${email}`);
}

displayUser({name: "Bob", age: 25});
```

### Template Literals

```javascript
// Basic template literals
const name = "Alice";
const greeting = `Hello, ${name}!`;

// Multi-line strings
const html = `
    <div>
        <h1>${name}'s Profile</h1>
        <p>Welcome to your dashboard</p>
    </div>
`;

// Expression in template literals
const a = 5;
const b = 10;
const result = `The sum of ${a} and ${b} is ${a + b}`;

// Tagged template literals
function highlight(strings, ...values) {
    return strings.reduce((result, string, i) => {
        const value = values[i] ? `<mark>${values[i]}</mark>` : '';
        return result + string + value;
    }, '');
}

const highlighted = highlight`Hello ${name}, you have ${5} messages`;
```

### Arrow Functions

```javascript
// Traditional function
function traditional(x) {
    return x * 2;
}

// Arrow function
const arrow = x => x * 2;

// Multiple parameters
const add = (a, b) => a + b;

// Block body
const complexOperation = (x, y) => {
    const temp = x * 2;
    const result = temp + y;
    return result;
};

// Arrow functions and 'this' context
const object = {
    name: "Alice",
    traditional: function() {
        return this.name; // 'this' refers to object
    },
    arrow: () => {
        return this.name; // 'this' refers to global/window
    }
};
```

### Spread and Rest Operators

```javascript
// Spread with arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Spread with objects
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};
const merged = {...obj1, ...obj2}; // {a: 1, b: 2, c: 3, d: 4}

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

// Rest in destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
const {name, ...otherProps} = {name: "Alice", age: 30, city: "NYC"};
```

---

## 6. Asynchronous JavaScript

### Callbacks

```javascript
// Basic callback
function fetchData(callback) {
    setTimeout(() => {
        const data = {id: 1, name: "Alice"};
        callback(data);
    }, 1000);
}

fetchData((data) => {
    console.log("Received data:", data);
});

// Callback hell example
getData(function(a) {
    getMoreData(a, function(b) {
        getEvenMoreData(b, function(c) {
            getYetMoreData(c, function(d) {
                // This is callback hell!
            });
        });
    });
});
```

### Promises

```javascript
// Creating a Promise
const fetchUserData = (userId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({id: userId, name: `User ${userId}`});
            } else {
                reject(new Error("Invalid user ID"));
            }
        }, 1000);
    });
};

// Using Promises
fetchUserData(1)
    .then(user => {
        console.log("User:", user);
        return fetchUserData(2); // Chain another Promise
    })
    .then(anotherUser => {
        console.log("Another user:", anotherUser);
    })
    .catch(error => {
        console.error("Error:", error.message);
    })
    .finally(() => {
        console.log("Operation completed");
    });

// Promise.all - Wait for all promises
const promises = [
    fetchUserData(1),
    fetchUserData(2),
    fetchUserData(3)
];

Promise.all(promises)
    .then(users => {
        console.log("All users:", users);
    })
    .catch(error => {
        console.error("One or more promises failed:", error);
    });

// Promise.race - First promise to complete
Promise.race(promises)
    .then(firstUser => {
        console.log("First user:", firstUser);
    });
```

### Async/Await

```javascript
// Async function declaration
async function fetchUser(userId) {
    try {
        const user = await fetchUserData(userId);
        console.log("User:", user);
        return user;
    } catch (error) {
        console.error("Error fetching user:", error.message);
        throw error;
    }
}

// Async arrow function
const fetchUserArrow = async (userId) => {
    const user = await fetchUserData(userId);
    return user;
};

// Using async/await with multiple operations
async function fetchMultipleUsers() {
    try {
        // Sequential execution
        const user1 = await fetchUserData(1);
        const user2 = await fetchUserData(2);
        
        // Parallel execution
        const [user3, user4] = await Promise.all([
            fetchUserData(3),
            fetchUserData(4)
        ]);
        
        return [user1, user2, user3, user4];
    } catch (error) {
        console.error("Error:", error);
    }
}

// Error handling with async/await
async function handleErrors() {
    try {
        await fetchUserData(-1); // This will throw an error
    } catch (error) {
        console.error("Caught error:", error.message);
    }
}
```

---

## 7. DOM Manipulation

### Selecting Elements

```javascript
// Single element selection
const elementById = document.getElementById('myId');
const elementByClass = document.querySelector('.myClass');
const elementByTag = document.querySelector('div');

// Multiple element selection
const elementsByClass = document.querySelectorAll('.myClass');
const elementsByTag = document.getElementsByTagName('div');

// Traversing the DOM
const parent = element.parentNode;
const children = element.children;
const siblings = element.nextElementSibling;
const firstChild = element.firstElementChild;
```

### Modifying Elements

```javascript
// Content manipulation
element.textContent = "New text content";
element.innerHTML = "<strong>New HTML content</strong>";

// Attribute manipulation
element.setAttribute('data-id', '123');
const dataId = element.getAttribute('data-id');
element.removeAttribute('data-id');

// Class manipulation
element.classList.add('new-class');
element.classList.remove('old-class');
element.classList.toggle('active');
element.classList.contains('existing-class');

// Style manipulation
element.style.color = 'red';
element.style.backgroundColor = 'blue';
element.style.fontSize = '16px';
```

### Creating and Removing Elements

```javascript
// Creating elements
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello, World!';
newDiv.className = 'greeting';

// Appending elements
document.body.appendChild(newDiv);
parentElement.insertBefore(newDiv, existingChild);

// Removing elements
element.remove(); // Modern way
parentElement.removeChild(element); // Older way

// Replacing elements
parentElement.replaceChild(newElement, oldElement);
```

### Event Handling

```javascript
// Adding event listeners
button.addEventListener('click', function(event) {
    console.log('Button clicked!');
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Stop event bubbling
});

// Arrow function event handler
button.addEventListener('click', (event) => {
    console.log('Button clicked with arrow function!');
});

// Event delegation
document.addEventListener('click', function(event) {
    if (event.target.matches('.dynamic-button')) {
        console.log('Dynamic button clicked!');
    }
});

// Removing event listeners
function handleClick(event) {
    console.log('Handled click');
}

button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick);

// Common events
element.addEventListener('mouseover', handleMouseOver);
element.addEventListener('mouseout', handleMouseOut);
form.addEventListener('submit', handleFormSubmit);
input.addEventListener('input', handleInputChange);
window.addEventListener('resize', handleWindowResize);
```

---

## 8. Object-Oriented Programming

### ES6 Classes

```javascript
// Basic class
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    // Instance method
    greet() {
        return `Hello, I'm ${this.name} and I'm ${this.age} years old.`;
    }
    
    // Static method
    static getSpecies() {
        return "Homo sapiens";
    }
    
    // Getter
    get info() {
        return `${this.name} (${this.age})`;
    }
    
    // Setter
    set age(newAge) {
        if (newAge >= 0) {
            this._age = newAge;
        }
    }
}

// Creating instances
const person1 = new Person("Alice", 30);
const person2 = new Person("Bob", 25);

console.log(person1.greet());
console.log(Person.getSpecies());
```

### Inheritance

```javascript
// Base class
class Animal {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }
    
    speak() {
        return `${this.name} makes a sound`;
    }
    
    getInfo() {
        return `${this.name} is a ${this.species}`;
    }
}

// Derived class
class Dog extends Animal {
    constructor(name, breed) {
        super(name, "Dog"); // Call parent constructor
        this.breed = breed;
    }
    
    // Override parent method
    speak() {
        return `${this.name} barks loudly!`;
    }
    
    // New method specific to Dog
    fetch() {
        return `${this.name} fetches the ball!`;
    }
    
    // Call parent method
    getInfo() {
        return `${super.getInfo()} of breed ${this.breed}`;
    }
}

const dog = new Dog("Buddy", "Golden Retriever");
console.log(dog.speak());   // "Buddy barks loudly!"
console.log(dog.fetch());   // "Buddy fetches the ball!"
console.log(dog.getInfo()); // "Buddy is a Dog of breed Golden Retriever"
```

### Prototypes (Pre-ES6)

```javascript
// Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Adding methods to prototype
Person.prototype.greet = function() {
    return `Hello, I'm ${this.name}`;
};

Person.prototype.haveBirthday = function() {
    this.age++;
};

// Creating instances
const person1 = new Person("Alice", 30);
const person2 = new Person("Bob", 25);

// Inheritance with prototypes
function Student(name, age, grade) {
    Person.call(this, name, age); // Call parent constructor
    this.grade = grade;
}

// Set up inheritance
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

// Add Student-specific methods
Student.prototype.study = function() {
    return `${this.name} is studying`;
};

const student = new Student("Charlie", 20, "A");
console.log(student.greet()); // Inherited method
console.log(student.study()); // Own method
```

### SOLID Principles in JavaScript

The SOLID principles help create maintainable and scalable JavaScript applications.

#### 1. Single Responsibility Principle (SRP)

```javascript
// ❌ Bad - Multiple responsibilities
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
    
    saveToDatabase() {
        // Database logic
        console.log('Saving to database...');
    }
    
    sendEmail() {
        // Email logic
        console.log('Sending email...');
    }
    
    validateEmail() {
        // Validation logic
        return this.email.includes('@');
    }
}

// ✅ Good - Single responsibility per class
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
}

class UserRepository {
    save(user) {
        console.log(`Saving ${user.name} to database...`);
    }
}

class EmailService {
    send(user, message) {
        console.log(`Sending email to ${user.email}: ${message}`);
    }
}

class EmailValidator {
    isValid(email) {
        return email.includes('@') && email.includes('.');
    }
}
```

#### 2. Open/Closed Principle (OCP)

```javascript
// ✅ Good - Open for extension, closed for modification
class Shape {
    area() {
        throw new Error('area() method must be implemented');
    }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }
    
    area() {
        return Math.PI * this.radius ** 2;
    }
}

class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }
    
    area() {
        return this.width * this.height;
    }
}

class AreaCalculator {
    calculateTotal(shapes) {
        return shapes.reduce((total, shape) => total + shape.area(), 0);
    }
}

// Adding new shapes doesn't modify existing code
class Triangle extends Shape {
    constructor(base, height) {
        super();
        this.base = base;
        this.height = height;
    }
    
    area() {
        return 0.5 * this.base * this.height;
    }
}
```

#### 3. Liskov Substitution Principle (LSP)

```javascript
// ✅ Good - Proper inheritance hierarchy
class Bird {
    move() {
        throw new Error('move() method must be implemented');
    }
}

class FlyingBird extends Bird {
    move() {
        return this.fly();
    }
    
    fly() {
        return 'Flying through the air';
    }
}

class WalkingBird extends Bird {
    move() {
        return this.walk();
    }
    
    walk() {
        return 'Walking on the ground';
    }
}

class Eagle extends FlyingBird {
    fly() {
        return 'Soaring majestically';
    }
}

class Penguin extends WalkingBird {
    walk() {
        return 'Waddling on ice';
    }
}

// All birds can be used interchangeably
function makeBirdMove(bird) {
    return bird.move();
}

const eagle = new Eagle();
const penguin = new Penguin();
console.log(makeBirdMove(eagle));   // Works correctly
console.log(makeBirdMove(penguin)); // Works correctly
```

#### 4. Interface Segregation Principle (ISP)

```javascript
// ❌ Bad - Fat interface
class Worker {
    work() {
        throw new Error('work() must be implemented');
    }
    
    eat() {
        throw new Error('eat() must be implemented');
    }
    
    sleep() {
        throw new Error('sleep() must be implemented');
    }
}

// ✅ Good - Segregated interfaces (using mixins in JavaScript)
const Workable = {
    work() {
        throw new Error('work() must be implemented');
    }
};

const Eatable = {
    eat() {
        throw new Error('eat() must be implemented');
    }
};

const Sleepable = {
    sleep() {
        throw new Error('sleep() must be implemented');
    }
};

class Human {
    constructor(name) {
        this.name = name;
        Object.assign(this, Workable, Eatable, Sleepable);
    }
    
    work() {
        return `${this.name} is working`;
    }
    
    eat() {
        return `${this.name} is eating`;
    }
    
    sleep() {
        return `${this.name} is sleeping`;
    }
}

class Robot {
    constructor(model) {
        this.model = model;
        Object.assign(this, Workable);
    }
    
    work() {
        return `${this.model} robot is working`;
    }
    // Robot doesn't implement eat() or sleep()
}
```

#### 5. Dependency Inversion Principle (DIP)

```javascript
// ❌ Bad - High-level module depends on low-level module
class FileLogger {
    log(message) {
        console.log(`File: ${message}`);
    }
}

class OrderService {
    constructor() {
        this.logger = new FileLogger(); // Direct dependency
    }
    
    createOrder(order) {
        // Create order logic
        this.logger.log(`Order ${order.id} created`);
    }
}

// ✅ Good - Depend on abstraction
class Logger {
    log(message) {
        throw new Error('log() method must be implemented');
    }
}

class FileLogger extends Logger {
    log(message) {
        console.log(`[FILE] ${new Date().toISOString()}: ${message}`);
    }
}

class DatabaseLogger extends Logger {
    log(message) {
        console.log(`[DB] ${new Date().toISOString()}: ${message}`);
    }
}

class ConsoleLogger extends Logger {
    log(message) {
        console.log(`[CONSOLE] ${message}`);
    }
}

class OrderService {
    constructor(logger) {
        this.logger = logger; // Depends on abstraction
    }
    
    createOrder(order) {
        // Create order logic
        this.logger.log(`Order ${order.id} created successfully`);
    }
}

// Usage with dependency injection
const fileLogger = new FileLogger();
const orderService = new OrderService(fileLogger);

// Easy to switch implementations
const consoleLogger = new ConsoleLogger();
const orderServiceWithConsole = new OrderService(consoleLogger);
```

#### SOLID Principles in Practice

```javascript
// Real-world example combining all SOLID principles

// Interfaces (using classes as contracts)
class PaymentProcessor {
    process(amount) {
        throw new Error('process() must be implemented');
    }
}

class NotificationService {
    send(message, recipient) {
        throw new Error('send() must be implemented');
    }
}

class Logger {
    log(message) {
        throw new Error('log() must be implemented');
    }
}

// Concrete implementations (SRP)
class StripePaymentProcessor extends PaymentProcessor {
    process(amount) {
        return { success: true, transactionId: `stripe_${Date.now()}` };
    }
}

class PayPalPaymentProcessor extends PaymentProcessor {
    process(amount) {
        return { success: true, transactionId: `paypal_${Date.now()}` };
    }
}

class EmailNotificationService extends NotificationService {
    send(message, recipient) {
        console.log(`Email sent to ${recipient}: ${message}`);
    }
}

class SMSNotificationService extends NotificationService {
    send(message, recipient) {
        console.log(`SMS sent to ${recipient}: ${message}`);
    }
}

class ConsoleLogger extends Logger {
    log(message) {
        console.log(`[LOG] ${new Date().toISOString()}: ${message}`);
    }
}

// High-level module (DIP)
class OrderProcessor {
    constructor(paymentProcessor, notificationService, logger) {
        this.paymentProcessor = paymentProcessor;
        this.notificationService = notificationService;
        this.logger = logger;
    }
    
    processOrder(order) {
        try {
            this.logger.log(`Processing order ${order.id}`);
            
            const result = this.paymentProcessor.process(order.amount);
            
            if (result.success) {
                this.notificationService.send(
                    `Your order ${order.id} has been processed successfully!`,
                    order.customerEmail
                );
                this.logger.log(`Order ${order.id} completed successfully`);
                return { success: true, transactionId: result.transactionId };
            }
        } catch (error) {
            this.logger.log(`Order ${order.id} failed: ${error.message}`);
            return { success: false, error: error.message };
        }
    }
}

// Usage with dependency injection
const stripeProcessor = new StripePaymentProcessor();
const emailService = new EmailNotificationService();
const logger = new ConsoleLogger();

const orderProcessor = new OrderProcessor(stripeProcessor, emailService, logger);

const order = {
    id: 'ORD-001',
    amount: 99.99,
    customerEmail: 'customer@example.com'
};

orderProcessor.processOrder(order);
```

---

## 9. Functional Programming

### Pure Functions

```javascript
// Pure function - no side effects, same input = same output
function add(a, b) {
    return a + b;
}

// Impure function - has side effects
let counter = 0;
function impureIncrement() {
    counter++; // Modifies external state
    return counter;
}

// Pure function alternative
function pureIncrement(value) {
    return value + 1;
}
```

### Array Methods for Functional Programming

```javascript
const numbers = [1, 2, 3, 4, 5];

// Map - transform each element
const doubled = numbers.map(n => n * 2);
const words = numbers.map(n => `Number ${n}`);

// Filter - select elements based on condition
const evens = numbers.filter(n => n % 2 === 0);
const greaterThanThree = numbers.filter(n => n > 3);

// Reduce - accumulate values
const sum = numbers.reduce((total, n) => total + n, 0);
const product = numbers.reduce((total, n) => total * n, 1);
const max = numbers.reduce((max, n) => n > max ? n : max, -Infinity);

// Chaining methods
const result = numbers
    .filter(n => n % 2 === 0)  // Get even numbers
    .map(n => n * n)           // Square them
    .reduce((sum, n) => sum + n, 0); // Sum them up

// Some and every
const hasEven = numbers.some(n => n % 2 === 0);    // true if any even
const allPositive = numbers.every(n => n > 0);     // true if all positive
```

### Function Composition

```javascript
// Simple function composition
const compose = (f, g) => (x) => f(g(x));
const pipe = (f, g) => (x) => g(f(x));

const addOne = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

// Using compose (right to left)
const addOneThenDouble = compose(double, addOne);
console.log(addOneThenDouble(3)); // (3 + 1) * 2 = 8

// Using pipe (left to right)
const doubleeThenAddOne = pipe(double, addOne);
console.log(doubleeThenAddOne(3)); // (3 * 2) + 1 = 7

// Multiple function composition
const multiCompose = (...fns) => (value) => fns.reduceRight((acc, fn) => fn(acc), value);
const multiPipe = (...fns) => (value) => fns.reduce((acc, fn) => fn(acc), value);

const complexOperation = multiPipe(addOne, double, square);
console.log(complexOperation(3)); // ((3 + 1) * 2) ^ 2 = 64
```

### Immutability

```javascript
// Immutable array operations
const originalArray = [1, 2, 3, 4, 5];

// Adding elements (immutable)
const withNewElement = [...originalArray, 6];
const withElementAtStart = [0, ...originalArray];

// Removing elements (immutable)
const withoutFirst = originalArray.slice(1);
const withoutLast = originalArray.slice(0, -1);
const withoutMiddle = originalArray.filter((_, index) => index !== 2);

// Modifying elements (immutable)
const doubled = originalArray.map(n => n * 2);
const replacedAtIndex = originalArray.map((n, i) => i === 2 ? 99 : n);

// Immutable object operations
const originalObject = {name: "Alice", age: 30, city: "NYC"};

// Adding properties (immutable)
const withNewProperty = {...originalObject, email: "alice@example.com"};

// Modifying properties (immutable)
const withModifiedAge = {...originalObject, age: 31};

// Removing properties (immutable)
const {city, ...withoutCity} = originalObject;

// Deep cloning for nested objects
const deepClone = obj => JSON.parse(JSON.stringify(obj));
const complexObject = {
    user: {name: "Alice", preferences: {theme: "dark"}}
};
const cloned = deepClone(complexObject);
```

---

## 10. Error Handling

### Try-Catch-Finally

```javascript
// Basic error handling
try {
    const result = riskyOperation();
    console.log("Success:", result);
} catch (error) {
    console.error("Error occurred:", error.message);
} finally {
    console.log("This always executes");
}

// Specific error types
try {
    JSON.parse(invalidJSON);
} catch (error) {
    if (error instanceof SyntaxError) {
        console.error("Invalid JSON format");
    } else if (error instanceof TypeError) {
        console.error("Type error occurred");
    } else {
        console.error("Unknown error:", error);
    }
}

// Rethrowing errors
function processData(data) {
    try {
        return JSON.parse(data);
    } catch (error) {
        console.error("Failed to parse data");
        throw error; // Rethrow for caller to handle
    }
}
```

### Custom Errors

```javascript
// Custom error class
class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

// Using custom errors
function validateAge(age) {
    if (typeof age !== 'number') {
        throw new ValidationError("Age must be a number", "age");
    }
    if (age < 0) {
        throw new ValidationError("Age cannot be negative", "age");
    }
    if (age > 150) {
        throw new ValidationError("Age seems unrealistic", "age");
    }
}

// Handling custom errors
try {
    validateAge(-5);
} catch (error) {
    if (error instanceof ValidationError) {
        console.error(`Validation error in ${error.field}: ${error.message}`);
    } else {
        console.error("Unexpected error:", error);
    }
}
```

### Error Handling with Promises

```javascript
// Promise error handling
fetchUserData(1)
    .then(user => {
        console.log("User:", user);
    })
    .catch(error => {
        console.error("Failed to fetch user:", error);
    });

// Async/await error handling
async function fetchUserSafely(userId) {
    try {
        const user = await fetchUserData(userId);
        return { success: true, data: user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Error handling with Promise.all
async function fetchMultipleUsersSafely(userIds) {
    try {
        const users = await Promise.all(
            userIds.map(id => fetchUserData(id))
        );
        return users;
    } catch (error) {
        console.error("One or more users failed to load:", error);
        
        // Alternative: Handle individual failures
        const results = await Promise.allSettled(
            userIds.map(id => fetchUserData(id))
        );
        
        const successful = results
            .filter(result => result.status === 'fulfilled')
            .map(result => result.value);
            
        const failed = results
            .filter(result => result.status === 'rejected')
            .map(result => result.reason);
            
        return { successful, failed };
    }
}
```

---

## 11. Node.js Backend Development

### Express.js Server

```javascript
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet()); // Security headers
app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies

// Basic routes
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to Node.js API!' });
});

app.get('/api/users', (req, res) => {
    const users = [
        { id: 1, name: 'Alice', email: 'alice@example.com' },
        { id: 2, name: 'Bob', email: 'bob@example.com' }
    ];
    res.json({ users });
});

app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    
    if (!name || !email) {
        return res.status(400).json({ error: 'Name and email required' });
    }
    
    const newUser = { id: Date.now(), name, email };
    res.status(201).json({ user: newUser });
});

app.get('/api/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    // Simulate database lookup
    const user = { id: userId, name: 'Sample User', email: 'user@example.com' };
    res.json(user);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// 404 handler
app.use('*', (req, res) => {
    res.status(404).json({ error: 'Route not found' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### File System Operations

```javascript
const fs = require('fs').promises;
const path = require('path');

class FileManager {
    async readFile(filePath) {
        try {
            const data = await fs.readFile(filePath, 'utf8');
            return data;
        } catch (error) {
            throw new Error(`Failed to read file: ${error.message}`);
        }
    }
    
    async writeFile(filePath, data) {
        try {
            await fs.writeFile(filePath, data, 'utf8');
            console.log(`File written successfully: ${filePath}`);
        } catch (error) {
            throw new Error(`Failed to write file: ${error.message}`);
        }
    }
    
    async listDirectory(dirPath) {
        try {
            const files = await fs.readdir(dirPath);
            return files.filter(file => !file.startsWith('.'));
        } catch (error) {
            throw new Error(`Failed to list directory: ${error.message}`);
        }
    }
    
    async createDirectory(dirPath) {
        try {
            await fs.mkdir(dirPath, { recursive: true });
            console.log(`Directory created: ${dirPath}`);
        } catch (error) {
            throw new Error(`Failed to create directory: ${error.message}`);
        }
    }
    
    async fileExists(filePath) {
        try {
            await fs.access(filePath);
            return true;
        } catch {
            return false;
        }
    }
}

// Usage
const fileManager = new FileManager();

async function exampleUsage() {
    try {
        await fileManager.writeFile('./example.txt', 'Hello, Node.js!');
        const content = await fileManager.readFile('./example.txt');
        console.log('File content:', content);
        
        const files = await fileManager.listDirectory('./');
        console.log('Directory contents:', files);
    } catch (error) {
        console.error('Error:', error.message);
    }
}
```

---

## 12. Testing Frameworks

### Jest Testing Framework

```javascript
// calculator.js
class Calculator {
    add(a, b) {
        return a + b;
    }
    
    subtract(a, b) {
        return a - b;
    }
    
    multiply(a, b) {
        return a * b;
    }
    
    divide(a, b) {
        if (b === 0) {
            throw new Error('Division by zero');
        }
        return a / b;
    }
    
    async fetchData(url) {
        // Simulate API call
        return new Promise(resolve => {
            setTimeout(() => resolve(`Data from ${url}`), 100);
        });
    }
}

module.exports = Calculator;

// calculator.test.js
const Calculator = require('./calculator');

describe('Calculator', () => {
    let calculator;
    
    beforeEach(() => {
        calculator = new Calculator();
    });
    
    describe('Basic Operations', () => {
        test('should add two numbers correctly', () => {
            expect(calculator.add(2, 3)).toBe(5);
            expect(calculator.add(-1, 1)).toBe(0);
        });
        
        test('should subtract two numbers correctly', () => {
            expect(calculator.subtract(5, 3)).toBe(2);
            expect(calculator.subtract(0, 5)).toBe(-5);
        });
        
        test('should multiply two numbers correctly', () => {
            expect(calculator.multiply(3, 4)).toBe(12);
            expect(calculator.multiply(-2, 3)).toBe(-6);
        });
        
        test('should divide two numbers correctly', () => {
            expect(calculator.divide(8, 2)).toBe(4);
            expect(calculator.divide(7, 2)).toBe(3.5);
        });
        
        test('should throw error when dividing by zero', () => {
            expect(() => calculator.divide(5, 0)).toThrow('Division by zero');
        });
    });
    
    describe('Async Operations', () => {
        test('should fetch data successfully', async () => {
            const result = await calculator.fetchData('https://api.example.com');
            expect(result).toBe('Data from https://api.example.com');
        });
        
        test('should handle multiple async calls', async () => {
            const promises = [
                calculator.fetchData('url1'),
                calculator.fetchData('url2')
            ];
            const results = await Promise.all(promises);
            expect(results).toHaveLength(2);
        });
    });
    
    describe('Edge Cases', () => {
        test('should handle floating point precision', () => {
            expect(calculator.add(0.1, 0.2)).toBeCloseTo(0.3);
        });
        
        test('should handle large numbers', () => {
            const largeNum = Number.MAX_SAFE_INTEGER;
            expect(calculator.add(largeNum, 1)).toBe(largeNum + 1);
        });
    });
});

// Mocking example
jest.mock('./external-service');
const externalService = require('./external-service');

test('should use mocked service', async () => {
    externalService.getData.mockResolvedValue({ id: 1, name: 'Test' });
    
    const result = await someFunction();
    expect(result).toEqual({ id: 1, name: 'Test' });
    expect(externalService.getData).toHaveBeenCalledTimes(1);
});
```

### Test-Driven Development (TDD)

```javascript
// 1. Write failing test first
describe('UserService', () => {
    test('should create user with valid data', () => {
        const userService = new UserService();
        const userData = { name: 'Alice', email: 'alice@example.com' };
        
        const user = userService.createUser(userData);
        
        expect(user.id).toBeDefined();
        expect(user.name).toBe('Alice');
        expect(user.email).toBe('alice@example.com');
        expect(user.createdAt).toBeInstanceOf(Date);
    });
    
    test('should throw error for invalid email', () => {
        const userService = new UserService();
        const userData = { name: 'Alice', email: 'invalid-email' };
        
        expect(() => userService.createUser(userData)).toThrow('Invalid email');
    });
});

// 2. Write minimal code to make test pass
class UserService {
    createUser(userData) {
        if (!this.isValidEmail(userData.email)) {
            throw new Error('Invalid email');
        }
        
        return {
            id: Date.now(),
            name: userData.name,
            email: userData.email,
            createdAt: new Date()
        };
    }
    
    isValidEmail(email) {
        return email.includes('@') && email.includes('.');
    }
}

// 3. Refactor code while keeping tests green
```

---

## 13. Advanced Concepts

### Closures

```javascript
// Basic closure
function outerFunction(x) {
    // Variable in outer scope
    return function innerFunction(y) {
        return x + y; // Accesses variable from outer scope
    };
}

const addFive = outerFunction(5);
console.log(addFive(3)); // 8

// Practical closure example - Module pattern
const counterModule = (function() {
    let count = 0; // Private variable
    
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
})();

console.log(counterModule.increment()); // 1
console.log(counterModule.increment()); // 2
console.log(counterModule.getCount()); // 2
// console.log(count); // ReferenceError - count is private
```

### Prototypal Inheritance

```javascript
// Creating objects with Object.create
const animalPrototype = {
    speak() {
        return `${this.name} makes a sound`;
    },
    eat() {
        return `${this.name} is eating`;
    }
};

const dog = Object.create(animalPrototype);
dog.name = "Buddy";
dog.speak = function() {
    return `${this.name} barks!`;
};

console.log(dog.speak()); // "Buddy barks!"
console.log(dog.eat());   // "Buddy is eating"

// Prototype chain
console.log(dog.__proto__ === animalPrototype); // true
console.log(animalPrototype.__proto__ === Object.prototype); // true
```

### Symbols

```javascript
// Creating symbols
const sym1 = Symbol('description');
const sym2 = Symbol('description');
console.log(sym1 === sym2); // false - each symbol is unique

// Using symbols as object properties
const SECRET_PROPERTY = Symbol('secret');
const obj = {
    name: 'Alice',
    [SECRET_PROPERTY]: 'This is secret'
};

console.log(obj.name); // 'Alice'
console.log(obj[SECRET_PROPERTY]); // 'This is secret'

// Symbols are not enumerable
console.log(Object.keys(obj)); // ['name'] - symbol property not included

// Well-known symbols
const customIterable = {
    data: [1, 2, 3],
    [Symbol.iterator]() {
        let index = 0;
        return {
            next: () => {
                if (index < this.data.length) {
                    return { value: this.data[index++], done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
};

for (const value of customIterable) {
    console.log(value); // 1, 2, 3
}
```

### Iterators and Generators

```javascript
// Generator function
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }

// Infinite generator
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

const fib = fibonacci();
console.log([fib.next().value, fib.next().value, fib.next().value]); // [0, 1, 1]

// Generator with parameters
function* range(start, end, step = 1) {
    for (let i = start; i < end; i += step) {
        yield i;
    }
}

console.log([...range(0, 10, 2)]); // [0, 2, 4, 6, 8]

// Async generators
async function* asyncNumberGenerator() {
    for (let i = 0; i < 3; i++) {
        await new Promise(resolve => setTimeout(resolve, 100));
        yield i;
    }
}

async function useAsyncGenerator() {
    for await (const num of asyncNumberGenerator()) {
        console.log(num); // 0, 1, 2 (with delays)
    }
}
```

---

## 14. Performance Optimization

### Memory Management

```javascript
// Avoiding memory leaks
// 1. Remove event listeners
function addListener() {
    const button = document.getElementById('myButton');
    const handler = () => console.log('Clicked');
    
    button.addEventListener('click', handler);
    
    // Remember to remove listener when done
    return () => button.removeEventListener('click', handler);
}

// 2. Clear timers
const timerId = setTimeout(() => {
    console.log('Timer executed');
}, 1000);

// Clear timer if needed
clearTimeout(timerId);

// 3. Weak references for caches
const cache = new WeakMap();

function expensiveOperation(obj) {
    if (cache.has(obj)) {
        return cache.get(obj);
    }
    
    const result = /* expensive computation */ obj.value * 2;
    cache.set(obj, result);
    return result;
}
```

### Debouncing and Throttling

```javascript
// Debouncing - delay execution until after calls have stopped
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

// Usage: Search input
const searchInput = document.getElementById('search');
const debouncedSearch = debounce((event) => {
    console.log('Searching for:', event.target.value);
    // Perform search API call
}, 300);

searchInput.addEventListener('input', debouncedSearch);

// Throttling - limit execution to once per time period
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Usage: Scroll event
const throttledScroll = throttle(() => {
    console.log('Scroll event handled');
}, 100);

window.addEventListener('scroll', throttledScroll);
```

### Object Pooling

```javascript
// Object pooling for performance
class ObjectPool {
    constructor(createFn, resetFn, maxSize = 10) {
        this.createFn = createFn;
        this.resetFn = resetFn;
        this.maxSize = maxSize;
        this.pool = [];
    }
    
    acquire() {
        if (this.pool.length > 0) {
            return this.pool.pop();
        }
        return this.createFn();
    }
    
    release(obj) {
        if (this.pool.length < this.maxSize) {
            this.resetFn(obj);
            this.pool.push(obj);
        }
    }
}

// Example: Vector pool for game development
const vectorPool = new ObjectPool(
    () => ({ x: 0, y: 0 }),
    (vector) => { vector.x = 0; vector.y = 0; }
);

function gameLoop() {
    const velocity = vectorPool.acquire();
    velocity.x = 10;
    velocity.y = 5;
    
    // Use velocity for calculations
    
    vectorPool.release(velocity); // Return to pool
}
```

---

## 15. Modern JavaScript Ecosystem

### Package.json and NPM

```json
{
  "name": "modern-js-project",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/",
    "format": "prettier --write src/",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.0.0",
    "@vitejs/plugin-react": "^4.0.0",
    "eslint": "^8.0.0",
    "jest": "^29.0.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0",
    "vite": "^4.0.0"
  }
}
```

### Vite Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    hot: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    minify: 'terser'
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
});
```

### ESLint Configuration

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    'prettier'
  ],
  rules: {
    'no-console': 'warn',
    'prefer-const': 'error',
    'no-var': 'error'
  }
};
```

### Modern Module System

```javascript
// ES Modules (modern)
// math.js
export const PI = 3.14159;
export function add(a, b) {
    return a + b;
}
export default function multiply(a, b) {
    return a * b;
}

// main.js
import multiply, { add, PI } from './math.js';
import * as math from './math.js';

console.log(add(2, 3));        // 5
console.log(multiply(2, 3));   // 6
console.log(math.PI);          // 3.14159

// Dynamic imports
async function loadModule() {
    const { add } = await import('./math.js');
    return add(5, 3);
}

// CommonJS (Node.js)
// math.js
const PI = 3.14159;
function add(a, b) {
    return a + b;
}
module.exports = { PI, add };

// main.js
const { PI, add } = require('./math');
```

---

## 🚀 Next Steps for JavaScript Mastery

### 1. **Advanced Patterns**
- Learn design patterns (Observer, Module, Factory)
- Master functional programming concepts
- Understand reactive programming with RxJS

### 2. **Framework Expertise**
- **React**: Hooks, Context, state management
- **Vue**: Composition API, Vuex/Pinia
- **Angular**: Components, services, dependency injection

### 3. **Node.js Mastery**
- Express.js and middleware
- Database integration (MongoDB, PostgreSQL)
- Authentication and security
- Microservices architecture

### 4. **Testing Strategy**
- Unit testing with Jest
- Integration testing
- End-to-end testing with Cypress
- Test-driven development (TDD)

### 5. **Build Tools & DevOps**
- Webpack, Vite, Rollup configuration
- CI/CD pipelines
- Docker containers
- Performance monitoring

### 6. **Modern Web APIs**
- Service Workers and PWAs
- WebRTC for real-time communication
- Web Workers for background processing
- WebAssembly integration

---

## 📖 JavaScript Concepts Quick Reference

| Category | Key Concepts |
|----------|-------------|
| **Fundamentals** | Variables, data types, operators |
| **Functions** | Arrow functions, closures, higher-order functions |
| **Objects** | Prototypes, classes, inheritance, SOLID principles |
| **Async** | Promises, async/await, event loop |
| **DOM** | Selectors, events, manipulation |
| **ES6+** | Destructuring, spread/rest, modules |
| **Functional** | Map, filter, reduce, immutability |
| **Advanced** | Generators, symbols, weak collections |
| **Testing** | Jest, mocking, TDD |
| **Performance** | Debouncing, throttling, memory management |

---

> **🎉 Congratulations!** You now have a complete JavaScript reference covering all concepts from beginner to expert level. This guide prepares you for modern web development, interviews, and advanced JavaScript projects.

**Ready for the next level?** Consider learning TypeScript, React/Vue/Angular, or diving deeper into Node.js backend development!