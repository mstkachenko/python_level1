# Так как данный скрипт ипользуется в качестве источника данных для файла normal5.py,
# то вся информация в нем, не относящаяся к непосредственно функциям, закомментирована. 
#
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Успешно создана директория {} '.format(dir_name))
    except FileExistsError:
        print('Невозможно создать директорию {}'.format(dir_name))

def remove_dir(dir_name):
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
		os.rmdir(dir_path)
		print('Успешно удалена директория {}'.format(dir_name))
	except FileNotFoundError:
		print('Невозможно удалить директорию {}'.format(dir_name))

#for i in range(1,10):
	#dir_name="dir_"+str(i) # Генерация имен dir_1 - dir_9
	#make_dir(dir_name)   #Создание папок dir_1 - dir_9 
    #remove_dir(dir_name) #Удаление папок dir_1 - dir_9

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории
def dirs_in_curdir():
    return [i for i in os.listdir() if os.path.isdir(i)]
#print (dirs_in_curdir()) #отображающий папки текущей директории

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
	file_path = os.path.abspath(__file__)
	file_name=os.path.basename(file_path)
	with open(file_path, 'r', encoding='utf-8') as file_path:
		i=file_path.readlines()
	try:
		with open("copy.py", "x", encoding='utf-8') as f:
			for k in i:
				f.write(k)
		print('копия "copy.py" файла {} успешно создана'.format(file_name))

	except FileExistsError:
		print('копия "copy.py" файла {} уже существует'.format(os.path.basename(file_name)))
#
# copy_file() #создание копии файла, из которого запущен данный скрипт