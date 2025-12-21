"""
Calculator Route - Handles all calculator-related operations
Supports: Basic, Advanced, Grade, BMI calculators
"""

from flask import Blueprint, request, jsonify
from services.calculator_service import CalculatorService
from services.grade_service import GradeService

calculator_bp = Blueprint('calculator', __name__)
calc_service = CalculatorService()
grade_service = GradeService()

@calculator_bp.route('/basic', methods=['POST'])
def basic_calculator():
    """
    Basic arithmetic calculator
    POST /api/calculator/basic
    Body: {
        "num1": 10,
        "num2": 5,
        "operation": "add"  # add, subtract, multiply, divide
    }
    """
    try:
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation', 'add')
        
        result = calc_service.basic_operation(num1, num2, operation)
        
        return jsonify({
            'success': True,
            'result': result,
            'calculation': f"{num1} {operation} {num2} = {result}"
        }), 200
    
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': 'Internal server error'}), 500


@calculator_bp.route('/advanced', methods=['POST'])
def advanced_calculator():
    """
    Advanced calculator with scientific functions
    POST /api/calculator/advanced
    Body: {
        "operation": "power",  # power, sqrt, factorial, percentage
        "num1": 2,
        "num2": 10  # optional for some operations
    }
    """
    try:
        data = request.get_json()
        operation = data.get('operation')
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        
        result = calc_service.advanced_operation(operation, num1, num2)
        
        return jsonify({
            'success': True,
            'result': result,
            'operation': operation
        }), 200
    
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@calculator_bp.route('/bmi', methods=['POST'])
def bmi_calculator():
    """
    BMI Calculator
    POST /api/calculator/bmi
    Body: {
        "weight": 70,  # in kg
        "height": 1.75  # in meters
    }
    """
    try:
        data = request.get_json()
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        
        if weight <= 0 or height <= 0:
            return jsonify({'success': False, 'error': 'Weight and height must be positive'}), 400
        
        bmi = weight / (height ** 2)
        category = calc_service.get_bmi_category(bmi)
        
        return jsonify({
            'success': True,
            'bmi': round(bmi, 2),
            'category': category,
            'weight': weight,
            'height': height
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@calculator_bp.route('/grade', methods=['POST'])
def grade_calculator():
    """
    Grade Calculator
    POST /api/calculator/grade
    Body: {
        "name": "Alice",
        "marks": 85
    }
    """
    try:
        data = request.get_json()
        name = data.get('name', 'Student')
        marks = float(data.get('marks', 0))
        
        if not 0 <= marks <= 100:
            return jsonify({'success': False, 'error': 'Marks must be between 0 and 100'}), 400
        
        grade = grade_service.calculate_grade(marks)
        status = 'Pass' if marks >= 60 else 'Fail'
        
        return jsonify({
            'success': True,
            'student': name,
            'marks': marks,
            'grade': grade,
            'status': status,
            'message': f"{name} scored {marks}% and got grade {grade}"
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@calculator_bp.route('/area', methods=['POST'])
def area_calculator():
    """
    Area Calculator for different shapes
    POST /api/calculator/area
    Body: {
        "shape": "circle",  # circle, rectangle, triangle
        "radius": 5  # or width/height/base/height based on shape
    }
    """
    try:
        data = request.get_json()
        shape = data.get('shape', '').lower()
        
        if shape == 'circle':
            radius = float(data.get('radius', 0))
            area = calc_service.circle_area(radius)
            return jsonify({
                'success': True,
                'shape': 'circle',
                'radius': radius,
                'area': round(area, 2)
            }), 200
        
        elif shape == 'rectangle':
            width = float(data.get('width', 0))
            height = float(data.get('height', 0))
            area = calc_service.rectangle_area(width, height)
            return jsonify({
                'success': True,
                'shape': 'rectangle',
                'width': width,
                'height': height,
                'area': round(area, 2)
            }), 200
        
        elif shape == 'triangle':
            base = float(data.get('base', 0))
            height = float(data.get('height', 0))
            area = calc_service.triangle_area(base, height)
            return jsonify({
                'success': True,
                'shape': 'triangle',
                'base': base,
                'height': height,
                'area': round(area, 2)
            }), 200
        
        else:
            return jsonify({'success': False, 'error': 'Invalid shape'}), 400
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@calculator_bp.route('/history', methods=['GET'])
def calculation_history():
    """
    Get calculation history
    GET /api/calculator/history
    """
    try:
        history = calc_service.get_history()
        return jsonify({
            'success': True,
            'history': history,
            'count': len(history)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@calculator_bp.route('/history', methods=['DELETE'])
def clear_history():
    """
    Clear calculation history
    DELETE /api/calculator/history
    """
    try:
        calc_service.clear_history()
        return jsonify({
            'success': True,
            'message': 'History cleared'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
