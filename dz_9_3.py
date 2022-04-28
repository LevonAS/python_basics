# Реализовать базовый класс Worker (работник).
# Определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position (Worker):
    def get_full_name(self):
        print(self.surname + ' ' + self.name)

    def get_total_income(self):
        res = self._income['wage'] + self._income['bonus']
        print("Доход работника: ", res)


a = Position('Иван', 'Иванов', 'сисадмин', 55000, 40000 )
a.get_full_name()
print(a.position)
a.get_total_income()
print()

b = Position('Пётр', 'Петров', 'водитель', 45000, 30000  )
b.get_full_name()
print(b.position)
b.get_total_income()

# Иванов Иван
# сисадмин
# Доход работника:  95000
#
# Петров Пётр
# водитель
# Доход работника:  75000
