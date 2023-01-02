from notebook_functions import*

if __name__ == '__main__':
    print('Програма, для введення та перегляду нотаток.')
    print('--------------------------------------------')

    tuple_keys = show_user_interface()  # Перевели ключі словника в кортеж
    get_user_choice(tuple_keys)  # Передали кортеж в функцію у вигляді аргументів для порівняння
