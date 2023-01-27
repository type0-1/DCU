#!/usr/bin/env python3

words = []
s = input()

while s != "end":
   words.append(s)
   s = input()

i = 0

while i < len(words):
   print(words[len(words) - i - 1])
   i += 1
