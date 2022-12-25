

def f(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return f(m - 1, 1)
    elif m > 0 and n > 0:
        return f(m - 1, f(m, n - 1))

print(f(int(input()), int(input())))