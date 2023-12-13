from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    hours = request.form.get('hours')

    # Hier kannst du mit den Daten arbeiten, z.B. in eine Datenbank speichern

    return f'Daten empfangen: Aufgabe - {task}, Stunden - {hours}'

if __name__ == '__main__':
    app.run(debug=True)
