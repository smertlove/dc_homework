import unittest



class Calculator:

    last = None
    
    def __init__(self):
        self.__history = []
    
    def __cache_it(method):
        def wrap(self, a, b, *args, **kwargs):
            answ = method(self, a, b, *args, **kwargs)

            self.__class__.last = f"{method.__name__}({a}, {b}) == {answ}"
            self.__history.append(self.last)

            return answ
        return wrap

    @__cache_it
    def sum(self, a, b):
        return a + b 

    @__cache_it
    def sub(self, a, b):
        return a - b 

    @__cache_it
    def mul(self, a, b):
        return a * b 

    @__cache_it
    def div(self, a, b, mod=False):
        if mod:
            return a % b
        return a / b

    def history(self, n):
        if len(self.__history) < n:
            return None
        return self.__history[-n]

    @classmethod
    def clear(cls):
        cls.last = None



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
