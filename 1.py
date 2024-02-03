f_ans = open('vacancy_new.csv', 'w', encoding='utf-8')
f = open('vacancy.csv', 'r', encoding='utf-8')
# Открытие файлов f - чтение с кодировкой utf-8, f_ans - запись с кодировкой utf-8

data = []
ans = [['', '', 0]] * 3
# инициализация переменных

for i in f.read().split('\n')[1:]:
    data.append(i.split(';'))
# считывание данных в массив data

data_w = {}
for i in data:
    if i[4] not in data_w:
        data_w[i[4]] = [i[3], i[0]]
    else:
        if int(i[0]) > int(data_w[i[4]][1]):
            data_w[i[4]] = [i[3], i[0]]
# запись нужных данных в массив под запись в следующий файл

s = ''
for i in data_w.keys():
    s += ''.join(i.split()) + ';' + ';'.join(data_w[i]) + '\n'
# сбор данных в строку

f_ans.write(s)
f_ans.close()
# запись и сохранение

for i in data:
    b = True
    for y in range(len(ans)):
        if int(i[0]) > int(ans[y][2]) and b:
            b = False
            ans[y] = [i[4], i[3], i[0]]
# обработка данных

for i in ans:
    print(i[0] + '-' + i[1] + '-' + i[2])
f.close()
# вывод ответа и закрытие файла
