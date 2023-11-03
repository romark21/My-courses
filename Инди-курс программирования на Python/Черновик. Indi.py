# a = float(input())
# print(round(a, 2), (round(a, 3)))
"""
------------------------------------------------------------------
h = int(input()) * 3600
m = int(input()) * 60
s = int(input())
h_2 = int(input()) * 3600
m_2 = int(input()) * 60
s_2 = int(input())

time_1 = h + m + s
time_2 = h_2 + m_2 + s_2

print(max(time_1, time_2) - (min(time_1, time_2)))
--------------------------------------------------------------------------------------------------------------------
"""
"""
--------------------------------------------------------------------------------------------------------------------

a, b, c = int(input()), int(input()), int(input())
# 1 вариант решения
summa_1 = a + b + c
summa_2 = a * b + c
summa_3 = a + b * c
summa_4 = a * (b + c)
summa_5 = (a + b) * c
summa_6 = a * b * c
print(max(summa_1, summa_2, summa_3, summa_4, summa_5, summa_6))

# 2 вариант решения
print(max(a + b + c, a * b + c, a + b * c, a * (b + c), (a + b) * c, a * b * c))

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения
num_1, num_2, num_3, num_4 = map(int, input().split())
print((num_1 + num_2 + num_3 + num_4) / 4)

# 2 вариант решения
num = sum(list(map(int, input().split())))
print(num / 4)

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения
n, a, b = map(int, input().split())
m_2 = 2 * (a * b)
print(m_2 * n)

# 2 вариант решения
n, a, b = int(input() * (int(input() * (int(input())))) * 2)

-------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------

s = int(input())
serg_i_pet = s / 6
kat = s - serg_i_pet * 2
print(serg_i_pet, kat, serg_i_pet)

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------

x, y, z = map(int, input().split())
pencil = 3
pen = pencil + 2
flom = pen + 7
print(x * pencil + y * pen + z * flom)

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------

garry_shot, larry_shot = map(int, input().split())

total_cans = (garry_shot + larry_shot) - 1
garry_not_shot = total_cans - larry_shot
larry_not_shot = total_cans - garry_shot
print(larry_not_shot, garry_not_shot)

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения
a, b, c = map(int, input().split())
print(a, b, c, sep=',')

# 2 вариант решения
print(*input().split(), sep=',')

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения

n = int(input())
smaller_num = n - 1
bigger_num = n + 1
print(smaller_num, n, bigger_num, sep='<')

# 2 вариант решения
n = int(input())
print('%s < %s < %s' % (n - 1, n, n + 1))

-------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения
string_1, string_2, string_3 = (str(input()), str(input()), str(input()))
print(string_1, string_2, string_3, sep='---')

# 2 вариант решения
print(input(), input(), input(), sep='---')


------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения
s = input()
print(f"1{s}2{s}3{s}4{s}5")

# 2 вариант решения
s = input()
print(1, 2, 3, 4, 5, sep=s)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------

print(input(), end=' - Сказала она!')

------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------

print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------ 

# 1 вариант решения

n = int(input())
k = int(input())
print(k // n)

# 2 вариант решения
n,k=int(input()),int(input())
print(k // n)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Дано целое положительное число, ваша задача вывести разряд сотен этого числа
num = int(input())
print(num // 100 % 10)

------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------

# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

num = int(input())
digit_1 = num % 10
digit_2 = num // 10 % 10
digit_3 = num // 100
print(digit_1 + digit_2 + digit_3)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# У Олега в банке есть n евро. Он хочет снять всю сумму наличными. Номиналы еврокупюр равны 1, 5, 10, 20, 100. 
# Какое минимальное число купюр должен получить Олег после того, как снимет все деньги? На вход программе поступает одно
# положительные целое число n.
n = int(input())

bill_100 = n // 100
n %= 100
bill_20 = n // 20
n %= 20
bill_10 = n // 10
n %= 10
bill_5 = n // 5
n %= 5
bill_1 = n // 1
n %= 1
print(bill_100 + bill_20 + bill_10 + bill_5 + bill_1)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные
# часы в этот момент.
# 
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# 
# Учтите, что число n может быть больше, чем количество минут в сутках.

n = int(input())
n = n % 1440
print(n // 60, n % 60)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Дано целое число n. Выведите следующее за ним четное число.
# 
# Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.
n = int(input())
print((n // 2) + (n // 2) + 2)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
n = int(input())

hour = n // 3600
minute = n // 60 % 60
seconds = n - (hour * 3600) - minute * 60
print(hour, str(minute).zfill(2), str(seconds).zfill(2), sep=':')

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступает целое положительное число.
# 
# Программа должна вывести True, если у введенного числа последняя цифра 2, в противном случае - False.
# 
# Сделать задачу необходимо без использования условного оператора.

n = int(input())
print(n % 10 == 2)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход программе поступают два целых числа в одной строке.
# 
# Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.
# 
# Сделать задачу необходимо без использования условного оператора.
m, n = map(int, input().split())
print(m % 7 == 0 and n % 7 == 0)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступают три целых числа - стороны треугольника.
# 
# Необходимо вывести True, если данные стороны образуют правильный треугольник, в противном случае - False.
# 
# Сделать задачу необходимо без использования условного оператора.

a, b, c = map(int, input().split())
print(a == b and b == c)

# Тоже самое

a, b, c = map(int, input().split())
print(a == b == c)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступает целое число.
# 
# Программа должна вывести True, если введенное значение принадлежит интервалу от 5 не включительно до 19 включительно ,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.

n = int(input())
print(5 < n <= 19)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступают два слова.
# 
# Программа должна вывести True, если хотя бы одно слово равно слову "awesome".
# 
# Сделать задачу необходимо без использования условного оператора.
m = input()
n = input()
print(m == 'awesome' or n == 'awesome')
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступает целое положительное число.
# 
# Программа должна вывести True, если данное число является двузначным, в противном случае - False.
# 
# Сделать задачу необходимо без использования условного оператора.
# 
# Sample Input 1:
# 
# 77
# Sample Output 1:
# 
# True
# Sample Input 2:
# 
# 777
# Sample Output 2:
# 
# False

num = int(input())
print(10 <= num <= 99)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# На вход поступают три целых числа - стороны треугольника.
# 
# Необходимо вывести True, если данные стороны образуют прямоугольный треугольник, в противном случае - False.
# 
# Для написания программы необходимо вспомнить теорему Пифагора
# 
# Сделать задачу необходимо без использования условного оператора.
# 
# Sample Input 1:
# 
# 8 6 10
# Sample Output 1:
# 
# True
# Sample Input 2:
# 
# 5 6 5
# Sample Output 2:
# 
# False

a, b, c = map(int, input().split())
print(a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2)

# Или так

f = sorted(map(int, input().split()))
print(f[0]**2 + f[1]**2 == f[2]**2)
------------------------------------------------------------------------------------------------------------------
"""


