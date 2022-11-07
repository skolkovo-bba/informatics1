n = int(input())

d = [[0] * n for _ in range(n)]

for i in range(n):
    k = list(map(int, input().split()))
    for j in range(n):
        d[j][n - 1 - i] = k[j]

for i in range(n):
    print(*d[i])