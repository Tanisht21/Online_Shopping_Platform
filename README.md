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

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo/Backend

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
# Activate venv
venv\Scripts\activate      # Windows  
source venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Backend Server
python app.py


Server will run at:
👉 http://127.0.0.1:5500/

API: http://127.0.0.1:5500/api/products

Frontend: http://127.0.0.1:5500/