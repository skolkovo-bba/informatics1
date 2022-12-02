"""ГОЛОСУЙ ЗА ИГОРЯ на выборах в студсовет"""

def make_exchange(money, coins):
    n = money 
    m = coins
    if not m:
        if n == 0:
            return 1
        else:
            return 0
    if n == 0:
        return 1
    
    m.sort()
    dp = [0] * (n + 1)
    dp[0] = 1
    for add in range(0, len(m)):
        dp_new = dp.copy()
        for i in range(0, n + 1):
            if dp[i]:
                how = 1
                while how * m[add] + i <= n:
                    dp_new[how * m[add] + i] += dp[i]
                    how += 1
        
        dp = dp_new


    return dp[n]


print(make_exchange(10, [5,2,3]))