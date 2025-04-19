
def test_task_init(task):
    """Тест инициализации класса Task"""
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.04.2025"

