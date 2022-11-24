# API Documentation

## Login API

### 1. Patient Signup
Request : `POST /signup/patient`

Request Body Content : JSON
```json
{
    "name": "patient_name",
    "password": "patient_password",
    "address": "patient_address",
    "number": "patient_phone_number",
    "email": "patient_email"
}
```

Response : JSON
```json
{
    "id": 123, //Auto generated Integer as ID
    "name": "patient_name",
    "password": "patient_password",
    "address": "patient_address",
    "number": "patient_phone_number",
    "email": "patient_email"
}
```
### 2. Doctor Signup
Request : `POST /signup/doctor`

Request Body Content : JSON
```json
{
    "name": "doctor_name",
    "password": "doctor_password",
    "type": "doctor_type", // Type of doctor. Ex. Cardiologist, Surgeon, etc.
    "available": "doctor_available_timings", // In the form "startHour-endHour" Ex. "10-17"
    "clinic_id": "clinic_id" // The clinic the doctor is associated with
}
```

Response : JSON
```json
{
    "id": 123, // Auto Generated Integer as ID
    "name": "doctor_name",
    "password": "doctor_password",
    "type": "doctor_type", // Type of doctor. Ex. Cardiologist, Surgeon, etc.
    "available": "doctor_available_timings", // In the form "startHour-endHour" Ex. "10-17"
    "clinic_id": "clinic_id" // The clinic the doctor is associated with
}
```
### 3. Clinic Signup
Request : `POST /signup/clinic`

Request Body Content: JSON
```json
{
    "name": "clinic_name",
    "email": "clinic_email",
    "password": "clinic_password",
    "contact_name": "contact_name",// The name of the person to be contacted on behalf of the clinic
    "contact_number": "contact_number", // Contact number of the contact_person
    "lat_lng": "lat-lng", // The latitude and longitude of the clinic separated by "-"
}
```

Response: JSON
```json
{
    "id": 123, // Auto Generated Integer as ID
    "name": "clinic_name",
    "email": "clinic_email",
    "password": "clinic_password",
    "contact_name": "contact_name",// The name of the person to be contacted on behalf of the clinic
    "contact_number": "contact_number", // Contact number of the contact_person
    "lat_lng": "lat-lng", // The latitude and longitude of the clinic separated by "-"
}
```
### 4. Patient Login
Request: `POST /login/patient`

Request Body: JSON
```json
{
    "email": "patient_email",
    "password": "patient_password"
}
```

Response: JSON `true` if username and password match else `false`

### 5. Doctor Login
Request: `POST /login/doctor`

Request Body: JSON
```json
{
    "name": "doctor_name",
    "password": "doctor_password"
}
```
Response: JSON `true` if username and password match else `false`
### 6. Clinic Login
Request: `POST /login/clinic`

Request Body: JSON
```json
{
    "email": "clinic_email",
    "password": "clinic_password"
}
```
Response: JSON `true` if username and password match else `false`

## Clinics API

### 1. Get All Clinics

Request: `GET /clinics`

Response: JSON
```json
[
    {
        "id": 123, // Auto Generated Integer as ID
        "name": "clinic_name",
        "email": "clinic_email",
        "password": "clinic_password",
        "contact_name": "contact_name",// The name of the person to be contacted on behalf of the clinic
        "contact_number": "contact_number", // Contact number of the contact_person
        "lat_lng": "lat-lng", // The latitude and longitude of the clinic separated by "-"
    },
    {...},
    {...},
    .
    .
]
```

### 2. Get Doctors In Clinic

Request: `GET /clinic/<clinic_id>`

Response: JSON
```json
[
    {
        "id": 123, // Auto Generated Integer as ID
        "name": "doctor_name",
        "password": "doctor_password",
        "type": "doctor_type", // Type of doctor. Ex. Cardiologist, Surgeon, etc.
        "available": "doctor_available_timings", // In the form "startHour-endHour" Ex. "10-17"
        "clinic_id": "clinic_id" // The clinic the doctor is associated with
    },
    {...},
    {...},
    .
    .
]
```

## Doctors API

### 1. Get All Doctors

Request: `GET /doctors`

Request Body: JSON
```json
[
    {
        "id": 123, // Auto Generated Integer as ID
        "name": "doctor_name",
        "password": "doctor_password",
        "type": "doctor_type", // Type of doctor. Ex. Cardiologist, Surgeon, etc.
        "available": "doctor_available_timings", // In the form "startHour-endHour" Ex. "10-17"
        "clinic_id": "clinic_id" // The clinic the doctor is associated with
    },
    {...},
    {...},
    .
    .
]
```