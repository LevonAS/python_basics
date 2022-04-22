# Написать скрипт, создающий из config.yaml стартер для проекта
# с заданной структурой.
# Структуру файла config.yaml придумайте сами, его можно создать
# в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации,
# библиотеки использовать нельзя.

import os
import yaml


def dict_to_dir(data, path):

    # Начиная с корня, каталог создается каждый раз, когда встречается словарь
    if isinstance(data, dict):
        for k, v in data.items():
            if not os.path.exists(os.path.join(path, k)):
                os.makedirs(os.path.join(path, k))
            dict_to_dir(v, os.path.join(path, str(k)))

    # Каждый список может содержать либо файлы (файл создаётся),
    # либо словари (уходим на рекурсию)
    elif isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                dict_to_dir(i, path)
            else:
                with open(os.path.join(path, i), "a"):
                    os.utime(os.path.join(path, i), None)

    if isinstance(data, dict):
        return list(data.keys())[0]

try:
    with open('dz_7_2_config.yaml', "r") as f:
        f_dict = yaml.safe_load(f)
        dest = dict_to_dir(data=f_dict, path=os.getcwd())
        print("Проект развёрнут в папке {}".format(os.getcwd()))
except Exception as e:
    print(e)

# Скажу честно - алгоритм решения вопроса нашёл на просторах известно чего.
# Данные из yaml получаются только в виде словаря, а развёртывать
# несколько уровней вложенности словаря в некую линейную
# последовательность - тот ещё полёт мысли.
# Работу алгоритма понял, хотя конечно сам-бы такое не написал.
# Впрочем, нас и учат использовать Инет для решений.
