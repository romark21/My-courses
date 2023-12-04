list = [*map(str, input('Введите элементы через пробел: ').split())]
even_num = []
odd_num = []

for i in range(len(list)):
    if i % 2 == 0:
        even_num.append(list[i])
    else:
        odd_num.append(list[i])

print(f'Элементы с чётным индексом: {even_num}')
print(f'Элементы с нечётным индексом: {odd_num}')

"""
--------------------------------------------------------------------------------------------------------------------
"""

list = [*map(str, input('Введите элементы через пробел: ').split())]
even_num = [list[i] for i in range(len(list)) if i % 2 == 0]
odd_num = [list[i] for i in range(len(list)) if i % 2 != 0]

print(f'Элементы с чётным индексом: {even_num}')
print(f'Элементы с нечётным индексом: {odd_num}')

