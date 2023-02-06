class Animal:
    def __init__(self, name: str, allowed_meal: set, age: int):
        """
        Класс некоего животного, отвечает за ведение жизнедеятельности представителя
        :param name: имя представителя
        :param allowed_meal: пищевые привычки
        :param age: возраст
        """
        self.name = name
        self.allowed_meal = allowed_meal
        self.age = age
        self.say_word = '???'
        self.eat_today = False  # Поле для перевірки чи їла тварина

    def eat(self, food: str):
        """
        Предлагаем животному еду, которое оно кушает в случае если та подходит
        :param food: предлагаемая еда
        """
        if food in self.allowed_meal:
            print(f'{self.name} кушает {food}')
            self.eat_today = True
        else:
            print(f'{self.name} не понимает что можно делать с {food}')
            #self.eat_today = False

    def say(self, count: int):
        """
        Что делает животное когда хочет привлечь ваше внимание
        :param count: насколько сильно животное хочет привлечь ваше внимание
        """
        for i in range(count):
            print(f'{self.name} привлекает ваше внимание: {self.say_word}')

    def treat(self):
        """
        Уделяем время животному, ухаживаем за ним
        """
        print(f'Вы ухаживаете за {self.name}')
