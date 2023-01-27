#!/usr/bin/env python3

num = int(input())

first = num // 100
first = first % 10

second = num // 1000
second = second % 10

print((first * 10) + second)
