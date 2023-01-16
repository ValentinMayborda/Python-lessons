def open_file() -> list:
    """
    Функція відкриває файл passwords.txt з таким вмістом:
    1232132133213
    asdasdasdasdasd
    qweqweqweqweqwe
    sdasdasdasdasd
    dsdsddsdsdsddds
    ...
    якщо той існує.
    Якщо його не має, то повідомляє користувача
    :return: повертає список елементів
    """
    while True:
        try:
            # Відкриваємо наш файл та зчитуємо його в список lst
            with open('passwords.txt', mode='r', encoding='utf-8') as tf:
                lst = tf.readlines()
                print('> Файл passwords.txt прочитано!')
            return lst
        except Exception:
            # Якщо файл відсутній повідомляємо що треба файл!
            print('> Файл відсутній! Додайте файл "passwords.txt" в один каталог з програмою!!! <')
            exit(0)


def enter_len() -> int:
    """
    Функція відповідає за коректний ввод значення від користувача
    :return: повертає довжину слова по якій фільтруються слова
    """
    while True:
        try:
            n = int(input('> Слова якої довжини відібрати : '))
        except Exception:
            print('> Введіть числове значення!')
            continue
        return n


def write_file(lst: list, len_of_word: int):
    """
    Функція виконує фільтрацію слів по довжині та записує їх до нового файлу
    :param lst: Список слів з вхідного файлу
    :param len_of_word: довжина по якій фільтруються слова
    """
    my_list = [elem.strip() for elem in lst if len(elem.strip()) == len_of_word]

    with open('passwords_filtered.txt', mode='w', encoding='utf-8') as tfw:
        for elem in my_list:
            tfw.write(elem)
            tfw.write('\n')
        print(f'> Паролі відфільтровано та збережено у файлі - > passwords_filtered.txt!')
        exit(0)


if __name__ == '__main__':
    print("*** Password filter ***\n")
    lst_ = open_file()
    len_word = enter_len()
    write_file(lst_, len_word)
