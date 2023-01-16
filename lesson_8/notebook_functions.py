def open_file() -> list:
    """
    Функція відкриває файл "text_file.txt" з нотатками, якщо той існує.
    Якщо його не має, то створює файл "text_file.txt"
    :return: повертає список нотатків
    """
    try:
        # Відкриваємо наш файл та зчитуємо його в список text_file_lst
        with open('text_file.txt', mode='r', encoding='utf-8') as tf:

            lst = tf.readlines()

    except Exception:
        # Якщо файл відсутній то створюємо пустий список та повертаємо його
        lst = list()

    return lst


def show_user_interface(dictionary: dict) -> tuple:
    """
    Функція виводить на екран користувацький інтерфейс
    :param dictionary: вхідним параметром є словник
    :return: кортеж ключів
    """
    print('Користувацький інтерфейс нотатника. Введіть команду з переліку: ')
    for key, value in dictionary.items():
        print(f'{key:10} {value}')

    return tuple(dictionary.keys())


def my_list_is_not_empty(mylist: list):
    """
    Функція перевіряє чи пустий список
    :param mylist: вхідним параментром є основний список де мають зберігатись записи
    :return: якщо список не пестий повертає True в іншому випадку повідомлення
    """
    if len(mylist) > 0:
        return True
    else:
        print('> Нотатки пусті!')


def how_many_notes() -> int:
    """
    Функція для команд earliest, latest, longest або shortest, яка запитує у користувача скільки
    записів виводити на екран, реагує на некоректний ввод.
    :return: повертає кількість записів
    """
    while True:
        try:
            how_notes = int(input('> Скільки нотаток Ви бажаєте побачити на екрані: '))
            if how_notes < 1:
                raise ValueError
            return how_notes
        except Exception:
            print('> Не коретне значення!')
            continue


def get_user_choice(keys: tuple, textfile: list):
    """
    Основна функція, яка веде діалог з користувачем, запитуючи в нього команди та реагує на них відповідно.
    :param textfile: список елементів(нотаток) з файлу text_file.txt
    :param keys:  кортеж ключів словника user_interface_dict
    :return: None (виводить на екран інформацію відповідно до діалогу з користувачем)
    """
    # Основний список, куди зберігаються записи нотатника
    # формування спиcку з відкиданням '\n'
    my_list = [elem.strip() for elem in textfile]

    while True:
        choice = input('> ')  # Змінна для вводу команд користувача

        if choice == keys[0]:  # add
            new_entry = input('> Введіть нотатку: ')
            my_list.append(new_entry)

        elif choice == keys[1]:  # earliest
            # виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
            if my_list_is_not_empty(my_list):
                how_notes = how_many_notes()

                print('> Від найранішої до найпізнішої:')
                for elem in my_list[:how_notes]:
                    print(f'> {elem}')

        elif choice == keys[2]:  # latest
            # виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
            if my_list_is_not_empty(my_list):
                how_notes = how_many_notes()

                print('> Від найпізнішої до найранішої:')
                list_reverse = my_list[::-1]
                for elem in list_reverse[:how_notes]:
                    print(f'> {elem}')

        elif choice == keys[3]:  # longest
            # виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
            if my_list_is_not_empty(my_list):
                how_notes = how_many_notes()

                print('> Від найдовшої до найкоротшоЇ:')
                longest_my_list = sorted(my_list, key=len, reverse=True)
                for elem in longest_my_list[:how_notes]:
                    print(f'> {elem}')

        elif choice == keys[4]:  # shortest
            # виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
            if my_list_is_not_empty(my_list):
                how_notes = how_many_notes()

                print('> Від найкоротшої до найдовшої:')
                shortest_my_list = sorted(my_list, key=len)
                for elem in shortest_my_list[:how_notes]:
                    print(f'> {elem}')

        elif choice == keys[5]:  # clear
            # чистить нотатник
            my_list.clear()
            print('> Нотатки видалено!')

        elif choice == keys[6]:  # save & exit
            # Відкриваємо наш файл та записуємо в нього наші нотатки.
            # Цикл добавляє елементи списку до файлу text_file.txt та добавляє перехід на новий рядок.
            with open('text_file.txt', mode='w', encoding='utf-8') as tfw:
                for elem in my_list:
                    tfw.write(elem)
                    tfw.write('\n')
                print('> До зустрічі!')
                exit(0)
        else:
            print('***Введена невідома команда!***')
