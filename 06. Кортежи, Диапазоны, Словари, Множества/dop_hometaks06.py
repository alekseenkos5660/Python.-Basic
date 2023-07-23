# # 1. Дан список чисел. Уберите дубликаты значений. Вывести уникальные значения.
#
# list_1 = [5, 7, 8, 2, 5]
# list_2 = [1, 5, 2, 4, 3]
# unique = []
# duplicate = []
# duplicate_set = []
#
# # Выведем уникальные значения:
#
# for i in list_1:
#     if list_1.count(i) == 1:
#         unique.append(i)
# print("Unique List Values:\n", unique, sep="")
#
# # Уберем дубликаты значений.
#
# # v.1
#
# for i in list_1:
#     if i in duplicate:
#         continue
#     else:
#         duplicate.append(i)
# print("Duplicate values:\n", duplicate, sep="")
#
# # v2.
#
# for i in set(list_1):
#     if i in set(list_1):
#         duplicate_set.append(i)
# print("Duplicate values:\n", duplicate_set, sep="")
#
# # 2. Даны два списка чисел.
# # Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
#
# list_3 = set(list_1).intersection(set(list_2))
# list_3 = list(list_3)
# print("List elements contained in the first and second lists:\n", list_3, sep="")
# print("Quantity of elements contained in both lists:\n", len(list_3), sep="")
#
# # 3. Дан текст: в первой строке записано число строк, далее идут сами строки.
# # Определите, сколько различных слов содержится в этом тексте.
# # Словом считается последовательность непробельных символов идущих подряд,
# # слова разделены одним или большим числом пробелов или символами конца строки.
#
# # Суть самого задания понял только найдя следующий код в интернете:
#
# Count_of_strings = int(input("Enter the number of lines: "))
# List = []
# for i in range(Count_of_strings):
#     for element in input().split():
#         List.append(element)
#
# print("Quantity of different words in the text:\n", len(set(List)), sep="")
#
# # Этот код я понимаю (вводим число строк, как задано в условии, переменную с этим числом передаем в range,
# # т.е указываем сколько раз отработает цикл, текст вводится с клавиатуры в новую строку при каждом страбатывании
# # цикла, вводимый текст сразу делится на элементы, которые передаются в пустой список, в конце выводится длина
# # списка приведенного к множеству, в котором не может быть дубликатов, что соответствует количеству различных
# # слов, содержащихся в тексте.). Но получается что я отталкивался от обратного, т.е. я понял условие задачи,
# # только увидев решение.
#
# # Скажу честно, если бы не первое условие, что в первой строке записано число строк текста, я бы просто решил задачу
# # следуюцим образом:
#
# text = "Дан текст: в первой строке записано число строк, далее идут сами строки. " \
#        "Определите, сколько различных слов содержится в этом тексте. " \
#        "Словом считается последовательность непробельных символов идущих подряд. " \
#        "Cлова разделены одним или большим числом пробелов или символами конца строки."
# text = text.split(" ")
# print("Quantity of different words in the text:\n", len(set(text)), sep="")

# # 4. Дан список стран и городов каждой страны. Для каждого города укажите, в какой стране он находится.

# countr_cit = {
#   "Kiyv":"Ukraine", 
#   "Dnipro":"Ukraine",
#   "Odessa":"Ukraine",
#   "Washington":"USA",
#   "Los Angeles":"USA",
#   "Las Vegas":"USA",
#   "London":"USA" ,
#   "Liverpool":"USA",
#   "Oxford":"USA"
# }
# cities = ["Kiyv", "Kharkiv", "Lviv", "Washington","Boston", "Chicago", "London", "Bristol", "Odessa"]

# for city in cities:
#   if city in countr_cit:
#     print("The city", city, "is in the country", countr_cit[city])
#   else:
#     print("The specified city is not in the dictionary", city)

# # 5. Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# # чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.
#
# list_1 = [1, 2, 3, 4]
# list_2 = ["one", "two", "three", "four"]
# dictionary = {}
# for i in range(len(list_1)):
#     dictionary.update({list_1[i]: list_2[i]})
# print(dictionary)
