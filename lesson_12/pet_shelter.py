from dog import Dog
import random
from datetime import datetime, timedelta


if __name__ == '__main__':
    last_vet_check = datetime.now()

    # Створюємо собак
    dogs = list()
    dog_food = ['мясо','молоко','вода','сухий корм','кісточка','каша']
    dogs_lst_name = ['Спайк', 'Скуби Ду', 'Саймон', 'Стич', 'Скай', 'Султан', 'Снежок', 'Сириус', 'Снупи', 'Спартак']

    for name in dogs_lst_name:
        last_vet_check -= timedelta(days=30)
        dogs.append(Dog(
            name=name,
            gender=random.choice(['пес', 'собака']),
            age=random.randint(1, 10),
            breed='',
            preferable_meal=set(random.choices(dog_food, k=3)),
            last_vet_check=last_vet_check
        ))
    # Наповнюємо подіями життя собак
    for dog in dogs:
        dog.walk(random.randint(1, 5))
        for food in random.choices(dog_food, k=3):
            dog.eat(food)

    # Перевіряємо як справи у собак
    for dog in dogs:
        print(f'Перевіряєм чи все добре з {dog}')
        # Чи собака їла
        if not dog.fed_check:
            if dog.gender == 'пес':
                print(f'Warning! {dog.name} хоче їсти!')
            elif dog.gender == 'собака':
                print(f'Warning! {dog.name} голодна!')
            else:
                print(f'{dog.name} - невідома осіб {dog.gender}!')
        else:
            print(f'{dog.name} сьогодні їла')

        # Чи собака гуляла
        if not dog.walk_check:
            if dog.gender == 'пес':
                print(f'Warning! {dog.name} сьогодні не гуляв!')
            elif dog.gender == 'собака':
                print(f'Warning! {dog.name} сьогодні не гуляла!!')
            else:
                print(f'{dog.name} - невідома осіб {dog.gender}!')
        else:
            print(f'{dog.name} сьогодні гуляла')

        # Чи собака була у ветеринара хоч раз за останні півроку
        if not dog.vet_check:
            if dog.gender == 'собака':
                print(f'Warning! {dog.name} давно не перевірялась  ветеринаром!')
            elif dog.gender == 'пес':
                print(f'Warning! {dog.name} давно не перевірявся ветеринаром!')
            else:
                print(f'{dog.name} - невідома осіб {dog.gender}!')
        else:
            print(f'{dog.name} була в ветеренара')

        print('*' * 200)
