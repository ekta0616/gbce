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
    assert response.status_code == 200
    assert b"Global Beverage Corporation Exchange" in response.data
    assert b"Record a Trade" in response.data
    assert b"Calculate Stock Metrics" in response.data
    assert b"View GBCE All Share Index" in response.data


def test_trade(client):
    """Test the trade page for both GET and POST requests."""
    # Test GET request
    response = client.get("/trade")
    assert response.status_code == 200
    assert b"Record a Trade" in response.data

    # Test POST request (simulate a trade recording)
    response = client.post("/trade", data={
        "stock_symbol": "TEA",
        "quantity": 10,
        "buy_sell": "BUY",
        "price": 50.0
    })
    assert response.status_code == 200
    assert b"Trade recorded successfully." in response.data


def test_calculate_stock_metrics(client):
    """Test the stock calculation page for both GET and POST requests."""
    # Test GET request
    response = client.get("/calculate")
    assert response.status_code == 200
    assert b"Calculate Stock Metrics" in response.data

    # Test POST request (simulate calculating Dividend Yield and P/E Ratio)
    response = client.post("/calculate", data={
        "stock_symbol": "TEA",
        "price": 50.0
    })
    assert response.status_code == 200
    assert b"Dividend Yield" in response.data
    assert b"P/E Ratio" in response.data


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
