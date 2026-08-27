import csv
import os

name = input("Enter student full name: ")

subjects = ["Python", "Database", "Maths", "English", "Computer"]
marks = []

for x in subjects:
    mark = float(input(f"Enter marks for {x}: "))
    marks.append(mark)

total = sum(marks)
avg = total / len(marks)
cgpa=avg/10

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B+"
elif avg >= 60:
    grade = "B"
elif avg >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if avg >= 40 else "Fail"

print(f"Student name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
print(f"Cgpa: {cgpa}")
print(f"Result: {result}")

file_name = "student_result.csv"
file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student Name",
            "Total Marks",
            "Average",
            "Grade",
            "Cgpa",
            "Result"
        ])

    writer.writerow([
        name,
        total,
        round(avg, 2),
        grade,
        cgpa,
        result
    ])

print("\nResult has been saved to student_result.csv")
