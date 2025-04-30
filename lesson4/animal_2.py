"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:
    name: str
    def __init__(self, name):
        self.name = name

    def walk(self):
        pass


class Dog(Animal):

    def bark(self):
        print('Bark!')


class Cat(Animal):

    def meow(self):
        print('Meow!')


if __name__ == "__main__":
    animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

    for animal in animals:
        if issubclass(type(animal), Dog):
            animal.bark()
        elif issubclass(type(animal), Cat):
            animal.meow()
