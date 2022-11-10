class Calculator:

    last = None
    
    def __init__(self):
        self._history = []
    
    def __cache_it(method):
        def wrap(self, a, b, *args, **kwargs):
            answ = method(self, a, b, *args, **kwargs)

            self.__class__.last = f"{method.__name__}({a}, {b}) == {answ}"
            self._history.append(self.last)

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
        if len(self._history) < n:
            return None
        return self._history[-n]

    @classmethod
    def clear(cls):
        cls.last = None

