# 🟨 JavaScript Complete Mastery Guide

> **Complete JavaScript Reference for Interview Preparation and Modern Development**  
> From Beginner to Expert Level - All Concepts Covered

---

## 📚 Table of Contents

### Core JavaScript
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

### Backend & Testing
11. [Node.js Backend Development](#11-nodejs-backend-development)
12. [Testing Frameworks](#12-testing-frameworks)

### Advanced Topics
13. [Advanced Concepts](#13-advanced-concepts)
14. [Performance Optimization](#14-performance-optimization)
15. [Modern JavaScript Ecosystem](#15-modern-javascript-ecosystem)

### Interview-Critical Topics ⭐
16. [⚛️ React Framework](#16-️-react-framework-essential-for-interviews)
17. [�️ Angular Framework](#17-️-angular-framework)
18. [�🎨 Design Patterns](#18--design-patterns-in-javascript)
19. [🔒 Security Best Practices](#19--security-best-practices)
20. [🔌 WebSockets & Real-time Communication](#20--websockets--real-time-communication)

---

## 1. JavaScript Fundamentals

**JavaScript is a dynamic, weakly-typed programming language that runs in browsers and on servers (Node.js).** Understanding variables, data types, and type coercion is fundamental to writing effective JavaScript code. JavaScript uses hoisting, which moves declarations to the top of their scope during compilation.

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

// Type checking - typeof operator returns string type
console.log(typeof number);    // "number"
console.log(typeof string);    // "string"
console.log(typeof boolean);   // "boolean"
console.log(typeof undefinedValue); // "undefined"
console.log(typeof nullValue); // "object" (historical quirk - bug in JS)
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

**JavaScript has 7 primitive types (string, number, bigint, boolean, undefined, null, symbol) and reference types (objects, arrays, functions).** Primitives are immutable and passed by value, while objects are passed by reference. Understanding the difference is crucial for avoiding bugs and memory issues.

### Strings

```javascript
// String creation
const singleQuotes = 'Hello, World!';
const doubleQuotes = "Hello, JavaScript!";
const templateLiteral = `Hello, ${name}!`;

// String methods - powerful built-in operations
const text = "JavaScript Programming";
console.log(text.length);              // 21 (number of characters)
console.log(text.toUpperCase());       // "JAVASCRIPT PROGRAMMING"
console.log(text.toLowerCase());       // "javascript programming"
console.log(text.slice(0, 10));       // "JavaScript" (extract substring)
console.log(text.substring(0, 10));    // "JavaScript" (similar to slice)
console.log(text.indexOf("Script"));   // 4 (position of substring)
console.log(text.includes("Program")); // true (checks if contains)
console.log(text.split(" "));          // ["JavaScript", "Programming"] (array)

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

**Functions are first-class citizens in JavaScript, meaning they can be assigned to variables, passed as arguments, and returned from other functions.** JavaScript supports multiple function syntaxes including declarations, expressions, and arrow functions. Understanding function scope, closures, and the 'this' keyword is essential for mastering JavaScript.

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

const double = createMultiplier(2);  // Returns function that multiplies by 2
const triple = createMultiplier(3);  // Returns function that multiplies by 3

console.log(double(5)); // 10 (5 * 2)
console.log(triple(5)); // 15 (5 * 3)

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

**Objects are key-value collections and the foundation of JavaScript's data structures, while arrays are ordered lists with powerful iteration methods.** Objects use prototypal inheritance, and arrays come with rich built-in methods like map, filter, and reduce. Destructuring and spread operators provide modern syntax for working with these structures efficiently.

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

// Array transformation - map/filter/reduce are essential
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8, 10]
const evens = numbers.filter(n => n % 2 === 0);  // [2, 4]
const sum = numbers.reduce((total, n) => total + n, 0);  // 15

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

**ES6 (ECMAScript 2015) and beyond introduced major improvements to JavaScript including let/const, arrow functions, classes, modules, and async/await.** These features make JavaScript more expressive, readable, and powerful. Modern JavaScript development relies heavily on these enhancements, making code cleaner and more maintainable.

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

**JavaScript is single-threaded but handles asynchronous operations through the event loop, callbacks, promises, and async/await.** Async programming is essential for handling API calls, file operations, and timers without blocking the main thread. Modern async/await syntax makes asynchronous code look and behave like synchronous code, improving readability.

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

**The Document Object Model (DOM) is a tree-like representation of HTML that JavaScript can interact with to dynamically modify web pages.** DOM manipulation involves selecting elements, modifying content/styles, handling events, and creating/removing elements. Understanding event propagation (bubbling and capturing) and event delegation is crucial for building interactive web applications.

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

**JavaScript uses prototypal inheritance but ES6 added class syntax for cleaner OOP code.** Classes support constructors, instance/static methods, getters/setters, and inheritance through extends. Understanding SOLID principles helps create maintainable, scalable object-oriented JavaScript applications.

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

**Functional programming treats computation as the evaluation of mathematical functions, avoiding state changes and mutable data.** Key concepts include pure functions (no side effects), immutability, higher-order functions, and function composition. Functional programming leads to more predictable, testable, and maintainable code.

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

// Using compose (right to left execution)
const addOneThenDouble = compose(double, addOne);
console.log(addOneThenDouble(3)); // 8 - first addOne(3)=4, then double(4)=8

// Using pipe (left to right execution)
const doubleThenAddOne = pipe(double, addOne);
console.log(doubleThenAddOne(3)); // 7 - first double(3)=6, then addOne(6)=7

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

**Proper error handling prevents application crashes and provides meaningful feedback when things go wrong.** JavaScript offers try-catch-finally blocks for synchronous code and .catch() for promises/async functions. Creating custom error classes helps categorize and handle different error types appropriately in production applications.

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

**Node.js enables JavaScript to run on servers, making it possible to use JavaScript for full-stack development.** Node.js uses an event-driven, non-blocking I/O model that makes it efficient for handling concurrent requests. Express.js is the most popular Node.js framework for building web servers and REST APIs.

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

### Express.js Middleware Patterns

```javascript
const express = require('express');
const app = express();

// Built-in middleware
app.use(express.json());  // Parse JSON bodies
app.use(express.urlencoded({ extended: true }));  // Parse URL-encoded bodies
app.use(express.static('public'));  // Serve static files

// Custom middleware - Logging
const requestLogger = (req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    console.log('Headers:', req.headers);
    console.log('Body:', req.body);
    next();  // Pass control to next middleware
};

app.use(requestLogger);

// Authentication middleware
const authenticate = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];
    
    if (!token) {
        return res.status(401).json({ error: 'No token provided' });
    }
    
    try {
        const decoded = verifyToken(token);
        req.user = decoded;  // Attach user to request
        next();
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
};

// Role-based authorization middleware
const authorize = (...roles) => {
    return (req, res, next) => {
        if (!req.user) {
            return res.status(401).json({ error: 'Not authenticated' });
        }
        
        if (!roles.includes(req.user.role)) {
            return res.status(403).json({ error: 'Insufficient permissions' });
        }
        
        next();
    };
};

// Validation middleware
const validateUser = (req, res, next) => {
    const { name, email, age } = req.body;
    const errors = [];
    
    if (!name || name.length < 2) {
        errors.push('Name must be at least 2 characters');
    }
    
    if (!email || !email.includes('@')) {
        errors.push('Valid email is required');
    }
    
    if (age && (age < 0 || age > 150)) {
        errors.push('Age must be between 0 and 150');
    }
    
    if (errors.length > 0) {
        return res.status(400).json({ errors });
    }
    
    next();
};

// Error handling middleware (must be last)
const errorHandler = (err, req, res, next) => {
    console.error('Error:', err);
    
    if (err.name === 'ValidationError') {
        return res.status(400).json({ error: err.message });
    }
    
    if (err.name === 'UnauthorizedError') {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    
    res.status(500).json({ error: 'Internal server error' });
};

// Using middleware in routes
app.post('/api/users', validateUser, (req, res) => {
    const user = createUser(req.body);
    res.status(201).json({ user });
});

app.get('/api/admin', authenticate, authorize('admin'), (req, res) => {
    res.json({ message: 'Admin access granted', user: req.user });
});

app.use(errorHandler);
```

### Express.js REST API Best Practices

```javascript
const express = require('express');
const router = express.Router();

// RESTful routes structure
// GET /api/users - Get all users
router.get('/users', async (req, res, next) => {
    try {
        const { page = 1, limit = 10, sort = 'createdAt' } = req.query;
        
        const users = await User.find()
            .limit(limit * 1)
            .skip((page - 1) * limit)
            .sort(sort)
            .select('-password');  // Exclude password field
        
        const count = await User.countDocuments();
        
        res.json({
            users,
            totalPages: Math.ceil(count / limit),
            currentPage: page,
            total: count
        });
    } catch (error) {
        next(error);  // Pass to error handler
    }
});

// GET /api/users/:id - Get single user
router.get('/users/:id', async (req, res, next) => {
    try {
        const user = await User.findById(req.params.id).select('-password');
        
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        
        res.json({ user });
    } catch (error) {
        next(error);
    }
});

// POST /api/users - Create user
router.post('/users', validateUser, async (req, res, next) => {
    try {
        const user = await User.create(req.body);
        res.status(201).json({ user: user.toJSON() });  // 201 = Created
    } catch (error) {
        if (error.code === 11000) {  // Duplicate key error
            return res.status(409).json({ error: 'User already exists' });
        }
        next(error);
    }
});

// PUT /api/users/:id - Update entire user
router.put('/users/:id', authenticate, async (req, res, next) => {
    try {
        const user = await User.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true, runValidators: true }
        );
        
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        
        res.json({ user });
    } catch (error) {
        next(error);
    }
});

// PATCH /api/users/:id - Partial update
router.patch('/users/:id', authenticate, async (req, res, next) => {
    try {
        const updates = req.body;
        const user = await User.findByIdAndUpdate(
            req.params.id,
            { $set: updates },
            { new: true, runValidators: true }
        );
        
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        
        res.json({ user });
    } catch (error) {
        next(error);
    }
});

// DELETE /api/users/:id - Delete user
router.delete('/users/:id', authenticate, authorize('admin'), async (req, res, next) => {
    try {
        const user = await User.findByIdAndDelete(req.params.id);
        
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        
        res.status(204).send();  // 204 = No Content
    } catch (error) {
        next(error);
    }
});

module.exports = router;
```

### Node.js Event Loop & Async Patterns

```javascript
// Understanding the Event Loop
console.log('1. Synchronous code');  // Executes first

setTimeout(() => {
    console.log('2. setTimeout callback');  // Macrotask - executes after microtasks
}, 0);

Promise.resolve().then(() => {
    console.log('3. Promise callback');  // Microtask - executes before macrotasks
});

process.nextTick(() => {
    console.log('4. nextTick callback');  // Executes before promises
});

console.log('5. More synchronous code');  // Executes second

// Output order:
// 1. Synchronous code
// 5. More synchronous code
// 4. nextTick callback
// 3. Promise callback
// 2. setTimeout callback

// Async patterns - Parallel execution
async function fetchAllData() {
    const start = Date.now();
    
    // Sequential (slow) - takes 3 seconds
    const user = await fetchUser(1);      // 1 second
    const posts = await fetchPosts(1);    // 1 second
    const comments = await fetchComments(1); // 1 second
    
    console.log(`Sequential: ${Date.now() - start}ms`);  // ~3000ms
    
    // Parallel (fast) - takes 1 second
    const [user2, posts2, comments2] = await Promise.all([
        fetchUser(2),
        fetchPosts(2),
        fetchComments(2)
    ]);
    
    console.log(`Parallel: ${Date.now() - start}ms`);  // ~1000ms
}

// Promise.allSettled - Handle both success and failure
async function fetchMultipleUsers(userIds) {
    const results = await Promise.allSettled(
        userIds.map(id => fetchUser(id))
    );
    
    const successful = results
        .filter(r => r.status === 'fulfilled')
        .map(r => r.value);
    
    const failed = results
        .filter(r => r.status === 'rejected')
        .map(r => ({ reason: r.reason.message }));
    
    return { successful, failed };
}

// Promise.race - First to complete wins
async function fetchWithTimeout(url, timeout = 5000) {
    return Promise.race([
        fetch(url),
        new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Request timeout')), timeout)
        )
    ]);
}

// Async iteration
async function processItems(items) {
    for (const item of items) {
        await processItem(item);  // Sequential processing
    }
}

async function processItemsConcurrent(items) {
    await Promise.all(items.map(item => processItem(item)));  // Parallel
}

// Async generators for streaming data
async function* fetchPages(startPage, endPage) {
    for (let page = startPage; page <= endPage; page++) {
        const data = await fetch(`/api/data?page=${page}`);
        yield data;
    }
}

async function processPages() {
    for await (const pageData of fetchPages(1, 10)) {
        console.log('Processing page:', pageData);
    }
}
```

### Node.js Worker Threads (Multithreading)

```javascript
// Node.js is single-threaded, but Worker Threads enable true parallelism
// main.js - Main thread
const { Worker } = require('worker_threads');
const path = require('path');

// Create a worker thread
function runWorker(data) {
    return new Promise((resolve, reject) => {
        const worker = new Worker(path.join(__dirname, 'worker.js'), {
            workerData: data
        });
        
        worker.on('message', resolve);  // Worker sends result
        worker.on('error', reject);     // Worker encounters error
        worker.on('exit', (code) => {
            if (code !== 0) {
                reject(new Error(`Worker stopped with exit code ${code}`));
            }
        });
    });
}

// Using worker for CPU-intensive task
async function calculatePrimes(max) {
    console.log('Main thread: Starting calculation...');
    const result = await runWorker({ task: 'calculatePrimes', max });
    console.log('Main thread: Calculation complete');
    return result;
}

// Using multiple workers for parallel processing
async function processDataParallel(dataChunks) {
    const workers = dataChunks.map(chunk => runWorker({ task: 'process', data: chunk }));
    return Promise.all(workers);
}

// Example usage
(async () => {
    const primes = await calculatePrimes(1000000);
    console.log(`Found ${primes.length} prime numbers`);
    
    // Process 4 chunks in parallel
    const chunks = [
        [1, 100000],
        [100001, 200000],
        [200001, 300000],
        [300001, 400000]
    ];
    const results = await processDataParallel(chunks);
    console.log('Parallel processing complete:', results);
})();

// worker.js - Worker thread
const { parentPort, workerData } = require('worker_threads');

function calculatePrimes(max) {
    const primes = [];
    for (let i = 2; i <= max; i++) {
        let isPrime = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primes.push(i);
    }
    return primes;
}

function processData(data) {
    // CPU-intensive processing
    return data.map(item => item * 2);
}

// Handle different tasks
if (workerData.task === 'calculatePrimes') {
    const result = calculatePrimes(workerData.max);
    parentPort.postMessage(result);
} else if (workerData.task === 'process') {
    const result = processData(workerData.data);
    parentPort.postMessage(result);
}

// Worker pool for reusable workers
class WorkerPool {
    constructor(workerScript, poolSize = 4) {
        this.workerScript = workerScript;
        this.poolSize = poolSize;
        this.workers = [];
        this.queue = [];
        
        for (let i = 0; i < poolSize; i++) {
            this.workers.push(this.createWorker());
        }
    }
    
    createWorker() {
        return {
            worker: null,
            inUse: false
        };
    }
    
    async execute(data) {
        return new Promise((resolve, reject) => {
            const availableWorker = this.workers.find(w => !w.inUse);
            
            if (availableWorker) {
                this.runTask(availableWorker, data, resolve, reject);
            } else {
                // Queue task if no workers available
                this.queue.push({ data, resolve, reject });
            }
        });
    }
    
    runTask(workerObj, data, resolve, reject) {
        workerObj.inUse = true;
        
        const worker = new Worker(this.workerScript, { workerData: data });
        workerObj.worker = worker;
        
        worker.on('message', (result) => {
            workerObj.inUse = false;
            worker.terminate();
            resolve(result);
            this.processQueue();
        });
        
        worker.on('error', (error) => {
            workerObj.inUse = false;
            worker.terminate();
            reject(error);
            this.processQueue();
        });
    }
    
    processQueue() {
        if (this.queue.length > 0) {
            const { data, resolve, reject } = this.queue.shift();
            const availableWorker = this.workers.find(w => !w.inUse);
            if (availableWorker) {
                this.runTask(availableWorker, data, resolve, reject);
            }
        }
    }
}

// Usage
const pool = new WorkerPool('./worker.js', 4);

async function processManyTasks() {
    const tasks = Array.from({ length: 100 }, (_, i) => ({ task: 'process', id: i }));
    const results = await Promise.all(tasks.map(task => pool.execute(task)));
    console.log('All tasks completed:', results.length);
}
```

### Node.js Streams for Large Data

```javascript
const fs = require('fs');
const { pipeline, Transform } = require('stream');
const zlib = require('zlib');

// Reading large files with streams (memory efficient)
const readStream = fs.createReadStream('large-file.txt', { 
    encoding: 'utf8',
    highWaterMark: 64 * 1024  // 64KB chunks
});

readStream.on('data', (chunk) => {
    console.log(`Received ${chunk.length} bytes`);
});

readStream.on('end', () => {
    console.log('Finished reading file');
});

readStream.on('error', (error) => {
    console.error('Error reading file:', error);
});

// Writing with streams
const writeStream = fs.createWriteStream('output.txt');
writeStream.write('Hello, ');
writeStream.write('World!\n');
writeStream.end();

// Pipe streams together
fs.createReadStream('input.txt')
    .pipe(fs.createWriteStream('output.txt'));

// Transform stream - process data as it flows
class UpperCaseTransform extends Transform {
    _transform(chunk, encoding, callback) {
        const upperCased = chunk.toString().toUpperCase();
        this.push(upperCased);
        callback();
    }
}

// Pipeline with error handling (recommended)
pipeline(
    fs.createReadStream('input.txt'),
    new UpperCaseTransform(),
    zlib.createGzip(),  // Compress
    fs.createWriteStream('output.txt.gz'),
    (error) => {
        if (error) {
            console.error('Pipeline failed:', error);
        } else {
            console.log('Pipeline succeeded');
        }
    }
);

// Backpressure handling
const readable = fs.createReadStream('large-file.txt');
const writable = fs.createWriteStream('output.txt');

readable.on('data', (chunk) => {
    const canContinue = writable.write(chunk);
    
    if (!canContinue) {
        // Backpressure - pause reading
        readable.pause();
    }
});

writable.on('drain', () => {
    // Buffer cleared - resume reading
    readable.resume();
});

// Async iteration over streams (Node.js 10+)
async function processFile(filePath) {
    const stream = fs.createReadStream(filePath, { encoding: 'utf8' });
    
    for await (const chunk of stream) {
        console.log('Processing chunk:', chunk.length);
        await processChunk(chunk);
    }
}
```

---

## 12. Testing Frameworks

**Automated testing ensures code reliability and makes refactoring safer by catching bugs early in development.** Jest is the most popular JavaScript testing framework, offering features like snapshot testing, mocking, and code coverage. Test-Driven Development (TDD) involves writing tests before implementing features, leading to better-designed code.

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

**Advanced JavaScript concepts include closures, prototypes, symbols, generators, and iterators that enable powerful programming patterns.** Closures allow functions to remember their lexical scope even when executed outside of it. Generators provide a way to create iterators with pause/resume functionality using yield.

### Closures

```javascript
// Basic closure
function outerFunction(x) {
    // Variable in outer scope
    return function innerFunction(y) {
        return x + y; // Accesses variable from outer scope
    };
}

const addFive = outerFunction(5);  // Returns inner function with x=5
console.log(addFive(3)); // 8 (5 + 3, closure remembers x=5)

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

console.log(counterModule.increment()); // 1 (count is now 1)
console.log(counterModule.increment()); // 2 (count is now 2)
console.log(counterModule.getCount()); // 2 (returns private count)
// console.log(count); // ReferenceError - count is private (not accessible)
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

**Performance optimization involves reducing memory usage, improving execution speed, and ensuring smooth user experiences.** Techniques like debouncing/throttling prevent excessive function calls, while proper memory management avoids leaks. Object pooling and lazy loading help manage resources efficiently in large applications.

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

**The modern JavaScript ecosystem includes package managers (npm/yarn), module bundlers (Webpack/Vite), transpilers (Babel), and development tools.** Package.json defines project dependencies and scripts, while build tools optimize code for production. Understanding the ecosystem is essential for professional JavaScript development.

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

## 16. ⚛️ React Framework (Essential for Interviews)

**React is the most popular JavaScript library for building user interfaces, using a component-based architecture and virtual DOM for efficient rendering.** React's declarative approach makes it easy to create interactive UIs. Understanding hooks, state management, and component lifecycle is crucial for modern React development.

### React Basics and JSX

```javascript
// React component with JSX
import React from 'react';

// Functional component
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;  // JSX - looks like HTML but is JavaScript
}

// Component with multiple elements
function App() {
    return (
        <div className="app">
            <Welcome name="Alice" />
            <Welcome name="Bob" />
        </div>
    );
}

// Component with props destructuring
const UserCard = ({ name, age, email }) => {
    return (
        <div className="user-card">
            <h2>{name}</h2>
            <p>Age: {age}</p>
            <p>Email: {email}</p>
        </div>
    );
};
```

### React Hooks - useState

```javascript
import React, { useState } from 'react';

// Simple counter with useState
function Counter() {
    const [count, setCount] = useState(0);  // Initial state = 0
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>
            <button onClick={() => setCount(0)}>Reset</button>
        </div>
    );
}

// Multiple state variables
function UserForm() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [age, setAge] = useState(0);
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log({ name, email, age });
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input 
                value={name} 
                onChange={(e) => setName(e.target.value)}
                placeholder="Name"
            />
            <input 
                value={email} 
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                type="email"
            />
            <input 
                value={age} 
                onChange={(e) => setAge(Number(e.target.value))}
                placeholder="Age"
                type="number"
            />
            <button type="submit">Submit</button>
        </form>
    );
}

// State with objects
function UserProfile() {
    const [user, setUser] = useState({
        name: 'Alice',
        age: 30,
        preferences: { theme: 'dark', language: 'en' }
    });
    
    // Update nested state immutably
    const updateTheme = (newTheme) => {
        setUser(prevUser => ({
            ...prevUser,
            preferences: {
                ...prevUser.preferences,
                theme: newTheme
            }
        }));
    };
    
    return (
        <div>
            <h2>{user.name} - {user.age} years old</h2>
            <p>Theme: {user.preferences.theme}</p>
            <button onClick={() => updateTheme('light')}>Light Theme</button>
            <button onClick={() => updateTheme('dark')}>Dark Theme</button>
        </div>
    );
}
```

### React Hooks - useEffect

```javascript
import React, { useState, useEffect } from 'react';

// Fetch data on component mount
function UserList() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        // This runs after component mounts
        const fetchUsers = async () => {
            try {
                const response = await fetch('https://api.example.com/users');
                const data = await response.json();
                setUsers(data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        
        fetchUsers();
    }, []); // Empty dependency array = run once on mount
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    
    return (
        <ul>
            {users.map(user => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    );
}

// useEffect with dependencies
function SearchBar() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    
    useEffect(() => {
        // This runs every time 'query' changes
        if (query.length > 2) {
            const fetchResults = async () => {
                const response = await fetch(`/api/search?q=${query}`);
                const data = await response.json();
                setResults(data);
            };
            
            // Debounce: delay search until user stops typing
            const timeoutId = setTimeout(fetchResults, 300);
            
            // Cleanup function
            return () => clearTimeout(timeoutId);
        }
    }, [query]); // Runs when query changes
    
    return (
        <div>
            <input 
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search..."
            />
            <ul>
                {results.map(result => (
                    <li key={result.id}>{result.title}</li>
                ))}
            </ul>
        </div>
    );
}

// Cleanup with useEffect
function Timer() {
    const [seconds, setSeconds] = useState(0);
    
    useEffect(() => {
        const intervalId = setInterval(() => {
            setSeconds(s => s + 1);
        }, 1000);
        
        // Cleanup function - runs on unmount
        return () => clearInterval(intervalId);
    }, []);
    
    return <div>Seconds: {seconds}</div>;
}
```

### React Hooks - useContext

```javascript
import React, { createContext, useContext, useState } from 'react';

// Create context
const ThemeContext = createContext();
const UserContext = createContext();

// Theme provider component
function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    const toggleTheme = () => {
        setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
    };
    
    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

// Component using context
function ThemedButton() {
    const { theme, toggleTheme } = useContext(ThemeContext);
    
    return (
        <button 
            onClick={toggleTheme}
            style={{
                background: theme === 'light' ? '#fff' : '#333',
                color: theme === 'light' ? '#000' : '#fff'
            }}
        >
            Current theme: {theme}
        </button>
    );
}

// App with multiple contexts
function App() {
    const [user, setUser] = useState({ name: 'Alice', role: 'admin' });
    
    return (
        <UserContext.Provider value={{ user, setUser }}>
            <ThemeProvider>
                <div>
                    <ThemedButton />
                    <UserProfile />
                </div>
            </ThemeProvider>
        </UserContext.Provider>
    );
}

function UserProfile() {
    const { user } = useContext(UserContext);
    const { theme } = useContext(ThemeContext);
    
    return (
        <div style={{ background: theme === 'light' ? '#f0f0f0' : '#222' }}>
            <h2>{user.name}</h2>
            <p>Role: {user.role}</p>
        </div>
    );
}
```

### Custom Hooks

```javascript
import { useState, useEffect } from 'react';

// Custom hook for API fetching
function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                const result = await response.json();
                setData(result);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        
        fetchData();
    }, [url]);
    
    return { data, loading, error };
}

// Using custom hook
function UserList() {
    const { data: users, loading, error } = useFetch('/api/users');
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    
    return (
        <ul>
            {users.map(user => <li key={user.id}>{user.name}</li>)}
        </ul>
    );
}

// Custom hook for local storage
function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            return initialValue;
        }
    });
    
    const setStoredValue = (newValue) => {
        try {
            setValue(newValue);
            window.localStorage.setItem(key, JSON.stringify(newValue));
        } catch (error) {
            console.error(error);
        }
    };
    
    return [value, setStoredValue];
}

// Using local storage hook
function TodoApp() {
    const [todos, setTodos] = useLocalStorage('todos', []);
    
    const addTodo = (text) => {
        setTodos([...todos, { id: Date.now(), text, completed: false }]);
    };
    
    return (
        <div>
            {/* Todo list UI */}
        </div>
    );
}

// Custom hook for window size
function useWindowSize() {
    const [size, setSize] = useState({
        width: window.innerWidth,
        height: window.innerHeight
    });
    
    useEffect(() => {
        const handleResize = () => {
            setSize({
                width: window.innerWidth,
                height: window.innerHeight
            });
        };
        
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);
    
    return size;
}
```

### React Router

```javascript
import { BrowserRouter, Routes, Route, Link, useNavigate, useParams } from 'react-router-dom';

// Main app with routes
function App() {
    return (
        <BrowserRouter>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
                <Link to="/users">Users</Link>
            </nav>
            
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/users" element={<Users />} />
                <Route path="/users/:id" element={<UserDetail />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </BrowserRouter>
    );
}

// Component with URL parameters
function UserDetail() {
    const { id } = useParams();  // Get URL parameter
    const navigate = useNavigate();  // Programmatic navigation
    
    return (
        <div>
            <h2>User ID: {id}</h2>
            <button onClick={() => navigate('/users')}>Back to Users</button>
        </div>
    );
}

// Protected route example
function ProtectedRoute({ children }) {
    const isAuthenticated = useAuth();
    
    if (!isAuthenticated) {
        return <Navigate to="/login" />;
    }
    
    return children;
}
```

### State Management with Redux Toolkit

```javascript
// Redux Toolkit slice
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
    name: 'counter',
    initialState: { value: 0 },
    reducers: {
        increment: (state) => {
            state.value += 1;  // Redux Toolkit uses Immer for mutations
        },
        decrement: (state) => {
            state.value -= 1;
        },
        incrementByAmount: (state, action) => {
            state.value += action.payload;
        }
    }
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;

// Configure store
const store = configureStore({
    reducer: {
        counter: counterSlice.reducer
    }
});

// React component using Redux
import { useSelector, useDispatch } from 'react-redux';

function Counter() {
    const count = useSelector((state) => state.counter.value);
    const dispatch = useDispatch();
    
    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={() => dispatch(increment())}>+</button>
            <button onClick={() => dispatch(decrement())}>-</button>
            <button onClick={() => dispatch(incrementByAmount(5))}>+5</button>
        </div>
    );
}
```

---

## 17. �️ Angular Framework

**Angular is a comprehensive TypeScript-based framework for building scalable web applications, featuring dependency injection, RxJS observables, and a powerful CLI.** Unlike React (library), Angular is a full-fledged framework providing routing, forms, HTTP client, and more out of the box. Understanding components, services, directives, and RxJS is essential for Angular development.

### Angular Components

```typescript
// app.component.ts - Basic component
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'My Angular App';
  count = 0;
  users: User[] = [];
  
  ngOnInit() {
    // Lifecycle hook - runs after component initialization
    console.log('Component initialized');
    this.loadUsers();
  }
  
  increment() {
    this.count++;
  }
  
  decrement() {
    this.count--;
  }
  
  loadUsers() {
    this.users = [
      { id: 1, name: 'Alice', email: 'alice@example.com' },
      { id: 2, name: 'Bob', email: 'bob@example.com' }
    ];
  }
}

// app.component.html - Template
/*
<div class="container">
  <h1>{{ title }}</h1>
  
  <!-- Data binding -->
  <p>Count: {{ count }}</p>
  
  <!-- Event binding -->
  <button (click)="increment()">+</button>
  <button (click)="decrement()">-</button>
  
  <!-- Two-way binding -->
  <input [(ngModel)]="title" />
  
  <!-- Structural directives -->
  <div *ngIf="count > 0">Count is positive</div>
  
  <ul>
    <li *ngFor="let user of users; let i = index">
      {{ i + 1 }}. {{ user.name }} ({{ user.email }})
    </li>
  </ul>
</div>
*/

// Component with Input and Output
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-user-card',
  template: `
    <div class="card">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <button (click)="onDelete()">Delete</button>
    </div>
  `
})
export class UserCardComponent {
  @Input() user!: User;  // Input from parent
  @Output() delete = new EventEmitter<number>();  // Output to parent
  
  onDelete() {
    this.delete.emit(this.user.id);
  }
}

// Parent component usage:
// <app-user-card [user]="user" (delete)="handleDelete($event)"></app-user-card>
```

### Angular Services & Dependency Injection

```typescript
// user.service.ts - Service for API calls
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'  // Singleton service available app-wide
})
export class UserService {
  private apiUrl = 'https://api.example.com/users';
  
  constructor(private http: HttpClient) {}
  
  // GET all users
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl).pipe(
      retry(2),  // Retry failed requests twice
      catchError(this.handleError)
    );
  }
  
  // GET single user
  getUser(id: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`).pipe(
      catchError(this.handleError)
    );
  }
  
  // POST create user
  createUser(user: Partial<User>): Observable<User> {
    return this.http.post<User>(this.apiUrl, user, {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    }).pipe(
      catchError(this.handleError)
    );
  }
  
  // PUT update user
  updateUser(id: number, user: Partial<User>): Observable<User> {
    return this.http.put<User>(`${this.apiUrl}/${id}`, user).pipe(
      catchError(this.handleError)
    );
  }
  
  // DELETE user
  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`).pipe(
      catchError(this.handleError)
    );
  }
  
  private handleError(error: any) {
    console.error('API Error:', error);
    return throwError(() => new Error('Something went wrong'));
  }
}

// Using service in component
import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html'
})
export class UserListComponent implements OnInit {
  users: User[] = [];
  loading = false;
  error: string | null = null;
  
  constructor(private userService: UserService) {}  // Dependency injection
  
  ngOnInit() {
    this.loadUsers();
  }
  
  loadUsers() {
    this.loading = true;
    this.userService.getUsers().subscribe({
      next: (users) => {
        this.users = users;
        this.loading = false;
      },
      error: (error) => {
        this.error = error.message;
        this.loading = false;
      }
    });
  }
  
  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe({
      next: () => {
        this.users = this.users.filter(u => u.id !== id);
      },
      error: (error) => console.error('Delete failed:', error)
    });
  }
}
```

### RxJS Observables in Angular

```typescript
import { Component, OnInit } from '@angular/core';
import { Observable, Subject, BehaviorSubject, interval, fromEvent } from 'rxjs';
import { map, filter, debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-rxjs-demo',
  template: `
    <input #searchInput placeholder="Search users..." />
    <div *ngFor="let user of searchResults$ | async">
      {{ user.name }}
    </div>
  `
})
export class RxjsDemoComponent implements OnInit {
  // Observable that emits search results
  searchResults$!: Observable<User[]>;
  
  // Subject - manually emit values
  private searchSubject = new Subject<string>();
  
  // BehaviorSubject - stores current value
  private currentUser$ = new BehaviorSubject<User | null>(null);
  
  constructor(private userService: UserService) {}
  
  ngOnInit() {
    // Search with debounce
    this.searchResults$ = this.searchSubject.pipe(
      debounceTime(300),  // Wait 300ms after user stops typing
      distinctUntilChanged(),  // Only if value changed
      filter(query => query.length >= 2),  // Minimum 2 characters
      switchMap(query => this.userService.searchUsers(query))  // Switch to new search
    );
  }
  
  onSearchInput(event: Event) {
    const query = (event.target as HTMLInputElement).value;
    this.searchSubject.next(query);
  }
  
  // Observable operators examples
  demonstrateOperators() {
    // Map - transform values
    interval(1000).pipe(
      map(n => n * 2)
    ).subscribe(value => console.log(value));  // 0, 2, 4, 6...
    
    // Filter - only even numbers
    interval(1000).pipe(
      filter(n => n % 2 === 0)
    ).subscribe(value => console.log(value));  // 0, 2, 4, 6...
    
    // Combine multiple observables
    const clicks$ = fromEvent(document, 'click');
    const timer$ = interval(1000);
    
    // switchMap - cancel previous, switch to new
    clicks$.pipe(
      switchMap(() => timer$)
    ).subscribe(value => console.log(value));
  }
}

// Custom Observable
import { Observable } from 'rxjs';

function createCustomObservable(): Observable<number> {
  return new Observable(subscriber => {
    let count = 0;
    
    const interval = setInterval(() => {
      count++;
      subscriber.next(count);  // Emit value
      
      if (count === 5) {
        subscriber.complete();  // Complete observable
        clearInterval(interval);
      }
    }, 1000);
    
    // Cleanup function
    return () => {
      clearInterval(interval);
    };
  });
}

// Usage
createCustomObservable().subscribe({
  next: (value) => console.log('Value:', value),
  error: (error) => console.error('Error:', error),
  complete: () => console.log('Complete!')
});
```

### Angular Routing

```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { UserListComponent } from './users/user-list.component';
import { UserDetailComponent } from './users/user-detail.component';
import { LoginComponent } from './auth/login.component';
import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { 
    path: 'users', 
    component: UserListComponent,
    canActivate: [AuthGuard]  // Protected route
  },
  { 
    path: 'users/:id', 
    component: UserDetailComponent,
    canActivate: [AuthGuard]
  },
  { path: '**', redirectTo: '' }  // 404 redirect
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

// auth.guard.ts - Route guard
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}
  
  canActivate(): boolean {
    if (this.authService.isAuthenticated()) {
      return true;
    }
    
    this.router.navigate(['/login']);
    return false;
  }
}

// Navigation in component
import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-detail',
  template: '<div>User Detail</div>'
})
export class UserDetailComponent {
  constructor(
    private router: Router,
    private route: ActivatedRoute
  ) {
    // Get route parameters
    this.route.params.subscribe(params => {
      const userId = params['id'];
      console.log('User ID:', userId);
    });
    
    // Get query parameters
    this.route.queryParams.subscribe(params => {
      const page = params['page'];
      console.log('Page:', page);
    });
  }
  
  navigateToUsers() {
    this.router.navigate(['/users']);
  }
  
  navigateWithParams() {
    this.router.navigate(['/users', 123], { 
      queryParams: { page: 2 }
    });
  }
}
```

### Angular Forms

```typescript
// Reactive Forms (Recommended)
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormArray } from '@angular/forms';

@Component({
  selector: 'app-user-form',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <input formControlName="name" placeholder="Name" />
      <div *ngIf="name?.invalid && name?.touched">
        <span *ngIf="name?.errors?.['required']">Name is required</span>
        <span *ngIf="name?.errors?.['minlength']">Min 2 characters</span>
      </div>
      
      <input formControlName="email" placeholder="Email" type="email" />
      <div *ngIf="email?.invalid && email?.touched">
        <span *ngIf="email?.errors?.['required']">Email is required</span>
        <span *ngIf="email?.errors?.['email']">Invalid email</span>
      </div>
      
      <input formControlName="age" placeholder="Age" type="number" />
      
      <!-- Form Array - Dynamic fields -->
      <div formArrayName="hobbies">
        <div *ngFor="let hobby of hobbies.controls; let i = index">
          <input [formControlName]="i" placeholder="Hobby" />
          <button type="button" (click)="removeHobby(i)">Remove</button>
        </div>
      </div>
      <button type="button" (click)="addHobby()">Add Hobby</button>
      
      <button type="submit" [disabled]="userForm.invalid">Submit</button>
    </form>
  `
})
export class UserFormComponent implements OnInit {
  userForm!: FormGroup;
  
  constructor(private fb: FormBuilder) {}
  
  ngOnInit() {
    this.userForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      age: [0, [Validators.required, Validators.min(0), Validators.max(150)]],
      hobbies: this.fb.array([])
    });
  }
  
  get name() {
    return this.userForm.get('name');
  }
  
  get email() {
    return this.userForm.get('email');
  }
  
  get hobbies() {
    return this.userForm.get('hobbies') as FormArray;
  }
  
  addHobby() {
    this.hobbies.push(this.fb.control(''));
  }
  
  removeHobby(index: number) {
    this.hobbies.removeAt(index);
  }
  
  onSubmit() {
    if (this.userForm.valid) {
      console.log('Form value:', this.userForm.value);
    }
  }
}

// Template-driven Forms (Simpler)
import { Component } from '@angular/core';

@Component({
  selector: 'app-simple-form',
  template: `
    <form #userForm="ngForm" (ngSubmit)="onSubmit(userForm)">
      <input 
        name="name" 
        [(ngModel)]="user.name" 
        required 
        minlength="2"
        #name="ngModel"
      />
      <div *ngIf="name.invalid && name.touched">
        Name is required (min 2 chars)
      </div>
      
      <input 
        name="email" 
        [(ngModel)]="user.email" 
        required 
        email
        #email="ngModel"
      />
      <div *ngIf="email.invalid && email.touched">
        Valid email is required
      </div>
      
      <button type="submit" [disabled]="userForm.invalid">Submit</button>
    </form>
  `
})
export class SimpleFormComponent {
  user = { name: '', email: '' };
  
  onSubmit(form: any) {
    console.log('Form value:', form.value);
  }
}
```

### Angular Directives

```typescript
// Custom Attribute Directive
import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  @Input() appHighlight = 'yellow';  // Default color
  
  constructor(private el: ElementRef) {}
  
  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.appHighlight);
  }
  
  @HostListener('mouseleave') onMouseLeave() {
    this.highlight('');
  }
  
  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }
}

