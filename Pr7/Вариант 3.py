# Задание 1
import math
def gipotenuza(x, y):
    return math.sqrt(x ** 2 + y ** 2)  # вычисляем гипотенузу

a1, b1 = map(float, input('Катеты 1-го треугольника a1, b1 = ').split())
a2, b2 = map(float, input('Катеты 2-го треугольника a2, b2 = ').split())
c1 = gipotenuza(a1, b1)
c2 = gipotenuza(a2, b2)
if c1 == c2:
    print('Гипотенузы равны')
if c1 > c2:
    print('Гипотенуза 1-го треугольника больше')
else:
    print('Гипотенуза 2-го треугольника больше')

# Задание 2
s = input('').lower().split(' ')
for i in range(len(s)):
    s[i] = ''.join(sorted(s[i]))
print(' '.join(s))