#Задачу смог выполнить только используя форматирование из второго урока
#Хотелось сразу красиво, без вывода пустых элементов
secs = int(input("Введите время в секундах: "))

days = secs // 86400
hours = (secs - days * 86400) // 3600
minutes = (secs - days * 86400 - hours * 3600) // 60
seconds = secs - days * 86400 - hours * 3600 - minutes * 60
result = (f'{days} дн ' if days else "") + \
         (f'{hours} час ' if hours else "") + \
         (f'{minutes} мин ' if minutes else "") + \
         (f'{seconds} сек ' if seconds else "")

print('duration =',secs)
print(result)
