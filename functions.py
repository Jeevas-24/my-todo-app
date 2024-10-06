FILEPATH = 'todo.txt'
def get_todos(filepath = FILEPATH):  # parameters (default argument)
    """
    Read the text file and return the list of todo items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the todo items in a text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(help(get_todos))
# print(help(write_todos))
# print("I am outside.")
#print(__name__)

if __name__ == '__main__':
    print("Hello")
    print(get_todos())
