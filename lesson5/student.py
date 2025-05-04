"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    """Класс, представляющий студента"""
    name: str
    age: int
    grades: list[int]
    __slots__ = ('name', 'age', 'grades')

class Course:
    """Класс, представляющий курс"""
    name: str
    students: list[Student]
    __slots__ = ('name', 'students')

if __name__ == "__main__":

    # код для проверки
    student1 = Student()
    student1.name = "John"
    student1.age = 20
    student1.grades = [90, 80, 85]

    student2 = Student()
    student2.name = "Jane"
    student2.age = 21
    student2.grades = [95, 85, 90]

    course = Course()
    course.name = "Math"
    course.students = [student1, student2]
