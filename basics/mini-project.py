# def func1():
#     side = int(input("Введите сторону квадрата: "))
#     perimetr = 4*side
#     ploshad = side*side
#     diogonal = 2**(1/2)*side
#     return (perimetr, ploshad, diogonal)

# print(func1())

# num = 3154
# list__ = list(str(num))
# list_ = []
# for i in list__:
#     list_.append(int(i))

# max_ = max(list_)
# min_ = min(list_)
# index_max = list_.index(max_)
# index_min = list_.index(min_)
# list1 = list_.copy()
# list1[index_max] = min_
# list1[index_min] = max_
# string = ''
# for j in list1:
#     string += str(j)
# print(int(string))



# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")


# names = [{'visit2':["deli", "india"]},
#          {'visit3': ['vladimir','russia']},
#          {'visit9':['kursk','russia']}
#          ]
# geo_logs = [key for i in names for key, val in i.items() if 'russia' in val]
# geo_logs.sort()
# print(geo_logs)



# list_ = []
# for i in range(10000, 100000):
#     if not i % 2 and int(str(i)[2]) % 2 != 0:
#         if (int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4])) % 4 == 0:
#             list_.append(i)

# print(list_)



# list1 = []
# for i in range(10000, 100000):
#     if not i % 2 and int(str(i)[2]) % 2 != 0:
#         summa = 0
#         for j in str(i):
#             summa += int(j)
#         if summa % 4 == 0:
#             list1.append(i)

# print(list1)
 
# num = 4321

# if str(num)[0] > str(num)[1] and str(num)[1] > str(num)[2] and str(num)[2] > str(num)[3]:
#     print('yes')
# else:
#     print('no')


# a = 0
# b = 2
# c = 5
# a, b, c = a + b, c - b, a + b + c
# print(a, b, c)


# x = int(input("Введите x кг: "))
# a = int(input("Введите a рублей: "))
# y = int(input("Введите y кг: "))
# k = int(input("Введите k рублей: "))

# kilo_1 =  a / x 
# y_kilo = kilo_1 * y
# k_rubley = k / kilo_1

# print(f"{y} кг этих конфет стоит {y_kilo}, на {k} рублей можно купить {k_rubley} кг конфет")