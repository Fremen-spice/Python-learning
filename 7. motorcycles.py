# modifying lists - below: replacing first element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(f"\n{motorcycles}")

# add new element at the end
motorcycles.append('honda')
print(motorcycles)

# add new elements to empty lists
auto = []
auto.append('benz')
auto.append('ferrari')
auto.append('lambo')
auto.append('bmw')
print(f"\n{auto}")

# add new element at any desired position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(f"\n{motorcycles}")

# remove elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(f"\n{motorcycles}")
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"My last owned motorcycle was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"My first owned motorcycle was a {first_owned.title()}.")

# removing a value when not knowing a position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nThe {too_expensive.title()} is too expensive for me.")




