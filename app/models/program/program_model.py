# Import statements
from datetime import datetime
from app.extensions import db


class Program(db.Model):
    __tablename__ = 'program'# Giving a table name
    
    # Creating columns
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    
    
    # # # Relationships
    # course = db.relationship('course', back_populates='program')
    # student = db.relationship('student', back_populates='program')

    # function that returns the program name
    def program_details(self):
        return f"The program name is {self.name}"