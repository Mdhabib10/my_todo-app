filePath = 'todos.tx'
def get_todos(filePath):
    with open(filePath, 'r') as file:
        todos_list = file.readlines()
    return todos_list

def write_todos(filePath, todo_write):
    with open(filePath, 'w') as file:
        file.writelines(todo_write)