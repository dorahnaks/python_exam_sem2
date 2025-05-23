from flask import Blueprint, request, jsonify # Importing the Blueprint and request and jsonify classes from the flask module
from app.status_codes import (HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR,                          
                              HTTP_201_CREATED, HTTP_200_OK , HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND)  # Importing the HTTP status codes from the status_codes module
from app.extensions import db  # Importing the db object from the extensions module
from app.models.student.student_model import Student # Importing the Student class from the student_model module

# Creating a Blueprint instance
student_bp = Blueprint('student', __name__, url_prefix='/api/v1/student')  

#Registering new product
@student_bp.route('/register', methods=['POST'])  # Defining a route for student registration
def create_student():
    data = request.json  
    name = data.get('name')  
    address = data.get('address')
    contact = data.get('contact')
    age = data.get('age')
    
    
    # Checking if all required fields are filled
    if not name or not address or not contact: 
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST
    
    # the try..except for handling errors
    try:      
        # Creating a new student instance 
        new_student= Student(
            id=id, name=name, address=address, contact=contact, age=age
        )
        
        db.session.add(new_student) # adding new student to database
        db.session.commit() # saving change to the database
  
        return jsonify({
            'message': new_student.name + ' has been created successfully',
            'student': {
                'id': new_student.id,
                'name': new_student.name,
                'address': new_student.address,
                'contact': new_student.contact,
                'age': new_student.age,
                'created_at': new_student.created_at
            }
    
            }), HTTP_201_CREATED
        
        
    except Exception as e:
        db.session.rollback() # db.session.rollback() is called to undo any changes made during the transaction in case of an error
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR