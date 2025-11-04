#!/usr/bin/env ts-node
/**
 * 🔷 TYPESCRIPT MASTERY GUIDE - COMPLETE REFERENCE FOR INTERVIEWS & MASTERY
 * =========================================================================
 * 
 * This comprehensive guide covers all TypeScript concepts from basics to advanced topics.
 * Perfect for interview preparation, skill assessment, and continuous learning.
 * 
 * Author: Tech Mastery Notebooks
 * Date: November 2025
 * Level: Beginner to Expert
 */

// ===============================================================
// 1. TYPESCRIPT FUNDAMENTALS - TYPE SYSTEM BASICS
// ===============================================================
console.log("🔷 TYPESCRIPT FUNDAMENTALS");
console.log("=".repeat(50));

// Basic Types
console.log("\n📊 BASIC TYPES:");

// Primitive types
const numberType: number = 42;
const stringType: string = "Hello, TypeScript!";
const booleanType: boolean = true;
const undefinedType: undefined = undefined;
const nullType: null = null;

console.log(`Number: ${numberType} (type: number)`);
console.log(`String: ${stringType} (type: string)`);
console.log(`Boolean: ${booleanType} (type: boolean)`);
console.log(`Undefined: ${undefinedType} (type: undefined)`);
console.log(`Null: ${nullType} (type: null)`);

// Array types
const numberArray: number[] = [1, 2, 3, 4, 5];
const stringArray: Array<string> = ["apple", "banana", "cherry"];
const mixedArray: (string | number)[] = ["hello", 42, "world", 100];

console.log(`\nNumber array: ${numberArray}`);
console.log(`String array: ${stringArray}`);
console.log(`Mixed array: ${mixedArray}`);

// Tuple types
const tuple: [string, number, boolean] = ["Alice", 30, true];
const namedTuple: readonly [name: string, age: number] = ["Bob", 25];

console.log(`Tuple: ${tuple}`);
console.log(`Named tuple: ${namedTuple}`);

// Enum types
enum Color {
    Red = "red",
    Green = "green",
    Blue = "blue"
}

enum Status {
    Pending,
    Approved,
    Rejected
}

console.log(`\nColor enum: ${Color.Red}`);
console.log(`Status enum: ${Status.Pending} (numeric)`);

// ===============================================================
// 2. OBJECT TYPES AND INTERFACES
// ===============================================================
console.log("\n\n🔷 OBJECT TYPES AND INTERFACES");
console.log("=".repeat(50));

// Object type annotations
const userObj: { name: string; age: number; email?: string } = {
    name: "Alice",
    age: 30
};

console.log(`\n👤 OBJECT TYPES:`);
console.log(`User object:`, userObj);

// Interface definitions
interface User {
    readonly id: number;
    name: string;
    age: number;
    email?: string; // Optional property
    isActive: boolean;
}

interface UserMethods {
    getName(): string;
    setAge(age: number): void;
    getFullProfile(): string;
}

// Combining interfaces
interface CompleteUser extends User, UserMethods {}

// Interface implementation
class UserClass implements CompleteUser {
    readonly id: number;
    name: string;
    age: number;
    email?: string;
    isActive: boolean;

    constructor(id: number, name: string, age: number, isActive: boolean = true) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.isActive = isActive;
    }

    getName(): string {
        return this.name;
    }

    setAge(age: number): void {
        this.age = age;
    }

    getFullProfile(): string {
        return `User ${this.name} (ID: ${this.id}, Age: ${this.age})`;
    }
}

const user = new UserClass(1, "Alice", 30);
console.log(`User profile: ${user.getFullProfile()}`);

// Index signatures
interface StringDictionary {
    [key: string]: string;
}

interface NumberDictionary {
    [key: string]: number;
    length: number; // Can have specific properties too
}

const colors: StringDictionary = {
    primary: "blue",
    secondary: "green",
    accent: "red"
};

console.log(`Colors dictionary:`, colors);

