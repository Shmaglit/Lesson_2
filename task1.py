# 1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку
# вида «Василий, 21 год(а), проживает в городе Москва»


def string(name_var, age_var, city_var):
    print(f'{name_var}, {age_var} год(а), проживает в городе {city_var}')
    return


name = input('Имя:')
age = input('Возраст:')
city = input('Город проживания:')
string(name, age, city)

