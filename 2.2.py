# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
# на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
n = int(input('Введите количество элементов в списке: '))

for i in range(n):
    type_el = int(input('Выберите тип данных нового элемента: 1 - int; 2 - float; 3 - str; 4 - bool; '))
    if type_el == 1:
        new_el = int(input('Введите значение: '))
        my_list.append(new_el)
    elif type_el == 2:
        new_el = float(input('Введите значение: '))
        my_list.append(new_el)
    elif type_el == 3:
        new_el = (input('Введите значение: '))
        my_list.append(new_el)
    elif type_el == 4:
        new_el = bool(input('Введите значение: '))
        my_list.append(new_el)
print(my_list)

if n % 2 == 1:
    even_number = n - 2

i = 0
for i in range(even_number):
    if i % 2 == 0:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)

