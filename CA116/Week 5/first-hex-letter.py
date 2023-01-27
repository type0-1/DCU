#!/usr/bin/env python3

digits = "0123456789abcdef"

n = int(input())
s = ""

while 0 < n:
   s = digits[n % 16] + s
   n = n // 16

i = 0
while i < len(s) and not ("a" <= s[i] and s[i] <= "f"):
   i += 1

if i < len(s):
   print(s[i])