// ===============================================================
// 3. UNION TYPES AND TYPE GUARDS
// ===============================================================
console.log("\n\n🔷 UNION TYPES AND TYPE GUARDS");
console.log("=".repeat(50));

// Union types
type StringOrNumber = string | number;
type Theme = "light" | "dark" | "auto";

function formatValue(value: StringOrNumber): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    } else {
        return value.toFixed(2);
    }
}

console.log(`\n🔀 UNION TYPES:`);
console.log(`Format string: ${formatValue("hello")}`);
console.log(`Format number: ${formatValue(42.789)}`);

// Discriminated unions
interface Circle {
    kind: "circle";
    radius: number;
}

interface Rectangle {
    kind: "rectangle";
    width: number;
    height: number;
}

interface Triangle {
    kind: "triangle";
    base: number;
    height: number;
}

type Shape = Circle | Rectangle | Triangle;

function calculateArea(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "rectangle":
            return shape.width * shape.height;
        case "triangle":
            return (shape.base * shape.height) / 2;
        default:
            // Exhaustiveness check
            const _exhaustiveCheck: never = shape;
            return _exhaustiveCheck;
    }
}

const circle: Circle = { kind: "circle", radius: 5 };
const rectangle: Rectangle = { kind: "rectangle", width: 10, height: 6 };

console.log(`Circle area: ${calculateArea(circle).toFixed(2)}`);
console.log(`Rectangle area: ${calculateArea(rectangle)}`);

// Type guards
function isString(value: any): value is string {
    return typeof value === "string";
}

function isUser(obj: any): obj is User {
    return obj && typeof obj.name === "string" && typeof obj.age === "number";
}

// Using type guards
function processValue(value: unknown) {
    if (isString(value)) {
        console.log(`Processing string: ${value.toUpperCase()}`);
    } else if (typeof value === "number") {
        console.log(`Processing number: ${value.toFixed(2)}`);
    } else {
        console.log(`Unknown type: ${typeof value}`);
    }
}

console.log(`\n🛡️ TYPE GUARDS:`);
processValue("hello");
processValue(42.789);
processValue(true);

// ===============================================================
// 4. GENERICS - REUSABLE TYPE DEFINITIONS
// ===============================================================
console.log("\n\n🔷 GENERICS");
console.log("=".repeat(50));

// Generic functions
function identity<T>(arg: T): T {
    return arg;
}

function getFirstElement<T>(array: T[]): T | undefined {
    return array[0];
}

function swapPair<T, U>(pair: [T, U]): [U, T] {
    return [pair[1], pair[0]];
}

console.log(`\n🧬 GENERIC FUNCTIONS:`);
console.log(`Identity string: ${identity("hello")}`);
console.log(`Identity number: ${identity(42)}`);
console.log(`First element: ${getFirstElement([1, 2, 3])}`);
console.log(`Swapped pair: ${swapPair(["hello", 42])}`);

// Generic interfaces
interface Container<T> {
    value: T;
    getValue(): T;
    setValue(value: T): void;
}

class Box<T> implements Container<T> {
    constructor(public value: T) {}

    getValue(): T {
        return this.value;
    }

    setValue(value: T): void {
        this.value = value;
    }
}

const stringBox = new Box<string>("Hello");
const numberBox = new Box<number>(42);

console.log(`String box: ${stringBox.getValue()}`);
console.log(`Number box: ${numberBox.getValue()}`);

// Generic constraints
interface Lengthwise {
    length: number;
}

function logAndReturn<T extends Lengthwise>(arg: T): T {
    console.log(`Length: ${arg.length}`);
    return arg;
}

logAndReturn("Hello, TypeScript!");
logAndReturn([1, 2, 3, 4, 5]);

// Conditional types
type NonNullable<T> = T extends null | undefined ? never : T;
type ArrayElement<T> = T extends (infer U)[] ? U : never;

type StringType = NonNullable<string | null>; // string
type NumberFromArray = ArrayElement<number[]>; // number

