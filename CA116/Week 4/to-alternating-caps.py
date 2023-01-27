#!/usr/bin/env python3

s = input()
i = 0
want_lower_case = True
t = ""

while i < len(s):

   if ("A" <= s[i] and s[i] <= "Z") and want_lower_case:
      t = t + chr(ord(s[i]) - ord("A") + ord("a"))
   elif ("a" <= s[i] and s[i] <= "z") and not want_lower_case:
      t = t + chr(ord(s[i]) - ord("a") + ord("A"))
   else:
      t = t + s[i]

   if ("A" <= s[i] and s[i] <= "Z") or ("a" <= s[i] and s[i] <= "z"):
      want_lower_case = not want_lower_case

   i = i + 1

print(t)
