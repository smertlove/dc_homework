RUBLE_COEF = 1
DOLLAR_COEF = 60
EURO_COEF = 70


class BaseWallet:

    exchange_rate = 1
    _log_name = "Base Wallet"

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.name

    def getexchange_rate(self):
        return self.exchange_rate

    def to_base(self):
        return self.amount * self.exchange_rate

    # Повторяющийся код математических операций. #
    def __apply_operation(self, other, operation):
        if isinstance(other, BaseWallet):
            return self.__class__(self.name,
                                  operation(
                                      self.to_base(),
                                      other.to_base()
                                      ) / self.exchange_rate)
        return self.__class__(self.name, operation(self.amount, other))

    def __add__(self, other):
        return self.__apply_operation(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
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
        return type(self) is type(other) and self.amount == other.get_amount()

    def __repr__(self):
        return f"{self._log_name} {self.name} {self.amount}"

    def spend_all(self):
        if self.get_amount() > 0:
            self.amount = 0


class RubbleWallet(BaseWallet):

    exchange_rate = RUBLE_COEF
    _log_name = "Rubble Wallet"


class DollarWallet(BaseWallet):

    exchange_rate = DOLLAR_COEF
    _log_name = "Dollar Wallet"


class EuroWallet(BaseWallet):

    exchange_rate = EURO_COEF
    _log_name = "Euro Wallet"
