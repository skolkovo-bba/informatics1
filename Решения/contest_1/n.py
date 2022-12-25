n = int(input())
m = int(input())
k = int(input())
x = int(input())

if m < n:
    print("NO")
elif m - k <= x and k < m:
    print("NO")
else:
    print("YES")