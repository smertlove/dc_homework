RUBLE_COEF = 1
DOLLAR_COEF = 60
EURO_COEF = 70

class BaseWallet:
    
    _coefficient = 1

    def __init__(self, name, amount):
        self._name = name
        self._amount = amount




    def get_amount(self):
        return self._amount

    def get_name(self):
            return self._name

    def get_coefficient(self):
        return self._coefficient

    def to_base(self):
        return self._amount * self._coefficient




    # Повторяющийся код математических операций. #
    def __apply_operation(self, other, operation):
        if isinstance(other, BaseWallet):
            return self.__class__(self._name, operation(self.to_base(), other.to_base()) // self._coefficient)
        return self.__class__(self._name, operation(self._amount, other))

    def __add__ (self, other):
        return self.__apply_operation(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__ (self, other):
        return self.__apply_operation(other, lambda a, b: a - b)

    def __rsub__(self, other):
        return self.__apply_operation(other, lambda a, b: b - a)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return self.__apply_operation(other, lambda a, b: a * b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__apply_operation(other, lambda a, b: a / b)

    def __rtruediv__(self, other):
        return self.__apply_operation(other, lambda a, b: b / a)

    def __eq__(self, other):
        return type(self) is type(other) and self._amount == other.get_amount() 

    def __repr__(self):
        return f"Base Wallet {self._name} {self._amount}"

    def spend_all(self):
        if self.get_amount() > 0:
            self._amount = 0







class RubbleWallet(BaseWallet):

    _coefficient = RUBLE_COEF

    def __repr__(self):
        return f"Rubble Wallet {self._name} {self._amount}"


class DollarWallet(BaseWallet):

    _coefficient = DOLLAR_COEF

    def __repr__(self):
        return f"Dollar Wallet {self._name} {self._amount}"


class EuroWallet(BaseWallet):

    _coefficient = EURO_COEF

    def __repr__(self):
        return f"Euro Wallet {self._name} {self._amount}"



def main():
    a = RubbleWallet("X", 20) 
    b = DollarWallet("D", 10)
    c = a + b
    d = RubbleWallet("X", 620)
    for i in (a, b, c, d):
        print(i)

if __name__ == "__main__":
    main()