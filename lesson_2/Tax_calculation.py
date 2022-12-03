print('Розрахунок податку на прибуток підприємця')

income = float(input('Введіть розмір надходження:'))
tax = float(input('Введіть % податку:'))

print(f'Вам потрібно сплатити: {round(income * tax / 100, 2)} податку.')
print(f'Ваш чистий прибуток складе: {round(income - (income * tax / 100), 2)}')
