n = int(input())
m = int(input())
x = []
y = []
for u in range(m):
    a = int(input('элемент массива'))
    x.append(a)
    for t in range(n):
        y.append(x)
for p in y:
    print((' '.join(p)))