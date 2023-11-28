"""
------------------------------------------------------------------------------------------------------------------
# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
#
# Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.
#
#
#
# Отличительной особенностью элементов, расположенных на главной диагонали, является то,
# что у них номер строки совпадает с номером столбца.
# У всех остальных элементов матрицы номера строки и столбца различаются
#
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке,
# а затем в N строках записаны элементы списка.
#
# Sample Input 1:
#
# 2
# 1 2
# 3 4
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 2:
#
# 15


n = int(input())
matrix = []
dig_summ = 0

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            dig_summ += matrix[i][j]

print(dig_summ)

    ------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы сверху вниз слева 
направо и вывести элементы именно в таком порядке в виде таблицы. 

Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих
 N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.

Sample Input 1:

5
3 4 9 1 2
8 2 0 5 1
4 7 4 8 7
7 1 3 3 8
5 6 3 7 0
Sample Output 1:

3 8 4 7 5
4 2 7 1 6
9 0 4 3 3
1 5 8 3 7
2 1 7 8 0

Sample Input 2:

2
6 7
9 0
Sample Output 2:

6 9
7 0

n = int(input())
matrix =[]

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы
# снизу вверх справа налево и вывести элементы именно в таком порядке в виде таблицы. 
# 
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. 
# В каждой из последующих N строк записаны N целых чисел – элементы матрицы. 
# 
# Разбор задачи Youtube Boosty Patreon
# 
# Sample Input 1:
# 
# 5
# 3 4 9 6 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
# Sample Output 1:
# 
# 0 8 7 1 2
# 7 3 8 5 6
# 3 3 4 0 9
# 6 1 7 2 4
# 5 7 4 8 3
# 
# Sample Input 2:
# 
# 3
# 5 4 1
# 6 7 9
# 9 3 0
# Sample Output 2:
# 
# 0 9 1
# 3 7 4
# 9 6 5
# 
# Sample Input 3:
# 
# 4
# 6 8 4 3
# 9 1 6 5
# 0 5 3 9 
# 5 3 4 7 
# Sample Output 3:
# 
# 7 9 5 3
# 4 3 6 4
# 3 5 1 8
# 5 0 9 6

matrix = [[*map(int, input().split())] for i in range(int(input()))]

for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix)-1, -1, -1):
        print(matrix[j][i], end=' ')
    print()
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы
# cправа налево сверху вниз и вывести элементы именно в таком порядке в виде таблицы. 
# 
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы.
# В каждой из последующих N строк записаны M целых чисел – элементы матрицы.
# 
# Sample Input 1:
# 
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
# 
# 6 2 9 5
# 3 4 2 6
# 7 8 2 1
# 
# Sample Input 2:
# 
# 5 3
# 1 4 5
# 2 5 3
# 7 3 2
# 6 7 9 
# 1 6 9
# Sample Output 2:
# 
# 5 4 1
# 3 5 2
# 2 3 7
# 9 7 6
# 9 6 1

n, m = map(int, input().split())

matrix = [[*map(int, input().split())] for i in range(n)]

for i in range(n):
    for j in range(m - 1, -1, -1):
        print(matrix[i][j], end=' ')
    print()
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы
# слева направо снизу вверх и вывести элементы именно в таком порядке в виде таблицы. 
# 
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы.
# В каждой из последующих N строк записаны M целых чисел – элементы матрицы. 
# 
# Sample Input 1:
# 
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
# 
# 1 2 8 7
# 6 2 4 3
# 5 9 2 6
# 
# Sample Input 2:
# 
# 4 2 
# 1 5
# 6 3
# 8 6
# 3 9
# Sample Output 2:
# 
# 3 9
# 8 6
# 6 3
# 1 5

n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]

for row in range(len(matrix)-1, -1, -1):
    for column in range(m):
        print(matrix[row][column], end=' ')
    print()
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Перед Вами матрица размера 5 × 5, состоящая из 24-x нулей и единственной единицы. 
# Строки матрицы пронумеруем числами от 1 до 5 сверху вниз, столбцы матрицы пронумеруем числами от 1 до 5 слева направо.
# За один ход разрешается применить к матрице одно из двух следующих преобразований:
# 
# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i + 1 для некоторого 
# целого i (1 ≤ i < 5).
# Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j + 1 для некоторого
# целого j (1 ≤ j < 5).
# Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы будет
# находиться в ее центре (в клетке, которая находится на пересечении третьей строки и третьего столбца). Посчитайте,
 какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.
# 
# Входные данные
# 
# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых чисел:
# j-ое число в i-ой строке входных данных обозначает элемент матрицы, стоящий на пересечении i-ой строки и j-ого столбца.
# Гарантируется, что матрица состоит из 24-x нулей и единственной единицы.
# 
# Выходные данные
# 
# Выведите единственное целое число — минимальное количество действий, которое требуется, чтобы сделать матрицу красивой.
# 
# Решение задачи Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 1:
# 
# 2
# Sample Input 2:
# 
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# Sample Output 2:
# 
# 1
# Sample Input 3:
# 
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 0 0 0
# Sample Output 3:
# 
# 2
# Sample Input 4:
# 
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# Sample Output 4:
# 
# 4


matrix = [[*map(int, input().split())]for i in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i
            column = j

print(abs(row - 2) + abs(column - 2))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. Требуется вычислить сумму элементов
# в каждой строке и в каждом столбце.
# 
# Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива.
# В каждой из последующих N строк записаны M целых чисел – элементы массива. Все числа во входных данных не превышают
 1000 по абсолютной величине.
# 
# В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
# 
# Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.
# 
# Sample Input 1:
# 
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
# 
# 22 15 18
# 12 13 14 16
# 
# Sample Input 2:
# 
# 2 5
# 1 6 4 7 9
# 4 7 3 8 2
# Sample Output 2:
# 
# 27 24
# 5 13 7 15 11

n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]
row_result = 0
overall_rows_results = []
column_result = 0
overall_columns_results = []

for row in range(len(matrix)):
    for column in range(m):
        row_result += matrix[row][column]
    overall_rows_results.append(row_result)
    row_result = 0

for column in range(m):
    for row in range(len(matrix)):
        column_result += matrix[row][column]
    overall_columns_results.append(column_result)
    column_result = 0

print(*overall_rows_results)
print(*overall_columns_results)
------------------------------------------------------------------------------------------------------------------
"""


