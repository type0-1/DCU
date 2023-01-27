import sys

n = sys.argv[1:]
n = int(n[0].strip())
eFib = []
prev = 0
curr = 1
for i in range(1, n):
    tmp = curr + prev
    curr = prev
    prev = tmp
    if tmp % 2 == 0:
        eFib.append(tmp)
total = 0
for i in range(len(eFib)):
    if n > eFib[i]:
        total += eFib[i]
    else:
        break
print(total)