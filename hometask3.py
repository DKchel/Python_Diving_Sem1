# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 0
MAX_ATTEMPTS = 10

num = LOWER_LIMIT - 1
target_num = randint(LOWER_LIMIT, UPPER_LIMIT)
while num != target_num and COUNT < MAX_ATTEMPTS:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if num < target_num:
        print(f'Не удача :( Загаданное число больше {num}. ')
        print()
        COUNT += 1
    elif num > target_num:
        print(f'Не удача :( Загаданное число меньше {num}.')
        print()
        COUNT += 1
if num == target_num:
    COUNT += 1
    res = f'Правильно, {num}! Вы угадали число! Количество попыток: {COUNT}.'
else:
    res = f'Вы использовали максимальное количество попыток ({MAX_ATTEMPTS})'
print(res)