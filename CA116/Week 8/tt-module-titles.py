#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   s = s.split(" ")
   list.append(s[5:])
   s = input()

i = 0

while i < len(list):
   pos = list[i]
   string = " ".join(pos)
   print(string)
   i += 1
