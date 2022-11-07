a = set(map(int, input().split()))
c = set(map(int, input().split()))
b = set(map(int, input().split()))

s = a | b | c
ans = []
for i in s:
    if i not in a and i in b and i in c:
        ans.append(i) 

ans.sort()

print(*ans)