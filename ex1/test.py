import unittest
from ex1 import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(4, 8), 12)

    def test_sub(self):
        self.assertEqual(self.calc.sub(70, 30), 40)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 2), 4)

    def test_div(self):
        self.assertEqual(self.calc.div(50, 2), 25)

    def test_history(self):
        self.calc.sum(4, 8)
        self.calc.sub(70, 30)
        self.calc.mul(2, 2)
        self.calc.div(50, 2)
        self.assertEqual(self.calc.history(2), "mul(2, 2) == 4")

    def test_last(self):
        self.calc.sum(4, 8)
        self.calc.sub(70, 30)
        self.calc.mul(2, 2)
        self.calc.div(50, 2)
        f = Calculator()
        self.assertEqual(f.last, "div(50, 2) == 25.0")

    def test_clear(self):
        self.calc.clear()
        self.assertEqual(Calculator.last, None)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
