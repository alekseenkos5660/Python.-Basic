# Циклы
# - while
# - for
# print("test")
# # v1
# i = 0
#
# while i < 10:
#     # i += 2  # i = i + 1
#     print(i, end=" ")
#     i += 1  # i = i + 1
# #
# #
# print("test")
#
# v2
# i = 12
#
# while True:
#     print(i)
#     i += 2

# v3
# i = 0
#
# while True:
#     i += 1
#
#     if i == 5:
#         print("continue...")
#         continue  # пропустит дальнейшие действия цикла, но цикл не остановится
#
#     if i >= 10:
#         print("break...")
#         break  # цикл остановится (полное завершение цикла)
#
#     print(i)
#
#
# print("hello")


###
# юзер вводит с клавиатуры числа
# если юзер ввел 0 -> прекратить ввод чисел
# в конце вывести среднее арифметическое числовой последовательности

sum_num = 0
count = 0

# v1
# try:
#     while True:
#         num = int(input("Enter number: "))
#
#         if num == 0:
#             print("end...")
#             break
#
#         sum_num += num
#         count += 1
#
#     average = sum_num / count
#     print(f"sum num: {sum_num}")
#     print(f"count: {count}")
#     print(f"average: {average}")
# except ValueError as error:
#     print("Enter numbers only")
#     print(error)
# except Exception as e:
#     print(e)


# v2
# try:
#     while True:
#         try:
#             num = int(input("Enter number: "))
#
#             if num == 0 and count == 0:
#                 print("Please enter a number")
#                 continue
#
#             elif num == 0:
#                 print("end...")
#                 break
#
#             sum_num += num
#             count += 1
#         except ValueError as e:
#             print("Enter numbers only")
#
#     average = sum_num / count
#     print(f"sum num: {sum_num}")
#     print(f"count: {count}")
#     print(f"average: {average}")
#
# except Exception as e:
#     print(e)

###

#
# for i in range(5):
#     # print("Hello")
#     print(i, end=" ")
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i, end=" ")
#
# start, end = 1, 10
# for i in range(end, start - 1, -2):
#     # print("Hello")
#     print(i, end=" ")


# for i in range(1, 10, -1):
#     print(i)

# for i in range(5):
#     print(i, end=" ")
#
# print()
#
# for i in 0, 1, 2, 3, 4:
#     print(i, end=" ")
#
# print()
#
# for i in 2, 5, 1, 2, 5, 7, "asdgfsdfb", True, 23.6:
#     print(i, end=" ")

######################
##
# message = "hello world"
# message_1 = 'hello world'
# print(message)
# print(message_1)

######

# text = ("hello"
#         "world")
# print(text)
#
# # raw строка
# text = '''
# qwerrty
#     asdfadsvf
#         asdvsvb
# '''
#
# print(text)
#
# # # v1
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
# # v2
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #
# print("hello, \"world\"\n\tfrom program")

########
# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)

###
# message = "hello world"
# # [] -> индексаторы
# # индекс - это порядковый номер элемента в коллекции (массиве). Note: не все коллекции поддерживают индексы.
# # Индексы считаются с нуля
# print(message[0])
# print(len(message))  # кол-во символов в строке
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

###
# # string - immutable тип данных, строчку изменить нельзя
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])
# result = sentence[::-1]
# print(result)

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенация (сложение строк)
# print(fullname)
#
#
# text = "Hello, world" * 3
# print(text)

# print("---" * 10)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(98))

####
text = "helLo woRlD"
#
# # isalpha(): возвращает True, если строка состоит только из алфавитных символов
#
print(text.isalpha())
#
# # islower(): возвращает True, если строка состоит только из символов в нижнем регистре
#
# print(text.islower())
#
# # isupper(): возвращает True, если все символы строки в верхнем регистре
#
# print(text.isupper())
#
# # isdigit(): возвращает True, если все символы строки - цифры
#
# print(text.isdigit())
#
# # isnumeric(): возвращает True, если строка представляет собой число
#
# print(text.isnumeric())
#
# # startswith(str): возвращает True, если строка начинается с подстроки str
#
# print(text.startswith("helLo"))
#
# # endswith(str): возвращает True, если строка заканчивается на подстроку str
#
# print(text.endswith("D"))
#
# # lower(): переводит строку в нижний регистр
#
# print(text.lower())
#
# # upper(): переводит строку в верхний регистр
#
# print(text.upper())
#
# # title(): начальные символы всех слов в строке переводятся в верхний регистр
#
# print(text.title())
#
# # capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
#
# print(text.capitalize())
#
# fio = input("Enter fio: ").title()
# print(fio)

#
# # lstrip(): удаляет начальные пробелы из строки
# text = "  helLo woRlD  "
# print(text)
# print(text.lstrip())
#
# # rstrip(): удаляет конечные пробелы из строки
# print(text)
# print(text.rstrip())
#
# # strip(): удаляет начальные и конечные пробелы из строки
# print(text)
# print(text.strip())
#
# # ljust(width): если длина строки меньше параметра width, то справа от строки добавляются пробелы,
# # чтобы дополнить значение width, а сама строка выравнивается по левому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): если длина строки меньше параметра width, то слева от строки добавляются пробелы,
# # чтобы дополнить значение width, а сама строка выравнивается по правому краю
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): если длина строки меньше параметра width, то слева и справа от строки равномерно добавляются пробелы,
# # чтобы дополнить значение width, а сама строка выравнивается по центру
# text = "hello world"
# print(text)
# print(text.center(20))

# # find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
# text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
#
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1
#
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1
#
#
#
# # replace(old, new[, num]): заменяет в строке одну подстроку на другую
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)
