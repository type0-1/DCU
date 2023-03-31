def count(word):
	if word == "":
		return 0
	return 1 + count(word[1:])

def main():
    len = None
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()