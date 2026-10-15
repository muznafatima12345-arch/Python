a = float(input("Enter first number: "))
operator = input("Enter operator(+,-,*,/): ")
b = float(input("Enter Second number: "))

if operator == "+":
    print("Result: ", a+b)
elif operator == "-":
    print("Result: ", a-b)
elif operator == "*":
    print("Result: ", a*b)
elif operator == "/":
    print("Result: ", a/b)
else:
    print("Invalid operator.")