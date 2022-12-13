# Програма шукає усі можливі підстроки у великому тексті та повертає їх індекси.
# Наприклад, для тексту 'This is your code' та пошукового запиту 'is', відповідь буде (2, 5).

print('Програма шукає усі можливі підстроки у великому тексті та повертає їх індекси.')
text = input('Введіть строку\n>>')
search = input('Введіть пошуковий запит\n>>')

marker = 0
while marker < len(text):
    if text.find(search, marker) == -1:
        #print("String not found")
        break
    else:
        print(text.find(search, marker), end=' ')
        marker = text.index(search, marker) + 1
