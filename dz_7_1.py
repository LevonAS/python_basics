# Написать скрипт, создающий стартер (заготовку) для проекта
# со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?).
# Как лучше хранить конфигурацию этого стартера, чтобы в будущем
# можно было менять имена папок под конкретный проект.
# Можно ли будет при этом расширять конфигурацию и хранить данные
# о вложенных папках и файлах (добавлять детали)?

import os

# Блок для именования папок проекта
dir_head = 'my_project_7_1'
dir_settings = 'settings'
dir_main = 'mainapp'
dir_admin = 'adminapp'
dir_auth = 'authapp'
folders = dir_settings, dir_main, dir_admin, dir_auth
#
for item in folders:
    # При определении dir_path количество переменных задаёт уровень
    # вложенности папок
    dir_path = os.path.join(dir_head, item)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
