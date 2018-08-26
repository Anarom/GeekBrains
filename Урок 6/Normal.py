import math
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def hit(self, target):
        target.health -= target._reduce(self.damage)

    def _reduce(self, damage):
        return damage / self.armor


class Player(Person):
    def __init__(self):
        super().__init__('player', 100, 13, 1.8)

class Enemy(Person):
    def __init__(self):
        super().__init__('enemy', 150, 15, 1.1)

class Battle():
    def __init__(self, first, second):
        while first.health > 0:
            first.hit(second)
            if second.health > 0:
                second.hit(first)
            else:
                winner = first
                break
        else:
            winner = second
        print(f'{winner.name} wins with {math.ceil(winner.health)} health')
player = Player()
enemy = Enemy()
do = Battle(player, enemy)
