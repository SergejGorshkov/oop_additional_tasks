"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:
    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, (int, float)):  # если other - число
            return self.pay + other
        if isinstance(other.pay, (int, float)) and isinstance(other.pay, Employee):  # если other - объект класса Employee
            return self.pay + other.pay
        raise TypeError("Можно складывать только числа или объекты классов-наследников Employee")

class Client:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, (int, float)):  # если other - число
            return self.pay + other
        if isinstance(other.pay, (int, float)) and isinstance(other.pay, Client):  # если other - объект класса Client
            return self.pay + other.pay


class Developer(Employee):
    pass


class Manager(Employee):
    pass


if __name__ == "__main__":

    # код для проверки
    users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

    total_salary = 0
    # for user in users:
    #     total_salary = user + total_salary

    for user in users:
        if isinstance(user, Employee):
            total_salary = user + total_salary

    print(total_salary)
    # Вывод: 150000

    total_salary = 0
    for user in users:
        if isinstance(user, Client):
            total_salary = user + total_salary

    print(total_salary)
    # Вывод: 100000
