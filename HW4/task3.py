#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from itertools import count
from random import randint, random

lst = [x for x in range(15)]
lst.append(int(random()*15))
print (lst)

lst_new = []
for i in lst:
    if lst.count (i) == 1:
        lst_new.append(i)
print (lst_new)    
