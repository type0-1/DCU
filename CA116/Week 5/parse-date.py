#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and s[i] != " ":
   i = i + 1

if i < len(s):
   weekday = "(" + s[0:i] + ")"
   j = i + 1

   while j < len(s) and s[j] != " ":
      j = j + 1

   if j < len(s):
      day = s[i + 1:j] + ","
      p = j + 1

      while p < len(s) and s[p] != ",":
         p = p + 1

      if p < len(s):
         month = s[j + 1:p]
         k = p + 1
         while k < len(s) and ("0" <= s[k] and s[k] <= "9"):
            k = k + 1
         if k < len(s):
            year = s[k + 1:len(s)]
            print(month, day, year, weekday)
