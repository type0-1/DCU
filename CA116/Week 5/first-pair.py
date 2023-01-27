#!/usr/bin/env python3

i = 1
s = input()

while i < len(s) and s[i] != s[i - 1]:
   i += 1

if i < len(s):
   print(s[i - 1:i + 1])
