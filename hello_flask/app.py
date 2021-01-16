from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
    json_info = json.load(raw_json)
    

@app.route('/')
def index():
    name = 'Rachel'
    friends = ['Zoe', 'Jill', 'Taylor', 'Yara', 'Gaby', 'Ajani']
    return render_template('index.html', greeting=name, friends=friends)

@app.route('/about')
def about ():
    return '<h1>About</h1><p>some other content</p>'

@app.route('/nasa')
def show_nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html', data=data)

@app.route('/album', methods=['GET'])
def album_json():
    album_info = os.path.join(app.static_folder, 'data', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

@app.route('/movies')
def all_movies():
        return jsonify(json_info)

@app.route('/movies/search_title', methods=['GET'])
def search_title():
    results = []
    if 'title' in request.args:
        title = request.args['title']

        for movie in json_info:
            if title in movie['title']:
                results.append(movie)

    if len(results) < 1:
        return "No results found"
    return render_template("movies.html", results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')