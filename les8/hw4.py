"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

class Warehouse():

    def __init__(self, size, color, weight):
        self.size = size
        self.color = color
        self.weight = weight

    def main_characteristics(self):
        print(
            f'Размер - {self.size}\n'
            f'Цвет - {self.color}\n'
            f'Вес - {self.weight}\n'
        )

    def name(self):
        print("Склад оргтехники")

    def electron(self):
        print("Прибор электрический")

class Printer(Warehouse):

    def name(self):
        print("Принтер (наследуется от Gadjet)")

    def print_out(self):
        print("Распечатать с электронного носителя")

class Scanner(Warehouse):

    def name(self):
        print("Сканнер (наследуется от Gadjet)")

    def scan(self):
        print("Сделать скан")

class Xserox(Warehouse):

    def name(self):
        print("Ксерокс (наследуется от Gadjet)")

    def copy(self):
        print("Сделать копию")

sklad1 = Warehouse(input("Введите размер(ШхД, через пробел): "), input("Введите цвет:"), input("Введите вес (в кг):"))
sklad1.name()

printer1 = Printer(input("Введите размер(ШхД, через пробел): "), input("Введите цвет:"), input("Введите вес (в кг):"))
printer1.main_characteristics()
printer1.electron()