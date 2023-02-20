from mainScreen import *
from modelProgram import *


def startApp():
    while True:
        match showMenu():
            case '1':
                addNote(newNote())
                confirmResult()
            case '2':
                required_id = checkNote(askForID())
                if required_id is not False:
                    editNote(required_id, newNote())
                    confirmResult()
                else:
                    error()
            case '3':
                required_id = checkNote(askForID())
                if required_id is not False:
                    showNote(getNote(required_id))
                else:
                    error()
            case '4':
                lst = getByDate(askForDate())
                for el in lst:
                    showNote(el)
            case '5':
                content = readFile(file)
                for el in content:
                    showNote(el)
            case '6':
                required_id = checkNote(askForID())
                if required_id is not False:
                    deleteNote(required_id)
                    confirmResult()
            case '7':
                break
            case _:
                error()

startApp()