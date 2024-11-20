import sys
if len(sys.argv) > 1:
  print(f"Number of parameters: {len(sys.argv) - 1}")
else:
  print("Number of parameters: 0")