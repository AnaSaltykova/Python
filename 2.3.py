# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input('Введите номер месяца '))
while (month < 1) or (month > 12):
    print('Номер месяца введен неверно! Попробуйте еще раз. ')
    month = int(input('Введите номер месяца '))

year_list = ['зима', 'весна', 'лето', 'осень']
if month >= 1 and month <= 3:
    print(year_list[0])
if month >= 4 and month <= 6:
    print(year_list[1])
if month >= 7 and month <= 9:
    print(year_list[2])
if month >= 10 and month <= 12:
    print(year_list[3])


year_dict = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь',
             7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12:'декабрь'}

key = month
if key >= 1 and key <= 3:
    print('зима')
if key >= 4 and key <= 6:
    print('весна')
if key >= 7 and key <= 9:
    print('лето')
if key >= 10 and key <= 12:
    print('осень')
