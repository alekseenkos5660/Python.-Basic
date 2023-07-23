# import random
#
# # Задание 1
#
# # В списке целых, заполненном случайными числами вычислить:
#
# # ■ Сумму отрицательных чисел;
# # ■ Сумму четных чисел;
# # ■ Сумму нечетных чисел;
# # ■ Произведение элементов с индексами кратными 3;
# # ■ Произведение элементов между минимальным и максимальным элементом;
# # ■ Сумму элементов, находящихся между первым и последним положительными элементами.
#
# NUM_SIZE = 10
# MIN_RANDOM = -9
# MAX_RANDOM = 9
# numbers = []
# SUM_NEGATIVE = 0
# SUM_EVEN = 0
# SUM_ODD = 0
# PRODUCT_MULTIPLE_THREE = 1
# PRODUCT_MIN_MAX = 1
# SUM_POSITIVE = 0
# NEW_LIST = []
# try:
#     for i in range(NUM_SIZE):
#         numbers.append(random.randint(MIN_RANDOM, MAX_RANDOM))
#     print("Список целых, заполненный случайными числами:", numbers, sep="\n")
#     for negative in numbers:
#         if negative < 0:
#             SUM_NEGATIVE += negative
#     print("Сумма отрицательных чисел списка:", SUM_NEGATIVE, sep="\n")
#     for even in numbers:
#         if even % 2 == 0:
#             SUM_EVEN += even
#     print("Сумма четных чисел списка:", SUM_EVEN, sep="\n")
#     for odd in numbers:
#         if odd % 2 != 0:
#             SUM_ODD += odd
#     print("Сумма нечетных чисел списка:", SUM_ODD, sep="\n")
#     for multiple_three in numbers[3::3]:
#         PRODUCT_MULTIPLE_THREE *= multiple_three
#     print("Элементы списка с индексами, кратными 3:", numbers[3::3], sep="\n")
#     print("Произведение элементов с индексами кратными 3:", PRODUCT_MULTIPLE_THREE, sep="\n")
#     print("Отсортированный список целых:", sorted(numbers), sep="\n")
#     for min_max in numbers:
#         if min(numbers) < min_max < max(numbers):
#             PRODUCT_MIN_MAX *= min_max
#     print("Произведение эл-тов между минимальным и "
#           "максимальным эл-том:", PRODUCT_MIN_MAX, sep="\n")
#     for new_list in numbers:
#         if new_list > 0:
#             NEW_LIST.append(new_list)
#     print("Положительные элементы списка в порядке их генерации:", NEW_LIST, sep="\n")
#     for sum_positive in NEW_LIST[1:len(NEW_LIST) - 1]:
#         SUM_POSITIVE += sum_positive
#     print("Сумма эл-тов между первым и последним "
#           "положительными эл-тами:", SUM_POSITIVE, sep="\n")
# except Exception as error:
#     print(error)
#
# # Задание 2
#
# # Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
#
# # ■ Создать список целых, содержащий только четные числа из первого списка;
# # ■ Создать список целых, содержащий только нечетные числа из первого списка;
# # ■ Создать список целых, содержащий только отрицательные числа из первого списка;
# # ■ Создать список целых, содержащий только положительные числа из первого списка.
#
# NUM_SIZE = 10
# MIN_RANDOM = -9
# MAX_RANDOM = 9
# numbers = []
# NEW_LIST_1 = []
# NEW_LIST_2 = []
# NEW_LIST_3 = []
# NEW_LIST_4 = []
# try:
#     for i in range(NUM_SIZE):
#         numbers.append(random.randint(MIN_RANDOM, MAX_RANDOM))
#     print("Список целых, заполненный случайными числами:", numbers, sep="\n")
#     for new_1 in numbers:
#         if new_1 % 2 == 0:
#             NEW_LIST_1.append(new_1)
#     # Если число оканчивается на ноль, то это признак четности. Соответственно и сам 0 относится к
#     # четным. Ноль делится на два без остатка. Поэтому его относят к четным числам. Но если нам не
#     # нужно включать ноль, то изменим условие на:
#     #     if new_1 % 2 == 0 and new_1 != 0:
#     #         NEW_LIST_1.append(new_1)
#     print("Список целых, содержащий только четные числа из "
#           "первого списка:", NEW_LIST_1, sep="\n")
#     for new_2 in numbers:
#         if new_2 % 2 != 0:
#             NEW_LIST_2.append(new_2)
#     print("Список целых, содержащий только нечетные числа "
#           "из первого списка:", NEW_LIST_2, sep="\n")
#     for new_3 in numbers:
#         if new_3 < 0:
#             NEW_LIST_3.append(new_3)
#     print("Список целых, содержащий только отрицательные числа "
#           "из первого списка:", NEW_LIST_3, sep="\n")
#     for new_4 in numbers:
#         if new_4 > 0:
#             NEW_LIST_4.append(new_4)
#     print("Список целых, содержащий только положительные числа "
#           "из первого списка:", NEW_LIST_4, sep="\n")
# except Exception as error:
#     print(error)
