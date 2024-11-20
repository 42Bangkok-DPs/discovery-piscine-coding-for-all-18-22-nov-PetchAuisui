#!/usr/bin/env python
import sys
import re
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    string = sys.argv[2]
    if keyword in string:
        count = len(re.findall(keyword, string))
        print(count)
    else:
        print("none")
else:
    print("none")