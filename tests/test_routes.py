import pytest
from app import app


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


def test_gbce_index_not_available(client):
    """Test the route to calculate GBCE All Share Index."""
    response = client.get("/share_index")
    expected_response = b'{"share_index": "Not available"}'
    assert response.status_code == 200
    assert response.data == expected_response


def test_new_trade(client):
    """Test the new trade for both GET and POST requests."""
    # Test GET request
    response = client.get("/new_trade")
    assert response.status_code == 200

    # Test POST request (simulate a trade addition for already existed trade)
    response = client.post("/new_trade", data={
        "stock_symbol": "TEST",
        "stock_type": "Common",
        "last_dividend": "0.3",
        "fixed_dividend": 0.4,
        "par_value": 100
    })
    expected_response = b'{"TEA": {"stock_type": "Common", "last_dividend": 0, "par_value": 100}, ' \
                        b'"POP": {"stock_type": "Common", "last_dividend": 8, "par_value": 100}, ' \
                        b'"ALE": {"stock_type": "Common", "last_dividend": 23, "par_value": 60}, ' \
                        b'"GIN": {"stock_type": "Preferred", "last_dividend": 8, "fixed_dividend": 0.02, ' \
                        b'"par_value": 100}, ' \
                        b'"JOE": {"stock_type": "Common", "last_dividend": 13, "par_value": 250}, ' \
                        b'"TEST": {"stock_type": "Common", "last_dividend": "0.3", "par_value": "100"}}'

    assert response.status_code == 200
    assert response.data == expected_response

    # Test POST request (simulate a trade addition for already existed trade)
    response = client.post("/new_trade", data={
        "stock_symbol": "TEA",
        "stock_type": "Common",
        "last_dividend": "0.3",
        "fixed_dividend": 0.4,
        "par_value": 100
    })
    assert response.status_code == 409
    assert response.data == b'Trade "TEA" already exists!'


def test_record_trade(client):
    """Test the trade record for both GET and POST requests."""
    # Test GET request
    response = client.get("/record_trade")
    assert response.status_code == 200

    # Test POST request (simulate a trade recording)
    response = client.post("/record_trade", data={
        "stock_symbol": "TEA",
        "quantity": 10,
        "trade_type": "BUY",
        "price": 50.0
    })
    assert response.status_code == 200
    assert b'{"TEA": {"stock_type": "Common", "last_dividend": 0, "par_value": 100, ' in response.data
    assert b'"trades": [{"timestamp":' in response.data

    # Test invalid stock symbol input (POST request to /record_trade)
    response = client.post("/record_trade", data={
        "stock_symbol": "INVALID",
        "quantity": 10,
        "trade_type": "BUY",
        "price": 50.0
    })
    assert response.status_code == 404
    assert b'Stock not found!' in response.data


def test_calculate_stock_metrics(client):
    """Test the stock calculation page for POST requests."""
    # Test POST request (simulate calculating Dividend Yield and P/E Ratio)
    response = client.post("/calculate", data={
        "stock_symbol": "POP",
        "price": 50.0
    })
    expected_response = b'{"symbol": "POP", "price": 50.0, "dividend_yield": 0.16, "pe_ratio": 6.25}'
    assert response.status_code == 200
    assert response.data == expected_response

    """Test invalid stock symbol input (POST request to /calculate)."""
    response = client.post("/calculate", data={
        "stock_symbol": "INVALID",
        "price": 50.0
    })
    assert response.status_code == 404
    assert b'Stock not found!' in response.data


def test_gbce_index(client):
    """Test the route to calculate GBCE All Share Index."""
    response = client.get("/share_index")
    expected_response = b'{"share_index": 50.0}'
    assert response.status_code == 200
    assert response.data == expected_response
