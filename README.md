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
✅ **Add new Trades**  
✅ **Record Trades** (Buy/Sell with timestamp, quantity, and price)  
✅ **Calculate Stock Metrics**   
✅ **Compute GBCE All Share Index** (Geometric mean of all stock prices)  
✅ **Unit Tests**  

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
## **<u>API Endpoints</u>**
### **1️⃣ Home Route**
📌 **GET "/"**
```
•  Description: Home API to get the details.
•  Response: List of all the stock data.
```

### **2️⃣ Trade Management**
📌 **POST "/new_trade"**
```
•  Description: Adds a new trade.
•  Response: List of all the stock data including new trade.
```
<b>Request Body (Form Data):</b>

| Parameter      | Type    | Required | Description                        |
|----------------|---------|----------|------------------------------------|
| stock_symbol   | string  | ✅ Yes    | Stock symbol (e.g., `ABC`)         |
| stock_type     | int     | ✅ Yes    | "Common" or "Preferred"            |
| last_dividend  | float   | ✅ Yes    | dividend value                     |
| fixed_dividend | float   | ❎ No     | value given if type is "Preferred" |
| par_value      | integer | ✅ Yes    | value of stock                     |


📌 **POST "/record_trade"**
```
•  Description: Records a trade.
•  Response: List of all the stock data including trade record.
```
<b>Request Body (Form Data):</b>

| Parameter     | Type    | Required | Description                      |
|--------------|--------|----------|----------------------------------|
| stock_symbol | string | ✅ Yes   | Stock symbol (e.g., `ABC`)       |
| quantity     | int    | ✅ Yes   | Number of shares traded         |
| price        | float  | ✅ Yes   | Price per share                 |
| trade_type   | string | ✅ Yes   | `"buy"` or `"sell"`             |

### **3️⃣ Stock Metrics**

📌 **POST "/calculate"**
```
•  Description: Calculates Dividend Yield and P/E Ratio for a given stock.
•  Response: Calculated Dividend Yield and P/E Ratio
```
<b>Request Body (Form Data):</b>

| Parameter     | Type   | Required | Description                      |
|--------------|--------|----------|----------------------------------|
| stock_symbol | string | ✅ Yes   | Stock symbol (e.g., `ABC`)       |
| price     | float  | ✅ Yes   | Market price for the stock       |

### **4️⃣ GBCE All Share Index**
📌 **GET "/share_index"**
```
•  Description: Computes the GBCE All Share Index (geometric mean of all stock prices).
•  Response: Returns All Share Index.
```

## **<u>HTML</u>**
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
‣ Choose Stock Type
‣ Enter Last Dividend
‣ Enter Par Value
‣ Enter Fixed Dividend if Stock Type selected is "Preferred"
‣ Submit Trade
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

