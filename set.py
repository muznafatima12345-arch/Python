fruits = {"apple", "mango", "banana"}
print(fruits)

#Adding value
fruits.add("orange")
print(fruits)

#Removing value
fruits.remove("apple")
print(fruits)

#Removing value by discort
fruits.discard("grapes")
print(fruits)

#Adding values
fruits.update(["kiwi", "grapes"])
print(fruits)

#Removing all values
fruits.clear()
print(fruits)

#duplicate values
numbers = {1, 2, 2, 3, 3}
print(numbers)

#length
print(len(numbers))

# Loop 
for x in numbers:
    print(x)
