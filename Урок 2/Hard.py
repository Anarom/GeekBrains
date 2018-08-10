# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
equation = equation[4:]
equation = equation.split()
equation[0] = float(equation[0][:-1])
equation[1] += equation[2]
print(equation[0] * x + float(equation[1]))

# вычислите и выведите y

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '1.12.1001'
#date = '-2.10.3001'

correct_date = False
date = input('Введите дату формата dd.mm.yyyy: ').split('.')
if len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4: #check size of inputs
    date[0],date[1],date[2] = float(date[0]),float(date[1]),float(date[2]) 
    if date[0].is_integer() and date[1].is_integer() and date[2].is_integer: #check if inputs are whole
        if 1 <= date[0] <= 32 and 1 <= date[1] <= 12 and date[2] >= 1: #check input limits
            correct_date = True
print('date is', correct_date)

