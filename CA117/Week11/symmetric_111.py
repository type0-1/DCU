import sys

lines = sys.stdin.readlines()
dic = {}

for word in lines:
    word = word.strip()
    if len(word) not in dic:
        dic[len(word)] = [word]
    else:
        dic[len(word)] += [word]

for word in sorted(dic):
    print(dic[word][0])

for word in sorted(dic, reverse=True):
    if len(dic[word]) == 2:
        print(dic[word][1])
