"""ГОЛОСУЙ ЗА ИГОРЯ на выборах в студсовет"""

def f(n):
    if n == 1:
        return 0.7 * 10000
    
    return 0.7 * (10000 + 2 * f(n - 1))
    


def m(n):
    if n == 1:
        return 0.3 * 10000 + 1000
    
    return 0.3 * (10000 + 2 * f(n - 1)) + 1000


print(int(m(int(input())) / 100))