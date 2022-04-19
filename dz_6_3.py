# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом
# — данные об их хобби. Известно, что при хранении данных используется
# принцип: одна строка — один пользователь, разделитель между значениями
# — запятая. Написать код, загружающий данные из обоих файлов и
# формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле,
# хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в
# словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#     Иванов,Иван,Иванович
#     Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
#     скалолазание,охота
#     горные лыжи

import csv
import sys


def parse_csv_file(filename):
    with open(filename ,encoding='utf-8') as f:
        return list(f)


users_l = parse_csv_file('dz_6_3_users.csv')
hobby_l = parse_csv_file('dz_6_3_hobby.csv')

# Дополняем hobby_l елементом None если длина hobby_l меньше длины users_l
if len(users_l) > len(hobby_l):
    for i in range(len(users_l) - len(hobby_l)):
        hobby_l.append(None)
        print(hobby_l)

if len(users_l) == len(hobby_l):
    dict = {}
    for i in range(0, len(users_l)):
       dict[users_l[i].rstrip('\n')] = hobby_l[i].rstrip('\n')
    print(dict)
    with open('dz_6_3_out.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=':')
        for key, value in dict.items():
            writer.writerow([key, value])

# Выход из программы с завершающим кодом 1 (sys.exit(1))
if len(users_l) < len(hobby_l):
    sys.exit(1)
