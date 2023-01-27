#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if bmi <= 18.5:
   print("underweight")
elif bmi <= 18.5 or bmi <= 25:
   print("normal")
elif bmi == 25 or bmi <= 29.9:
   print("overweight")
elif bmi == 30 or 30 < bmi:
   print("obese")