"""
------------------------------------------------------------------------------------------------------------------

# После вечеринки компания из N человек хочет добраться домой с помощью такси. Максимальное количество человек, которое 
может уместиться в машину равно 4. Сколько машин придется вызвать ребятам, чтобы все могли уехать?
# 
# Программа получает на вход положительное целое число N - количество человек в компании.
# 
# Sample Input 1:
# 
# 16
# Sample Output 1:
# 
# 4
# Sample Input 2:
# 
# 9
# Sample Output 2:
# 
# 3

from math import ceil, floor

n = int(input()) / 4
print(ceil(n))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них. 
# 
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов 
# (числа не превышают 1000).
# 
# Разбор решения Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 5
# 6
# 7
# Sample Output 1:
# 
# 10
# Sample Input 2:
# 
# 1
# 1
# 2
# Sample Output 2:
# 
# 3


from math import ceil

cl_1 = int(input())
cl_2 = int(input())
cl_3 = int(input())
print(ceil(cl_1 / 2) + ceil(cl_2 / 2) + ceil(cl_3 / 2))
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
from math import ceil
l, w, h = map(int, input().split())
area = (l * h + w * h) * 2
print(ceil(area / 16))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
s ="Я стану крутым программистом!\n"
print(s * 3)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
word_1 = input()
word_2 = input()
word_3 = input()
print(word_3, word_2, word_1, sep='\n')

------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Вариант первый
sym_1, sym_2, sym_3 = map(str, input().split())
print("Simvol code", sym_1, "is", str(ord(sym_1)) + ".")
print("Simvol code", sym_2, "is", str(ord(sym_2)) + ".")
print("Simvol code", sym_3, "is", str(ord(sym_3)) + ".")

# Вариант второй
sym_1, sym_2, sym_3 = map(str, input().split())
print("Simvol code", sym_1, "is", ord(sym_1), end='.\n')
print("Simvol code", sym_2, "is", ord(sym_2), end='.\n')
print("Simvol code", sym_3, "is", ord(sym_3), end='.\n')

# Вариант третий
[print(f"Simvol code {el} is {ord(el)}.") for el in input().split()]
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Вариант первый
string_1 = input()[::-1]
print(string_1[::3])

# Вариант второй
string_2 = input()
print(string_2[-1::-3])
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
string = input()
print(string[-1] + string[:-1])
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# На вход подается строка. Ваша задача отформатировать строку так, чтобы первые 3 и последние 3 символа были заглавными,
# а оставшиеся строчные.
# 
# Примечание:
# Количество букв может быть различным, но гарантируется что их количество не меньше 6
# 
# Sample Input 1:
# 
# pyThon
# Sample Output 1:
# 
# PYTHON
# Sample Input 2:
# 
# прогРаммирОВАНИЕ
# Sample Output 2:


name = input()
print(name[:3].upper() + name[3:-3].lower() + name[-3:].upper())
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# На вход программе поступает строка, состоящая как из заглавных так из строчных букв. 
# Ваша задача преобразовать строку так, чтобы первая буква у каждого слова стала маленькой, 
# а остальные буквы превратились в заглавные. Символы пунктуации и цифры не нужно преобразовывать.
# 
# В качестве ответа нужно вывести полученную строку
# 
# 🚀>P.S.: Подсказка для решения 🚀
# Sample Input 1:
# 
# Every You Every Me
# Sample Output 1:
# 
# eVERY yOU eVERY mE
# Sample Input 2:
# 
# RunnING up That HILL
# Sample Output 2:
# 
# rUNNING uP tHAT hILL
# Sample Input 3:
# 
# Sleeping with GHOSTS
# Sample Output 3:
# 
# sLEEPING wITH gHOSTS

string = input().upper()
print((string.title().swapcase()))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
string = input()
print(string.count("e") + (string.count("E")))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
string = input().lower()
string = string.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
print('.', end='')
print('.'.join(string))

string = input().lower()
for i in string:
    if i not in 'aoyeui':
        print(f'.{i}', end='')
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
r = hex(int(input())).replace('x', '').upper()
g = hex(int(input())).replace('x', '').upper()
b = hex(int(input())).replace('x', '').upper()
print('#' + r[-2:], g[-2:], b[-2:], sep='')
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Напишите программу, которая считывает слово, затем выводит:

«Что Вы сказали? [это слово] ? Какое интересное слово».

Sample Input 1:

Конвульсия
Sample Output 1:

Что Вы сказали? Конвульсия? Какое интересное слово
Sample Input 2:

выхухоль
Sample Output 2:

Что Вы сказали? выхухоль? Какое интересное слово


print("Что Вы сказали? {word}? Какое интересное слово".format(word=input()))
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем формате «Здравствуйте, <фамилия> <имя>!»

Sample Input 1:

Петя
Иванов
Sample Output 1:

Здравствуйте, Иванов Петя!
Sample Input 2:

Никита
Рассказов
Sample Output 2:

Здравствуйте, Рассказов Никита!

# Первый вариант
name, last_name = input(), input()
print("Здравствуйте, {l} {n}!".format(n=name, l=last_name))

# Второй вариант
name, last_name = input(), input()
print(f"Здравствуйте, {last_name} {name}!")
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Напишите программу, которая считывает целое число, и затем сообщает какие числа будут 
следующим и предыдущим в определенном формате. Пробелы, знаки препинания, заглавные и строчные буквы важны!

Sample Input:

99
Sample Output:

Для числа 99 предыдущим будет число 98.
Для числа 99 следующим будет число 100.

# Первый вариант
num = int(input())
print("Для числа {n} предыдущим будет число {s_n}.".format(n=num, s_n=num - 1))
print("Для числа {n} следующим будет число {b_n}.".format(n=num, b_n=num + 1))

# Второй вариант
num = int(input())
print(f"Для числа {num} предыдущим будет число {num - 1}.")
print(f"Для числа {num} следующим будет число {num + 1}.")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
print(f"Мое имя {input()}!")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
name, age = input(),input()
print(f"Hello {name.upper()}. You are {age} years old.")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
name, yaer_of_birth = input(),int(input())
print(f"{name}, вам исполнится 77 лет в {yaer_of_birth + 77} ")
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Давайте при помощи F-строк выведем информацию о трех видах деления, которые мы с вами изучили ранее:
обычное деление, целочисленное и деление по остатку. 

Входные данные
На вход программе поступают два целых числа, при этом гарантируется, что второе число не равно 0.

Выходные данные 
Необходимо вывести результат трех видов деления первого числа на второе в определенном формате (см. примеры ниже)

Sample Input 1:

11
5
Sample Output 1:

11 / 5 = 2.2
11 // 5 = 2
11 % 5 = 1
Sample Input 2:

25
5
Sample Output 2:

25 / 5 = 5.0
25 // 5 = 5
25 % 5 = 0

num_1, num_2 = int(input()), int(input())
print(f"{num_1} / {num_2} = {num_1 / num_2}", f"{num_1} // {num_2} = {num_1 // num_2}",
      f"{num_1} % {num_2} = {num_1 % num_2}", sep='\n')
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Нашей программе поступает на вход x, y, z - три целых числа, обозначающие координаты вектора А.
Затем необходимо найти координаты вектора B, путем увеличения на 5 каждой из координаты вектора А.

Оба вектора необходимо распечатать в определенном формате

Sample Input 1:

1
2
3
Sample Output 1:

Vector A(1, 2, 3)
Vector B(6, 7, 8)
Sample Input 2:

-5
0
15
Sample Output 2:

Vector A(-5, 0, 15)
Vector B(0, 5, 20)

x, y, z = [int(input()) for i in range(3)]
print(f"Vector A({x}, {y}, {z})", f"Vector B({x + 5}, {y +5}, {z + 5})", sep='\n')
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число),
которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:

Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
You must pay <стоимость>

Sample Input 1:

56.77
11
Sample Output 1:

Current dollar rate is 56.77. You want to buy 11 dollars
You must pay 624.47
Sample Input 2:

77.25
75
Sample Output 2:

Current dollar rate is 77.25. You want to buy 75 dollars
You must pay 5793.75

dollar_rate, dollars_count = [float(input()) for i in range(2)]
print(f"Current dollar rate is {dollar_rate}. You want to buy {int(dollars_count)} dollars\n"
      f"You must pay {dollar_rate * dollars_count}")
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
x, y = [int(input()) for i in range(2)]
print(f"Точка({x = }, {y = })")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
number_pi = 3.141592653589793
print(f'{number_pi:.6f}')

a = 5 / 8
print(f"{a = :.4f}")

a = 5 / 8
print(f"{a = :.2f}")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
У курсов валют на биржах обычно указываются 4 знака после запятой,
 пример :43.3213
Но при купле/продаже обычно оставляют только два знака после запятой. В этом и будет заключаться,
ваша задача - принять вещественное число, и вывести его в формате двух знаков после запятой

price = float(input())
print(f"{price:.2f}")

print(f"{float(input()):.2f}")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Вводится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов под отображение числа.
Если в числе не хватает разрядов, необходимо выводить незначащие нули

Sample Input 1:

57
Sample Output 1:

0000000057
Sample Input 2:

84827642786827
Sample Output 2:

84827642786827
Sample Input 3:

378216
Sample Output 3:

0000378216

print(f"{int(input()):010d}")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Вводится целое число, необходимо выполнить выравнивание его по центру, отведя 15 символов под отображение числа.
Символом заполнителем должен являться знак дефиса -

Sample Input 1:

17
Sample Output 1:

------17-------
Sample Input 2:

123456789
Sample Output 2:

---123456789---

num = int(input())
print(f"{num:-^15}")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Вам необходимо подправить код ниже так, чтобы он выравнивал

1.первый print по центру
2. второй print по правому краю
3. третий print по левому краю
Количество знаков для выравнивания 20 символов, знак разделителя - &
s = input()
print(f"|{s:&^20}|\n|{s:&>20}|\n|{s:&<20}|")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
a = [1, 2, 7]
b = [34] + a
print((sum(a) + sum(b)) / (len(a) + len(b)))
print(f"{(sum(a) + sum(b)) / (len(a) + len(b)):.3f}")
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Вывести список из q, w, t 15 раз.

my_list = ["q", "w", "t"] * 15
print(my_list)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518,
           -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696,
           993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407,
           -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77,
           -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422,
           -895, 198, 284, 472, -986, -964, -989, 29]

print(min(my_list), max(my_list))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
Сумм введённых чисел через пробел

print(sum(list(map(int, input().split()))))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
num = list(map(int, input().split()))
print(sum(num) / len(num))
------------------------------------------------------------------------------------------------------------------
"""
# a =map(int, input().split())
# print(a)
# b = input().split()
# print(b)
# c = [i for i in input().split()]
# print(c)
#
# print(input().split()[1])
# print([int(i) for i in input().split()[1::3]])
# print(list(map(int, input().split()[::-1])))

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1], top[2] = "Сверхъестественное", "Настоящий детектив"
# print(top)
# top[1::2] = ["Yelowstone", "WAR", "Club"]
# print(top)
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# print(months[int(input()) - 1])
"""
------------------------------------------------------------------------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
count = 0
num = int(input())
for i in range(1, num):
    count += 1
print(months[count])
------------------------------------------------------------------------------------------------------------------
"""
# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# for i in range(len(numbers)):
#     if i == 5:
#         numbers.insert(i, 111)
#     if i == 8:
#         numbers.insert(i, 222)
#     if i == 0:
#         numbers.insert(i, 789)
#     if i == 11:
#         numbers.insert(i, 201)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers_del =[]
# numbers_del.append(numbers.pop())
# numbers_del.append(numbers.pop(0))
# numbers_del.append(numbers.pop(12))
# numbers_del.append(numbers.pop(7))
# print(numbers)
# print(sum(numbers_del))

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True)
# print(numbers)

