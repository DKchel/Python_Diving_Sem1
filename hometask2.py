# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 0
UPPER_LIMIT = 100_000
RULE = 1

num = LOWER_LIMIT - 1
while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
count = 0

for i in range(1, num // 2):
    if num % i == 0:
        count += 1
    
if count == RULE:
    res = f'Число {num} - является простым.'
else:
    res = f'Число {num} - является составным.'    
print(res)