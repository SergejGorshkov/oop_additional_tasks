"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime


class Car:
    brand: str
    model: str
    year: int
    def __init__(self, brand, model, year):
        self.model = model
        self.brand = brand
        if year > datetime.datetime.now().year:
            raise Exception("Эта машина еще не была выпущена")
        self.year = year

if __name__ == "__main__":

    # код для проверки
    car = Car('Toyota', 'Corolla', 2022)

    car = Car('Toyota', 'Corolla', 3000)
    # raises Exception('Эта машина еще не была выпущена')
