#!/usr/bin/env node
/**
 * 🟨 JAVASCRIPT MASTERY GUIDE - COMPLETE REFERENCE FOR INTERVIEWS & MASTERY
 * ========================================================================
 * 
 * This comprehensive guide covers all JavaScript concepts from basics to advanced topics.
 * Perfect for interview preparation, skill assessment, and continuous learning.
 * 
 * Author: Tech Mastery Notebooks
 * Date: November 2025
 * Level: Beginner to Expert
 */

// ===============================================================
// 1. JAVASCRIPT FUNDAMENTALS - BUILDING BLOCKS
// ===============================================================
console.log("🔥 JAVASCRIPT FUNDAMENTALS");
console.log("=".repeat(50));

// Variables and Data Types
console.log("\n📊 VARIABLES AND DATA TYPES:");

// Variable declarations
var oldStyle = "var keyword (function-scoped)";
let modernBlock = "let keyword (block-scoped)";
const constant = "const keyword (immutable reference)";

console.log(`var: ${oldStyle}`);
console.log(`let: ${modernBlock}`);
console.log(`const: ${constant}`);

// Data types
const dataTypes = {
    // Primitive types
    number: 42,
    string: "Hello, JavaScript!",
    boolean: true,
    undefined: undefined,
    nullValue: null,
    symbol: Symbol('id'),
    bigint: BigInt(9007199254740991),
    
    // Reference types
    object: { name: "Alice", age: 30 },
    array: [1, 2, 3, 4, 5],
    function: function() { return "I'm a function!"; }
};

console.log("\nData Types Demo:");
for (const [type, value] of Object.entries(dataTypes)) {
    console.log(`${type}: ${value} (typeof: ${typeof value})`);
}

// Type checking and conversion
console.log("\n🔄 TYPE CONVERSION:");
console.log(`String to Number: "123" -> ${Number("123")}`);
console.log(`Number to String: 123 -> "${String(123)}"`);
console.log(`Boolean conversion: 0 -> ${Boolean(0)}, 1 -> ${Boolean(1)}`);
console.log(`Implicit conversion: "5" + 3 = ${("5" + 3)}`);
console.log(`Explicit conversion: +"5" + 3 = ${(+"5" + 3)}`);

// String operations
console.log("\n🔤 STRING OPERATIONS:");
const text = "JavaScript Programming";
console.log(`Original: "${text}"`);
console.log(`Length: ${text.length}`);
console.log(`Uppercase: "${text.toUpperCase()}"`);
console.log(`Lowercase: "${text.toLowerCase()}"`);
console.log(`Split: [${text.split(" ")}]`);
console.log(`Replace: "${text.replace("JavaScript", "Advanced JavaScript")}"`);
console.log(`Index of 'Programming': ${text.indexOf("Programming")}`);
console.log(`Starts with 'JavaScript': ${text.startsWith("JavaScript")}`);

// Template literals
const name = "Bob";
const age = 25;
console.log(`\nTemplate literal: Hello, ${name}! You are ${age} years old.`);
console.log(`Multiline string:
First line
Second line
Third line`);

// ===============================================================
// 2. DATA STRUCTURES - ARRAYS AND OBJECTS
// ===============================================================
console.log("\n\n🔥 DATA STRUCTURES");
console.log("=".repeat(50));

// Arrays
console.log("\n📋 ARRAYS:");
const fruits = ["apple", "banana", "cherry", "date"];
console.log(`Original array: [${fruits}]`);
console.log(`First item: ${fruits[0]}`);
console.log(`Last item: ${fruits[fruits.length - 1]}`);
console.log(`Slice [1:3]: [${fruits.slice(1, 3)}]`);

// Array methods
const numbers = [1, 2, 3, 4, 5];
console.log(`\nArray methods demo:`);
console.log(`Original: [${numbers}]`);
console.log(`map (x2): [${numbers.map(x => x * 2)}]`);
console.log(`filter (even): [${numbers.filter(x => x % 2 === 0)}]`);
console.log(`reduce (sum): ${numbers.reduce((sum, x) => sum + x, 0)}`);
console.log(`find (>3): ${numbers.find(x => x > 3)}`);
console.log(`some (>4): ${numbers.some(x => x > 4)}`);
console.log(`every (<10): ${numbers.every(x => x < 10)}`);

// Array destructuring
const [first, second, ...rest] = numbers;
console.log(`Destructuring: first=${first}, second=${second}, rest=[${rest}]`);

