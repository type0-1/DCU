#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

seventeen = [word.strip() for word in inputs if len(word) == 18]
eighteenPlus = [word.strip() for word in inputs if len(word) >= 19]
fourA = [word.strip() for word in inputs if word.lower().count("a") == 4]
twoPlusQ = [word.strip() for word in inputs if word.lower().count("q") >= 2]
cie = [word.strip() for word in inputs if "cie" in word]
anagrams = [word.strip() for word in inputs if "".join(sorted("angle")) == "".join(sorted(word.lower().strip()))]
anagrams.remove("angle")

print(f'Words containing 17 letters: {seventeen}')
print(f'Words containing 18+ letters: {eighteenPlus}')                                                                                                               
print(f"Words with 4 a's: {fourA}")
print(f"Words with 2+ q's: {twoPlusQ}")
print(f'Words containing cie: {cie}')
print(f'Anagrams of angle: {anagrams}')
