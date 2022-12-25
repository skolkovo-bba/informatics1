a = list(map(int, input().split()))

print(*a)

while True:
    ready = True
    for i in range(0, len(a) - 1):
        if a[i + 1] < a[i]:
            a[i + 1], a[i] = a[i], a[i + 1]
            print(*a)
            ready = False
    if ready:
        break