"=================================OOP=========================="
# OOP - Object Oriented Programming


class Person:
    name = "Myrzaiym"
    age = 22
    arms = 2
    legs = 2

    def walk(arg):
        print(arg)
        print("Я иду")

    def add_age(obj):
        obj.age +=1

person1 = Person()
person1.add_age()
print(person1.age)
person1.walk()