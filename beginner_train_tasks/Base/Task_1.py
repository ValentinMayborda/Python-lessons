# Програма приймає два числа та повідомляє яке з них більше та на скільки (7 більше 5 на 2)
print('Програма приймає два числа та повідомляє, яке з них більше та на скільки.')

a, b = int(input('Введіть перше число: ')), int(input('Введіть друге число: '))
if a > b:
    print(f'{a} більше {b} на {a - b}')
elif b > a:
    print(f'{b} більше {a} на {b - a}')
else:
    print('Числа рівні!')
