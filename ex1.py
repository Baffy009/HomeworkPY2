# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

print('Сумма цифр:', sum(int(i) for i in input('Введите число: ') if i.isdigit()))

