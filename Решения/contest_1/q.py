n, what = map(int, input().split())

d = []
for i in range(n):
    k = input().split()
    d.append([k[0], int(k[1])])

m = int(input())

now = 0
for _ in range(m):
    if d[now][1] == 1:
        if what == 1:
            now += 1
        else:
            del d[now]
    
    elif d[now][1] == 0:
        if what == 0:
            what = 1
        else:
            what = 0
        
        if what == 1:
            d[now][1] = 1
            now += 1
        else:
            now += 1

    if len(d) == 1:
        break
    
    now %= len(d)

for i in d:
    print(*i)
