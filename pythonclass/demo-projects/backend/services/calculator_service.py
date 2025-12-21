"""
Calculator Service - Business logic for calculator operations
"""

import math
from datetime import datetime

class CalculatorService:
    """Service class for all calculator operations"""
    
    def __init__(self):
        self.history = []
    
    def basic_operation(self, num1, num2, operation):
        """Perform basic arithmetic operations"""
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else None
        }
        
        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")
        
        if operation == 'divide' and num2 == 0:
            raise ValueError("Cannot divide by zero")
        
        result = operations[operation](num1, num2)
        
        # Save to history
        self.add_to_history({
            'operation': operation,
            'num1': num1,
            'num2': num2,
            'result': result,
            'timestamp': datetime.now().isoformat()
        })
        
        return result
    
    def advanced_operation(self, operation, num1, num2=None):
        """Perform advanced mathematical operations"""
        try:
            if operation == 'power':
                if num2 is None:
                    raise ValueError("Power operation requires two numbers")
                result = num1 ** num2
            
            elif operation == 'sqrt':
                if num1 < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                result = math.sqrt(num1)
            
            elif operation == 'factorial':
                if num1 < 0 or not num1.is_integer():
                    raise ValueError("Factorial requires non-negative integer")
                result = math.factorial(int(num1))
            
            elif operation == 'percentage':
                if num2 is None:
                    raise ValueError("Percentage operation requires two numbers")
                result = (num1 / 100) * num2
            
            elif operation == 'log':
                if num1 <= 0:
                    raise ValueError("Logarithm requires positive number")
                result = math.log10(num1)
            
            elif operation == 'ln':
                if num1 <= 0:
                    raise ValueError("Natural logarithm requires positive number")
                result = math.log(num1)
            
            elif operation == 'sin':
                result = math.sin(math.radians(num1))
            
            elif operation == 'cos':
                result = math.cos(math.radians(num1))
            
            elif operation == 'tan':
                result = math.tan(math.radians(num1))
            
            else:
                raise ValueError(f"Unknown operation: {operation}")
            
            # Save to history
            self.add_to_history({
                'operation': operation,
                'num1': num1,
                'num2': num2,
                'result': result,
                'timestamp': datetime.now().isoformat()
            })
            
            return result
        
        except Exception as e:
            raise ValueError(f"Calculation error: {str(e)}")
    
    def get_bmi_category(self, bmi):
        """Get BMI category based on BMI value"""
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal weight'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
    
    def circle_area(self, radius):
        """Calculate area of circle"""
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (radius ** 2)
    
    def rectangle_area(self, width, height):
        """Calculate area of rectangle"""
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        return width * height
    
    def triangle_area(self, base, height):
        """Calculate area of triangle"""
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height
    
    def add_to_history(self, calculation):
        """Add calculation to history"""
        self.history.append(calculation)
        # Keep only last 100 calculations
        if len(self.history) > 100:
            self.history = self.history[-100:]
    
    def get_history(self, limit=50):
        """Get calculation history"""
        return self.history[-limit:]
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
