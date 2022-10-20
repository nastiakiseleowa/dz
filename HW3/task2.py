#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

list=[]
list2=[]
number = 7 #int(input('Введите размер списка '))
for i in range(number):
    list.append(randint(1, 9))

print(list)

for i in range(0,(round(len(list)/2))):
    m = list[i] * list[len(list)-i-1]
    list2.append(m)

print (list2)