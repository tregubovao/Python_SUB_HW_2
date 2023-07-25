# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions
import os
os.system('cls')

def addition_func (chisl1: int, znam1: int, chisl2: int, znam2: int):
    chisl_rez = chisl1 * znam2 + chisl2 * znam1
    znam_rez = znam1 * znam2    
    fraction_rez = fraction_simplification (chisl_rez, znam_rez)
    return fraction_rez

def multiplication_func (chisl1: int, znam1: int, chisl2: int, znam2: int):
    chisl_rez = chisl1 * chisl2
    znam_rez = znam1 * znam2
    fraction_rez = fraction_simplification (chisl_rez, znam_rez)
    return fraction_rez

def fraction_simplification (chisl_rez: int, znam_rez: int):

    LIMIT1 = int(chisl_rez / 2) + 1
    LIMIT2 = int(znam_rez / 2) + 1

    deliteli_chisl_rez = []
    for item1 in range(1, LIMIT1):
        if chisl_rez % item1 == 0:
            deliteli_chisl_rez.append(item1)
    deliteli_chisl_rez.append(chisl_rez)

    deliteli_znam_rez = []
    for item2 in range(1, LIMIT2):
        if znam_rez % item2 == 0:        
            deliteli_znam_rez.append(item2)
    deliteli_znam_rez.append(znam_rez)

    nod = 1
    for item1 in deliteli_chisl_rez:
        for item2 in deliteli_znam_rez:
            if item1  == item2:
                nod = item1
    result_chisl = int(chisl_rez / nod)
    result_znam = int(znam_rez / nod)
    result_fraction = str(result_chisl) + '/' + str(result_znam)
    return (result_fraction)

chisl1, znam1 = map(int, input('Введите первую простую дробь в формате “a/b”: ').split('/'))
chisl2, znam2 = map(int, input('Введите вторую простую дробь в формате “a/b”: ').split('/')) 
f1 = fractions.Fraction(chisl1, znam1)
f2 = fractions.Fraction(chisl2, znam2)

print(f'Результат сложения дробей: {addition_func(chisl1, znam1, chisl2, znam2)}')
print(f'Результат сложения дробей: {f1 + f2}')

print(f'Результат умножения дробей: {multiplication_func(chisl1, znam1, chisl2, znam2)}')
print(f'Результат умножения дробей: {f1 * f2}')


