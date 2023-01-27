#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):

   if "A" <= s[i] and s[i] <= "Z":
      t = t + s[i]
   elif ("a" <= s[i] and s[i] <= "z"):
      t = t + chr(ord(s[i]) + ord("A") - ord("a"))
   elif ("A" != s[i] or s[i] != "Z") and ("a" != s[i] or s[i] != "z"):
      t = t + s[i]

   i = i + 1
print(t)
