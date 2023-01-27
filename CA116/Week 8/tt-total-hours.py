#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   content = s.split(" ")
   list.append(content)
   s = input()

i = 0
total = 0
while i < len(list):
   pos = list[i]
   total = total + int(pos[2])
   i += 1
print(total)
