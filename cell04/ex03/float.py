#!/usr/bin/env python
number = input("Give me a number: ") 
float_number = float(number)
if float_number % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")