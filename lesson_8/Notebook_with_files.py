from notebook_functions import*

if __name__ == '__main__':
    # Словник з користувацьким інтерфейсом
    user_interface_dict = {
        'add': '- додати нотатку',
        'earliest': '- виводить збережені нотатки у хронологічному порядку від найранішої до найпізнішої',
        'latest': '- виводить збережені нотатки у хронологічному порядку від найпізнішої до найранішої',
        'longest': '- виводить збережені нотатки у порядку їх довжини від найдовшої до найкоротшої',
        'shortest': '- виводить збережені нотатки у порядку їх довжини від найкоротшої до найдовшої',
        'clear': '- очистити нотатник',
        'exit': '- зберегти та вийти з нотатника'
    }

    # Вивід привітання, пояснення
    print('Програма, для введення та перегляду нотаток.')
    print('--------------------------------------------')

    # Викликаэмо функцію відкриття файлу та отримуємо список нотатків
    text_file_lst = open_file()

    # Змінна для ключів словника
    tuple_keys = show_user_interface(user_interface_dict)

    # Передаємо кортеж в функцію у вигляді аргументів для порівняння та список з нотатками
    get_user_choice(tuple_keys, text_file_lst)
