import random

def RollDice(rolls):
	for i in range(0, rolls):
		number = random.randint(1,6)
		print(number)
	Menu()

def Menu():
	print("------------------------------------")
	print("1. Press '1' to roll a die: ")
	print("2. Press '2' to roll multiple dice: ")
	print("3. press '3' to quit: ")
	print("------------------------------------")
	print()
	choice = int(input("Enter a number here: "))

	if choice == 1:
		RollDice(1)
	if choice == 2:
		rolls = int(input("How many rolls? "))
		RollDice(rolls)
	if choice == 3:
		exit()

Menu()