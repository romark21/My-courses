from contextlib import contextmanager
import time


@contextmanager
def timer():
    start_time = time.time()
    try:
        yield

    except ValueError:   #Вслучае возникновения ошибки ValueError, выводим сообщение.
        print(f'Во время выполнения функции: {timer()}, возникло исключение типа ValueError,'
              f' сообщение: Проверьте правильость введённых данных!')

    except TypeError:  #Вслучае возникновения ошибки TypeError, выводим сообщение.
        print(f'Во время выполнения функции: {timer()}, возникло исключение типа TypeError,'
              f' сообщение: Проверьте правильость введённых данных!')

    finally:
        finish_time = time.time() - start_time
        print(f'Время выполнения функции: {finish_time}')


'''
 Для того, чтобы вызвать ошибку в программе и увидеть, как отработает except. Добавим параметр в  функцию get_list,
  но при вызове этой функции не передадим никаких аргументов.
'''

def get_list(num):
    result = [i for i in range(num)]
    return result


with timer():
    get_list()
