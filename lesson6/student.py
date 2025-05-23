"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    name: str
    course: int
    rates: list[int] | list
    def __init__(self, name, course, rates):
        self.name = name
        self.course = course
        self.rates = rates if rates else []

    def avg_rate(self):
        result = round(sum(self.rates) / len(self.rates), 2) if self.rates else 0.0
        print(result)


if __name__ == "__main__":

    # код для проверки
    student = Student('Ivan', 'Python', [5, 4, 5, 5])
    student.avg_rate() # 4.75

    student = Student('Ivan', 'Python', [])
    student.avg_rate() # 0.0
