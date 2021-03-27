from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat

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
    return render_template('success.html', message = message, name = name)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 