#!/usr/bin/env python3

modules = []
s = input()

while s != "end":
   modules.append(s)
   s = input()

i = 0

while i < len(modules):
   check = modules[i]
   print(check[7:12])
   i = i + 1
