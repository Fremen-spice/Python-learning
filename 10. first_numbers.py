#for value in range(1,6):
#	print(value)
print("\n")

#for value in range(6):
#	print(value)
#print("\n")
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

experiment = list(range(2, 47, 3))
print(experiment)
print("\n")

# adding squares of numbers in a list
square_num = []
for value in range(1,11):
	square = value ** 2
	square_num.append(square)
print(square_num)

# same, but shorter code
square_num = []
for value in range(1,11):
	square_num.append(value**2)
print(square_num)


# Some useful functions
digits = [1,2,3,4,5,6,7,8,9,0]
dig1 = min(digits)
print(dig1)
dig2 = max(digits)
print(dig2)
sum1 = sum(digits)
print(sum1)

# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)





#exercises
print("\n")
threes = list(range(3,31,3))
for num_3 in threes:
	print(num_3)

cube_num = []
for value in range(1,11):
	three = value**3
	cube_num.append(three)
print(cube_num)

cubes = [value**3 for value in range(1,11)]
print(cubes)

