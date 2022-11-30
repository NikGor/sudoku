import time

def timing(function):
    def inner(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print('Elapsed time:', round((end - start) * 1000, 2), 'ms')
        return result
    return inner