# 1. Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа
# выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
#
# В решении задачи для определения наибольшего, наименьшего, среднего арифметического трех
# чисел, используется тип данных int, если то же самое необходимо проделать для десятичных чисел,
# тип данных следует изменить на float
#
# num_one = int(input("Enter first number: "))
# num_two = int(input("Enter second number: "))
# num_three = int(input("Enter third number: "))
# choice_one = "Enter 1 to see the largest of the three numbers."
# choice_two = "Enter 2 to see the smallest of three numbers."
# choice_three = "Enter 3 to see the average of three numbers."
# user_choice = int(input(f"\t{choice_one} \n\t{choice_two} \n\t{choice_three} \nMake your choice: "))
# if user_choice == 1:
#     if num_one > num_two and num_one > num_three:
#         print("\tResult:", num_one)
#     elif num_two > num_one and num_two > num_three:
#         print("\tResult:", num_two)
#     elif num_three > num_one and num_three > num_two:
#         print("\tResult:", num_three)
#     else:
#         print("\tResult: Entered numbers are equal")
# elif user_choice == 2:
#     if num_one < num_two and num_one < num_three:
#         print("\tResult:", num_one)
#     elif num_two < num_one and num_two < num_three:
#         print("\tResult:", num_two)
#     elif num_three < num_one and num_three < num_two:
#         print("\tResult:", num_three)
#     else:
#         print("\tResult: Entered numbers are equal")
# elif user_choice == 3:
#     print("\tResult:", (num_one+num_two+num_three)/3)
# else:
#     print("\tResult: Wrong choice. Make a choice from 1 to 3")

# 2. Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит
# метры в мили, дюймы или ярды.
#
# Для того чтобы перевести метры в мили, необходимо значение метров разделить на 1609
# Для того чтобы перевести метры в дюймы, необходимо значение метров умножить на 39.37
# Для того чтобы перевести метры в ярды, необходимо значение метров умножить на 1.094
#
# meters = float(input("Enter distance in meters: "))
# choice_one = "Enter 1 if you want to convert distances to miles."
# choice_two = "Enter 2 if you want to convert distances to inches."
# choice_three = "Enter 3 if you want to convert distances to yards."
# user_choice = int(input(f"\t{choice_one} \n\t{choice_two} \n\t{choice_three} \nMake your choise: "))
# if user_choice == 1:
#     print("\tResult:", meters/1609)
# elif user_choice == 2:
#     print("\tResult:", meters*39.37)
# elif user_choice == 3:
#     print("\tResult:", meters*1.094)
# else:
#     print("\tResult: Wrong choice. Make a choice from 1 to 3")
