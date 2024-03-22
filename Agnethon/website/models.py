from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
        user_id = db.Column(db.Integer,primary_key=True)
        username = db.Column(db.String(150),nullable=False)
        password = db.Column(db.String(150),nullable=False)
        email = db.Column(db.String(150),nullable=False)

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