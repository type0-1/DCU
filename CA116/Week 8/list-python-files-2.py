#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i]) - 3:] == ".py":
      with open(files[i]) as f:
         content = f.readlines()
         if len(content) > 0:
            print(files[i])
   i += 1
