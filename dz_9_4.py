# Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name,
# is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась,повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина  остановилась')

    def turn(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(f'Текущая скорость автомобиля:  {self.speed} км/ч')

    def check_police(self):
        if self.is_police == True:
            print(f'Это полицейский автомобиль')

class TownCar (Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение допустимой скорости на '
                  f'{self.speed - 60} км/ч')
        else:
            print(f'Текущая скорость автомобиля:  {self.speed} км/ч')


class SportCar (Car):
    pass

class WorkCar (Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение допустимой скорости на '
                  f'{self.speed - 40} км/ч')
        else:
            print(f'Текущая скорость автомобиля:  {self.speed} км/ч')

class PoliceCar (Car):
    pass


ferrari = SportCar(180, 'red', 'Ferrari', False )
print(f'Марка автомобиля: {ferrari.name}, Цвет автомобиля: {ferrari.color}')
ferrari.go()
ferrari.show_speed()
ferrari.check_police()
print()

ford = PoliceCar(0, 'black', 'Ford', True )
print(f'Марка автомобиля: {ford.name}, Цвет автомобиля: {ford.color}')
ford.stop()
ford.show_speed()
ford.check_police()
print()

kia = TownCar(80, 'blue', 'Kia', False )
print(f'Марка автомобиля: {kia.name}, Цвет автомобиля: {kia.color}')
kia.show_speed()
kia.check_police()
print()

skoda = TownCar(40, 'grey', 'Skoda', False )
print(f'Марка автомобиля: {skoda.name}, Цвет автомобиля: {skoda.color}')
skoda.turn()
skoda.show_speed()
skoda.check_police()

# Марка автомобиля: Ferrari, Цвет автомобиля: red
# Машина поехала
# Текущая скорость автомобиля:  180 км/ч
#
# Марка автомобиля: Ford, Цвет автомобиля: black
# Машина  остановилась
# Текущая скорость автомобиля:  0 км/ч
# Это полицейский автомобиль
#
# Марка автомобиля: Kia, Цвет автомобиля: blue
# Превышении допустимой скорости на 20 км/ч
#
# Марка автомобиля: Skoda, Цвет автомобиля: grey
# Машина повернула налево
# Текущая скорость автомобиля:  40 км/ч

