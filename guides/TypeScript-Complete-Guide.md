# 🔷 TypeScript Complete Mastery Guide

> **Complete TypeScript Reference for Modern Development**  
> From JavaScript to Type-Safe Development - All Concepts Covered

---

## 📚 Table of Contents

1. [TypeScript Fundamentals](#1-typescript-fundamentals)
2. [Basic Types](#2-basic-types)
3. [Interfaces and Types](#3-interfaces-and-types)
4. [Classes and Inheritance](#4-classes-and-inheritance)
5. [Generics](#5-generics)
6. [Advanced Types](#6-advanced-types)
7. [Modules and Namespaces](#7-modules-and-namespaces)
8. [Decorators](#8-decorators)
9. [TypeScript with React](#9-typescript-with-react)
10. [Node.js with TypeScript](#10-nodejs-with-typescript)
11. [Configuration and Build](#11-configuration-and-build)
12. [Best Practices](#12-best-practices)

---

## 1. TypeScript Fundamentals

### What is TypeScript?

TypeScript is a superset of JavaScript that adds static type definitions. It compiles to plain JavaScript and runs anywhere JavaScript runs.

### Getting Started

```bash
# Install TypeScript globally
npm install -g typescript

# Create tsconfig.json
tsc --init

# Compile TypeScript file
tsc app.ts

# Watch mode
tsc app.ts --watch
```

### Basic TypeScript File

```typescript
// app.ts
function greet(name: string): string {
    return `Hello, ${name}!`;
}

const user = "Alice";
console.log(greet(user));

// Compile: tsc app.ts
// Output: app.js (plain JavaScript)
```

---

## 2. Basic Types

### Primitive Types

```typescript
// Boolean
let isDone: boolean = false;
let isActive: boolean = true;

// Number
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;

// String
let color: string = "blue";
let fullName: string = `Bob Smith`;
let age: number = 37;
let sentence: string = `Hello, my name is ${fullName}. I'll be ${age + 1} years old next month.`;

// Null and Undefined
let u: undefined = undefined;
let n: null = null;

// Void (typically for functions that don't return a value)
function warnUser(): void {
    console.log("This is my warning message");
}

// Never (for functions that never return)
function error(message: string): never {
    throw new Error(message);
}

// Any (disable type checking)
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // okay, definitely a boolean

// Unknown (type-safe any)
let userInput: unknown;
let userName: string;

userInput = 5;
userInput = "hello";

if (typeof userInput === "string") {
    userName = userInput; // Type guard required
}
```

### Arrays and Tuples

```typescript
// Arrays
let list: number[] = [1, 2, 3];
let listGeneric: Array<number> = [1, 2, 3];
let mixedArray: (string | number)[] = ["hello", 42, "world"];

// Tuples
let x: [string, number];
x = ["hello", 10]; // OK
// x = [10, "hello"]; // Error

// Tuple with optional elements
let optionalTuple: [string, number?] = ["hello"];

// Rest elements in tuples
let restTuple: [string, ...number[]] = ["hello", 1, 2, 3];

// Named tuples
let namedTuple: [name: string, age: number] = ["Alice", 30];
```

### Enums

```typescript
// Numeric enum
enum Color {
    Red,    // 0
    Green,  // 1
    Blue    // 2
}
let c: Color = Color.Green;

// String enum
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT",
}

// Mixed enum
enum BooleanLikeHeterogeneousEnum {
    No = 0,
    Yes = "YES",
}

// Const enum (optimized)
const enum Status {
    Active = "ACTIVE",
    Inactive = "INACTIVE"
}
```

---

## 3. Interfaces and Types

### Interfaces

```typescript
// Basic interface
interface User {
    name: string;
    age: number;
    email: string;
}

function createUser(user: User): User {
    return user;
}

const newUser = createUser({
    name: "Alice",
    age: 30,
    email: "alice@example.com"
});

// Optional properties
interface Config {
    color?: string;
    width?: number;
}

// Readonly properties
interface Point {
    readonly x: number;
    readonly y: number;
}

let p1: Point = { x: 10, y: 20 };
// p1.x = 5; // Error: Cannot assign to 'x' because it is a read-only property

// Index signatures
interface StringArray {
    [index: number]: string;
}

interface StringDictionary {
    [key: string]: string;
}

// Function types in interfaces
interface SearchFunc {
    (source: string, subString: string): boolean;
}

let mySearch: SearchFunc = function(source: string, subString: string): boolean {
    return source.search(subString) > -1;
};

// Class types
interface ClockInterface {
    currentTime: Date;
    setTime(d: Date): void;
}

class Clock implements ClockInterface {
    currentTime: Date = new Date();
    setTime(d: Date) {
        this.currentTime = d;
    }
}
```

### Type Aliases

```typescript
// Basic type alias
type Name = string;
type Age = number;
type User = {
    name: Name;
    age: Age;
};

// Union types
type StringOrNumber = string | number;
type Theme = "light" | "dark";

// Function type alias
type EventHandler = (event: Event) => void;

// Generic type alias
type Container<T> = {
    value: T;
};

// Conditional types
type NonNullable<T> = T extends null | undefined ? never : T;

// Template literal types
type Greeting = `hello ${string}`;
type EmailAddress = `${string}@${string}.${string}`;
```

### Interface vs Type

```typescript
// Interface - can be extended and merged
interface Animal {
    name: string;
}

interface Animal {
    age: number; // Declaration merging
}

interface Dog extends Animal {
    breed: string;
}

// Type - more flexible for unions and complex types
type Pet = Dog | Cat;
type EventNames = "click" | "scroll" | "mousemove";
```

---

## 4. Classes and Inheritance

### Basic Classes

```typescript
class Person {
    // Properties
    private name: string;
    protected age: number;
    public email: string;
    readonly id: number;

    // Constructor
    constructor(name: string, age: number, email: string) {
        this.name = name;
        this.age = age;
        this.email = email;
        this.id = Date.now();
    }

    // Methods
    greet(): string {
        return `Hello, I'm ${this.name}`;
    }

    // Getter
    get displayName(): string {
        return this.name.toUpperCase();
    }

    // Setter
    set displayName(newName: string) {
        if (newName.length > 0) {
            this.name = newName;
        }
    }

    // Static method
    static createGuest(): Person {
        return new Person("Guest", 0, "guest@example.com");
    }
}

// Inheritance
class Employee extends Person {
    private department: string;
    private salary: number;

    constructor(name: string, age: number, email: string, department: string, salary: number) {
        super(name, age, email); // Call parent constructor
        this.department = department;
        this.salary = salary;
    }

    // Override method
    greet(): string {
        return `${super.greet()} I work in ${this.department}`;
    }

    // New method
    getAnnualSalary(): number {
        return this.salary * 12;
    }
}

// Parameter properties (shorthand)
class Student {
    constructor(
        public name: string,
        private grade: number,
        protected school: string
    ) {}
}
```

### Abstract Classes

```typescript
abstract class Animal {
    abstract makeSound(): void;

    move(): void {
        console.log("Moving...");
    }
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

// const animal = new Animal(); // Error: Cannot create instance of abstract class
const dog = new Dog();
dog.makeSound(); // "Woof!"
dog.move(); // "Moving..."
```

---

## 5. Generics

### Basic Generics

```typescript
// Generic function
function identity<T>(arg: T): T {
    return arg;
}

let output1 = identity<string>("myString");
let output2 = identity<number>(100);

// Generic with type inference
let output3 = identity("myString"); // TypeScript infers string

// Generic with constraints
interface Lengthwise {
    length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
    console.log(arg.length);
    return arg;
}

loggingIdentity("hello"); // OK
loggingIdentity([1, 2, 3]); // OK
// loggingIdentity(3); // Error: number doesn't have length property
```

### Generic Classes

```typescript
class GenericNumber<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;

    constructor(zeroValue: T, addFunction: (x: T, y: T) => T) {
        this.zeroValue = zeroValue;
        this.add = addFunction;
    }
}

let myGenericNumber = new GenericNumber<number>(0, (x, y) => x + y);
let stringNumeric = new GenericNumber<string>("", (x, y) => x + y);

// Generic interfaces
interface Repository<T> {
    create(item: T): T;
    findById(id: string): T | null;
    update(id: string, item: Partial<T>): T;
    delete(id: string): boolean;
}

class UserRepository implements Repository<User> {
    private users: User[] = [];

    create(user: User): User {
        this.users.push(user);
        return user;
    }

    findById(id: string): User | null {
        return this.users.find(u => u.id === id) || null;
    }

    update(id: string, updates: Partial<User>): User {
        const user = this.findById(id);
        if (user) {
            Object.assign(user, updates);
        }
        return user!;
    }

    delete(id: string): boolean {
        const index = this.users.findIndex(u => u.id === id);
        if (index > -1) {
            this.users.splice(index, 1);
            return true;
        }
        return false;
    }
}
```

### Advanced Generics

```typescript
// Multiple type parameters
function combine<T, U>(first: T, second: U): T & U {
    return { ...first as any, ...second as any };
}

// Generic constraints with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let person = { name: "Alice", age: 30, email: "alice@example.com" };
let name = getProperty(person, "name"); // string
let age = getProperty(person, "age"); // number

// Conditional types
type ApiResponse<T> = T extends string ? string : T extends number ? number : object;

// Mapped types
type Optional<T> = {
    [P in keyof T]?: T[P];
};

type PersonOptional = Optional<Person>; // All properties become optional

// Utility types
type PartialPerson = Partial<Person>; // All properties optional
type RequiredPerson = Required<Person>; // All properties required
type PersonName = Pick<Person, "name">; // Only name property
type PersonWithoutName = Omit<Person, "name">; // All except name
```

---

## 6. Advanced Types

### Union and Intersection Types

```typescript
// Union types
type StringOrNumber = string | number;
type Theme = "light" | "dark" | "auto";

function formatValue(value: StringOrNumber): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    } else {
        return value.toString();
    }
}

// Intersection types
interface Colorful {
    color: string;
}

interface Circle {
    radius: number;
}

type ColorfulCircle = Colorful & Circle;

const cc: ColorfulCircle = {
    color: "red",
    radius: 42
};

// Discriminated unions
interface Bird {
    type: "bird";
    flyingSpeed: number;
}

interface Horse {
    type: "horse";
    runningSpeed: number;
}

type Animal = Bird | Horse;

function moveAnimal(animal: Animal) {
    switch (animal.type) {
        case "bird":
            console.log("Flying at speed: " + animal.flyingSpeed);
            break;
        case "horse":
            console.log("Running at speed: " + animal.runningSpeed);
            break;
    }
}
```

### Type Guards

```typescript
// typeof type guard
function isString(value: unknown): value is string {
    return typeof value === "string";
}

// instanceof type guard
class Car {
    drive() {
        console.log("Driving a car...");
    }
}

class Truck {
    drive() {
        console.log("Driving a truck...");
    }
    
    loadCargo() {
        console.log("Loading cargo...");
    }
}

function useVehicle(vehicle: Car | Truck) {
    vehicle.drive();
    if (vehicle instanceof Truck) {
        vehicle.loadCargo();
    }
}

// Custom type guard
interface Cat {
    meow(): void;
}

interface Dog {
    bark(): void;
}

function isCat(animal: Cat | Dog): animal is Cat {
    return (animal as Cat).meow !== undefined;
}

function makeSound(animal: Cat | Dog) {
    if (isCat(animal)) {
        animal.meow();
    } else {
        animal.bark();
    }
}
```

### Template Literal Types

```typescript
// Basic template literal types
type World = "world";
type Greeting = `hello ${World}`; // "hello world"

// Template literal patterns
type EmailAddress = `${string}@${string}.${string}`;
type EventNames = `on${Capitalize<string>}`;

// Template literal with unions
type Color = "red" | "green" | "blue";
type Quantity = "one" | "two" | "three";
type SeussFish = `${Quantity | Color} fish`;
// "one fish" | "two fish" | "three fish" | "red fish" | "green fish" | "blue fish"

// Key remapping with template literals
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type Person = {
    name: string;
    age: number;
};

type PersonGetters = Getters<Person>;
// {
//   getName: () => string;
//   getAge: () => number;
// }
```

---

## 7. Modules and Namespaces

### ES6 Modules

```typescript
// math.ts
export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}

export const PI = 3.14159;

export default function multiply(a: number, b: number): number {
    return a * b;
}

// main.ts
import multiply, { add, subtract, PI } from "./math";
import * as MathUtils from "./math";

console.log(add(2, 3)); // 5
console.log(multiply(2, 3)); // 6
console.log(MathUtils.PI); // 3.14159

// Re-exports
export { add, subtract } from "./math";
export { default as multiply } from "./math";
```

### Namespaces

```typescript
// geometry.ts
namespace Geometry {
    export interface Point {
        x: number;
        y: number;
    }

    export namespace Shapes {
        export class Circle {
            constructor(public center: Point, public radius: number) {}

            area(): number {
                return Math.PI * this.radius ** 2;
            }
        }

        export class Rectangle {
            constructor(
                public topLeft: Point,
                public width: number,
                public height: number
            ) {}

            area(): number {
                return this.width * this.height;
            }
        }
    }

    export function distance(p1: Point, p2: Point): number {
        return Math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2);
    }
}

// Usage
const point1: Geometry.Point = { x: 0, y: 0 };
const point2: Geometry.Point = { x: 3, y: 4 };
const circle = new Geometry.Shapes.Circle(point1, 5);
const distance = Geometry.distance(point1, point2);
```

### Module Augmentation

```typescript
// Extending existing modules
declare global {
    interface Array<T> {
        last(): T | undefined;
    }
}

Array.prototype.last = function() {
    return this[this.length - 1];
};

// Augmenting third-party modules
declare module "lodash" {
    interface LoDashStatic {
        customFunction(): string;
    }
}
```

---

## 8. Decorators

> Note: Decorators are experimental. Enable with `"experimentalDecorators": true` in tsconfig.json

### Class Decorators

```typescript
// Simple class decorator
function sealed(constructor: Function) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}

@sealed
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}

// Decorator factory
function Entity(tableName: string) {
    return function <T extends { new (...args: any[]): {} }>(constructor: T) {
        return class extends constructor {
            tableName = tableName;
        };
    };
}

@Entity("users")
class User {
    constructor(public name: string) {}
}
```

### Method Decorators

```typescript
// Method decorator
function log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${propertyName} with args:`, args);
        const result = originalMethod.apply(this, args);
        console.log(`Method ${propertyName} returned:`, result);
        return result;
    };
}

class Calculator {
    @log
    add(a: number, b: number): number {
        return a + b;
    }
}

// Property decorator
function readonly(target: any, propertyName: string) {
    Object.defineProperty(target, propertyName, {
        writable: false
    });
}

class Person {
    @readonly
    name: string = "Alice";
}

// Parameter decorator
function logParameter(target: any, propertyName: string, parameterIndex: number) {
    console.log(`Parameter ${parameterIndex} of ${propertyName} was decorated`);
}

class Service {
    method(@logParameter param1: string, @logParameter param2: number) {
        // Method implementation
    }
}
```

---

## 9. TypeScript with React

### React Component Types

```typescript
import React, { useState, useEffect, ReactNode } from 'react';

// Function component with props
interface Props {
    name: string;
    age?: number;
    children?: ReactNode;
}

const UserProfile: React.FC<Props> = ({ name, age = 0, children }) => {
    const [isVisible, setIsVisible] = useState<boolean>(true);

    return (
        <div>
            <h1>{name}</h1>
            {age > 0 && <p>Age: {age}</p>}
            {children}
            <button onClick={() => setIsVisible(!isVisible)}>
                Toggle
            </button>
        </div>
    );
};

// Class component
interface State {
    count: number;
}

class Counter extends React.Component<Props, State> {
    state: State = {
        count: 0
    };

    increment = (): void => {
        this.setState({ count: this.state.count + 1 });
    };

    render(): ReactNode {
        return (
            <div>
                <p>Count: {this.state.count}</p>
                <button onClick={this.increment}>Increment</button>
            </div>
        );
    }
}
```

### Hooks with TypeScript

```typescript
import { useState, useEffect, useRef, useCallback, useMemo } from 'react';

// useState with type inference
const [name, setName] = useState(""); // string
const [age, setAge] = useState(0); // number
const [user, setUser] = useState<User | null>(null); // User | null

// useEffect
useEffect(() => {
    // Effect logic
    return () => {
        // Cleanup
    };
}, []);

// useRef
const inputRef = useRef<HTMLInputElement>(null);
const countRef = useRef<number>(0);

// useCallback
const handleClick = useCallback((id: string) => {
    console.log(`Clicked item ${id}`);
}, []);

// useMemo
const expensiveValue = useMemo(() => {
    return computeExpensiveValue(data);
}, [data]);

// Custom hook
function useCounter(initialValue: number = 0) {
    const [count, setCount] = useState(initialValue);

    const increment = useCallback(() => setCount(c => c + 1), []);
    const decrement = useCallback(() => setCount(c => c - 1), []);
    const reset = useCallback(() => setCount(initialValue), [initialValue]);

    return { count, increment, decrement, reset };
}

// Using custom hook
const MyComponent: React.FC = () => {
    const { count, increment, decrement, reset } = useCounter(10);

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={increment}>+</button>
            <button onClick={decrement}>-</button>
            <button onClick={reset}>Reset</button>
        </div>
    );
};
```

### Event Handling

```typescript
import React from 'react';

const EventExample: React.FC = () => {
    const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
        console.log('Button clicked', event.currentTarget);
    };

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        console.log('Input changed', event.target.value);
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log('Form submitted');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input onChange={handleChange} />
            <button onClick={handleClick}>Submit</button>
        </form>
    );
};
```

---

## 10. Node.js with TypeScript

### Setting Up Node.js Project

```bash
# Initialize project
npm init -y

# Install TypeScript and dependencies
npm install -D typescript @types/node ts-node nodemon
npm install express
npm install -D @types/express

# Create tsconfig.json
npx tsc --init
```

### Express Server with TypeScript

```typescript
// server.ts
import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Types
interface User {
    id: number;
    name: string;
    email: string;
}

interface CreateUserRequest {
    name: string;
    email: string;
}

// Routes
app.get('/', (req: Request, res: Response) => {
    res.json({ message: 'TypeScript Express Server' });
});

app.get('/api/users', (req: Request, res: Response) => {
    const users: User[] = [
        { id: 1, name: 'Alice', email: 'alice@example.com' },
        { id: 2, name: 'Bob', email: 'bob@example.com' }
    ];
    res.json({ users });
});

app.post('/api/users', (req: Request<{}, User, CreateUserRequest>, res: Response<User>) => {
    const { name, email } = req.body;
    
    const newUser: User = {
        id: Date.now(),
        name,
        email
    };
    
    res.status(201).json(newUser);
});

// Error handling
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### Database Integration

```typescript
// database.ts
import { Pool } from 'pg';

interface DatabaseConfig {
    host: string;
    port: number;
    database: string;
    user: string;
    password: string;
}

class Database {
    private pool: Pool;

    constructor(config: DatabaseConfig) {
        this.pool = new Pool(config);
    }

    async query<T = any>(text: string, params?: any[]): Promise<T[]> {
        const client = await this.pool.connect();
        try {
            const result = await client.query(text, params);
            return result.rows;
        } finally {
            client.release();
        }
    }

    async close(): Promise<void> {
        await this.pool.end();
    }
}

// User repository
class UserRepository {
    constructor(private db: Database) {}

    async findById(id: number): Promise<User | null> {
        const users = await this.db.query<User>(
            'SELECT * FROM users WHERE id = $1',
            [id]
        );
        return users[0] || null;
    }

    async create(userData: CreateUserRequest): Promise<User> {
        const users = await this.db.query<User>(
            'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
            [userData.name, userData.email]
        );
        return users[0];
    }

    async findAll(): Promise<User[]> {
        return this.db.query<User>('SELECT * FROM users');
    }
}
```

---

## 11. Configuration and Build

### tsconfig.json

```json
{
  "compilerOptions": {
    // Target and Module
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    
    // Output
    "outDir": "./dist",
    "rootDir": "./src",
    "removeComments": true,
    "sourceMap": true,
    
    // Type Checking
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    
    // Module Resolution
    "moduleResolution": "node",
    "baseUrl": "./",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    },
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    
    // Experimental
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    
    // Advanced
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist",
    "**/*.test.ts"
  ]
}
```

### Build Scripts

```json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node src/index.ts",
    "watch": "tsc --watch",
    "dev:watch": "nodemon --exec ts-node src/index.ts",
    "lint": "eslint src/**/*.ts",
    "test": "jest",
    "clean": "rimraf dist"
  }
}
```

### Webpack Configuration

```javascript
// webpack.config.js
const path = require('path');

module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

---

## 12. Best Practices

### Type Safety

```typescript
// Use strict types
interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

// Avoid any, use unknown instead
function processData(data: unknown): string {
    if (typeof data === 'string') {
        return data.toUpperCase();
    }
    if (typeof data === 'object' && data !== null) {
        return JSON.stringify(data);
    }
    return String(data);
}

// Use type assertions carefully
const userInput = document.getElementById('user-input') as HTMLInputElement;

// Prefer type guards
function isUser(obj: any): obj is User {
    return obj && typeof obj.name === 'string' && typeof obj.email === 'string';
}
```

### Error Handling

```typescript
// Result pattern for error handling
type Result<T, E = Error> = {
    success: true;
    data: T;
} | {
    success: false;
    error: E;
};

async function fetchUser(id: number): Promise<Result<User>> {
    try {
        const user = await api.getUser(id);
        return { success: true, data: user };
    } catch (error) {
        return { success: false, error: error as Error };
    }
}

// Usage
const result = await fetchUser(1);
if (result.success) {
    console.log(result.data.name); // TypeScript knows this is User
} else {
    console.error(result.error.message); // TypeScript knows this is Error
}
```

### Performance Tips

```typescript
// Use const assertions for better inference
const colors = ['red', 'green', 'blue'] as const;
type Color = typeof colors[number]; // 'red' | 'green' | 'blue'

// Lazy loading with dynamic imports
async function loadModule() {
    const { heavyFunction } = await import('./heavy-module');
    return heavyFunction();
}

// Use branded types for type safety
type UserId = string & { readonly brand: unique symbol };
type Email = string & { readonly brand: unique symbol };

function createUserId(id: string): UserId {
    return id as UserId;
}

function createEmail(email: string): Email {
    if (!email.includes('@')) {
        throw new Error('Invalid email');
    }
    return email as Email;
}

// Now these can't be mixed up
function sendEmail(userId: UserId, email: Email): void {
    // Implementation
}
```

### Testing with TypeScript

```typescript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
  ],
};

// Example test
import { Calculator } from '../Calculator';

describe('Calculator', () => {
    let calculator: Calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    it('should add two numbers correctly', () => {
        const result = calculator.add(2, 3);
        expect(result).toBe(5);
    });

    it('should handle edge cases', () => {
        expect(calculator.add(0, 0)).toBe(0);
        expect(calculator.add(-1, 1)).toBe(0);
    });
});
```

---

## 🚀 Next Steps for TypeScript Mastery

### 1. **Advanced Type System**
- Conditional types and mapped types
- Template literal types
- Recursive types and type-level programming

### 2. **Framework Integration**
- **React**: Advanced patterns with TypeScript
- **Vue**: Composition API with TypeScript
- **Angular**: Full TypeScript integration

### 3. **Backend Development**
- **Express**: Type-safe REST APIs
- **NestJS**: Decorator-based architecture
- **GraphQL**: Type-safe schema definition

### 4. **Build and Tooling**
- Webpack and TypeScript
- ESBuild and SWC for fast compilation
- Monorepo setup with TypeScript

### 5. **Testing Strategy**
- Type-safe testing with Jest
- End-to-end testing with Playwright
- Property-based testing

---

## 📖 TypeScript Quick Reference

| Feature | Syntax | Use Case |
|---------|--------|----------|
| **Basic Types** | `let name: string` | Type annotation |
| **Interfaces** | `interface User { name: string }` | Object shapes |
| **Generics** | `function id<T>(arg: T): T` | Reusable components |
| **Union Types** | `string \| number` | Multiple possible types |
| **Type Guards** | `if (typeof x === 'string')` | Runtime type checking |
| **Utility Types** | `Partial<T>`, `Pick<T, K>` | Type transformations |
| **Decorators** | `@Component` | Metadata and enhancement |

---

> **🎉 Congratulations!** You now have a complete TypeScript reference covering all concepts from basic types to advanced patterns. TypeScript will help you write more maintainable, scalable, and bug-free JavaScript applications!

**Ready for production?** Start building type-safe applications with React, Node.js, or your favorite framework!