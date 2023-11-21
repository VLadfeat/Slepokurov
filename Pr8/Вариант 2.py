# Задание 1
A = [[1, 5, 9], [4, 8, 6], [3, 7, 2]]
N = 3
s = 0
for j in range(N):
    s += A[0][j]
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[i][j]
if s1 != s or s2 != s:
    print('Не является')
else:
    print('Является')

# Задание 2
n = 3
m = 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(n):
    A1 = A[i][0]
    A[i][0] = A[i][m-1]
    A[i][m-1] = A1
for i in range(n):
    for j in range(m):
        print(A[i][j], end = ' ')
    print()