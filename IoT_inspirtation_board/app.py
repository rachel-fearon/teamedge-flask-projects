from flask import Flask, render_template, redirect, url_for, request, current_app as current_app
from sense_hat import SenseHat

sensor = SenseHat()

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

sense.show_message("I'm still an egg!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')