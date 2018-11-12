# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
	
	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3

	
	def verify(self):
		a=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
		b=((self.x3-self.x1)**2+(self.y3-self.y1)**2)**0.5
		c=((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
		if (a>abs(b-c)) and (a<(b+c)):
			return True
		else:
			return False
			
	def square(self):
		a=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
		b=((self.x3-self.x1)**2+(self.y3-self.y1)**2)**0.5
		c=((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
		p=(a+b+c)/2
		return (p*(p-a)*(p-b)*(p-c))**0.5
	
	def perimetr(self):
		a=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
		b=((self.x3-self.x1)**2+(self.y3-self.y1)**2)**0.5
		c=((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
		return a+b+c
		

	def heights(self):
		a=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
		b=((self.x3-self.x1)**2+(self.y3-self.y1)**2)**0.5
		c=((self.x3-self.x2)**2+(self.y3-self.y2)**2)**0.5
		p=(a+b+c)/2
		ha = round(2*(p*(p-a)*(p-b)*(p-c))**0.5/(a),2)
		hb = round(2*(p*(p-a)*(p-b)*(p-c))**0.5/(b),2)
		hc = round(2*(p*(p-a)*(p-b)*(p-c))**0.5/(c),2)
		return ha, hb, hc

print("Введите через пробел координаты 3-х точек (x1 y1 x2 y2 x3 y3)") 
(x1, y1, x2, y2, x3, y3) = [float(i) for i in input().split()]
a=Triangle(x1, y1, x2, y2, x3, y3) 
if a.verify()==True:
	print("Это треугольник")
	print("Площадь треугольника равна",round(a.square(),2))
	print("Периметр треугольника равен", round(a.perimetr(),2))
	print("Выстоы треугольника равны",a.heights())
else:
	print("Это не треугольник")