// Objects
console.log("\n📚 OBJECTS:");
const student = {
    name: "Charlie",
    age: 22,
    major: "Computer Science",
    gpa: 3.8,
    courses: ["Data Structures", "Algorithms", "Database"],
    
    // Method
    introduce() {
        return `Hi, I'm ${this.name}, studying ${this.major}`;
    },
    
    // Getter
    get status() {
        return this.gpa >= 3.5 ? "Honor Roll" : "Regular";
    },
    
    // Setter
    set newGrade(grade) {
        // Simplified - just update GPA
        this.gpa = (this.gpa + grade) / 2;
    }
};

console.log(`Student: ${JSON.stringify(student, null, 2)}`);
console.log(`Introduction: ${student.introduce()}`);
console.log(`Status: ${student.status}`);

// Object methods
console.log(`\nObject methods:`);
console.log(`Keys: [${Object.keys(student)}]`);
console.log(`Values: [${Object.values(student).slice(0, 4)}...]`); // Limit output
console.log(`Entries: ${Object.entries(student).slice(0, 2).map(([k, v]) => `${k}: ${v}`)}`);

// Object destructuring
const { name: studentName, age: studentAge, major } = student;
console.log(`Destructuring: name=${studentName}, age=${studentAge}, major=${major}`);

// ===============================================================
// 3. FUNCTIONS - REUSABLE CODE BLOCKS
// ===============================================================
console.log("\n\n🔥 FUNCTIONS");
console.log("=".repeat(50));

// Function declarations and expressions
console.log("\n⚡ FUNCTION TYPES:");

// Function declaration
function greet(name, greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Function expression
const multiply = function(a, b) {
    return a * b;
};

// Arrow function
const add = (a, b) => a + b;
const square = x => x * x;
const sayHello = () => "Hello from arrow function!";

console.log(`Function declaration: ${greet("Alice")}`);
console.log(`Function expression: ${multiply(4, 5)}`);
console.log(`Arrow function: ${add(3, 7)}`);
console.log(`Single param arrow: ${square(6)}`);
console.log(`No param arrow: ${sayHello()}`);

// Higher-order functions
console.log("\n🔗 HIGHER-ORDER FUNCTIONS:");

function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(`Double 5: ${double(5)}`);
console.log(`Triple 4: ${triple(4)}`);

// Callback functions
function processArray(arr, callback) {
    return arr.map(callback);
}

const nums = [1, 2, 3, 4, 5];
console.log(`Process with double: [${processArray(nums, double)}]`);
console.log(`Process with square: [${processArray(nums, square)}]`);

// Closures
console.log("\n🔒 CLOSURES:");

function createCounter() {
    let count = 0;
    return {
        increment: () => ++count,
        decrement: () => --count,
        getValue: () => count
    };
}

const counter = createCounter();
console.log(`Initial value: ${counter.getValue()}`);
console.log(`After increment: ${counter.increment()}`);
console.log(`After increment: ${counter.increment()}`);
console.log(`After decrement: ${counter.decrement()}`);

// ===============================================================
// 4. ASYNCHRONOUS JAVASCRIPT - CALLBACKS, PROMISES, ASYNC/AWAIT
// ===============================================================
console.log("\n\n🔥 ASYNCHRONOUS JAVASCRIPT");
console.log("=".repeat(50));

// Callbacks
console.log("\n📞 CALLBACKS:");

function simulateAsyncOperation(callback) {
    setTimeout(() => {
        const result = Math.random() > 0.5 ? "Success!" : "Error!";
        callback(result);
    }, 100);
}

// Promises
console.log("\n🤝 PROMISES:");

function createPromise(shouldSucceed = true) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (shouldSucceed) {
                resolve("Promise resolved successfully!");
            } else {
                reject(new Error("Promise rejected!"));
            }
        }, 100);
    });
}

// Promise chaining
createPromise(true)
    .then(result => {
        console.log(`Promise result: ${result}`);
        return "Modified result";
    })
    .then(modifiedResult => {
        console.log(`Modified: ${modifiedResult}`);
    })
    .catch(error => {
        console.error(`Promise error: ${error.message}`);
    });

// Async/Await
console.log("\n⏰ ASYNC/AWAIT:");

async function asyncFunction() {
    try {
        console.log("Starting async operation...");
        const result1 = await createPromise(true);
        console.log(`First result: ${result1}`);
        
        const result2 = await createPromise(true);
        console.log(`Second result: ${result2}`);
        
        return "All operations completed!";
    } catch (error) {
        console.error(`Async error: ${error.message}`);
        throw error;
    }
}

