from lesson1.src.task import Task


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
        self.task_list = task_list if task_list else []

        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0  # Счетчик количества задач будет увеличиваться
        # на длину списка задач, если он существует. Если список пустой, тогда не увеличивается


if __name__== "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    task_2 = Task("Купить помидоры", "Купить помидоры для салата")
    task_3 = Task("Купить лук", "Купить лук для салата")
    task_4 = Task("Купить перец", "Купить перец для салата")

    user = User("OleJik", "oleg@mail.com", "Oleg", "Ivanov", [task_1, task_2, task_3, task_4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_count)

