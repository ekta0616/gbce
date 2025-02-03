import datetime
import math


class Stock:
    def __init__(self, symbol, stock_type, last_dividend, par_value, fixed_dividend=None):
        self.symbol = symbol
        self.stock_type = stock_type  # "Common" or "Preferred"
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend  # Only for Preferred stock
        self.par_value = par_value
        self.trades = []  # Stores all trade records

    def calculate_dividend_yield(self, price):
        """Calculate dividend yield based on stock type."""
        if price <= 0:
            return None
        if self.stock_type == "Common":
            return self.last_dividend / price
        elif self.stock_type == "Preferred" and self.fixed_dividend:
            return (self.fixed_dividend * self.par_value) / price
        return None

    def calculate_pe_ratio(self, price):
        """Calculate P/E Ratio."""
        dividend = self.calculate_dividend_yield(price) * price if price > 0 else 0
        return price / dividend if dividend > 0 else None

    def record_trade(self, quantity, trade_type, price):
        """Record a trade (Buy/Sell)."""
        trade = {
            "timestamp": datetime.datetime.now(),
            "quantity": quantity,
            "trade_type": trade_type,  # "BUY" or "SELL"
            "price": price
        }
        self.trades.append(trade)

    def calculate_vwsp(self):
        """Calculate Volume Weighted Stock Price (VWSP) for the last 5 minutes."""
        five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
        recent_trades = [t for t in self.trades if t["timestamp"] >= five_minutes_ago]

        if not recent_trades:
            return None  # No recent trades

        total_traded_value = sum(t["price"] * t["quantity"] for t in recent_trades)
        total_quantity = sum(t["quantity"] for t in recent_trades)

        return total_traded_value / total_quantity if total_quantity > 0 else None


class GBCE:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        """Add a new stock to GBCE."""
        self.stocks[stock.symbol] = stock

    def calculate_all_share_index(self):
        """Calculate the GBCE All Share Index using geometric mean of VWSP."""
        vwsp_values = [stock.calculate_vwsp() for stock in self.stocks.values() if stock.calculate_vwsp() is not None]

        if not vwsp_values:
            return 'Not available'  # No VWSP values available

        product = math.prod(vwsp_values)
        return product ** (1 / len(vwsp_values))
