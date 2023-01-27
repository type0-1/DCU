#!/usr/bin/env python3

import sys

word = sys.argv[1:]
list = []
s = input()

while s != "end":
   list.append(s)
   s = input()

new_word = word[0]
i = 0

while i < len(list):
   pos = list[i]
   j = 0
   while j < len(pos) and pos[j] != new_word[0]:
      j += 1
   if j < len(pos):
      p = j
      while p < len(pos) and pos[p] != new_word[len(new_word) - 1]:
         p += 1
      if p < len(pos):
         print(pos)
   i += 1
