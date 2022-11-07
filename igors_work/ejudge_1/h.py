m = [int(input())]

while m[-1] != 0:
    m.append(int(input()))


even = list(filter(lambda x: x % 2 == 0, m))

if even:
    print(max(even))
else:
    print(0)