#!/usr/bin/env python3

year = int(input())

leap_year = year % 400 == 0
leap_year2 = year % 4 == 0
leap_year3 = year % 100 != 0

print(leap_year or leap_year2 and leap_year3)
