# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# перацией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import os
os.system('cls')

summ = 0
count = 0
MIN_INPUT = 1
MAX_INPUT = 3
MULTIPLICITY = 50       # Кратность пополнения / снятия
POROG_1 = 2000          # Значение суммы снятия, при котором комиссия меняется с фиксированных 30 у.е. 
                        # на 1.5 % от суммы снятия
POROG_2 = 40000         # Значение суммы снятия, при котором комиссия меняется с 1.5 % от суммы снятия 
                        # на фиксированные 600 у.е. 
WEALTH_TAX = 0.1        # ставка налога на богатство
POROG_WEALTH_TAX = 5_000_000    # порог для начисления налога на богатство
print('Ваш баланс 0 у.е.')
while True:    
    if count == 3:
        summ *= 1.03
        print(f'Это третья операция подряд. '\
              f'Ваш баланс пополнен на 3 % и составляет: {round(summ, 2)} у.е.')
        count = 0
    if summ >= POROG_WEALTH_TAX:
        summ -= summ * WEALTH_TAX
        print(f'Сумма на счете превышает 5000000 у.е. '\
              f'Применен налог на богатство. Ваш баланс: {round(summ, 2)} у.е.')
    a = int(input('Введите цифру,соответствующую запрашиваемому действию: '\
                  '1 - пополнить, 2 - снять, 3 - выйти\n'))
    if a < MIN_INPUT or a > MAX_INPUT:
        print(f'Ошибка. Ваш баланс: {round(summ, 2)}. Повторите ввод...')
    elif a == 1:
        add_summ = int(input('Внесите сумму кратную 50 у.е.:'))
        if add_summ % MULTIPLICITY == 0 and add_summ > 0:
            summ += add_summ
            print(f'Ваш баланс: {round(summ, 2)}')
            count += 1
        else:
            print(f'НЕКОРРЕКТНЫЙ ВВОД. Ваш баланс: {round(summ, 2)}. '\
                  'Повторите...')
    elif a == 2:
        print('Процент за снятие — 1.5% от суммы снятия,'\
                ' но не менее 30 и не более 600 у.е.\n' 
                'Введите сумму для снятия кратную 50 у.е.:')
        subtraction_summ = int(input())      
        if subtraction_summ % MULTIPLICITY == 0 and subtraction_summ > 0:
            if subtraction_summ <= POROG_1:
                if summ >= (subtraction_summ + 30):
                    summ -= (subtraction_summ + 30)
                    print(f'Заберите деньги. Ваш баланс: {round(summ, 2)}')
                    count += 1
                else:
                    print(f'НЕДОСТАТОЧНО СРЕДСТВ. Ваш баланс: {round(summ, 2)}')
            elif (POROG_1 < subtraction_summ < POROG_2):
                if (summ >= subtraction_summ * 1.015):
                    summ -= subtraction_summ * 1.015
                    print(f'Заберите деньги. Ваш баланс: {round(summ, 2)}')
                    count += 1
                else:
                    print(f'НЕДОСТАТОЧНО СРЕДСТВ. Ваш баланс: {round(summ, 2)}')
            else:
                if summ >= (subtraction_summ + 600):
                    summ -= (subtraction_summ + 600)
                    print(f'Заберите деньги. Ваш баланс: {round(summ, 2)}')
                    count += 1
                else:
                    print(f'НЕДОСТАТОЧНО СРЕДСТВ. Ваш баланс: {round(summ, 2)}')
        else:
            print(f'НЕКОРРЕКТНЫЙ ВВОД. Ваш баланс: {round(summ, 2)}. Повторите')
    else:
        print(f'Операция завершена. Ваш баланс: {round(summ, 2)}. '\
                'До скорых встреч!')
        break