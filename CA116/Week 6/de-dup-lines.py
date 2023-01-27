#!/usr/bin/env python3

seen = []
new = []
s = input()

while s != "end":
   seen.append(s)
   s = input()

i = 0
while i < len(seen):
   j = i + 1
   while j < len(seen):
      if seen[j] == seen[i]:
         seen.pop(j)
      j += 1
   i += 1

i = 0
while i < len(seen):
   j = i + 1
   while j < len(seen):
      if seen[i] == seen[j]:
         seen.pop(j)
      j += 1
   i += 1

i = 0
while i < len(seen):
   print(seen[i])
   i += 1