// Usage: <p appHighlight="lightblue">Hover over me!</p>

// Structural Directive
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appUnless]'
})
export class UnlessDirective {
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}
  
  @Input() set appUnless(condition: boolean) {
    if (!condition) {
      this.viewContainer.createEmbeddedView(this.templateRef);
    } else {
      this.viewContainer.clear();
    }
  }
}

// Usage: <div *appUnless="condition">Content shown when condition is false</div>
```

---

## 18. �🎨 Design Patterns in JavaScript

**Design patterns are reusable solutions to common programming problems, improving code organization and maintainability.** JavaScript supports various design patterns including Singleton, Factory, Observer, Module, and Strategy patterns. Understanding these patterns is essential for building scalable applications and acing technical interviews.

### Singleton Pattern

```javascript
// Singleton - Ensure only one instance exists
class Database {
    constructor() {
        if (Database.instance) {
            return Database.instance;
        }
        
        this.connection = null;
        this.isConnected = false;
        Database.instance = this;
    }
    
    connect() {
        if (!this.isConnected) {
            this.connection = 'Connected to database';
            this.isConnected = true;
            console.log('Database connected');
        }
        return this.connection;
    }
    
    disconnect() {
        this.isConnected = false;
        this.connection = null;
        console.log('Database disconnected');
    }
}

