from animal import Animal


class Cow(Animal):
    def __init__(self, name: str, age: int):
        """
        Класс коровы, отвечает за жизнедеятельность представителей
        :param name:
        :param age:
        """
        # вызов метода класса-родителя
        super().__init__(f'Корова {name}', {'трава', 'сено'}, age)
        # уточняем методы привлечения внимания для коровы
        self.say_word = 'мууу'

    def treat(self) -> str:
        """
        Уделяем время животному, ухаживаем за ним
        :return: корова даёт молоко!
        """
        print(f'Вы ухаживаете за {self.name} и корова даёт молоко!')
        return 'Ведро молока'


# if __name__ == '__main__':
#     c = Cow('Бурёнка', 3)
#     # c = Cow('Бурёнка', {'трава', 'сено'}, age=3)
#     print(c)
#     c.eat('мясо')
#     c.eat('трава')
#     c.say(2)
#     c.treat()
#     print(isinstance(c, Cow))
#     print(isinstance(c, Animal))
#     # super (superior class) - родительский класс
#     # наследники получают "в наследство" все поля/атрибуты/свойства и методы/поведение/функции родительского класса
#     # так же на вопрос: являешься ли ты представителем "родительского класса"? Наследник имеет полное право отвечать: Да!
#     # наследник может расширять, дополнять и частично менять наследуемое
#
#     a = Animal('Неизвестная дичь', {'?'}, age=5)
#     print(a)
#     a.eat('мясо')
#     a.say(3)
#     a.treat()
#     # a.moo(3)  # выдаёт ошибку
#     print(isinstance(a, Cow))
#     print(isinstance(a, Animal))
#     # класс-родитель вообще не вкурсе того что происходит и не знает о своих наследниках
#     # нету никакой обратной связи, в принципе