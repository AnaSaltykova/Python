"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции."""

number = int(input('введите целое положительное число: '))

max_symbol = -1
while number > 10:
    result = number % 10
    number = number // 10
    if result > max_symbol:
        max_symbol = result
print('Самая большая цифра в числе: ', max_symbol)