// Usage
const db1 = new Database();
const db2 = new Database();
console.log(db1 === db2);  // true - same instance

// Modern ES6 singleton
const Singleton = (() => {
    let instance;
    
    class SingletonClass {
        constructor() {
            if (instance) {
                return instance;
            }
            this.data = [];
            instance = this;
        }
        
        addData(item) {
            this.data.push(item);
        }
        
        getData() {
            return this.data;
        }
    }
    
    return SingletonClass;
})();
```

### Factory Pattern

```javascript
// Factory - Create objects without specifying exact class
class Car {
    constructor(options) {
        this.doors = options.doors || 4;
        this.state = options.state || 'new';
        this.color = options.color || 'white';
    }
}

class Truck {
    constructor(options) {
        this.doors = options.doors || 2;
        this.state = options.state || 'new';
        this.wheelSize = options.wheelSize || 'large';
    }
}

class VehicleFactory {
    createVehicle(type, options) {
        switch(type) {
            case 'car':
                return new Car(options);
            case 'truck':
                return new Truck(options);
            default:
                throw new Error('Unknown vehicle type');
        }
    }
}

// Usage
const factory = new VehicleFactory();
const myCar = factory.createVehicle('car', { color: 'blue', doors: 4 });
const myTruck = factory.createVehicle('truck', { wheelSize: 'extra-large' });

