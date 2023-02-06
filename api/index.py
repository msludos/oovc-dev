from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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
    return render_template("news/index.html")

@app.route('/news/<id>')
def new(id):
    return render_template("news/news.html")

@app.route('/host')
def host():
    return os.environ.get("HOST")


if __name__ == "__main__":
    app.run()