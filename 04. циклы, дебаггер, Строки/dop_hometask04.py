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
#     punctuation = ".,:;!?-()\"" # символ \ не учитывается, использован для отображения "
#     punctuation_count = 0
#     for i in text:
#       if i.isalpha():
#           letters += 1
#       if i.isdigit():
#           numbers += 1
#       if i == "!":
#           exclamation_mark += 1
#       if i in punctuation:
#         punctuation_count += 1
#     text = text.split(sep=". ") # разобьем текст на подстроки по точке с пробелом
#     cap_text = []
#     for i in text:
#       i = i.capitalize() # сделаем каждую подстроку с большой буквы
#       cap_text.append(i) # добавим каждую измененную подстроку в пустой список
#     text = ". ".join(cap_text) # объединим этот список в одну строку
#     # Данный вариант выведения текста с большой буквы сработает только при условии если предложение
#     # заканчивается точкой, после которой следует пробел.
#     print("Num of letters:", letters)
#     print("Num of digits:", numbers)
#     print("Num of exclamation_mark:", exclamation_mark)
#     print("Num of punctuation_count:", punctuation_count)
#     print(text)
# except Exception as error:
#     print("Error:", error)
#
# # Вывести на экран фигуры, заполненные звездочками.
# # Диалог с пользователем реализовать при помощи меню.
#
# STARS_MAX = 15
# STARS_MIN = 1
# SYMB = "*"
# STEP = 2
# try:
#     choose = int(input("Choose num from 1 to 10 to see the different shapes: "))
#     if choose == 1:
#         print("Your choosen shape is: ")
#         i = SYMB
#         while i < SYMB * STARS_MAX:
#             print(i.center(STARS_MAX - 1))
#             i += STEP * SYMB
#     elif choose == 2:
#         print("Your choosen shape is: ")
#         i = SYMB
#         while i < SYMB * STARS_MAX:
#             print(i.rjust(STARS_MAX - 1))
#             i += STEP * SYMB
#     elif choose == 3:
#         print("Your choosen shape is: ")
#         i = SYMB
#         while i < SYMB * STARS_MAX:
#             print(i.ljust(STARS_MAX - 1))
#             i += STEP * SYMB
#     elif choose == 4:
#         print("Your choosen shape is: ")
#         i = STARS_MAX
#         while i > 0:
#             print((i * SYMB).ljust(STARS_MAX))
#             i -= STEP
#     elif choose == 5:
#         print("Your choosen shape is: ")
#         i = STARS_MAX
#         while i > 0:
#             print((i * SYMB).rjust(STARS_MAX))
#             i -= STEP
#     elif choose == 6:
#         print("Your choosen shape is: ")
#         i = STARS_MAX
#         while i > 0:
#             print((i * SYMB).center(STARS_MAX))
#             i -= STEP
#     elif choose == 7:
#         print("Your choosen shape is: ")
#         i = -STARS_MIN
#         while True:
#             i += STEP
#             if i > (STARS_MAX / 2):
#                 break
#             print((i * SYMB).rjust(int(STARS_MAX / 2)))
#         i = int(STARS_MAX / 2)
#         while True:
#             i -= STEP
#             if i < STARS_MIN:
#                 break
#             print((i * SYMB).rjust(int(STARS_MAX / 2)))
#     elif choose == 8:
#         i = -STARS_MIN
#         while True:
#             i += STEP
#             if i > (STARS_MAX / 2):
#                 break
#             print((i * SYMB).ljust(int(STARS_MAX / 2)))
#         i = int(STARS_MAX / 2)
#         while True:
#             i -= STEP
#             if i < STARS_MIN:
#                 break
#             print((i * SYMB).ljust(int(STARS_MAX / 2)))
#     elif choose == 9:
#         print("Your choosen shape is: ")
#         i = int(STARS_MAX / 2) + 2
#         while True:
#             i -= STEP
#             if i < 0:
#                 break
#             print((i * SYMB).center(int(STARS_MAX / 2)))
#         i = STARS_MIN
#         while True:
#             i += STEP
#             if i > int(STARS_MAX / 2):
#                 break
#             print((i * SYMB).center(int(STARS_MAX / 2)))
#     elif choose == 10:
#         print("Your choosen shape is: ")
#         i_1 = 0
#         i_2 = 0
#         while True:
#             i_1 += 1
#             i_2 += 1
#             if i_1 > int(STARS_MAX / 2) and i_2 > int(STARS_MAX / 2):
#                 break
#             print((i_1 * SYMB).ljust(int(STARS_MAX / 2)), (i_2 * SYMB).rjust(int(STARS_MAX / 2)))
#         i_1 = int(STARS_MAX / 2)
#         i_2 = int(STARS_MAX / 2)
#         while True:
#             i_1 -= STARS_MIN
#             i_2 -= STARS_MIN
#             if i_1 < 0 and i_2 < 0:
#                 break
#             print((i_1 * SYMB).ljust(int(STARS_MAX / 2)), (i_2 * SYMB).rjust(int(STARS_MAX / 2)))
#     else:
#         raise Exception("Please select a number from 1 to 10")
# except Exception as e:
#     print(e)
