class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # Получается геттер
    def email(self): # геттер
        return f'{self.first}.{self.last}@email.com'

    @property  # Получается геттер (преобразует метод в атрибут класса Employee, хранящий значение после `return`)
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter  # Сеттер (принимает имя геттера `fullname` и указывает, что это сеттер `.setter`).
    # Не имеет `return`!!! Описывает только процедуру изменения атрибутов
    def fullname(self, new_fullname):
        first, last = new_fullname.split(' ')
        self.first = first  # Переприсвоение нового имени
        self.last = last    # Переприсвоение новой фамилии

    @fullname.deleter  # Делитер (принимает имя геттера `fullname` и указывает, что это делитер `.deleter`).
    # Не имеет параметров и `return`!!! Только процедуру обнуления/удаления значений атрибутов
    def fullname(self):
        self.first = None  # Удаление имени
        self.last = None  # Удаление фамилии


    # def set_email(self, email): # сеттер
    #     self._email = email

emp1 = Employee('Ivan', 'Ivanov')
print(emp1.fullname)  # Вызов геттера. Получим 'Ivan Ivanov'

emp1.fullname = 'Petr Petrov'  # Так как есть сеттер для `fullname`, то можно переприсвоить новые значения
print(emp1.fullname)  # Вызов геттера. Получим 'Petr Petrov'

del emp1.fullname   # Удалили имя и фамилию через вызов делитера (del).
# Для этого нужно предварительно создать делитер для `fullname`
print(emp1.fullname)  # Получим 'None None'

