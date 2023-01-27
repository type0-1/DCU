#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   list.append(s)
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
   print(list[i])
   i += 1
