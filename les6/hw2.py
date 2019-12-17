"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

2. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Road:
    _length = "Длина"
    _width = "Ширина"

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        weight = 25
        depth = 5
        print(f"{weight*depth*self._width*self._length / 1000} - тонн")

asphalt_mass = Road(5000, 20)
asphalt_mass.calculation()

asphalt_mass2 = Road(3333, 10)
asphalt_mass2.calculation()


# class Worker:
#     name = 'Имя'
#     surname = 'Фамилия'
#     position = 'Должность'
#     wage = "Оклад"
#     bonus = "Премия"
#     _income = {"wage": wage, "bonus": bonus}
#
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print(self.name, self.surname)
#
#     def get_total_income(self):
#         print(self._income.get("wage") + self._income.get("bonus"))
#
# people1 = Position("Иван", "Иванов", "Слесарь", {"wage": 35000, "bonus": 15000})
# people1.get_full_name()
# people1.get_total_income()

