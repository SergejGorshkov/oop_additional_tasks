# Команда `pytest -s` в терминале - запуск тестов с выводом print-ов
import pytest


def test_periodic_task_init(task_periodic_1):
    """Тест инициализации класса PeriodicTask"""
    assert task_periodic_1.name == "Купить огурцы"
    assert task_periodic_1.description == "Купить огурцы для салата"
    assert task_periodic_1.start_date == "01.04.2025"
    assert task_periodic_1.end_date == "01.06.2025"
    assert task_periodic_1.status == "Ожидает старта"
    assert task_periodic_1.created_at == "20.04.2025"
    assert task_periodic_1.frequency == "Ежедневная"


def test_periodic_task_add(task_periodic_1, task_periodic_2):
    """Тест на сложение объектов (времени выполнения задачи) класса PeriodicTask с использованием фикстур task_periodic_1(2)"""
    assert task_periodic_1 + task_periodic_2 == 120


def test_periodic_task_add_error(task_periodic_1):
    """Тест на сложение объекта (времени выполнения задачи) класса PeriodicTask (с использованием фикстуры task_periodic_1) и другого класса"""
    with pytest.raises(TypeError):
        assert task_periodic_1 + 1

