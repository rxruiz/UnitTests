import unittest
import datetime

class mod13_rxrfcb(unittest.TestCase):
    
    def test_symbol(self):
        symbol = "AARP"
        self.assertTrue(symbol.isalpha(), "Alpha characters only.")
        self.assertTrue(len(symbol)<8, "Please keep the symbol between 1 and 7 characters.")
        self.assertTrue(len(symbol)>0, "Please keep the symbol between 1 and 7 characters.")
        self.assertEqual(symbol.upper(), symbol, "All characters must be capitalized.")
    def test_chart(self):
        chart = "1"
        self.assertIn(chart, ['1','2'])
        self.assertTrue(chart.isdigit())
    def test_time_series(self):
        time = "2"
        self.assertIn(time, ['1','2','3','4'])
        self.assertTrue(time.isdigit())
    def test_start_date(self):
        date = "2012-04-19"
        self.assertIsInstance(date, str)
        self.assertIsInstance(datetime.datetime.strptime(date, '%Y-%m-%d'), datetime.datetime)
    def test_end_date(self):
        date = "2012-04-19"
        self.assertIsInstance(date, str)
        self.assertIsInstance(datetime.datetime.strptime(date, '%Y-%m-%d'), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
