#!/usr/bin/env python3

i = 0
s = input()

while i < len(s) and s[i] != " ":
   i += 1

if i < len(s):
   print(i)
else:
   print("-1")
