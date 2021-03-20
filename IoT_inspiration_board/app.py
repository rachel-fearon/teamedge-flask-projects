from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat

sensor = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/success', methods=['GET', 'POST'])
def success(name):
    message = request.form['message']
    message = request.form['name']
    return render_template("success.html", message = message, name = message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')