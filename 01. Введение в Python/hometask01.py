# 1. Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.
#
# Вариант решения №1
#
# number_one = int(input("Enter first num: "))
# number_two = int(input("Enter second num: "))
# number_three = int(input("Enter third num: "))
# print("Sum of entered numbers =", number_one+number_two+number_three)
# print("Product of entered numbers =", number_one*number_two*number_three)
# #
# Вариант решения №2
#
# n_one = int(input("Enter first num: "))
# n_two = int(input("Enter second num: "))
# n_three = int(input("Enter third num: "))
# print("Sum of entered numbers =", n_one+n_two+n_three, "\nProduct of entered numbers =", n_one*n_two*n_three)
#
# Вариант решения №3
#
# num_one = int(input("Enter first num: "))
# num_two = int(input("Enter second num: "))
# num_three = int(input("Enter third num: "))
# sum_entered_numbers = num_one+num_two+num_three
# product_entered_numbers = num_one*num_two*num_three
# print(f"Sum of entered numbers = {sum_entered_numbers} \nProduct of entered numbers = {product_entered_numbers}")
#
# Если необходимо вычислить сумму и произведение десятичных чисел, тип данных int необходимо заменить на float
#
# number_one = float(input("Enter first num: "))
# number_two = float(input("Enter second num: "))
# number_three = float(input("Enter third num: "))
# sum_entered_numbers = number_one+number_two+number_three
# product_entered_numbers = number_one*number_two*number_three
# print(f"Sum of entered numbers = {sum_entered_numbers} \nProduct of entered numbers = {product_entered_numbers}")
#
# 2. Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.
#
# Площадь ромба равна половине произведения его диагоналей: S = (AC · BD) / 2.
# Так как длина диагонали может быть десятичным числом, используем тип данных float
#
# diagonal_ac = float(input("Enter the length of the diagonal AC: "))
# diagonal_bd = float(input("Enter the length of the diagonal BD: "))
# area_of_a_rhombus = (diagonal_ac*diagonal_bd)/2
# print(f"Area of a rhombus = {area_of_a_rhombus}")
#
# # 3. Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
# # Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.
#
# number = int(input ("Enter 4-digit num: "))
# n1 = number // 1000
# n2 = number % 1000 // 100
# n3 = number % 100 // 10
# n4 = number % 10
# print (f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# result = n1*n2*n3*n4
# print (f"Result {result}")
