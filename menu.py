from student import Student

def add_student(students):
    print("\nAdd Student")

    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    marks = input("Marks: ")

    student = Student(
        student_id,
        name,
        age,
        course,
        marks
    )

    students.append(student)

    print("\nStudent added successfully.")

def view_students(students):
    print("\nView Students")

    if not students:
        print("No students found.")
        return

    for student in students:
        student.display_student()

def show_menu(students):
    while True:
        print("\n==============================")
        print(" Student Management System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Sort Students")
        print("8. Save Data")
        print("9. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "9":
            print("Exiting Student Management System.")
            break

        else:
            print("Feature not added yet.")