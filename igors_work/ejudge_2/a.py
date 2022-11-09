x, p, y = map(int, input().split())
x *= 100
y *= 100
now = 0

while x < y:
    x = int(x * (1 + p / 100))
    now += 1

print(now)