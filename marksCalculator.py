subject1 = input("Enter subject name: ")
marks1 = int(input("Enter marks:"))
subject2 = input("Enter subject name:")
marks2= int(input("Enter marks:"))
subject3 = input("Enter Subject name:")
marks3 = int(input("Enter marks:"))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("STUDENT'S RESULT")
print("Total Marks:", total)
print("Grade:", grade)
