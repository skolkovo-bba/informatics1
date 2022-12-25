m = [[0] * 3 for i in range(10000)]
a = input()
while a[-1] != "3":
    age, res = map(int, a.split())
    if age >= 10000:
        exit(-1)
    m[age][res] += 1
    a = input()

for i in range(0, 10000):
    if m[i][0] + m[i][2] > 0:
        print(i, int(m[i][2] * 100 / (m[i][0] + m[i][2]) + 0.5))