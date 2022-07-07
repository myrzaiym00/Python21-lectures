# import random
# vegetables = ["помидор", "огурец", "капуста", "редка", "перец"]

# while True:
#     attempts = 5
#     word = random.choice(vegetables)
#     word1 = word
#     letters = ""
#     for w in range(len(word)):
#         letters += "*"
#     print(f"Угадайте слово (овощь): {letters}")

#     while True:
#         letter = input("Введите букву: ").lower()
#         if letter in word:
#             for i in word:
#                 if letter == i:
#                     index = word1.index(i)
#                     letters = letters[:index] + letter + letters[index+1:]
#                     word1 = word1[:index] + '!' + word1[index+1:]
#             print("Правильно")
#             print(letters)
#             if letters == word:
#                 print("Вы выиграли!")
#                 print(f"Загаданное слово: {word}")
#                 break
#         else:
#             attempts -= 1
#             print("Такой буквы нет в загаданном слове")
#             print(f"У вас осталось {attempts} попыток")
#             if attempts == 0:
#                 print("Вы проиграли")
#                 break
#     one_more = input("Хотите сыграть ещё раз? (да/нет): ")
#     if one_more.lower() == "нет":
#         break
#     elif one_more.lower() == "да":
#         continue
#     else:
#         print("Такой команды нет")
#         break

# place = input()
# board = [['.'] * 8 for _ in range(8)]
# x, y = ord(place[0]) - 97, 8 - int(place[1]),
# for i in range(8):
#     for j in range(8):
#         if abs(y - i) == abs(x - j):
#             board[i][j] = '*'
# board[y][x] = 'E'
# for line in board:
#     print(*line)

# numbers = input('Введите числа через запятую: ')
# str_numbers = numbers.split(',')
# int_numbers = map(int, str_numbers)
# list_ = list(int_numbers)
# tuple_ = tuple(list_)
# print('Список:', list_)
# print('Кортеж:', tuple_)

# from functools import reduce
# num = input()
# str_nums = list(num)
# int_nums = [int(i) for i in str_nums]
# max_ = max(int_nums)
# min_ = min(int_nums)
# max_index = int_nums.index(max_)
# min_index = int_nums.index(min_)
# int_nums[max_index] = min_
# int_nums[min_index] = max_
# num1 = int(reduce(lambda x, y: str(x)+str(y), int_nums))
# print(num1)

x = ["Яблоко", "Апельсин", "Автомобиль"]
print(max(x, key=len))

