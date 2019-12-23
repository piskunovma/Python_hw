"""
3. Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

# class MyListError(Exception):
#
#     def __init__(self, my_list):
#         self.my_list = my_list
#
#     def check_func(self):
#         try:
#             self.my_list = list(self.my_list)
#             i = 0
#             for itm in self.my_list:
#                 if not itm.isdigit():
#                     raise TypeError("Введите только числа!")
#                 self.my_list[i] = int(itm)
#                 i += 1
#             return self.my_list
#         except TypeError as err:
#             return err
#
# a = MyListError(input("Введите элемент списка: \n"))
#
# print(a.check_func())


class MyListError(Exception):

    def check_func(self):
        my_list = []
        while True:
            my_number = input("Введите элемент списка: для завершения программы введите 'exit'\n")
            my_number.lower()
            if my_number == "exit":
                break
            try:
                if not my_number.isdigit():
                    raise TypeError("Введите число!")
                my_number = int(my_number)
                my_list.append(my_number)
            except TypeError as err:
                print(err)
        return my_list

a = MyListError()
print(a.check_func())

