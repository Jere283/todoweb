FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """This function open the file we give and return the files in a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """This function save the file we give into the filepath"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
