from flask import Flask, render_template, session, redirect, url_for, request
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Index.html" )

@app.route("/Panier")
def Panier():
    return render_template("Panier.html" )

@app.route("/shop")
def shop():
    products = loadproducts()
    return render_template("Shop.html", products=products)

def loadproducts():
    with open("database.json") as f: 
        data=json.load(f)
        return data["products"]

@app.route('/admin')
def formulaire():
    return render_template('Admin.html')

# Reçoit et traite les données du form  ulaire
@app.route('/traitement', methods=['POST'])
def traitement():
    # Récupère la donnée du champ 'nom'
    nom = request.form['Name']
    category = request.form['Category']
    description = request.form['Description']
    price = request.form['Price']
    image = request.form['Image']
    return f"Bonjour {nom},{category},{description},{price} ,données reçues avec succès !"
