from flask import Flask, render_template, url_for
import os, requests

def get_host():
    host = os.environ.get("HOST")

def get_token():
    api = os.environ.get("API")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", host=get_host())

@app.route('/map')
def map():
    return render_template("map/index.html")

@app.route('/map/accept')
def accept():
    return render_template("map/accept.html")

@app.route('/countries')
def countries():
    return render_template("countries/index.html")

@app.route('/countries/<id>')
def country(id):
    return render_template("countries/country.html", id=id)

@app.route('/faq')
def faq():
    return render_template("faq/index.html")

@app.route('/news')
def news():
    params = (
        ('v', '5.107'),
        ('access_token', get_token()),
        ('owner_id', "")
    )
    response = requests.get('https://api.vk.com/method/wall.get?', params=params) 
    return render_template("news/index.html")

@app.route('/news/<id>')
def new(id):
    return render_template("news/news.html")


if __name__ == "__main__":
    app.run()