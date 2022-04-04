# Написать функцию num_translate_adv(), переводящую числительные
# от 0 до 10 c английского на русский язык.
# Если числительное начинается с заглавной буквы — результат тоже
# должен быть с заглавной. Например:
# >>> num_translate_adv("One") >>> "Один"
# >>> num_translate_adv("eight") >>> "восемь"
# Если перевод сделать невозможно, вернуть None.


def num_translate_adv(eng_number):
    translate = {
        'zero':  'ноль',
        'one':   'один',
        'two':   'два',
        'three': 'три',
        'four':  'четыре',
        'five':  'пять',
        'six':   'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine':  'девять',
        'ten':   'десять',
    }
    result = translate.get(eng_number.lower())
    if result != None:
        if eng_number.istitle():
            return result.title()
        else:
            return result
    return None


number = input('Введите название цифры от 0 до 10 на английском, '
               'учитывая регистр первой буквы\n'
               '>>> '
              )
print(num_translate_adv(number))

# Содержимое блока функции не засоряет память и уничтожается
# с завершением работы функции (лекция).
# Поэтому данные (в виде словаря) вносим внутрь функции.
# Но программа будет так же работать если словарь вынести в global.
