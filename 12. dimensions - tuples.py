# tuples - lists that cannot be changed

#Example - length and width of a rectangle:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# this below returns an error, as the dimension cannot be changed
# dimensions[0] = 250

print(dimensions[:])
print("\n")

#tuples are defined by commas - if you have one element:
my_t = (3,)

for dimension in dimensions:
    print(dimension)

#redefining:

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


#exercise:
foods = ("rice", "gourmet fish", "stake", "seafood", "tears of anaconda")
print("\nThis is our official menu:")
for food in foods:
    print(food)

#foods[0] = "nuts"

foods = ("nuts", "gourmet fish", "stake", "seafood", "tears of anaconda")
print(F"\nOur updated menu is: {foods}")

    