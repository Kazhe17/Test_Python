# 1
a = []
n = int(input('input rows...'))
m = int(input('input columns'))

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input('input numbers...')))
    a.append(b)
for i in a:
    print(i)

# 2
a = []
n = int(input())
for i in range(n):
    a.append([0] * n)
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i < j:
            a[i][j] = 3
        else:
            a[i][j] = 5

for i in a:
    print(i)
