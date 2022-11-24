from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Clinic(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))
    contact_name = db.Column('contact_name', db.String(100))
    contact_number = db.Column('contact_number', db.String(100))
    lat_lng = db.Column('lat_lng', db.String(100))

    def __init__(self, name, email, password, contact_name, contact_number, lat_lng):
        self.name = name
        self.email = email
        self.password = password
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.lat_lng = lat_lng

class ClinicSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password','contact_name','contact_number', 'lat_lng')


class Patient(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100))
    password = db.Column('password', db.String(100))
    address = db.Column('address', db.String(100))
    number = db.Column('number', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, password, address="", number="", email=""):
        self.name = name
        self.password = password
        self.address = address
        self.number = number
        self.email = email


class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password', 'address', 'number', 'email')


class Doctor(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100))
    password = db.Column('password', db.String(100))
    type = db.Column('type', db.String(100))
    available = db.Column('available', db.String(100))
    clinic_id = db.Column('clinic_id', db.Integer,db.ForeignKey('clinic.id'))

    def __init__(self, name, password, type, available, clinic_id):
        self.name = name
        self.password = password
        self.type = type
        self.available = available
        self.clinic_id = clinic_id


class DoctorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password', 'type', 'available', 'clinic_id')


class Appointment(db.Model):
    id = db.Column('id', db.String(100), primary_key=True)
    doctor_id = db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column('patient_id', db.Integer,db.ForeignKey('patient.id'))
    appointment_time = db.Column('time', db.String(100))


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)

clinic_schema = ClinicSchema()
clinics_schema = ClinicSchema(many=True)
