#!/usr/bin/env python3

list = []
s = input()

while s != "end":
   s = s.split(" ")
   list.append(s)
   s = input()

i = 0
while i < len(list):
   pos = list[i]
   if pos[0] == "3":
      string = " ".join(pos[0:len(pos)])
      print(string)
   i += 1
