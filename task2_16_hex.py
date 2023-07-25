# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

import os
os.system('cls')

def encoder_func(num: int, n: int):
    data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    result_number = ''
    while num != 0:
        res = int(num % n)
        result_number = str(data[res]) + result_number
        num //= n
    return result_number

num: int = int(input("Введите число: "))
OSNOVA = 16
SREZ = 2
SYSTEM = hex
print(encoder_func(num, OSNOVA))
print(SYSTEM(num)[SREZ:])
