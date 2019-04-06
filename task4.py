#4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2
# (величина брони персонажа)
#    Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#    Следовательно, у вас должно быть 2 функции:
#    1. Наносит урон. Это улучшенная версия функции из задачи 3.
#    2. Вычисляет урон по отношению к броне.
#
#    Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
#    персонажа.


def armor_result(damage, armor):
    print(damage/armor)
    print(round(damage/armor, 1))
    return round(damage/armor, 1)


def attack(person1,person2):
    person1['health'] -= armor_result(person2['damage'], person1['armor'])


player = {'name': '', 'health': 120, 'damage': 60, 'armor': 1.8}
enemy = {'name': '', 'health': 180, 'damage': 40, 'armor': 1.2}
player['name'] = input('Введите имя игрока:')
enemy['name'] = input('Введите имя врага:')
attack(player, enemy)
print(player, '\n', enemy)
attack(enemy, player)
print(player, '\n', enemy)


