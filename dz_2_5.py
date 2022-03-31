# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде # <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
# или 00 коп).

prices = [57.8, 46.51, 97, 5.4, 34.1, 43, 0.99, 434.5, 2.09, 14.5]

temp_prices = []
for price in prices:
    temp_prices.append(f'{int(price)} руб {int(price * 100 % 100):02d} коп')
print('Заданные цены: ' , ', '.join(temp_prices))

print()
#
print('id cписка до сортировки:   ', id(prices))
prices.sort()
print('id cписка после сортировки:', id(prices))
temp_prices = []
for price in prices:
    temp_prices.append(f'{int(price)} руб {int(price * 100 % 100):02d} коп')
print('Цены по возрастанию: ' , ', '.join(temp_prices))

print()
# Создание нового списка с отсортированными ценами по убыванию
decr_price = sorted(prices, reverse=True)

# Вывывод цен пяти самых дорогих товаров через срез [:5]
temp_prices = []
for price in decr_price[:5]:
    temp_prices.append(f'{int(price)} руб {int(price * 100 % 100):02d} коп')
print('Пять самых дорогих товаров : ' , ', '.join(temp_prices))
# Вывести цены этих товаров по возрастанию, написав минимум кода
print('Пять самых дорогих товаров : ' , ', '.join(temp_prices[::-1]))
