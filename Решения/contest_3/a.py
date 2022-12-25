a = list(map(int, input().split()))

while True:
    for i in range(0, len(a) - 1):
        if a[i + 1] < a[i]:
            a[i + 1], a[i] = a[i], a[i + 1]
            print(*a)
            break
    else:
        exit(0)
