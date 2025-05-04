# Команда `pytest -s` в терминале - запуск тестов с выводом print-ов

from src.task import Task
import datetime

def test_task_init(task):
    """Тест инициализации класса Task"""
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.04.2025"


def test_task_create():
    """Тест на добавление новой задачи"""
    new_task = Task.new_task("Купить билеты", "Купить билеты на самолет")  #Создаем новую задачу
    assert new_task.name == "Купить билеты"
    assert new_task.description == "Купить билеты на самолет"
    assert new_task.status == "Ожидает старта"
    assert new_task.created_at == datetime.date.today().strftime("%d.%m.%Y")


def test_task_update(capsys, task):
    """
    Тест на обновление списка задач (проверка сеттера).
    Перехватываем поток печати в консоль при помощи capsys.
    """
    task.created_at = "01.04.2025"  # Задаем заведомо ошибочную дату (из прошлого)
    message = capsys.readouterr()  # Перехват сообщения в консоль и проверка последней строки в сообщении
    assert message.out.strip().split("\n")[-1] == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.date.today().strftime("%d.%m.%Y")  # Задаем текущую дату
    assert task.created_at == datetime.date.today().strftime("%d.%m.%Y")


def test_task_str(task):
    """Тест на строковое представление объектов класса Task (с использованием фикстуры task)"""
    # Вызов магического метода __str__ из класса Task для отображения информации об экземпляре класса
    assert str(task) == "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 20.04.2025"


def test_task_add(task_with_runtime1, task_with_runtime2):
    """Тест на сложение объектов (времени выполнения задачи) класса Task с использованием фикстур task_with_runtime1(2)"""
    assert task_with_runtime1 + task_with_runtime2 == 130
