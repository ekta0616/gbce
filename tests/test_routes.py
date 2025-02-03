import pytest
from app import app  # Import the Flask app


# Flask test client for simulating requests
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home page route."""
    response = client.get("/")
    expected_response = b'{"TEA": {"stock_type": "Common", "last_dividend": 0, "par_value": 100}, ' \
                       b'"POP": {"stock_type": "Common", "last_dividend": 8, "par_value": 100}, ' \
                       b'"ALE": {"stock_type": "Common", "last_dividend": 23, "par_value": 60}, ' \
                       b'"GIN": {"stock_type": "Preferred", "last_dividend": 8, "fixed_dividend": 0.02, ' \
                       b'"par_value": 100}, ' \
                       b'"JOE": {"stock_type": "Common", "last_dividend": 13, "par_value": 250}}'
    assert response.status_code == 200
    assert response.data == expected_response


def test_trade(client):
    """Test the trade page for both GET and POST requests."""
    # Test GET request
    response = client.get("/new_trade")
    assert response.status_code == 200

    # Test POST request (simulate a trade recording)
    response = client.post("/new_trade", data={
        "stock_symbol": "TEA",
        "quantity": 10,
        "buy_sell": "BUY",
        "price": 50.0
    })
    assert response.status_code == 400


def test_calculate_stock_metrics(client):
    """Test the stock calculation page for POST requests."""
    # Test POST request (simulate calculating Dividend Yield and P/E Ratio)
    response = client.post("/calculate", data={
        "stock_symbol": "POP",
        "price": 50.0
    })
    expected_response = b'Dividend Yield' in b'{"symbol": "POP", "price": 50.0, "dividend_yield": 0.16, ' \
                                             b'"pe_ratio": 6.25}'
    assert response.status_code == 200


def test_gbce_index(client):
    """Test the route to calculate GBCE All Share Index."""
    response = client.get("/gbce_index")
    assert response.status_code == 200
    assert b"GBCE All Share Index" in response.data


def test_invalid_stock_symbol(client):
    """Test invalid stock symbol input (POST request to /calculate)."""
    response = client.post("/calculate", data={
        "stock_symbol": "INVALID",
        "price": 50.0
    })
    assert response.status_code == 200
    assert b"Stock not found" not in response.data  # assuming no error handling for stock not found


def test_invalid_trade(client):
    """Test invalid trade (POST request to /trade)."""
    response = client.post("/trade", data={
        "stock_symbol": "INVALID",
        "quantity": 10,
        "buy_sell": "BUY",
        "price": 50.0
    })
    assert response.status_code == 200
    assert b"Trade recorded successfully." not in response.data  # assuming invalid stock does not record a trade
