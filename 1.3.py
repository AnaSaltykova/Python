"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

number = input('n=')

first_number = number + number
second_number = first_number + number

result = int(number) + int(first_number) + int(second_number)
print('Сумма = ', result)


