# # 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на
# # экран названия дня недели. Например, если 1, то на экране надпись понедельник, 2 — вторник
# # и т.д.
#
# try:
#     week_day = int(input("Enter the number of the day of the week: "))
#     if week_day == 1:
#         print("\tYou have chosen the first day of the week and it is Monday")
#     elif week_day == 2:
#         print("\tYou have chosen the second day of the week and it is Tuesday")
#     elif week_day == 3:
#         print("\tYou have chosen the third day of the week and it is Wednesday")
#     elif week_day == 4:
#         print("\tYou have chosen the fourth day of the week and it is Tuesday")
#     elif week_day == 5:
#         print("\tYou have chosen the fifth day of the week and it is Friday")
#     elif week_day == 6:
#         print("\tYou have chosen the sixth day of the week and it is Saturday")
#     elif week_day == 7:
#         print("\tYou have chosen the seventh day of the week and it is Sunday")
#     else:
#         raise Exception("\tPlease select a number from 1 to 7")
# except ValueError as error:
#     print("\tEnter only integer numbers please!")
# except Exception as error:
#     print(f"\tError:{error}")
#
# # 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их
# # на экран в порядке возрастания
#
# try:
#     num_1 = float(input("Enter first number: "))
#     num_2 = float(input("Enter second number: "))
#     if num_1 == num_2:
#         print("\tThe entered numbers are equal")
#     elif num_1 < num_2:
#         print("\tNumbers listed in ascending order:")
#         print(f"\t{num_1}\n\t{num_2}")
#     elif num_1 > num_2:
#         print("\tNumbers listed in ascending order:")
#         print(f"\t{num_2}\n\t{num_1}")
# except ValueError as error:
#     print(f"\tError: Please enter only int or float numbers")
# except Exception as error:
#     print(f"\tError:{error}")
#
# # 3. Пользователь вводит два числа и матем действие: + - * или /
# # В зависимости от введенного матем действия вывести результат
#
# try:
#     num_1 = float(input("Enter first number: "))
#     num_2 = float(input("Enter second number: "))
#     math_action = input("Enter one of the available mathematical operations: + - * /: ")
#     if math_action == "+":
#         print("\tResult:", num_1+num_2)
#     elif math_action == "-":
#         print("\tResult:", num_1-num_2)
#     elif math_action == "*":
#         print("\tResult:", num_1*num_2)
#     elif math_action == "/":
#         print("\tResult:", num_1/num_2)
#     else:
#         raise Exception("\tPlease choose valid mathematical operations.")
# except ValueError as error:
#     print("\tError: Please enter correct information.")
# except ZeroDivisionError as error:
#     print("\tError: You can't divide by zero.")
# except Exception as error:
#     print(f"\tError:{error}")
