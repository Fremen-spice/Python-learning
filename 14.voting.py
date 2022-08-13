age = 19
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote")

# More than two possible situations:

age = 12
print(f"\nAge is: {age}")
if age < 4:
    print("your admission cost is $0")
elif age <18:
    print("your admission cost is $25")
else:
    print("your admission cost is #40")


ages = [12, 18, 20, 50]
for age in ages:
    print(f"\nAge is: {age}")
    if age < 4:
        print("your admission cost is $0")
    elif age <18:
        print("your admission cost is $25")
    else:
        print("your admission cost is #40")


# more than elif one condition
ages = [12, 18, 20, 50]
for age in ages:
    print(f"\nAge is: {age}")
    if age < 4:
        price = 0
    elif age <18:
        price = 25
    elif age < 50:
        price = 40
    else:
        price = 20
    print(f"Your admission cost is ${price}\n")

print("toppings")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'peperoni' in requested_toppings:
    print("adding peperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")





