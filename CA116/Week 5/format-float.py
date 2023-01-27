#!/usr/bin/env python3

i = 0
s = input()
before = ""
after = ""

while i < len(s) and not "0" <= s[i]:
   i = i + 1

if i < len(s):
   print(s + "." + "0")
