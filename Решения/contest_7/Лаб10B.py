a=[]
for s in input().split():
    i=int(s)
    if i>0:
        a.append(i)
    if i<0 and a:
        if -i<a[-1]:
            a[-1]+=i
        else:
            a.pop()
print(len(a),a[-1] if a else -1)
