n = int(input())
w = int(input())

m = []
p = []
for _ in range(n):
    m.append(int(input()))
    p.append(int(input()))


dp = [-99999999] * (w + 1)
dp[0] = 0
for weight, pay in zip(m, p):
    copy = dp.copy()
    for k in range(weight, w + 1):
        copy[k] = max(dp[k], dp[k - weight] + pay)
    dp = copy


print(max(dp))