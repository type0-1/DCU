#!/usr/bin/env python3


i = 0

n = int(input())

s = " "

while i < n:

   if i == 0 or i == n - 1:
      print("*" * n)
   else:
      print("*" + (s * (n - 2)) + "*")

   i = i + 1
