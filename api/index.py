from flask import Flask, render_template, url_for, request
import os, requests
from time import sleep

def get_host():
    host = os.environ.get("HOST")
    return host

def get_vcs_api():
    host = os.environ.get("VCS_API")
    return host

def get_news():
    url = get_host()+"/method/news.gets?access_token="+get_vcs_api()
    news = requests.get(url).json() 
    r = []

    for n in news:
        if n["id"] > 1249:
            r.append(n)

    return r

def get_countries():
    url = get_host()+"/method/countries.gets?access_token="+get_vcs_api()
    countries = list(requests.get(url).json()["countries"])

    return countries

def get_countriesids():
    url = get_host()+"/method/countries.ids?access_token="+get_vcs_api()
    ids = list(requests.get(url).json()["ids"])

    return ids

def get_country(id):
    url = get_host()+"/method/country.get?access_token="+get_vcs_api()+"&id="+id
    country = requests.get(url).json()

    return country

def get_geo():
    ids = requests.get("https://vcs.pythonanywhere.com/method/geo.ids?access_token="+get_vcs_api()).json()
    return ids


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/map')
def map():
    return render_template("map/index.html", ids=get_geo())

@app.route('/map/accept')
def accept():
    return render_template("map/accept.html")

@app.route('/countries')
def countries():
    return render_template("countries/index.html")

@app.route('/countries/<id>')
def country(id):
    return render_template("countries/country.html", country=get_country(id))

@app.route('/news')
def news():
    news_j = get_news()
    return render_template("news/index.html", len=len(news_j), news=news_j)

@app.route('/news/<id>')
def news_id(id):
    return render_template("news/news.html")

@app.route('/faq')
def faq():
    return render_template("faq/index.html")

@app.route('/redirect/geo')
def Rgeo():
    return requests.get("https://vcs.pythonanywhere.com/method/geo.get?id="+request.args.get("id"))

if __name__ == "__main__":
    app.run()