// Promise.all and Promise.race
async function promiseCombinations() {
    console.log("\n🏁 PROMISE COMBINATIONS:");
    
    const promises = [
        createPromise(true),
        createPromise(true),
        createPromise(true)
    ];
    
    try {
        // Promise.all - wait for all
        const allResults = await Promise.all(promises);
        console.log(`Promise.all results: [${allResults}]`);
        
        // Promise.race - first to complete
        const firstResult = await Promise.race(promises);
        console.log(`Promise.race result: ${firstResult}`);
        
        // Promise.allSettled - all settled (success or failure)
        const settledResults = await Promise.allSettled(promises);
        console.log(`Promise.allSettled: ${settledResults.length} promises settled`);
    } catch (error) {
        console.error(`Promise combination error: ${error.message}`);
    }
}

// ===============================================================
// 5. OBJECT-ORIENTED PROGRAMMING - CLASSES AND PROTOTYPES
// ===============================================================
console.log("\n\n🔥 OBJECT-ORIENTED PROGRAMMING");
console.log("=".repeat(50));

// ES6 Classes
console.log("\n👤 CLASSES:");

class Person {
    // Static property
    static species = "Homo sapiens";
    
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this._id = Math.random().toString(36).substr(2, 9); // Private-ish
    }
    
    // Instance method
    introduce() {
        return `Hi, I'm ${this.name} and I'm ${this.age} years old.`;
    }
    
    // Getter
    get isAdult() {
        return this.age >= 18;
    }
    
    // Setter
    set age(newAge) {
        if (newAge >= 0 && newAge <= 150) {
            this._age = newAge;
        } else {
            throw new Error("Invalid age");
        }
    }
    
    get age() {
        return this._age;
    }
    
    // Static method
    static getSpecies() {
        return Person.species;
    }
    
    // Method with default parameter
    greet(greeting = "Hello") {
        return `${greeting}, ${this.name}!`;
    }
}

const alice = new Person("Alice", 25);
const bob = new Person("Bob", 17);

console.log(`Alice: ${alice.introduce()}`);
console.log(`Bob is adult: ${bob.isAdult}`);
console.log(`Species: ${Person.getSpecies()}`);
console.log(`Alice greeting: ${alice.greet("Hi")}`);

// Inheritance
console.log("\n🎓 INHERITANCE:");

class Student extends Person {
    constructor(name, age, studentId, major) {
        super(name, age); // Call parent constructor
        this.studentId = studentId;
        this.major = major;
        this.grades = [];
    }
    
    addGrade(grade) {
        this.grades.push(grade);
    }
    
    getGPA() {
        if (this.grades.length === 0) return 0;
        return this.grades.reduce((sum, grade) => sum + grade, 0) / this.grades.length;
    }
    
    // Override parent method
    introduce() {
        const baseIntro = super.introduce();
        return `${baseIntro} I'm studying ${this.major}.`;
    }
    
    // Static method
    static createHonorStudent(name, age, studentId, major) {
        const student = new Student(name, age, studentId, major);
        student.addGrade(4.0);
        return student;
    }
}

const charlie = new Student("Charlie", 20, "S12345", "Computer Science");
charlie.addGrade(3.7);
charlie.addGrade(3.9);
charlie.addGrade(3.5);

console.log(`Charlie: ${charlie.introduce()}`);
console.log(`Charlie's GPA: ${charlie.getGPA().toFixed(2)}`);

// Prototypes (alternative to classes)
console.log("\n🔗 PROTOTYPES:");

function Animal(name, species) {
    this.name = name;
    this.species = species;
}

Animal.prototype.speak = function() {
    return `${this.name} makes a sound.`;
};

Animal.prototype.getInfo = function() {
    return `${this.name} is a ${this.species}`;
};

function Dog(name, breed) {
    Animal.call(this, name, "Dog"); // Call parent constructor
    this.breed = breed;
}

// Set up inheritance
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Override method
Dog.prototype.speak = function() {
    return `${this.name} barks!`;
};

Dog.prototype.getBreed = function() {
    return this.breed;
};

const rover = new Dog("Rover", "Golden Retriever");
console.log(`Dog info: ${rover.getInfo()}`);
console.log(`Dog sound: ${rover.speak()}`);
console.log(`Dog breed: ${rover.getBreed()}`);

// ===============================================================
// 6. ADVANCED FEATURES - DESTRUCTURING, SPREAD, REST
// ===============================================================
console.log("\n\n🔥 ADVANCED FEATURES");
console.log("=".repeat(50));

// Destructuring
console.log("\n📦 DESTRUCTURING:");

