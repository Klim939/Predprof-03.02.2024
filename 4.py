f = open('vacancy.csv', 'r', encoding='utf-8')
# открытие файла для чтения

f_ans = open('vacancy_procent.csv', 'w', encoding='utf-8')

data = []
# инициализация массива

for i in f.read().split('\n')[1:]:
    data.append(i.split(';'))
# считывание данных в массив

roles = {}
# инициализация коллекции

for i in data:
    if i[1] not in roles:
        roles[i[1]] = [int(i[0])]
    else:
        roles[i[1]].append(int(i[0]))
# сбор данных в коллекцию

for i in roles.keys():
    roles[i] = int(sum(roles[i]) / len(roles[i]) // 1)
# перезапись в среднюю зарплату

s = ''
# инициализация переменной для записи

for i in data:
    s += ';'.join(i + [str(int(int(i[0]) / roles[i[1]] * 100)) + '%']) + '\n'
# сборка данных

f_ans.write(s)
f_ans.close()
f.close()
# запись, сохранение и закрытие файлов
