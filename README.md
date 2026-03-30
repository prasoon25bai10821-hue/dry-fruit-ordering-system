📌 Dry Fruit Shop Recommendation System

🧠 AI-Powered CLI-Based Retail System

A Python-based command-line application that simulates a smart dry fruit shop with AI-powered product recommendations using collaborative filtering.

🚀 Features
🛒 Interactive shopping cart system
💰 Automatic billing with discount logic
📊 Popular product suggestions
🤖 AI-based recommendation engine
⚡ Fast startup using pre-trained model (joblib)
🧾 Input validation & error handling
🎯 Objective

To demonstrate how AI/ML concepts like collaborative filtering can be applied in a simple CLI-based retail system to improve customer experience and increase sales.

🧩 Technologies Used
Python 3.x
pandas
scikit-learn
joblib

🧠 How AI Works in This Project

The system uses Collaborative Filtering with Cosine Similarity:

Builds a user-item matrix from ratings data
Computes similarity between users
Identifies users with similar preferences
Recommends products based on similar users' choices
📂 Project Structure
├── main.py
├── products_data.csv
├── ratings.csv
├── model.pkl
└── README.md
⚙️ Installation & Setup
Install dependencies:
pip install pandas scikit-learn joblib
Run the project:
python main.py
🛍️ How to Use
Start the program
View popular products
Select items by entering product number
Enter quantity
Checkout
View bill + discount (if applicable)
Get AI-based recommendations
💡 Discount Rule
If total > ₹2000 → 10% discount applied automatically
📊 Sample Output
Popular Products:
Cashew
Almond
Masala Kaju

Bill:
Masala Kaju - 1 kg - ₹1299
Pista - 1 kg - ₹1499
Discount: ₹279.8
Total: ₹2518.2

Recommended:
Salted Cashew
Chocolate Almond
Cranberry
⚠️ Limitations
No user login system
Static product list
No database (CSV-based)
Cold start problem for new users
🔮 Future Enhancements
User authentication system
Database integration (SQLite/MySQL)
Web/GUI interface
Hybrid recommendation system
Real-time inventory tracking
🌍 Real-World Applications
Small retail shops
E-commerce recommendation engines
POS systems
Food delivery apps
👨‍💻 Author

Prasoon Yadav
CSE (AI & ML)
VIT Vellore

📚 References
Scikit-learn Documentation
Pandas Documentation
Recommender Systems Handbook
