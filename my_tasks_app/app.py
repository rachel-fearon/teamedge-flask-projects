from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3
from flask_apscheduler import APScheduler

sense = SenseHat()
app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()



@app.route('/', methods=['GET', 'POST'])
def index():
    task = request.form['task']
    date = request.form['date']
    sense.show_message(task)
    sense.show_message(date)
    conn = sqlite3.connect('./static/data/my_tasks_app.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks VALUES((?),(?))", (task, date))
    conn.commit()
    conn.close()
    return render_template ('index.html', task = task, date = date)

@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/my_tasks_app.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * from tasks")
    for row in rows:
        task = {'task': row[0], 'date': row[1]}
        tasks.append(task)
    conn.close()
    return render_template('all.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 