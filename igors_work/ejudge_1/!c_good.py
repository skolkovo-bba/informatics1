n = int(input())

ans = []

if n % 3 == 0:
    ans.append("Fizz")

if n % 5 == 0:
    ans.append("Buzz")

if n % 7 == 0:
    ans.append("Pozz")

print("".join(ans))