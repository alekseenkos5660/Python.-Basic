# # Задание 1.
# # Написать рекурсивную функцию нахождения степени числа.
#
#
# def power(num, n_pow):
#     if n_pow == 1:
#         return num
#     return num * power(num, n_pow - 1)
#
#
# print(power(int(input("Enter base of degree: ")), int(input("Enter exponent: "))))
#
# # Задание 2.
# # Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# # Проиллюстрируйте работу функции примером. (протестировать)
#
#
# def star(num_star):
#     if num_star == 1:
#         return "*"
#     return "*" + star(num_star - 1)
#
#
# print(star(int(input("Enter num of stars: "))))
#
# # star(5) -> "*" + star(4) => *****
# # star(4) -> "*" + star(3) => ****
# # star(3) -> "*" + star(2) => ***
# # star(2) -> "*" + star(1) => **
# # star(1) -> "*"           => *
#
# # Задание 3.
# # Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# # Пользователь вводит a и b. Проиллюстрируйте работу функции примером.
#
#
# def sum_of(num_a, num_b):
#     if num_a == num_b:
#         return num_a
#     return num_a + sum_of(num_a + 1, num_b)
#
#
# print(sum_of(int(input("Enter first number: ")), int(input("Enter second number: "))))
#
# # sum_of(2, 6) -> 2 + sum_of(3, 6) => 20
# # sum_of(3, 6) -> 3 + sum_of(4, 6) => 18
# # sum_of(4, 6) -> 4 + sum_of(5, 6) => 15
# # sum_of(5, 6) -> 5 + sum_of(6, 6) => 11
# # sum_of(6, 6) -> 6                => 6
#
# # дополнительно: расписать вызовы: fib(2) и fib(3)
#
#
# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number - 2) + fib(number - 1)
#
#
# print(fib(3))
#
# # fib(3) -> fib(1) => 1 + fib(3) -> fib(2) => nothing ==> 2
# # fib(0)           => 0 + fib(2) -> fib(1) => 1       ==> 1
#
# print(fib(2))
#
# # fib(2) -> fib(0) => 0 + fib(2) -> fib(1) => 1 ==> 1
