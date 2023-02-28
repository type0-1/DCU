import sys 

first, second = sys.stdin.readline().strip().split()
first, second = first.lower(), second.lower()

i = len(second) - 1

while i >= 0:
    if second[i] in first and ("a" <= second[i] <= "z"):
        break
    i -= 1
    
lastLetter, index = second[i], i
i = len(first) - 1
count = 0
lastDots = (len(second) - 1) - index
grid = []

while i >= 0:
    if first[i] != lastLetter or (first[i] == lastLetter and count == 1):
        append = (("." * index) + first[i] + ("." * (lastDots)))
        grid.append(append)
    elif first[i] == lastLetter and count < 1:
        count += 1
        grid.append(second)
    i -= 1
    
i = len(grid) - 1
while i >= 0:
    print(grid[i])
    i -= 1