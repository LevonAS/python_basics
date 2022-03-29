#В задаче нет условия вводить число вручную
#поэтому сгенерил последовательность через range
for item in range(1,101):
    if item == 1:
        print(item, 'процент')
    elif 2 <= item <= 4:
        print(item, 'процента')
    else:
        print(item, 'процентов')
