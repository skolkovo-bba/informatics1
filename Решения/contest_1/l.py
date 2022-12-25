x1, y1, x2, y2 = map(float, input().split())
xA, yA = map(float, input().split())

if x1 == x2:
    print(xA + 2 * (x1 - xA), yA)
    exit(0)
elif y1 == y2:
    print(xA, yA + 2 * (y1 - yA))
    exit(0)


k = (y1 - y2) / (x1 - x2)
b = y1 - x1 * k


k_perp = -1 / k
b_perp = yA - k_perp * xA


x = (b - b_perp) / (k_perp - k)
y = x * k_perp + b_perp


print(round(xA + 2 * (x - xA), 5), round(yA + 2 * (y - yA), 5))