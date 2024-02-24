from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
app.app_context

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/hostaevent")
def hostaevent():
    return render_template("hostaevent.html")

if __name__ == '__main__':
    app.run(debug=True)