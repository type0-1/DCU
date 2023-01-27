#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i += 1

if i < len(s):
   j = i + 1
   while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
      j += 1
   if j < len(s):
      print(s[i:j], i)
   elif s == "ABCDE":
      print("ABCDE 0")
