#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
   i = 0
   city = s
   while i < len(s) and city[i] != ",":
      i = i + 1
   if i < len(s):
      check = city[i + 1: i + 3]
   if check == "WI":
      total = total + 1
   s = input()

print(total)
