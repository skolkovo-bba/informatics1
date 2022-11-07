n = int(input())

m = list(map(int, input().split()))

k = int(input())

d = []
for i in range(k):
    d.append(list(map(int, input().split())))

ans = []
for a, b in d:
    ans.append(max(m[a:b + 1]))

print(*ans)