"""
Напишите класс Counter, имеющий следующие методы:

- __init__(self): конструктор, создающий счетчик и устанавливающий его значение в 0;
- __call__(self): магический метод, который позволяет использовать объект класса Counter как функцию, возвращающую текущее значение счетчика;
- increment(self): метод, увеличивающий значение счетчика на 1.
"""


class Counter:
    def __init__(self):
        self.value = 0

    def __call__(self, *args, **kwargs):
        return self.value

    def increment(self):
        self.value += 1
        return self.value

if __name__ == '__main__':
    # код для проверки
    counter = Counter()
    print(counter())  # 0

    counter.increment()
    print(counter())  # 1

    counter.increment()
    print(counter())  # 2
