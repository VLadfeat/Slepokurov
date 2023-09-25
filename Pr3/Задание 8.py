x = int(input('Введите номер месяца:'))
if x == 2:
        print('В месяце 28 дней')
elif x == 4 or x == 6 or x == 9 or x == 11:
        print('В месяце 30 дней')
else:
        print('В месяце 31 день')