// ===============================================================
// 5. ADVANCED TYPES AND UTILITY TYPES
// ===============================================================
console.log("\n\n🔷 ADVANCED TYPES AND UTILITY TYPES");
console.log("=".repeat(50));

// Mapped types
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};

type Partial<T> = {
    [P in keyof T]?: T[P];
};

type Required<T> = {
    [P in keyof T]-?: T[P];
};

interface Person {
    name: string;
    age: number;
    email?: string;
}

type ReadonlyPerson = Readonly<Person>;
type PartialPerson = Partial<Person>;
type RequiredPerson = Required<Person>;

console.log(`\n🗺️ MAPPED TYPES:`);
console.log("Readonly, Partial, and Required utility types applied");

// Template literal types
type EventName<T extends string> = `on${Capitalize<T>}`;
type ButtonEvents = EventName<"click" | "hover" | "focus">; // "onClick" | "onHover" | "onFocus"

// Conditional types with template literals
type ExtractRouteParams<T extends string> = 
    T extends `${string}:${infer Param}/${infer Rest}`
        ? { [K in Param | keyof ExtractRouteParams<Rest>]: string }
        : T extends `${string}:${infer Param}`
        ? { [K in Param]: string }
        : {};

type RouteParams = ExtractRouteParams<"/users/:id/posts/:postId">; // { id: string, postId: string }

// Utility types in action
interface ApiResponse {
    id: number;
    name: string;
    email: string;
    createdAt: Date;
    updatedAt: Date;
}

type CreateUserRequest = Pick<ApiResponse, "name" | "email">;
type UpdateUserRequest = Partial<Pick<ApiResponse, "name" | "email">>;
type UserSummary = Omit<ApiResponse, "createdAt" | "updatedAt">;

function createUser(data: CreateUserRequest): ApiResponse {
    return {
        id: Math.random(),
        ...data,
        createdAt: new Date(),
        updatedAt: new Date()
    };
}

const newUser = createUser({ name: "John", email: "john@example.com" });
console.log(`Created user: ${newUser.name}`);

// ===============================================================
// 6. CLASSES AND INHERITANCE
// ===============================================================
console.log("\n\n🔷 CLASSES AND INHERITANCE");
console.log("=".repeat(50));

// Abstract classes
abstract class Animal {
    protected name: string;
    protected age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    abstract makeSound(): string;
    
    protected getInfo(): string {
        return `${this.name} is ${this.age} years old`;
    }

    public introduce(): string {
        return `${this.getInfo()} and says: ${this.makeSound()}`;
    }
}

class Dog extends Animal {
    private breed: string;

    constructor(name: string, age: number, breed: string) {
        super(name, age);
        this.breed = breed;
    }

    makeSound(): string {
        return "Woof!";
    }

    public getBreed(): string {
        return this.breed;
    }
}

class Cat extends Animal {
    private isIndoor: boolean;

    constructor(name: string, age: number, isIndoor: boolean = true) {
        super(name, age);
        this.isIndoor = isIndoor;
    }

    makeSound(): string {
        return "Meow!";
    }

    public isIndoorCat(): boolean {
        return this.isIndoor;
    }
}

const dog = new Dog("Buddy", 3, "Golden Retriever");
const cat = new Cat("Whiskers", 2, true);

console.log(`\n🐕 CLASSES AND INHERITANCE:`);
console.log(dog.introduce());
console.log(cat.introduce());
console.log(`Dog breed: ${dog.getBreed()}`);
console.log(`Cat is indoor: ${cat.isIndoorCat()}`);

// Static members and getters/setters
class MathUtils {
    private static readonly PI = 3.14159;
    private _value: number = 0;

    static circleArea(radius: number): number {
        return this.PI * radius * radius;
    }

    get value(): number {
        return this._value;
    }

    set value(newValue: number) {
        if (newValue < 0) {
            throw new Error("Value cannot be negative");
        }
        this._value = newValue;
    }
}

console.log(`Circle area: ${MathUtils.circleArea(5)}`);

const mathUtils = new MathUtils();
mathUtils.value = 42;
console.log(`Math utils value: ${mathUtils.value}`);

