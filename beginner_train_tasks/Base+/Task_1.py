# Програма приймає два числа та змінює їх місцями (a стає b, b стає a).
# Бонус: зробити це, не використовуючи третьої змінної
print('Програма приймає два числа та змінює їх місцями')
a = int(input('a: '))
b = int(input('b: '))
a, b = b, a
print(f'a = {a}, b = {b}')
