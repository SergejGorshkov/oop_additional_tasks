"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "Flying".

Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".

Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:

- hunt(self): метод, который выводит сообщение "Hunting".
"""


class Bird:
    """Класс, представляющий птицу"""
    # def __init__(self):
    def fly(self):
        """ Метод, который выводит сообщение "Flying" """
        print("Flying")

class Penguin(Bird):
    """Подкласс, представляющий пингвина"""
    def fly(self):
        """ Метод, который выводит сообщение "I am a penguin and cannot fly" """
        print("I am a penguin and cannot fly")

class Eagle(Bird):
    """Подкласс, представляющий орла"""
    def hunt(self):
        """ Метод, который выводит сообщение "Hunting" """
        print("Hunting")


if __name__ == "__main__":
    # код для проверки
    bird = Bird()
    bird.fly()  # Flying

    penguin = Penguin()
    penguin.fly()  # I am a penguin and cannot fly

    eagle = Eagle()
    eagle.fly()  # Flying (класс Eagle по умолчанию имеет метод fly от родительского класса Bird)
    eagle.hunt()  # Hunting
