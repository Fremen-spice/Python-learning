# 14. toppings.py

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in requested_toppings:
	print (f"Adding {requested_toppings}.")
print("\nFinished making your pizza")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in requested_toppings:
	if requested_toppings == 'green peppers':
		print("Sorry, we are out of green peppers")
	else:
		print (f"Adding {requested_toppings}.")
print("\nFinished making your pizza")

requested_toppings = []
if requested_toppings:
	for requested_toppings in requested_toppings:
		print("adding {requested_toppings}.") # EMPTY LIST EVALUATES FALSE, IF THERE ARE VALUES IT RETURNS TRUE
	print("\nFinished making your pizza")
else:
	print("are you sure you want a plain pizza?")


available_toppings = ['mushrooms','olives','green peppers,','peperoni','pineapple','extra cheese']
requested_toppings = requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

print("\nnew order")
for requested_toppings in requested_toppings:
	if requested_toppings in available_toppings:
		print(f"adding {requested_toppings}")
	else:
		print(f"Sorry, we don't have {requested_toppings}.")
print('Pizza finished.')


# exercise - admins task;
usernames = ['admin','fake_admin','fake admin 2','Gosho','lazy Vanka']
admin = ['admin']
vanka = ['lazy Vanka']
for usernames in usernames:
	if usernames in admin:
		print("\n\n\n\n\n\n\n\n\nHello Admin, would you like to see a status report?")
	if usernames in vanka:
		print("------------\nВанка, сядай да пишеш код, боклук, стига си гледал глупости в нета")
	else:
		print(f"Hello {usernames}, thank you for logging in")


#Exercise 2 - END OF CHAPTER 5 IN THE BOOK


print('---\n\n\nPlease check username verification:')
current_users = ['bokluk','turtei','dancho','manaf','Nqma_hora']
current_users_case = [current_users.lower() for current_users in current_users]

new_users = ['Bokluk','Noble dib','Noble dib 2','Extra_noble_dib','dancho']
new_users_case = [new_users.lower() for new_users in new_users]
for case in new_users_case:
	if case in current_users_case or case in current_users:
		print(f'----\nSorry, {case} is taken')
	else:
		print(f'---\nSuccessful registration as {case}')






			