spisok = [0, 1]
n, k = int(input('Введите число:')), int(input('Введите число:'))-1
for i in range(1, n + 1):
    spisok.append(spisok[-2] + spisok[-1])
    print(sum(spisok[k: len(spisok)]))