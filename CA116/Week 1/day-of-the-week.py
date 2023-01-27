#!/usr/bin/env python3

month = int(input()) - 1
day = int(input()) - 1

month = month * 30

total = month + day

print((total) % 7 + 1)
