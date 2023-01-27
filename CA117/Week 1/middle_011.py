import sys

for word in sys.stdin:
   word = word.strip()
   if len(word) % 2 == 0:
      print("No middle character!")
   else:
      print(word[len(word) // 2])
