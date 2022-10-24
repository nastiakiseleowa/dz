#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def Generate(coef):
    if k == 1:
        return str(coef)+'x'
    if k == 0:
        return str(coef)
    else:
        return str(coef)+'x**'+str(k)

k = randint(2,7)
polynomial = []

coef = [randint(0,100) for x in range(k+1)]
while coef[0] == 0:
    coef[0] = randint(1,100)

for i in coef:
    if i != 0:
            polynomial.append(Generate(i))
    k -= 1
    
print(" + ".join(polynomial))

data = open('log.txt','a')
data.writelines(" + ".join(polynomial) + ' = 0\n')
data.close()

k = randint(2, 5)

