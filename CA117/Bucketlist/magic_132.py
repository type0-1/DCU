import sys

input = sys.stdin.readlines()
num = int(input[0].strip())

values = ["3", "9"]
nums = []
final = []
pos = 0
count = 0

for i in range(1500):
	if i % 3 == 0:
		if str(i)[0] in values and str(i)[-1] in values and count != num + 5:
				nums.append(i)
				count += 1
for n in nums:
	if str(n)[len(str(n)) // 2] in values:
		final.append(n)
print(final[num - 1])