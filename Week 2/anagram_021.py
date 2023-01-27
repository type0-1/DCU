#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
for words in lines:
   word1, word2 = words.strip().split()
   if len(word1) == len(word2):
      for c in word2:
         if c in word1:
            word1 = word1.replace(c, "", 1)
   if len(word1) == 0:
      print(True)
   else:
      print(False)
