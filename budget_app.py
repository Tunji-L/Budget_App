class Budget:
	"""This app helps you to manage your Budgets
for food, clothing and entertainment"""
	def __init__(self, category):
		self.category = category
		self.amount = 0


	def __repr__(self):
		return "*****Welcome to your budget app*****"


	def Operation(self):
		print("This are the available option: ")
		print("1. Withdraw Fund")
		print("2. Deposit Fund")
		print("3. Check Balance")
		print("4. Transfer Fund to another budget\n")

		option = int(input("Select from the available option: "))
		if option == 1:
			self.WithdrawFund()

		elif option == 2:
			self.DepositFund()

		elif option == 3:
			print("Your balance is %.2f" %self.Balance())
		elif option == 4:
			Transfer(self.category, self.Balance())



	def DepositFund(self):
		d_amount = float(input("Enter amount to Deposit or press 0 to go back: "))
		if d_amount == 0.00:
			self.Operation()
		else:
			self.amount += d_amount
			print("Your new %s balance is %.2f" %(self.category,self.Balance()))


	def WithdrawFund(self):
		w_amount = int(input("Enter amount to Withdraw or press 0 to go back: "))
		if w_amount == 0:
			self.Operation()
		else:
			if self.amount >= w_amount:
				self.amount -= w_amount
				print("Take your money")
				print("Your balance is %.2f" %self.Balance())
			else:
				print("insufficient fund")
				self.WithdrawFund()


	def Balance(self):
		return self.amount



# making instances for food, cloth and entertainment
food = Budget("Food")
cloth = Budget("Clothing")
entertainment = Budget("Entertainment")


# Budget app initialization
def init():
	print(Budget("budget"), "\n")
	print(Budget.__doc__,"\n")
	print("This are the available Budget:")
	print("1. Food")
	print("2. Clothing")
	print("3. Entertainment\n")
	selection = int(input("Select budget to manage (1-3): "))
	if selection == 1:
		food.Operation()
	elif selection == 2:
		cloth.Operation()
	elif selection == 3:
		entertainment.Operation()
	else:
		print("Invalid selection")
		init()
	Repeat()


# Repeat operations
def Repeat():
	again = int(input("Do you want to perform another transaction (1) yes (2) no: "))
	if again == 1:
		init()
	elif again == 2:
		print("Thank you for using our App")
	else:
		print("Error Selection")
		Repeat()

def Transfer(category, balance):
	c_account = input("Enter account to credit: ")
	d_amount = int(input ("Enter amount to transfer: "))
	c_account = c_account.lower()
	# self.amount -= d_amount
	# return d_amount
	if category == "Food":
		if balance >= d_amount:
			if c_account == "clothing":
				cloth.amount += d_amount
				food.amount -= d_amount
				print("\nThe balance on your clothing budget is %.2f" %cloth.amount)
				print("The balance on your food budget is %.2f" %food.amount)
			elif c_account == "entertainment":
				entertainment.amount += d_amount
				food.amount -= d_amount
				print("\nThe balance on your entertainment budget is %.2f" %entertainment.amount)
				print("The balance on your food budget is %.2f" %food.amount)
			elif c_account == "food":
				print("You cannot transfer to the same category")
				Transfer()
			else:
				print("you've enter an invalid category")
				Transfer(category, balance)
		else:
			print("Insufficient fund")
			Repeat()

	elif category == "Clothing":
		if balance >= d_amount:
			if c_account == "food":
				food.amount += d_amount
				cloth.amount -= d_amount
				print("\nThe balance on your food budget is %.2f" %food.amount)
				print("The balance on your clothing budget is %.2f" %cloth.amount)
			elif c_account == "entertainment":
				entertainment.amount += d_amount
				cloth.amount -= d_amount
				print("\nThe balance on your entertainment budget is %.2f" %entertainment.amount)
				print("The balance on your clothing budget is %.2f" %cloth.amount)
			elif c_account == "clothing":
				print("You cannot transfer to the same category")
				Transfer()
			else:
				print("you've enter an invalid category")
				Transfer(category, balance)
		else:
			print("Insufficient fund")
			Repeat()

	elif category == "Entertainment":
		if balance >= d_amount:
			if c_account == "food":
				food.amount += d_amount
				entertainment.amount -= d_amount
				print("\nThe balance on your food budget is %.2f" %food.amount)
				print("The balance on your entertainment budget is %.2f" %entertainment.amount)
			elif c_account == "clothing":
				cloth.amount += d_amount
				entertainment.amount -= d_amount
				print("\nThe balance on your clothing budget is %.2f" %cloth.amount)
				print("The balance on your entertainment budget is %.2f" %entertainment.amount)

			elif c_account == "entertainment":
				print("You cannot transfer to the same category")
				Transfer()
			else:
				print("you've enter an invalid category")
				Transfer(category, balance)
		else:
			print("Insufficient Fund")
			Repeat()

# initialize app
init()
print("\n**** Balance****\n")
print("Food: %.2f" %food.amount)
print("Clothing: %.2f" %cloth.amount)
print("Entertainment: %.2f" %entertainment.amount)








