import sys

def emails(email, name=""):
    name = email[:email.index("@")].split(".")
    final = name[0].capitalize() + " " + name[1].capitalize()
    return "".join([l for l in final if l.isalpha() or l == " "])

def main():
    for data in sys.stdin:
        print(emails(data.strip()))

if __name__ == "__main__":
    main()