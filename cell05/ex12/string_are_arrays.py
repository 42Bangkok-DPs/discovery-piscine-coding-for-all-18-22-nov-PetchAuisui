#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
    count = string.count('z')
    if count > 0:
        print('z' * count)
    else:
        print("none")
else:
    print("none")