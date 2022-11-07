from math import sqrt
n = int(input())

d = list(map(int, input().split()))

def check(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

ans = 0
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            continue

        if d[i] + d[j] > ans and check(d[i] + d[j]):
            ans = d[i] + d[j]


print(ans)