n = int(input())

m = list(map(int, input().split()))

houses = []
markets = []
for i in range(0, len(m)):
    if m[i] == 1:
        houses.append(i)
    elif m[i] == 2:
        markets.append(i)

houses.sort()
markets.sort()



ans = 0
for home in houses:


    l = 0
    r = len(markets)

    while r - l > 1:
        mid = (l + r) // 2
        if markets[mid] > home:
            r = mid
        else:
            l = mid


    if 0 <= r < len(markets) and 0 <= l < len(markets):
        if min(abs(markets[r] - home), abs(markets[l] - home)) > ans:
            ans = min(abs(markets[r] - home), abs(markets[l] - home))
    elif 0 <= l < len(markets) and abs(markets[l] - home) > ans:
        ans = abs(markets[l] - home)
    elif 0 <= r < len(markets) and abs(markets[r] - home) > ans:
        ans = abs(markets[r] - home)

print(ans)