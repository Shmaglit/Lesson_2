# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_number():
    number_var = []
    for i in range(3):
        number_var.append(int(input('Введите число:')))
    return max(number_var)


print('Максимальное число:', max_number())

