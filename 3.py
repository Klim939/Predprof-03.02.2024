f = open('vacancy.csv', 'r', encoding='utf-8')
# открытие файла для чтения

data = []
# инициализация массива

for i in f.read().split('\n')[1:]:
    data.append(i.split(';'))
# считывание данных в массив

s = input('Введите название компании: ')
# Вывод + считывание введенного значения в s

while s != 'None':
    # цикл с условием

    b = True
    for i in data:
        if i[4] == s:
            b = False
            print('В ' + i[4] + ' найдена вакансия: ' + i[3] + '. З/п составит: ' + i[0])
            #вывод после проверки перебранного значения по условию
    if b:
        print('К сожалению, ничего не удалось найти')
        # вывод при неправильном значении

    s = input('Введите название компании: ')
    # Вывод + считывание введенного значения в s

f.close()
# закрытие файла