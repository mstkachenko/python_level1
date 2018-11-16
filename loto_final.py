# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа, 
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86 
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
# случайная карточка. 
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
# 
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71   
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87      
#       16 49    55 77    88    
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать 
# модуль random: http://docs.python.org/3/library/random.html

import random
def bilet():
	return random.sample(range(1,90),15)
def stroka_s_probelami(m):
	m=sorted(m)
	pos=1
	mesto=sorted(random.sample(range(1,9),5))
	newline=[]
	i=0
	while pos<=9:
		if  pos in mesto:
			newline.append(m[i])
			i+=1
		else:
			newline.append("")
		pos+=1
	return newline

def final_bilet(m):
	for i in range(9):
		if m[i]=="":
			print ("  ",end=" ")
		elif m[i]=="-":
			print(" -", end=" ")
		elif m[i]<10:
			print ("",m[i],end=" ")
		elif m[i]>=10:
			print(m[i], end=" ")
	print("")

me=bilet()
comp=bilet()
me1=stroka_s_probelami(me[:5])
me2=stroka_s_probelami(me[5:10])
me3=stroka_s_probelami(me[10:15])
comp1=stroka_s_probelami(comp[:5])
comp2=stroka_s_probelami(comp[5:10])
comp3=stroka_s_probelami(comp[10:15])
print ("------"+"Ваша карточка"+"-----")
final_bilet(me1)
final_bilet(me2)
final_bilet(me3)
print ("------------------------")
me_new=me1+me2+me3
print ("--"+"Карточка компьютера"+"---")
final_bilet(comp1)
final_bilet(comp2)
final_bilet(comp3)
print ("------------------------")
comp_new=comp1+comp2+comp3

burrel=random.sample(range(1,91),90)
i=0
while i<90:

	print ("Новый бочонок:",burrel[i], "(осталось",str(89-i)+")")
	choose=input("Зачеркнуть цифру(1) или продолжить(2)?")
	print("")
	if burrel[i] in comp_new:
		comp_new[comp_new.index(burrel[i])]="-"
	if choose=="1" and burrel[i] in me_new:
		me_new[me_new.index(burrel[i])]="-"
	elif choose=="1" and burrel[i] not in me_new:
		print("Приехали")
		break
	elif choose=="2" and burrel[i] not in me_new:
		pass
	elif choose=="2" and burrel[i] in me_new:
		print("Приехали")
		break
	print("------" + "Ваша карточка" + "-----")
	me1 = me_new[:9]
	me2 = me_new[9:18]
	me3 = me_new[18:27]
	final_bilet(me1)
	final_bilet(me2)
	final_bilet(me3)
	print("------------------------")
	print("--" + "Карточка компьютера" + "---")
	comp1 = comp_new[:9]
	comp2 = comp_new[9:18]
	comp3 = comp_new[18:27]
	final_bilet(comp1)
	final_bilet(comp2)
	final_bilet(comp3)
	print("------------------------")
	if me_new.count("-")==15:
	 	print("Вы победили!")
	 	break
	elif comp_new.count("-")==15:
		print("Вы проиграли!")
		break
	i+=1
