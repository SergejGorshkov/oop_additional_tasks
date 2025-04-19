import pytest

from lesson1.src.task import Task
from lesson1.src.user import User


@pytest.fixture
def first_user():
    return User(
        username="OleJik",
        email="oleg@mail.com",
        first_name="Oleg",
        last_name="Ivanov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата")
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username="Ivan",
        email="ivan@mail.com",
        first_name="Ivan",
        last_name="Olegov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить лук", "Купить лук для салата")
        ]
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025")
