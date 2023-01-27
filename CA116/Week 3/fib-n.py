#!/usr/bin/env python3

n = int(input())
n1 = 0
n2 = 1
n3 = 0

i = 0 + 2

print("0")
print("1")
while i < n:

   n1 = n2 + n3
   n3 = n2
   n2 = n1

   print(n2)

   i = i + 1
