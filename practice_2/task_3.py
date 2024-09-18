# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input('Введите Ваш вес в кг: ')
height = input('Введите Ваш рост в м (например, 1.73): ')

print(f"BIM = {float(weight) / float(height) ** 2:.1f} кг/м2")