// Array destructuring
const colors = ["red", "green", "blue", "yellow", "purple"];
const [primary1, primary2, primary3, ...secondary] = colors;
console.log(`Primary colors: ${primary1}, ${primary2}, ${primary3}`);
console.log(`Secondary colors: [${secondary}]`);

// Object destructuring
const user = {
    id: 1,
    username: "johndoe",
    email: "john@example.com",
    profile: {
        firstName: "John",
        lastName: "Doe",
        avatar: "avatar.jpg"
    }
};

const { 
    username, 
    email, 
    profile: { firstName, lastName },
    age: userAge = 25 // Default value
} = user;

console.log(`User: ${username} (${firstName} ${lastName})`);
console.log(`Email: ${email}, Age: ${userAge}`);

// Spread operator
console.log("\n📤 SPREAD OPERATOR:");

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(`Combined arrays: [${combined}]`);

const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const mergedObj = { ...obj1, ...obj2, e: 5 };
console.log(`Merged object: ${JSON.stringify(mergedObj)}`);

// Rest parameters
console.log("\n📥 REST PARAMETERS:");

function sumAll(first, second, ...remaining) {
    console.log(`First: ${first}, Second: ${second}`);
    console.log(`Remaining: [${remaining}]`);
    return [first, second, ...remaining].reduce((sum, num) => sum + num, 0);
}

const total = sumAll(1, 2, 3, 4, 5, 6);
console.log(`Total sum: ${total}`);

// ===============================================================
// 7. ERROR HANDLING AND DEBUGGING
// ===============================================================
console.log("\n\n🔥 ERROR HANDLING");
console.log("=".repeat(50));

// Basic error handling
console.log("\n⚠️ EXCEPTION HANDLING:");

function safeDivide(a, b) {
    try {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new TypeError("Arguments must be numbers");
        }
        if (b === 0) {
            throw new Error("Division by zero is not allowed");
        }
        return a / b;
    } catch (error) {
        console.error(`Error in safeDivide: ${error.message}`);
        return null;
    } finally {
        console.log("Division operation completed");
    }
}

console.log(`10 / 2 = ${safeDivide(10, 2)}`);
console.log(`10 / 0 = ${safeDivide(10, 0)}`);
console.log(`"10" / 2 = ${safeDivide("10", 2)}`);

// Custom errors
console.log("\n🔧 CUSTOM ERRORS:");

class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

function validateUser(userData) {
    if (!userData.name) {
        throw new ValidationError("Name is required", "name");
    }
    if (!userData.email || !userData.email.includes("@")) {
        throw new ValidationError("Valid email is required", "email");
    }
    if (userData.age < 0) {
        throw new ValidationError("Age must be positive", "age");
    }
    return true;
}

try {
    validateUser({ name: "John", email: "invalid-email", age: 25 });
} catch (error) {
    if (error instanceof ValidationError) {
        console.log(`Validation error in ${error.field}: ${error.message}`);
    } else {
        console.log(`Unexpected error: ${error.message}`);
    }
}

// ===============================================================
// 8. MODULES AND IMPORTS
// ===============================================================
console.log("\n\n🔥 MODULES AND IMPORTS");
console.log("=".repeat(50));

// Module concepts (syntax examples)
console.log("\n📦 MODULE CONCEPTS:");

console.log("Exporting (ES6 modules):");
console.log("  // math.js");
console.log("  export const PI = 3.14159;");
console.log("  export function add(a, b) { return a + b; }");
console.log("  export default function multiply(a, b) { return a * b; }");

console.log("\nImporting:");
console.log("  import multiply, { PI, add } from './math.js';");
console.log("  import * as MathUtils from './math.js';");

console.log("\nCommonJS (Node.js):");
console.log("  // Exporting");
console.log("  module.exports = { add, multiply };");
console.log("  // Importing");
console.log("  const { add, multiply } = require('./math');");

// ===============================================================
// 9. DOM MANIPULATION AND EVENTS
// ===============================================================
console.log("\n\n🔥 DOM MANIPULATION");
console.log("=".repeat(50));

// DOM concepts (browser environment)
console.log("\n🌐 DOM CONCEPTS:");

