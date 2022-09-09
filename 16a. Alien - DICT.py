#Alien - using dictionaries

alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)


alien_0['color'] = 'yellow'
print(f"\nthe alien is now {alien_0['color']}")

alien_0 = {'x_position': 0, "y_position": 25, 'speed': 'medium', "points": 2}
print(f"Original position:{alien_0['x_position']}")
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"\nNew position: {alien_0['x_position']}")

del alien_0['points']
print(f"\npoints removed:\n{alien_0}")


print(f"\n===========================\n")

favorite_languages = {
	'jen': 'python',
	'dib': 'c++', 
	'edward': 'ruby',
	'phil': 'python'
	}
print(favorite_languages)

language = favorite_languages['dib'].title()
print(f"Dib's favorite language is {language}.")

#get() command = can return 
print(f"\n===========================\n")
alien_0 = {'color': 'green', 'points':5}
point_value = alien_0.get('points', 'No point value asigned')
print(point_value)

# 
print(f"\n===========================\n -> LOOPING THROUGH DICTIONARIES")
user_0 = {
	'username': 'efermi',
	'first_name': 'Enrico',
	'last_name': 'Fermi'
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

# keys()

for name in favorite_languages.keys():
	print(name.title())

print(f"\n===========================-> LOOPING THROUGH A LIST ")
# 
friends = ['jen', 'dib']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll")

print(favorite_languages.keys()) # <- THIS PRINTS ALL KEYS IN A DICTIONARY

print(f"\n===========================\n")
# LOOPING THROUGH A DIFFERENT ORDER
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll")

print(f"\n===========================-> ") #LOOPING THROUGH ALL VALUES IN A DICT:
print("the following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

#LOOPING THROUGH ALL VALUES IN A DICT - UNIQUE VALUES ONLY:
print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())


# DIFFERENCE BETWEEN SETS AND DICT - ONE HAS KEY-VALUE, OTHER DOES NOT; THEY BOTH USE BRACES {}
# YOU CAN CREATE A SET OF DATA DIRECTLY JUST LIKE DICT; NOTE: SETS DO NOT RETURN ITEMS IN A SPECIFIC ORDER


#EXERCISE
rivers = {
	'marica': 'trakiq',
	'struma': 'makedoniq',
	'iskar': 'miziq'
}

for river, place in rivers.items():
	print(f"{river.title()} minava prez {place}")

print("\nTezi tri reki minavat prez oblastite:")
for place in rivers.values():
	print(f"{place.title()}")









