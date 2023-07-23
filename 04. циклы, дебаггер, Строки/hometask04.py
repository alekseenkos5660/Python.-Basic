# # 1. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке.
# # Выведите оба количества на экран. (использовать цикл)
#
# try:
#     text = input("Enter text: ")
#     numbers = 0
#     letters = 0
#     for i in text:
#         if i.isalpha():
#             letters += 1
#         if i.isdigit():
#             numbers += 1
#     print("Num of letters:", letters)
#     print("Num of numbers:", numbers)
# except Exception as error:
#     print(error)
#
# # 2. Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке
# # встречается искомый символ. Полученное число выведите на экран.
#
# try:
#     text = input("Enter text: ")
#     symbol = input ("Enter symbol to search: ")
#     sum_symbols = 0
#     for i in text:
#         if i == symbol:
#             sum_symbols += 1
#     print("Num of searching symbols:", sum_symbols)
# except Exception as e:
#     print(e)
#
# # 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в
# # строке замену одного слова на другое. Полученную строку отобразите на экране.
#
# text = input("Enter text: ")
# text_for_search = input ("Enter word for search: ")
# text_for_replacement = input("Enter word for replacement: ")
# text = text.replace(text_for_search, text_for_replacement)
# print(text)
#
# # 4. Дана строка. (сделать срезы)
# #
# # - Сначала выведите третий символ этой строки.
# # - Во второй строке выведите предпоследний символ этой строки.
# # - В третьей строке выведите первые пять символов этой строки.
# # - В четвертой строке выведите всю строку, кроме последних двух символов.
# # - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# # поэтому символы выводятся начиная с первого).
# # - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# # - В седьмой строке выведите все символы в обратном порядке.
# # - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# # - В девятой строке выведите длину данной строки.
#
# text = input("Enter text: ")
# print("Third character of a string:", "\n\t",  text[2])
# print("Penultimate character of a string:", "\n\t", text[-2])
# print("First five characters of a string:", "\n\t",  text[:5])
# print("The entire string except the last two characters:", "\n\t",  text[:-2])
# print("All characters with even indices:", "\n\t",  text[::2])
# print("All characters with odd indices:", "\n\t",  text[1::2])
# print("All characters in reverse order:", "\n\t",  text[::-1])
# print("All characters of the string in reverse order. Through one:", "\n\t",  text[-1::-2])
# print("Line length:", "\n\t",  len(text))
#
# # Дополнительно:
# #
# # Есть некоторый текст. Реализуйте следующую функциональность:
# # ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# # ■ Посчитайте сколько раз цифры встречаются в тексте;
# # ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# # ■ Посчитайте количество восклицательных знаков в тексте.
#
# try:
#     text = input("Enter text: ")
#     numbers = 0
#     letters = 0
#     exclamation_mark = 0
#     for i in text:
#         if i.isalpha():
#             letters += 1
#         if i.isdigit():
#             numbers += 1
#         if i == "!":
#             exclamation_mark += 1
#         if i.endswith("."):
#             print(text.title())
#         elif i.endswith(".!?..."):
#             print(text.title())
#     print("Num of letters:", letters)
#     print("Num of digits:", numbers)
#     print("Num of exclamation mark:", exclamation_mark)
# except Exception as error:
#     print("Error:", error)

# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

# try:
#     choose = int(input("Choose num from 1 to 10 to see the different shapes: "))
#     if choose == 1:
#         print("Your choosen shape is: ")
#         i = "*"
#         while i < "*" * 15:
#             print(i.center(14))
#             i += "**"
#     elif choose == 2:
#         print("Your choosen shape is: ")
#         i = "*"
#         while i < "*" * 15:
#             print(i.rjust(14))
#             i += "**"
#     elif choose == 3:
#         print("Your choosen shape is: ")
#         i = "*"
#         while i < "*" * 15:
#             print(i.ljust(14))
#             i += "**"
#     elif choose == 4:
#         print("Your choosen shape is: ")
#         i = 15
#         while i > 0:
#             print((i * "*").ljust(15))
#             i -= 2
#     elif choose == 5:
#         print("Your choosen shape is: ")
#         i = 15
#         while i > 0:
#             print((i * "*").rjust(15))
#             i -= 2
#     elif choose == 6:
#         print("Your choosen shape is: ")
#         i = 15
#         while i > 0:
#             print((i * "*").center(15))
#             i -= 2
#     elif choose == 7:
#         print("Your choosen shape is: ")
#         i = -1
#         while True:
#             i += 2
#             if i > 9:
#                 break
#             print((i * "*").rjust(9))
#         i = 9
#         while True:
#             i -= 2
#             if i < 1:
#                 break
#             print((i * "*").rjust(9))
#     elif choose == 8:
#         print("Your choosen shape is: ")
#         i = 2
#         while True:
#             i += 2
#             if i > 9:
#                 break
#             print((i * "*").ljust(9))
#         i = 9
#         while True:
#             i -= 2
#             if i < 1:
#                 break
#             print((i * "*").ljust(9))
#     elif choose == 9:
#         print("Your choosen shape is: ")
#         i = 11
#         while True:
#             i -= 2
#             if i < 0:
#                 break
#             print((i * "*").center(9))
#         i = 1
#         while True:
#             i += 2
#             if i >9:
#                 break
#             print((i * "*").center(9))
#     elif choose == 10:
#         print("Your choosen shape is: ")
#         i_1 = 0
#         i_2 = 0
#         while True:
#             i_1 += 1
#             i_2 += 1
#             if i_1 > 9 and i_2 > 9:
#                 break
#             print((i_1 * "*").ljust(9), (i_2 * "*").rjust(9))
#         i_1 = 9
#         i_2 = 9
#         while True:
#             i_1 -= 1
#             i_2 -= 1
#             if i_1 < 0 and i_2 < 0:
#                 break
#             print((i_1 * "*").ljust(9), (i_2 * "*").rjust(9))
#     else:
#         raise Exception("Please select a number from 1 to 10")
# except Exception as e:
#     print(e)
