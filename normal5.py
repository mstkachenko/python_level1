import pprint
import os
import sys
import easy5



def print_help():
	print ("1. Перейти в папку")
	print ("2. Просмотреть содержимое текущей папки")
	print ("3. Удалить папку")
	print ("4. Создать папку")
	print() 
print_help()

def open_dir():
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
		print('Успешно открыта директория {}'.format(dir_name))
		print("Cодержимое директории: ",os.listdir(dir_path))
	except FileNotFoundError:
		print('Невозможно открыть директорию {}'.format(dir_name))

def remove_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директория {} не существует'.format(dir_name))

def list_dir():
	print(os.listdir())

do = {
	"1": open_dir,
	"2": list_dir,
	"3": easy5.remove_dir,
	"4": easy5.make_dir
}



try:
	key=input("Выберите пункт меню: ")

	if key=="1" or key=="3" or key=="4":
		dir_name=input("Введите имя директроии: ")
		if key=="1":
			do[key]()
		else:
			do[key](dir_name)
	elif key=="2":
		do[key]()
	else:
		print("Задан неверный ключ")
		print("Укажите ключ 1-4")
except IndexError:
	key = None
	print("Ключ не задан")
	print("Укажите ключ help для получения справки")


