#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
string = lines[1].strip()
n = lines[0].strip().split()
new_n = []
for numbers in n:
   new_n.append(int(numbers))
new_n.sort()
output = ""
for letter in string:
   if letter == "A":
      output += str(new_n[0]) + " "
   elif letter == "B":
      output += str(new_n[1]) + " "
   elif letter == "C":
      output += str(new_n[2]) + " "
print(output.strip())