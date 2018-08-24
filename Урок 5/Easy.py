import os
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки

def set_dirX9():
    path = os.getcwd()
    for index in range(1,10):
        dir_path = os.path.join(path, 'dir_{}'.format(index))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Файл уже существует')

def del_dirX9():
    path = os.getcwd()
    for index in range(1,10):
        dir_path = os.path.join(path, 'dir_{}'.format(index))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Файл на найден')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def get_dirs():
    dirs = []
    for file in os.scandir(os.getcwd()):
        if not file.is_file():
            dirs.append(file.name)
    return dirs


        
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def create_copy():
    name = os.path.basename(__file__)
    with open(name, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    extension = name[name.find('.'):]
    copy_name = name[:name.find('.')] + '_copy' + extension
    with open(copy_name, 'w', encoding = 'utf-8') as file:
        for line in lines:
            file.write(line)


# Для Normal

def set_dir(name):
    path = os.getcwd()
    dir_path = os.path.join(path, name)
    try:
        os.mkdir(dir_path)
        print('---------------------')
        print('Успешно создано')
        print('---------------------')
    except (FileExistsError, PermissionError) as error:
        print('---------------------')
        print('Невозможно создать')
        print('---------------------')

def del_dir(name):
    path = os.getcwd()
    dir_path = os.path.join(path, name)
    try:
        os.rmdir(dir_path)
        print('---------------------')
        print('Успешно удалено')
        print('---------------------')
    except (FileNotFoundError, PermissionError) as error:
        print('---------------------')
        print('Невозможно удалить')
        print('---------------------')
            
def get_items():
    itmes = []
    for file in os.scandir(os.getcwd()):
        itmes.append(file.name)
    return itmes

def set_cwd(path):
    try:
        os.chdir(path)
        if path == os.getcwd():
            print('---------------------')
            print('Успешно перешел')
            print('---------------------')
        else:
            raise PermissionError
        
    except (FileNotFoundError, PermissionError) as error:
        print('---------------------')
        print('Невозможно перейти')
        print('---------------------')    
