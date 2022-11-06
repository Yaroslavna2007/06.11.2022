n = int(input())
a = []
for x in range(n):
    a.append(['.']*n)
for e in range(n):
    for w in range(n):
        a[e][w] = '0'
for z in a:
    print((' '.join(z)))