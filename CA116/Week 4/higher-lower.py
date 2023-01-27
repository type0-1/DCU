#!/usr/bin/env python3

prev = int(input()) + 1
i = 0

while i < 5:
   curr = int(input())
   if curr > prev:
      print("higher")
   elif curr == prev:
      print("equal")
   else:
      print("lower")
   prev = curr

   i = i + 1
