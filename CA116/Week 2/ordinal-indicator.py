#!/usr/bin/env python3

n = int(input())

newnum = n

if newnum == 11 or newnum == 12 or newnum == 13:
   print("th")
elif newnum % 100 == 11 or newnum % 100 == 12 or newnum % 100 == 13:
   print("th")
elif newnum % 10 == 1:
   print("st")
elif newnum % 10 == 2:
   print("nd")
elif newnum % 10 == 3:
   print("rd")
else:
   print("th")
