# # Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
#
# text = "пользователь вводит с клавиатуры строку. посчитайте количество букв, цифр в строке." \
#        " выведите оба количества на экран."
#
# SEPARATOR = ". "
# print(text)
# sentences = text.split(SEPARATOR)
# print(sentences)
#
# for i in range(len(sentences)):
#     sentences[i] = sentences[i].capitalize()
#
# print(sentences)
# text = SEPARATOR.join(sentences)
# print(text)

################################

# import random
#
# matrix = []
#
# for i in range(4):
#     matrix.append([])
#     for j in range(4):
#         matrix[i].append(random.randint(10, 99))
#
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()
#
# print()
#
# for i in range(len(matrix)):
#     print(matrix[i][i], end=" ")
#
# print()
#
# j = len(matrix)
# for i in range(len(matrix)):
#     print(matrix[i][j - 1], end=" ")
#     j -= 1


# stars = 5
# spaces = 0
#
# for i in range(5):
#     for j in range(spaces):
#         print(" ", end="")
#     for j in range(stars):
#         print("*", end="")
#     for j in range(spaces):
#         print(" ", end="")
#     if i < 2:
#         stars -= 2
#         spaces += 1
#     else:
#         stars += 2
#         spaces -= 1
#     print()

################################################################

# кортеж (tuple) - константный (immutable) список
# можно работать как с обычным списком,
# только нельзя ничего менять (функции которые меняют коллекцию - отсутствуют в кортеже)
# crud -> create, read, update, delete (в кортеже можно делать только read)

# info = ("test1", 123)
# print(info)
# print(type(info))
#
# info = "test2",
# print(info)
# print(type(info))
#
# print(info[0])

# info[0] = 123  # TypeError: 'tuple' object does not support item assignment

# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: "))
# print(nums)

# import copy
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)
# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

####
# for num in 1, 3, 4, 5, 6, 7:
#     print(num)

# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

################################################################
# dict -> словарь, коллекция key: value

# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     # 2: "qwerty",  # дублировать ключи нельзя!
# }
# #
# print(users)
# print(type(users))
# print(users[1])  # [1] -> это не индекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])
#

#
# users_list = [
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# ]
#
# users_dict = dict(users_list)
# print(users_dict)
#
# users_list = list(users_dict)
# print(users_list)

##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# print(users["+33333333"])
# users["+33333333"] = "Petya"
# print(users["+33333333"])
#
# users["+4444444"] = "Test"  # если ключа нет - он будет добавлен с значением
# print(users["+4444444"])
#
# print(users)
# #
# for key in users:
#     print(users[key], end=" ")
#
# print()
# #
# for key in users.keys():
#     print(key, end=" ")
# #
# print()
# print(users.keys())
# print(list(users.keys()))
# # #
# for value in users.values():
#     print(value, end=" ")
#
# print()
# print(users.values())
# #
# print()
# for key, value in users.items():
#     print(f"key: {key} value: {value}")
#
# print()
# print(users.items())
##
# print("one", "two", "three", sep=", ", end=" ")
# print("test")

##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# print(users["+33333333"])
# print(users.get("+33333333", "key not exists"))
#
# del users["+55555555"]
# deleted_value = users.pop("+55555555", "key not exists")
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

##
# users_1 = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# #
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)

# users_2 = {
#     "+11111111": "eeeeeee",
#     "+44444": "qqqqqq",
#     "+12341234": "wwwwwww"
# }
# # #
# users_1.update(users_2)
# print(users_1)
# print(users_2)
###
# json
# users = {
#     "Vasya": {
#         "phone": "123123",
#         "email": "qwerty1@gmail.com",
#         "hobbies": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "1345555",
#         "email": "aqwfafdbsdb@gmail.com",
#         "hobby": "uerhukjshbdjbkhdf",
#         "add_data": {
#             1: "test-1",
#             2: "test-2",
#         }
#     }
# }
# #
# print(users["Vasya"]["hobbies"])
# print(users["Petya"]["add_data"][2])
#
# key = input("Enter key: ").strip().lower()
# for curr_key in users.keys():
#     temp_key = curr_key
#     if temp_key.lower() == key:
#         print(users[curr_key])
#         break
# else:
#     print("Nothing found!")
# ##
# if key in users:
#     print(users[key])
# else:
#     print("Nothing found!")

##########
# # Множество (set) представляют еще один вид набора, который хранит только уникальные элементы.
# Дубликаты значений будут удалены.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# user = "Tom"
# if user in users:
#     users.remove(user)  # если нет значения - генерируется исключение
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# users.discard("Tim")  # элемент "Tim" отсутствует, и метод ничего не делает
# print(users)
# # #
# users.clear()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# # copy() копирование работает так же как и в list, dict и тд
#
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)
#
users = {"Tom", "Bob", "Alice"}
users2 = {"Tom", "Sam", "Kate", "Bob"}

# v1
users3 = users.intersection(users2)
# v2
print(users & users2)
print(users3)
#
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users.intersection_update(users2)
print(users)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
#
# # v1
users3 = users.difference(users2)
print(users3)  # {"Tom", "Alice"}
# v2
print(users - users2)
#
users.difference_update(users2)
print(users)
print(users2)
# #
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

# v1
users3 = users.symmetric_difference(users2)
print(users3)

# v2
users4 = users ^ users2

# ##
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))  # True
print(superusers.issubset(users))  # False

#
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issuperset(superusers))  # False
print(superusers.issuperset(users))  # True

#
# # Тип frozen set является видом множеств, которое не может быть изменено (по типу tuple у list)
users = frozenset({"Tom", "Bob", "Alice"})
print(users)
users = set(users)
print(users)
# # можно использовать все функции обычного set, кроме тех которые модифицируют значения

