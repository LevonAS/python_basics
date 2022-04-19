# Не используя библиотеки для парсинга, распарсить (получить
# определённые данные) файл логов web-сервера nginx_logs.txt —
# получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>).
# Например:
#[
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Код должен работать даже с файлами, размер которых превышает
# объем ОЗУ компьютера.

# Намёк на оооочень большой размер иходного log-файла -
# видимо рекомендация на использование генератора.
from pprint import pprint


def parse_log(filename):
    with open(filename, encoding='utf-8') as f:
        res = []
        line_gen = (line for line in f)
        for el in line_gen:
            # Разделяем строку исходного запроса по пробелам
            req = el.split(" ")
            # Из трёх необходимых выделенных элементов составляем кортеж
            tup = req[0], req[5].lstrip('"'), req[6]
            # Кортежи превращаются в список
            res.append(tup)
        return res


result = parse_log('nginx_logs.txt')
pprint(result)
with open('parse_log.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))

# [('93.180.71.3', 'GET', '/downloads/product_1'),
# ... ,
# ('144.76.151.58', 'GET', '/downloads/product_2'),
# ('79.136.114.202', 'GET', '/downloads/product_1')]

# Объём исходных данных превышает допустимый размер вывода в PyCharm.
# На экран выводится только последняя допустимая часть результата.
# Поэтому дополнительно сделал полный вывод в файл parse_log.txt

# pprint нужен только для более приятного глазу вывода кортежей.
# С простым print будет одна мегадлинная строка с кривыми переносами.
