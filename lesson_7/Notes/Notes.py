def show_user_interface():
    print('Користувацький інтерфейс нотатника. Введіть команду з переліку: ')
    user_interface_dict = {
        'add': '- додати нотатку',
        'earliest': '- виводить збережені нотатки у хронологічному порядку від найранішої до найпізнішої',
        'latest': '- виводить збережені нотатки у хронологічному порядку від найпізнішої до найранішої',
        'longest': '- виводить збережені нотатки у порядку їх довжини від найдовшої до найкоротшої',
        'shortest': '- виводить збережені нотатки у порядку їх довжини від найкоротшої до найдовшої',
        'clear': '- очистити нотатник',
        'exit': '- вийти з нотатника'
    }

    for key, value in user_interface_dict.items():
        print(f'{key:10} {value}')

    return tuple(user_interface_dict.keys())


def get_user_choice(keys):
    my_list = list()

    while True:
        choice = input('> ')

        if choice == keys[0]:  # add
            new_entry = input('> Введіть нотатку: ')
            my_list.append(new_entry)

        elif choice == keys[1]:  # earliest
            # виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
            if len(my_list) == 0:
                print('> Нотатки пусті!')
            else:
                print('> Від найранішої до найпізнішої:')
                for elem in my_list:
                    print(f'> {elem}')
        elif choice == keys[2]:  # latest
            # виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
            if len(my_list) == 0:
                print('> Нотатки пусті!')
            else:
                print('> Від найпізнішої до найранішої:')
                list_reverse = my_list[::-1]
                for elem in list_reverse:
                    print(f'> {elem}')

        elif choice == keys[3]:  # longest
            # виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
            if len(my_list) == 0:
                print('> Нотатки пусті!')
            else:
                print('> Від найдовшої до найкоротшоЇ:')
                longest_my_list = sorted(my_list, key=len, reverse=True)
                for elem in longest_my_list:
                    print(f'> {elem}')

        elif choice == keys[4]:  # shortest
            # виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
            if len(my_list) == 0:
                print('> Нотатки пусті!')
            else:
                print('> Від найкоротшої до найдовшої:')
                shortest_my_list = sorted(my_list, key=len)
                for elem in shortest_my_list:
                    print(f'> {elem}')

        elif choice == keys[5]:  # clear
            my_list.clear()
            print('> Нотатки видалено!')
        elif choice == keys[6]:  # exit
            print('> До зустрічі!')
            exit(0)
        else:
            print('***Введена невідома команда!***')

        print(my_list)




if __name__ == '__main__':
    print('Програма, для введення та перегляду нотаток.')
    print('--------------------------------------------')

    tuple_keys = show_user_interface()  # Перевели ключі словника в кортеж
    # print(list_keys)
    get_user_choice(tuple_keys)  # Передали кортеж в функцію у вигляді аргументів для порівняння
