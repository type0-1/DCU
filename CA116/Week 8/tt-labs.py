#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   content = s.split(" ")
   list.append(content)
   s = input()

i = 0
while i < len(list):
   pos = list[i]
   if int(pos[2]) > 1:
      print(" ".join(pos))
   i += 1
