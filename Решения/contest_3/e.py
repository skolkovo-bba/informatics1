a = list(map(int, input().split()))

d = {i: 0 for i in range(0, 10)}

for i in a:
    d[i] += 1
    print(*[d[i] for i in range(0, 10)])

a = []
for i in range(0, 10):
    a += [i] * d[i]

print(*a)