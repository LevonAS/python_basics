"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта
и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod

# класс Одежда
class Clothes(ABC):
    @abstractmethod
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def fabric_calc(self):
        pass

    @property
    def sum_fabric_calc(self):
        return coat.fabric_calc + сostume.fabric_calc

# класс Пальто, наследующий Одежда
class Сoat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def fabric_calc(self):
        return self.size/6.5 + 0.5

# класс Костюм, наследующий Одежда
class Costume(Clothes):
    def __init__(self, name ,height):
        self.name = name
        self.height = height

    @property
    def fabric_calc(self):
        return 2*self.height/100 + 0.3


if __name__ == '__main__':
    coat = Сoat('Редингот', 52)
    print(f'Пальто модели {coat.name} размера {coat.size} '
          f'требует для пошива {coat.fabric_calc} кв.м. ткани.')

    сostume = Costume('Классика', 185)
    print(f'Костюм модели {сostume.name} на рост {сostume.height} см '
          f'требует для пошива {сostume.fabric_calc} кв.м. ткани.')

    print(f'Общий расход ткани - {coat.sum_fabric_calc} кв.м.')
    print(f'Общий расход ткани - {сostume.sum_fabric_calc} кв.м.')

# Пальто модели Редингот размера 52 требует для пошива 8.5 кв.м. ткани.
# Костюм модели Классика на рост 185 см требует для пошива 4.0 кв.м. ткани.
# Общий расход ткани - 12.5 кв.м.
# Общий расход ткани - 12.5 кв.м.
