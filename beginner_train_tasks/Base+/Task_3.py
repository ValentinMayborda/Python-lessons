# Програма має підробіток нумерологом) отримавши строку з числами (дату народження наприклад)
# , видаляє зайві не-цифрові символи та рахує суму усіх знайдених цифр, скорочуючи довге число до цифри:
# 20.11.2002 -> 2 + 0 + 1 + 1 + 2 + 0 + 0 + 2 = 8 18.04.1984 -> 1 + 8 + 0 + 4 + 1 + 9 + 8 + 4 = 35 = 3 + 5 = 8
print('Програма нумеролог от Бога')
date = input('Введіть дату: ')

tmp = 0  # Змінна для зберігання першого додавання
total = 0  # Змінна для розрахунку суми чисел
for c in date:
    if c.isdigit():
        tmp += int(c)

for i in str(tmp):
    total += int(i)

print(f'Сума всіх знайдених цифр = {total}')
