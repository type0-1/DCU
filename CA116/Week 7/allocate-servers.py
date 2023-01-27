#!/usr/bin/env python3

list = []
s = input()
jobs = 0
while s != "end":
   s = int(s)
   list.append(s)
   if list[0] + 1000 > list[len(list) - 1]:
      jobs = jobs + 1
   else:
      list.pop(0)
   s = input()
print(len(list))
