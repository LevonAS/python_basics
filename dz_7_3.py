# Создать структуру файлов и папок,при помощи скрипта или «руками»
# в проводнике. Написать скрипт, который собирает все шаблоны в одну
# папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Исходные файлы необходимо оставить.

import os
import shutil


dir_home = 'my_project_7_2'
dir_temp = 'my_project_7_2/templates'

if os.path.exists(dir_temp):
    shutil.rmtree(dir_temp)

for root, dirs, files in os.walk(dir_home):
    print(dirs)
    if 'templates' in dirs:
        j = dirs.index('templates')
        shutil.copytree(
            os.path.join(root, dirs[j]),
            dir_temp,
            dirs_exist_ok=True
        )
