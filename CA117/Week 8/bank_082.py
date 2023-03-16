class BankAccount():

	def __init__(self, balance=0):
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, withdrawal):
		if self.balance - withdrawal >= 0:
			self.balance -= withdrawal

	def __str__(self):
		return f'Your current balance is {self.balance:.2f} euro'