// ===============================================================
// 7. MODULES AND NAMESPACES
// ===============================================================
console.log("\n\n🔷 MODULES AND NAMESPACES");
console.log("=".repeat(50));

// Namespace example
namespace Validation {
    export interface StringValidator {
        isAcceptable(s: string): boolean;
    }

    const lettersRegexp = /^[A-Za-z]+$/;
    const numberRegexp = /^[0-9]+$/;

    export class LettersOnlyValidator implements StringValidator {
        isAcceptable(s: string) {
            return lettersRegexp.test(s);
        }
    }

    export class ZipCodeValidator implements StringValidator {
        isAcceptable(s: string) {
            return s.length === 5 && numberRegexp.test(s);
        }
    }
}

// Module-like structure
export class DataProcessor<T> {
    private data: T[] = [];

    add(item: T): void {
        this.data.push(item);
    }

    process(callback: (item: T) => T): T[] {
        return this.data.map(callback);
    }

    filter(predicate: (item: T) => boolean): T[] {
        return this.data.filter(predicate);
    }

    getCount(): number {
        return this.data.length;
    }
}

const validator = new Validation.LettersOnlyValidator();
const zipValidator = new Validation.ZipCodeValidator();

console.log(`\n📦 MODULES AND NAMESPACES:`);
console.log(`Letters validation: ${validator.isAcceptable("Hello")}`);
console.log(`Zip validation: ${zipValidator.isAcceptable("12345")}`);

const processor = new DataProcessor<number>();
processor.add(1);
processor.add(2);
processor.add(3);
console.log(`Processed data: ${processor.process(x => x * 2)}`);

// ===============================================================
// 8. DECORATORS AND METADATA
// ===============================================================
console.log("\n\n🔷 DECORATORS AND METADATA");
console.log("=".repeat(50));

