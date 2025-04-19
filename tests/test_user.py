import datetime


def test_user_init(first_user, second_user):
    """Тест инициализации класса User"""
    assert first_user.username == "OleJik"
    assert first_user.email == "oleg@mail.com"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2  # То же, что и assert User.users_count == 2
    assert second_user.users_count == 2  # То же, что и assert User.users_count == 2

    assert first_user.all_tasks_count == 5  # Кол-во задач у обоих пользователей д.б. одинаковым и равным сумме всех задач
    assert second_user.all_tasks_count == 5


def test_user_task_list_property(first_user):
    """"Тест геттера `user_task_list`"""
    assert first_user.task_list == (f"Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: "
                                    f"{datetime.date.today().strftime("%d.%m.%Y")}\nКупить помидоры, Статус "
                                    f"выполнения: Ожидает старта, Дата создания: "
                                    f"{datetime.date.today().strftime("%d.%m.%Y")}\n")
    # Здесь дата задана неявно, т.к. при запуске тестов в другой день, значения не совпадут


def test_user_task_list_setter(first_user, task):
    """"Тест сеттера `user_task_list`"""
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task  # Задаем новую задачу и общее кол-во задач должно увеличиться на 1
    assert len(first_user.task_in_list) == 3
