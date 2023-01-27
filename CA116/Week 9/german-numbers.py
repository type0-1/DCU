#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

numbers = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

i = 0
while i < len(inputs):
   content = inputs[i].strip()
   if content in numbers:
      print(numbers[content])
   i += 1
