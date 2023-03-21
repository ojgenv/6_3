import random

n = int(input('Введите количество элементов в массиве '))
print (n)
list_t = []
y = 0
min1 = 10
min2 = 10
z = 0

for i in range(n):
    list_t.append(random.randint(0,9))

print(*list_t)
x = int(input('Введите искомый элемент '))

for i in range(n):
    if (list_t[i] == x):
        y = x
        z += 1 
    else:
        min2 = abs(x - list_t[i])
        if min2 < min1:
            min1 = min2
            y = list_t[i]

print(x)
print("ближайший элемент", y)
print("встречается", z, "раз(а)")