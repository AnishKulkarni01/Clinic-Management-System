
import email
from flask import Flask, jsonify, request
from models import db, ma, patient_schema, Patient, Doctor, doctor_schema, doctors_schema, Clinic, clinic_schema, clinics_schema
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dpqqwwnmvotenj:6c9e955e75b2989f3636188147d7d812813344250f93bb0f6d06ed4f21c05b97@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/d11t67ifq42kkv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return 'Hello World!'


@app.route('/signup/patient', methods=['POST'])
def patient_signup():
    data = request.json

    name = data['name']
    password = data['password']
    address = data['address']
    number = data['number']
    email = data['email']

    patient = Patient(name, password, address, number, email)

    db.session.add(patient)
    db.session.commit()

    return patient_schema.dump(patient)


@app.route('/login/patient', methods=['POST'])
def patient_login():
    email = request.json['email']
    patient = db.session.query(Patient).filter_by(
        email=email).first()

    res = request.json['password'] == patient.password

    return jsonify(res)


@app.route("/signup/doctor", methods=['POST'])
def doctor_signup():
    data = request.json

    name = data['name']
    password = data['password']
    type = data['type']
    available = data['available']
    clinic_id = data['clinic_id']

    doctor = Doctor(name, password, type, available, clinic_id)

    db.session.add(doctor)
    db.session.commit()

    return doctor_schema.dump(doctor)


@app.route("/login/doctor", methods=['POST'])
def doctor_login():
    name = request.json['name']
    doctor = db.session.query(Doctor).filter_by(name=name).first()

    res = request.json['password'] == doctor.password

    return jsonify(res)

@app.route("/signup/clinic", methods=["POST"])
def clinic_signup():
    data = request.json

    name = data['name']
    email = data['email']
    password = data['password']
    contact_name = data['contact_name']
    contact_number = data['contact_number']
    lat_lng = data['lat_lng']

    clinic = Clinic(name, email, password, contact_name, contact_number, lat_lng)

    db.session.add(clinic)
    db.session.commit()

    return clinic_schema.dump(clinic)

@app.route("/login/clinic", methods=["POST"])
def clinic_login():
    email = request.json

    clinic = db.session.query(Clinic).filter_by(email=email).first()

    res = request.json['password'] == clinic.password

    return res


@app.route("/clinics", methods=['GET'])
def get_all_clinics():
    all_clinics = clinics_schema.jsonify(Clinic.query.all())
    return all_clinics

@app.route("/clinic/<clinic_id>", methods=['GET'])
def get_doctors_by_clinic(clinic_id):
    doctors_in_clinic = db.session.query(Doctor).filter_by(clinic_id=clinic_id)
    return doctors_schema.jsonify(doctors_in_clinic)

@app.route("/doctors", methods=['GET'])
def get_all_doctors():
    all_doctors = doctors_schema.jsonify(Doctor.query.all())
    return all_doctors


if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 4000)), debug=True)
