from flask import Flask, jsonify, request, url_for, send_from_directory
from flask_cors import CORS
import os

# Path steup as we have images in frontend file and app.py in Backend
current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(current_dir, '..', 'Frontend')
static_dir = os.path.join(frontend_dir, 'static')


# Configure Flask to serve static files from the Frontend/static directory
app = Flask(__name__, static_folder=static_dir)
CORS(app)

print("--- Flask Debug ---")
print(f"Serving static files from: {app.static_folder}")
print(f"Frontend directory: {frontend_dir}")
print("------------------")

# product data "list of dictionaries saved in key:value pairs"
PRODUCTS = [
    {"id": 1, "name": "Grey T-Shirt", "price": 1200, "description": "High-quality cotton t-shirt.", "category": "Apparel", "stock": 10, "image": "GreyTshirt.png"},
    {"id": 2, "name": "Blue Hoodie", "price": 1500, "description": "Comfortable hoodie for casual wear.", "category": "Apparel", "stock": 5, "image": "BlueHoddie.png"},
    {"id": 3, "name": "Slim Fit Jeans", "price": 1100, "description": "Stylish slim fit jeans.", "category": "Apparel", "stock": 25, "image": "SlimFitJeans.png"},
    {"id": 4, "name": "Casual Shirt", "price": 1200, "description": "Smart casual shirt suitable for work.", "category": "Apparel", "stock": 8, "image": "FormalShirts.png"},
    {"id": 5, "name": "Denim Jacket", "price": 2200, "description": "Classic denim jacket.", "category": "Apparel", "stock": 6, "image": "Denimjacket.png"},
    {"id": 6, "name": "Formal White Shirt", "price": 1700, "description": "Elegant white shirt for office.", "category": "Apparel", "stock": 12, "image": "FormalWhiteShirt.png"},
    {"id": 7, "name": "Polo Shirt", "price": 999, "description": "Smart casual polo shirt.", "category": "Apparel", "stock": 15, "image": "Polo.png"},
    {"id": 8, "name": "Denim Shorts", "price": 799, "description": "Comfortable denim shorts.", "category": "Apparel", "stock": 20, "image": "DenimShorts.png"},
]

# cart is a empty list , acn add as many orders as we place no limit 
# order_id starts from 1001 and incremnetrs by 1
cart = []
next_order_id = 1001

# used to locate image for the product from frontend\static\images
def map_product_to_url(product):
    
    p = product.copy()
    p['image'] = url_for('static', filename=f"images/{p['image']}")
    return p

# route or directiosn to frontend file
@app.route('/')
def serve_index():
    return send_from_directory(frontend_dir, 'index.html')


# GET request for fetching products (Products API)
@app.route('/api/products', methods=['GET'])
def get_products():
    
    return jsonify([map_product_to_url(p) for p in PRODUCTS]), 200


@app.route('/api/cart', methods=['GET'])
def get_cart():
    
    return jsonify(cart), 200

@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": f"Product with ID {product_id} not found."}), 404
    if product['stock'] <= 0:
        return jsonify({"message": f"Product '{product['name']}' is out of stock."}), 400

    cart_item = next((item for item in cart if item['id'] == product_id), None)
    if cart_item:
        cart_item['quantity'] += 1
    else:
        # Item is mapped to URL here before storing in the global 'cart' list.
        new_item = map_product_to_url(product) 
        new_item['quantity'] = 1
        cart.append(new_item)

    product['stock'] -= 1
    return get_cart()

@app.route('/api/cart/update/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    data = request.get_json()
    delta = data.get('delta', 0)

    cart_item = next((item for item in cart if item['id'] == product_id), None)
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)

    if not cart_item or not product:
        return jsonify({"message": "Item not found."}), 404

    if delta > 0 and product['stock'] <= 0:
        return jsonify({"message": f"No more stock for '{product['name']}'."}), 400
    # here when we add quanity the stock reduces
    cart_item['quantity'] += delta
    product['stock'] -= delta
    # if we make the quanity less than 1 ie 0 the product is removed from the cart
    if cart_item['quantity'] <= 0:
        cart.remove(cart_item)

    return get_cart()

@app.route('/api/checkout', methods=['POST'])
def checkout():
    global cart, next_order_id
    if not cart:
        return jsonify({"message": "Cart is empty."}), 400

    
    order_summary = {
        "order_id": next_order_id,
        "items": cart, 
        "total": sum(item['price'] * item['quantity'] for item in cart)
    }

    cart = []
    next_order_id += 1
    return jsonify(order_summary), 200

# running of the app
if __name__ == '__main__':
    print("Running Flask app at http://127.0.0.1:5500")
    app.run(debug=True, host='0.0.0.0', port=5500)