// Modern factory with classes
class UserFactory {
    static createUser(type, data) {
        const users = {
            admin: () => new AdminUser(data),
            regular: () => new RegularUser(data),
            guest: () => new GuestUser(data)
        };
        
        return users[type] ? users[type]() : null;
    }
}

class AdminUser {
    constructor(data) {
        this.name = data.name;
        this.role = 'admin';
        this.permissions = ['read', 'write', 'delete'];
    }
}

class RegularUser {
    constructor(data) {
        this.name = data.name;
        this.role = 'user';
        this.permissions = ['read', 'write'];
    }
}
```

### Observer Pattern (Pub/Sub)

```javascript
// Observer - Notify multiple objects about state changes
class EventEmitter {
    constructor() {
        this.events = {};
    }
    
    on(event, listener) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(listener);
    }
    
    emit(event, ...args) {
        if (this.events[event]) {
            this.events[event].forEach(listener => listener(...args));
        }
    }
    
    off(event, listenerToRemove) {
        if (this.events[event]) {
            this.events[event] = this.events[event].filter(
                listener => listener !== listenerToRemove
            );
        }
    }
}

// Usage
const emitter = new EventEmitter();

// Subscribe to events
emitter.on('userLoggedIn', (user) => {
    console.log(`Welcome ${user.name}!`);
});

