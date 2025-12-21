"""
Demo Project 3: Advanced Calculator with Functions
Part 1: Python Fundamentals - Hour 5
Difficulty: ⭐⭐⭐ Advanced

Features:
- 9 different calculation modes
- Power, square root, factorial
- Percentage calculator
- BMI calculator
- Area calculators (circle, rectangle, triangle)
- Menu-driven interface
"""

import math

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
    if n < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(n)

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
    print("10. Area Calculator")
    print("0. Exit")
    print("=" * 30)

def area_calculator():
    """Area calculator submenu"""
    print("\n--- Area Calculator ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = input("Choose shape (1-3): ")
    
    if choice == "1":
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
        print(f"Area of circle: {area:.2f}")
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area of rectangle: {area:.2f}")
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of triangle: {area:.2f}")
    else:
        print("Invalid choice!")

def main():
    """Main program"""
    while True:
        display_menu()
        choice = input("Enter choice (0-10): ")
        
        if choice == "0":
            print("Thank you for using Advanced Calculator! 👋")
            break
        
        elif choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = add(a, b)
            print(f"Result: {result}")
        
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = subtract(a, b)
            print(f"Result: {result}")
        
        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = multiply(a, b)
            print(f"Result: {result}")
        
        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = divide(a, b)
            print(f"Result: {result}")
        
        elif choice == "5":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            result = power(base, exponent)
            print(f"Result: {result}")
        
        elif choice == "6":
            n = float(input("Enter number: "))
            result = square_root(n)
            print(f"Result: {result}")
        
        elif choice == "7":
            value = float(input("Enter value: "))
            percent = float(input("Enter percentage: "))
            result = percentage(value, percent)
            print(f"Result: {result}")
        
        elif choice == "8":
            n = int(input("Enter number: "))
            result = factorial(n)
            print(f"Result: {result}")
        
        elif choice == "9":
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            bmi, category = calculate_bmi(weight, height)
            print(f"BMI: {bmi:.2f}")
            print(f"Category: {category}")
        
        elif choice == "10":
            area_calculator()
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


