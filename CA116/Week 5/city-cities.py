#!/usr/bin/env python3

s = input()

while s != "end":
   i = 0
   city = s
   while i < len(city) and city[i] != "," and city[0:4] != "City":
      i = i + 1
   if i < len(city):
      location = city[i - 4:i]
   if location == "City":
      print(city[0:i])
   s = input()
