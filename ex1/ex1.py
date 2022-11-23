from time import time

def time_decorator(func):
    def wrap(*args, **kwargs):
        start = time()
        answ = func(*args, **kwargs)
        print(round(time() - start))
        return answ
    return wrap
