n = int(input())
w = int(input())

m = []
p = []
for _ in range(n):
    m.append(int(input()))
    p.append(int(input()))


dp = [0] * (w + 1)
for i in range(0, n):
    for k in range(1, w + 1):
        if k >= m[i]:
            dp[k] = max(dp[k], dp[k - m[i]] + p[i])


print(max(dp))