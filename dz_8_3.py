# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Можно-ли вы вывести тип значения функции?
# Можно-ли решить задачу для именованных аргументов?
# Можно-ли вы замаскировать работу декоратора?
# Можно-ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        args_res = (', '.join([f' {i}: {type(i)}' for i in args]))
        if not kwargs:
            kwargs_res = None
        kwargs_res = (', '.join([f', {i} = {kwargs[i]}: {type(i)}'
                      for i in kwargs]))
        print(f'{func.__name__}(',args_res, kwargs_res, ')')
        print('Вывод типов значений функции',
              ', '.join([f'{i}: {type(i)}' for i in res]))
        return res
    return wrapper


@type_loger
def calc_cube(*args, **kwargs):
    calc = []
    for x in args:
        calc.append(x**3)
    if kwargs:
        for i in kwargs:
            calc.append(kwargs[i] ** 3)
    return calc


result = calc_cube(3, 4.3, a=10, b=12.5)
print('Результат возведения в куб каждого числа: ',result)

# calc_cube(  3: <class 'int'>,  4.3: <class 'float'> ,
# a = 10: <class 'str'>, , b = 12.5: <class 'str'> )
# Вывод типов значений функции 27: <class 'int'>,
# 79.50699999999999: <class 'float'>, 1000: <class 'int'>,
# 1953.125: <class 'float'>
# Результат возведения в куб каждого числа:
# [27, 79.50699999999999, 1000, 1953.125]

# Для примера работы декоратора выбрана функция возведения в куб
# каждого из заданных значений