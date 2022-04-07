# Написать функцию currency_rates(), принимающую в качестве аргумента
# код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой
# валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре
# был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#
# Функция должна возвращать кроме курса дату, которая передаётся в
# ответе сервера.

import requests
# Google рекомендует для парсинга XML использовать ElementTree
import xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_05UP
'''
Decimal смог придумать использовать только для округления выдаваемой
величины до более приятного глазу двух знаков в дробной части.
ROUND_05UP округляет 0 до единицы, если после него идет число 5 и выше.
"round =" - флаг необходимости округления
Поскольку Decimal не принимает NoneType пришлось вводить проверку '!= None'
'''


def currency_rates(char_code='USD', round = True):
    valute = {}
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    root = ET.fromstring(requests.get(url).content)
    # Парсим XML-сылку и создаём словарь из двух выбранных значений
    for child in root:
        valute[child[1].text] = float(child[4].text.replace(',', '.'))
    # Метод .upper() позволяет принимать код валюты в любом регистре
    result = valute.get(char_code.upper())
    if result != None:
        if round != True:
            return (valute.get(char_code.upper()))
        else:
            result = Decimal(valute.get(char_code.upper()))
            return (result.quantize(Decimal("1.00"), ROUND_05UP))
    else:
        return


def get_date():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    root = ET.fromstring(requests.get(url).content)
    return (root.attrib['Date'])

if __name__ == "__main__":
    print('  Дата запроса курса валюты: ', get_date())
    print('Курс валюты USD: ', currency_rates(),      ' руб.')
    print('  возвращаемое значение имеет type', type(currency_rates()))
    print('Курс валюты EUR: ', currency_rates('EUR', False), ' руб.')
    print('  возвращаемое значение имеет type',
          type(currency_rates('EUR', False)))
    # Запрашиваем код валюты с разным регистром символов
    print('Курс валюты gBp: ', currency_rates('gBp', True), ' руб.')
    # Запрашиваем заведомо неправильный код валюты
    print('Курс валюты AAA: ', currency_rates('AAA'), ' руб.')
