#!/usr/bin/env python3

import sys
inputs = sys.stdin.readlines()
graph = [" "] * 20

i = 0
while i < len(graph):
   graph[i] = "|" + (" " * 20) + "|"
   i += 1

i = 0
while i < len(inputs):
   new = inputs[i].strip()
   newer = new.split(" ")
   x = int(newer[0])
   y = int(newer[1])
   pos = graph[y]
   graph[y] = graph[y][:x + 1] + "*" + graph[y][x + 2:]
   i += 1


i = 0
print(" " + "-" * 19 + "-")
while i < len(graph):
   print(graph[len(graph) - i - 1])
   i += 1
print(" " + "-" * 19 + "-")
