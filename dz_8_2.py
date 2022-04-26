# Написать регулярное выражение для парсинга файла логов web-сервера
# из ДЗ 6 урока nginx_logs.txt
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000]
# "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')

import re


# Можно за 2 мин написать код через сплит и индексы и получить результат
def parse_log(filename):
    with open(filename, encoding='utf-8') as f:
        res = []
        line_gen = (line for line in f)
        for row in line_gen:
            req = re.split(r' ', row)
            tup = req[0], req[3].lstrip('[') + " " + req[4].rstrip(']'),\
                  req[5].lstrip('"'), req[6], req[8], req[9]
            print('raw = ', row)
            print('parsed_raw = ', tup)
            with open('parse_log.txt', 'w', encoding='utf-8') as f:
                f.write(str(tup))


# А можно два дня собирать нужный pattern ..... и не собрать
def parse_log_r(filename):
    with open(filename, encoding='utf-8') as f:
        line_gen = (line for line in f)
        for row in line_gen:
            #print(el)
            # pattern for IP = r'^\d+(?:\.\d+){3}'
            # pattern for IP = r'^(\d+\.\d+\.\d+\.\d+)'
            pattern = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'#<remote_addr>
                       r'.*\[(\d{1,2}/\w+/\d{4}(?::\d\d){3}\s\+\d{4})\]'
                       r'.*"(\w+)\s'   #<request_type>
                       r'.*(/\w+/\w+)' #<requested_resource>
                       r'.*"\s(\d+)'   #<response_code>
                       r'.*\s(\d+)\s"'   #<response_size>
                       )
            number_re = re.compile(pattern)
            res = re.findall(number_re, row)
            if not res:
                raise TypeError('Строка содержит нечитаемые данные :',row)
            print('raw = ', row)
            print('parsed_raw = ', res[0])


parse_log('nginx_logs.txt')
parse_log_r('nginx_logs.txt')
