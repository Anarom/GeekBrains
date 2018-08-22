# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def make_copy():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
       with open(dir_name, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('Файл {} не найден'.format(dir_name))
        return
    extension = dir_name[dir_name.find('.'):]
    copy_name = dir_name[:dir_name.find('.')] + '_copy' + extension
    with open(copy_name, 'w', encoding = 'utf-8') as file:
        for line in lines:
            file.write(line)

def remove():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path = os.getcwd()
    dir_path = os.path.join(path, dir_name)
    try:
        os.remove(dir_path)
        print('Успешно удалено')
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        try:
            os.rmdir(dir_path)
            print('Успешно удалено')
        except:
            print('Отказано в доступе')

def set_cwd():
    if dir_name[1:2] == ':' or dir_name[:1] == '/':
        dir_path = dir_name
        os.chdir(dir_path)
    else:
        path = os.getcwd()
        dir_path = os.path.join(path, dir_name)
        os.chdir(dir_path)
    if dir_path == os.getcwd():
        print('Успешный переход')
        os.system('cd {}'.format(dir_path)) ######
    else:
        print('Некорректный путь')
        
def print_cwd():
    print(os.getcwd())
            
do = {"help": print_help, "mkdir": make_dir, "ping": ping, "cp": make_copy,
      "rm": remove,"cd": set_cwd, "ls": print_cwd}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
