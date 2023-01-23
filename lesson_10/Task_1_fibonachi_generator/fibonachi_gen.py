def fibonachi_gen(_n: int):
    """
    Функція генератор послідовності чисел Фібаначі
    :param _n: кількість елементів послідовності Фібаначі які треба згенерувати
    :return: генерує значення послідовності Фібаначі
    """
    a = 0
    b = 1
    c = 1
    for i in range(_n):
        yield a
        a = b
        b = c
        c = a + b


if __name__ == '__main__':

    while True:
        try:
            n = int(input('Скільки елементів послідовності Фібоначі вивести?: '))
        except Exception:
            print('Введіть цифрове значення!')
            continue

        for elem in fibonachi_gen(n):
            print(elem)

        exit(0)
