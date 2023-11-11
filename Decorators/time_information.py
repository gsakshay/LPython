# This is designed to be a decorator, providing information about time it takes to run a piece of code.
from time import time


def time_information(fun):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fun(*args, *kwargs)
        t2 = time()
        print(f'Time taken to run the function is {t2 - t1} seconds')
        return result

    return wrapper
