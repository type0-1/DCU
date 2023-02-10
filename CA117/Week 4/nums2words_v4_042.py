#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
zerotoNine = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
tentoTwenty = {11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}
thirtytoHundred = {30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

for line in lines:
	line = line.strip().split()
	s = ""
	for n in line:
		if len(n) == 1 and int(n) in zerotoNine:
			s += zerotoNine[int(n)] + " "
		elif int(n) in tentoTwenty:
			s += tentoTwenty[int(n)] + " "
		elif int(n) in thirtytoHundred:
			s += thirtytoHundred[int(n)] + " "
		elif len(n) == 2 and n[0] == "2":
			s += "twenty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "3" and n[1] != "0":
			s += "thirty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "4":
			s += "forty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "5" and n[1] != "0":
			s += "fifty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "6":
			s += "sixty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "7":
			s += "seventy-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "8":
			s += "eighty-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 2 and n[0] == "9":
			s += "ninety-" + zerotoNine[int(n[1])] + " "
		elif len(n) == 3:
			s += "one hundred" + " " 
	print(s.strip())
