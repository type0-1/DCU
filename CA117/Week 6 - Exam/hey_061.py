import sys

for word in sys.stdin:
	word = word.strip()
	eWord = ""
	for c in word:
		if c == "e":
			eWord += c
	eWord = eWord * 2
	print("h" + eWord + "y")
