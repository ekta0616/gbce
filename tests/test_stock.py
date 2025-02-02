import unittest
from stock import Stock, GBCE


class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock("TEA", "Common", 10, 100)

    def test_dividend_yield(self):
        self.assertEqual(self.stock.calculate_dividend_yield(50), 0.2)

    def test_pe_ratio(self):
        self.assertEqual(self.stock.calculate_pe_ratio(50), 5.0)


class TestGBCE(unittest.TestCase):
    def setUp(self):
        self.gbce = GBCE()
        self.gbce.add_stock(Stock("POP", "Common", 8, 100))

    def test_calculate_all_share_index(self):
        self.gbce.stocks["POP"].record_trade(100, "BUY", 50)
        self.assertIsNotNone(self.gbce.calculate_all_share_index())


if __name__ == "__main__":
    unittest.main()
