n = int(input())

s = []
for i in range(0, n):
    s.append(input())

ind = []
for i in range(0, n):
    ind.append(int(input()))

ans = []
for i in range(0, n):
    ans.append(s[ind[i]])

print(" ".join(ans))