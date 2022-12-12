import time

print('****************** Український чат-бот v.1.001 ******************')

user_input = input("""Для початку спілкування введіть текст.
Для закінчення спілкування введіть - (Бувай/Надобраніч/Гудбай/До зустрічі)\n>>>""").lower()

while True:

    if 'бувай' in user_input or 'надобраніч' in user_input or 'гудбай' in user_input or 'до зустрічі' in user_input:
        print("Побачимось у мережі, I'll be back.")
        time.sleep(1)
        exit(0)
    elif 'привіт' in user_input or 'хай' in user_input or 'доброго дня' in user_input:
        print('Вітаю, я бот з України!')
    elif 'як справи' in user_input or 'що робиш' in user_input or 'чим займаєшся' in user_input:
        time.sleep(2)
        print('Вчусь програмувати на Python!')
    elif 'фільм' in user_input or 'кінотеатр' in user_input or 'серіал' in user_input:
        if 'фільм' in user_input:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм "Престиж", він просто бомба!')
        elif 'кінотеатр' in user_input:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але сходіть в кінотеатр на фільм \
"Вартові галактик", він просто бомба!')
        else:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Венздей", він дуже цікавий!')
    else:
        print('Розмовляли, балакали і на тобі ЗдрастЄ! Нічого не зрозуміло!')

    user_input = input(">>>").lower()
