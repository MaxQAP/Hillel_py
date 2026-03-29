from functools import wraps
import datetime


def log_arguments_and_result(func=None, *, logger=None):

    def actual_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(repr(a) for a in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{timestamp}] ВИКЛИК   {f.__name__}({all_args})")

            try:
                result = f(*args, **kwargs)
                print(f"[{timestamp}] ПОВЕРНЕННЯ {f.__name__} → {result!r}")
                return result
            except Exception as e:
                print(f"[{timestamp}] ПОМИЛКА   {f.__name__} → {type(e).__name__}: {e}")
                raise

        return wrapper
    if func is None:
        return actual_decorator
    else:
        return actual_decorator(func)

@log_arguments_and_result
def add(a, b, c=0):
    return a + b + c


@log_arguments_and_result
def multiply(x, y):
    return x * y


# Тест
print("Тест 1:")
add(5, 12)

print("\nТест 2:")
multiply(7, 8)