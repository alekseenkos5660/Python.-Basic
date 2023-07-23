# 1
# абстрактные методы

# from abc import ABC, abstractmethod
#
#
# абстрактный класс - содержит в себе абстрактные методы, то есть методы без реализации помеченные
# декоратором @abstractmethod из модуля abc, а так же методы с реализацией (обычные методы)
# Так как абстрактный класс содержит в себе абстрактные методы -
# все дочерние классы обязаны предоставить реализации этих методов,
# так же нельзя создать экземпляр класса у которого есть хотя бы один абстрактный метод

# интерфейс - это класс, у которого только абстрактные методы,
# такой класс необходим если вам нужно создать некий контракт, обязательство предоставить реализацию этих методов для
# других классов наследников
# class Polygon(ABC):
#     @abstractmethod  # этот метод без реализации и все дочерние классы обязаны предоставить реализацию этого метода
#     def noofsides(self):
#         pass
#
#     def show_info(self):
#         print("I am from polygon")
#
#
# class Triangle(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")


# TypeError: Can't instantiate abstract class Polygon with abstract method noofsides
# test = Polygon()
# test.noofsides()

# Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()
# K.show_info()

# 2
# Полиморфизм функций
# print(len("Программист"))
# print(len(["Яблоко", "Банан", "Груша"]))
# print(len({"Имя": "Максим", "Address": "Киев"}))
#
# #Полиморфизм классов
# class Cat:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я кошка. Меня зовут {self.klichka}. Мой возраст {self.vozrast} лет")
#
#     def say(self):
#         print("Мяу")
#
#
# class Dog:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я собака. Меня зовут {self.klichka}. Мой возраст {self.vozrast} лет")
#
#     def say(self):
#         print("Гав")
#
#     def hello(self):
#         print(f"Hello {self.klichka}")
#
#
# class PetDog(Dog):
#     def __init__(self, klichka, vozrast, owner):
#         super().__init__(klichka, vozrast)
#         self.owner = owner
#
#     # переопределение метода
#     def hello(self):
#         super().hello()
#         print(f"Owner: {self.owner}")
#
#
# test = PetDog("test", 1, "Vasya")
# test.hello()
#
# cat_obj = Cat("Муська", 10)
# dog_obj = Dog("Барон", 12)
#
# for pet in (cat_obj, dog_obj):
#     pet.say()
#     pet.status()
#     pet.say()


# # Полиморфизм и наследование
# from math import pi
# from abc import ABC, abstractmethod
#
#
# # интерфейс
# class BaseShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Shape(BaseShape):
#     def __init__(self, name):
#         self.name = name
#
#     # def area(self):
#     #     pass
#
#     def info(self):
#         return "Я двухмерная форма."
#
#     # строковое представление объекта
#     def __str__(self):
#         return "строковое представление объекта Shape"
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Квадрат")
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def info(self):
#         return "Квадраты имеют каждый угол равный 90 градусам."
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Круг")
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#
# class AreaCalculator:
#     def __init__(self, geom_object):
#         self.geom_object = geom_object
#
#     def get_area(self):
#         print(self.geom_object.area())
#
#
# # my_shape = Shape("my_shape")
# # print(my_shape)
# #
# kvadrat = Square(8)
# krug = Circle(14)
# # print(kvadrat)
# # print(kvadrat.info())
# # print(krug.info())
# # print(kvadrat.area())
#
# areaCalculator = AreaCalculator(kvadrat)
# areaCalculator.get_area()
# areaCalculator = AreaCalculator(krug)
# areaCalculator.get_area()
# print(Square.mro())
# print(AreaCalculator.mro())
