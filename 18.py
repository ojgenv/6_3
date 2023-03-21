"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5"""

import random

n = int(input('Введите количество элементов в массиве '))
print (n)
list_t = []
y = 0
min1 = 10
min2 = 10

for i in range(n):
    list_t.append(random.randint(0,9))

print(*list_t)
x = int(input('Введите искомый элемент '))

for i in range(n):
    if (list_t[i] == x):
        y = x
        break
    else:
        min2 = abs(x - list_t[i])
        if min2 < min1:
            min1 = min2
            y = list_t[i]

print (x)
print("->", y)