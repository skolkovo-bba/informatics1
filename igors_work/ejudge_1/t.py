s = input()

ans = 0
now = 0

for symb in s.split(".")[::-1]:
    conv = symb.count("<") * 10 + symb.count("v")

    ans += conv * (60 ** now)

    now += 1

print(ans)