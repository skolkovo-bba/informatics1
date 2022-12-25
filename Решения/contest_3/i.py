x, y, n = map(int, input().split())

def check(h):
    global x, y, n

    f = lambda n, x: n // x if x > 0 else 0
    return f(h, x) * f(h, y) >= n

    



l = 0
r = 1_000_000_000_000 ** 10

while r - l > 1:
    m = (l + r) // 2

    if check(m):
        r = m
    else:
        l = m



if l >= 0 and check(l):
    print(l)
else:
    print(l + 1)