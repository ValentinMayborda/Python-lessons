print('Програма рахує витрати на паливо')

expenditure = float(input('Введіть витрачання палива автомобілем на 100км:'))
fuel_price = float(input('Введіть вартість палива за 1 літр:'))
distance = float(input('Введіть скільки кілометрів треба проїхати:'))

print(f'Ви витратите на {distance} км: {round(expenditure / 100 * fuel_price * distance, 2)} UA')
