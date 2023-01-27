#!/usr/bin/env python3

n = int(input()) - 2

num1 = 0
num2 = 1
i = 0

print(i)

print(num2)


while i < n:

   num3 = num1 + num2

   num1 = num2

   num2 = num3

   if num2 < (n + 2):
      print(num2)

   i = i + 1
