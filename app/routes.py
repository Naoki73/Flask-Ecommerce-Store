# - A route that shows a list of all available products
# - When you click on a product it should be able to link to a route which shows a single product (with the information of the product you just clicked)
# - A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
# - Add a route that, when clicked handles functionality that removes all items from your cart one time. Also create a button that, when pressed, it removes that specific product object from the cart.

from flask import render_template, request, redirect, url_for, session
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        session['name'] = name
        return redirect(url_for('products'))
    return render_template('index.html')

@app.route('/allproducts')
def Show_all_products():
    name = session.get('name')
    return render_template('products.html', name=name)

@app.route('/allproducts')
def ShowAllProducts():


@app.route('/product1')
def ShowProduct1():

@app.route('/product2')
def ShowProduct2():

@app.route('/product3')
def ShowProduct3():

@app.route('/product4')
def ShowProduct4():

@app.route('/product5')
def ShowProduct5():

@app.route('/product6')
def ShowProduct6():

@app.route('/cart')
def ShowCart():
    return render_template('cart.html')

@app.route('/removefromcart')
def Remove_from_cart():
    return redirect(url_for('cart'))
#Also add a button to just remove 1 item from the cart





