
# Looping variables - below magician is newly created variable
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

for magician in magicians:
	print(f"{magician.title()}, that was a good trick!")
	print(f"Do it again, {magician.title()}!\n")

print("thank you!")


#example errors - Indentation error
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)

#example 2 
# for magician in magicians:
#	print(f"{magician.title()}, that was a good trick!")
#	print(f"Do it again, {magician.title()}!\n")
#	print (f"thank you everyone!")

#example 3: forgetting the colon
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians
#	print(magician)
