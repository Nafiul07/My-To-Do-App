import os

FILEPATH = "todos.txt"


def create_file():
    if not os.path.exists((FILEPATH)):
        with open(FILEPATH, 'w') as file:
            pass


def get_todos(filepath=FILEPATH):
    """ read a text file and return an item list """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_write, filepath=FILEPATH):
    """ write the todo items in the text file """
    with open(filepath, "w") as file:
        file.writelines(todos_write)


if __name__ == "__main__": # if want to execute the file here but not in the main file
    print("Hello")