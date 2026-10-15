'''Question 4: String Slicer & Manipulator
Write a program that takes a user's full name as input (e.g., "Muhammad Ali"). Use string slicing and indexing to
extract the first name and the last name into separate variables. Print the following:
The initials (e.g., "M. A.").
The entire name in uppercase.
The entire name reversed.'''

name = input("Enter your full name: ")
space = name.index(" ")

first_name = name[:space]
last_name = name[space + 1:]
print("Initial of First Name:", first_name[0])
print("Initial of Last Name:", last_name[0])
print("Uppercase:", name.upper())
print("Reversed:", name[::-1])