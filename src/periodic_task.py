from src.task import Task

class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status="Ожидает старта", created_at=None, run_time=0,
                 frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError


if __name__== "__main__":
    periodic_task = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2025", "01.06.2025", run_time=60)
    print(periodic_task.name)
    print(periodic_task.description)
    print(periodic_task.status)
    print(periodic_task.created_at)

    print(periodic_task.start_date)
    print(periodic_task.end_date)
    print(periodic_task.frequency)
    print()  # Пустая строка

    periodic_task_2 = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2025", "01.06.2025", run_time=60)
    task_1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)

    print(periodic_task + periodic_task_2)  # 120
    print(periodic_task + task_1)  # TypeError, т.к. разные классы у объектов




