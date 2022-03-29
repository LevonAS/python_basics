#Задаём список состоящий из кубов нечётных чисел от 1 до 1000
init_data = [i**3 for i in range(1, 1001, 2)]

result = 0
#Перевод элементов списка в строку через временную переменную temp
for i in range(len(init_data)):
    temp = str(init_data[i])
    sum_temp  = 0
    #Каждое число из строки представляем как сумму его цифр
    for j in temp:
        sum_temp += int(j)
    #Полученное значение проверям на целое деление на 7
    if sum_temp % 7 == 0:
        #Прошедшее проверку число прибавляется к итоговой переменной
        result += int(temp)
print('Вариант ответа a:', result)

inc_result = 0
for i in range(len(init_data)):
    #Переводя список в строку, увеличиваем каждый элемент списка на 17
    temp = str(init_data[i] + 17)
    sum_temp  = 0
    for j in temp:
        sum_temp += int(j)
    if sum_temp % 7 == 0:
        inc_result += int(temp)

print('Вариант ответа b,c:', inc_result)