def f(n):
    if n == 0: return 1
    return f(n - 1) * 2


n = int(input())
print(f(n))