#!/usr/bin/env python3

import sys
from datetime import datetime

lines = sys.stdin.readlines()
for input in lines:
   d, m, y = input.strip().split()
   calendarData = datetime(int(y), int(m), int(d))
   day = calendarData.strftime('%A')
   if day == "Monday":
      print("You were born on a", day, "and", day + "'s child is fair of face.")
   elif day == "Tuesday":
      print("You were born on a", day, "and", day + "'s child is full of grace.") 
   elif day == "Wednesday":
      print("You were born on a", day, "and", day + "'s child is full of woe.")
   elif day == "Thursday":
      print("You were born on a", day, "and", day + "'s child has far to go.")
   elif day == "Friday":
      print("You were born on a", day, "and", day + "'s child is loving and giving.")
   elif day == "Saturday":
      print("You were born on a", day, "and", day + "'s child works hard for a living.")
   elif day == "Sunday":
      print("You were born on a", day, "and", day + "'s child is fair and wise and good in every way.")
