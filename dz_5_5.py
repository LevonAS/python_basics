# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка
# их следования в исходном списке, например:
#   src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#     result = [23, 1, 3, 10, 4, 11]

from time import perf_counter as TPC

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

# Вариант в лоб
result.clear()
start = TPC()
result = [el for el in src if src.count(el) == 1]
print('Результат = ', result, '  Затраченное время: ', TPC() - start)

# Через множества, предпочтителен при большом количестве исходных данных
result.clear()
start = TPC()
unique_el = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_el.add(el)
    else:
        unique_el.discard(el)
    tmp.add(el)
result = [el for el in src if el in unique_el]
print('Результат = ', result, '  Затраченное время: ', TPC() - start)

# Собственно оба варианта из методички
