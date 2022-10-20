#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fib(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def NegFib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
k = int(input('Введите число: '))
for e in range(1, k + 1):
    list.append(Fib(e))
    list.insert(0, NegFib(e))
print(list)