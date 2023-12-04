from contextlib import contextmanager
from _datetime import datetime


@contextmanager
def timer():
    start_time = datetime.now()
    try:
        yield
    finally:
        finish_time = datetime.now() - start_time
        print(f'Время выполнения функции: {finish_time}')


def get_list():
    result = [i for i in range(100000)]
    return result


with timer():
    get_list()
