import unittest

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()

    def test_usd_to_eur(self):
        result = self.converter.convert('USD', 'EUR', 100)
        self.assertAlmostEqual(result, 85.0, delta=0.01)

    def test_brl_to_usd(self):
        result = self.converter.convert('BRL', 'USD', 100)
        self.assertAlmostEqual(result, 19.0, delta=0.01)

if __name__ == "__main__":
    unittest.main()
