# Задание 1
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
summ = 0
for i in range(len(s)):
    if i % 2 == 0:  #проверка на четность номера элемента
       summ += s[i]  #сумма нечетных элементов
print(s, summ)

# Задание 2
s = [1, 5, 8, 11, 10, 13, 16, 18, 21]
for i in range(len(s)):
    if s[i] < 15:  # Проверка элемента на то, меньше ли он 15
        s[i] = s[i] * 2  # Замена элемента на удвоенный
print(s)