const domConcepts = `
// Selecting elements
const element = document.getElementById('myId');
const elements = document.querySelectorAll('.myClass');
const firstElement = document.querySelector('div.container');

// Creating elements
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello, World!';
newDiv.className = 'my-class';

// Modifying elements
element.innerHTML = '<strong>Bold text</strong>';
element.textContent = 'Plain text';
element.style.color = 'blue';
element.setAttribute('data-value', '123');

// Adding to DOM
document.body.appendChild(newDiv);
element.insertBefore(newDiv, element.firstChild);

// Event handling
element.addEventListener('click', function(event) {
    console.log('Element clicked!');
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Stop event bubbling
});

// Event delegation
document.addEventListener('click', function(event) {
    if (event.target.matches('.button')) {
        console.log('Button clicked!');
    }
});
`;

console.log(domConcepts);

// ===============================================================
// 10. ALGORITHMS AND DATA STRUCTURES
// ===============================================================
console.log("\n\n🔥 ALGORITHMS AND DATA STRUCTURES");
console.log("=".repeat(50));

// Sorting algorithms
console.log("\n🔄 SORTING ALGORITHMS:");

function bubbleSort(arr) {
    const n = arr.length;
    const result = [...arr]; // Don't modify original
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (result[j] > result[j + 1]) {
                [result[j], result[j + 1]] = [result[j + 1], result[j]]; // Swap
            }
        }
    }
    return result;
}

function quickSort(arr) {
    if (arr.length <= 1) return arr;
    
    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(x => x < pivot);
    const middle = arr.filter(x => x === pivot);
    const right = arr.filter(x => x > pivot);
    
    return [...quickSort(left), ...middle, ...quickSort(right)];
}

const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
console.log(`Original: [${unsortedArray}]`);
console.log(`Bubble sort: [${bubbleSort(unsortedArray)}]`);
console.log(`Quick sort: [${quickSort(unsortedArray)}]`);

// Search algorithms
console.log("\n🔍 SEARCH ALGORITHMS:");

function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

const sortedArray = [1, 3, 5, 7, 9, 11, 13, 15];
const target = 7;
const index = binarySearch(sortedArray, target);
console.log(`Binary search for ${target} in [${sortedArray}]: index ${index}`);

// Data structures
console.log("\n📊 DATA STRUCTURES:");

// Stack implementation
class Stack {
    constructor() {
        this.items = [];
    }
    
    push(item) {
        this.items.push(item);
    }
    
    pop() {
        return this.items.pop();
    }
    
    peek() {
        return this.items[this.items.length - 1];
    }
    
    isEmpty() {
        return this.items.length === 0;
    }
    
    size() {
        return this.items.length;
    }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(`Stack peek: ${stack.peek()}`);
console.log(`Stack pop: ${stack.pop()}`);
console.log(`Stack size: ${stack.size()}`);

// Queue implementation
class Queue {
    constructor() {
        this.items = [];
    }
    
    enqueue(item) {
        this.items.push(item);
    }
    
    dequeue() {
        return this.items.shift();
    }
    
    front() {
        return this.items[0];
    }
    
    isEmpty() {
        return this.items.length === 0;
    }
    
    size() {
        return this.items.length;
    }
}

const queue = new Queue();
queue.enqueue("first");
queue.enqueue("second");
queue.enqueue("third");
console.log(`Queue front: ${queue.front()}`);
console.log(`Queue dequeue: ${queue.dequeue()}`);
console.log(`Queue size: ${queue.size()}`);

// ===============================================================
// 11. DESIGN PATTERNS
// ===============================================================
console.log("\n\n🔥 DESIGN PATTERNS");
console.log("=".repeat(50));

// Singleton pattern
console.log("\n🏗️ SINGLETON PATTERN:");

class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        
        this.data = [];
        Singleton.instance = this;
    }
    
    addData(item) {
        this.data.push(item);
    }
    
    getData() {
        return this.data;
    }
}

const singleton1 = new Singleton();
const singleton2 = new Singleton();
singleton1.addData("Item 1");
singleton2.addData("Item 2");

console.log(`Singleton1 data: [${singleton1.getData()}]`);
console.log(`Singleton2 data: [${singleton2.getData()}]`);
console.log(`Same instance: ${singleton1 === singleton2}`);

