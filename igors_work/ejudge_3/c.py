a = list(map(int, input().split()))

print(*a)


for i in range(1, len(a)):
    j = i
    while j > 0 and a[j] < a[j - 1]:
        a[j - 1], a[j] = a[j], a[j - 1]
        print(*a)
        j -= 1