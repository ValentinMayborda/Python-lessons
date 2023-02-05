# Написати клас собака (Dog), схожий до класу кішка (Cat) з запису заняття.
# Інтегрувати клас собака до приюту домашніх питомців
# (скористатись файлом https://github.com/kyrrylo/learn-python-hillel-30-11-2022/blob/
# main/lesson_12/pet_shelter.py та доповнити його).
#
# Реалізувати наступні методи/поведінку в повсякденному житті собак:
#
# Їсти +
# Гуляти +
# Гавкати +
#
# Створити якнайменше 6 об'єктів класу собака (представників)' \
# рандомною генерацією чи вписати в код (можна читати з файлу,
# але краще уникати введення від користувача - так на користування
# програмою витрачається забагато часу).
#
# Включити перевірку кожного дня:
#
# Чи собака гуляла
# Чи собака їла
# Чи собака була у ветерінара хоч раз за останні півроку
from datetime import datetime


class Dog:

    def __init__(self, name: str, age: int, gender: str, breed: str,
                 preferable_meal: set, last_vet_check: datetime = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.fed_check = True

        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        return f'{self.gender.capitalize()} породи {self.breed} по імені {self.name}, віку {self.age}' \
               f' років, зазвичай їсть: {", ".join(self.preferable_meal)}'

    def woof(self, count: int):
        for i in range(count):
            print(f'{self.name} гавкає !')

    def eat(self, food: str):
        """
        Собака їсть. Ящко їжа не підходить собака лає та не їсть.
        :param food: їжа що дають собаці
       """
        if food in self.preferable_meal:
            print(f'{self.name} їсть {food} с задоволенням')
            self.fed_check = True
        else:
            print(f'{self.name} проходить повз {food} не по смаку! ')
            self.woof(3)
            self.fed_check = False

    def walk(self, hours: int):
        """
        Собака гуляє визначену кількість годин, якщо не голодна
        :param hours: скільки год гуляти
        """
        if self.fed_check:
            print(f'{self.name} гуляє з задоволенням ')
        else:
            print(f'{self.name} голодний, тому гуляти не піде')


# if __name__ == '__main__':
#     d = Dog('Джек', 3, 'мужской', 'дворняга', {'мясо', 'сухий корм', 'вода'})
#     print(d)
#     d.eat('мясо')
#     d.woof(1)
#     d.walk(3)
