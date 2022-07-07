"================== Полиморфизм ===================="
# Полиморфизм - принцип ООП, в котором методы в разных классах называются одинаково
# (один интерфейс - разный функционал)
class Dog:
    def speak(self):
        print("гав гав")
class Cat:
    def speak(self):
        print("мяу мяу")
class Frog:
    def speak(self):
        print("ква ква")
animals = [Cat(), Dog(), Frog(), Frog()]
for animal in animals:
    animal.speak()
print(dir(str))
print(dir(list))
print(dir(dict))