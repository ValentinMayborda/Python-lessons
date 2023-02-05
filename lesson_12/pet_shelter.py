#from cat import Cat
import random
from datetime import datetime, timedelta


if __name__ == '__main__':
    # create pets
    cats = list()
    cat_food = [
        'whiskas',
        'мясо',
        'рыба',
        'молоко',
        'вода',
        'сухой корм',
        'purina pro',
        'gourmet',
        'club 4 paws'
    ]
    last_vet_check = datetime.now()
    for name in [
        'Белочка', 'Арабика', 'Пинки', 'Дымка', 'Санни', 'Тень', 'Бланка', 'Лили', 'Фокси', 'Блэки', 'Полоска', 'Брауни', 'Злата'
    ]:
        last_vet_check -= timedelta(days=30)
        cats.append(Cat(
            name=name,
            gender=random.choice(['кот', 'кошка']),
            age=random.randint(1, 15),
            breed='',
            preferable_meal=set(random.choices(cat_food, k=5)),
            last_vet_check=last_vet_check
        ))

    # performing pet everyday lifestyle
    for cat in cats:
        cat.sleep(4)
        for food in random.choices(cat_food, k=5):
            cat.eat(food)

    # check if all pets are good
    for cat in cats:
        print(f'Проверяем всё ли хорошо с {cat}')
        if not cat.fed_check:
            if cat.gender == 'кошка':
                print(f'Warning! {cat.name} голодна!')
            elif cat.gender == 'кот':
                print(f'Warning! {cat.name} голоден!')
            else:
                print(f'{cat.name} - unknown gender {cat.gender}!')
        if not cat.vet_check:
            if cat.gender == 'кошка':
                print(f'Warning! {cat.name} давно не проверялась у ветеринара!')
            elif cat.gender == 'кот':
                print(f'Warning! {cat.name} давно не проверялся у ветеринара!')
            else:
                print(f'{cat.name} - unknown gender {cat.gender}!')