n = int(input())

ans = []

n_sum = n
while n_sum >= 10:
    n_sum = sum(map(int, str(n_sum)))

if n_sum in (0, 3, 6, 9):
    ans.append("Fizz")

if int(str(n)[-1]) in (0, 5):
    ans.append("Buzz")

n_7 = n
while n_7 >= 100:
    n_7 = int(str(n_7)[:-1]) * 3 + int(str(n_7)[-1])

if n_7 in (7 * i for i in range(0, 100)):
    ans.append("Pozz")

print("".join(ans if ans else ["Nedelizz"]))