// Observer pattern
console.log("\n👀 OBSERVER PATTERN:");

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
    
    emit(event, data) {
        if (this.events[event]) {
            this.events[event].forEach(listener => listener(data));
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

const emitter = new EventEmitter();

const listener1 = (data) => console.log(`Listener 1: ${data}`);
const listener2 = (data) => console.log(`Listener 2: ${data}`);

emitter.on('test', listener1);
emitter.on('test', listener2);
emitter.emit('test', 'Hello from observer pattern!');

// Factory pattern
console.log("\n🏭 FACTORY PATTERN:");

class VehicleFactory {
    static createVehicle(type, model) {
        switch (type.toLowerCase()) {
            case 'car':
                return new Car(model);
            case 'motorcycle':
                return new Motorcycle(model);
            default:
                throw new Error(`Unknown vehicle type: ${type}`);
        }
    }
}

class Vehicle {
    constructor(model) {
        this.model = model;
    }
    
    start() {
        return `${this.model} started`;
    }
}

class Car extends Vehicle {
    start() {
        return `Car ${this.model} engine started`;
    }
}

class Motorcycle extends Vehicle {
    start() {
        return `Motorcycle ${this.model} engine revved`;
    }
}

const car = VehicleFactory.createVehicle('car', 'Tesla Model 3');
const bike = VehicleFactory.createVehicle('motorcycle', 'Harley Davidson');

console.log(car.start());
console.log(bike.start());

// ===============================================================
// 12. PERFORMANCE AND OPTIMIZATION
// ===============================================================
console.log("\n\n🔥 PERFORMANCE AND OPTIMIZATION");
console.log("=".repeat(50));

// Debouncing
console.log("\n⏱️ DEBOUNCING:");

function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

const debouncedLog = debounce((message) => {
    console.log(`Debounced: ${message}`);
}, 300);

// Throttling
console.log("\n🚦 THROTTLING:");

function throttle(func, delay) {
    let lastCall = 0;
    return function(...args) {
        const now = Date.now();
        if (now - lastCall >= delay) {
            lastCall = now;
            func.apply(this, args);
        }
    };
}

const throttledLog = throttle((message) => {
    console.log(`Throttled: ${message}`);
}, 300);

// Memoization
console.log("\n💾 MEMOIZATION:");

function memoize(func) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            console.log(`Cache hit for ${key}`);
            return cache.get(key);
        }
        const result = func.apply(this, args);
        cache.set(key, result);
        console.log(`Cache miss for ${key}, result cached`);
        return result;
    };
}

const memoizedFibonacci = memoize(function fibonacci(n) {
    if (n < 2) return n;
    return memoizedFibonacci(n - 1) + memoizedFibonacci(n - 2);
});

console.log(`Fibonacci(10): ${memoizedFibonacci(10)}`);
console.log(`Fibonacci(10) again: ${memoizedFibonacci(10)}`);

// ===============================================================
// JAVASCRIPT MASTERY SUMMARY
// ===============================================================
console.log("\n" + "=".repeat(60));
console.log("🏆 JAVASCRIPT MASTERY SUMMARY");
console.log("=".repeat(60));

const jsConcepts = {
    "Fundamentals": [
        "Variables (var, let, const) and scoping",
        "Data types and type conversion",
        "String operations and template literals"
    ],
    "Data Structures": [
        "Arrays and array methods (map, filter, reduce)",
        "Objects and object destructuring",
        "Spread operator and rest parameters"
    ],
    "Functions": [
        "Function declarations, expressions, and arrows",
        "Higher-order functions and callbacks",
        "Closures and lexical scoping"
    ],
    "Async Programming": [
        "Callbacks and callback hell",
        "Promises and promise chaining",
        "Async/await and error handling"
    ],
    "OOP": [
        "ES6 classes and inheritance",
        "Prototypes and prototype chain",
        "Static methods and getters/setters"
    ],
    "Advanced Features": [
        "Destructuring assignment",
        "Modules (ES6 and CommonJS)",
        "Error handling and custom errors"
    ],
    "DOM & Browser": [
        "DOM manipulation and selection",
        "Event handling and delegation",
        "Browser APIs and local storage"
    ],
    "Algorithms": [
        "Sorting algorithms (bubble, quick)",
        "Search algorithms (binary search)",
        "Data structures (stack, queue)"
    ],
    "Design Patterns": [
        "Singleton and Factory patterns",
        "Observer pattern and event emitters",
        "Module pattern and namespacing"
    ],
    "Performance": [
        "Debouncing and throttling",
        "Memoization and caching",
        "Memory management and optimization"
    ]
};

console.log("\n📚 TOPICS MASTERED:");
for (const [category, topics] of Object.entries(jsConcepts)) {
    console.log(`\n✅ ${category}:`);
    topics.forEach(topic => console.log(`    - ${topic}`));
}

console.log("\n💼 INTERVIEW READINESS:");
const interviewTopics = [
    "ES6+ features and modern JavaScript",
    "Asynchronous programming patterns",
    "Prototypal inheritance vs class-based",
    "Event loop and concurrency model",
    "Scope, hoisting, and closures",
    "Design patterns implementation",
    "Algorithm and data structure coding",
    "Performance optimization techniques",
    "Error handling and debugging strategies"
];

