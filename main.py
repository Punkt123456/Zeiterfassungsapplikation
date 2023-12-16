from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# SQLite-Datenbank-Konfiguration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Datenbank-Modell für Benutzer erstellen
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # corrected column name

# Beispielbenutzer in die Datenbank einfügen (ersetzen Sie dies durch Ihre eigene Logik)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username='admin').first():
            hashed_password = generate_password_hash('admin_password', method='sha256')
            admin_user = User(username='admin', password_hash=hashed_password)
            db.session.add(admin_user)
            db.session.commit()

# Route für die Indexseite
@app.route('/')
def index():
    return render_template('index.html')

# Route für den Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        return redirect(url_for('dashboard', username=username))
    else:
        return 'Falscher Benutzername oder Passwort'

if __name__ == '__main__':
    app.run(debug=True)
