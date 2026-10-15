thisdict = {
    "name" : "Muzna",
    "Roll no" : 1333,
    "year" : 2024
}
print(thisdict["name"])

car_dict = {
    "name" : "Supra",
    "brand": "Toyota",
    "year" : 1994
}
print(car_dict["year"])

#GET : value of the key 
x = thisdict.get("name")
print(x)

x = thisdict.keys()
print(x)

car_dict["year"] = 1111
print(car_dict["year"])

#To determine how many items a dictionary has, use the len() function:
print(len(thisdict))


print(thisdict.values())
print(thisdict.items())

if "year" in thisdict:
  print("Yes, 'year' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020})
print(thisdict.items())

#Add a color item to the dictionary by using the update() method:
thisdict.update({"color": "red"})
print(thisdict["color"])


#copy function

mydict = dict(thisdict)
print("Mydict", mydict)
#The pop() method removes the item with the specified key name
print(thisdict)
print(thisdict.items())
thisdict.pop("color")
print(thisdict.items())
del thisdict["name"]
print(thisdict.items())
del thisdict
"""print(thisdict)"""


'''LOOPING WITH DICTIONARIES--------------'''
for x in car_dict:
  print(x)

for x in car_dict:
  print(car_dict[x])

for x in car_dict.values():
  print(x)

for x in car_dict.keys():
  print(x)

for x in car_dict.items():
  print(x)



# if you want to add three dictionaries into a new dictionary
child1 = {
  "name" : "anna",
  "year" : 2004
}
child2 = {
  "name" : "henna",
  "year" : 2007
}
child3 = {
  "name" : "lily",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)





















'''
#Another method to make a dictionary 
dict1 = dict("name" : "Muzna", "BS" : "IT")
print(dict1)'''






#Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates
'''When we say that dictionaries are ordered, it means that the items have a defined order,
 and that order will not change.
Unordered means that the items do not have a defined order,
 you cannot refer to an item by using an index.
 
 Dictionaries cannot have two items with the same key:

'''