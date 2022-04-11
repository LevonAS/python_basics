# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#
# Вар2: решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя  ключевое слово yield.

# Вариант через yield


def nums_gen_y(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


num_gen_y = nums_gen_y(9)
print('Вывод результата варианта через yield :')
# Можно вывести результат списком
# print(list(num_gen_y))
# Можно вывести результат через next
print(type(num_gen_y))
print(next(num_gen_y))
print(next(num_gen_y))
print(next(num_gen_y))
print(next(num_gen_y))
print(next(num_gen_y))
print(next(num_gen_y))

# Вариант без yield
n = 9
nums_gen = (num for num in range(1, n + 1, 2))
print('Вывод результата варианта без yield :')
print(type(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
