"""
В задании было условие, возвратить, только элементы с чётными или нечётными индексами.
Но я вывел все, только в результате подписал, какой элемент под чётным индексом, а какой под нечётным.
"""

class OddEven:

    def __init__(self, data):
        self.data = data
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.data):
            value = self.data[self.current]
            self.current += 1
            if self.current % 2 == 0:
                return f'"{value}" - Чётный индекс'
            else:
                return f'"{value}" - Нечётный индекс'
        else:
            raise StopIteration


my_data = ['one', 'two', 'three', 'car', 'phone', 7, 'python', '234']

it = OddEven(my_data)

for count, item in enumerate(it, 1):
    print(count, item)


# data = [*map(str, input('Введите элементы через пробел: ').split())]
# even_num = []
# odd_num = []
#
# for i in range(len(data)):
#     if i % 2 == 0:
#         even_num.append(data[i])
#     else:
#         odd_num.append(data[i])
#
# print(f'Элементы с чётным индексом: {even_num}')
# print(f'Элементы с нечётным индексом: {odd_num}')
#
# """
# --------------------------------------------------------------------------------------------------------------------
# """
#
# list = [*map(str, input('Введите элементы через пробел: ').split())]
# even_num = [list[i] for i in range(len(list)) if i % 2 == 0]
# odd_num = [list[i] for i in range(len(list)) if i % 2 != 0]
#
# print(f'Элементы с чётным индексом: {even_num}')
# print(f'Элементы с нечётным индексом: {odd_num}')






