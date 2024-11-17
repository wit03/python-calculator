import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # added test cases
    def test_add1(self):
        self.assertEqual(self.calc.add(100, 2), 102)
    def test_add2(self):
        self.assertEqual(self.calc.add(10000, 99), 10099)
    def test_sub1(self):
        self.assertEqual(self.calc.subtract(10000, 99), 9901)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(100, 99), 1)
    def test_mul1(self):
        self.assertEqual(self.calc.multiply(9, 9), 81)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
    def test_div1(self):
        self.assertEqual(self.calc.divide(10000, 10), 1000)
    def test_div2(self):
        self.assertEqual(self.calc.divide(20, 10), 2)
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(8, 4), 0)
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)
    


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()