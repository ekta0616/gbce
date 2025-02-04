from flask import Flask, render_template, request, Response
from stock import Stock, GBCE
import json
import constants as const

app = Flask(__name__)

# Sample stocks
gbce = GBCE()
gbce.add_stock(Stock('TEA', 'Common', 0, 100))
gbce.add_stock(Stock('POP', 'Common', 8, 100))
gbce.add_stock(Stock('ALE', 'Common', 23, 60))
gbce.add_stock(Stock('GIN', 'Preferred', 8, 100, 0.02))
gbce.add_stock(Stock('JOE', 'Common', 13, 250))


def get_home_data():
    """
    Method to return the default data to be displayed i.e. all the stocks data
    :return: stocks data
    """
    stocks_data = dict()
    for stock in gbce.stocks:
        stock_values = dict()
        stock_values['stock_type'] = gbce.stocks[stock].stock_type
        stock_values['last_dividend'] = gbce.stocks[stock].last_dividend
        if stock_values['stock_type'] == 'Preferred':
            stock_values['fixed_dividend'] = gbce.stocks[stock].fixed_dividend
        stock_values['par_value'] = gbce.stocks[stock].par_value
        if gbce.stocks[stock].trades:
            stock_values['trades'] = gbce.stocks[stock].trades
        stocks_data[stock] = stock_values
    return stocks_data


def send_response(headers, data=None, message=None, status=const.SUCCESS, template=None):
    """
    Method to send the response back to the client on the basis of user-agent.
    It will render page if request is sent via WEB browser and return json data otherwise.
    :param headers: request headers
    :param data: data to be sent
    :param message: message to be displayed, if any
    :param status: status code
    :param template: html page to be rendered
    :return: Response/rendered template
    """
    if 'Mozilla' in str(headers):
        return render_template(template, message=message, status=status, data=data)
    if data and status == 200:
        return Response(json.dumps(data, default=str), status=status, mimetype='application/json')
    return Response(message, status=status, mimetype='application/json')


@app.route('/', methods=['GET'])
def home():
    return send_response(request.headers, get_home_data(), template='home.html')


@app.route('/new_trade', methods=['GET', 'POST'])
def new_trade():
    status = const.SUCCESS
    msg = None
    template = 'new_trade.html'
    if request.method == 'POST':
        symbol = request.form['stock_symbol']
        stock_type = request.form['stock_type']
        last_dividend = request.form['last_dividend']
        fixed_dividend = request.form['fixed_dividend']
        par_value = request.form['par_value']
        template = 'result.html'

        if symbol in gbce.stocks:
            msg = 'Trade "{}" already exists!'.format(symbol)
            status = const.CONFLICT
        else:
            gbce.add_stock(Stock(symbol, stock_type, last_dividend, par_value, fixed_dividend))
            msg = 'Trade "{}" added successfully.'.format(symbol)

    return send_response(request.headers, get_home_data(), msg, status, template=template)


@app.route('/record_trade', methods=['GET', 'POST'])
def record_trade():
    msg = None
    template = 'record_trade.html'
    if request.method == 'POST':
        symbol = request.form['stock_symbol']
        quantity = int(request.form['quantity'])
        trade_type = request.form['trade_type']
        price = float(request.form['price'])
        if symbol not in gbce.stocks:
            return send_response(request.headers, None, "Stock not found!", const.NOT_FOUND, template=template)

        gbce.stocks[symbol].record_trade(quantity, trade_type, price)
        msg = 'Trade recorded successfully.'
        template = 'result.html'

    return send_response(request.headers, get_home_data(), msg, template=template)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    template = 'stock.html'
    if request.method == 'POST':
        symbol = request.form['stock_symbol']
        price = float(request.form['price'])
        data = dict()
        if symbol not in gbce.stocks:
            return send_response(request.headers, None, "Stock not found!", const.NOT_FOUND, template=template)
        stock = gbce.stocks[symbol]
        dividend_yield = stock.calculate_dividend_yield(price)
        pe_ratio = stock.calculate_pe_ratio(price)
        data['symbol'] = symbol
        data['price'] = price
        data['dividend_yield'] = dividend_yield
        data['pe_ratio'] = pe_ratio
        template = 'result.html'
    else:
        data = get_home_data()

    return send_response(request.headers, data, template=template)


@app.route('/share_index', methods=['GET'])
def share_index():
    data = dict()
    data['share_index'] = gbce.calculate_all_share_index()
    return send_response(request.headers, data, template='result.html')


if __name__ == '__main__':
    app.run(debug=True)
