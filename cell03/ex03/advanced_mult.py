#!/usr/bin/env python3
i = 0
while i <= 10:
    x = 0
    line = f"Table de {i}: "
    while x <= 10:
        line += str(i * x) + " "
        x += 1
    print(line)
    i += 1