summa, how = map(int, input().split())

if summa > 9 * how or summa < 1 * how:
    print("impossible")
else:
    ans = [0] * how
    for i in range(0, how):
        ans[i] = min(9, summa - (how - i - 1))
        summa -= ans[i]
    
    print(*ans[::-1], sep="")