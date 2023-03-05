import sys

def es(word, check=["ch", "sh", "x", "s", "z", "o"]):
    words = []
    if word[-2:] in check or word[-1] in check:
        word += "es"
        words.append(word)
    return words

def consonant(word, vowels="aeiou"):
    words = es(word)
    if word[-2] not in vowels and word[-1] == "y":
        word = word[:-1] + "ies"
        words.append(word)
    return words

def fe(word):
    words = consonant(word)
    if word[-2:] == "fe":
        word = word[:-2] + "ves"
        words.append(word)
    elif word[-1] == "f":
        word = word[:-1] + "ves"
        words.append(word)
    return words
            
def otherwise(word, vowels="aeiou"):
    words = fe(word)
    if word[-2] in vowels and word[-1] == "y":
        word += "s"
        words.append(word)
    elif word[-1] != "s":
        word += "s"
        words.append(word)
    return words[0]
    
def main():
    for data in sys.stdin:
        print(otherwise(data.strip()))
        
if __name__ == "__main__":
    main()