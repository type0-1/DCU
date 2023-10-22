"""
Program: wk1-lab.py
Date: 15/09/2023.
Author: Samson Oloruntola

Description:
Set of problems given for week 1 lab.
"""

# Question 1:

def q1_sum(matrix):
	even = 0
	for array in matrix:
		for num in array:
			if not num % 2:
				even += num
	return even

# Question 2:

def move_vow(string):
	result = ""
	vowels = "aeiouAEIOU"

	for chr in string:
		if chr in vowels:
			result += chr
			string = string.replace(chr, "")
	
	return result + string

# Question 3:

class Memories(object):
    
    def __init__(self, key, **attributes):
        for key in attributes:
            setattr(self, key, attributes[key])
    
    def remember(self, string):
        if hasattr(self, string):
            return getattr(self, string)
        return False
		
# Question 4:

class Test(object):

	def __init__(self, subject_name, correct_answers, passing_mark):
		self.subject_name = subject_name
		self.correct_answers = correct_answers
		self.passing_mark = passing_mark


class Student(object):

	def __init__(self, name):
		self.name = name

	def take_test(self, other, answer):
		right_answers = 0
		question_amount = len(other.correct_answers)

		for i, paper_answer in enumerate(other.correct_answers):
			if(answer[i] == paper_answer):
				right_answers += 1

		result = (right_answers/question_amount) * 100
		minimum = int(other.passing_mark[0:-1])

		if result > minimum:
			return f'{self.name} passed the {other.subject_name} test with the score {result}%'
		else:
			return f'{self.name} has failed the {other.subject_name} test!'

		
# Question 5:

def histogram(num_list, character):
	for n in num_list:
		print(character * n)

# Question 6:

def filter_star(dictionary, number):

	result = {}
	
	for key, value in dictionary.items():
		if len(value) == number:
			result[key] = value

	if not len(result):
		return f'No result found!'
	
	return f'{result}'
