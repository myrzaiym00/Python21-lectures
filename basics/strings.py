# "======================Строки======================="
# # строки - неизменяемый тип данных, который предназначен для хранения текста я(последовательности символов), заключенного в одинарные или двойные кавычки
# # Синтаксис:
# string1 = 'строка c одинарными кавычками'
# string2 =  'строка c двойными кавычками'
# string3 = "Don't" # внутри двойных кавычек все одинарные -  просто символы
# string4 = '"Makers Bootcamp"' # внутри одинарных кавычек все двойные - просто символы

# string5 = '''
# Многострочный текст
# в одинарных кавычках
# Тут можно ставить "любые" 'кавычки'
# """""
# '''
# string6 = """Многострочный текст
# в двойных кавычках
# Тут можно ставить "любые" 'кавычки'
# '''''
# """


# "==================Экранизация строк==================="
# # экранизация спец-символов
# '\n' # перенос на новую строку
# '\t' # табуляция
# '\\' #  \ отображает следующий символ (в нашем случае отображает  \)
# '\r' # возвращение каретки в начало строки
# '\v' # перенос в новую строку со смещением вправо на длину предыдущей строки 

# 'hello\nworld' 
# # hello
# # world

# 'hello\tworld'
# # hello    world

# 'чтобы эранировать нужен символ \\'
# # чтобы эранировать нужен символ \

# 'My website is Latracal \rSolution'
# # Solutionte is Latracal


# "==================Форматирование строк===================="
# title = 'Плов'
# price = 1500
# format1 = f'Название: {title}, Цена: {price}'
# # Название: Плов, Цена: 1500

# format2 = "Название: %s, Цена: %s"
# print(format2 % ("Гуляш", "250"), format2 % ("Самсы", "70"), sep='\n')
# # Название: Гуляш, Цена: 250
# # Название: Самсы, Цена: 70

# format3 = 'Название: {}, Цена: {}'
# print(format3.format('Шакарап', '35'))
# # Название: Шакарап, Цена: 35


# "=====================Методы строк====================="
# # методы типов данных - функции, к которым мы обращаемся через точку
# dir(str) # показывает все методы str (класса)

# 'HELLO'.lower() # 'hello'
# 'hello'.upper() # 'HELLO'
# 'Hello'.swapcase() # 'hELLO'
# 'hello'.title() # "Hello"
# 'hello world'.capitalize() # Hello world

# 'hello'.center(11) # '   hello   '
# 'hello'.center(11, '-') # '---hello---'

# 'hello'.count('l') # 2
# 'hello'.count('ll') # 1

# 'hello world'.startswith('hell') # True
# 'hello world'.endswith('ld') # True

# 'hello world'.find(' ') #5
# 'hello world'.find('o') #4
# 'hello world'.find('wo') #6

# 'hello world'.split() # ['hello', 'world']
# 'hello world'.split('o') # ['hell', ' w', 'rld']

# '$'.join(['hello', 'world']) # 'hello$world'
# ' '.join(['hello', 'world']) # 'hello world'
# ''.join(['hello', 'world']) # 'helloworld'

# # конкатенация - склеивание строк
# 'hello' + 'world' # 'helloworld'
# 'hello' + ' ' + 'world' # 'hello world'


# "======================Индексы======================"
# # индекс - это порядковый номер символа в строке
# 'h e l l o   w o r l d'
# #0 1 2 3 4 5 6 7 8 9 10
# string = "hello world"
# string[0] # 'h'
# string[10] # 'd'
# string[5] # ' '


# # срезы - подстрока строки
# string[0:5] # 'hello'
# string[2:4] # 'll'

# string[:5] # 'hello'
# string[6:] # 'world'

# string[0:11:2] # 'hlowrd'
# string[::3] # 'hlwl'
# string[::-1] # 'dlrow olleh'
# string[::-2] # 'drwolh'

# # Tasks

# # Task1

# password = input('Введите пароль: ')
# if password.isdigit():
#   if len(password) >= 8:
#     print('Ваш пароль сохранен')
#   else:
#     print('Ваш пароль должен содержать не менее 8 символов')
# else:
#   if len(password) >= 8:
#     print('Ваш пароль должен содержать только буквы')
#   else:
#     print('аш пароль должен содержать не менее 8 символов\nВаш пароль должен содержать только буквы')

# # Task 2

# marks = input('Введите свои баллы по математике, английскому языку и литературе через запятую: ')

# list_ = marks.split()
# math = int(list_[0])
# english = int(list_[1])
# lit = int(list_[2])
# gpa = round((math + english + lit) / 3, 1)

# if gpa > 69:
#   print(f'Вы допущены к экзаменам. Ваш средний балл составляет {gpa}')
# else:
#   print(f'У вас недопуск к экзаменам. Ваш средний балл составляет {gpa}')

# Task 3

import random

user = input('Ваш выбор: ')
choices = ['Камень', 'Ножницы', 'Бумага']
comp = random.choice(choices)
print(f'Выбор компьютера: {comp}')

if user == 'Камень':
    if comp == 'Ножницы':
        print('Вы выиграли!')
    elif comp == 'Бумага':
        print('Вы проиграли!')
    else:
        print('Ничья!')
elif user == 'Ножницы':
    if comp == 'Камень':
        print('Вы проиграли!')
    elif comp == 'Бумага':
        print('Вы выиграли!')
    else:
        print('Ничья!')
else:
    if comp == 'Ножницы':
        print('Вы проиграли!')
    elif comp == 'Камень':
        print('Вы выиграли!')
    else:
        print('Ничья!')
        





