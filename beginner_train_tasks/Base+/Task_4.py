# Програма приймає 3 числа (день, місяць та рік) і повідомляє чи існує така дата в Григоріанському календарі.
# Не забувайте про високосні роки!
day = int(input('Введіть дату: '))
month = int(input('Введіть місяць: '))
year = int(input('Введіть рік: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Якщо високосний рік
    # якщо в місяці  31 день
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    # якщо в місяці  30 днів
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    # якщо в місяці  29 днів
    elif month == 2:
        if 1 <= day <= 29:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    else:
        print('Такого місяця не існує!!!')
# Якщо звичайний рік
else:
    # якщо в місяці  31 день
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    # якщо в місяці  30 днів
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    # якщо в місяці  28 днів
    elif month == 2:
        if 1 <= day <= 28:
            print('Така дата існує')
        else:
            print('Невірна дата!!!')
    else:
        print('Такого місяця не існує!!!')
