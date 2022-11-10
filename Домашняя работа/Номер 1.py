n = int(input())
a = []
t = 0
for x in range(n):
    a.append(['.']*n)
for e in range(n):
    a[e][e] = '0'
for z in a:
    print((' '.join(z)))

# не получилось