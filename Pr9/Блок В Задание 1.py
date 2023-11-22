# задание 1
def f():
    n = int(input('Введите число: '))
    if n == 0:
        return 0
    max_znach = f()
    if n > max_znach:
        return n
    else:
        return max_znach
print(f())