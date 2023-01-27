#!/usr/bin/env python3

i = 0

while i < 10:
   s = input()
   j = 0

   while j < len(s) and not s[j] == "+":
      j = j + 1

   if j < len(s):
      first = int(s[0:j])
      second = int(s[j:])
      print(first + second)

   i = i + 1
