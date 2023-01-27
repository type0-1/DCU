#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   s = int(s)
   a.append(s)
   s = input()

i = 0
smallest = a[0]
p = 1

while i < len(a):
   while p < len(a):
      if smallest > a[p]:
         smallest = a[p]
      p = p + 1
   i = i + 1

print(smallest)
