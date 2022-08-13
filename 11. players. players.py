# working with lists - Slicing:

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:4])

#prints first 4
print(players[:5])

#prints last 3
print(players[-3:])

#printing with skip
print(players[0:3:2])

print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player)

#copying a list: 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"\n{my_foods}")
print(f"\n{friend_foods}")


# !!! IF YOU make a list = another list, python doesnt make a second list, it just uses the same