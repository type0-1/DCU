import sys

def middle(word):
    if len(word) % 2 != 0:
        return word[len(word) // 2]
    return "No middle character!"

def main():
    for data in sys.stdin:
        print(middle(data.strip()))

if __name__ == "__main__":
    main()