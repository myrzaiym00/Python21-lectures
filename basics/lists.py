"===================Lists=================="
# списки - индексируемый, изменяемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list_ = [1,2,3,"hello",[0.1,2],{"a":3}]
list_[1] # 2
list_[4] # [0.1, 2]
list_[4][0] # 0.1
list_[3][0] # 'h'
list_[-1]["a"] # 3


"==================Создание списков==========="
list1 = [1,2,3]
list2 = list('hello') # ['h', 'e', 'l', ''l', 'o']
list3 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
list4 = [1] * 5 # [1,1,1,1,1] (при изменении одного элемента меняются все 5 элементов автоматически)


"==================Методы списков============="
# method append adds new element to the end of the list (only one element)
list_ = []
list_.append(1)
print(list_) # [1]
list_.append("hello")
print(list_) # [1, "hello"]

# clear очищает список
list_.clear()
print(list_) # []

# count считает количество принятых элементов
list_ = [1,2,1,4,1,5,1,7,2]
list_.count(1) # 4
list_.count(2) # 2

# extend добавляет элементы второго списка в первый, изменяя первый
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

# index возвращает индекс первого вхождения принятого элемента
list1 = [1,2,3,4,1,2,3,5,4,1]
list1.index(3) # 2
list1.index(1) # 0

# insert добавляет элемент по индексу list.insert(index, obj)
list_ = [1,2,3]
list_.insert(0, 'hello')
print(list_) # ['hello',1,2,3]
list_.insert(2, 10)
print(list_) # ['hello',1,10,2,3]
list_.insert(100, "bye")
print(list_) # ['hello',1,10,2,3,"bye"]

# pop удаляет из списка по индексу и возвращает удаленный элемент
list_ = [1,2,3,4,5,6,7]
popped = list_.pop()
print(list_, popped) # [1,2,3,4,5,6] 7
popped = list_.pop(1)
print(list_, popped) # [1,3,4,5,6] 2

print([1,2,[3,4,[5,6]]].pop(2).pop(2).pop(1)) # 6

# remove  удаляет первого вхождения принятого элемента
list_ = [1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_) # [1,3,1,2,4,1,2,6]

# reverse изменяет список, раставляя его элементы в обратном порядке
list_ = [1,2,3,4,5]
list_.reverse()
print(list_) # [5,4,3,2,1]
new_list = list_[::-1] # [1,2,3,4,5]

# sort сортирует список, состоящий из элементов одного типа данных в возрастающем порядке (алфавитном для строк)
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] # TypeError: '<' not supported between instances of 'str' and 'int'
list_.sort()

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]

#Tasks

#Task1
numbers = input("Введите цифры через запятую: ").split(', ')
numbers1 = []

for number in numbers:
  numbers1.append(int(number))
  
print(numbers[0], numbers[-1])
numbers1.pop()
numbers1.append("Makers")
print(numbers1)

#Task2
import random
random_numbers = random.sample(range(0,100),k=10)
random_numbers.sort()
print(random_numbers)

#Task3
word_count = int(input("Сколько слов вы хотите ввести? "))
list_str = []
list_int = []
for i in range(word_count):
  word = input("Введите слово: ")
  list_str.append(word)
  list_int.append(len(word))
print(list_str)
print(list_int)

list1 = [1, 2, 3, 'a', 'bc', [-1, 0, 'd'], {5:'e'}]
print(list1[-1])
print(list1[5][-2])