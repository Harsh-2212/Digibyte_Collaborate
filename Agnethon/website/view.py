from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
from .models import Admin, User
from . import db

view = Blueprint('view',__name__)

@view.route("/" ,methods=('GET','POST')) 
def home():
    return render_template("dash.html")

@view.route("/hostaevent", methods=('GET','POST'))
def hostaevent():
    if request.method == 'POST':
        event_name = request.form.get("eventName")
        c_name = request.form.get("committee")
        v_name = request.form.get("venue")
        pr_message = request.form.get("prMessage")
        event_head = request.form.get("eventHeadName")
        event_number = int(request.form.get("eventHeadNumber"))
        president = request.form.get("presidentName")
        president_num = int(request.form.get("presidentNumber"))
        vc_president = request.form.get("vpName")
        vc_president_num = int(request.form.get("vpNumber"))
        desc = request.form.get("description")

        host = Admin(event_name=event_name,c_name=c_name,v_name=v_name,pr_message=pr_message,event_head=event_head,event_number=event_number,president=president,president_num=president_num,vc_president=vc_president,vc_president_num=vc_president_num,desc=desc)

        db.session.add(host)
        db.session.commit()

    organizer = Admin.query.all()
    return render_template("hostaevent.html", organizer=organizer)

@view.route("/schedule",methods=( "GET","POST"))
def schedule():
    organizer = Admin.query.all()
    return render_template("schedule.html", organizer=organizer)

@view.route("/email_template",methods=( "GET","POST"))
def email_template():
    if request.method == 'POST':
        subject = 'Hello from SparkEd'

        # email_content = render_template('email_template.html')
        # msg = Message(subject,sender='noreply@demo.com',recipients=('landeomkar133@gmail.com'))
        # msg.html = email_content
        # mail.send(msg)

        return 'Email sent successfully!'
    return redirect('incharge')

@view.route("/reject",methods=( "GET","POST"))
def approve():
    if request.method == 'POST':
        subject = 'Hello from SparkEd'  

        # email_content = render_template('email_template.html')
        # msg = Message(subject,sender='noreply@demo.com',recipients=('landeomkar133@gmail.com'))
        # msg.html = email_content
        # mail.send(msg)

    return 'Email sent successfully!'

@view.route("/reject",methods=( "GET","POST"))
def reject():
    if request.method == 'POST':
        subject = 'Hello from SparkEd'  

        # email_content = render_template('email_template.html')
        # msg = Message(subject,sender='noreply@demo.com',recipients=('landeomkar133@gmail.com'))
        # msg.html = email_content
        # mail.send(msg)

    return 'Email sent successfully!'

@view.route("/student_dashboard")
def student_dashboard():
    return render_template("s_dash.html")

@view.route("/incharge_dashboard")
def incharge_dashboard():
    return render_template("incharge_dashboard.html")