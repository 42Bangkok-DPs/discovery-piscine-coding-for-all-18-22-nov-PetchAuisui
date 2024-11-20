#!/usr/bin/env python
print("Enter the first number:")
number_1 = int(input(""))
print("Enter the second number:")
number_2 = int(input(""))
result = number_1 * number_2
print(f"{number_1} x {number_2}")
if result>0 :
    print('This number is positive')
elif result<0 :
    print('This number is negative')
else:
    print('This number is both positive and negative')