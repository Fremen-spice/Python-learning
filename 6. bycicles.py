
# Lists 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("\n")

#this prints elements through index

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

# access last element in a list:
print(bicycles[-1].title())
print(bicycles[-2].title())
 
message = f"\nmy first bike was a: \n{bicycles[0].title()}"
print(message)

# Exercise - friends, page 95 in the book
frnd = ['adasha', 'drugiq adash', 'da i ba', 'vankoto', 'RsN']
message = f"srebro ili olovo, {frnd[0]}"
print(message)
message = f"ili i dvete, {frnd[1]}"
print(message)