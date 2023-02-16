import sys

for line in sys.stdin:
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	word = "".join([l.lower() for l in line if l.lower().isalpha()])
	for l in word:
		if l in alphabet:
			alphabet = alphabet.replace(l, "")
	if len(alphabet) > 1:
		print(f'missing {alphabet}')
	else:
		print(f'pangram')