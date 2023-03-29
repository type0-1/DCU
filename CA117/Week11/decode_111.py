import sys

lines = sys.stdin.readlines()
vowels = "aeiou"

def codeBreaker(word, s="",i=0):
    while i < len(word):
        if word[i] in vowels:
            i += 2
            s += word[i]
        else:
            s += word[i]
        i += 1
    return s
            
    
for word in lines:
    print(codeBreaker(word.strip()))