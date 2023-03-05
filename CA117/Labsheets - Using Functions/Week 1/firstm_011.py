import sys

def firstm(line, count=0):
    line = line.strip().split()
    s = ""
    for word in line:
        if word[0] == "m" and count == 0:
            word = word.replace(word[0], "M")
            count += 1
            s += word + " "
        else:
            s += word + " "
    return s.strip()

def main():
    for data in sys.stdin:
        print(firstm(data))
        
if __name__ == "__main__":
    main()