#!/usr/bin/env python
import sys
if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        numbers = list(range(start, end + 1)) 
        print(numbers)
    except ValueError:
        print("none")
else:
    print("none")