# Перевернуть значение списока из полученных чисел
#
# 1ый вариант
# a = list(map(int, input().split()))
# a.reverse()
# print(a)
#
# 2ой вариант
# a = list(map(int, input().split()))
# print(a[::-1])

"""
------------------------------------------------------------------------------------------------------------------
Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

a = list(map(int, input().split()))
Sample Input 1:

8 11 5 6 9
Sample Output 1:

0
Sample Input 2:

99 999 9 999
Sample Output 2:

2

# 1ый вариант
a = [int(i) for i in input().split()]
print(a.count(999))

# 2ой вариант
print([int(i) for i in input().split()].count(999))
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# В вашем распоряжении список numbers. Ваша задача скопировать все содержимое списка numbers в новую переменную
# copy_numbers
#
#  В качестве ответа необходимо вывести список copy_numbers
#
# 1ый вариант
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
copy_numbers = numbers.copy()
copy_numbers[0] = 34
print(copy_numbers)
print(numbers)

# 2ой вариант
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
copy_numbers = numbers[:]
copy_numbers[0] = 34
print(copy_numbers)
print(numbers)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# a = [str(i) for i in input().upper().split()]
# print(*a[0], sep='-', end=' ')
# print(*a[1], sep='-')
#
# print(*['-'.join(i) for i in input().upper().split()])
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# name, mid_name, last_name = [str(i) for i in input().split()]
# print(f"{last_name} {name[0]}.{mid_name[0]}.")
#
# name, mid_name, last_name = input().split()
# print(f"{last_name} {name[0]}.{mid_name[0]}.")
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Напишите программу, которая выводит слова введённой строки (части, разделённые символами пустого пространства)
 в столбик. Нужно обойтись только методами split и join у строк, в программе должен быть всего один вызов print.
 Sample Input:

Буря мглою небо кроет
Sample Output:

Буря
мглою
небо
кроет

 
print('\n'.join(input().split()))
------------------------------------------------------------------------------------------------------------------
"""
a = int(input())
if a % 2 == 0:
    print("Чётное")
else:
    print("Не чётное")
