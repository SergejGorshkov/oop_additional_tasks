import pytest
from pyexpat.errors import messages

from src.task import Task


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
    assert first_user.task_list == (f"Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 20.04.2025\n"
                                    f"Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 20.04.2025\n")


def test_user_task_list_setter(first_user, task):
    """"Тест сеттера `user_task_list`"""
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task  # Задаем новую задачу и общее кол-во задач должно увеличиться на 1
    assert len(first_user.task_in_list) == 3


def test_user_str(first_user):
    """Проверка работы строкового представления объекта класса User с фикстурой first_user"""
    assert str(first_user) == "Ivanov Oleg, Email: oleg@mail.com, Всего задач в списке: 2"


# Тестирование работы класса TaskIterator выполняем здесь, чтобы не переопределялись фикстуры и не увеличивалось
# количество задач и кол-во пользователей
def test_task_iterator(task_iterator):
    """Тест работы итератора из класса TaskIterator с фикстурой task_iterator"""
    iter(task_iterator)  # Переопределение метода __iter__, чтобы индекс для перебора последовательности объектов
    # класса Task обнулился

    assert task_iterator.index == 0  # Проверка, что первоначальное значение индекса = 0

    # В task_iterator указана фикстура second_user с тремя задачами
    assert next(task_iterator).name == "Купить огурцы"  # Проверка, что имя экземпляра класса Task соответствует
    # названию первой задачи
    assert next(task_iterator).name == "Купить помидоры"  # Проверка, что имя экземпляра класса Task соответствует
    # названию второй задачи
    assert next(task_iterator).name == "Купить лук"  # Проверка, что имя экземпляра класса Task соответствует
    # названию третьей задачи

    with pytest.raises(StopIteration):  # Проверка корректного завершения работы итератора
        next(task_iterator)


def test_user_task_list_setter_error(first_user):
    """"Тест сеттера `user.task_list` на сложение объекта класса Task c объектом другого класса"""
    with pytest.raises(TypeError):
        first_user.task_list = 1

def test_user_task_list_setter_periodic_task(first_user, task_periodic_1):
    """"Тест сеттера `user.task_list` на сложение родственных объектов класса Task и PeriodicTask"""
    first_user.task_list = task_periodic_1
    assert first_user.task_in_list[-1].name == "Купить огурцы"  # Проверка, что новая задача добавлена в список задач

def test_middle_runtime(first_user, user_without_tasks):
    """Тест работы метода для определения среднего времени выполнения всех задач объекта класса User"""
    assert first_user.middle_task_runtime() == 45
    assert user_without_tasks.middle_task_runtime() == 0

def test_custom_exception(capsys, first_user):
    """Тест на возбуждение ошибки """
    assert len(first_user.task_in_list) == 2

    task_add = Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025")
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя задать задачу с нулевым временем выполнения"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"

    task_add = Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025", run_time=60)
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Задача добавлена успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"
