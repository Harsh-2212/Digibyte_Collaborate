from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import Admin, User
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        email = request.form.get('email')

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully","success")
                return redirect(url_for("view.student_dashboard"))
            else:
                flash("Incorrect Password","error")
        else:
            flash("User doesn't exist","error")

    return render_template('login.html')

@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("User already exists",'error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters","error")
        elif len(username) < 2:
            flash("Username must be greater than 2 character","error")
        elif len(password) < 2:
            flash("Password must be greater than 2 characters","error")
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Registered Successfully","success")

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"



