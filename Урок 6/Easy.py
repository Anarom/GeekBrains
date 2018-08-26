# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    
    speed = 80
    color = 'black'
    name = 'town car'
    is_police = False

    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stopes')

    def turn(self, direction):
        print(f'{self.name} turns to the {direction}')        
 

class SportCar:
    
    speed = 150
    color = 'red'
    name = 'sport car'
    is_police = False

    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stopes')

    def turn(self, direction):
        print(f'{self.name} turns to the {direction}')


class WorkCar:
 
    speed = 50
    color = 'yellow'
    name = 'work car'
    is_police = False

    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stopes')

    def turn(self, direction):
        print(f'{self.name} turns to the {direction}')


class TownCar:
    
    speed = 120
    color = 'blue'
    name = 'police car'
    is_police = True

    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stopes')

    def turn(self, direction):
        print(f'{self.name} turns to the {direction}')

        
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def  __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stopes')

    def turn(self, direction):
        print(f'{self.name} turns to the {direction}')



class TownCar(Car):
    def __init__(self):
        super().__init__(80, 'black', 'town car', False)


class SportCar(Car):
    def __init__(self):
        super().__init__(150, 'red', 'sport car', False)


class WorkCar(Car):
    def __init__(self):
        super().__init__(50, 'yellow', 'work car', False)


class PoliceCar(Car):
    def __init__(self):
        super().__init__(120, 'blue', 'police car', True)