emitter.on('userLoggedIn', (user) => {
    console.log(`Logging: User ${user.id} logged in`);
});

// Emit event
emitter.emit('userLoggedIn', { id: 1, name: 'Alice' });
// Output:
// Welcome Alice!
// Logging: User 1 logged in

// Real-world example: Shopping cart
class ShoppingCart {
    constructor() {
        this.items = [];
        this.observers = [];
    }
    
    subscribe(observer) {
        this.observers.push(observer);
    }
    
    notify(event, data) {
        this.observers.forEach(observer => observer.update(event, data));
    }
    
    addItem(item) {
        this.items.push(item);
        this.notify('itemAdded', { item, total: this.getTotal() });
    }
    
    removeItem(itemId) {
        this.items = this.items.filter(item => item.id !== itemId);
        this.notify('itemRemoved', { itemId, total: this.getTotal() });
    }
    
    getTotal() {
        return this.items.reduce((sum, item) => sum + item.price, 0);
    }
}

// Observers
class CartDisplay {
    update(event, data) {
        console.log(`Display: ${event}`, data);
    }
}

class CartAnalytics {
    update(event, data) {
        console.log(`Analytics: Tracking ${event}`, data);
    }
}

// Usage
const cart = new ShoppingCart();
cart.subscribe(new CartDisplay());
cart.subscribe(new CartAnalytics());

