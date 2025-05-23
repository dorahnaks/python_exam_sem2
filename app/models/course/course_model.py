# Import statements
from datetime import datetime
from app.extensions import db
from app.models.program.program_model import Program

class Course(db.Model):
    __tablename__ = 'course' # Giving a table name
    
    # Creating columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    #foreign key
    program_id = db.Column(db.Integer, db.ForeignKey(Program.id), nullable=True)
    
    # # # Relationship to Program
    # program = db.relationship('Program', back_populates='course')

    
