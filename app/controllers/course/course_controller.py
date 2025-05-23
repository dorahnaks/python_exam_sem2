from flask import Blueprint, request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from app.models.course.course_model import Course
from app.extensions import db




#course blueprint
course_bp = Blueprint('course', __name__, url_prefix='/api/v1/course')

#creating  a course
@course_bp.route('/create', methods=['POST'])
def create_course():
    data = request.get_json()
    name = data.get('name')
    code = data.get('code')


    # Checking if all required fields are filled

    if not name or not code:
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST
        
    try:
      

       #creating a new course
       new_course = Course(id=id,name=name,code=code)
       
       # saving the company to the database
       db.session.add(new_course)
       db.session.commit()



       return jsonify({
           'message': new_course.name + " has been successfully created as a new course ",
           'user': {
               'id':new_course.id,
               'name': new_course.name,
               'code': new_course.code
           }
       }),HTTP_201_CREATED

    except Exception as e:   
        db.session.rollback() 
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    