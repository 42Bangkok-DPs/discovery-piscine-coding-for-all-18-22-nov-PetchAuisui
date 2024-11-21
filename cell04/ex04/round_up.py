#!/usr/bin/env python
number = float(input("Give me a number: "))
if number == int(number):
  rounded_number = int(number)
else:
  rounded_number = int(number) + 1
print(rounded_number)