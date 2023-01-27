#!/usr/bin/env python3

s = input()

while s != "end":
   city = s
   i = 0
   while i < len(city) and city[i] != ",":
      i = i + 1
   if i < len(city):
      code = city[i + 1:i + 3]
   if code == "WI":
      print(city[0:i])
   s = input()
