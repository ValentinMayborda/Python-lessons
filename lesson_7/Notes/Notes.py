def show_user_interface():
    print('Користувацький інтерфейс нотатника. Введіть команду з переліку: ')
    user_interface_dict = {
        'add': '- додати нотатку',
        'earliest': '- виводить збережені нотатки у хронологічному порядку',
        'latest': '- виводить збережені нотатки у хронологічному порядку',
        'longest': '- виводить збережені нотатки у порядку їх довжини',
        'shortest': '- виводить збережені нотатки у порядку їх довжини',
        'clear': '- очистити нотатник',
        'exit': '- вийти з нотатника'
    }

    for key, value in user_interface_dict.items():
        print(f'{key:10} {value}')


def get_user_choice():
    my_list = list()

    while True:
        choice = input('> ')

        if choice == 'add':
            tmp = input('> Введіть нотатку: ')
            my_list.append(tmp)
        elif choice == 'earliest':
            # виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
            print('> Від найранішої до найпізнішої:')
            for elem in my_list:
                print(f'> {elem}')
        elif choice == 'latest':
            # виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
            print('> Від найпізнішої до найранішої:')
            list_reverse = my_list[::-1]
            for elem in list_reverse:
                print(f'> {elem}')

        elif choice == 'longest':
            # виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
            print('> Від найдовшої до найкоротшоЇ:')
            pass
        elif choice == 'shortest':
            # виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
            print('> Від найкоротшої до найдовшої:')
            pass
        elif choice == 'clear':
            my_list.clear()
            print('Нотатки видалено!')
        elif choice == 'exit':
            print('До зустрічі!')
            exit(0)
        else:
            print('Введена невірна команда!')

        print(my_list)




if __name__ == '__main__':
    print('Програма, для введення та перегляду нотаток.')
    print('--------------------------------------------')

    show_user_interface()
    get_user_choice()
