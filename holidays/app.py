from flask import Flask, render_template, json, jsonify, current_app as current_app
import requests

app = Flask(__name__)

@app.route('/nz')
def nz_holidays():
    response = requests.get('https://data.nager.at/api/v2/PublicHolidays/2021/NZ')
    data = response.json()
    return render_template('nz.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')