'''
ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда содержимое рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.


files: victory.py, bill.py, main.py
dirs: modules, packages

'''

import os
import shutil

while True:
    print('выберите пунк меню:')
    print()
    print('1 - создать папку')
    print('2 - удалить файл или папку')
    print('3 - копировать файл или папку')
    print('4 - просмотр рабочей директории и запись содержимого в файл')
    print('5 - посмотреть файлы в директории')
    print('6 - посмотреть подпапки в директории')
    print('7 - сведения об операционной системе')
    print('8 - смена директории')
    print('9 - выход')
    print()

    choice = input('Выберите пункт меню: ')

    # Создание папки.
    print()
    if choice == '1':
        name = input('Введите имя папки: ')
        if os.path.exists(name):
            print('Такая папка уже существует.')
        else:
            os.mkdir(name)
        print()

    # Удаление.
    elif choice == '2':
        print()
        name = input('Введите имя папки: ')
        if os.path.exists(name):
            shutil.rmtree(name, ignore_errors=True)
        else:
            print('Такой папки нет.')
        print()

    # Копирование.
    elif choice == '3':
        print()
        name = input('Введите имя копируемой папки: ')
        rename = input('Введите новое имя папки: ')
        if os.path.exists(name):
            shutil.copytree(name, rename)
        else:
            print('Такой папки нет.')
        print()

    # Просмотр содержимого директории и записать содержимое в файл.
    elif choice == '4' or choice == '10':
        print()
        list_dir = os.listdir()
        for i in list_dir:
            print(i)
        print()
        list_dir_f = open('list_dir', 'w')
        list_dir_f.write(str(list_dir))
        list_dir_f.close()

    # Просмотр файлов директории.
    elif choice == '5':
        print()
        file = os.listdir()
        for f in file:
            if os.path.isfile(f):
                print(f)
        print()

    # Просмотр папок рабочей директории.
    elif choice == '6':
        print()
        list_fold = os.listdir()
        for fold in list_fold:
            if os.path.isdir(fold):
                print(fold)
        print()

    # Сведения об операционной системе.
    elif choice == '7':
        print()
        import platform
        print(platform.uname())
        print()

    # Смена рабочей директории.
    elif choice == '8':
        print()
        print('Папки текущей директории: ')
        print()
        list_fold = os.listdir()
        for fold in list_fold:
            if os.path.isdir(fold):
                print(fold)
        print()
        fold = input('Введите имя директории, куда перейти (для перехода на уровень выше - введите две точки): ')
        print()
        if not os.path.isdir(fold): # почему отработало в этой последовательности - непонятно.
            print('Такой директории нет.')
        elif fold == '..':
            os.chdir('..')
        else:
            os.chdir(fold)
            print()

    # Выход из программы.
    elif choice == '9':
        break