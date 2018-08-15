# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

def attack(att_ent, def_ent): 
    def_ent['health'] -= att_ent['damage']
    print("{} was hit by {}, leaving {} with {} health".format(def_ent['name'], att_ent['name'], def_ent['name'], def_ent['health']))
    
player = {'name': input('Введите имя персонажа: '), 'health': 215, 'damage': 50}
enemy = {'name': input('Введите имя противника: '), 'health': 250, 'damage': 70}

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
 
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def reduct(dmg, armor):
    return dmg / armor

def attack(att_ent, def_ent): 
    def_ent['health'] -= reduct(att_ent['damage'],def_ent['armor'])
    #def_ent['health'] -= (lambda dmg, armor: dmg / armor)(att_ent['damage'],def_ent['armor']) Через lambda
    


def battle(player, enemy):           # передаются именно name сущностей, иначе не получится обратиться к файлу
    entities = {player: 0, enemy: 0} # словарь сущностей, кривее некуда, но можно работать, зная лишь name сущностей, а не название их словарей
    for entity in player, enemy:     # И при необходимости функция получает любое количество сущностей и обрабатывает их
        entity_dict = []             # player и enemy можно заменить на entity1 и entity2 и биться смогут любые сущности, причем entity1 ударит первой
        with open('{}.txt'.format(entity)) as file:
            for line in file:
                line = line[:-1]     #убрал \n
                line = line.split('-') 
                if line[0] != 'name': 
                    line[1] = float(line[1])
                entity_dict.append(line)
        entities[entity] = dict(entity_dict)
                
    while entities[player]['health'] > 0 and entities[enemy]['health'] > 0: #игровая сессия
        attack(entities[player], entities[enemy])
        if entities[enemy]['health'] <= 0:
            return player, entities[player]['health']
        attack(entities[enemy], entities[player])
    return enemy, entities[enemy]['health']

    
player['armor'] = 2
enemy['armor'] = 1.3 
for entity in player, enemy:
    with open('{}.txt'.format(entity['name']), 'w') as file:
        for key, value in entity.items():
            file.write(f'{key}-{value}\n')
            
winner, health = battle(player['name'],enemy['name'])
print('{} wins with {} health!'.format(winner, round(health)))

