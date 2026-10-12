# check input is even or odd
number = int(input("Enter number to check odd or even : "))

if number % 2 == 0:
    print("Number is EVEN.")
else:
    print("Number is ODD.")

#Largest of Three numbers
a = float(input("Enter first Number: "))
b = float(input("Enter second Number: "))
c = float(input("Enter third Number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest Number is: ", largest)


#login validation Demo

correct_username = "Muzna"
correct_password = "@01234"

username = str(input("Enter Username: "))
password = str(input("Enter Password: "))

if username == correct_username and password == correct_password:
    print("Login successful.")
elif username == correct_username:
    print("Incorrect Password.")
elif password == correct_password:
    print("Incorrect username.")
else:
    print("Invalid Password and Username.")




