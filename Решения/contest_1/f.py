n = int(input())

p = list(map(int, input().split()))

ans = n
for i in range(n, -1, -1):
    p_test = p + p[0:i][::-1]

    if p_test == p_test[::-1]:
        ans = i

print(ans)
print(*p[0:ans][::-1])