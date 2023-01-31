#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

qNoU = [word.strip() for word in inputs if word.strip().lower().count("q") > word.strip().lower().count("qu")]
print(f'Words with q but no u: {qNoU}')