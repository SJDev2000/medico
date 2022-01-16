from asyncio import events
from calendar import day_abbr
from ctypes.wintypes import MSG
from sqlalchemy.orm import backref
from flaskproject import db

class Patient(db.Model):
    __tablename__="patient"
    id = db.Column(db.Integer, primary_key=True)
    prescriptions = db.relationship('Prescription',backref='patient',lazy="dynamic")
    fullname = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120), unique = False)
    age = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(20), nullable = True)
    address = db.Column(db.String(120), nullable = True)
    phone = db.Column(db.String(15), nullable = True)

    # Deprecated attributes
    image = db.Column(db.Text, nullable = True)
    filename = db.Column(db.Text, nullable = True)
    mimetype = db.Column(db.Text, nullable = True)
    
    def __repr__(self):
        return f"Patient('{self.fullname}', '{self.email}')" 

class Doctor(db.Model):
    __tablename__="doctor"
    id = db.Column(db.Integer, primary_key=True)
    prescriptions = db.relationship('Prescription',backref='doctor',lazy="dynamic")
    fullname = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120), unique = False)
    image = db.Column(db.String(1000), nullable = True)
    desc = db.Column(db.String(200), nullable = True)
    
    def __repr__(self):
        return f"Doctor('{self.fullname}', '{self.email}')" 