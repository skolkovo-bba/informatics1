n = int(input())

m = []

for i in range(n):
    m.append(input())

s = ''.join(m)
for i in range(10000, -1, -1):
    if s.find("1" * i) != -1:
        print(i)
        break