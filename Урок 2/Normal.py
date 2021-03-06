import math
import random
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

num_list = [2, -5, 8, 9, -25, 25, 4, 144, -1024, 256, 1]
new_list1 = []
for element in num_list:
    if element >= 0 and float(math.sqrt(element)).is_integer():
        new_list1.append(int(math.sqrt(element)))
print(new_list1)
print()
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date_list = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое',
             'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое',
             'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое',
             'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое',
             'двадцатое', 'двадцать первое', 'двадцать второе',
             'двадцать третье', 'двадцать четвёртое', 'двадцать пятое',
             'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
             'двадцать девятое', 'тридцатое', 'тридцать первое']

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
              'августа', 'сентября', 'октября', 'ноября', 'декабря']

date_string = input('Введите дату формата dd.mm.yyyy: ').split('.')
print(f'{date_list[int(date_string[0]) - 1]} {month_list[int(date_string[1]) - 1]} {int(date_string[2])} года')
print()
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

rand_list = []
n = int(input('Введите количество элементов: '))
for _ in range(n):
        rand_list.append(random.randint(-100,100))
print(rand_list)
print()
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list1 = [1, 2, 4, 5, 6, 2, 5, 2, 12, 5, 12, 9, 3]
list2 = []
list3 = []
for element in list1:
    if element not in list2:
        list2.append(element)
print(list2)
for index in range(len(list1)):
    if list1[index] not in list1[:index] and list1[index] not in list1[index + 1:]:
        list3.append(list1[index])
print(list3)
