# Задание 4
n = int(input('Введите число: '))
def f(n):
    if n < 10:
        return n
    else:
        return f(n // 10) + n % 10
print(f(n))