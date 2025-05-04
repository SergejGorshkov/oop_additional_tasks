from pyexpat.errors import messages

from src.task import Task
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


def test_print_mixin(capsys):  # Перехват потока вывода в консоль при создании нового экземпляра класса Task
    Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025")
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.04.2025)"


    PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2025", "01.06.2025", created_at="20.04.2025",
                 run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.04.2025)"

    DeadlineTask("Купить перец", "Купить перец для салата", "20.05.2025", created_at="20.04.2025", run_time=60)
    message = capsys.readouterr()
    assert message.out.strip() == "DeadlineTask(Купить перец, Купить перец для салата, Ожидает старта, 20.04.2025)"
