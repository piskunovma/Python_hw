"""
1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def data_numb(cls, data):

        res = data.split('-')
        i = 0
        for itm in res:
            res[i] = int(itm)
            i += 1
        return res

    @staticmethod
    def valid_data(res):

        if res[1] > 12 or res[1] < 1 or res[0] < 1 or res[0] > 31 or res[-1] < 1920 or res[-1] > 2019:
            return "Неверная дата"
        else:
            return res
        pass

# print(Data.data_numb("25-04-2019"))

result_data = Data("30-11-2000")
print(result_data.valid_data(Data.data_numb(result_data.data)))