interviewTopics.forEach(topic => console.log(`🎯 ${topic}`));

console.log("\n🚀 NEXT STEPS:");
// ===============================================================
// 11. NODE.JS AND BACKEND DEVELOPMENT
// ===============================================================
console.log("\n\n🔥 NODE.JS BACKEND DEVELOPMENT");
console.log("=".repeat(50));

// Express.js server setup
console.log("\n🌐 EXPRESS.JS SERVER:");

const expressServerCode = `
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

// Routes
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

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
    console.log(\`Server running on port \${PORT}\`);
});
`;

console.log("Express.js server setup:");
console.log(expressServerCode);

// File system operations
console.log("\n📁 FILE SYSTEM OPERATIONS:");

const fileSystemCode = `
const fs = require('fs').promises;
const path = require('path');

class FileManager {
    async readFile(filePath) {
        try {
            const data = await fs.readFile(filePath, 'utf8');
            return data;
        } catch (error) {
            throw new Error(\`Failed to read file: \${error.message}\`);
        }
    }
    
    async writeFile(filePath, data) {
        try {
            await fs.writeFile(filePath, data, 'utf8');
            console.log(\`File written successfully: \${filePath}\`);
        } catch (error) {
            throw new Error(\`Failed to write file: \${error.message}\`);
        }
    }
    
    async listDirectory(dirPath) {
        try {
            const files = await fs.readdir(dirPath);
            return files.filter(file => !file.startsWith('.'));
        } catch (error) {
            throw new Error(\`Failed to list directory: \${error.message}\`);
        }
    }
    
    async createDirectory(dirPath) {
        try {
            await fs.mkdir(dirPath, { recursive: true });
            console.log(\`Directory created: \${dirPath}\`);
        } catch (error) {
            throw new Error(\`Failed to create directory: \${error.message}\`);
        }
    }
}

// Usage
const fileManager = new FileManager();
// await fileManager.writeFile('./example.txt', 'Hello, Node.js!');
// const content = await fileManager.readFile('./example.txt');
`;

console.log("File system operations:");
console.log(fileSystemCode);

// ===============================================================
// 12. TESTING FRAMEWORKS AND TDD
// ===============================================================
console.log("\n\n🔥 TESTING AND TEST-DRIVEN DEVELOPMENT");
console.log("=".repeat(50));

console.log("\n🧪 JEST TESTING FRAMEWORK:");

const jestTestCode = `
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
            setTimeout(() => resolve(\`Data from \${url}\`), 100);
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
`;

console.log("Complete Jest testing example:");
console.log(jestTestCode);

// ===============================================================
// 13. FUNCTIONAL PROGRAMMING ADVANCED CONCEPTS
// ===============================================================
console.log("\n\n🔥 ADVANCED FUNCTIONAL PROGRAMMING");
console.log("=".repeat(50));

console.log("\n🔄 ADVANCED FUNCTIONAL CONCEPTS:");

// Currying and partial application
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

const addThree = (a, b, c) => a + b + c;
const curriedAdd = curry(addThree);

console.log("Currying examples:");
console.log(`curriedAdd(1)(2)(3): ${curriedAdd(1)(2)(3)}`);
console.log(`curriedAdd(1, 2)(3): ${curriedAdd(1, 2)(3)}`);
console.log(`curriedAdd(1)(2, 3): ${curriedAdd(1)(2, 3)}`);

// Function composition
const compose = (...fns) => (value) => fns.reduceRight((acc, fn) => fn(acc), value);
const pipe = (...fns) => (value) => fns.reduce((acc, fn) => fn(acc), value);

const addOne = x => x + 1;
const doubleNum = x => x * 2;
const squareNum = x => x * x;

const composedFunction = compose(squareNum, doubleNum, addOne);
const pipedFunction = pipe(addOne, doubleNum, squareNum);

console.log("\nFunction composition:");
console.log(`compose(square, double, addOne)(3): ${composedFunction(3)}`); // (3+1)*2^2 = 64
console.log(`pipe(addOne, double, square)(3): ${pipedFunction(3)}`); // ((3+1)*2)^2 = 64

// Monads (Maybe/Option pattern)
class Maybe {
    constructor(value) {
        this.value = value;
    }
    
    static of(value) {
        return new Maybe(value);
    }
    
    static nothing() {
        return new Maybe(null);
    }
    
    isNothing() {
        return this.value === null || this.value === undefined;
    }
    
