d = input()

now = []

try:
    for i in range(0, len(d)):
        if d[i] in {"{", "[", "("}:
            now.append(d[i])
        elif d[i] == "}" and now[-1] == "{":
            now.pop(-1)
        elif d[i] == ")" and now[-1] == "(":
            now.pop(-1)
        elif d[i] == "]" and now[-1] == "[":
            now.pop(-1)
        else:
            raise KeyError
    
    if now:
        print("NO")
    else:
        print("YES")
except:
    print("NO")