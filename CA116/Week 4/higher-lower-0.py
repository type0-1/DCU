#!/usr/bin/env python3

prev = int(input())

while prev != 0:
   curr = int(input())
   if curr > prev:
      print("higher")
   elif curr == prev:
      print("equal")
   elif curr < prev and curr > 0:
      print("lower")
   prev = curr
