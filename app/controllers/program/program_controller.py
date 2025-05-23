from flask import Blueprint, request, jsonify # Importing the Blueprint and request and jsonify classes from the flask module
from app.status_codes import (HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR,                          
                              HTTP_201_CREATED, HTTP_200_OK , HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND)  # Importing the HTTP status codes from the status_codes module
from app.extensions import db  # Importing the db object from the extensions module
from app.models.program.program_model import Program  # Importing the Program class from the program_model module

# Creating a Blueprint instance
program_bp = Blueprint('program', __name__, url_prefix='/api/v1/program')  

#Registering new product
@program_bp.route('/register', methods=['POST'])  # Defining a route for product registration
def create_program():
    data = request.json  
    name = data.get('name')  
    description = data.get('description')
    
    
    # Checking if all required fields are filled
    if not name or not description: 
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST
    
    # the try..except for handling errors
    try:      
        # Creating a new program instance 
        new_program = Program(
            id=id, name=name, description=description
        )
        
        db.session.add(new_program) # adding new program to database
        db.session.commit() # saving change to the database
  
        return jsonify({
            'message': new_program.name + ' has been created successfully',
            'author': {
                'id': new_program.id,
                'name': new_program.name,
                'description': new_program.last_name,
                'created_at': new_program.created_at
            }
    
            }), HTTP_201_CREATED
        
        
    except Exception as e:
        db.session.rollback() # db.session.rollback() is called to undo any changes made during the transaction in case of an error
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
    
@program_bp.route('/delete', methods=['DELETE'])
def delete_program(id):
    program = program.query.get(id)
    
    if not id:
        return jsonify({'message': 'Enter id'}), HTTP_404_NOT_FOUND
    
    try:
        data = request.get_json() # Extracting the JSON data    
        name = data.get('name')
        description = data.get('description')        

        program.name =  name
        program.description = description

        db.session.commit() # Committing the changes to the database
        
        return jsonify ({
            'message' : 'program updated successfully'
            'program' : {
                'name' : program.name
                'description' : prrogram.description
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR













