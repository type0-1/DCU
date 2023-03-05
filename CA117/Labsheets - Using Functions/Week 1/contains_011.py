import sys

def contains(word1, word2, letterList=[]):
    word1, word2 = word1.lower(), word2.lower()
    letterList = [l for l in word1 if l in word2 and word1.count(l) == 1]
    return len(letterList) == len(word1)
  
def main():
    for data in sys.stdin:
        first, second = data.strip().split()
        print(contains(first, second))

if __name__ == "__main__":
    main()