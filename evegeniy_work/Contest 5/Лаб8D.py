N,W=map(int,(input(),input()))
F = [ [0] * (W + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    w,p=map(int,(input(),input()))
    for k in range(1, W + 1):
        if k >= w:
            F[i][k] = max(F[i - 1][k], F[i - 1][k - w] + p) 
        else: 
            F[i][k] = F[i - 1][k]
print(max(map(max,F)))
