from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "ta_clé_secrète"

products = [
    {   "id":"1",
        "image": "https://b2c-media.maxmara.com/sys-master/m0/MM/2023/1/5221073106/057/s3details/5221073106057-b-vertice_normal.jpg#product",
        "category": "Robe",
        "name": "Robe Bleu",
        "description": "La mannequin porte une taille 40 (IT) et mesure 177 cm, tour de taille de 58 cm, tour de hanches 88 cm",
        "price": "50"
    },
    {   "id":"2",
        "image": "https://tse3.mm.bing.net/th/id/OIP.h_9POf0O3QdszAiFrB0MlwHaLH?rs=1&pid=ImgDetMain&o=7&rm=3",
        "category": "Robe",
        "name": "Robe Noir",
        "description": "La mannequin porte une taille 40 (IT) et mesure 177 cm, tour de taille de 58 cm, tour de hanches 88 cm",
        "price": "35"
    }
]


@app.route("/")
def Base():
    return render_template("Base.html")


@app.route("/cart")
def Panier():
    cart = session.get("cart", {})
    cart_items = list(cart.values())
    subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    return render_template("Panier.html", cart_items=cart_items, subtotal=subtotal)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    # product_id = index dans la liste products
    if product_id < 0 or product_id >= len(products):
        return redirect(url_for("shop"))

    product = products[product_id]
    cart = session.get("cart", {})
    key = str(product_id)

    if key in cart:
        cart[key]["quantity"] += 1
    else:
        cart[key] = {
            "id":       product_id,
            "name":     product["name"],
            "category": product["category"],
            "price":    float(product["price"]),  # converti depuis string
            "image":    product["image"],
            "quantity": 1,
        }

    session["cart"] = cart
    session.modified = True
    return redirect(request.referrer or url_for("shop"))


@app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    session.modified = True
    return redirect(url_for("Panier"))


if __name__ == "__main__":
    app.run(debug=True)