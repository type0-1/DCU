#!/usr/bin/env python3

import sys
input = sys.argv[1]
prev = 0
curr = 1
list = []
result = 0

i = 0
while result <= int(input):
    result = curr + prev
    prev = curr
    curr = result
    if result % 2 == 0:
        list.append(result)
    i += 1

total = 0
i = 0

while i < len(list):
    if int(input) > list[i]:
        total += list[i]
    i += 1
print(total)
