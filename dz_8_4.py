# Написать декоратор с аргументом-функцией (callback), позволяющий
# валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Можно-ли замаскировать работу декоратора?

from functools import wraps

def val_checker(check_expression):
    def checking(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not check_expression(arg):
                    raise ValueError(
                     'Отрицательное число в списке аргументов: '
                        , f'{func.__name__}',arg)
            for i in kwargs:
                if not check_expression(kwargs[i]):
                    raise ValueError(
                     'Отрицательное число в списке аргументов: '
                        , f'{func.__name__}', kwargs[i])
            return func(*args, **kwargs)
        return wrapper
    return checking


@val_checker(lambda x: x > 0)
def calc_cube(*args, **kwargs):
    calc = []
    for x in args:
        calc.append(x**3)
    if kwargs:
        for i in kwargs:
            calc.append(kwargs[i] ** 3)
    return calc


result = calc_cube(3, 5, a=-8)
print('Результат возведения в куб каждого числа: ',result)

# result = calc_cube(3, 5, a=8)
# Результат возведения в куб каждого числа:  [27, 125, 512]

# result = calc_cube(3, -5, a=8)
#
# Traceback (most recent call last):
#     raise ValueError(
# ValueError: ('Отрицательное число в списке аргументов: ', 'calc_cube', -5)

# result = calc_cube(3, 5, a=-8)
#
# Traceback (most recent call last):
#    raise ValueError(
# ValueError: ('Отрицательное число в списке аргументов: ', 'calc_cube', -8)

# Для примера работы декоратора выбрана функция возведения в куб
# каждого из заданных значений.
# Запрещено обрабатывать отрицательные значения.
