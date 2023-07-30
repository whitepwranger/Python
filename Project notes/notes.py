import json

fileR = open('notes.txt', "r")
fileR.close()
try:
    notes = json.load(fileR)
except:
    notes = []
    print('Нет заметок!"')

while True:
    print('1. Добавить заметку 2. Удалить заметку 3. Найти заметку 4. Вывести все заметки')
    b = input()
    if b == '1':
        print('Название заметки:')
        name = input()
        for n in notes:
            if n['name'] == name:
                print('Заметка с таким именем уже существует!')
                continue
        note = {'name': name}
        print('Текст заметки:')
        note['text'] = input()
        notes.append(note)
        f = open('notes.txt', 'w')
        json.dump(notes, f)
        f.close()
    elif b == '2':
        print('Введите имя заметки которую нужно удалить:')
        name = input()
        for n in notes:
            if n['name'] == name:
                notes.remove(n)
                f = open('notes.txt', 'w')
                json.dump(notes, f)
                f.close()
                print('Заметка удалена!')
    elif b == '3':
        print('Название заметки должно содержать:')
        name = input()
        for n in notes:
            if n['name'].find(name) != -1:
                print(n['name'] + '\n' + n['text'] + '\n\n')
    elif b == '4':
        for n in notes:
            print(n['name'] + '\n' + n['text'] + '\n\n')
    else:
        print('Недопустимая команда!')
