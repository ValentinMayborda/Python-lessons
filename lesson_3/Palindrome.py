print('Програма перевіряє чи є введена строка паліндромом :')

# Вводимо строку, перевівши її в нижній регістр, позбавляючись пробілів
# та знаків табуляції і розділових знаків .,-:;?!"'
input_str = input('Введіть Вашу строку:').lower().replace(' ', '').replace('\t', '')\
    .replace('.', '').replace(',', '').replace('-', '').replace(':', '').replace(';', '')\
    .replace('?', '').replace('!', '').replace('"', '').replace("'", '')
palindrome_str = input_str[::-1]  # Створює зворотню копію вхідної строки

if input_str == palindrome_str:
    print(f'Cтрока є паліндромом!')
else:
    print(f'Cтрока не являється паліндромом!')