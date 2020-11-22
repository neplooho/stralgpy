import datetime


def loggable_decorator(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        elapsed = end - start
        print("{}.{} function took {} time to finish.".format(func.__globals__.get("__name__"), func.__name__, elapsed))
        return result

    return inner
