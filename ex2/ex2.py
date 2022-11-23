import functools
import inspect
import datetime

def logging_decorator(loglist):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            call_time = datetime.datetime.now()
            answ = func(*args, **kwargs)
            loglist.append({
                "name": func.__name__,
                "arguments": inspect.getcallargs(func, *args, **kwargs),
                "call_time": call_time,
                "result": answ
            })
            return answ
        return wrap
    return decorator
