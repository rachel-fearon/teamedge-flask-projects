from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/success', methods=['GET', 'POST'])
def success():
    message = request.form['message']
    name = request.form['name']
    sense.show_message(message)
    sense.show_message(name)
    conn = sqlite3.connect('./static/data/inspiration.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages VALUES((?),(?))", (name, message))
    conn.commit()
    conn.close()
    return render_template('success.html', message = message, name = name)
    
@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/inspiration.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message': row[1]}
        messages.append(message)
    conn.close()
    return render_template('all.html', messages = messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 