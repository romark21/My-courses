def decoration_function(func):
    from _datetime import datetime

    def wrapper():
        start_time = datetime.now()
        func()
        finish_time = datetime.now() - start_time
        return f'Время выполнения функции: {finish_time}'

    return wrapper()


@decoration_function
def get_list():
    result = [i for i in range(100000)]
    return result


timer = get_list
print(timer)
