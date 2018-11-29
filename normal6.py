# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import os
import re
def file_str(f):
	file_path = f
	file_name=os.path.basename(file_path)
	with open(file_path, 'r') as file_path:
		return str(file_path.readlines())


strings_last_names=file_str("last_names.txt")
pattern_last_names = '[А-Я]+[а-я]+'
last_names=re.findall(pattern_last_names, strings_last_names)
#print(last_names)

strings_female_names=file_str("female_names.txt")
pattern_female_names = '[А-Я]+[а-я]+'
female_names=re.findall(pattern_female_names, strings_female_names)
#print(female_names)

strings_male_names=file_str("male_names.txt")
pattern_male_names = '[А-Я]+[а-я]+'
male_names=re.findall(pattern_male_names, strings_male_names)
#print(male_names)

class School:
	def __init__(self, classes):
		self.classes=classes
		
		
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# Сами классы наследуем
class Student(People):
	def __init__(self, name, surname, parents, class_room):
        # Явно вызываем конструктор родительского класса
		People.__init__(self, name, surname)
        # Добавляем уникальные атрибуты
		self.parents = parents
		self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
		

    # И уникальные методы
	@property
	def class_room(self):
		return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

	def next_class(self):
		self._class_room['class_num'] += 1


class Teacher(People):
	def __init__(self, name, surname, subject, teach_classes):
		People.__init__(self, name, surname)
		self.subject = subject
		self.teach_classes = list(teach_classes)


Students = [Student("Александр", "Иванов","Иванов А.Ю Иванова И.Г.", "5 А"),Student("Петр", "Сидоров", "Сидоров К.К. Сидорова Е.И", "8 Б"),
Student("Сергей", "Куликов","Куликов А.С. Куликова Е.Г.", "5 А"),Student("Евгения", "Спиридонова","Спиридонов Ф.С. Спиридонова И.М.", "1 А"),
Student("Макар", "Гочергин","Гочергин В.Я. Гочергина Т.А.", "5 А"),Student("Ирина", "Квакина", "Квакин З.У. Квакина Д.И.", "7 А"),
Student("Александр", "Смирнов","Смирнов К.Е. Смирнова Т.В.", "2 Б"),Student("Прохор", "Альшевский", "Альшевский В.Л. Альшевская Н.Р.", "3 Б")]

Teachers= [Teacher("Марь", "Иванна", "Математика", ["5 А","3 Б","7 А", "8 Б"]),Teacher("Пал", "Саныч", "Физкультура", ["5 А","3 Б","7 А","8 Б", "1 А", "2 Б"]),
Teacher("Виолетта", "Сергеевна", "Химия", ["8 Б"]),Teacher("Зося", "Бурлаковна", "Русский язык", ["5 А","3 Б","7 А", "8 Б"]),
Teacher("Тарас", "Гандапас", "Естествознание", ["2 Б","1 А","3 Б"]), Teacher("Клим", "Чугункин", "Математика", ["2 Б","1 А","3 Б"])]

# Находим уникальные классы из "Учеников"
school=[]
for i in Students:
	school.append(i.class_room)
	if school.count(school[-1])>1:
		school.remove(school[-1])


print ("В школе есть следующие классы: ",sorted(school))

klas=input("Введите класс: ")
#klas="8 Б"
print("В", klas, "классе учатся:")
for i in Students:
	if i.class_room==klas:
		print (i.name, i.surname)
 
print("В", klas, "преподают:")
for i in Teachers:
	if klas in i.teach_classes:
		print (i.name, i.surname)

name=input("Введите имя ученика: ")
surname=input("Введите фамилию ученика: ")
for i in Students:
	if i.name==name and i.surname==surname:
		print (name, surname, "имеет родителей", i.parents)
		print ("А также ходит на следующие уроки:")
		for k in Teachers:
			if i.class_room in k.teach_classes:
				print (k.subject)
				




