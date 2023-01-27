#!/usr/bin/env python3

import sys
new_line = "\n"
with open("characters.txt") as f:
   content = f.read(1)

   while content != "":
      if content == new_line:
         sys.stdout.write(content)
      else:
         sys.stdout.write(content + "\n")

      content = f.read(1)
