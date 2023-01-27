#!/usr/bin/env python3

s = input()
numbers = []
odd = []

while s != "end":
   s = int(s)
   numbers.append(s)
   s = input()

i = 0

while i < len(numbers):
   if numbers[i] % 2 == 0:
      print(numbers[i])
   else:
      odd.append(numbers[i])
   i += 1

i = 0

while i < len(odd):
   print(odd[i])
   i += 1
