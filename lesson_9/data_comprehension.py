print("""Написати програму що читає текстовий файл та, використовуючи тільки list
comprehension і ніякі інше цикли, розділяє текст на лінії (строки) методом readlines()
та створює список таких строк. В кожній строці мають бути застосовані такі перетворення в такому порядку:""")

if __name__ == '__main__':

    with open('file.txt', mode='r', encoding='utf-8') as f:
        lst = f.readlines()

    my_list = [elem.strip()[elem.find('a'):].capitalize() for elem in lst if 'a' in elem]

    print(my_list)
