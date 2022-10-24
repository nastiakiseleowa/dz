#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.20

import random

list=[]
number = 7
for i in range(number):
    list.append(round(random.uniform(0, 10),2))

list2 = [round(i%1,2) for i in list if i%1 != 0]

print(list)
print (max(list2),min(list2), round(max(list2)-min(list2),2))