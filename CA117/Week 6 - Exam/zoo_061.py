import sys

lines = sys.stdin.readlines()
animals = {}
for line in lines:
	line = line.strip().split()
	for animal in line:
		if animal not in animals:
			animals[animal] = 1
		else:
			animals[animal] += 1
all_animals = []
for animal in animals:
	if animals[animal] == len(lines):
		all_animals.append(animal)
all_animals.sort()
print(len(all_animals))
for animal in all_animals:
	print(animal)