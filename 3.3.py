# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.


def my_func(arg_1, arg_2, arg_3):
    # поиск минимального значения
    if arg_1 < arg_2:
        min_arg = arg_1
    else:
        min_arg = arg_2
    if arg_3 < min_arg:
        min_arg = arg_3
    result = arg_1 + arg_2 + arg_3 - min_arg
    return result


sum_max = my_func(20, 30, 10)
print(sum_max)

