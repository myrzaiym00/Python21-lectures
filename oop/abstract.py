"========================Абстракция======================="
# Абстракция - принцип ООП, в котором создается абстрактный класс (класс - пустышка), в котором задаются названия аттрибутов и методов, для того, чтобы в дочерних классах переопределить их нужным образом. От абстрактных классов мы не создаем объектов, потому что в них есть только названия и нет логики

from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        pass

    @abstractproperty
    def legs(self):
        pass

# obj = AbstractAnimal()   # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    pass

# obj = Dog()   # TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print("гав-гав")

class Cat(AbstractAnimal):
    legs = 4

    def voice(self):
        print("мяу")

dog = Dog()
dog.voice() # гав-гав

cat = Cat()
cat.legs # 4

