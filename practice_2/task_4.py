# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
string_of_number = input('Введите целое четырёхзначное число: ')

digits = list(string_of_number)
number = int(string_of_number)
sum_of_digits = number % 10 + number // 10 % 10 + number // 100 % 10 + number // 1000
print(" + ".join(digits), '=', sum_of_digits)