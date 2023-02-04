message = input("Tell me something and I will repeat it back at you:")
print(message)

name = input("Please enter your name:")
print(f"hello, {name}")

prompt = "if you tell us who you are, we can personalize messages you see"
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"hello, {name}")



age = input("how old are you? ")
age = int(age)
age >=18

height = input("How tall are you in cm")
height = int(height)

if height >= 170:
	print("you are tall enough to ride")
else: 
	print("\nYou'll be able to ride when you are a little older")



# the operator '%'' -> returns the remainder of a division  
number = input("enter a number and I'll tell you if it is even or odd")
number = int(number)
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else: 
	print(f"\nThe number {number} is odd.")



	# Execrcise
number = input("enter a number and I'll tell you if it is devisible by 10 \n \tPlease insert: ")
number = int(number)
if number % 10 == 0:
	print(f"\nThe number {number} can be devided by 10")
else: 
	print(f"\nThe number {number} cannot be devided by 10")



# MY FIRST INPUT PROGRAM

prompt = "\nTell me something and I will repeat it back at you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

# USING A FLAG TO EXIT THE PROGRAM:

prompt = "\nTell me something and I will repeat it back at you: "
prompt += "\nEnter 'quit' to end the program.  "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

# USING BREAK TO EXIT A LOOP
prompt = "\nplease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' to end the program.):   "
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

# USING CONTINUE IN A LOOP ==================
current_number = 0
while current_number <10:
	current_number +=1
	if current_number % 2 == 0:
		continue
	print(current_number)
















