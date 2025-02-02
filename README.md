# 📌 Global Beverage Corporation Exchange (GBCE) - Flask App  

A Flask-based stock market system for trading beverage company stocks. This app allows users to **record trades, calculate stock metrics** (Dividend Yield, P/E Ratio, Volume Weighted Stock Price), and compute the **GBCE All Share Index**.

---

## 📂 Project Structure
```plaintext
gbce/
│── app.py                 # Main Flask application
│── stock.py               # Stock and Trade logic
│── templates/             # HTML templates
│   ├── home.html
│   ├── new_trade.html
│   ├── record_trade.html
│   ├── stock.html
│   ├── result.html
│── static/                # Static files (CSS)
│   ├── style.css
│── tests/                 # Unit tests
│   ├── test_routes.py
│   ├── test_stock.py
│── README.md              # Documentation
│── requirements.txt       # Python dependencies

```
---

## **🚀 Features**
✅ **Record Trades** (Buy/Sell with timestamp, quantity, and price)  
✅ **Calculate Stock Metrics**  
✅ **Volume Weighted Stock Price** (Based on trades in the last 5 minutes)  
✅ **Compute GBCE All Share Index** (Geometric mean of all stock prices)  
✅ **Unit Tests for Routes & Models**  

---

## **⚙️ Setup & Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/gbce.git
cd gbce
```
### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```bash
python app.py
```
The app will start at http://127.0.0.1:5000/ 🚀

---

## **📌 Usage**
### **<u>HTML</u>**
### **1️⃣ Home Page**
```plaintext
Go to http://127.0.0.1:5000/
Choose from:
💲 Add a Trade
📝 Record a Trade
📈 Calculate Stock Metrics
📊 View GBCE All Share Index
```

### **2️⃣ Add a Trade**
```plaintext
‣ Enter Stock Symbol
‣ Choose Buy/Sell
‣ Enter Quantity & Price
‣ Submit & View Confirmation
```

### **3️⃣ Record a Trade**
```plaintext
‣ Enter Stock Symbol
‣ Choose Buy/Sell
‣ Enter Quantity & Price
‣ Submit & View Confirmation
```

### **4️⃣ Calculate Stock Metrics**
```plaintext
‣ Enter Stock Symbol & Price
‣ View Dividend Yield & P/E Ratio
```

### **5️⃣ GBCE All Share Index**
```plaintext
‣ Computes the Geometric Mean of all stock prices.
```
---

## **🛠️ Running Tests**
### **Run Unit Tests (Using pytest)**
```bash
pytest tests/
```

### **Test Files**
```plaintext
📌 tests/test_routes.py - Tests Flask Routes
📌 tests/test_models.py - Tests Stock Calculation Logic
```

