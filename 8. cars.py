# use sort() - orders in alphabetical order
cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# keeps the original order, but presents it in new order

cars = ['bmw', 'audi', 'subaru', 'toyota']
print("\nThis is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nThis is the original list again:")
print(cars)

# adding reverse=true will sort them in reverse alph order

# reverse order:
cars = ['bmw', 'audi', 'subaru', 'toyota']
print(f"\n{cars}")
cars.reverse()
print(cars)

# find the lenght of a list
print(len(cars))


