"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card:

    def check_number(self, number):
        self.numbers.remove(number)
        for line in range(3):
            for element in range(9):
                if self.lines[line][element] == number:
                    self.lines[line][element] = ' -'

                        
    def generate_numbers(self):
        line = []
        while len(line) < 5:
                number = random.randint(1,90)
                if number not in self.numbers:
                    self.numbers.append(number)
                    line.append(number)
        line.sort()
        return line


    def generate_spaces(self):
        count = 0
        line = [None for _ in range(9)]
        while count < 4:
                space = random.randint(0,8)
                if line[space] == None:
                    line[space] = '  '
                    count += 1
        return line


    def generate_line(self):
        line = self.generate_numbers()
        spaced_line = self.generate_spaces()
        for index in range(9):
                if spaced_line[index] == None:
                    spaced_line[index] = line[0]
                    line.pop(0)
        return spaced_line


    def print_card(self):
        print(f'{self.title}')
        for line in self.lines:
            for element in line:
                element = str(element)
                if len(element) == 2:
                    print(element, end = ' ')
                else:
                    print(' ' + element, end = ' ')
            print()
        print('--------------------------')

        
    def __init__(self, title, name):
        self.name = name
        self.title = title
        self.numbers = []
        self.lines = [None, None, None]
        for index in range(len(self.lines)):
            self.lines[index] = self.generate_line()
        self.numbers.sort()
        
        
class Game:

    
    def get_barrel(self):
        new_barrel = False
        while not new_barrel:
            barrel = random.randint(1,90)
            if barrel in self.barrels:
                new_barrel = True
                self.barrels.remove(barrel)
        return barrel


    def turn(self):
        print('\n')
        barrel = self.get_barrel()
        if barrel == 0:
            return
        print(f'Новый бочонок: {barrel} (осталось {len(self.barrels)})\n')
        self.player.print_card()
        self.computer.print_card()
        if barrel in self.computer.numbers:
            self.computer.check_number(barrel)
        choice = input('\nЗачеркнуть цифру? (y/n) ')
        if choice == 'y':
            if barrel in self.player.numbers:
                self.player.check_number(barrel)
            else:
                self.winner = self.computer
                return
        else:
            if choice != 'n':
                print("\nincorrect input treated as 'n'")
            if barrel in self.player.numbers:
                self.winner = self.computer
                return

        
    def __init__(self):
        self.player = Card('------ Ваша карточка -----', 'player')
        self.computer = Card('-- Карточка компьютера ---', 'computer')
        self.winner = None
        self.barrels = [element for element in range(1,91)]
        while not self.winner:
            if len(self.player.numbers) == 0:
                if len(self.computer.numbers) == 0:
                    print('\n Draw')
                    return
                else:
                    self.winner = self.player
            elif len(self.computer.numbers) == 0:
                self.winner = self.computer
            else:
                self.turn()
        print('\nwinner is', self.winner.name)

        
a = Game()
