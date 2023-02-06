from cat import Cat
from hen import Hen
from cow import Cow
from dog import Dog
import random


if __name__ == '__main__':
    animals = [
        Cat('Дымок', 3, 'дворовая'),
        Hen(1),
        Cow('Бурёнка', 4),
        Dog('Скубі Ду', 8, 'богзнаякої')
    ]
    food_variants = [
        'трава',
        'сено',
        'пшено',
        'зерно',
        'рыба',
        'мясо',
        'молоко',
        'кісточка',
        'вода'
    ]

    what_we_get = list()
    what_they_get = list()

    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=5):
            a.eat(food)
            what_they_get.append(food)
        what_we_get.append(a.treat())

    print(f'What we lost: {what_they_get}')
    print(f'What we got: {what_we_get}')

    # Для всіх представників класів Cow, Cat, Hen, Dog реалізувати перевірку голодна чи сита
    # наприкінці дня (тобто активності). Вивести на екран які тварини потребує догляду.
    is_ok_count = 0
    for animal in animals:
        if not animal.eat_today:
            print(f'{animal.name} потребує Вашого догляду, погодуйте!!')
            is_ok_count += 1

    if is_ok_count == 0:
        print('Всі тварини нагодовані!')