    map(fn) {
        return this.isNothing() ? Maybe.nothing() : Maybe.of(fn(this.value));
    }
    
    flatMap(fn) {
        return this.isNothing() ? Maybe.nothing() : fn(this.value);
    }
    
    getOrElse(defaultValue) {
        return this.isNothing() ? defaultValue : this.value;
    }
}

const maybeExample = Maybe.of(5)
    .map(x => x * 2)
    .map(x => x + 1)
    .getOrElse(0);

console.log("\nMaybe monad example:");
console.log(`Maybe.of(5).map(x2).map(+1): ${maybeExample}`);

// ===============================================================
// 14. PERFORMANCE OPTIMIZATION ADVANCED
// ===============================================================
console.log("\n\n🔥 ADVANCED PERFORMANCE OPTIMIZATION");
console.log("=".repeat(50));

console.log("\n⚡ MEMORY MANAGEMENT:");

// Memory-efficient techniques
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

// Example usage
const vectorPool = new ObjectPool(
    () => ({ x: 0, y: 0 }),
    (vector) => { vector.x = 0; vector.y = 0; }
);

console.log("Object pooling for memory efficiency");

// Web Workers for CPU-intensive tasks
const webWorkerCode = `
// worker.js
self.onmessage = function(e) {
    const { data, operation } = e.data;
    
    let result;
    switch(operation) {
        case 'factorial':
            result = factorial(data);
            break;
        case 'fibonacci':
            result = fibonacci(data);
            break;
        case 'primes':
            result = generatePrimes(data);
            break;
        default:
            result = null;
    }
    
    self.postMessage({ result, operation });
};

function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

function generatePrimes(max) {
    const primes = [];
    for (let i = 2; i <= max; i++) {
        if (isPrime(i)) primes.push(i);
    }
    return primes;
}

function isPrime(num) {
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

// main.js
class WorkerManager {
    constructor(workerScript) {
        this.worker = new Worker(workerScript);
        this.worker.onmessage = this.handleMessage.bind(this);
    }
    
    calculate(operation, data) {
        return new Promise((resolve) => {
            this.resolveCallback = resolve;
            this.worker.postMessage({ operation, data });
        });
    }
    
    handleMessage(e) {
        const { result, operation } = e.data;
        if (this.resolveCallback) {
            this.resolveCallback({ result, operation });
        }
    }
    
    terminate() {
        this.worker.terminate();
    }
}

// Usage
// const workerManager = new WorkerManager('worker.js');
// const result = await workerManager.calculate('factorial', 10);
`;

console.log("\nWeb Workers for CPU-intensive tasks:");
console.log(webWorkerCode);

// ===============================================================
// 15. MODERN JAVASCRIPT ECOSYSTEM
// ===============================================================
console.log("\n\n🔥 MODERN JAVASCRIPT ECOSYSTEM");
console.log("=".repeat(50));

console.log("\n📦 MODERN TOOLING:");

const modernToolingGuide = `
// package.json - Modern project setup
{
  "name": "modern-js-project",
  "version": "1.0.0",
  "type": "module", // Enable ES modules
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

// vite.config.js - Build tool configuration
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

// .eslintrc.js - Code quality
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
`;

console.log("Modern JavaScript tooling setup:");
console.log(modernToolingGuide);

console.log("\n🚀 NEXT STEPS FOR MASTERY:");
const nextSteps = [
    "Practice algorithmic challenges on LeetCode",
    "Build full-stack projects with React/Vue/Angular",
    "Master Node.js and Express.js for backend",
    "Learn TypeScript for type safety",
    "Study advanced patterns (functional programming)",
    "Master testing frameworks (Jest, Cypress)",
    "Understand build tools (Webpack, Vite, Rollup)",
    "Learn browser DevTools for debugging",
    "Explore modern frameworks (Next.js, Nuxt.js)",
    "Study performance optimization techniques",
    "Learn Web APIs (Service Workers, WebRTC)",
    "Master async patterns and reactive programming",
    "Understand micro-frontends architecture",
    "Learn GraphQL and modern state management"
];

nextSteps.forEach(step => console.log(`📈 ${step}`));

console.log("\n" + "=".repeat(60));
console.log("🎉 COMPLETE JAVASCRIPT MASTERY ACHIEVED!");
console.log("💪 Ready for Senior/Lead JavaScript Developer roles!");
console.log("🏆 Interview-ready with modern JS ecosystem knowledge!");
console.log("=".repeat(60));

// Run async demos
(async () => {
    await asyncFunction();
    await promiseCombinations();
})();