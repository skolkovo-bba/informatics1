from collections import Counter

n = int(input())

m = []
for i in range(0, n):
    m.append(int(input()))

c = Counter(m)

print(c.most_common()[0][0])