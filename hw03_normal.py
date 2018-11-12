# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):

    fibo=[]
    fibo.append(1)
    fibo.append(1)

    k=2
    while k<m+1:
        fibo.append(fibo[k-1]+fibo[k-2])
        k=k+1
    print (fibo[n:m+1])
    return fibo[n:m+1]

fibonacci(5, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print(" ")
def sort_to_max(origin_list):
    b=len(origin_list)
    new_list=[]
    k=0
    while k<b:
        maxi = float('-inf')
        for i in origin_list:
            if i>maxi:
                maxi=i
        new_list.append(maxi)
        origin_list.remove(maxi)
        k+=1
    print (new_list[::-1])


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print(" ")
def my_filter(filter, data):
    return [i for i in data if filter(i)]


print(my_filter(lambda x: x>0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
