from calculate_cost import calculate

if __name__ == '__main__':
    print('Програма рахує витрати на паливо.')

    # Запит на ввод даних від користувача
    expenditure = float(input('Введіть витрачання палива автомобілем на 100км: '))
    fuel_price = float(input('Введіть вартість палива за 1 літр: '))
    distance = float(input('Введіть скільки кілометрів треба проїхати: '))

    # Виклик функції calculate(розрахунку) та зберігаєм значення в змінну cost
    cost = (calculate(expenditure, fuel_price, distance))
    print(f'Ви витратите на {distance} км: {cost} UA')
