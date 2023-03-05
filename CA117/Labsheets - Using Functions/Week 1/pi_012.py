import sys
from math import pi

lines = sys.stdin.readlines()

def output(num):
    num = int(num.strip())
    return f'{pi:.{num}f}'

def main():
    for num in lines:
        print(output(num))

if __name__ == "__main__":
    main()