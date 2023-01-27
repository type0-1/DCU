#!/usr/bin/env python3

short = input()
medium = input()
long = input()

len_sh = len(short)
len_me = len(medium)
len_lo = len(long)

if len_sh < len_lo and len_me < len_lo:
   print(long)
elif len_sh < len_me and len_lo < len_me:
   print(medium)
elif len_me < len_sh and len_lo < len_sh:
   print(short)
