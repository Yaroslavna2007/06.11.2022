#Дано число n. Создай массив размером n×n и заполни его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0. Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведи на экран. Числа в строке разделяй одним пробелом.

n = int(input())
a = []
for x in range(n):
    a.append(['.']*n)
for e in range(n):
    for w in range(n):
        if e + w == n-1:
            a[e][w] = '1'
        elif e + w > n -1:
            a[e][w] = '2'
        elif e +w < n-1:
            a[e][w] = '0'
for z in a:
    print((' '.join(z)))