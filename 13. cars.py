# IF statements:
cars = ['audi', 'bmw', 'subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# '=' sets value, '==' sets a condition to be checked
car1 = 'bmw'
print("\n")
if car1 == 'bmw':
    print(car1)
else:
    print("error")

#checking if something is not equal
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold!")

answer = 17
if answer != 42:
    print("wrong, arsh")


# also: +, <, <=, >, >= are things that can check stuff

# more than one condition:

age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 17:
    print("\nThe specified is correct")
else:
    print("false")
if age_0 == age_1 and age_1 >=17:
    print("no")
else: 
    print("nooo")


# checking if a value is not in a list:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
user_2 = 'andrew'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response")

if user_2 in banned_users:
    print(f"{user_2.title()}, you have no access")

#Boolean Expressions - either true or false:
game_active = True
can_edit = False


#Exercise:
car = 'subaru'
print("Is car == 'subaru'?")
print(car == 'subaru')

