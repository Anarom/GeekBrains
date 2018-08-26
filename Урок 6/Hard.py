# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

class Factory:
    
    def get_materials(self):
        print('Получили материалы')
                        
    def tailor(self, name, toy_type):
        print(f'Сшили игрушкку {name} типа - {toy_type}')

    def paint(self, color):
        print(f'Окрасили игрущку в {color}')
        
    def __init__(self, name, color , toy_type):
        self.get_materials()
        self.tailor(name, toy_type)
        self.paint(color)
        toy = Toy(name, color, toy_type)
        print(f'producted {toy}')

do = Factory('слон', 'серый', 'животное')

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
print()
class Toy:
    
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type


class Animal(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, 'животное')


class Character(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, 'персонаж')

        
class Factory:
    
    def get_materials(self):
        print('Получили материалы')
                        
    def tailor(self, name, toy_type):
        print(f'Сшили игрушкку {name} типа - {toy_type}')

    def paint(self, color):
        print(f'Окрасили игрущку в {color}')
        
    def __init__(self, name, color , toy_type):
        self.get_materials()
        self.tailor(name, toy_type)
        self.paint(color)
        if toy_type == 'животное':
            toy = Animal(name, color)
        else:
            toy = Character(name, color)
        print(f'producted {toy}')

do = Factory('медведь', 'белый', 'животное')
print()
do = Factory('Чебурашка', 'коричневый', 'персонаж')
