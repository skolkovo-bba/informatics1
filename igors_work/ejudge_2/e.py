n = int(input())

m = [[] for _ in range(n)]

a = input()
while a != "#":
    stud, how = map(int, a.split())
    m[stud].append(how)
    a = input()

m = list(filter(lambda x: len(x) > 0, m))
m = [sorted(i, reverse=True) for i in m]
m.sort(key=sum, reverse=True)

for i in m:
    print(*i, end=" ")