def power(n, n2):
   if n == 0 or n2 == 0:
      return 1
   return n * power(n, n2-1)