"""
------------------------------------------------------------------------------------------------------------------
# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та,
# которая идёт из левого верхнего угла двумерного массива в правый нижний.
#
# Входные данные
#
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3
# 0 1 2
# 1 5 3
# 2 3 4
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# 3
# 0 0 0
# 0 0 0
# 1 0 0
# Sample Output 2:
#
# No
# Sample Input 3:
#
# 5
# 0 0 0 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 3:
#
# No
# Sample Input 4:
#
# 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 4:
#
# Yes


# 1 вариант
# n = int(input())
# matrix = [[*map(int, input().split())] for i in range(n)]
# count_yes = 0
# count_no = 0
#
# for i in range(len(matrix)):
#     for j in range(n):
#         if i == j:
#             continue
#         if matrix[i][j] != matrix[j][i]:
#             count_no += 1
#         else:
#             count_yes += 1
#
# print("yes" if count_no == 0 else "no")

# 2 вариант


n = int(input())
matrix = [[*map(int, input().split())] for i in range(n)]
result = "Yes"

for i in range(len(matrix)):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = "No"
            break

print(result)

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем считается тот спортсмен,
# у которого сумма результатов по всем броскам максимальна.
# Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1, 
# то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел.
# Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки,
# для которой достигается эта сумма.
# 
# Входные данные
# 
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
# 
# Выходные данные
# 
# Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается. Если таких строк несколько,
# то выводится номер наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0.
# 
# Sample Input 1:
# 
# 2 2
# 5 4
# 3 5
# Sample Output 1:
# 
# 9
# 0
# Sample Input 2:
# 
# 3 4
# 1 2 3 4
# 9 10 11 12
# 5 6 7 8
# Sample Output 2:
# 
# 42
# 1
# Sample Input 3:
# 
# 1 1
# 5
# Sample Output 3:
# 
# 5
# 0
# Sample Input 4:
# 
# 3 5
# 1 2 3 4 5
# 3 3 3 3 3
# 5 4 3 2 1
# Sample Output 4:
# 
# 15
# 0

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for i in range(n)]
result = []

for i in range(len(matrix)):
    if sum(matrix[i]) in result:
        continue
    else:
        result.append(sum(matrix[i]))

print(max(result))
print(result.index(max(result)))

------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем соревнований объявляется
# тот спортсмен, у которого максимален наилучший результат по всем броскам. Таким образом, программа должна найти
# значение максимального элемента в данном массиве, а также его индексы (то есть номер спортсмена и номер попытки).
# 
# Входные данные
# 
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
# 
# Выходные данные
# 
# Программа выводит значение максимального элемента, затем номер строки и номер столбца, в котором он встречается. 
# Если в массиве несколько максимальных элементов, то нужно вывести минимальный номер строки,
# в которой встречается такой элемент, а если в этой строке таких элементов несколько,
# то нужно вывести минимальный номер столбца. Не забудьте, что все строки и столбцы нумеруются с 0.
# 
# Разбор задачи Youtube Boosty Patreon
# 
# Sample Input 1:
# 
# 3 3
# 3 1 2
# 1 3 4
# 3 3 3
# Sample Output 1:
# 
# 4
# 1 2
# Sample Input 2:
# 
# 3 3
# 7 5 3
# 4 2 1
# 16 8 9
# Sample Output 2:
# 
# 16
# 2 0
# Sample Input 3:
# 
# 3 4
# 7 5 3 5
# 4 2 1 9
# 6 8 9 10
# Sample Output 3:
# 
# 10
# 2 3
# Sample Input 4:
# 
# 2 4
# 7 5 9 9
# 9 2 1 9
# Sample Output 4:
# 
# 9
# 0 2
# Sample Input 5:
# 
# 3 2
# 7 7
# 7 7
# 7 7
# Sample Output 5:
# 
# 7
# 0 0


# 1 Вариант

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for i in range(n)]
count_max_elem = 0
result_max = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] <= count_max_elem:
            continue
        else:
            result_max.clear()
            count_max_elem = matrix[i][j]
            result_max.append(matrix[i][j])
            result_max.append(i)
            result_max.append(j)


print(result_max[0])
print(result_max[1], result_max[2])


# 2 Вариант

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for i in range(n)]
num_str = 0
num_row = 0
result_max = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] <= result_max:
            continue
        else:
            result_max = matrix[i][j]
            num_str = i
            num_row = j


print(result_max)
print(num_str, num_row)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен,
# у которого максимален наилучший бросок. Если таких несколько, то из них побеждает тот, 
# у которого наилучшая сумма результатов по всем попыткам. Если и таких несколько, 
# победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.
# 
# Входные данные
# 
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
# 
# Выходные данные
# 
# Программа должна вывести одно число - номер победителя соревнований. Не забудьте,
# что  строки  (спортсмены) нумеруются с 0.
# 
# Решение задачи Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 3 3
# 1 2 7
# 1 3 5
# 4 1 6
# Sample Output 1:
# 
# 0
# Sample Input 2:
# 
# 2 3
# 1 2 7
# 1 7 5
# Sample Output 2:
# 
# 1
# Sample Input 3:
# 
# 2 3
# 7 5 7
# 7 7 5
# Sample Output 3:
# 
# 0
# Sample Input 4:
# 
# 4 4
# 9 9 9 9
# 8 8 8 8
# 1 1 10 1
# 7 7 7 7
# Sample Output 4:
# 
# 2
# Sample Input 5:
# 
# 4 4
# 5 5 5 5
# 7 7 7 7
# 4 4 4 4
# 7 7 7 7
# Sample Output 5:
# 
# 1


n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]
max_result = 0
num_of_sport = 0
count_points = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_result:
            max_result = matrix[i][j]
            num_of_sport = i
            count_points = sum(matrix[i])
        if matrix[i][j] == max_result and sum(matrix[i]) > count_points:
            max_result = matrix[i][j]
            num_of_sport = i
            count_points = sum(matrix[i])

print(num_of_sport)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
# Победитель определяется по лучшему результату. Определите количество участников состязаний,
# которые разделили первое место, то есть определите количество строк в массиве, которые содержат значение, 
# равное наибольшему.
# 
# Входные данные
# 
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
# 
# Выходные данные
# 
# Программа должна вывести  одно число - количество победителей соревнования.
# 
# Разбор Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 3 3
# 3 1 2
# 1 3 4
# 4 3 3
# Sample Output 1:
# 
# 2
# Sample Input 2:
# 
# 4 3
# 7 8 9
# 9 3 10
# 4 3 8
# 5 6 7
# Sample Output 2:
# 
# 1
# Sample Input 3:
# 
# 5 5
# 1 5 2 3 5
# 1 3 2 3 5
# 4 1 4 2 4
# 5 5 2 1 5
# 5 5 1 2 5
# Sample Output 3:
# 
# 4


# 1 Вариант (Много лишних действий)

n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]
max_scores = []
score_count = 0

for i in range(len(matrix)):
    score_count = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] > score_count:
            score_count = matrix[i][j]
            max_scores.append(score_count)

print(max_scores.count(max(max_scores)))

# 2 Вариант
n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]
max_scores = []

for i in range(len(matrix)):
    max_scores.append(max(matrix[i]))
print(max_scores.count(max(max_scores)))
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# На днях Иван у себя в прихожей выложил кафель, состоящий из квадратных черных и белых плиток.
# Прихожая Ивана имеет квадратную форму 4х4, вмещающую 16 плиток. Теперь Иван переживает, что узор из плиток,
# который у него получился, может быть не симпатичным. С точки зрения дизайна симпатичным узором считается тот,
# который не содержит в себе квадрата 2х2, состоящего из плиток одного цвета.
# 
# Примеры возможных узоров:
# 
# Симпатичный узор
# 
# По заданному расположению плиток в прихожей Ивана требуется определить: является ли выполненный узор симпатичным.
# 
# Программе поступает на вход 4 строки по 4 символа «W» или «B» в каждой, описывающие узор из плиток. 
# Символ «W» обозначает плитку белого цвета, а «B» - черного.
# 
# Ваша задача вывести «Yes», если узор является симпатичным и «No» в противном случае.
# 
# Sample Input 1:
# 
# BWBW
# BBWB
# WWBB
# BWWW
# Sample Output 1:
# 
# Yes
# Sample Input 2:
# 
# BBWB
# BBWB
# WWBW
# BBWB
# Sample Output 2:
# 
# No

drawing = [list(input()) for i in range(4)]
answear = ["Yes", "No"]
count = 0


for i in range(len(drawing) - 1):
    for j in range(len(drawing[i]) - 1):
        if drawing[i][j] == drawing[i + 1][j] == drawing[i][j + 1] == drawing[i][j + 1] == drawing[i - 1][j] == drawing[i][j - 1]:
            count = 1
            break

print(answear[count])
print(drawing)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Миша уже научился хорошо фотографировать и недавно увлекся программированием. Первая программа, которую он написал,
# позволяет формировать негатив бинарного черно-белого изображения.
# 
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным,
# либо белым. Негатив такого изображения получается путем замены каждого черного пикселя на белый,
# а каждого белого пикселя – на черный.
# 
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться
# некорректный негатив. Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению,
# Миша начал тестировать свою программу.
# 
# В качестве входных данных он использовал исходные изображения. Сформированные программой негативы он начал тщательно
# анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
# 
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение
# и полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
# 
# Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях).
# Последующие n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W». 
# Символ «B» соответствует черному пикселю, а символ «W» – белому. Далее следует пустая строка,
# а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное изображение.
# 
# Необходимо вывести на экран число пикселей негатива, которые неправильно сформированы Мишиной программой.
# 
# Решение задачи Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 3 4
# WBBW
# BBBB
# WBBW
# 
# BWWW
# WWWB
# BWWB
# Sample Output 1:
# 
# 2
# Sample Input 2:
# 
# 2 2
# BW
# BB
# 
# WW
# BW
# Sample Output 2:
# 
# 2

n, m = map(int, input().split())
b_w_picture = [input() for i in range(n)]
input()
misha_result = [input() for i in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if b_w_picture[i][j] == misha_result[i][j]:
            count += 1

print(count)
------------------------------------------------------------------------------------------------------------------
"""

