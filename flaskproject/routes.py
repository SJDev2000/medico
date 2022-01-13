from flaskproject import app, db
from flask import request, session, url_for, make_response
from flask.json import jsonify
from werkzeug.utils import redirect
import hashlib
from datetime import datetime, timedelta
import jwt
from flaskproject.models import Patient, Doctor
from flask.templating import render_template


# Home Page route

@app.route('/home')
def home():
    return render_template('homePage.html')

# sign up for patient

@app.route('/signUp')
def signUp():
    return render_template('register.html')

@app.route('/signIn')
def signIn():
    return render_template('login.html')


# Patient Register

@app.route('/createPatient', methods= ["POST", "GET"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest() 

        # register the new patient to the database
        new_user = Patient(fullname = fullname, email = email, password = hashedPassword)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('signIn')) #function name and urel_for name should be same
    return {"message": "success"}

# Patient Login
@app.route('/patientLogin', methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = Patient.query.filter_by(email = email).first()
        if result == None or hashedPassword != result.password:
            return "Invalid email or password"
        token = jwt.encode({'user':result.email, 'exp': datetime.utcnow()+timedelta(minutes=15)}, app.config['SECRET_KEY'])
        session["jwt"] = token
        return redirect(url_for('patientDashboard'))
    return jsonify({"jwt": "token"}) 
   