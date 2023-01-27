#!/usr/bin/env python3

list = []

s = input()

while s != "end":
   s = int(s)
   list.append(s)
   s = input()

s1 = input()

while s1 != "end":
   s1 = int(s1)
   list.append(s1)
   s1 = input()

i = 0
while i < len(list):
   p = i
   j = i + 1
   while j < len(list):
      if list[p] > list[j]:
         p = j
      j = j + 1
   tmp = list[i]
   list[i] = list[p]
   list[p] = tmp
   i = i + 1

i = 0
while i < len(list):
   print(list[i])
   i = i + 1
