from flask import Flask, render_template, redirect, url_for, request, jsonify
import requests

app = Flask(__name__)

# landing page
# backend_url = 'http://localhost:4000'
backend_url = 'https://electronic-health-requirement.herokuapp.com'


@app.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('landing-page.html')

# choose clinic
@app.route('/patient/appointment/booking', methods=['GET', 'POST'])
def clinicChoosing():
    req = requests.get(f"{backend_url}/clinics")
    res = req.json()
    return render_template('clinic-choosing.html', data=res)

#choose doctor
@app.route('/patient/appointment/booking/<clinicid>', methods=['GET', 'POST'])
def doctorChoosing(clinicid):
    req = requests.get(f"{backend_url}/clinic/{clinicid}")
    res = req.json()
    return render_template('doctor-choosing.html', data=res)

# login page


@app.route('/login/<role>', methods=['GET', 'POST'])
def loginPage(role):
    if request.method == "POST":
        if(role == 'Patient'):
            reqBody = {
                "email": request.form['username'],
                "password": request.form['password']
            }
            req = requests.post(
                f"{backend_url}/login/patient", json=reqBody,
                headers={'Content-Type': 'application/json'})
            res = req.json()
            return (str(res))
        elif(role == 'Doctor'):
            reqBody = {
                "name": request.form['username'],
                "password": request.form['password']
            }
            req = requests.post(
                f"{backend_url}/login/doctor", json=reqBody,
                headers={'Content-Type': 'application/json'})
            res = req.json()
            return (str(res))
        elif(role == 'Clinic'):
            reqBody = {
                "email": request.form['username'],
                "password": request.form['password']
            }
            req = requests.post(
                f"{backend_url}/login/clinic", json=reqBody,
                headers={'Content-Type': 'application/json'})
            res = req.json()
            return (str(res))
    else:
        return render_template('login-template.html', role=role)
    return render_template('login-template.html', role=role)

# clinic signup


@app.route('/clinic/signup', methods=['GET', 'POST'])
def signupClinic():
    if request.method == "POST":
        reqBody = {
            "name": request.form['name'],
            "email": request.form['email'],
            "password": request.form['password'],
            "contact_name": request.form['contact_name'],
            "contact_number": request.form['contact_number'],
            "lat_lng": request.form['lat_lng']

        }
        req = requests.post(
            f"{backend_url}/signup/clinic", json=reqBody,
            headers={'Content-Type': 'application/json'})
        res = req.json()
        return (res)
    else:
        return render_template('clinic-signup.html')

# patient signup


@app.route('/patient/signup', methods=['GET', 'POST'])
def signupPatient():
    if request.method == "POST":
        reqBody = {
            "name": request.form['name'],
            "password": request.form['password'],
            "address": request.form['address'],
            "number": request.form['contact'],
            "email": request.form['email']
        }
        req = requests.post(
            f"{backend_url}/signup/patient", json=reqBody,
            headers={'Content-Type': 'application/json'})
        res = req.json()
        return (res)
    else:
        return render_template('patient-signup.html')

# doctor signup


@app.route('/doctor/signup', methods=['GET', 'POST'])
def signupDoctor():
    if request.method == "POST":
        reqBody = {
            "name": request.form['name'],
            "password": request.form['password'],
            "type": request.form['type'],
            "available": (str(request.form['fromtime'])+"-"+str(request.form['totime'])),
            "clinic_id": request.form['clinic_id']
        }
        req = requests.post(
            f"{backend_url}/signup/doctor", json=reqBody,
            headers={'Content-Type': 'application/json'})
        res = req.json()
        return (res)
    else:
        return render_template('doctor-signup.html')


if __name__ == '__main__':
    app.run(debug=True)