# a = [['asdt'], ['fght'], ['tyu']]
# b = ['fgty', 'turyf', 'tiyuh']
#
# # print(a[1][2])
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         print(b[i][j], end='')
#     print()

"""
------------------------------------------------------------------------------------------------------------------
# Рассмотрим таблицу из n строк и n столбцов. Известно, что в клетке, образованной пересечением i-й строки и j-го столбца,
# записано число i × j. Строки и столбцы нумеруются с единицы.
# 
# Дано целое положительное число x. Требуется посчитать количество клеток таблицы, в которых находится число x.
# 
# Входные данные
# 
# В единственной строке находятся числа n и x — размер таблицы и число,
# которое мы ищем в таблице.
# 
# Выходные данные
# 
# Выведите единственное число: количество раз, которое число x встречается в таблице.
# 
# Решение задачи Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 10 5
# Sample Output 1:
# 
# 2
# Sample Input 2:
# 
# 6 12
# Sample Output 2:
# 
# 4
# Sample Input 3:
# 
# 5 13
# Sample Output 3:
# 
# 0

n, x = map(int, input().split())
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == x:
            count += 1

print(count)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Дана матрица размером NxN, требуется найти максимальное значение среди элементов, расположенных на побочной диагонали.
# 
# Под побочной диагональю матрицы подразумевается диагональ, проведённая из правого верхнего угла до левого нижнего угла.
# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, 
# а затем в N строках записаны элементы списка.
# 
# Выходные данные
# Вывести самой большой элемент на побочной диагонали
# 
# Sample Input 1:
# 
# 2
# 1 2
# 3 4
# Sample Output 1:
# 
# 3
# Sample Input 2:
# 
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 2:
# 
# 7
# Sample Input 3:
# 
# 5
# 100 2 3 90 100
# 1 54 3 90 100
# 1 2 5 90 100
# 1 2 3 2 100
# 1 2 3 90 100
# Sample Output 3:
# 
# 100

matrix = [list(map(int, input().split())) for i in range(int(input()))]
max_num = 0

for i in range(len(matrix)):
    j = len(matrix) - 1 - i
    if matrix[i][j] > max_num:
        max_num = matrix[i][j]

print(max_num)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# Заполнение матрицы
# Ваша задача сформировать квадратную матрицу размером NxN, в которой используется следующее заполнение:
# 
# все элементы, находящиеся выше главной диагонали, заполняются значением A;
# все элементы, находящиеся ниже главной диагонали, заполняются значением B;
# все элементы, находящиеся на главной диагонали, заполняются значением C.
# В качестве ответа, выведите на экран полученную матрицу
# 
# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в матрицы,
# а затем на новой строке три целых числа  A, B и C. Данные числа используются для заполнения
# 
# Выходные данные
# Заполните и распечатайте матрицу
# 
# Sample Input 1:
# 
# 3
# 1 0 3
# Sample Output 1:
# 
# 3 1 1
# 0 3 1
# 0 0 3
# Sample Input 2:
# 
# 5
# 7 2 1
# Sample Output 2:
# 
# 1 7 7 7 7
# 2 1 7 7 7
# 2 2 1 7 7
# 2 2 2 1 7
# 2 2 2 2 1
# Sample Input 3:
# 
# 6
# 0 0 1
# Sample Output 3:
# 
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1

# 1 Вариант
n = int(input())
a, b, c = map(int, input().split())

for i in range(n):
    for j in range(n):
        if i == j:
            print(c, end=' ')
        elif i > j:
            print(b, end=' ')
        else:
            print(a, end=' ')
    print()

# 2 Вариант
n = int(input())
a, b, c = map(int, input().split())
for i in range(n):
    print(*[(c if i == j else b if i > j else a) for j in range(n)])

------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Манао работает на спортивном телевидении. Он долгое время наблюдал за футбольными матчами чемпионата одной страны и
# начал замечать разные закономерности. Например, у каждой команды есть две формы: домашняя и выездная. Когда команда 
# проводит матч на своем стадионе, футболисты надевают домашнюю форму, а когда на чужом — выездную. 
# Единственное исключение из этого правила — когда цвет домашней формы принимающей команды совпадает
# с цветом формы гостей. В таком случае домашняя команда облачается в свою выездную форму. 
# Цвета домашней и выездной формы для каждой команды различны.
# 
# В чемпионате страны участвует n команд и он состоит из n матчей: каждая из команд принимает каждую
# другую команду на своем стадионе. Манао задумался, а сколько раз в течение одного чемпионата случится, что команда,
# играющая на своем стадионе, оденет выездную форму? Обратите внимание, что для подсчета этого количества 
# порядок матчей не играет никакого значения.
# 
# Вам даны цвета домашней и выездной формы каждой команды. Для удобства эти цвета пронумерованы целыми 
# числами таким образом, что никакие два разных цвета не имеют одинаковый номер. Помогите Манао найти ответ на его вопрос.
# 
# Входные данные
# В первой строке содержится целое число n. В каждой из следующих n строк записана пара
# разделенных одним пробелом различных целых чисел hi, ai — номер цвета домашней и выездной форм i-ой команды
# соответственно.
# 
# Выходные данные
# В единственной строке выведите количество матчей, в которых домашняя команда выступит в выездной форме.
# 
# Разбор задачи Youtube Patreon Boosty
# 
# Sample Input 1:
# 
# 3
# 1 2
# 2 4
# 3 4
# Sample Output 1:
# 
# 1
# Sample Input 2:
# 
# 4
# 100 42
# 42 100
# 5 42
# 100 5
# Sample Output 2:
# 
# 5
# Sample Input 3:
# 
# 2
# 1 2
# 1 2
# Sample Output 3:
# 
# 0

# 1 Вариант
home_away = [[*map(int, input().split())]for i in range(int(input()))]
count = 0
for i in range(len(home_away)):
    for j in range(i + 1, len(home_away)):
        if home_away[i][0] == home_away[j][1]:
            count += 1
        if home_away[i][1] == home_away[j][0]:
            count += 1

print(count)


# 2 Вариант
home_away = [[*map(int, input().split())]for i in range(int(input()))]
count = 0
for i in range(len(home_away)):
    for j in range(len(home_away)):
        if home_away[i][0] == home_away[j][1]:
            count += 1
print(count)
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
«Морской бой» - игра для двух участников, в которой игроки по очереди называют координаты на неизвестной им карте
соперника. Если у соперника по этим координатам имеется корабль, то корабль или его часть «топится»,
а попавший получает право сделать еще один ход. Цель игрока - первым поразить все корабли противника.

«Морской бой» очень популярен среди учеников одной физико-математической школы.
Ребята очень любят в него играть на переменах. Вот и сейчас ученики Иннокентий и Емельян начали новую партию.

Правила, по которым ребята расставляют корабли перед началом партии, несколько отличаются от классических.
Во-первых, игра происходит на поле размером N×M, а не 10×10. Во-вторых, число кораблей,
их размер и форма выбираются ребятами перед партией - так играть намного интереснее.

Емельян уже расставил все свои корабли, кроме одного однопалубного. Такой корабль занимает ровно одну клетку.

Задана расстановка кораблей Емельяна. Найдите число способов поставить оставшийся однопалубный корабль.
При этом учитывайте, что по правилам его можно ставить только в ту клетку, все соседние с которой не заняты.
В этой задаче соседними считаются клетки, имеющие общую сторону.

Программа считывает два числа: N и M (1 ≤ N, M ≤ 100).
Последующие N строк описывают игровое поле - каждая из них содержит M символов.
Символом «.» (точка) обозначена свободная клетка, символом «*» (звездочка) - занятая кораблем.

Необходимо вывести на экран ответ на задачу

Разбор задачи 

Sample Input 1:

4 4
****
**..
*...
*...
Sample Output 1:

4
Sample Input 2:

4 3
***
...
...
***
Sample Output 2:

0
Sample Input 3:

2 3
...
...
Sample Output 3:

6
Sample Input 4:

3 5
***..
..**.
...**
Sample Output 4:

3

n, m = map(int, input().split())
playing_field = ['.' * (m + 2)]

for i in range(n):
    row = '.' + input() + '.'
    playing_field.append(row)
playing_field.append('.' * (m + 2))

count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if playing_field[i - 1][j] == '.' and playing_field[i + 1][j] == '.' and playing_field[i][j - 1] == '.' and playing_field[i][j + 1] == '.' and playing_field[i][j] == '.':
            count += 1

print(count)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Дана прямоугольная матрица размером NxM, в которой заполнены значения только в первом столбце и в первом ряду.
Все остальные элементы равны нулю и мы считаем их незаполненными.

Ваша задача заполнить каждый пустой элемент путем сложения соседа слева и соседа сверху.Начинать нужно с тех элементов,
у которых оба указанных соседа заполнены (не равны нулю)

Входные данные
Программа сперва принимает в одной строке на вход два числа N и M - количество строк и столбцов в списке,
а затем в N строках записаны элементы списка.

Выходные данные
Вывести заполненную матрицу

Sample Input 1:

5 4
1 1 1 1
1 0 0 0
1 0 0 0
1 0 0 0
1 0 0 0
Sample Output 1:

1 1 1 1
1 2 3 4
1 3 6 10
1 4 10 20
1 5 15 35
Sample Input 2:

3 6
5 3 1 4 4 4
3 0 0 0 0 0
1 0 0 0 0 0
Sample Output 2:

5 3 1 4 4 4
3 6 7 11 15 19
1 7 14 25 40 59
Sample Input 3:

6 3
5 1 2
5 0 0
5 0 0
5 0 0
2 0 0
5 0 0
Sample Output 3:

5 1 2
5 6 8
5 11 19
5 16 35
2 18 53
5 23 76
n, m = map(int, input().split())
matrix = []


for i in range(n):
    row = [*map(int, input().split())]
    matrix.append(row)

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]


for row in matrix:
    print(*row)
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Дана прямоугольная матрица размером NxM, в которой заполнены значения только в последнем столбце и в последнем ряду.
Все остальные элементы равны нулю и мы считаем их незаполненными.

Ваша задача заполнить каждый пустой элемент путем сложения соседа справа и соседа снизу. Начинать нужно с тех элементов,
у которых оба указанных соседа заполнены (не равны нулю)

Входные данные
Программа сперва принимает в одной строке на вход два числа N и M - количество строк и столбцов в списке,
а затем в N строках записаны элементы списка.

Выходные данные
Вывести заполненную матрицу

Sample Input 1:

4 4
0 0 0 1
0 0 0 1
0 0 0 1
1 1 1 1
Sample Output 1:

20 10 4 1
10 6 3 1
4 3 2 1
1 1 1 1
Sample Input 2:

3 5
0 0 0 0 4
0 0 0 0 2
4 4 2 5 4
Sample Output 2:

50 33 20 11 4
17 13 9 7 2
4 4 2 5 4
Sample Input 3:

4 8
0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 3
4 3 4 4 4 4 5 3
Sample Output 3:

464 324 215 133 75 37 15 5
140 109 82 58 38 22 10 2
31 27 24 20 16 12 8 3
4 3 4 4 4 4 5 3

  # 1ый вариант
  
n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = matrix.append([*map(int, input().split())])

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        matrix[i][j] = matrix[i][j + 1] + matrix[i + 1][j]

for row in matrix:
    print(*row)
    

  # 2ой вариант
  
n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

[print(*matrix[row]) for row in range(n)]

------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

Sample Input 1:

4 10
Sample Output 1:

0  1  2  3  4  5  6  7  8  9
19 18 17 16 15 14 13 12 11 10
20 21 22 23 24 25 26 27 28 29
39 38 37 36 35 34 33 32 31 30
Sample Input 2:

3 4
Sample Output 2:

0 1 2 3 
7 6 5 4 
8 9 10 11
Sample Input 3:

10 2
Sample Output 3:

0 1 
3 2 
4 5 
7 6 
8 9 
11 10 
12 13 
15 14 
16 17 
19 18 
Sample Input 4:

5 5
Sample Output 4:

0 1 2 3 4 
9 8 7 6 5 
10 11 12 13 14 
19 18 17 16 15 
20 21 22 23 24 
Sample Input 5:

1 1
Sample Output 5:

0

n, m = map(int, input().split())
matrix = []
count = 0

for i in range(n):
    if i % 2 != 0:
        a = [i for i in range(count, count + m)]
        a.reverse()
        matrix.append(a)
    else:
        matrix.append([i for i in range(count, count + m)])
    count += m

[print(*matrix[row]) for row in range(n)]

------------------------------------------------------------------------------------------------------------------
"""