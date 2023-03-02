import sys

first, second = sys.stdin.readline().lower().strip().split()
letters = [l for l in first if l.isalpha() and l in second]
firstLast, secondLast = first.rfind(letters[-1]), second.rfind(letters[-1])

i = 0
while i < len(first):
    if i != firstLast:
        print(("." * secondLast) + first[i] + ("." * (len(second) - 1 - secondLast)))
    else:
        print(second)
    i += 1
