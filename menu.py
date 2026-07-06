from student import Student
from file_handler import save_students

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

def search_student(students):
    print("\nSearch Student")

    if not students:
        print("No students found.")
        return

    print("\nSearch By")
    print("1. Student ID")
    print("2. Student Name")

    choice = input("\nChoose an option: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")

        for student in students:
            if student.student_id == student_id:
                print("\nStudent Found")
                student.display_student()
                return

        print("Student not found.")

    elif choice == "2":
        name = input("Enter Student Name: ").lower()

        for student in students:
            if student.name.lower() == name:
                print("\nStudent Found")
                student.display_student()
                return

        print("Student not found.")

    else:
        print("Invalid option.")

def update_student(students):
    print("\nUpdate Student")

    if not students:
        print("No students found.")
        return

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student.student_id == student_id:

            print("\nCurrent Details")
            student.display_student()

            print("\nLeave a field blank to keep the current value.")

            name = input(f"New Name ({student.name}): ")
            age = input(f"New Age ({student.age}): ")
            course = input(f"New Course ({student.course}): ")
            marks = input(f"New Marks ({student.marks}): ")

            if name:
                student.name = name

            if age:
                student.age = age

            if course:
                student.course = course

            if marks:
                student.marks = marks

            print("\nStudent updated successfully.")
            return

    print("Student not found.")

def delete_student(students):
    print("\nDelete Student")

    if not students:
        print("No students found.")
        return

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("\nStudent deleted successfully.")
            return

    print("Student not found.")

def student_statistics(students):
    print("\nStudent Statistics")

    if not students:
        print("No students found.")
        return

    total_students = len(students)

    marks = [float(student.marks) for student in students]

    average_marks = sum(marks) / total_students

    highest_student = max(
        students,
        key=lambda student: float(student.marks)
    )

    lowest_student = min(
        students,
        key=lambda student: float(student.marks)
    )

    print(f"\nTotal Students : {total_students}")
    print(f"Average Marks  : {average_marks:.2f}")

    print("\nHighest Marks")
    highest_student.display_student()

    print("\nLowest Marks")
    lowest_student.display_student()

def sort_students(students):
    print("\nSort Students")

    if not students:
        print("No students found.")
        return

    print("\nSort By")
    print("1. Name (A-Z)")
    print("2. Age (Lowest to Highest)")
    print("3. Marks (Highest to Lowest)")

    choice = input("\nChoose an option: ")

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student.name.lower()
        )

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: int(student.age)
        )

    elif choice == "3":
        sorted_students = sorted(
            students,
            key=lambda student: float(student.marks),
            reverse=True
        )

    else:
        print("Invalid option.")
        return

    print("\nSorted Students")

    for student in sorted_students:
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

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            student_statistics(students)

        elif choice == "7":
            sort_students(students)

        elif choice == "8":
            save_students(students)

        elif choice == "9":
            print("Exiting Student Management System.")
            break

        else:
            print("Feature not added yet.")