from dz_4_3_currency_rates import currency_rates, get_date

print('  Дата запроса курса валюты: ', get_date())
print('Курс валюты USD: ', currency_rates(),      ' руб.')
print('Курс валюты EUR: ', currency_rates('EUR', False), ' руб.')
# Запрашиваем код валюты с разным регистром символов
print('Курс валюты gBp: ', currency_rates('gBp', True), ' руб.')
# Запрашиваем заведомо неправильный код валюты
print('Курс валюты AAA: ', currency_rates('AAA'), ' руб.')
