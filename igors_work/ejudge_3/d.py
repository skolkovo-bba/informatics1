a = list(map(int, input().split()))

print(*a)

for i in range(0, len(a) - 1):
        move = i 
        for j in range(i + 1, len(a)): 
            if a[j] < a[move]: 
                move = j
         
        a[i], a[move] = a[move], a[i]
        print(*a)
