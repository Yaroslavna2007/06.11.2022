#Дан двумерный массив и два числа: i и j.
# Поменяй в массиве столбцы с номерами i и j и выведи результат.
#Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
#Решение оформи в виде функции swap_columns(a, i, j).

n = int(input())
m = int(input())
i = int(input())
j = int(input())
x = []
y = []
for u in range(m):
    a = str(input('элемент массива'))
    x.append(a)
for t in range(n):
    y.append(x)
print(y)
for p in y:
    print((' '.join(p)))