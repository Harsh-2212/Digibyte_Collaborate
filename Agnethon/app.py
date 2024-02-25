from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.security import check_password_hash
from flask_mail import Mail, Message
from flask_login import UserMixin

import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
app.app_context().push()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'landeomkar133@gmail.com'
app.config['MAIL_PASSWORD'] = 'fmuj wlxy ndoy huly'
# app.config['MAIL_PASSWORD'] = 'Lande@0305'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    c_name = db.Column(db.String, nullable=False)
    v_name = db.Column(db.String, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    desc = db.Column(db.String, nullable=False)
    pr_message = db.Column(db.String, nullable=False)
    event_head = db.Column(db.String, nullable=False)
    event_number = db.Column(db.Integer, nullable=False)
    president = db.Column(db.String, nullable=False)
    president_num = db.Column(db.Integer, nullable=False)
    vc_president = db.Column(db.String, nullable=False)
    vc_president_num = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

@app.route("/" ,methods=['GET','POST']) 
def home():
    return render_template("dash.html")

@app.route("/hostaevent", methods=['GET','POST'])
def hostaevent():
    if request.method == 'POST':
        event_name = request.form["eventName"]
        c_name = request.form["committee"]
        v_name = request.form["venue"]
        pr_message = request.form["prMessage"]
        event_head = request.form["eventHeadName"]
        event_number = int(request.form["eventHeadNumber"])
        president = request.form["presidentName"]
        president_num = int(request.form["presidentNumber"])
        vc_president = request.form["vpName"]
        vc_president_num = int(request.form["vpNumber"])
        desc = request.form["description"]

        adlib = Admin(event_name=event_name, c_name=c_name, v_name=v_name, pr_message=pr_message, event_head=event_head, event_number=event_number, president=president, president_num=president_num, vc_president=vc_president, vc_president_num=vc_president_num, desc=desc)
        db.session.add(adlib)
        db.session.commit()

    organizer = Admin.query.all()
    return render_template("hostaevent.html", organizer=organizer)

# @app.route("/dashboard", methods=['GET','POST'])
# def dashboard():    
#     selected_button = request.form.get('dash.html')

@app.route("/alogin", methods=['GET','POST'])
def loginevent():
    return render_template('login.html')

@app.route("/incharge_dashboard",methods=[ "GET","POST"])
def incharge_dashboard():
    organizer = Admin.query.all()
    return render_template("incharge_dashboard.html", organizer=organizer)

@app.route("/approve",methods=[ "GET","POST"])
def approve():
    if request.method == 'POST':
        subject = 'Hello from SparkEd'

        email_content = render_template('email_template.html')
        msg = Message(subject,sender='noreply@demo.com',recipients=['landeomkar133@gmail.com'])
        msg.html = email_content
        mail.send(msg)

    return 'Email sent successfully!'
    return redirect(url_for('incharge_dashboard'));

@app.route("/reject",methods=[ "GET","POST"])
def reject():
    if request.method == 'POST':
        subject = 'Hello from SparkEd'

        email_content = render_template('email_template.html')
        msg = Message(subject,sender='noreply@demo.com',recipients=['landeomkar133@gmail.com'])
        msg.html = email_content
        mail.send(msg)

    return 'Email sent successfully!'
    return redirect(url_for('incharge_dashboard'));

from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # existing_user = User.query.filter_by(username=username).first()
        # existing_email = User.query.filter_by(email=email).first()

        # if existing_user:
        #     flash('Username already exists. Please choose a different one.', 'error')
        #     return redirect(url_for('register'))
        # elif existing_email:
        #     flash('Email address is already registered.', 'error')
        #     return redirect(url_for('register'))

        # Add the new user to the database
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template("login.html")

@app.route("/student_dashboard")
def  student_dashboard():
    return render_template("s_dash.html")

@app.route("/incharge")
def  incharge():
    return render_template("incharge.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Query user from the database based on email
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            # session['user_id'] = user.id
            # session['username'] = user.username
            # session['email'] = user.email
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('loginevent'))

    return render_template("s_dash.html")
    
        



if __name__ == '__main__':
    app.run(debug=True,port=3000)
