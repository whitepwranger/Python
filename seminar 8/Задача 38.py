import os
import json

def write_contacts(filename:str,list_contact:list) -> None:
    file = open(filename,'w',encoding='UTF-8')
    json.dump(list_contact,file,ensure_ascii='False')
    file.close()

def read_contacts(filename:str) -> list:
    file = open(filename, 'r', encoding='UTF-8')
    ls = json.load(file)
    file.close()
    return ls

def show_contacts(list_contact:list) -> list:
    for contact in list_contact:
        show_contact(contact)

def show_contact(contact:dict) -> None:
    keycontact = {'firstname': 'Имя:', 'lastname': 'Фамилия:', 'phonenumber': 'Номер телефона:'}
    print('\n'.join(f'{keycontact[k]} {v}' for k, v in dict.items(contact)))
    print('----------------------------')
def input_contact(list_contact:list) -> None:
    contact = dict(
        firstname = input('Имя:'),
        lastname = input('Фамилия:'),
        phonenumber = input('Номер телефона:')
    )
    if len(find_contact(list_contact, phonenumber=contact['phonenumber'])) > 0:
        if input('Такой номер существует, заменить? Введите \"Да\" или любой другой текст.\n').upper() == 'ДА':
            delete_contact(list_contact, contact['phonenumber'])
            list_contact.append(contact)
            print('Контакт изменен!')
    else:
        list_contact.append(contact)
        print('Контакт добавлен!')
def change_contact(contacts,phonenumber:str):
    if len(find_contact(list_contact, phonenumber=phonenumber)) > 0:
        contact = dict(
            firstname=input('Имя:'),
            lastname=input('Фамилия:'),
            phonenumber=phonenumber
        )
        delete_contact(contacts, phonenumber)
        list_contact.append(contact)
    else:
        print('Контакт не найден!')

def find_and_delete_contact():
    print('Введите имя и фамилю:')
    firstname = input('Имя:')
    lastname = input('Фамилия:')

def delete_contact(contacts:list,phonenumber:str) -> None:
    try:
        contacts.remove(check_exist_number(contacts,phonenumber=phonenumber))
    except:
        print('Контакт с таким номером не найден!')

def check_exist_number(contacts:list, phonenumber:str) -> dict:
    for contact in contacts:
        if contact['phonenumber'] == phonenumber:
            return contact

def find_contact(contacts:list,firstname = '',lastname = '',phonenumber = '') -> list:
    found_contact = []
    firstname = firstname.upper()
    lastname = lastname.upper()
    phonenumber = phonenumber.upper()
    for contact in contacts:
        if contact['firstname'].upper().find(firstname) != -1 and contact['lastname'].upper().find(lastname) != -1  and contact['phonenumber'].upper().find(phonenumber) != -1:
            found_contact.append(contact)
    return found_contact

list_contact = read_contacts('contacts.txt')
while True:
    print('1 - Вывести все контакты, 2 - поиск по контактам, 3 - добавить контакт, 4 - удалить контакт, 5 - сохранить и выйти')
    choiсe = input()
    if choiсe == '1':
        show_contacts(list_contact)
    elif choiсe == '2':
        print('Введите данные для поиска:')
        found = find_contact(list_contact,firstname=input('Имя:'), lastname = input('Фамилия:'), phonenumber=input('Номер:'))
        print('Найденные контакты:\n--------------------------------------')
        show_contacts(found)
        print('1 - Удалить, 2 - Изменить, 3 - Вернуться')
        choiсe = input()
        if choiсe == '1':
            delete_contact(list_contact,input('Введите номер:\n'))
        elif choiсe == '2':
            change_contact(list_contact,input('Введите номер:\n'))
    elif choiсe == '3':
        input_contact(list_contact)
    elif choiсe == '4':
        delete_contact(list_contact,input('Введите номер:\n'))
    elif choiсe == '5':
        break
write_contacts('contacts.txt',list_contact)