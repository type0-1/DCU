#!/usr/bin/env python3

year = int(input())

leap = year % 4

year = year - leap

print(year)
