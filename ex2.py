# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.

n = int(input('N = '))
numbersList = []
for i in range(0, n):
    numbersList.append(i+1)
    print(f'{numbersList[i]} ', end = '')
factorialList = []
print()
for i in range(0, len(numbersList)):
    if numbersList[i] == 1:
        factorialList.append(numbersList[i])
    else:
        factorialList.append(factorialList[i-1] * numbersList[i])
    print(f'{factorialList[i]} ', end = '')