import csv
import os

from student import Student


def save_students(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Name",
            "Age",
            "Course",
            "Marks"
        ])

        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.age,
                student.course,
                student.marks
            ])

    print("\nStudent data saved successfully.")


def load_students():
    students = []

    if not os.path.exists("students.csv"):
        return students

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

            students.append(student)

    return students