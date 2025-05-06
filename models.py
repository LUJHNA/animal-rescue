from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'animals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'very-cool-key'  # Denne skal obviously være hemmelig og "sikker"/encrypted hvis appen skulle deployes/ikke kun køres lokalt
# Secret_Key skal bruges pga. CSRF beskyttelse i Flask-WTF (som jeg har brugt til mine forms for lettere validering)

db = SQLAlchemy(app)

class Animal(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), nullable=False)
    Species = db.Column(db.String(64), nullable=False)
    Breed = db.Column(db.String(64))
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(20))
    Description = db.Column(db.Text)
    ImageUrl = db.Column(db.String(256))
    Status = db.Column(db.String(20), default='Available') 
    
    # Relation med Adopter
    AdopterId = db.Column(db.Integer, db.ForeignKey('adopter.Id'), nullable=True)
    AdoptionDate = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, name, species, breed=None, age=None, gender=None, description=None, image_url=None, status='Available'):
        super().__init__()
        self.Name = name
        self.Species = species
        self.Breed = breed
        self.Age = age
        self.Gender = gender
        self.Description = description
        self.ImageUrl = image_url
        self.Status = status

class Adopter(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(64), nullable=False)
    LastName = db.Column(db.String(64), nullable=False)
    Email = db.Column(db.String(120), nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Address = db.Column(db.String(256))
    ApplicationDate = db.Column(db.DateTime, default=datetime.now)
    
    # Relation med Animal
    AdoptedAnimals = db.relationship('Animal', backref='adopter')
    
    def __init__(self, first_name, last_name, email, phone, address=None):
        super().__init__()
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Phone = phone
        self.Address = address