from flask import Flask, render_template, request
from stock import Stock, GBCE

app = Flask(__name__)

# Sample stocks
gbce = GBCE()
gbce.add_stock(Stock("TEA", "Common", 0, 100))
gbce.add_stock(Stock("POP", "Common", 8, 100))
gbce.add_stock(Stock("ALE", "Common", 23, 60))
gbce.add_stock(Stock("GIN", "Preferred", 8, 100, 0.02))
gbce.add_stock(Stock("JOE", "Common", 13, 250))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/new_trade", methods=["GET", "POST"])
def new_trade():
    if request.method == "POST":
        symbol = request.form["stock_symbol"]
        stock_type = request.form["stock_type"]
        last_dividend = request.form["last_dividend"]
        fixed_dividend = request.form["fixed_dividend"]
        par_value = request.form["par_value"]

        if symbol in gbce.stocks:
            return render_template("result.html", message="Trade already added.")
        else:
            gbce.add_stock(Stock(symbol, stock_type, last_dividend, par_value, fixed_dividend))
            return render_template("result.html", message="Trade added successfully.")

    return render_template("new_trade.html")


@app.route("/record_trade", methods=["GET", "POST"])
def record_trade():
    if request.method == "POST":
        symbol = request.form["stock_symbol"]
        quantity = int(request.form["quantity"])
        trade_type = request.form["trade_type"]
        price = float(request.form["price"])

        if symbol in gbce.stocks:
            gbce.stocks[symbol].record_trade(quantity, trade_type, price)
            return render_template("result.html", message="Trade recorded successfully.")

    # Extract unique stock symbols from trades
    stock_symbols = sorted(set(trade for trade in [*gbce.stocks]))
    return render_template("record_trade.html", stock_symbols=stock_symbols, trades=gbce.stocks)


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        symbol = request.form["stock_symbol"]
        price = float(request.form["price"])

        if symbol in gbce.stocks:
            stock = gbce.stocks[symbol]
            dividend_yield = stock.calculate_dividend_yield(price)
            pe_ratio = stock.calculate_pe_ratio(price)

            return render_template("result.html", symbol=symbol, price=price, dividend_yield=dividend_yield,
                                   pe_ratio=pe_ratio)

    # Extract unique stock symbols from trades
    stock_symbols = sorted(set(trade for trade in [*gbce.stocks]))
    return render_template("stock.html", stock_symbols=stock_symbols)


@app.route("/gbce_index")
def gbce_index():
    index = gbce.calculate_all_share_index()
    return render_template("result.html", gbce_index=index)


if __name__ == "__main__":
    app.run(debug=True)
