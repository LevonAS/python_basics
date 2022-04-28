# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

# класс Stationery
class Stationery:
    def __init__(self,name):
        self.title = name

    def draw(self):
        print(f'{self.title} нужна каждому')

# класс Pen (ручка), наследующий Stationery
class Pen(Stationery):
    def draw(self):
        print(f'{self.title} на каждом столе')

# класс Pencil (карандаш), наследующий Stationery
class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} можно стереть')

# класс Handle (маркер), наследующий Stationery
class Handle(Stationery):
    def draw(self):
        print(f'{self.title} не смоешь')

a = Stationery('Канцелярская принадлежность')
a.draw()

b = Pen('Ручка')
b.draw()

c = Pencil('Карандаш')
c.draw()

d = Handle('Маркер')
d.draw()


# Канцелярская принадлежность нужна каждому
# Ручка на каждом столе
# Карандаш можно стереть
# Маркер не смоешь

