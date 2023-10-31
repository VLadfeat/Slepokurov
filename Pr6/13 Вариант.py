# Задание 1
spisok1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
if len(set(spisok1)) != len(spisok1):
    print('Одинаковые элементы есть')
else:
    print('Одинаковых элементов нет')


# Задание 2
spisok2 = [10, 1, 11, 12, 30, 14, 20, 15]
for i in range(len(spisok2)):
    if spisok2[i] < 15:
        spisok2[i] *= 2
print(spisok2)