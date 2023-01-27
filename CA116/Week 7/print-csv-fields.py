#!/usr/bin/env python3

s = input()
csv = []

while s != "end":
   csv.append(s)
   s = input()

i = 0
n = int(input())

while i < len(csv):
   j = 0
   p = csv[i]

   while j < len(p) and not p[j] == ",":
      j = j + 1
   if j < len(p) and n == 0:
      print(p[0:j])

   else:
      k = j + 1
      while k < len(p) and not p[k] == ",":
         k = k + 1

      if k < len(p) and n == 1:
         print(p[j + 1:k])

      else:
         g = k + 1
         while g < len(p) and not p[g] == ",":
            g = g + 1

         if g <= len(p) and n == 2:
            print(p[k + 1:g])
   i = i + 1
