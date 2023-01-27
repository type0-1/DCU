#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   content = s.split(" ")
   list.append(content)
   s = input()

i = 0
n = int(input())

while i < len(list):
   pos = list[i]
   if n == int(pos[0]):
      print(" ".join(pos))
   i += 1
