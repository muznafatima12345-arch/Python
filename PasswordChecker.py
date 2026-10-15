password = input("Enter your password: ")

if len(password) >= 8 and password.isupper() and password.islower() and password.isdigit():
    print("Strong Password")
elif len(password) >= 6 and password.islower():
    print("Moderate Password")
elif len(password) < 6:
    print("Weak Password")
else:
    print("Moderate Password")
