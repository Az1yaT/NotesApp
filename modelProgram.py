import datetime
import os
from jsonWriter import *

date_format = '%d.%m.%Y'
file = 'data.json'


def addNote(note):
    current_id = int(get_last_id(file))
    current_id += 1
    new_note = dict(id=str(current_id), header=note[0], body=note[1],
                    modified=datetime.datetime.now().strftime(date_format))

    if os.path.isfile(file):
        content = readFile(file)
        content.append(new_note)
        writeToFile(content, file)
    else:
        createFile(new_note, file)

def editNote(element_id, note):
    content = readFile(file)
    for element in content:
        if element['id'] == element_id:
            element['header'] = note[0]
            element['body'] = note[1]
            element['modified'] = datetime.datetime.now().strftime(date_format)
            break
    writeToFile(content, file)

def checkNote(required_id):
    content = readFile(file)
    for element in content:
        if element['id'] == required_id:
            return required_id
    return False

def getNote(required_id):
    content = readFile(file)
    for element in content:
        if element['id'] == required_id:
            return element
    return False

def getByDate(required_date):
    content = readFile(file)
    result = []
    for element in content:
        if element['modified'] == required_date:
            result.append(element)
    return result

def deleteNote(required_id):
    content = readFile(file)
    index = -1
    for element in content:
        if element['id'] == required_id:
            index = content.index(element)
            break
    if index != -1:
        content.pop(index)
        writeToFile(content, file)