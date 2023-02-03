#!/usr/bin/env python3

import sys

l = sys.stdin.read().split()

def allVowels(s):
   return "a" in s and "e" in s and "i" in s and "o" in s and "u" in s 

short = [word.strip() for word in l if allVowels(word)]
iary = [word.strip() for word in l if "iary" in word]
eLetters = [word.lower().count("e") for word in l if word.strip().lower().count("e") > 0]

c = max(eLetters)
mostE = [word.strip() for word in l if word.strip().lower().count("e") >= c]

print(f'Shortest word containing all vowels: {min(short, key=len)}')
print(f'Words ending in iary: {len(iary)}')
print(f"Words with most e's: {mostE}")
