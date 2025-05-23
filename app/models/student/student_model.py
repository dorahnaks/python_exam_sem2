# Import statements
from datetime import datetime
from app.extensions import db
from app.models.program.program_model import Program

class Student(db.Model):
    __tablename__ = 'student' # Giving a table name
    
    # Creating columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(255), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    #foreign key
    program_id = db.Column(db.Integer, db.ForeignKey(Program.id), nullable=True)
    
    # # Relationship to Program
    # program= db.relationship('program', back_populates='student')
    