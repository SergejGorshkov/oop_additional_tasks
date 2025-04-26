"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import datetime


class Timer:
    def __init__(self):
        self.elapsed_time = 0


    def __enter__(self):
         self.start = datetime.datetime.now()
         return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        self.elapsed_time = (self.end - self.start).total_seconds()  # Определяет разницу во времени в секундах (до микросекунд)



if __name__ == '__main__':

    with Timer() as timer:
        # блок кода
        sum_ = 0
        for i in range(1000000):
            sum_ += i + 1
        print(sum_)


    # код для проверки
    print("Execution time:", timer.elapsed_time)
