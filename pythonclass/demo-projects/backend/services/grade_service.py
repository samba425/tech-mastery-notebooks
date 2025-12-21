"""
Grade Service - Business logic for grade calculations
"""

class GradeService:
    """Service class for grade-related operations"""
    
    def calculate_grade(self, marks):
        """
        Calculate letter grade from marks
        A: 90-100
        B: 80-89
        C: 70-79
        D: 60-69
        F: 0-59
        """
        if marks >= 90:
            return 'A'
        elif marks >= 80:
            return 'B'
        elif marks >= 70:
            return 'C'
        elif marks >= 60:
            return 'D'
        else:
            return 'F'
    
    def calculate_gpa(self, grades):
        """
        Calculate GPA from list of grades
        A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
        """
        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        
        total_points = sum(grade_points.get(grade, 0) for grade in grades)
        return round(total_points / len(grades), 2) if grades else 0.0
    
    def get_grade_statistics(self, marks_list):
        """Calculate statistics for a list of marks"""
        if not marks_list:
            return {
                'average': 0,
                'highest': 0,
                'lowest': 0,
                'pass_rate': 0
            }
        
        passed = sum(1 for marks in marks_list if marks >= 60)
        
        return {
            'average': round(sum(marks_list) / len(marks_list), 2),
            'highest': max(marks_list),
            'lowest': min(marks_list),
            'pass_rate': round((passed / len(marks_list)) * 100, 1),
            'total_students': len(marks_list),
            'passed': passed,
            'failed': len(marks_list) - passed
        }
    
    def get_percentile(self, marks, all_marks):
        """Calculate percentile rank of a student"""
        if not all_marks:
            return 0
        
        below = sum(1 for m in all_marks if m < marks)
        return round((below / len(all_marks)) * 100, 1)
