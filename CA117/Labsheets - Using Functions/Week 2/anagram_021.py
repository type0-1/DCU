import sys

def anagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
def main():
    for data in sys.stdin:
        first, last = data.strip().split()
        print(anagram(first, last))

if __name__ == "__main__":
    main()