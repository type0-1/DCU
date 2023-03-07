
class BankAccount():

	def set_attributes(self, name, number, balance):
		self.name = name
		self.number = number
		self.balance = balance

	def print_attributes(self):
		print(f'Name: {self.name}')
		print(f'Account number: {self.number}')
		print(f'Balance: {self.balance:.2f}')

	def deposit(self, x):
		self.balance += x