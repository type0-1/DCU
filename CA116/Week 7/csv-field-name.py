#!/usr/bin/env python3

import sys

number = sys.argv[1:]
input = sys.stdin.readline()
position = -1
i = 0

while i < len(input):
   if int(number[0]) == 0:
      print(input[0:4].strip())
      i = len(input)
   elif int(number[0]) == 9:
      print(input[len(input) - 6:].strip())
      i = len(input)
   else:
      if input[i] == ",":
         position = position + 1
         if int(number[0]) == position:
            j = i - 1
            while j < i and input[j] != ",":
               j -= 1
            if input[j] == ",":
               print(input[j + 1:i])
   i += 1
