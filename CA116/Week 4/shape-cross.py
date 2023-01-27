#!/usr/bin/env python3

i = 0

n = int(input())

while i < n:

   if (n // 2) == i:
      print("*" * n)
   else:
      print((" " * (n // 2)) + "*")

   i = i + 1
