
def test_user_init(first_user, second_user):
    """Тест инициализации класса User"""
    assert first_user.username == "OleJik"
    assert first_user.email == "oleg@mail.com"
    assert len(first_user.task_list) == 2

    assert first_user.users_count == 2  # То же, что и assert User.users_count == 2
    assert second_user.users_count == 2  # То же, что и assert User.users_count == 2

    assert first_user.all_tasks_count == 5  # Кол-во задач у обоих пользователей д.б. одинаковым и равным сумме всех задач
    assert second_user.all_tasks_count == 5
