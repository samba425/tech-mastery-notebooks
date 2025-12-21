"""
Demo Project 1: Simple Calculator
Part 1: Python Fundamentals - Hour 2
Difficulty: ⭐ Easy

Features:
- Basic arithmetic operations (+, -, *, /)
- User input handling
- Error handling for division by zero
"""

print("=" * 40)
print("SIMPLE CALCULATOR")
print("=" * 40)

# Get two numbers from user
try:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform all operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Handle division by zero
    if num2 == 0:
        division = "Error: Cannot divide by zero!"
    else:
        division = num1 / num2
    
    # Display results
    print("\n" + "=" * 40)
    print("RESULTS:")
    print("=" * 40)
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} × {num2} = {multiplication}")
    if isinstance(division, str):
        print(division)
    else:
        print(f"{num1} ÷ {num2} = {division:.2f}")
    print("=" * 40)
    
except ValueError:
    print("❌ Error: Please enter valid numbers!")
except Exception as e:
    print(f"❌ Error: {e}")


