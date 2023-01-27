import sys

n = sys.argv[1:]
n = int(n[0].strip())
dNums = []
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        dNums.append(i)
print(sum(dNums))