bill = int(input("Enter Total Bill: "))
tip_percentage = int(input("Enter Tip% : "))
no_of_people = int(input("Enter Number of People splitting the bill : "))

#Total Tip
tip = bill * tip_percentage / 100
print("Total tip: ", tip)

#Total bill Including TIP
bill = bill + tip
print("Total Bill payment: ", bill)
#Amount of bill each person has to pay 
amount_for_each = bill /no_of_people
print("Amount for each person to pay: ",amount_for_each )

