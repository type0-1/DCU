#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   s = int(s)
   a.append(s)
   s = input()

i = 0

n = int(input())
while i < len(a):
   print(a[i] + n)
   i = i + 1
