# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

from time import perf_counter as TPC
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print('Вариант через индексы :')
start = TPC()
result_prev = [src[i+1] for i in range(1, len(src)-1) if src[i] < src[i+1]]
print(result_prev)
print('Время:', TPC() - start,  '  Память:', sys.getsizeof(result_prev))
print()

# Вариант с использованием генератора


def previous_values(values):
    result = []
    gen_num = (num for num in values)
    el_prev = next(gen_num)
    for el in gen_num:
        if el > el_prev:
            result.append(el)
        el_prev = el
    return result


start = TPC()
print('Вариант с использованием генератора :')
print(previous_values(src))
print('Время:', TPC() - start,  '  Память:', sys.getsizeof(previous_values(src)))

# На таком коротком списке сложно оценить производительность
