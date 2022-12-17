# Програма шукає усі можливі підстроки у великому тексті та повертає їх індекси.
# Наприклад, для тексту 'This is your code' та пошукового запиту 'is', відповідь буде (2, 5).

print('Програма шукає усі можливі підстроки у великому тексті та повертає їх індекси.')
text = input('Введіть строку\n>>').lower()
search = input('Введіть пошуковий запит\n>>').lower()

if search not in text:
    print("Строка відсутня")
else:
    marker = 0
    while marker < len(text):
        if text.find(search, marker) == -1:
            break
        else:
            print(text.find(search, marker), end=' ')
            marker = text.index(search, marker) + 1
