import sys

def palindrome(word):
    final = "".join([l.lower() for l in word if l.isalnum()])
    return final == final[::-1]
    
def main():
    for word in sys.stdin:
        print(palindrome(word.strip()))
if __name__ == "__main__":
    main()