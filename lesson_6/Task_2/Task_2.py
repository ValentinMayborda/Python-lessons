from compute import *

if __name__ == '__main__':
    print('Програма перевіряє чи існує трикутник по введеним сторонам.')

    a, b, c = user_input()
    if is_triangle(a, b, c):
        perimeter = calcul_perimeter(a, b, c)
        square = calcul_square(perimeter, a, b, c)
        print(f"Периметр трикутника зі сторонами {a}, {b}, {c} складає: {perimeter}")
        print(f"Площа трикутника зі сторонами {a}, {b}, {c} складає: {square}")
    else:
        print(f'Трикутник зі сторонами {a}, {b}, {c} існувати не може!!!)')
