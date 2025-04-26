# Продолжение работы над задачей из lesson1, lesson2 (уроки 14_1_9, 14_2_8)

from src.task import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []  # Атрибут `task_list` сделали приватным

        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0  # Счетчик количества задач будет увеличиваться
        # на длину списка задач, если он существует. Если список пустой, тогда не увеличивается


    def __str__(self):
        return f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"


    @property
    def task_list(self):
        """Геттер. Возвращает новую строку (тип str), содержащую подстроки из списка задач"""
        task_str = ""
        for task in self.__task_list:  # Перебор списка задач
            task_str += f"{str(task)}\n" # Представление задачи (объекта класса Task) в строковом формате путем вызова
            # магического метода def __str__(self) из класса Task
        return task_str

    @task_list.setter
    def task_list(self, new_task: Task):      # new_task - передаем новую задачу (тип - экземпляр класса Task)
        """Сеттер. Дополняет список задач новой задачей"""
        self.__task_list.append(new_task)

        User.all_tasks_count += 1  # Увеличиваем значение количества всех задач на 1

    @property
    def task_in_list(self):
        """Геттер. Возвращает список задач (тип list). Нужен для чтения(только!) содержимого приватного атрибута __task_list"""
        return self.__task_list


if __name__== "__main__":
    # Создаем 4 новых задачи
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    task_2 = Task("Купить помидоры", "Купить помидоры для салата")
    task_3 = Task("Купить лук", "Купить лук для салата")
    task_4 = Task("Купить перец", "Купить перец для салата")

    # Создаем 1 нового пользователя
    user = User("OleJik", "oleg@mail.com", "Oleg", "Ivanov", [task_1, task_2, task_3, task_4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_count)

    # Добавление новой задачи и вывод обновленного списка задач и количества всех задач
    task_5 = Task("Купить рукколу", "Купить рукколу для салата")
    user.task_list = task_5  # Вызов сеттера `task_list`
    print(user.task_list)
    print(User.all_tasks_count)

    print(user)
