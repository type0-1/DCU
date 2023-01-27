#!/usr/bin/env python3

s = input()
i = 0
j = 0
total = 0

while i < len(s):
   j = i
   while j < len(s) and not s[j] == "+":
      j += 1
   total = total + int(s[i:j])
   i = j + 1
print(total)
