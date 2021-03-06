"================Логические операторы================="
# логические операторы - выражения, которые возвращают True, если правда, False - если ложь

5 == 5 #True
4 == 5 #False


5 != 5 #False
5 != 2 #True

5 > 10 #False
10 > 5 #False

5 < 10 #True
10 < 5 #False

5 <=10 #True
10 <= 5 #False

5 >= 10 #False
10 >=5 #True
5 >= 5 #True

'5' == 5 #False


"=======================And Or Not========================="
# and - и
# or - или
a = 5
b = 6
a == 5 and b == 6 # True (because right side is True, left side is True)
a == 5 and b == 5 # False (right side is True, left side is False)
a == 5 or b == 5 # True (one side is True)
a == 4 or b == 5 # False (both sides are False)

not True #False
not False #True
not a == 4 #True

2 in [1,2,3,4,5] # True
"a" in {"b":3, "c":"a"} # False


"=====================Boolean Type======================"
# Булевый тип данных - имеет всего 2 значения: True, False

bool(1) #True все числа
bool(-277) #True
bool(0) #False

bool('hello') #True
bool(' ') #True
bool('') #False


"=====================None Type========================"
# None - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствия значения
bool(None) # False

# is - это проверка на полное соответствие (проверяет ячейки памяти)
a = None
print(bool(None)) #False
print(a is None) # True


"====================Условные операторы=================="
# условные операторы нужны для того, чтобы при разных входных данных код работал по-разному
# в одной конструкции мы можем использоать неограниченное количество elif
# в одной кончтрукции мы можем использовать только один if
# else мы можем использовать только один раз или не указывать вообще

# if условие1:
#     тело1 

# if условие1:
#     тело1
# else:
#     тело2

# if условие1:
#     тело1
# elif условие2:
#     тело2

# if условие1:
#     тело1
# elif условие2:
#     тело2
# else:
#     тело3


a = int(input('Введите число: '))

if a > 0:
    print(f'Число {a} положительное')
elif a < 0:
    print(f'Число {a} отрицательное')
else:
    print(f'Число {a} - это 0')


"===============FizzBuzz================="
#Введите числа от 1 до 100
#если число кратно 3, вывести Fizz
#если число кратно 5, вывести Buzz
#если число кратно и 5 и 3, вывести FizzBuzz
#если число не кратно не 5 ни 3, вывести число


for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


"==================Тернарные операторы================="
# условие в одну строчку
# bodyIfTrue if condition else bodyIfFalse

res = 'Hello' if a == 5 else 'Bye'
print(res)
# "Hello" if a == 5
# "Bye" if a != 5