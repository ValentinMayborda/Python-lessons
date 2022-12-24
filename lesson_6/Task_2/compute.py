def user_input() -> tuple[int, int, int]:
    """
    Функція вводу коректних значень користувачем
    :return: повертає сторони трикутника a, b, c в основну программу кортежем з int елементами
    """
    while True:
        try:
            a, b, c = int(input('Введіть сторону а: ')), int(input('Введіть сторону b: ')),\
                      int(input('Введіть сторону c: '))
            if a > 0 and b > 0 and c > 0:
                return a, b, c
            else:
                print('Введіть значення більше нуля!')
        except Exception:
            print('Ви ввели неадекватні значення!')


def is_triangle(a, b, c) -> bool:
    """
    Функція перевіряє чи може існувати трикутник з вказаними сторонами
    :param a: сторона трикутника а
    :param b: сторона трикутника b
    :param c: сторона трикутника c
    :return:  повертає булеве значення
    """
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


def calcul_perimeter(a, b, c) -> float:
    """
    Функція підраховує периметр трикутника по вхідним параметрам
    :param a: сторона трикутника а
    :param b: сторона трикутника b
    :param c: сторона трикутника c
    :return: повертає периметр трикутника в флоте
    """
    perimetr = (a + b + c) / 2
    return perimetr


def calcul_square(perimeter, a, b, c) -> float:
    """
    Функція підраховує площу трикутника по вхідним параметрам
    :param perimeter: периметр трикутника a, b, c
    :param a: сторона трикутника а
    :param b: сторона трикутника b
    :param c: сторона трикутника c
    :return: повертає значення площі трикутника, округлене до 2 цифр після коми в значенні флоат
    """
    square = pow(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c), 1 / 2)
    return round(square, 2)
