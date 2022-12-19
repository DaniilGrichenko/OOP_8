from datetime import datetime


def timer(func_name: str):
    def decorate(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            print(
                "function execution time: {time.seconds}s, {time.microseconds}ms".format(
                    time=end - start
                )
            )
            return result
        return wrapper
    return decorate