def z_function (s: str):
    n = len(s)
    z = [0] * n
    i = 1
    l = 0
    r = 0
    while i < n:
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        i += 1
    return z


s = input()

c = s + "#" +s[::-1]

print(*z_function(c)[::-1][:len(s)])