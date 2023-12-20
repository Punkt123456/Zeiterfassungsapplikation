from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# DB-Konfig
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB-Modell für User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15))  # optional

# Beispielbenutzer in die DB einfügen
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(email='admin@example.com').first():
            hashed_password = generate_password_hash('admin_password', method='pbkdf2:sha256')
            admin_user = User(email='admin@example.com', password_hash=hashed_password, name='Admin')
            db.session.add(admin_user)
            db.session.commit()

# Landingpage
@app.route('/')
def index():
    return render_template('index.html')

# Login Logik
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user is not None and check_password_hash(user.password_hash, password):
        print("Anmeldung erfolgreich")
        return redirect(url_for('dashboard', email=email))
    else:
        print("Falsche E-Mail oder Passwort")
        if user is not None:
            print("Passwort-Hash aus der Datenbank:", user.password_hash)
        return 'Falsche E-Mail oder Passwort'


# Registrierungsseite link
@app.route('/registrierung')
def registrierung():
    return render_template('Registrierung.html')
# Passwort vergessen Seite
@app.route('/passwort')
def passwort():
    return render_template('passwort.html')
# Dashboard link
@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

# Registrierungsformular Verarbeitungslogik
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    phone = request.form.get('phone')

    # E-Mail bereits vorhanden
    if User.query.filter_by(email=email).first():
        return 'E-Mail bereits registriert'

    # Hash des Passworts und User in die DB einfügen
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(email=email, password_hash=hashed_password, name=name, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return 'Registrierung erfolgreich'

if __name__ == '__main__':
    app.run(debug=True)
