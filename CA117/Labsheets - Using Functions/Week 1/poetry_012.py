import sys

lines = sys.stdin.readlines()

def getMax1(word, maximum=0):
    maximum = max([len(word.strip()) for word in lines])
    return maximum

def output(word):
    maximum = getMax1(word)
    return f'{word:^{maximum}}'
    
for line in lines:
    print(output(line.strip()))
