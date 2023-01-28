# - A route that shows a list of all available products
# - When you click on a product it should be able to link to a route which shows a single product (with the information of the product you just clicked)
# - A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
# - Add a route that, when clicked handles functionality that removes all items from your cart one time. Also create a button that, when pressed, it removes that specific product object from the cart.

from flask import render_template, request, redirect, url_for, session
from app import app

app.secret_key = 'random_secret_key'

products = [
    {'id': 1, 'name': 'Product 1', 'price':9.99},
    {'id': 2, 'name': 'Product 2', 'price':9.99},
    {'id': 3, 'name': 'Product 3', 'price':9.99}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        session['name'] = name
        return redirect(url_for('products'))
    return render_template('index.html', product=products)

@app.route('/allproducts')
def Show_all_products():
    name = session.get('name')
    return render_template('products.html', name=name)

@app.route('/product/<int:product_id>')
def singleproduct(product_id):
    product = next(p for p in products if p['id'] == product_id)
    return render_template('product.html', product=product)

def add_to_cart():
    if 'username' not in session:
        return "You must be logged in to add items to your cart"

    product_id = request.form['product_id']
    product = next(p for p in products if p['id'] == int(product_id))

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(product)

    return "Product added to cart"


@app.route('/cart')
def ShowCart():
    if 'cart' not in session:
        return "Your cart is empty"
    
    total_price = sum(item['price'] for item in session['cart'])

    return render_template('cart.html', cart=session['cart'], total_price = total_price)

@app.route('/remove_all_items')
def remove_all_items():
    session.pop('cart', None)
    return redirect(url_for('cart'))

@app.route('/remove_item/<int:product_id>')
def remove_item(product_id):
    cart = session['cart']
    session['cart'] = [item for item in cart if item['id'] != product_id]
    return redirect(url_for('cart'))






