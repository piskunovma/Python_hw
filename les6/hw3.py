"""
3. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    speed = "Скорость"
    color = "Цвет"
    name = "Название"
    is_police = 'Полицеская машина'

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч ')

    def police(self):
        if self.is_police == True:
            print("Полиция")
        else:
            print('Не полиция')

class TownCar(Car):

    is_police = False

    def surname(self):
        print('Городская машина')

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Ваша скорость - {self.speed} км/ч ')

class WorkCar(Car):

    is_police = False

    def surname(self):
        print('Рабочая машина')

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Ваша скорость - {self.speed} км/ч ')

class SportCar(Car):

    is_police = False

    def surname(self):
        print('Спортивная машина')

class PoliceCar(Car):

    is_police = True

    def surname(self):
        print('Полицейская машина')


car1 = WorkCar(77, 'Green', 'Kia')
car1.surname()
car1.turn("вправо")
car1.police()
car1.show_speed()

car2 = TownCar(23, 'Red', 'Audi')
car2.surname()
car2.police()

car3 = PoliceCar(334, "Black", "Lada")
car3.surname()
car3.show_speed()
car3.police()
print(car3.color)

car4 = SportCar(100, "White", 'Porshe')
car4.surname()
car4.go()
car4.stop()
car4.show_speed()


