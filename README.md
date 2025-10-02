🛍️ Flask Shop Backend

This is a simple Flask-based e-commerce backend with products, cart management, and checkout features.
It works with a separate frontend (HTML/JS) that consumes the APIs.

🚀 Features

Serve frontend static files (HTML, CSS, JS)

Fetch products with image URLs

Add / update / remove items in cart

Checkout system with order ID and total price

In-memory storage (no database)

📂 Project Structure
.
├── Backend/
│   ├── app.py              # Flask backend
│   ├── requirements.txt    # Dependencies
├── Frontend/
│   ├── index.html          # Frontend entry page
│   └── static/             # Images, CSS, JS
└── README.md

🖥️ Backend Setup & Running

Step 1: Install Standard Python

Go to python.org
 and download Python 3.13 (or 3.10 / 3.11).

During installation, check the box “Add Python to PATH”.

Verify installation by running in PowerShell or Command Prompt:

python --version
py --version


Step 2: Clone the Repository

git clone https://github.com/Tanisht21/Online_Shopping_Platform.git
cd Online_Shopping_Platform/Backend


Step 3: Install Dependencies

Use the Python launcher to ensure the correct environment:

py -3.13 -m pip install --upgrade pip
py -3.13 -m pip install -r requirements.txt


⚠️ Avoid using pip from MSYS2 or other non-standard Python environments to prevent errors like ModuleNotFoundError: No module named 'encodings'.

Step 4: Run the Backend

py -3.13 -m flask run


Step 5: Open in Browser

Access the app at:

http://127.0.0.1:5500


Step 6: Notes

Ensure the Frontend folder is in the correct location relative to the Backend folder so Flask can serve index.html and static files.

Flask-CORS is already included in requirements.txt for handling cross-origin requests.


Server will run at:
👉 http://127.0.0.1:5500/

API: http://127.0.0.1:5500/api/products

Frontend: http://127.0.0.1:5500/
