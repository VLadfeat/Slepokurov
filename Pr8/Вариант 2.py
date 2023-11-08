# Задание 1
N = 3
A = [
[2, 7, 6],
[9, 5, 1],
[4, 3, 8]]
s = 0
for i in range(N):
    s += A[0][i]
b = 'является'
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = 'не является'
        break
print(b)
# Задание 2
N = 3
M = 4
A = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]
for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp
for i in range(N):
    for j in range(M):
        print(A[i][j], end = ' ')
    print()