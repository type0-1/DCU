#!/usr/bin/env python3

i = 0
space = " "
n = int(input())

while i < n:
   if i == n // 2:
      print(space * (n // 2) + "*")
   elif i < n // 2:
      mid = space * ((n - 2 - i) - len((space * i)))
      print((space * i) + "*" + mid + "*")
   elif i > n // 2:
      m = 2 * (n // 2 - i) * - 1 - 1
      print((space * (n - i - 1) + "*" + space * m + "*"))
   i = i + 1
