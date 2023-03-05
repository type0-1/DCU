import sys

def capital(word, firstUp="", secondUp=""):
    firstUp = word[0].upper()
    secondUp = word[-1].upper()
    return firstUp + word[1:-1] + secondUp

def main():
    for data in sys.stdin:
        print(capital(data.strip()))

if __name__ == "__main__":
    main()