cart.addItem({ id: 1, name: 'Book', price: 20 });
```

### Module Pattern

```javascript
// Module - Encapsulate private data
const CounterModule = (() => {
    // Private variables
    let count = 0;
    
    // Private method
    function logCount() {
        console.log(`Current count: ${count}`);
    }
    
    // Public API
    return {
        increment() {
            count++;
            logCount();
        },
        decrement() {
            count--;
            logCount();
        },
        getCount() {
            return count;
        },
        reset() {
            count = 0;
            logCount();
        }
    };
})();

// Usage
CounterModule.increment();  // Current count: 1
CounterModule.increment();  // Current count: 2
console.log(CounterModule.getCount());  // 2
// console.log(CounterModule.count);  // undefined - private variable

// Modern ES6 module
class UserService {
    #users = [];  // Private field (ES2022)
    
    addUser(user) {
        this.#users.push(user);
        this.#notifyObservers();
    }
    
    #notifyObservers() {
        console.log('User list updated');
    }
    
    getUsers() {
        return [...this.#users];  // Return copy
    }
}
```

### Strategy Pattern

```javascript
// Strategy - Define family of algorithms, make them interchangeable
class PaymentStrategy {
    pay(amount) {
        throw new Error('pay() must be implemented');
    }
}

class CreditCardPayment extends PaymentStrategy {
    constructor(cardNumber) {
        super();
        this.cardNumber = cardNumber;
    }
    
    pay(amount) {
        console.log(`Paid $${amount} with credit card ${this.cardNumber}`);
        return { success: true, method: 'credit-card', amount };
    }
}

class PayPalPayment extends PaymentStrategy {
    constructor(email) {
        super();
        this.email = email;
    }
    
    pay(amount) {
        console.log(`Paid $${amount} via PayPal account ${this.email}`);
        return { success: true, method: 'paypal', amount };
    }
}

class CryptoPayment extends PaymentStrategy {
    constructor(walletAddress) {
        super();
        this.walletAddress = walletAddress;
    }
    
    pay(amount) {
        console.log(`Paid $${amount} via crypto wallet ${this.walletAddress}`);
        return { success: true, method: 'crypto', amount };
    }
}

class ShoppingCart {
    constructor(paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
        this.items = [];
    }
    
    setPaymentStrategy(strategy) {
        this.paymentStrategy = strategy;
    }
    
    checkout() {
        const amount = this.calculateTotal();
        return this.paymentStrategy.pay(amount);
    }
    
    calculateTotal() {
        return this.items.reduce((sum, item) => sum + item.price, 0);
    }
}

// Usage
const cart = new ShoppingCart(new CreditCardPayment('1234-5678-9012-3456'));
cart.items = [{ name: 'Book', price: 20 }, { name: 'Pen', price: 5 }];
cart.checkout();  // Paid $25 with credit card

// Switch payment strategy
cart.setPaymentStrategy(new PayPalPayment('user@example.com'));
cart.checkout();  // Paid $25 via PayPal
```

### Decorator Pattern

```javascript
// Decorator - Add functionality to objects dynamically
class Coffee {
    cost() {
        return 5;
    }
    
    description() {
        return 'Simple coffee';
    }
}

// Decorators
class MilkDecorator {
    constructor(coffee) {
        this.coffee = coffee;
    }
    
    cost() {
        return this.coffee.cost() + 2;
    }
    
    description() {
        return this.coffee.description() + ', milk';
    }
}

class SugarDecorator {
    constructor(coffee) {
        this.coffee = coffee;
    }
    
    cost() {
        return this.coffee.cost() + 1;
    }
    
    description() {
        return this.coffee.description() + ', sugar';
    }
}

class WhipDecorator {
    constructor(coffee) {
        this.coffee = coffee;
    }
    
    cost() {
        return this.coffee.cost() + 3;
    }
    
    description() {
        return this.coffee.description() + ', whipped cream';
    }
}

// Usage
let myCoffee = new Coffee();
console.log(myCoffee.description(), `$${myCoffee.cost()}`);  
// Simple coffee $5

myCoffee = new MilkDecorator(myCoffee);
myCoffee = new SugarDecorator(myCoffee);
myCoffee = new WhipDecorator(myCoffee);

console.log(myCoffee.description(), `$${myCoffee.cost()}`);  
// Simple coffee, milk, sugar, whipped cream $11

// Modern decorator with functions
function withLogging(fn) {
    return function(...args) {
        console.log(`Calling ${fn.name} with:`, args);
        const result = fn(...args);
        console.log(`Result:`, result);
        return result;
    };
}

function add(a, b) {
    return a + b;
}

const addWithLogging = withLogging(add);
addWithLogging(5, 3);
// Output:
// Calling add with: [5, 3]
// Result: 8
```

---

## 19. 🔒 Security Best Practices

**Web security is critical for protecting user data and preventing attacks like XSS, CSRF, and SQL injection.** Understanding common vulnerabilities and implementing proper security measures is essential for professional web development. Always validate input, sanitize output, use HTTPS, and follow the principle of least privilege.

### Cross-Site Scripting (XSS) Prevention

```javascript
// ❌ Vulnerable to XSS
function displayUserInput(input) {
    document.getElementById('output').innerHTML = input;  // DANGEROUS!
    // If input = "<img src=x onerror='alert(document.cookie)'>"
    // This will execute malicious JavaScript
}

