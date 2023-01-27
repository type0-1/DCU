#!/usr/bin/env python3

import sys
import string
result = string.punctuation
lines = sys.stdin.read()
lines = lines.strip().split()
list = []

for word in lines:
   if word[-1] in result:
      if word[0:len(word) - 1].lower() not in list:
         list.append(word[0:len(word) - 1].lower())
   elif word.isdigit():
      list.append(word)
   elif word.lower() not in list:
      list.append(word.lower())
i = 0
while i < len(list):
   if list[i] in result:
      list.pop(i)
   i += 1
print(len(list))
