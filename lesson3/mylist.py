"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
которое можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""


class MyList:
    data: list


    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            raise ValueError("Это не список!")

    def __repr__(self):
        return f"{self.__class__.__name__}({[i for i in self.data]})"

    def __str__(self):
        return f"{[i for i in self.data]}"

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        if isinstance(other.data, list):
            return self.data + other.data


if __name__ == '__main__':

    # код для проверки
    my_list1 = MyList([1, 2, 3])
    print(repr(my_list1))  # MyList([1, 2, 3])
    print(str(my_list1))  # [1, 2, 3]
    print(len(my_list1))  # 3

    my_list2 = MyList([4, 5, 6])
    my_list3 = my_list1 + my_list2
    print(my_list3)  # [1, 2, 3, 4, 5, 6]
