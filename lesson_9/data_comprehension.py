print("""Программа читає текстовий файл та використовуює тільки list comprehension і ніякі інше цикли,
розділяє текст на лінії (строки) методом readlines() та створює список.""")

if __name__ == '__main__':

    with open('file.txt', mode='r', encoding='utf-8') as f:
        lst = f.readlines()

    my_list = [elem.strip()[elem.find('a'):].capitalize() if 'a' in elem else '' for elem in lst]
    print()
    print(f'Вихідний список: {my_list}')
