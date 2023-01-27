#!/usr/bin/env python3

i = 0
s = input()
length = len(s)

while i < len(s):

    if "A" <= s[i] and s[i] <= "Z":
      s = s[i]

    i = i + 1

print(i - 1)
