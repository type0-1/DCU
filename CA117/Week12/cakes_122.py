import sys

lines = sys.stdin.readlines()

def getFree(cakes, freeCakes=None):

	cakes.sort(reverse=True)

	if freeCakes is None:
		freeCakes = []

	for i in range(2, len(cakes), 3):
		freeCakes.append(cakes[i])

	return sum(cakes) - sum(freeCakes)


def main():

	for line in lines:
		cakes = [int(n) for n in line.strip().split()]
		print(getFree(cakes))

if __name__ == "__main__":
	main()