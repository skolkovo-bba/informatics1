n = int(input())
m = int(input())

d = [0] *  (m * n)

for i in range(0, n):
    for j in range(0, m):
        d[i * m + j] = int(input())

d.sort()

for i in range(0, n):
    print(*d[i * m: i * m + m])
