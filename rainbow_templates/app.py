from flask import Flask, render_template, current_app as current_app

app = Flask(__name__)

@app.route('/rainbow')
def rainbow():
    colors = ['red', 'orange', 'yellow', 'blue', 'green', 'blue', 'indigo', 'violet']
    return render_template('rainbow.html', colors = colors)

@app.route('/red')
def red():
    color = 'red'
    return render_template('rainbow_templates.html', color = color)

@app.route('/orange')
def orange():
    color = 'orange'
    return render_template('rainbow_templates.html', color = color)

@app.route('/yellow')
def yellow():
    color = 'yellow'
    return render_template('rainbow_templates.html', color = color)

@app.route('/green')
def green():
   color = 'green'
   return render_template('rainbow_templates.html', color = color)

@app.route('/blue')
def blue():
    color = 'blue'
    return render_template('rainbow_templates.html', color = color)

@app.route('/indigo')
def indigo():
    color = 'indigo'
    return render_template('rainbow_templates.html', color = color)

@app.route('/violet')
def violet():
    color = 'violet'
    return render_template('rainbow_templates.html', color = color)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')