from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'thisisasecretkey'
    db.init_app(app)
    

    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USERNAME'] = 'landeomkar133@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'fmuj wlxy ndoy huly'
    # # app.config['MAIL_PASSWORD'] = 'Lande@0305'
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False

    # mail = Mail(app)
    with app.app_context():

        from .view import view
        from .auth import auth

        app.register_blueprint(view, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')

        from .models import Admin, User
        
        create_database(app)

        return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print("Database created")