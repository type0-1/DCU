import sys

n = sys.argv[1:]
n = int(n[0].strip())
if n == 0:
    print(0)
else:
   i = n
   total = 1
   while i > 0:
      total *= i
      i -= 1
   s = str(total)
   total = 0
   for n in s:
      total += int(n)
   print(total)