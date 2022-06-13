"==================Dictionaries=============="
# dict = изменяемый, итерируемый, неиндексируемый, неупорядоченный тип данных, в котором значения хранятся в парах (ключ : значение)

dict_ = {"a":"hello", "b":2, "c":3}
print(dict_["a"]) # hello

# ключами в словаре могут являться все неизменяемые типы данных
# значениями в словаре могут являться любые типы данных
# ключи должны быть уникальными

dict_ = {
    1:"hello",
    "a":4,
    4.5:{"a":5}
    # {"s":5}:44 # TypeError: Unhashable type: 'dict'
}

print(dict_[4.5]) # {"a":5}
print(dict_[4.5]['a']) # 5


"=====================Методы словарей===================="
dict_.clear() # чистит словарь
print(dict_) # {}

dict.fromkeys([1, 2, 3])
print(dict_) #{1:None, 2:None, 3:None}

dict.fromkeys([1, 2, 3], "HELLO")
print(dict_) #{1:"HELLO", 2:"HELLO", 3:"HELLO"}

dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError

dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c", 5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(['a', 'b'])
dict_.values() # dict_values([1, 2])
dict_.items() # dict_items([('a':1), ('b':2)])

# method update adds pairs from second dictionary to first dictionary
dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}

# method pop removes pair by key and returns value
popped = dict1.pop(3) # d
print(dict1) # {1:"a", 2:"b", 4:"e"}
print(popped) #d

# method popitem removes and returns last pair
print(dict1.popitem()) # (4, "e")
print(dict1) # {1:"a", 2:"b"}

