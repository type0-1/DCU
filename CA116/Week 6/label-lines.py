#!/usr/bin/env python3

s = input()
list = []

while s != "end":
   list.append(s)
   s = input()

i = 0

while i < len(list):
   print(i, len(list), list[i])
   i += 1
