import csv


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