# Дано натуральные числа Х,N Вычислить выражение вида: x^n / n!.
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

x = 4
n = 7
result = power(x, n) / factorial(n)
print(f"{x}^{n} / {n}! = {result}")
