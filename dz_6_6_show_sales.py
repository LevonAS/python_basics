# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки:
# для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
#     ● просто запуск скрипта — выводить все записи;
#     ● запуск скрипта с одним параметром-числом — выводить все записи
#       с номера, равного этому числу, до конца;
#     ● запуск скрипта с двумя числами — выводить записи, начиная с
#       номера, равного первому числу, по номер, равный второму числу,
#       включительно.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# Нумерация записей начинается с 1.
import sys

FILENAME = 'bakery.csv'


def out_all():
    with open(FILENAME, encoding='utf-8') as f:
        for line in f:
            print(line, end="")


def out_start(start):
    with open(FILENAME, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= start - 1:
                print(line, end="")


def out_start_end(start, end):
    with open(FILENAME, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= start - 1 and i < end:
                print(line, end="")
            if i == end:
                break


if len(sys.argv) == 1:
    out_all()
if len(sys.argv) == 2:
    out_start(int(sys.argv[1]))
if len(sys.argv) > 2:
    out_start_end(int(sys.argv[1]), int(sys.argv[2]))

# Вероятно правильнее было-бы выполнять задание через .seek,
# но не понял как высчитывать начало строки при рандомной длине
# значения в строке.