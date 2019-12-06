# def my_f(*args):
#     print(type(args))
#     result = 0
#     for itm in args:
#         result += itm
#     return result
#
# myl_list = [1, 2, 3, 4 ,5, 6]
# test = my_f(*myl_list)
# print(test)

# def my_f(var1: int, var2: int) -> int:
#     """
#     Функция возводит в степень
#     :param var1: int - первый аргумент
#     :param var2: int - второй аргумент
#     :return: int - результат работы функции
#     """
#
#     result = var1 ** var2
#     def my_f2(var3, var4):
#         return result + var3 * var4
#     return my_f2
#
# a1 = 2
# a2 = 3
#
# test = my_f(a1, a2)
# test2 = my_f(12, 3)
# test3 = my_f(4, 6)
# print(test(2, 3))
# print(test2(2, 3))
# print(test3(2, 3))
# print(my_f.__doc__)

def my_f(**kwargs) -> dict:
    """
    Функция возводит в степень
    :param var1: int - первый аргумент
    :param var2: int - второй аргумент
    :return: int - результат работы функции
    """
    for key, value in kwargs.items():
        print(key, value)

tmp = {'name':222, 'value': 'fhfhfhfh'}
test = my_f(**tmp)