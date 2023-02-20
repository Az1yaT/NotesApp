import json


def readFile(file):
    with open(file, 'r') as f:
        return json.load(f)


def writeToFile(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


def createFile(data, file):
    with open(file, 'w') as f:
        json.dump([data, ], f, indent=4)


def get_last_id(file):
    try:
        content = readFile(file)
        return max(note['id'] for note in content)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

