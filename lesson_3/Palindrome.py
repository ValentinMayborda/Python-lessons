print('Програма перевіряє чи є введена строка паліндромом :')

# Вводимо строку, перевівши її в нижній регістр, позбавляючись пробілів та знаків табуляції
input_str = input('Введіть Вашу строку:').lower().replace(' ', '').replace('\t', '')
palindrome_str = input_str[::-1]  # Створює зворотню копію вхідної строки

#print(input_str)
if input_str == palindrome_str:
    print(f'Cтрока є паліндромом!')
else:
    print(f'Cтрока не являється паліндромом!')
