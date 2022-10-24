#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randint

def Generate(coef):
    if k == 1:
        return str(coef)+'x'
    if k == 0:
        return str(coef)
    else:
        return str(coef)+'x**'+str(k)

k = randint(2,7)
polynomial_1 = []
polynomial_2 = [] #для задачи 5

coef = [randint(0,100) for x in range(k+1)]
while coef[0] == 0:
    coef[0] = randint(1,100)

for i in coef:
    if i != 0:
            polynomial_1.append(Generate(i))
    k -= 1

for i in coef:
    if i != 0:
            polynomial_2.append(Generate(i))
    k -= 1
    
print(" + ".join(polynomial_1))
print(" + ".join(polynomial_2))

data = open('polynomial_1.txt','w')
data.writelines(" + ".join(polynomial_1) + ' = 0\n')
data = open('polynomial_2.txt','w')
data.writelines(" + ".join(polynomial_2) + ' = 0\n')
data.close()

print(f'{polynomial_1.txt} + {polynomial_2.txt}')
sum_polynomial = polynomial_1 + polynomial_2

with open('sum_polynomial.txt', 'w') as file:
    file.write(f'{polynomial_1} + {polynomial_2}')