// Method decorators
function log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${propertyName} with arguments: ${JSON.stringify(args)}`);
        const result = method.apply(this, args);
        console.log(`${propertyName} returned: ${JSON.stringify(result)}`);
        return result;
    };
    
    return descriptor;
}

function validate(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        for (const arg of args) {
            if (arg == null) {
                throw new Error(`Null or undefined argument passed to ${propertyName}`);
            }
        }
        return method.apply(this, args);
    };
    
    return descriptor;
}

// Class using decorators
class Calculator {
    add(a: number, b: number): number {
        console.log(`Calling add with arguments: [${a}, ${b}]`);
        const result = a + b;
        console.log(`add returned: ${result}`);
        return result;
    }

    multiply(a: number, b: number): number {
        console.log(`Calling multiply with arguments: [${a}, ${b}]`);
        const result = a * b;
        console.log(`multiply returned: ${result}`);
        return result;
    }
}

console.log(`\n🎭 DECORATORS:`);
const calc = new Calculator();
console.log(`Addition result: ${calc.add(5, 3)}`);
console.log(`Multiplication result: ${calc.multiply(4, 6)}`);

// Property example (without decorators for compatibility)
class Product {
    readonly id: number;
    name: string;
    price: number;

    constructor(id: number, name: string, price: number) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
}

// ===============================================================
// 9. ASYNC/AWAIT AND PROMISES WITH TYPES
// ===============================================================
console.log("\n\n🔷 ASYNC/AWAIT AND PROMISES");
console.log("=".repeat(50));

// Generic promise types
interface ApiUser {
    id: number;
    name: string;
    email: string;
}

interface ApiError {
    message: string;
    code: number;
}

type ApiResult<T> = {
    success: true;
    data: T;
} | {
    success: false;
    error: ApiError;
};

// Async functions with proper typing
async function fetchUser(id: number): Promise<ApiResult<ApiUser>> {
    try {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 100));
        
        if (id <= 0) {
            return {
                success: false,
                error: { message: "Invalid user ID", code: 400 }
            };
        }

        return {
            success: true,
            data: {
                id,
                name: `User ${id}`,
                email: `user${id}@example.com`
            }
        };
    } catch (error) {
        return {
            success: false,
            error: { message: "Network error", code: 500 }
        };
    }
}

async function fetchMultipleUsers(ids: number[]): Promise<ApiUser[]> {
    const promises = ids.map(id => fetchUser(id));
    const results = await Promise.all(promises);
    
    return results
        .filter((result): result is { success: true; data: ApiUser } => result.success)
        .map(result => result.data);
}

// Usage example
(async () => {
    console.log(`\n🔄 ASYNC/AWAIT:`);
    
    const userResult = await fetchUser(1);
    if (userResult.success) {
        console.log(`Fetched user: ${userResult.data.name}`);
    } else {
        console.log(`Error: ${userResult.error.message}`);
    }

    const users = await fetchMultipleUsers([1, 2, 3]);
    console.log(`Fetched ${users.length} users`);
})();

// ===============================================================
// 10. ERROR HANDLING AND CUSTOM TYPES
// ===============================================================
console.log("\n\n🔷 ERROR HANDLING");
console.log("=".repeat(50));

// Custom error types
class ValidationError extends Error {
    constructor(
        message: string,
        public field: string,
        public value: any
    ) {
        super(message);
        this.name = "ValidationError";
    }
}

class NotFoundError extends Error {
    constructor(resource: string, id: string | number) {
        super(`${resource} with id ${id} not found`);
        this.name = "NotFoundError";
    }
}

// Result type pattern
type Result<T, E = Error> = 
    | { success: true; data: T }
    | { success: false; error: E };

function validateEmail(email: string): Result<string, ValidationError> {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!emailRegex.test(email)) {
        return {
            success: false,
            error: new ValidationError("Invalid email format", "email", email)
        };
    }
    
    return { success: true, data: email };
}

function findUserById(id: number): Result<ApiUser, NotFoundError> {
    // Simulate user lookup
    if (id === 999) {
        return {
            success: false,
            error: new NotFoundError("User", id)
        };
    }
    
    return {
        success: true,
        data: { id, name: `User ${id}`, email: `user${id}@example.com` }
    };
}

console.log(`\n❌ ERROR HANDLING:`);

const emailResult = validateEmail("invalid-email");
if (!emailResult.success) {
    console.log(`Validation error: ${emailResult.error.message} for field: ${emailResult.error.field}`);
}

const userResult2 = findUserById(999);
if (!userResult2.success) {
    console.log(`Not found error: ${userResult2.error.message}`);
}

// ===============================================================
// 11. PERFORMANCE AND OPTIMIZATION
// ===============================================================
console.log("\n\n🔷 PERFORMANCE OPTIMIZATION");
console.log("=".repeat(50));

// Type-only imports for better tree shaking
type UserType = User; // Type-only import/usage

// Const assertions for better type inference
const themes = ["light", "dark", "auto"] as const;
type ThemeType = typeof themes[number]; // "light" | "dark" | "auto"

const config = {
    apiUrl: "https://api.example.com",
    timeout: 5000,
    retries: 3
} as const;

type Config = typeof config;

// Lazy evaluation with getters
class ExpensiveCalculation {
    private _result?: number;

    get result(): number {
        if (this._result === undefined) {
            console.log("Performing expensive calculation...");
            this._result = Array.from({ length: 1000000 }, (_, i) => i)
                .reduce((sum, i) => sum + i, 0);
        }
        return this._result;
    }
}

console.log(`\n⚡ PERFORMANCE:`);
console.log(`Themes type: ${themes.join(", ")}`);
console.log(`Config keys: ${Object.keys(config).join(", ")}`);

const calc2 = new ExpensiveCalculation();
console.log(`First access: ${calc2.result > 0 ? "Calculated" : "Error"}`);
console.log(`Second access: ${calc2.result > 0 ? "Cached" : "Error"}`);

// ===============================================================
// 12. TESTING WITH TYPESCRIPT
// ===============================================================
console.log("\n\n🔷 TESTING WITH TYPESCRIPT");
console.log("=".repeat(50));

// Type-safe testing utilities
interface TestCase<T, R> {
    input: T;
    expected: R;
    description: string;
}

function createTestSuite<T, R>(
    name: string,
    testFunction: (input: T) => R,
    testCases: TestCase<T, R>[]
): void {
    console.log(`\n🧪 Test Suite: ${name}`);
    
    testCases.forEach((testCase, index) => {
        try {
            const result = testFunction(testCase.input);
            const passed = JSON.stringify(result) === JSON.stringify(testCase.expected);
            
            console.log(`  Test ${index + 1}: ${testCase.description} - ${passed ? "✅ PASS" : "❌ FAIL"}`);
            if (!passed) {
                console.log(`    Expected: ${JSON.stringify(testCase.expected)}`);
                console.log(`    Received: ${JSON.stringify(result)}`);
            }
        } catch (error) {
            console.log(`  Test ${index + 1}: ${testCase.description} - ❌ ERROR: ${error}`);
        }
    });
}

// Example test usage
function addNumbers(a: number, b: number): number {
    return a + b;
}

const mathTestCases: TestCase<[number, number], number>[] = [
    { input: [2, 3], expected: 5, description: "Add positive numbers" },
    { input: [-1, 1], expected: 0, description: "Add negative and positive" },
    { input: [0, 0], expected: 0, description: "Add zeros" }
];

createTestSuite("Math Operations", ([a, b]) => addNumbers(a, b), mathTestCases);

// Mock types for testing
interface MockUser {
    id: number;
    name: string;
    email: string;
}

type MockFunction<T extends (...args: any[]) => any> = {
    (...args: Parameters<T>): ReturnType<T>;
    mockReturnValue(value: ReturnType<T>): void;
    mockImplementation(fn: T): void;
    calls: Parameters<T>[];
};

function createMock<T extends (...args: any[]) => any>(): MockFunction<T> {
    const calls: Parameters<T>[] = [];
    let returnValue: ReturnType<T>;
    let implementation: T;

    const mockFn = ((...args: Parameters<T>): ReturnType<T> => {
        calls.push(args);
        if (implementation) {
            return implementation(...args);
        }
        return returnValue;
    }) as MockFunction<T>;

    mockFn.mockReturnValue = (value: ReturnType<T>) => {
        returnValue = value;
    };

    mockFn.mockImplementation = (fn: T) => {
        implementation = fn;
    };

    mockFn.calls = calls;

    return mockFn;
}

console.log("\n🎭 MOCKING:");
const mockGetUser = createMock<(id: number) => MockUser>();
mockGetUser.mockReturnValue({ id: 1, name: "Test User", email: "test@example.com" });

const result = mockGetUser(1);
console.log(`Mock result: ${result.name}`);
console.log(`Mock was called ${mockGetUser.calls.length} times`);

// ===============================================================
// 13. REAL-WORLD PATTERNS AND BEST PRACTICES
// ===============================================================
console.log("\n\n🔷 REAL-WORLD PATTERNS");
console.log("=".repeat(50));

// Builder pattern with TypeScript
class ApiRequestBuilder {
    private url: string = "";
    private method: "GET" | "POST" | "PUT" | "DELETE" = "GET";
    private headers: Record<string, string> = {};
    private body?: any;

    setUrl(url: string): this {
        this.url = url;
        return this;
    }

    setMethod(method: "GET" | "POST" | "PUT" | "DELETE"): this {
        this.method = method;
        return this;
    }

    setHeader(key: string, value: string): this {
        this.headers[key] = value;
        return this;
    }

    setBody(body: any): this {
        this.body = body;
        return this;
    }

    build(): { url: string; method: string; headers: Record<string, string>; body?: any } {
        if (!this.url) {
            throw new Error("URL is required");
        }
        return {
            url: this.url,
            method: this.method,
            headers: this.headers,
            body: this.body
        };
    }
}

// Factory pattern
interface Logger {
    log(message: string): void;
    error(message: string): void;
}

class ConsoleLogger implements Logger {
    log(message: string): void {
        console.log(`[LOG] ${message}`);
    }

    error(message: string): void {
        console.error(`[ERROR] ${message}`);
    }
}

class FileLogger implements Logger {
    constructor(private filename: string) {}

    log(message: string): void {
        console.log(`[FILE LOG to ${this.filename}] ${message}`);
    }

    error(message: string): void {
        console.log(`[FILE ERROR to ${this.filename}] ${message}`);
    }
}

class LoggerFactory {
    static create(type: "console" | "file", filename?: string): Logger {
        switch (type) {
            case "console":
                return new ConsoleLogger();
            case "file":
                if (!filename) throw new Error("Filename required for file logger");
                return new FileLogger(filename);
            default:
                throw new Error(`Unknown logger type: ${type}`);
        }
    }
}

console.log(`\n🏗️ DESIGN PATTERNS:`);

const request = new ApiRequestBuilder()
    .setUrl("https://api.example.com/users")
    .setMethod("POST")
    .setHeader("Content-Type", "application/json")
    .setBody({ name: "John", email: "john@example.com" })
    .build();

console.log(`Built request: ${request.method} ${request.url}`);

const logger = LoggerFactory.create("console");
logger.log("Application started");

// Observer pattern with TypeScript
interface Observer<T> {
    update(data: T): void;
}

interface Subject<T> {
    subscribe(observer: Observer<T>): void;
    unsubscribe(observer: Observer<T>): void;
    notify(data: T): void;
}

class EventEmitter<T> implements Subject<T> {
    private observers: Observer<T>[] = [];

    subscribe(observer: Observer<T>): void {
        this.observers.push(observer);
    }

    unsubscribe(observer: Observer<T>): void {
        const index = this.observers.indexOf(observer);
        if (index > -1) {
            this.observers.splice(index, 1);
        }
    }

    notify(data: T): void {
        this.observers.forEach(observer => observer.update(data));
    }
}

class UserActivityObserver implements Observer<string> {
    update(activity: string): void {
        console.log(`User activity detected: ${activity}`);
    }
}

const activityEmitter = new EventEmitter<string>();
const activityObserver = new UserActivityObserver();

activityEmitter.subscribe(activityObserver);
activityEmitter.notify("User logged in");

console.log("\n🚀 TYPESCRIPT MASTERY COMPLETE!");
console.log("=".repeat(60));
console.log("🎯 Key Concepts Covered:");

const conceptsCovered = [
    "✅ Type System (primitives, arrays, tuples, enums)",
    "✅ Object Types and Interfaces",
    "✅ Union Types and Type Guards", 
    "✅ Generics and Constraints",
    "✅ Advanced Types and Utility Types",
    "✅ Classes and Inheritance",
    "✅ Modules and Namespaces",
    "✅ Decorators and Metadata",
    "✅ Async/Await with Types",
    "✅ Error Handling Patterns",
    "✅ Performance Optimization",
    "✅ Type-Safe Testing",
    "✅ Real-World Design Patterns"
];

conceptsCovered.forEach(concept => console.log(concept));

console.log("\n🎓 NEXT STEPS FOR MASTERY:");
const nextSteps = [
    "📚 Practice with real TypeScript projects",
    "🔧 Learn advanced compiler options",
    "🏗️ Study framework-specific TypeScript (React, Angular, Vue)",
    "📦 Master module resolution and bundling",
    "🔍 Learn advanced type manipulation techniques",
    "🧪 Practice test-driven development with TypeScript",
    "⚡ Optimize build performance and bundle size",
    "🌐 Explore TypeScript in Node.js backend development",
    "📖 Study TypeScript compiler API",
    "🎯 Master strict mode and advanced linting"
];

nextSteps.forEach(step => console.log(step));

console.log("\n" + "=".repeat(60));
console.log("🎉 READY FOR SENIOR TYPESCRIPT DEVELOPER ROLES!");
console.log("💪 Complete mastery achieved - from basics to advanced patterns!");
console.log("=".repeat(60));