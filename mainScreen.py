def showMenu():
    print('''
    1. Добавить заметку
    2. Редактировать заметку
    3. Найти заметку
    4. Показать заметки за дату
    5. Показать все заметки
    6. Удалить заметку
    7. Выход 
    ''')
    return input("Выберите действие: ")


def showNote(data):
    result = 'id:' + data['id'] + ' Название: ' + data['header'] + ' Текст: ' + data['body'] + ' Изменено: ' + data['modified']
    print(result)

def newNote():
    note = input("Введите название: "), input('Введите текст: ')
    return note

def error():
    print("Ошибка. Значение не найдено")

def askForID():
    return input('Введите id заметки: ')

def askForDate():
    return input('Введите дату в формате dd.mm.yyyy: ')

def confirmResult():
    print('Действие выполнено успешно')