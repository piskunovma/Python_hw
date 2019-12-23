"""
2. Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyError(Exception):

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def my_func(self):
        try:
            self.var1, self.var2 = int(self.var1), int(self.var2)
            if self.var2 == 0:
                raise ZeroDivisionError("Ошибка! На ноль делить нельзя!")
            return self.var1 / self.var2
        except ValueError:
            return "Введите число!"
        except ZeroDivisionError as err:
            return err

a = MyError(input("Введите делимое: \n"), input("Введите делитель: \n"))
print(a.my_func())