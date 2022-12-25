a = list(map(int, input().split()))


for i in range(0, len(a) - 1):
        move = i
        if a[i] == 0:
            continue
        for j in range(i + 1, len(a)): 
            if a[j] == 0:
                continue
            
            if a[j] < a[move]: 
                move = j
         
        a[i], a[move] = a[move], a[i]
print(*a)
