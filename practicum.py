from random import randint 
diapozon = randint(1,100)
print('Угадайте число от 1 до 100')
while True:
    choose_number = (int(input('Введите предполагаемое число:')))
    if choose_number > diapozon:
        print('Ваше число больше того, что загаданно')
    elif choose_number < diapozon:
        print('Ваше число меньше того, что загаданно')
    elif choose_number == diapozon:
        print('Отличная интуиция! Вы угадали число:)')
else:
    print(int(input('Попробуйте снова, введте предполагаемое число:')))