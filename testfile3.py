#!/usr/bin/env

def square():
    return number ** 2
square(5)
square(10)
square(12)
square(square(2))
square('2')

def sum_numbers(number1, number2):
    return int(number1) + int(number2)