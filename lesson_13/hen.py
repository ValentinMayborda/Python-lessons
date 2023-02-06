from animal import Animal


class Hen(Animal):
    def __init__(self, age: int):
        super().__init__('Курица', {'пшено', 'зерно'}, age)
        self.say_word = 'Кудах-кудах'

    def treat(self) -> str:
        """
        Уделяем время животному, ухаживаем за ним
        :return: курица несет яйца!
        """
        print(f'Вы ухаживаете за {self.name} и курица несёт яйца!')
        return 'Куриные яйца'