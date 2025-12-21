"""
Demo Project 6: Student Management System (OOP)
Part 1: Python Fundamentals - Hour 9
Difficulty: ⭐⭐⭐ Advanced

Features:
- Student class with enrollment
- Course class with capacity limits
- Add students to courses
- Calculate GPA
- Generate transcripts
- Class statistics
"""

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = {}  # {course_name: grade}
    
    def enroll(self, course_name):
        """Enroll student in a course"""
        if course_name not in self.courses:
            self.courses[course_name] = None
            return True
        return False
    
    def add_grade(self, course_name, grade):
        """Add grade for a course"""
        if course_name in self.courses:
            self.courses[course_name] = grade
            return True
        return False
    
    def calculate_gpa(self):
        """Calculate GPA"""
        grades = [g for g in self.courses.values() if g is not None]
        if not grades:
            return 0.0
        
        # Convert letter grades to points
        grade_points = {
            'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0
        }
        
        total_points = sum(grade_points.get(g.upper(), 0) for g in grades)
        return total_points / len(grades)
    
    def get_transcript(self):
        """Generate transcript"""
        transcript = f"\n{'='*50}\n"
        transcript += f"TRANSCRIPT FOR {self.name.upper()}\n"
        transcript += f"Student ID: {self.student_id}\n"
        transcript += f"{'='*50}\n"
        transcript += f"{'Course':<30} {'Grade':<10}\n"
        transcript += f"{'-'*50}\n"
        
        for course, grade in self.courses.items():
            grade_display = grade if grade else "In Progress"
            transcript += f"{course:<30} {grade_display:<10}\n"
        
        transcript += f"{'-'*50}\n"
        transcript += f"GPA: {self.calculate_gpa():.2f}\n"
        transcript += f"{'='*50}\n"
        
        return transcript
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name}, GPA: {self.calculate_gpa():.2f})"


class Course:
    def __init__(self, course_name, capacity=30):
        self.course_name = course_name
        self.capacity = capacity
        self.students = []
    
    def add_student(self, student):
        """Add student to course"""
        if len(self.students) < self.capacity:
            if student not in self.students:
                self.students.append(student)
                student.enroll(self.course_name)
                return True
        return False
    
    def get_average_grade(self):
        """Calculate average grade for course"""
        grades = []
        for student in self.students:
            if self.course_name in student.courses:
                grade = student.courses[self.course_name]
                if grade:
                    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
                    grades.append(grade_points.get(grade.upper(), 0))
        
        if not grades:
            return 0.0
        return sum(grades) / len(grades)
    
    def get_statistics(self):
        """Get course statistics"""
        enrolled = len(self.students)
        available = self.capacity - enrolled
        
        return {
            'course_name': self.course_name,
            'enrolled': enrolled,
            'capacity': self.capacity,
            'available': available,
            'average_grade': self.get_average_grade()
        }
    
    def __str__(self):
        return f"Course({self.course_name}, {len(self.students)}/{self.capacity})"


class StudentSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_student(self, student_id, name, email):
        """Add a new student"""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, email)
            print(f"✅ Student added: {name}")
            return True
        print(f"❌ Student {student_id} already exists!")
        return False
    
    def create_course(self, course_name, capacity=30):
        """Create a new course"""
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name, capacity)
            print(f"✅ Course created: {course_name}")
            return True
        print(f"❌ Course {course_name} already exists!")
        return False
    
    def enroll_student(self, student_id, course_name):
        """Enroll student in course"""
        if student_id in self.students and course_name in self.courses:
            student = self.students[student_id]
            course = self.courses[course_name]
            if course.add_student(student):
                print(f"✅ {student.name} enrolled in {course_name}")
                return True
            else:
                print(f"❌ Course {course_name} is full or student already enrolled!")
        else:
            print("❌ Student or course not found!")
        return False
    
    def add_grade(self, student_id, course_name, grade):
        """Add grade for student"""
        if student_id in self.students:
            student = self.students[student_id]
            if student.add_grade(course_name, grade):
                print(f"✅ Grade added: {student.name} - {course_name}: {grade}")
                return True
        print("❌ Student not found or not enrolled in course!")
        return False
    
    def show_student_transcript(self, student_id):
        """Show student transcript"""
        if student_id in self.students:
            print(self.students[student_id].get_transcript())
        else:
            print("❌ Student not found!")
    
    def show_course_statistics(self, course_name):
        """Show course statistics"""
        if course_name in self.courses:
            stats = self.courses[course_name].get_statistics()
            print(f"\n{'='*50}")
            print(f"COURSE STATISTICS: {course_name}")
            print(f"{'='*50}")
            print(f"Enrolled: {stats['enrolled']}/{stats['capacity']}")
            print(f"Available spots: {stats['available']}")
            print(f"Average Grade: {stats['average_grade']:.2f}")
            print(f"{'='*50}\n")
        else:
            print("❌ Course not found!")


def show_menu():
    """Display menu"""
    print("\n" + "="*50)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. Create Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade")
    print("5. Show Student Transcript")
    print("6. Show Course Statistics")
    print("7. List All Students")
    print("8. List All Courses")
    print("0. Exit")
    print("="*50)


def main():
    """Main program"""
    system = StudentSystem()
    
    # Add sample data
    system.add_student("S001", "Alice Johnson", "alice@example.com")
    system.add_student("S002", "Bob Smith", "bob@example.com")
    system.create_course("Python Programming", 30)
    system.create_course("Data Structures", 25)
    
    while True:
        show_menu()
        choice = input("Enter choice (0-8): ")
        
        if choice == '0':
            print("Goodbye! 👋")
            break
        
        elif choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            system.add_student(student_id, name, email)
        
        elif choice == '2':
            course_name = input("Enter course name: ")
            try:
                capacity = int(input("Enter capacity [30]: ") or "30")
                system.create_course(course_name, capacity)
            except ValueError:
                print("❌ Invalid capacity!")
        
        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            system.enroll_student(student_id, course_name)
        
        elif choice == '4':
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade (A/B/C/D/F): ").upper()
            system.add_grade(student_id, course_name, grade)
        
        elif choice == '5':
            student_id = input("Enter student ID: ")
            system.show_student_transcript(student_id)
        
        elif choice == '6':
            course_name = input("Enter course name: ")
            system.show_course_statistics(course_name)
        
        elif choice == '7':
            print("\nAll Students:")
            for student_id, student in system.students.items():
                print(f"  {student}")
        
        elif choice == '8':
            print("\nAll Courses:")
            for course_name, course in system.courses.items():
                print(f"  {course}")
        
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()


