# - A route that shows a list of all available products
# - When you click on a product it should be able to link to a route which shows a single product (with the information of the product you just clicked)
# - A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
# - Add a route that, when clicked handles functionality that removes all items from your cart one time. Also create a button that, when pressed, it removes that specific product object from the cart.

from flask import render_template, request, redirect, url_for, session, flash
from app import app

app.secret_key = 'random_secret_key'

products = [
    {'id': 1, 'name': 'iPhone 14', 'price': 999.99,
        'img': '/static/images/iphone14.jpg'},
    {'id': 2, 'name': "Keyboard", 'price': 69.99,
        'img': '/static/images/keyboard.jpg'},
    {'id': 3, 'name': 'Headphones', 'price': 79.99,
        'img': '/static/images/headphones.jpg'},
    {'id': 4, 'name': 'Microphone', 'price': 49.99,
        'img': '/static/images/microphone.jpg'},
    {'id': 5, 'name': 'iPod', 'price': 109.99, 'img': '/static/images/ipod.jpg'},
    {'id': 6, 'name': 'TV', 'price': 9999.99, 'img': '/static/images/tv.jpg'}
]

cart = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products', methods=['GET', 'POST'])
def showproducts():
    return render_template('products.html', products=products)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def singleproduct(product_id):
    product = next(p for p in products if p['id'] == product_id)

    # If "add to cart" button is pressed
    if request.method == 'POST':
        # adds to cart list
        cart.append(product)

        return redirect(url_for('cart'))

    return render_template('product.html', product=product)


@app.route('/add_to_cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == int(product_id)), None)

    if product is None:
        flash('Product not found.')
        return redirect(request.referrer)

    if 'cart' not in session:
        session['cart'] = {}

    if product_id in session['cart']:
        session['cart'][product_id]['quantity'] += 1
    else:
        session['cart'][product_id] = {
            'name': product['name'],
            'price': product['price'],
            'quantity': 1
        }

    flash('Product added to cart.')

    return redirect(request.referrer)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    
    cart = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity']
                      for item in cart.values())
    
    print(cart)
    if request.method == 'POST':
        if 'remove_item' in request.form:
            product_id = request.form['remove_item']
            if product_id in cart:
                del cart[product_id]
        elif 'remove_all_items' in request.form:
            session.pop('cart', None)
            cart = {}
        session['cart'] = cart
        flash('Cart updated.')
        return redirect(url_for('cart'))
    return render_template('cart.html', cart=cart, total_price=total_price)


@app.route('/signup')
def SignUp():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')





@app.route('/remove_all_items', methods=['POST'])
def remove_all_items():
    session.pop('cart', None)
    return redirect(url_for('cart'))


@app.route('/remove_from_cart/<product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})

    if product_id in cart:
        if cart[product_id]['quantity'] > 1:
            cart[product_id]['quantity'] -= 1
        else:
            del cart[product_id]
        session['cart'] = cart
        print(f"Removed 1 item of product with ID {product_id} from cart")
    else:
        print(f"Product with ID {product_id} not found in cart")

    return redirect(url_for('cart'))


@app.route('/purchase', methods=['POST'])
def purchase():
    session.pop('cart', None)
    flash("Purchase successful!")
    return "Purchase has been made!"

