from flask import Flask, render_template, session, redirect, url_for, request
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Index.html" )


@app.route("/shop")
def shop():
    products = loadproducts()
    return render_template("Shop.html", products=products)

def loadproducts():
    with open("database.json") as f: 
        data=json.load(f)
        return data["products"]
