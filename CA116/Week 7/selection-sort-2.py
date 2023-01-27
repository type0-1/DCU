#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   s = int(s)
   a.append(s)
   s = input()

p = int(input())
i = p

while i < len(a):
   if a[i] < a[p]:
      p = i
   i = i + 1

print(p)
