from email.policy import default
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

with app.app_context():
    User

    
    @app.route('/')
    def start_page():
        return render_template('index.html')


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.db'
#
#db = SQLAlchemy(app)

#class Login(db.Model):
 #   id = db.Column(db.Integer, primary_key=true)
  #  user = db.Column(db.string(200), nullable=true)
   # content = db.Column(db.string(500), nullable=true)
    #created_at = db.Column(db.DateTime(), default=datetime.utcnow)

#@app.route('/')
#def start_page():
#    return "<h1> Hello World </h1>"

if __name__ == '__main__':
    app.run(debug=True)
