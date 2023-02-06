from animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(f'Пес {name}', {'мясо', 'кісточка', 'вода'}, age)
        self.say_word = 'Гав'
        self.breed = breed

    def treat(self) -> str:
        """
        Доглядаємо за собакою, прибираємо какахи на вулиці
        :return: Настрій піднявся + пакетик с какахамі
        """
        print(f'Ви доглядаєте за  {self.name} і Вам стає краще!')
        return 'Настрій піднявся + пакетик с какахамі!'
