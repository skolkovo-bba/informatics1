start = int(input())
m = list(map(int, input().split()))

n = [-1] * len(m)
n[0] = start

for i in range(2, len(m)):
    if i - 2 >= 0:
        if i - 3 >= 0:
            n[i] = max(n[i - 2], n[i - 3])
        else:
            n[i] = n[i - 2]
    
    n[i] *= (100 + m[i]) / 100
    n[i] = int(n[i])

#print(n)
now = n.index(max(n))
#print(now)
way = [now]
while now != 0:
    if now - 2 >= 0:
        if now - 3 >= 0:
            if n[now - 2] > n[now - 3]:
                now -= 2
            else:
                now -= 3
        else:
            now -= 2
    #print(now)
    way.append(now)


print(*map(lambda x: x + 1, way[::-1]))