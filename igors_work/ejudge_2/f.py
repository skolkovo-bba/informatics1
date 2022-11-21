def create(now):
    if 0 == now:
        ans = {1, 4, 7, }
    elif 1 == now:
        ans = {0, 6, }
    elif 2 == now:
        ans = {5, }
    elif 3 == now:
        ans = {4, }
    elif 4 == now:
        ans = {0, 3}
    elif 5 == now:
        ans = {2, }
    elif 6 == now:
        ans = {1}
    elif 7 == now:
        ans = {0}
    return ans

n = int(input())

m = [[0] * 8 for _ in range(n + 1)]
m[0][0] = 1

for i in range(1, n + 1):
    for fr in range(8):
        if m[i - 1][fr] > 0:
            for to in create(fr):
                m[i][to] += m[i - 1][fr]

print(m[n][0])