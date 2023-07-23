import random

# Доп задания по матрицам (прислать как обычно мне в лс после выполнения основного дз):
# - создать матрицу 10 на 10, заполнить рандомными значениями от 10 до 99
# - вывести на экран
# - вывести сумму чисел главной диагонали матрицы
# - вывести минимальное и максимальное значения побочной диагонали матрицы
# - ввести с клавиатуры порядковый номер столбца - вывести цифры с этого столбца на экран
# (аналогично сделать со строчкой)
# - ввести с клавиатуры порядковый номер одного столбца и потом другого столбца и поменять их местами в матрица
# (аналогично сделать со строчкой)

matrix = []
NUM = 10
SUM_MAIN = 0

for i in range(NUM):
    matrix.append([])
    for j in range(NUM):
        matrix[i].append(random.randint(10, 99))
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
for i in range(NUM):
    SUM_MAIN += matrix[i][i]
print("Sum of main matrix diagonal:", SUM_MAIN)
min_max_list = []
for i in range(NUM):
    min_max_list.append(matrix[i][NUM - i - 1])
print("Smallest side diagonal number:", min(min_max_list))
print("Largest side diagonal number:", max(min_max_list))
try:
    choose_c = int(input("Enter column from 1 to 10: "))
    if choose_c == choose_c:  # чтобы не перебирать десять условий, возьмем переменную choose_c и приравняем ее 
        #к себе самой, при этом индекс столбца также приравняем к choose_c, только отнимем от него единицу, 
        #так как индексы начинаются с нуля, а не с единицы.
        for i in range(NUM):
            print(matrix[i][choose_c - 1], end=" ")
        print()
except Exception as error:  # если пользователь введет некорректное значение ширины матрицы, то исключение Exception 
    #поймает ошибку и поможет программе адекватно на нее отреагировать.
    print("Please choose num from 1 to 10,", error)
# то же самое проделаем для строк
try:
    choose_l = int(input("Enter line from 1 to 10: "))
    if choose_l == choose_l:
        for i in range(NUM):
            print(matrix[choose_l - 1][i], end=" ")
        print()
except Exception as error:
    print("Please choose num from 1 to 10,", error)
# поменять местами строки поможет метод множественного присваивания, после применения метода, выведем матрицу  
#тем же способом что и в начале.
try:
    copy = matrix.copy()
    cho_1_l = int(input("Enter first line to change: "))
    cho_2_l = int(input("Enter second line to change: "))
    print("Result:")
    copy[cho_1_l - 1], copy[cho_2_l - 1] = copy[cho_2_l - 1], copy[cho_1_l - 1]
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            print(copy[i][j], end=" ")
        print()
except Exception as error:
    print(error)
try:  # так же используем метод множественного присваивания, для смены местами столбцов
    copy_1 = matrix.copy()
    cho_1 = int(input("Enter first column to change: "))
    cho_2 = int(input("Enter second column to change: "))
    print("Result:")
    for i in range(NUM):
        copy_1[i][cho_1 - 1], copy_1[i][cho_2 - 1] = copy_1[i][cho_2 - 1], copy_1[i][cho_1 - 1]
        for j in range(len(copy_1[i])):
            print(copy_1[i][j], end=" ")
        print()
except Exception as error:
    print(error)