// ✅ Prevent XSS by escaping HTML
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

function displayUserInputSafely(input) {
    const escaped = escapeHtml(input);
    document.getElementById('output').textContent = escaped;  // Safe
}

// Using DOMPurify library (recommended for production)
import DOMPurify from 'dompurify';

function displayRichContent(html) {
    const clean = DOMPurify.sanitize(html);
    document.getElementById('output').innerHTML = clean;
}

// Content Security Policy (CSP) header
// Set in your server or meta tag:
// <meta http-equiv="Content-Security-Policy" 
//       content="default-src 'self'; script-src 'self' https://trusted.com">
```

### CSRF Protection

```javascript
// Cross-Site Request Forgery prevention

// Generate CSRF token (server-side)
const crypto = require('crypto');

function generateCSRFToken() {
    return crypto.randomBytes(32).toString('hex');
}

// Store token in session
app.get('/form', (req, res) => {
    req.session.csrfToken = generateCSRFToken();
    res.render('form', { csrfToken: req.session.csrfToken });
});

// Verify token on submission
app.post('/submit', (req, res) => {
    const token = req.body.csrfToken;
    if (token !== req.session.csrfToken) {
        return res.status(403).json({ error: 'Invalid CSRF token' });
    }
    // Process form...
});

// Client-side: Include token in forms
// <form method="POST" action="/submit">
//     <input type="hidden" name="csrfToken" value="<%= csrfToken %>">
//     <!-- other fields -->
// </form>

// For AJAX requests
fetch('/api/data', {
    method: 'POST',
    headers: {
        'X-CSRF-Token': getCsrfToken(),  // Get from cookie or meta tag
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
});
```

### Authentication with JWT

```javascript
// JSON Web Token authentication
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const app = express();
const SECRET_KEY = process.env.JWT_SECRET || 'your-secret-key-change-this';

// Register user
app.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;
        
        // Validate input
        if (!username || !password || password.length < 8) {
            return res.status(400).json({ error: 'Invalid credentials' });
        }
        
        // Hash password
        const saltRounds = 10;
        const hashedPassword = await bcrypt.hash(password, saltRounds);
        
        // Save user to database (example)
        const user = await User.create({
            username,
            password: hashedPassword
        });
        
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Registration failed' });
    }
});

// Login user
app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        
        // Find user
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }
        
        // Verify password
        const isValid = await bcrypt.compare(password, user.password);
        if (!isValid) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }
        
        // Generate JWT
        const token = jwt.sign(
            { userId: user.id, username: user.username },
            SECRET_KEY,
            { expiresIn: '24h' }
        );
        
        res.json({ token, user: { id: user.id, username: user.username } });
    } catch (error) {
        res.status(500).json({ error: 'Login failed' });
    }
});

// Middleware to verify JWT
function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];  // Bearer TOKEN
    
    if (!token) {
        return res.status(401).json({ error: 'Access token required' });
    }
    
    jwt.verify(token, SECRET_KEY, (err, user) => {
        if (err) {
            return res.status(403).json({ error: 'Invalid token' });
        }
        req.user = user;
        next();
    });
}

// Protected route
app.get('/api/profile', authenticateToken, (req, res) => {
    res.json({ user: req.user });
});

// Refresh token implementation
app.post('/refresh', (req, res) => {
    const { refreshToken } = req.body;
    
    // Verify refresh token
    jwt.verify(refreshToken, REFRESH_SECRET, (err, user) => {
        if (err) {
            return res.status(403).json({ error: 'Invalid refresh token' });
        }
        
        // Generate new access token
        const accessToken = jwt.sign(
            { userId: user.userId, username: user.username },
            SECRET_KEY,
            { expiresIn: '15m' }
        );
        
        res.json({ accessToken });
    });
});
```

### Input Validation and Sanitization

```javascript
// Input validation with Joi
const Joi = require('joi');

const userSchema = Joi.object({
    username: Joi.string()
        .alphanum()
        .min(3)
        .max(30)
        .required(),
    email: Joi.string()
        .email()
        .required(),
    password: Joi.string()
        .pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/)
        .required()
        .messages({
            'string.pattern.base': 'Password must contain uppercase, lowercase, number, and special character'
        }),
    age: Joi.number()
        .integer()
        .min(18)
        .max(120)
});

app.post('/api/users', (req, res) => {
    // Validate input
    const { error, value } = userSchema.validate(req.body);
    
    if (error) {
        return res.status(400).json({ error: error.details[0].message });
    }
    
    // Process validated data
    createUser(value);
    res.status(201).json({ message: 'User created' });
});

// SQL Injection prevention (use parameterized queries)
// ❌ Vulnerable
const userId = req.params.id;
const query = `SELECT * FROM users WHERE id = ${userId}`;  // DANGEROUS!

// ✅ Safe - use parameterized queries
const query = 'SELECT * FROM users WHERE id = ?';
db.execute(query, [userId]);

// With MongoDB (use ORM/ODM like Mongoose)
// ❌ Vulnerable
User.find({ username: req.body.username });  // Can be exploited with $ne, $gt, etc.

// ✅ Safe - validate input type
const username = String(req.body.username);  // Ensure it's a string
User.find({ username: username });
```

### CORS Configuration

```javascript
// CORS (Cross-Origin Resource Sharing) setup
const express = require('express');
const cors = require('cors');

const app = express();

// Simple CORS - Allow all origins (NOT recommended for production)
app.use(cors());

// Configured CORS - Production recommended
const corsOptions = {
    origin: ['https://yourdomain.com', 'https://app.yourdomain.com'],
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization'],
    credentials: true,  // Allow cookies
    maxAge: 86400  // Cache preflight request for 24 hours
};

app.use(cors(corsOptions));

// Dynamic CORS based on request
app.use(cors((req, callback) => {
    const allowedOrigins = ['https://yourdomain.com', 'https://app.yourdomain.com'];
    const origin = req.header('Origin');
    
    if (allowedOrigins.includes(origin)) {
        callback(null, { origin: true });
    } else {
        callback(new Error('Not allowed by CORS'));
    }
}));

// Manual CORS headers
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'https://yourdomain.com');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.header('Access-Control-Allow-Credentials', 'true');
    
    // Handle preflight
    if (req.method === 'OPTIONS') {
        return res.sendStatus(200);
    }
    
    next();
});
```

### Security Headers

```javascript
// Set security headers with Helmet
const helmet = require('helmet');

app.use(helmet());

// Custom security headers
app.use(helmet({
    contentSecurityPolicy: {
        directives: {
            defaultSrc: ["'self'"],
            scriptSrc: ["'self'", "'unsafe-inline'", "https://trusted-cdn.com"],
            styleSrc: ["'self'", "'unsafe-inline'"],
            imgSrc: ["'self'", "data:", "https:"],
            connectSrc: ["'self'", "https://api.yourdomain.com"],
            fontSrc: ["'self'", "https:", "data:"],
            objectSrc: ["'none'"],
            mediaSrc: ["'self'"],
            frameSrc: ["'none'"]
        }
    },
    hsts: {
        maxAge: 31536000,  // 1 year
        includeSubDomains: true,
        preload: true
    }
}));

// Rate limiting to prevent brute force
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
    windowMs: 15 * 60 * 1000,  // 15 minutes
    max: 100,  // Limit each IP to 100 requests per windowMs
    message: 'Too many requests, please try again later'
});

app.use('/api/', limiter);

// Stricter limit for authentication endpoints
const authLimiter = rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 5,  // Only 5 login attempts per 15 minutes
    message: 'Too many login attempts, please try again later'
});

app.use('/api/login', authLimiter);
app.use('/api/register', authLimiter);
```

---

## 20. 🔌 WebSockets & Real-time Communication

**WebSockets provide full-duplex communication channels over a single TCP connection, enabling real-time data transfer between client and server.** Unlike HTTP polling, WebSockets maintain persistent connections for instant, bidirectional communication. This is essential for chat applications, live notifications, real-time dashboards, and multiplayer games.

### Native WebSocket API

```javascript
// Client-side WebSocket
const socket = new WebSocket('ws://localhost:8080');

// Connection opened
socket.addEventListener('open', (event) => {
    console.log('Connected to WebSocket server');
    socket.send(JSON.stringify({ type: 'greeting', message: 'Hello Server!' }));
});

// Listen for messages
socket.addEventListener('message', (event) => {
    console.log('Message from server:', event.data);
    const data = JSON.parse(event.data);
    
    if (data.type === 'notification') {
        showNotification(data.message);
    }
});

