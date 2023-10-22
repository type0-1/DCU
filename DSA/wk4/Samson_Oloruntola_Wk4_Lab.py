"""
Program: wk4-lab.py
Date: 02/10/2023.
Author: Samson Oloruntola

Description:
Set of problems given for week 4 lab.

"""

# Question 1:

def sum_q1(n):
    if n == 0:
        return n
    else:
        return n + sum_q1(n-1)
    
# Question 2:

def reverse_number(n, reverse=0, count=0):
    if count == 0:
        return reverse + n
    else:
        count = len(str(n))
        reverse += (n%10)*(10**count)
        return reverse_number(n//10, reverse, count-1)
        
# Question 3:

def reverse_string(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string(string[:-1])

# Question 4:

def inverse_list(array):
    if not len(array):
        return array
    else:
        return [array[-1]] + inverse_list(array[:-1])

# Question 5:

def multiply(n, m):
    if n-1 == 0:
        return m
    else:
        if n < 0:
            return -m + multiply(n-1, m)
        else:
            return m + multiply(n-1 , m)

# Question 6:
    
def is_heteromecic(n, m=0):
    if m*(m+1) >= n:
        return m*(m+1) == n
    return is_heteromecic(n, m+1)
        
# Question 7:

def length_string(string, length=0):
    if not len(string):
        return length
    return length_string(string[:-1], length+1)

def main():
    
    # Question 1:

    n = 6
    sum_q1(n)

    # Question 2:

    n = 987654321

    reverse_number(n)

    # Question 3:

    string = "Hello, World!"
    reverse_string(string)

    # Question 4:

    array = [1,2,3,4,5,6,7,8,9,10]
    inverse_list(array)

    # Question 5:

    n = 35
    m = 2
    
    multiply(n, m)

    # Question 6:
    
    n = 110
    is_heteromecic(n)

    # Question 7:

    string = "Hello, World!"
    length_string(string)

if __name__ == "__main__":
    main() 