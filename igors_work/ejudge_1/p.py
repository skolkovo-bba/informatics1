d = list(input().split())
k = input()

def g(fr, to, k):
    global d

    if to - fr == 1:
        if d[fr] == k:
            return fr
        else:
            return -1
    elif to - fr == 2:
        if d[fr] == k:
            return fr
        elif d[fr + 1] == k:
            return fr + 1
        else:
            return -1
    else:
        res1 = g(fr, fr + (to - fr) // 2, k)
        if res1 != -1:
            return res1
        res2 = g(fr + (to - fr) // 2, to, k)
        return res2

res = g(0, len(d), k)

if res == -1:
    print(-1)
else:
    print(res + 1)