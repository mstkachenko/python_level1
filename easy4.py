#Задача 1
arr = [1, 2, 4, 0]
new_arr=[i**2 for i in arr]
print (new_arr)

#Задача 2
fruit1=['ананас','персик','банан','киви','апельсин']
fruit2=['абрикос','кокос','банан','киви','манго']
fruit3=[i for i in fruit1 if i in fruit1 and i in fruit2]
print (fruit1,fruit2,fruit3,sep='\n')


#Задача 3
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
arr=[random.randint(-10,10) for i in range(10)]
new_arr=[i for i in arr if i%3==0 and i>0 and i%4!=0]
print (arr,new_arr,sep='\n')

			
		
		
		


