n = int(input())
a = []
for x in range(n):
    a.append(['.']*n)
for e in range(n):
    a[e][(n-e)-1] = '1'
    a[e][] = '0'
for z in a:
    print((' '.join(z)))