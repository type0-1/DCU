import sys

def substring(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    if word1 in word2:
        return True
    return False

def main():
    for data in sys.stdin:
        first, second = data.strip().split()
        print(substring(first, second))

if __name__ == "__main__":
    main()