#!/usr/bin/env python
import sys
import re

if len(sys.argv) > 1:
  for arg in sys.argv[1:]:
    if not re.search(r"ism$", arg):
      print(arg + "ism")
else:
  print("none")