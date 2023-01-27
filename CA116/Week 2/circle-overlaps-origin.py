#!/usr/bin/env python3

x = int(input())
y = int(input())
z = int(input())

first = (((x <= y) or (y <= x)) and (x < z) and (y < z))

print(first)
