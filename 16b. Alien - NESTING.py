# STORE INFORMATION ABOUT MULTIPLE DICT

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 30}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
print("==================================")

# FILL AN EMPTY LIST

aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 30

for alien in aliens[:5]:
	print(alien)
print("...")
print(f"total number of aliens: {len(aliens)}")

print("==================================")



# USING A DICT, WHICH CONTAINS LISTS

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

print(f"you ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)



favorite_languages = {
	'jen': ['python', 'ruby'],
	'dib': ['c++', 'java'], 
	'edward': ['ruby'],
	'phil': ['python', 'java'],
	}
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is:")
	else:
		print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# USING A DICTIONARY INSIDE A DICTIONARY

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}

for username, user_info in users.items():
	print(f"\nusername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")


print (f"\n=====================")
#EXERCISE

chovek_0 = {'name': 'dancho', 'condition': 'bezraboten'}
chovek_1 = {'name': 'dib', 'condition': 'prekaleno raboten'}
chovek_2 = {'name': 'gosho st', 'condition': 'zen master'}

choveci = [chovek_0, chovek_1, chovek_2]
for chovek in choveci:
	print(f"{chovek['name'].title()} e {chovek['condition']}.")







