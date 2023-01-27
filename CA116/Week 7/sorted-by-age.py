#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   list.append(s[6:8] + s[3:5] + s[0:2] + s[8:])
   s = input()

i = 0
while i < len(list):
   j = i
   while j < len(list):
      if list[i] > list[j]:
         tmp = list[i]
         list[i] = list[j]
         list[j] = tmp
      j += 1
   i += 1

i = 0
while i < len(list):
   print(list[i][7:])
   i += 1
