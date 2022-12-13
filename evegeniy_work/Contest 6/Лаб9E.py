s=input()
r=''
i=0
for v in s:
    if not v.isalpha():
        r+=v
        continue
    if i%2:
        r+=v.lower()
    else:
        r+=v.upper()
    i+=1
print(r)
