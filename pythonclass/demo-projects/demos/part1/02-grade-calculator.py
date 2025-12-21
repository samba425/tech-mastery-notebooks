"""
Demo Project 2: Grade Calculator
Part 1: Python Fundamentals - Hour 3
Difficulty: ⭐⭐ Medium

Features:
- Calculate student grades (A, B, C, D, F)
- Validate marks (0-100)
- Determine pass/fail status
- Display formatted results
"""

print("GRADE CALCULATOR")
print("=" * 40)

# Get student information
name = input("\nEnter student name: ")

try:
    marks = int(input("Enter marks (0-100): "))
    
    # Validate marks (0-100)
    if marks < 0 or marks > 100:
        print("❌ Invalid marks! Must be between 0 and 100")
    else:
        # Calculate grade
        if marks >= 90:
            grade = "A"
            remarks = "Excellent! 🌟"
        elif marks >= 80:
            grade = "B"
            remarks = "Very Good! 👍"
        elif marks >= 70:
            grade = "C"
            remarks = "Good! ✅"
        elif marks >= 60:
            grade = "D"
            remarks = "Satisfactory 📚"
        else:
            grade = "F"
            remarks = "Needs Improvement 📖"
        
        # Check if passed (>= 60)
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
        
except ValueError:
    print("❌ Error: Please enter a valid number!")
except Exception as e:
    print(f"❌ Error: {e}")


