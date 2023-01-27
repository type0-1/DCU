#!/usr/bin/env python3

i = 0

total = 0

while i < 10:

   n = int(input())

   if n > 0:

      n = n % 10

      total = total + n

   elif 0 > n:

      n = n % -10 * -1

      total = total + n

   i = i + 1

print(total)
