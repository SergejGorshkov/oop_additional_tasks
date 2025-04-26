"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    data:list


    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            raise ValueError("It`s not list!")
        self.index = 0

    def __iter__(self):
        """Возвращает итератор (сам объект - self, так как у него есть __next__)."""
        return self

    def __next__(self):
        """Возвращает следующий элемент последовательности."""
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # Завершаем итерацию


    def __getitem__(self, index):
        """Обеспечивает доступ к элементам по индексу или срезу."""
        if isinstance(index, int):  # Обработка обычного индекса
            if index < 0 or index >= len(self.data):
                raise IndexError("Индекс за пределами списка")
            return self.data[index]
        else:
            raise TypeError("Индекс должен быть целым числом")


if __name__ == '__main__':

    # код для проверки
    my_list = MyList2([1, 2, 3])
    for i in my_list:
        print(i)  # 1 2 3

    print(my_list[1])  # 2 (происходит вызов метода def __getitem__(self, index=1))
    print(my_list[2])  # 3
    print(my_list[0])  # 1


