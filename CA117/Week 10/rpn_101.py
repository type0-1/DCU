from math import sqrt

twoOperations = ["+", "-", "*", "/"]
oneOperation = ["r", "n"]

def calculator(line):
    line = [float(dex) if dex[0].isnumeric() else dex for dex in line.strip().split()]
    nums = []
    for char in line:
	    if isinstance(char, float):
		    nums.append(char)
	    elif char in twoOperations:
	        num2 = nums.pop()
	        num1 = nums.pop()
	        if char == "+":
	            num1 += num2
	            nums.append(num1)
	        elif char == "-":
	            num1 -= num2
	            nums.append(num1)
	        elif char == "*":
	            num1 *= num2
	            nums.append(num1)
	        elif char == "/":
	            num1 /= num2
	            nums.append(num1)
	    elif char in oneOperation:
	       num1 = nums.pop()
	       if char == "n":
	          num1 = -num1
	          nums.append(num1)
	       elif char == "r":
	          num1 = sqrt(num1)
	          nums.append(num1)
    return nums.pop()
