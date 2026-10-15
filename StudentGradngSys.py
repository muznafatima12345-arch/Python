'''Question 7: The Student Grading System
Create a dictionary where the keys are the names of 5 students and the values are their marks out of 100 (e.g.,
{"Ali": 85, "Ayesha": 92} ). Use a for loop to iterate through the dictionary. Use if/elif/else statements
to assign and print a grade for each student based on their marks (A: 90+, B: 80-89, C: 70-79, F: <70).'''

studentsdict = {
    "Ali": 85,
    "Ayesha": 92,
    "Anum": 90,
    "Sara": 88,
    "Amna": 98
}
for name, marks in studentsdict.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"
    print("Marks:", marks)
    print("Grade:", grade)