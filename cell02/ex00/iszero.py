#!/usr/bin/env python
try:
  number = int(input("Please enter a number: "))
  if number == 0:
    print("This number is equal to zero.")
  else:
    print("This number is different from zero.")
except ValueError:
  print("Invalid 1  input. Please enter a valid integer.")