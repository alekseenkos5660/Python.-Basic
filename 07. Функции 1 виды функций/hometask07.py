# import random
#
# # 1. Напишите функцию, вычисляющую произведение элементов списка целых. Список передаётся в качестве параметра.
# # Полученный результат возвращается из функции.
#
# list_nums = []
# NUM = 10
# for i in range(NUM):
#     list_nums.append(random.randint(1, 99))
# print(list_nums)
#
# list_nums_2 = [1, 3, 4, 5, 7, 8, 10, 13, 17, 1]
#
# # v.1
#
#
# def product_list(mylist):
#     product = 1
#     for num in mylist:
#         product *= num
#     print("The product of the elements of a list of integers:")
#     return product
#
#
# print(product_list(list_nums))
#
# # V2
#
#
# def product_list(mylist):
#     product = 1
#     for num in mylist:
#         product *= num
#     print("The product of the elements of a list of integers:\n", product, sep='')
#
#
# product_list(list_nums)
#
#
# # 2. Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
# # Полученный результат возвращается из функции.
#
#
# def min_in_list(mylist):
#     print("Minimum number in a list of integers:")
#     return min(mylist)
#
#
# print(min_in_list(list_nums))
#
# # 3. Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве параметра.
# #  Полученный результат возвращается из функции.
#
#
# def prime_number(mylist):
#     count = 0
#     for num in mylist:
#         divider = 2
#         while num >= divider * divider:
#             if num % divider == 0:
#                 count += 0
#                 break
#             divider += 1
#         else:
#             if i > 1:
#                 count += 1
#     #         print("Prime numbers from a list of integers:\n", num, end=" ", sep='')
#     # print()
#     print("Number of primes in a list of integers:")
#     return count
#
#
# print(prime_number(list_nums))
#
# # 4. Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть количество удаленных
# # элементов.
#
#
# def delete_value(del_val, mylist):
#     count = 0
#     new_list = []
#     for num in mylist:
#         if num == del_val:
#             mylist.remove(num)
#             count += 1
#         elif num != del_val:
#             new_list.append(num)
#     # print("New list with elements already removed:\n", new_list, sep="")
#     print("Number of elements removed from the list:")
#     return count
#
#
# print(delete_value(1, list_nums_2))
#
# # 5. Напишите функцию, которая получает два списка в качестве параметра и возвращает список,
# # содержащий элементы обоих списков.
#
#
# def list_sum(list_1, list_2):
#     list_3 = list_1 + list_2
#     print("List containing elements of two lists:")
#     return list_3
#
#
# print(list_sum(list_nums, list_nums_2))
#
# # 6. Напишите функцию, высчитывающую степень каждого элемента списка целых. Значение для степени передаётся
# # в качестве параметра, список тоже передаётся в качестве параметра. Функция возвращает новый список, содержащий
# # полученные результаты.
#
#
# def exponentiate(exp, mylist):
#     exp_list = []
#     for num in mylist:
#         exp_list.append(num**exp)
#     print("List of exponentiated:")
#     return exp_list
#
#
# print(exponentiate(3, list_nums_2))
