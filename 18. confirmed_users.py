# USING WHILE LOOP WITH LISTS AND DICTS

# for loops are useful for looping through a list, but litsts should be modified with a while loop (why?)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print(f"verifying user: {current_user.title()}")
	confirmed_users.append(current_user)
# POP() FUNCTION REMOVES USERS FROM THE LIST, STARTING FROM THE LAST ONE
print("\n\tthe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

print(f"============================")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit','cat']
print(pets)
while 'dog' in pets:
	pets.remove('dog')
print(pets)



# CREATING A POLL

responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name?")
	response = input("which montain would you like to climb today?")
	responses[name] = response
	repeat = input("would you like another person to respond? (yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n--Poll results--")
for name, response in responses.items():
	print(f"{name} wpuld like to climb {response}.")