// Connection closed
socket.addEventListener('close', (event) => {
    console.log('Disconnected from server');
    // Attempt to reconnect
    setTimeout(() => connectWebSocket(), 1000);
});

// Handle errors
socket.addEventListener('error', (error) => {
    console.error('WebSocket error:', error);
});

// Send messages
function sendMessage(message) {
    if (socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ type: 'message', content: message }));
    } else {
        console.error('WebSocket is not open');
    }
}

// Close connection
function closeConnection() {
    socket.close(1000, 'Client closing connection');
}
```

### WebSocket Server with Node.js

```javascript
// Server-side WebSocket with 'ws' library
const WebSocket = require('ws');
const http = require('http');

const server = http.createServer();
const wss = new WebSocket.Server({ server });

// Store connected clients
const clients = new Set();

wss.on('connection', (ws, req) => {
    console.log('New client connected');
    clients.add(ws);
    
    // Send welcome message
    ws.send(JSON.stringify({
        type: 'welcome',
        message: 'Connected to server',
        clientCount: clients.size
    }));
    
    // Broadcast to all clients
    broadcastMessage({ type: 'userJoined', count: clients.size });
    
    // Handle messages from client
    ws.on('message', (data) => {
        try {
            const message = JSON.parse(data);
            console.log('Received:', message);
            
            // Echo message to all clients
            broadcastMessage({
                type: 'message',
                content: message.content,
                timestamp: new Date().toISOString()
            });
        } catch (error) {
            console.error('Error parsing message:', error);
        }
    });
    
    // Handle client disconnect
    ws.on('close', () => {
        console.log('Client disconnected');
        clients.delete(ws);
        broadcastMessage({ type: 'userLeft', count: clients.size });
    });
    
    // Handle errors
    ws.on('error', (error) => {
        console.error('WebSocket error:', error);
        clients.delete(ws);
    });
});

// Broadcast to all connected clients
function broadcastMessage(message) {
    const data = JSON.stringify(message);
    clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(data);
        }
    });
}

// Start server
server.listen(8080, () => {
    console.log('WebSocket server running on port 8080');
});
```

### Socket.IO (Advanced WebSocket Library)

```javascript
// Socket.IO Client
import io from 'socket.io-client';

const socket = io('http://localhost:3000', {
    auth: {
        token: 'your-auth-token'
    }
});

// Connect event
socket.on('connect', () => {
    console.log('Connected:', socket.id);
});

// Listen for events
socket.on('message', (data) => {
    console.log('Received message:', data);
});

socket.on('notification', (data) => {
    showNotification(data.title, data.body);
});

// Send events
socket.emit('sendMessage', { to: 'user123', message: 'Hello!' });

// Room-based communication
socket.emit('joinRoom', 'room-1');
socket.on('roomMessage', (data) => {
    console.log('Room message:', data);
});

// Disconnect
socket.on('disconnect', (reason) => {
    console.log('Disconnected:', reason);
    if (reason === 'io server disconnect') {
        // Manually reconnect
        socket.connect();
    }
});

// Socket.IO Server
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: {
        origin: 'http://localhost:3000',
        methods: ['GET', 'POST']
    }
});

// Middleware for authentication
io.use((socket, next) => {
    const token = socket.handshake.auth.token;
    if (isValidToken(token)) {
        socket.userId = getUserIdFromToken(token);
        next();
    } else {
        next(new Error('Authentication error'));
    }
});

// Connection handling
io.on('connection', (socket) => {
    console.log('User connected:', socket.userId);
    
    // Join user to their personal room
    socket.join(`user-${socket.userId}`);
    
    // Handle events
    socket.on('sendMessage', (data) => {
        // Send to specific user
        io.to(`user-${data.to}`).emit('message', {
            from: socket.userId,
            message: data.message,
            timestamp: new Date()
        });
    });
    
    // Room management
    socket.on('joinRoom', (roomId) => {
        socket.join(roomId);
        socket.to(roomId).emit('userJoined', {
            userId: socket.userId,
            roomId
        });
    });
    
    socket.on('leaveRoom', (roomId) => {
        socket.leave(roomId);
        socket.to(roomId).emit('userLeft', {
            userId: socket.userId,
            roomId
        });
    });
    
    // Broadcast to room
    socket.on('roomMessage', (data) => {
        io.to(data.roomId).emit('roomMessage', {
            from: socket.userId,
            message: data.message,
            timestamp: new Date()
        });
    });
    
    // Disconnect
    socket.on('disconnect', (reason) => {
        console.log('User disconnected:', socket.userId, reason);
    });
});

server.listen(3000, () => {
    console.log('Socket.IO server running on port 3000');
});
```

### Real-time Chat Application

```javascript
// Complete chat application with React + Socket.IO

// ChatApp.jsx
import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';

function ChatApp() {
    const [socket, setSocket] = useState(null);
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');
    const [username, setUsername] = useState('');
    const [isConnected, setIsConnected] = useState(false);
    const [onlineUsers, setOnlineUsers] = useState(0);
    const messagesEndRef = useRef(null);
    
    useEffect(() => {
        // Initialize socket connection
        const newSocket = io('http://localhost:3000', {
            auth: { username: username || 'Anonymous' }
        });
        
        newSocket.on('connect', () => {
            setIsConnected(true);
            console.log('Connected to chat server');
        });
        
        newSocket.on('disconnect', () => {
            setIsConnected(false);
            console.log('Disconnected from chat server');
        });
        
        newSocket.on('message', (message) => {
            setMessages(prev => [...prev, message]);
            scrollToBottom();
        });
        
        newSocket.on('userCount', (count) => {
            setOnlineUsers(count);
        });
        
        setSocket(newSocket);
        
        return () => newSocket.close();
    }, [username]);
    
    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };
    
    const sendMessage = (e) => {
        e.preventDefault();
        
        if (inputMessage.trim() && socket) {
            socket.emit('sendMessage', {
                text: inputMessage,
                timestamp: new Date()
            });
            setInputMessage('');
        }
    };
    
    return (
        <div className="chat-app">
            <div className="chat-header">
                <h2>Real-time Chat</h2>
                <div className="status">
                    <span className={isConnected ? 'connected' : 'disconnected'}>
                        {isConnected ? '● Online' : '○ Offline'}
                    </span>
                    <span>{onlineUsers} users online</span>
                </div>
            </div>
            
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className="message">
                        <span className="username">{msg.username}:</span>
                        <span className="text">{msg.text}</span>
                        <span className="time">
                            {new Date(msg.timestamp).toLocaleTimeString()}
                        </span>
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>
            
            <form onSubmit={sendMessage} className="input-form">
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    placeholder="Type a message..."
                    disabled={!isConnected}
                />
                <button type="submit" disabled={!isConnected || !inputMessage.trim()}>
                    Send
                </button>
            </form>
        </div>
    );
}

export default ChatApp;
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
| **Fundamentals** | Variables, data types, operators, hoisting |
| **Functions** | Arrow functions, closures, higher-order functions |
| **Objects** | Prototypes, classes, inheritance, SOLID principles |
| **Async** | Promises, async/await, event loop, async iteration |
| **DOM** | Selectors, events, manipulation, event delegation |
| **ES6+** | Destructuring, spread/rest, modules, template literals |
| **Functional** | Map, filter, reduce, immutability, composition |
| **Advanced** | Generators, symbols, weak collections, proxies |
| **Testing** | Jest, mocking, TDD, test coverage |
| **Performance** | Debouncing, throttling, memory management, lazy loading |
| **Node.js** | Express.js, middleware, REST APIs, Worker Threads, Streams |
| **⚛️ React** | Hooks, Context, State Management, Custom Hooks, Router, Redux |
| **🅰️ Angular** | Components, Services, RxJS, Routing, Forms, Directives |
| **🎨 Patterns** | Singleton, Factory, Observer, Module, Strategy, Decorator |
| **🔒 Security** | XSS/CSRF prevention, JWT, Input validation, CORS, Rate limiting |
| **🔌 Real-time** | WebSockets, Socket.IO, bidirectional communication |
| **Ecosystem** | npm, Webpack, Vite, Babel, ESLint, build tools |

---

> **🎉 Congratulations!** You now have a complete JavaScript reference covering all concepts from beginner to expert level. This guide prepares you for modern web development, interviews, and advanced JavaScript projects.

**Ready for the next level?** Consider learning TypeScript, React/Vue/Angular, or diving deeper into Node.js backend development!