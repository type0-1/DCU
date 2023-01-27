#!/usr/bin/env python3

import sys

text = sys.argv[1]

with open(text, "w") as f:
   f.write("Hello world.\n")
