# Задание 1
from random import randint
file = open('Слепокуров В.С._УБ-32_vvod.txt')
size = int(next(file))
min = 1
max = 9
k = int(next(file))
A = []
file1 = open('Слепокуров В.С._УБ-32_vivod.txt', 'w', encoding = 'utf-8')
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(randint(min, max)))
    A.append(b)
file1.write('Задание 1\nНачальная матрица:\n')
file1.write(str(A))
def f(A, k):
    dg = A[k-1][k-1]
    for j in range(len(A[k-1])):
        A[k-1][j] /= dg
    return A

i = f(A, k)
file1.write('\nИзменённая матрица:\n')
file1.write(str(A))

# Задание 2
a = int(next(file))
b = str(next(file))
c = []
file1.write('\nЗадание 2\n')
file1.write(b)
m = b.split(';')
m = [i.split() for i in m]
for i in range(a):
    c.append([0] * a)
for i in range(a):
    for j in range(a):
        c[j][i] = m[i][j]
file1.write('\nИзменённая матрица:\n')
file1.write(str(c))
file1.close()