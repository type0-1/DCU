#!/usr/bin/env python3

home_s = int(input())
away_s = int(input())

if away_s < home_s:
   print("Home win.")
elif away_s == home_s:
   print("Draw.")
else:
   print("Away win.")
