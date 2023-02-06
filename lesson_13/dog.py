from animal import Animal


# Клас Dog наслідник супер класу Animal
class Dog(Animal):
    # Конструктор класу створює новий обєкт, тобто собаку по переданим параметрам
    def __init__(self, name: str, age: int, breed: str):
        # Ініціалізація супер класу Animal
        super().__init__(f'Пес {name}', {'мясо', 'кісточка', 'вода'}, age)
        self.say_word = 'Гав'
        self.breed = breed

    def treat(self) -> str:
        """
        Доглядаємо за собакою, прибираємо какахи на вулиці
        :return: Настрій піднявся + пакетик с какахамі
        """
        print(f'Ви доглядаєте за  {self.name} і граєтесь з ним на вулиці!')
        return 'Настрій піднявся + пакетик с какахамі!'
