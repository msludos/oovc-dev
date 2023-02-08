from flask import Flask, render_template, url_for
import os, requests

async def get_host():
    host = os.environ.get("HOST")
    return "https://OOVCbot.msludos.repl.co"

async def get_news():
    url = await get_host()+"/api/news"
    news = requests.get(url).json()
    r = []

    for n in news:
        if n["id"] > 1250:
            r.append(n)

    return r

app = Flask(__name__)


@app.route('/')
async def index():
    return render_template("index.html")

@app.route('/map')
async def map():
    return render_template("map/index.html")

@app.route('/map/accept')
async def accept():
    return render_template("map/accept.html")

@app.route('/countries')
async def countries():
    return render_template("countries/index.html")

@app.route('/countries/<id>')
async def country(id):
    return render_template("countries/country.html", id=id)

@app.route('/faq')
async def faq():
    return render_template("faq/index.html")

@app.route('/news')
async def news():
    news_j = await get_news()
    return render_template("news/index.html", len=len(news_j), news=news_j)

@app.route('/news/<id>')
async def new(id):
    return render_template("news/news.html")


if __name__ == "__main__":
    app.run()