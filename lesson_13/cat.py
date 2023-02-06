from animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str):
        """

        :param name:
        :param age:
        :param breed:
        """
        super().__init__(f'Кошка/кот {name}', {'рыба', 'мясо', 'молоко'}, age)
        self.say_word = 'Мяу'

    def treat(self) -> str:
        """
        Уделяем время животному, ухаживаем за ним
        :return: гладим кошку и настроение улучшается :)
        """
        print(f'Вы ухаживаете за {self.name} и вам становится приятно!')
        return 'Настроение улучшилось!'