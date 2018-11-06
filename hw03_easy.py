__author__ = 'Ткаченко Михаил Сергеевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
	number=str(number)
	a=int(number[number.index(".")+1:number.index(".")+1+ndigits]) #оставшаяся дробная часть
	celaya = int (number[:number.index(".")])
	poryadok = int(10**len(number[number.index(".")+1:number.index(".")+1+ndigits]))
	drobnaya = a/(10**len(number[number.index(".")+1:number.index(".")+1+ndigits]))
	if ndigits>=len(number[number.index(".")+1:]):
		print (number)
	elif len(number[number.index(".")+1:])-ndigits==1:
		if float(number[-1:])>=5:
			print ((int((celaya + drobnaya)*poryadok)+1)/poryadok)
		elif float(number[-1:])<5:
			print(int((celaya + drobnaya) * poryadok)/poryadok)
	else:
		if int(number[number.index(".")+2+ndigits])>=5:
			b=(celaya + drobnaya)*poryadok+1
			if (int(b)/poryadok)-(int((b)/poryadok))==0:
				c=int(((celaya + drobnaya)*poryadok)+1)
				print (int(c/poryadok))
			elif (int(b)/poryadok)-(int((b)/poryadok))!=0:
				print ((int((celaya + drobnaya)*poryadok)+1)/poryadok)
		elif number[number.index(".")+2+ndigits]<=5:
			print(int((celaya + drobnaya) * poryadok)/poryadok)
	return (" ")


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number=str(ticket_number)
    if len (ticket_number)==6:
        a=int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])
        b=int(ticket_number[3])+int(ticket_number[4]) + int(ticket_number[5])
        if a == b:
            return "Бинго!"
    return "Не бинго"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))