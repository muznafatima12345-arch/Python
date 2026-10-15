
numbers = [10,20,30,40,50,60,70,80,90,100]

for number in numbers:
    print("Number is: ", number)

for i in range(1,10):
    print("Number : ", i)


print("Even numbers in the list.")
for i in range(1,11,2):
    print(i)


#while loop
i = 1
while i < 6:
    print(i)
    i += 1

#With the break statement we can stop the loop 
# even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break 
    i += 1

#With the continue statement we can stop 
# the current iteration, and continue with the next
#Continue to the next iteration if i is 3...... i is not gonna be printed i will be skipped 


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)