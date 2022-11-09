N = int(input())
a = [True] * (N + 1)
a[0] = False
a[1] = False
n = 2
while n*n <= N:
    if a[n]:
        i = n*n
        while i <= N:
            a[i] = False
            i += n
    n += 1

d = []
for i in range(2, N+1):
    if a[i]:
        d.append(i)
if d:
    print(*d)
else:
    print(0)