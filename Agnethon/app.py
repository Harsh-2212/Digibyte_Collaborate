from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_mail import Mail, Message
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

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

@app.route("/" ,methods=['GET','POST']) 
def hello_world():
    selected_button = request.form.get('redirect_button')

    if selected_button == 'login':
        return redirect(url_for('loginevent'))
    # elif selected_button == 'login':
    #     return redirect(url_for('login'))
    # elif selected_button == 'login_incharge':
    #     return redirect(url_for('incharge_login'))
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

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():    
    selected_button = request.form.get('dash.html')

@app.route("/alogin", methods=['GET','POST'])
def loginevent():    
    selected_button = request.form.get('login')


    if selected_button == 'Login':
        return redirect(url_for('hostaevent'))
        # username = request.form.get['username']
        # password = request.form.get['password']
        # user = User.query.filter_by(username=username, password=password).first()
        # db.session.add(user)
        # db.session.commit()

        # host = User.query.all()
        # if user:
        #     session['logged_in'] = True
        #     session['username'] = username
        #     return redirect(url_for('hello_world'),host=host)
        # else:
        #     return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route("/incharge_dashboard",methods=[ "GET","POST"])
@app.route("/email",methods=[ "GET","POST"])
# @app.route("/",methods=[ "GET","POST"])
def incharge_dashboard():
    # if request.method == 'POST':
    #     msg = Message("Hey",sender='noreply@demo.com',recipients=['landeomkar133@gmail.com'])
    #     msg.body = "Hey your form has been approved"
    #     mail.send(msg)
    organizer = Admin.query.all()
    return render_template("incharge_dashboard.html", organizer=organizer)

@app.route("/approve",methods=[ "GET","POST"])
def approve():
    if request.method == 'POST':
        msg = Message("Hey",sender='noreply@demo.com',recipients=['landeomkar133@gmail.com'])
        msg.body = "Hey your form has been approved"
        mail.send(msg)
    return redirect(url_for('incharge_dashboard'))

@app.route("/reject",methods=[ "GET","POST"])
def reject():
    if request.method == 'POST':
        msg = Message("Hey",sender='noreply@demo.com',recipients=['landeomkar133@gmail.com'])
        msg.body = "Hey your form has been Rejected"
        mail.send(msg)
    return redirect(url_for('incharge_dashboard'))

if __name__ == '__main__':
    app.run(debug=True,port=8000)
