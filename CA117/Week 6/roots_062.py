import math
import sys

def quadraticRoot(a, b, c):
   try:
      root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
      root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
      roots = [root1, root2]
      roots.sort()
      return str(round(roots[0], 1)) + ", " + str(round(roots[1], 1))
   except ValueError:
      return f'None'

for nums in sys.stdin:
   a, b, c = nums.strip().split()
   print(quadraticRoot(int(a), int(b), int(c)))
