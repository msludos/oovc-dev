from flask import Flask, render_template, url_for
import os, requests

def get_host():
    host = os.environ.get("HOST")
    return host

def get_news():
    url = get_host()+"/api/news"
    news = requests.get(url).json()
    r = []

    for n in news:
        if n["id"] > 1250:
            r.append(n)

    return r

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
    news_j = get_news()
    return render_template("news/index.html", len=len(news_j), news=news_j)

@app.route('/news/<id>')
def new(id):
    return render_template("news/news.html")


if __name__ == "__main__":
    app.run()