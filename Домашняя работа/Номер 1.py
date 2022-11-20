n = int(input())
a = []
t = 1
for x in range(n):
    a.append(['.']*n)
for e in range(n):
    for w in range(n):
        a[e][w] = str(abs(e-w))
for z in a:
    print((' '.join(z)))