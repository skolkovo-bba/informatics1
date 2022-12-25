def f(st, m, a):
    global b
    if len(st)==m:
        if pr(int(st)):
            b.append(st)
    else:
        for digit in a:
            if digit not in st:
                f(st + digit, m, a)


def pr(x):
    pr.pr_m
    if x == 1:
        return False
    i = 0
    while pr.pr_m[i] * pr.pr_m[i] <= x:
        if x % pr.pr_m[i] == 0:
            return False
        i += 1
    return True


def main():
    n, m = map(int, input().split())
    
    N = int(987654321 ** 0.5) + 2
    resh = [True] * (N + 1)
    resh[0] = False
    resh[1] = False
    v = 2
    while v * v <= N:
        if resh[v]:
            i = v * v
            while i <= N:
                resh[i] = False
                i += v
        v += 1
    pr_m=[]
    for i in range (len(resh)):
        if resh[i]:
            pr_m.append(i)
    pr.pr_m = pr_m

    if m > n:
        m = n
    
    a = ''
    st = ''
    global b
    b = []
    for k in range (1, n + 1):
        a += str(k)
    f(st, m, a)
    print(len(b))

if __name__ == "__main__":
    main()