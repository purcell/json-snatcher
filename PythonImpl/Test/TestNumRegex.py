import unittest
import re

class TestNumRegex(unittest.TestCase):
    
    def setUp(self):
        self.regex = re.compile(r'-?0(?:\.\d+)?(?:[eE][-+]?[\d]+)?|-?[1-9][\d]*(?:\.?\d+)?(?:[eE][-+]?[\d]+)?')

    def test_simple(self):
        test_str = '1234 5678'
        result = self.regex.findall(test_str)
        self.assertEqual('1234', result[0])
        self.assertEqual('5678', result[1])

    def test_zero(self):
        test_str = '0'
        result = self.regex.findall(test_str)
        self.assertEqual('0', result[0])

    def test_negative(self):
        test_str = '-25'
        result = self.regex.findall(test_str)
        self.assertEqual('-25', result[0])

    def test_decimal(self):
        test_str = '3.14159'
        result = self.regex.findall(test_str)
        self.assertEqual('3.14159', result[0])

    def test_neg_decimal(self):
        test_str = '-3.14159'
        result = self.regex.findall(test_str)
        self.assertEqual('-3.14159', result[0])

    def test_exp(self):
        test_str = '-3E+5'
        result = self.regex.findall(test_str)
        self.assertEqual('-3E+5', result[0])

    def test_exp2(self):
        test_str = '-3e+5'
        result = self.regex.findall(test_str)
        self.assertEqual('-3e+5', result[0])

    def test_exp3(self):
        test_str = '-3E5'
        result = self.regex.findall(test_str)
        self.assertEqual('-3E5', result[0])

    def test_exp_w_dec(self):
        test_str = '-3.0123E5'
        result = self.regex.findall(test_str)
        self.assertEqual('-3.0123E5', result[0])

    def test_exp_incomplete(self):
        test_str = '-3.0123E'
        result = self.regex.findall(test_str)
        self.assertEqual('-3.0123', result[0])

    def test_no_match(self):
        test_str = 'ssseeEEEskdjsdkjf++++----'
        result = self.regex.findall(test_str)
        self.assertEqual(0, len(result))
        
    def test_zeros1(self):
        test_str = '9200'
        result = self.regex.findall(test_str)
        self.assertEqual('9200', result[0])

    def test_zeros2(self):
        test_str = '1.009'
        result = self.regex.findall(test_str)
        self.assertEqual('1.009', result[0])

    def test_zeros3(self):
        test_str = '9006'
        result = self.regex.findall(test_str)
        self.assertEqual('9006', result[0])

    def test_zeros3(self):
        test_str = '0.01'
        result = self.regex.findall(test_str)
        self.assertEqual('0.01', result[0])

if __name__ == '__main__':
    unittest.main()