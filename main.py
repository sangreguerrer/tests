documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# command p


def people_docs(name):
    doc_num = input('Введите номер документа: ')
    for doc in documents:
        holder_name = doc['name']
        if doc_num == doc['number']:
            return holder_name
    doc_not_found = 'Не найдено'
    return doc_not_found

# command s

def direction_finder(spot):
    shelf_num = input('Введите номер документа:')
    for key, value in directories.items():
        if shelf_num in value:
            return key
    not_found = 'Документ не найден'
    return not_found

# command l

def list(info):
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" " {doc["name"]}"')
    return ''

# command a

def add_list(directory,type,number,name):
    if directory in directories:
        new_doc={"type":type,
                 "number":number,
                 "name":name}
        documents.append(new_doc)
        directories[directory].append(number)
    else:
        print('Полка не найдена')

# command pallete
def remove_doc(directory,number,name):
    shelf=directories[directory]
    for holder in documents:
        if number in shelf and name in holder:
            shelf.remove(number)
            documents.remove(holder)
            break

def main(search):
    while True:
        command = input("Введите команду:")
        if command == 'p':
            print(people_docs(documents))
        elif command == 's':
            print(direction_finder(directories))
        elif command == 'l':
            print(list(documents))
        elif command == 'a':
            add_list(documents, directories)
        elif command == 'q':
            print('Выход')
            break


if __name__ == '__main__':
    main(documents)

