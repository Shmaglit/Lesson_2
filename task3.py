# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#
#     name — строка, полученная от пользователя,
#     health = 100,
#
#     damage = 50.
#     Поэкспериментируйте с значениями урона и жизней по желанию.
#     Теперь надо создать функцию attack(person1, person2).
#
#     Примечание: имена аргументов можете указать свои.
#
#     Функция в качестве аргумента будет принимать атакующего и атакуемого.
#     В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
#     Функция должна сама работать со словарями и изменять их значения.


def attack(person1,person2):
    person1['health'] -= person2['damage']


player = {'name': '', 'health': 180, 'damage': 20}
enemy = {'name': '', 'health': 180,'damage': 40}
player['name'] = input('Введите имя игрока:')
enemy['name'] = input('Введите имя врага:')
print(player, enemy)

while True:
    attack(player,enemy)
    if player['health'] <= 0:
        print('Winner:', enemy['name'])
        break
    attack(enemy, player)
    if enemy['health'] <= 0:
        print('Winner:', player['name'])
        break


print(player, enemy)


