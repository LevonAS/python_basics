"""
Разработайте проект «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру
(например, словарь).

Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
# Склад получился в достаточно базовом варианте.
# Особых проверок для него не придумал.
# Только ввёл лимит на количество размещения техники.


from datetime import datetime

class WarehouseLimit(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self, title):
        self.title = title
        self.bd = {}
        self.count = 0
        self.count_limit = 10

    # Приём оргтехники на склад: внесение в словарь данных об оборудовании,
    # серийный номер (ключ) и время поступления на склад
    def get_to_wh(self, equipment):
        if self.count == self.count_limit:
            raise WarehouseLimit('Закончилось место для размещения оборудования')
        else:
            dt = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.bd.update({equipment.serial_number:[equipment.type_eq,
                equipment.manufacturer, equipment.model, str(dt)]})
            print(f'{self.title} принял : {equipment.type_eq} '
                f'{equipment.manufacturer} {equipment.model}, '
                f'серийный номер - {equipment.serial_number}. '
                f'Дата поступления: {str(dt)}')
            self.count += 1
            if self.count == self.count_limit:
               raise WarehouseLimit('Закончилось место для размещения оборудования')

    # Передача оборудование на другой склад или в подразделение
    def transfer_to_wh(self, equipment, other):
        dt = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.bd.pop(equipment.serial_number)
        self.count -= 1
        print(f'{self.title} передал в {other.title} : {equipment.type_eq} '
              f'{equipment.manufacturer} {equipment.model}, '
              f'серийный номер - {equipment.serial_number}. '
              f'Дата передачи: {str(dt)}')
        other.get_to_wh(equipment)


class OfficeEquipment:
    def __init__(self, type_eq, manufacturer, model, serial_number):
        self.type_eq = type_eq
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number

class Printer(OfficeEquipment):
    def __init__(self, type_eq, manufacturer, model, print_speed, serial_number):
        super().__init__(type_eq, manufacturer, model, serial_number)
        self.print_speed = print_speed

    def __str__(self):
        return f'Название оборудования: {self.type_eq} {self.manufacturer} {self.model},\n' \
               f' Параметры: скорость печати - {self.print_speed} стр/мин (A4),\n' \
               f' Серийный номер: {self.serial_number}'

class Scanner(OfficeEquipment):
    def __init__(self, type_eq, manufacturer, model, scan_speed, serial_number):
        super().__init__(type_eq, manufacturer, model, serial_number)
        self.scan_speed = scan_speed

    def __str__(self):
        return f'Название оборудования: {self.type_eq} {self.manufacturer} {self.model},\n' \
               f' Параметры: скорость сканирования  - {self.scan_speed} стр/мин (A4),\n' \
               f' Серийный номер: {self.serial_number}'

class Copier(OfficeEquipment):
    def __init__(self, type_eq, manufacturer, model, copy_speed, serial_number):
        super().__init__(type_eq, manufacturer, model, serial_number)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Название оборудования: {self.type_eq} {self.manufacturer} {self.model},\n' \
               f' Параметры: скорость копирования  - {self.copy_speed} стр/мин,\n' \
               f' Серийный номер: {self.serial_number}'


if __name__ == '__main__':
    printer_1 = Printer('принтер', 'HP', 'LaserJet Pro M404dn', 38 ,'F03FSDV4FS332')
    scanner_1 = Scanner('сканер', 'Brother', 'ADS-2700W', 35 ,'9034DSF-23445')
    copier_1  = Copier('копир', 'Xerox', 'B205', 30 ,'SDSF00SDF9V')

    print(printer_1)
    print()
    print(scanner_1)
    print()
    print(copier_1)
    print()
    main_wh = Warehouse('Основной склад')
    pr_depart = Warehouse('Отдел PR')
    sales_depart = Warehouse('Отдел продаж')

    main_wh.get_to_wh(printer_1)
    main_wh.get_to_wh(scanner_1)
    main_wh.get_to_wh(copier_1)
    print(f'{main_wh.title} имеет в наличии {main_wh.count} единиц(ы) оборудования.')

    print()
    main_wh.transfer_to_wh(copier_1, pr_depart)
    print()
    main_wh.transfer_to_wh(printer_1, sales_depart)
    print()
    print(f'{main_wh.title} имеет в наличии {main_wh.count} единиц(ы) оборудования.')
    print(f'{main_wh.title} может разместить ещё '
          f'{main_wh.count_limit - main_wh.count} единиц(ы) оборудования.')
    print(main_wh.bd)
    print(f'{pr_depart.title} имеет в наличии {pr_depart.count} единиц(ы) оборудования.')
    print(f'{pr_depart.title} может разместить ещё'
          f' {pr_depart.count_limit - pr_depart.count} единиц(ы) оборудования.')
    print(pr_depart.bd)
    print(f'{sales_depart.title} имеет в наличии {sales_depart.count} единиц(ы) оборудования.')
    print(f'{sales_depart.title} может разместить ещё '
          f'{sales_depart.count_limit - sales_depart.count} единиц(ы) оборудования.')
    print(sales_depart.bd)

# Название оборудования: принтер HP LaserJet Pro M404dn,
#  Параметры: скорость печати - 38 стр/мин (A4),
#  Серийный номер: F03FSDV4FS332
#
# Название оборудования: сканер Brother ADS-2700W,
#  Параметры: скорость сканирования  - 35 стр/мин (A4),
#  Серийный номер: 9034DSF-23445
#
# Название оборудования: копир Xerox B205,
#  Параметры: скорость копирования  - 30 стр/мин,
#  Серийный номер: SDSF00SDF9V
#
# Основной склад принял : принтер HP LaserJet Pro M404dn, серийный номер - F03FSDV4FS332. Дата поступления: 07-05-2022 03:02
# Основной склад принял : сканер Brother ADS-2700W, серийный номер - 9034DSF-23445. Дата поступления: 07-05-2022 03:02
# Основной склад принял : копир Xerox B205, серийный номер - SDSF00SDF9V. Дата поступления: 07-05-2022 03:02
# Основной склад имеет в наличии 3 единиц(ы) оборудования.
#
# Основной склад передал в Отдел PR : копир Xerox B205, серийный номер - SDSF00SDF9V. Дата передачи: 07-05-2022 03:02
# Отдел PR принял : копир Xerox B205, серийный номер - SDSF00SDF9V. Дата поступления: 07-05-2022 03:02
#
# Основной склад передал в Отдел продаж : принтер HP LaserJet Pro M404dn, серийный номер - F03FSDV4FS332. Дата передачи: 07-05-2022 03:02
# Отдел продаж принял : принтер HP LaserJet Pro M404dn, серийный номер - F03FSDV4FS332. Дата поступления: 07-05-2022 03:02
#
# Основной склад имеет в наличии 1 единиц(ы) оборудования.
# Основной склад может разместить ещё 9 единиц(ы) оборудования.
# {'9034DSF-23445': ['сканер', 'Brother', 'ADS-2700W', '07-05-2022 03:02']}
# Отдел PR имеет в наличии 1 единиц(ы) оборудования.
# Отдел PR может разместить ещё 9 единиц(ы) оборудования.
# {'SDSF00SDF9V': ['копир', 'Xerox', 'B205', '07-05-2022 03:02']}
# Отдел продаж имеет в наличии 1 единиц(ы) оборудования.
# Отдел продаж может разместить ещё 9 единиц(ы) оборудования.
# {'F03FSDV4FS332': ['принтер', 'HP', 'LaserJet Pro M404dn', '07-05-2022 03:02']}
