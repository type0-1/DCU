#!/usr/bin/env python3

import sys

ends = ["ch", "sh", "x", "s", "z"]
vowels = "aeiou"

for words in sys.stdin:
   w = words.strip().lower()
   if w[-2:] in ends or w[-1] in ends or w[-1] == "o":
      print(w + "es")
   elif (w[-2] not in vowels) and w[-1] == "y":
      print(w[0:len(words) - 2] + "ies")
   elif w[-1] == "f":
      print(w[0:len(words) - 2] + "ves")
   elif w[-2:] == "fe":
      print(w[0:len(words) - 3] + "ves")
   else:
      print(w + "s")
