# print("Hello World")

# 1

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# print(num1 + num2 + num3)
# print(num1 * num2 * num3)

# 2
# S = (AC · BD) / 2.

# first_d = int(input("Enter first diagonal: "))
# second_d = int(input("Enter second diagonal: "))
# area = (first_d * second_d) / 2
# print(area)

# 3
# number = int(input("Enter 4-digit number: "))
# print(number)
# # 4321
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number % 100 // 10
# n4 = number % 10
#
# print(n1)
# print(n2)
# print(n3)
# print(n4)

################################################################
# Ctrl + C - copy

# условные конструкции и операторы сравнения

# > -> строго больше
# < -> строго меньше
# >= -> больше либо равно
# <= -> меньше либо равно
# == -> вернет True если оба операнда одинаковые (равны), иначе False
# != -> вернет True если оба операнда разные, иначе False
# not -> унарное отрицание, если значение равно True -> ключевое слово not сделает False и наоборот

# операторы бывают: унарные и бинарные
# унарный - у него один операнд
# бинарный - у него два операнда

# and -> логическое и, вернет True если оба операнда равны True, иначе вернет False
# or -> логическое или, вернет True если хотя бы один операнд равен True, иначе вернет False

# hours = int(input("Enter hours: "))
#
# if 12 <= hours < 24:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours")

##
# film_rating = int(input("Enter film rating: "))
#
# if film_rating == 5 or film_rating == 4:
#     print("Good")
# else:
#     print("Bad")

##########
# Обработка исключений

# v1
# n1, n2 = 10, 0  # множественное присваивание
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))
#
# print("hello")

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовый тип исключения пишем самым последним из except
#     print(f"Exception occurred: {error}")
# finally:  # Отрабатывает всегда. Писать по надобности
#     print("End of calculation")
#
# print("some text")

# В Python есть следующие базовые типы исключений:
#
# BaseException: базовый тип для всех встроенных исключений
#
# Exception: базовый тип, который обычно применяется для создания своих типов исключений
#
# ArithmeticError: базовый тип для исключений, связанных с арифметическими операциями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: тип исключения, которое возникает при невозможности выполнить операцию с буффером
#
# LookupError: базовый тип для исключений, которое возникают при обращении в коллекциях
# по некорректному ключу или индексу (например, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона
#
# KeyError: возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.
#
# OverflowError: возникает, если результат арифметической операции не может быть представлен текущим
# числовым типом (обычно типом float).
#
# RecursionError: возникает, если превышена допустимая глубина рекурсии.
#
# TypeError: возникает, если операция или функция применяется к значению недопустимого типа.
#
# ValueError: возникает, если операция или функция получают объект корректного типа с некорректным значением.
#
# ZeroDivisionError: возникает при делении на ноль.
#
# NotImplementedError: тип исключения для указания, что какие-то методы класса не реализованы
#
# ModuleNotFoundError: возникает при при невозможности найти модуль при его импорте директивой import
#
# OSError: тип исключений, которые генерируются при возникновении ошибок системы (например, невозможно найти файл,
# память диска заполнена и т.д.)

#########
# if 1:
#     raise Exception("Invalid")

###
try:
    name = input("Enter you name: ")

    if name == "vasya":
        raise Exception("Вася, пока!")

    if 1 < len(name) <= 20:
        print(f"Hello, {name}")
    else:
        raise Exception("Please enter a valid name!")  # raise -> сгенерировать исключение (бросить исключение)

    num = 0
    if num == 0:
        raise ZeroDivisionError("Не дели на ноль!")
except ZeroDivisionError as err:
    print("ashdfvbsdfvblsdvfbldsfv")
except Exception as e:
    print(f"Error: {e}")

print("asdfasdf")
